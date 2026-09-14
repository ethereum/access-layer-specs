# Governance

> **Status: open.** The licence choice below has not been made. It needs an answer from EF legal before the repository takes contributions at any volume, because a contributor agreement cannot be applied retroactively to text people have already written.

Four things need to be written down before the repository grows. Retrofitting any of them after people have contributed is considerably harder than agreeing them now.

## 1. Contributor agreement

Everyone contributing spec text agrees up front that the project can use it, so that nobody can later claim rights over a spec that others have implemented.

## 2. Spec licence

The repository currently carries [MIT](../LICENSE), inherited from its time as `zkspecs`. Two options are on the table.

- A spec licence with patent commitments, where contributors promise not to sue anyone who implements a spec over patents covering it. An open-source licence alone does not give this, because copyright and patents are separate grants. This is what makes companies comfortable building on a spec.
- Public domain via CC0, which is what the EIP process uses. It makes moving text into an ERC trivial, and it gives implementers no patent protection at all. The EIP process lives with that gap.

Whichever is chosen, the licence must permit re-releasing a graduated spec's text as CC0, because the ERC process requires it.

## 3. Approval rule

What counts as consensus for merging a spec, and for promoting one to `review` or `stable`. See [intake.md](intake.md) for the current working rule, which needs ratifying rather than inventing.

## 4. Tie-breaker

A named person who decides when reviewers disagree, so that a dispute cannot freeze the repository indefinitely.

## A ready-made option

Rather than drafting all four from scratch, the Linux Foundation's [Community Specification template](https://github.com/CommunitySpecification/1.0) ships them as complete documents. SPDX runs on a modified version of it. Adopting it would settle pieces 1, 3 and 4 at once and make piece 2 the only real decision left.
