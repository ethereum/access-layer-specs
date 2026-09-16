# Intake

## Proposing a spec

1. Open an issue describing what the spec would cover and which Access Layer verbs it serves. Label it `intake` and add the `type` label you expect it to carry.
2. A maintainer confirms it belongs here, using the decision tree in [README.md](README.md). If it belongs to W3C, the Tor process or the ERC process, the editor writes that in the issue, names where to file it instead, and closes the issue.
3. Write the spec by copying [spec-template.md](spec-template.md) into `specs/0000-shortname/README.md`, where `shortname` is the spec's shortname in lowercase, for example `specs/0000-private-read/`.
4. Open a pull request. Leave the number at `0000` while it is in review.
5. On merge, a maintainer renames the folder and sets `id` to the assigned number. The spec starts at `status: draft`. Moving on to `review` and `stable` happens later, in further pull requests, see [lifecycle.md](lifecycle.md).

Small changes to an existing spec skip all of this. Open a pull request.

## Numbering

Numbers are assigned by the merging maintainer, taking the next free number.

- Numbers are never reused, not even when a draft is withdrawn.
- A spec's number never changes, including when it moves to another body.
- The number carries no meaning beyond identity. It is not a priority, a category or a version.

This follows EIP, ENSIP and PEP, which all assign at merge. Some processes instead use the pull request number, which avoids the assignment step but leaves permanent gaps and makes the first spec after a busy period land at an arbitrary number.

While a spec is in review, refer to it by its pull request. Once merged, refer to it by number.

## Review

Two roles are involved. The editor is the person named in the spec's front matter, who writes it and stays accountable for it. Maintainers are the people with write access to this repository, who review and merge.

- Merging a new spec, which hands out its number, needs one approval from a maintainer who is not the editor.
- Moving a spec to `review` or to `stable` needs the same, one approval from a maintainer who is not the editor.
- Small edits that change nothing for implementers, a typo or a better example, need no approval.
