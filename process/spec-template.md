# Spec template

Copy this into `specs/0000-shortname/README.md`, with your shortname in lowercase, and fill it in. Leave `id` and the folder number at `0000` until the spec is merged.

Delete any section that genuinely does not apply, and say why in the pull request.

````md
---
id: 0000
title: Your Spec Name
description: One line, shown in the index table
shortname: YOUR-SPEC
role: hosted
type: protocol
status: draft
domains: []
tags: []
editor: Your Name <you@example.com>
contributors: []
depends_on: []
replaces: []
replaced_by: null
upstream: null
# index_reason: dependency | moved   (required when role is indexed)
---

# Your Spec Name

## Abstract

One paragraph. What this specifies, and for whom.

## Motivation

What breaks today without this. Be concrete about who is blocked.

## Terminology

Define every term the spec relies on, including ones that look obvious.

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT,
RECOMMENDED, MAY and OPTIONAL are to be interpreted as described in
[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

## Specification

The normative part. Anything an implementer must follow belongs here, and
nothing else does. Use the RFC 2119 words above and mean them.

## Rationale

Why this design rather than the alternatives you considered. Record the
alternatives, so the next reader does not reopen a settled question.

## Security Considerations

Threat model, what the spec does not protect against, and what an
implementer can get wrong.

## Privacy Considerations

What is observable, by whom, and what is leaked by ordinary use.

## Conformance

How an implementer checks they got it right. Point at `fixtures/` if the
spec has test vectors.

## Copyright

Copyright and related rights waived via [CC0](../../LICENSE).
````

## Fixtures

Conformance test vectors live next to the spec, in `specs/0000-shortname/fixtures/`. Name them for what they assert, for example `valid-receipt.json` and `invalid-missing-proof.json`.

A spec needs fixtures, or two interoperating implementations, before it can reach `stable`. Starting them at `draft` is much easier than retrofitting them later.
