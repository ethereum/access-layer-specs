#!/usr/bin/env python3
"""Build registry.yaml and the README spec table from spec front matter.

Front matter is the single source of truth. Everything this script writes is
derived, so nothing is maintained in two places.

    python3 scripts/build_registry.py           regenerate the derived files
    python3 scripts/build_registry.py --check    fail if they are out of date
"""

import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml is required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "specs")
REGISTRY = os.path.join(ROOT, "registry.yaml")
README = os.path.join(ROOT, "README.md")

BEGIN = "<!-- BEGIN GENERATED SPEC TABLE -->"
END = "<!-- END GENERATED SPEC TABLE -->"

ROLES = {"hosted", "mirrored", "indexed"}
TYPES = {"protocol", "interface", "profile", "schema", "process"}
STATUSES = {"draft", "review", "stable", "deprecated",
            "stagnant", "withdrawn", "living"}
DOMAINS = {"read", "write", "prove", "delegate", "exit"}
# The two reasons an indexed entry may exist, see process/front-matter.md.
INDEX_REASONS = {"dependency", "moved"}
REQUIRED = ("id", "title", "shortname", "role", "type", "status", "editor")


def load_specs():
    """Read every spec folder, returning (specs, errors)."""
    entries, errors = [], []
    if not os.path.isdir(SPECS):
        return [], ["specs/ does not exist"]

    for folder in sorted(os.listdir(SPECS)):
        path = os.path.join(SPECS, folder, "README.md")
        if not os.path.isfile(path):
            continue

        # A bare number is a legacy path kept as a pointer to the renamed
        # folder, so links made before the rename keep working. Not a spec.
        if re.fullmatch(r"\d+", folder):
            continue

        match = re.match(r"^(\d+)-([a-z0-9-]+)$", folder)
        if not match:
            errors.append(f"{folder}: folder must be named <number>-<shortname>, all lower case")
            continue

        text = open(path, encoding="utf-8").read()
        if not text.startswith("---\n"):
            errors.append(f"{folder}: file does not start with a front matter block")
            continue

        try:
            data = yaml.safe_load(text.split("---\n", 2)[1])
        except yaml.YAMLError as exc:
            errors.append(f"{folder}: front matter is not valid YAML, {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{folder}: front matter is not a mapping")
            continue

        for field in REQUIRED:
            if data.get(field) in (None, "", []):
                errors.append(f"{folder}: {field} is required")

        spec_id = data.get("id")
        if isinstance(spec_id, bool) or not isinstance(spec_id, int):
            errors.append(f"{folder}: id {spec_id!r} must be a whole number")
        elif int(match.group(1)) != spec_id:
            errors.append(f"{folder}: id {spec_id!r} does not match the folder number")
        shortname = data.get("shortname")
        if not isinstance(shortname, str) or not re.fullmatch(r"[A-Z0-9-]+", shortname):
            errors.append(f"{folder}: shortname {shortname!r} must be upper case letters, digits and hyphens")
        elif match.group(2) != shortname.lower():
            errors.append(f"{folder}: folder must end in the shortname in lowercase, {shortname.lower()}")
        if data.get("role") not in ROLES:
            errors.append(f"{folder}: role {data.get('role')!r} is not one of {sorted(ROLES)}")
        if data.get("type") not in TYPES:
            errors.append(f"{folder}: type {data.get('type')!r} is not one of {sorted(TYPES)}")
        if data.get("status") not in STATUSES:
            errors.append(f"{folder}: status {data.get('status')!r} is not one of {sorted(STATUSES)}")
        for domain in data.get("domains") or []:
            if domain not in DOMAINS:
                errors.append(f"{folder}: domain {domain!r} is not one of {sorted(DOMAINS)}")
        if data.get("role") in ("mirrored", "indexed") and not data.get("upstream"):
            errors.append(f"{folder}: role {data['role']} requires an upstream URL")

        data["folder"] = folder
        entries.append(data)

    # A spec in review sits at 0000 until a maintainer assigns its number on
    # merge, see process/intake.md. It goes through every check below like the
    # others but is kept out of registry.yaml and the README table until then.
    specs = [e for e in entries
             if isinstance(e["id"], int) and not isinstance(e["id"], bool) and e["id"] != 0]

    ids = [s["id"] for s in specs]
    for spec_id in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"id {spec_id} is used by more than one spec")

    known = set(ids)
    # While a 0000 draft is in the tree, 0 names "the draft in this same pull
    # request", so a new spec can depend on an external standard proposed next
    # to it. On merge the maintainer swaps 0 for the assigned number, and once
    # no 0000 folder is left a leftover 0 fails like any other missing spec.
    if any(e["id"] == 0 for e in entries):
        known.add(0)
    for spec in entries:
        for field in ("depends_on", "replaces"):
            for ref in spec.get(field) or []:
                if ref not in known:
                    errors.append(f"{spec['folder']}: {field} names spec {ref}, which does not exist")

        # replaced_by takes a spec number, an external identifier such as
        # ERC-9999, or a path in this repo. Only a number is checkable here.
        target = spec.get("replaced_by")
        if isinstance(target, bool):
            errors.append(f"{spec['folder']}: replaced_by must be a spec number, an external id, or a path")
        elif isinstance(target, int) and target not in known:
            errors.append(f"{spec['folder']}: replaced_by names spec {target}, which does not exist")
        elif isinstance(target, str) and target.strip().isdigit() and int(target) not in known:
            errors.append(f"{spec['folder']}: replaced_by names spec {target}, which does not exist")

    # Every indexed entry names why it exists in index_reason, and each value
    # has one condition that is checked here. Without such a rule the repo
    # becomes a catalogue of every spec in the world.
    depended_on = {ref for s in entries if s.get("role") == "hosted"
                   for ref in s.get("depends_on") or []}
    for spec in entries:
        if spec.get("role") != "indexed":
            continue
        reason = spec.get("index_reason")
        if reason not in INDEX_REASONS:
            errors.append(
                f"{spec['folder']}: an indexed entry needs index_reason set to one of "
                f"{sorted(INDEX_REASONS)}, see process/front-matter.md")
            continue
        if reason == "dependency" and spec["id"] not in depended_on:
            errors.append(
                f"{spec['folder']}: index_reason dependency, but no hosted spec lists "
                f"{spec['id']} in depends_on")
        if reason == "moved" and not spec.get("upstream"):
            errors.append(
                f"{spec['folder']}: index_reason moved requires upstream to be set")

    return sorted(specs, key=lambda s: s["id"]), errors


def render_registry(specs):
    entries = []
    for spec in specs:
        entry = {
            "id": spec["id"],
            "title": spec["title"],
            "path": f"specs/{spec['folder']}/README.md",
            "role": spec["role"],
            "type": spec["type"],
            "status": spec["status"],
        }
        for field in ("shortname", "domains", "tags", "editor",
                      "depends_on", "replaces", "replaced_by", "upstream",
                      "index_reason"):
            if spec.get(field):
                entry[field] = spec[field]
        entries.append(entry)
    header = ("# Generated by scripts/build_registry.py. Do not edit.\n"
              "# Front matter in each spec's README.md is the source of truth.\n")
    return header + yaml.safe_dump({"specs": entries}, sort_keys=False,
                                   allow_unicode=True, width=100)


def render_table(specs):
    rows = ["| # | Name | Type | Status | Domains | Description |",
            "|---|------|------|--------|---------|-------------|"]
    for spec in specs:
        name = f"{spec['id']}/{spec['shortname']}"
        link = f"[{name}](specs/{spec['folder']}/README.md)"
        domains = ", ".join(spec.get("domains") or []) or "—"
        note = spec.get("description") or spec["title"]
        rows.append(f"| {spec['id']} | {link} | {spec['type']} | {spec['status']} | {domains} | {note} |")
    return "\n".join(rows)


def splice(readme_text, table):
    if BEGIN not in readme_text or END not in readme_text:
        sys.exit(f"README.md is missing the {BEGIN} / {END} markers")
    before = readme_text.split(BEGIN)[0]
    after = readme_text.split(END)[1]
    return f"{before}{BEGIN}\n{table}\n{END}{after}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="exit non-zero if the generated files are out of date")
    args = parser.parse_args()

    specs, errors = load_specs()
    if errors:
        print("Front matter problems:\n", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    registry = render_registry(specs)
    readme = splice(open(README, encoding="utf-8").read(), render_table(specs))

    if args.check:
        stale = []
        if not os.path.exists(REGISTRY) or open(REGISTRY, encoding="utf-8").read() != registry:
            stale.append("registry.yaml")
        if open(README, encoding="utf-8").read() != readme:
            stale.append("README.md")
        if stale:
            print(f"Out of date: {', '.join(stale)}", file=sys.stderr)
            print("Run: python3 scripts/build_registry.py", file=sys.stderr)
            return 1
        print(f"{len(specs)} specs, generated files up to date")
        return 0

    open(REGISTRY, "w", encoding="utf-8").write(registry)
    open(README, "w", encoding="utf-8").write(readme)
    print(f"Wrote registry.yaml and the README table for {len(specs)} specs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
