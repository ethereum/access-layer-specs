# Front matter

Each spec is a `README.md` inside its own numbered folder, and begins with a YAML block. That block is the single source of truth for the spec's metadata. The index tables and `registry.yaml` are generated from it, so nothing is maintained twice.

```yaml
---
id: 6
title: Private Read Protocol
role: hosted
type: protocol
status: draft
domains: [read]
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
| `role` | yes | `hosted`, `mirrored` or `indexed` |
| `type` | yes | `protocol`, `interface`, `profile`, `schema` or `process` |
| `status` | yes | See [lifecycle.md](lifecycle.md) |
| `domains` | no | Any of `read`, `write`, `prove`, `delegate`, `exit` |
| `editor` | yes | The person accountable for the text |
| `contributors` | no | Everyone else who wrote part of it |
| `depends_on` | no | Spec ids this one cannot be understood or used without |
| `replaces` | no | Spec ids this one supersedes |
| `replaced_by` | no | The spec id or external standard that supersedes this one |
| `upstream` | when `role` is `mirrored` or `indexed` | URL of the canonical text |

## role

Where the canonical text lives, and what this repository promises about it.

- `hosted`, the text lives here and this repository is its source of truth.
- `mirrored`, a full copy is kept here while an upstream stays authoritative. Used for fragile upstreams such as shared notes and papers, and for frozen audit snapshots.
- `indexed`, only a stub with a link. The spec is read upstream.

An external standard gets an indexed entry only when a hosted spec names it in `depends_on`. Anything merely worth mentioning stays an ordinary hyperlink in a spec's prose. Without that rule the repository slowly becomes a catalogue of every interesting spec in the world.

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

## Versioning

A clarifying edit changes the spec in place.

A behavior change is a new numbered spec. Semaphore v4 to v5 is the example to have in mind. The old spec flips to `status: deprecated` and gets `replaced_by` pointing at the new number, and the new spec carries `replaces`. Permalinks to the old text keep working, and anyone who built against v4 can still read exactly what they built against.
