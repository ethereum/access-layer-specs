# Front matter

Each spec is a `README.md` inside its own folder under `specs/`, named number plus slug, for example `specs/6-private-read/`. The file begins with a YAML block. That block is the single source of truth for the spec's metadata. The index table in the README and `registry.yaml` are generated from it, so nothing is maintained twice. Until the generator lands, the README table is edited by hand to match.

```yaml
---
id: 6
title: Private Read Protocol
shortname: PRIVATE-READ
role: hosted
type: protocol
status: draft
domains: [read]
tags: [privacy, rpc]
editor: Name <email>
contributors:
  - Name <email>
depends_on: []
replaces: []
replaced_by: null
upstream: null
---
```

## Fields

| Field | Required | Value |
|---|---|---|
| `id` | yes | The spec's number. Assigned on merge, never reused, never changed |
| `title` | yes | Plain name, no number in it |
| `shortname` | no | Upper-case short handle, used in the `N/SHORTNAME` form other specs cite |
| `role` | yes | `hosted`, `mirrored` or `indexed` |
| `type` | yes | `protocol`, `interface`, `profile`, `schema` or `process` |
| `status` | yes | See [lifecycle.md](lifecycle.md) |
| `domains` | no | Any of `read`, `write`, `prove`, `delegate`, `exit` |
| `tags` | no | Free-form keywords for search. Carries no process meaning |
| `editor` | yes | The person accountable for this entry. For an indexed stub that means the link and the context line, not the upstream text |
| `contributors` | no | Everyone else who wrote part of it |
| `depends_on` | no | Spec ids this one cannot be understood or used without |
| `replaces` | no | Spec ids this one supersedes |
| `replaced_by` | no | What supersedes this spec. See below for the accepted forms |
| `index_reason` | when `role` is `indexed` | `dependency` or `moved`, why this entry exists |
| `upstream` | when `role` is `mirrored` or `indexed` | URL of the canonical text |

## role

Where the canonical text lives, and what this repository promises about it.

- `hosted`, the text lives here and this repository is its source of truth.
- `mirrored`, a full copy is kept here while an upstream stays authoritative. Used for fragile upstreams such as shared notes and papers, and for frozen audit snapshots.
- `indexed`, the spec is read upstream. Usually a short stub with a link and a sentence of context. A spec that was hosted here and moved out keeps its full text if any spec here depends on it or it had reached `stable`, so that old links still resolve. Otherwise it becomes a stub.

An indexed entry has to earn its place, or the repository slowly becomes a catalogue of every interesting spec in the world. There are exactly two reasons, every indexed entry names its reason in `index_reason`, and CI checks the matching condition.

| How it qualifies | When it applies | Checked |
|---|---|---|
| `index_reason: dependency` | the usual case for an external standard | a hosted spec lists it in `depends_on` |
| `index_reason: moved` | its text was hosted here and now lives in another standards body or repository | `upstream` must be set |

No other value is accepted, and there is deliberately no free-text route in. "This looks useful" is not a reason. Any further context goes in the stub's one sentence.

Anything merely worth mentioning stays an ordinary hyperlink in a spec's prose.

## type

What kind of document it is.

- `protocol`, the complete behavior of one system.
- `interface`, an API or message format.
- `profile`, how existing standards are combined for one use case.
- `schema`, an exact data shape that a validator can check against.
- `process`, this repository's own working rules.

New values get added when the first spec of a new kind arrives, not in advance. Conformance fixtures are not a type. They live in each spec's `fixtures/` folder.

## domains

Optional tags naming which Access Layer verbs a spec serves. A spec usually serves more than one, and that is expected rather than a problem to resolve. Semaphore, for example, is `[read, write, prove]`, because it covers adding an identity to a group, reading a leaf position, and proving membership.

The tags exist to group specs and to help find the right reviewer. They do not affect where a spec is filed, because every spec lives in the same flat numbered list.

## shortname

Specs in this repository have long been cited in the form `1/COSS` and `3/SEMAPHORE-V4`, and specs 2, 3 and 4 each cite `1/COSS` that way in their change-process section. `shortname` keeps that handle available and makes the folder slug derivable from it. It is optional, and a spec without one is cited by number and title.

## replaced_by

Three forms are accepted, and the validator treats each differently.

| Form | Example | Checked |
|---|---|---|
| A spec number | `4` | yes, the spec must exist here |
| An external identifier | `ERC-9999` | no, it is outside this repository |
| A path in this repository | `process/` | no, the reviewer confirms it opens |

`replaces` points the other way and only takes spec numbers.

## Versioning

A clarifying edit changes the spec in place.

A behavior change is a new numbered spec. Semaphore v3 to v4 is the example to have in mind, v4 replaced the Merkle tree and changed the identity scheme, so code written against v3 stopped working. The old spec flips to `status: deprecated` and gets `replaced_by` pointing at the new number, and the new spec carries `replaces`. Permalinks to the old text keep working, and anyone who built against v3 can still read exactly what they built against.
