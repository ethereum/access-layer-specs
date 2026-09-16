# Intake

## Proposing a spec

1. Open an issue describing what the spec would cover and why no existing standards body should own it. Label it `intake` and add the `type` label you expect it to carry.
2. An editor confirms it belongs here, using the decision tree in [README.md](README.md). If it belongs to W3C, the Tor process or the ERC process, the issue records that and closes.
3. Write the spec by copying [spec-template.md](spec-template.md) into `specs/0000-your-slug/README.md`.
4. Open a pull request. Leave the number at `0000` while it is in review.
5. On merge, the maintainer renames the folder and sets `id` to the assigned number.

Small changes to an existing spec skip all of this. Open a pull request.

## Numbering

Numbers are assigned by the maintainer at merge, taking the next free number.

- Numbers are never reused, including by withdrawn specs.
- A spec's number never changes, including when it graduates to another body.
- The number carries no meaning beyond identity. It is not a priority, a category or a version.

This follows EIP, ENSIP and PEP, which all assign at merge. Some processes instead use the pull request number, which avoids the assignment step but leaves permanent gaps and makes the first spec after a busy period land at an arbitrary number.

While a spec is in review, refer to it by its pull request. Once merged, refer to it by number.

## Labels

Intake issues carry a `type` label so the incoming queue can be filtered by what kind of spec is being proposed. Labels mirror the `type` field and are a convenience only. Front matter is the source of truth, since labels cannot attach to files.

## Review

Every spec needs a named editor before it is merged, and that person stays accountable for the entry.

Promotion to `review` and to `stable` needs a reviewer other than the editor. Editorial changes, typo fixes and clarifications need one approval from anyone with write access.
