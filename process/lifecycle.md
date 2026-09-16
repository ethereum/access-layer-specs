# Lifecycle

Every spec carries a `status`. Four main stages run in order, and three side statuses sit outside that order.

A spec is merged into `main` early, as soon as it is readable and in scope. That merge gives it its number and puts it at `draft`. Everything after that, `review`, `stable`, `deprecated`, is a change to the `status` line of an already merged spec, made in a later pull request. So `draft` does not mean unmerged, it means merged and still being argued about. Before the merge there is no status, only the intake issue.

## Main stages

| Status | Means | Entry condition |
|---|---|---|
| `draft` | Written well enough to read and argue with | Merged as a numbered spec |
| `review` | The author considers it complete and wants scrutiny | The editor asks for it in a pull request |
| `stable` | Safe to build against, changes only for clarification | Evidence gate below is met |
| `deprecated` | Superseded or retired, kept so links keep working | `replaced_by` is set, or a retirement note is added |

## The evidence gate for stable

A spec reaches `stable` only when one of these is true and recorded in the promoting pull request.

- Conformance fixtures exist in the spec's `fixtures/` folder and at least one implementation passes them.
- Two independent implementations interoperate. Independent means separate teams and separate codebases.

This is the gate W3C and IETF both use. It is the difference between a document that looks finished and one that has been shown to work.

## Side statuses

| Status | Means |
|---|---|
| `stagnant` | Six months without activity. Can be revived by any contributor picking it up |
| `withdrawn` | Given up on. Terminal, and the number is never reused |
| `living` | Meant to change continually and never freeze |

`living` covers this repository's own process documents, and indexed entries that track an upstream spec which keeps moving.

## Movement between stages

Anyone can propose a status change in a pull request. Moving to `review` or `stable` needs one approval from a maintainer who is not the spec's editor, the other moves are merged by any maintainer without a second approval. See [intake.md](intake.md).

A spec that moves out, to another standards body or another repository, keeps its folder and number. Its `role` flips to `indexed`, its `upstream` points at the new canonical text, and it gains `index_reason: moved`. If any spec here depends on it or it had reached `stable`, the old text stays in place so that existing links and `depends_on` references keep resolving. Otherwise a stub with the link is enough.
