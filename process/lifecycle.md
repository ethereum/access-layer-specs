# Lifecycle

Every spec carries a `status`. Five main stages run in order, and three side statuses sit outside that order.

## Main stages

| Status | Means | Entry condition |
|---|---|---|
| `idea` | The shape of a spec exists, the detail does not | An editor accepted the intake issue |
| `draft` | Written well enough to read and argue with | Merged as a numbered spec |
| `review` | The author considers it complete and wants scrutiny | Author requests it, reviewers are assigned |
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

Anyone can propose a status change in a pull request. Promotion to `review` and `stable` needs a reviewer's approval, the rest are editorial.

A spec that moves out, to another standards body or another repository, keeps its folder and number. Its `role` flips to `indexed`, its `upstream` points at the new canonical text, and it gains `index_basis: moved` and an `index_reason` recording the move. If any spec here depends on it or it had reached `stable`, the old text stays in place so that existing links and `depends_on` references keep resolving. Otherwise a stub with the link is enough.
