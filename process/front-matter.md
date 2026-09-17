# Front matter

Each spec is a `README.md` inside its own folder under `specs/`, named number plus the spec's shortname in lowercase, for example `specs/6-private-read/`. The file begins with a YAML block. That block is the single source of truth for the spec's metadata. The index table in the README and `registry.yaml` are generated from it, so nothing is maintained twice.

```yaml
---
id: 6
title: Private Read Protocol
description: Private reads from Ethereum without revealing what was read
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
| `description` | no | One line for the index table. Falls back to `title` when absent |
| `shortname` | yes | Upper-case short name, used for citations and the folder name. See below |
| `role` | yes | `hosted`, `mirrored` or `indexed` |
| `type` | yes | `protocol`, `interface`, `profile`, `schema` or `process` |
| `status` | yes | See [lifecycle.md](lifecycle.md) |
| `domains` | no | Any of `read`, `write`, `prove`, `delegate`, `exit` |
| `tags` | no | Free-form keywords for search, lower case with hyphens instead of spaces. Carries no process meaning |
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
- `indexed`, the spec is read upstream. Usually a short stub with a link and a sentence of context. A spec that was hosted here and moved out keeps its full text if any spec here depends on it or it had reached `stable`, so that old links still resolve. Otherwise it becomes a stub. A stub carries no `contributors`, because the text is not here, and its `editor` is whoever keeps the link and the context line correct rather than whoever wrote the upstream spec.

An indexed entry has to earn its place, or the repository slowly becomes a catalogue of every interesting spec in the world. There are exactly two reasons, every indexed entry names its reason in `index_reason`, and CI checks the matching condition.

| How it qualifies | When it applies | Checked |
|---|---|---|
| `index_reason: dependency` | the usual case for an external standard | a hosted spec lists it in `depends_on` |
| `index_reason: moved` | its text was hosted here and now lives in another standards body or repository | `upstream` must be set |

The field takes only these two values, on purpose. A sentence of your own is not a reason, and "this looks useful" never gets a spec in.

A spec that is only worth mentioning gets a plain link in the text of the spec that mentions it, not an entry of its own. A dependency is something a spec cannot be used without. A comparison or a rejected alternative in the rationale section is a mention.

## type

What kind of document it is.

- `protocol`, the complete behavior of one system.
- `interface`, an API or message format, a call and its answer. Proven by two implementations talking to each other.
- `profile`, how existing standards are combined for one use case.
- `schema`, an exact data shape written by one side and read by the other. Proven by fixtures a validator can pass or fail.
- `process`, this repository's own working rules.

New values get added when the first spec of a new kind arrives, not in advance. Conformance fixtures are not a type. They live in each spec's `fixtures/` folder.

## domains

Optional tags naming which Access Layer verbs a spec serves. A spec usually serves more than one, and that is expected rather than a problem to resolve. Semaphore, for example, is `[read, write, prove]`, because it covers adding an identity to a group, reading a leaf position, and proving membership.

The tags exist to group specs and to help find the right reviewer. They do not affect where a spec is filed, because every spec lives in the same flat numbered list.

## shortname

A short upper-case name for the spec, with no spaces, for example `SEMAPHORE-V4`. It is used in two places. Other specs cite this one as number slash shortname, `3/SEMAPHORE-V4`, which specs 2, 3 and 4 already do for `1/COSS`. And the folder name is the number plus the shortname in lowercase, `specs/3-semaphore-v4/`. CI checks that the folder matches.

## replaced_by

What took this spec's place once it is deprecated. Three kinds of thing can.

| What replaced it | Example | Checked by CI |
|---|---|---|
| A newer spec here | `4` | yes, a spec with that number must exist in `specs/` |
| A standard somewhere else, when a spec here is dropped because it covers the same ground | `ERC-9999` | no, a maintainer confirms it |
| A folder in this repository | `process/` | no, a maintainer confirms it opens |

The last form exists for one case, 1/COSS is retired by the process documents.

Replaced is not the same as moved. A replaced spec is no longer maintained, its `status` becomes `deprecated`, its `role` stays `hosted` and its text stays as a record, and `replaced_by` points at whatever made it pointless. A moved spec is still maintained, only somewhere else, so its `role` becomes `indexed` with `index_reason: moved` and `upstream` points at the new home, while `status` stays what it was.

`replaces` is the matching field on the newer spec. It lists the number of the older spec here that it takes over from, so the two specs point at each other. It only ever holds spec numbers from this repository.

## Versioning

There are two kinds of change to a spec, and they are handled differently.

A change that only makes the text clearer, a fixed typo, a better example, a tighter definition, is edited into the existing spec. Nothing else happens.

A change that alters what implementers have to do gets a new spec with a new number. Semaphore v3 to v4 is the kind of change meant here. v4 swapped the Merkle tree for the Lean IMT and moved identities from Poseidon to EdDSA, so code written for v3 no longer works with v4. Had v3 been a spec here, it would get `status: deprecated` and `replaced_by` pointing at the v4 number, and the v4 spec would carry `replaces` with the v3 number. The v3 text stays where it is, so anyone who built against it can still read exactly what they built against.
