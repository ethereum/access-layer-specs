---
id: 0000
title: Anonymized RPC
description: Anonymized RPC by running hash-pinned client code in a sandboxed, capability-limited worker
shortname: ANON-RPC
role: indexed
type: interface
status: draft
domains: [read, write]
tags: [privacy, rpc, anonymity, sandboxing, content-addressing, wallet]
editor: Andrew Morris <andrew.morris@ethereum.org>
contributors: []
depends_on: [0]   # 0000-kps, added in the same pull request
replaces: []
replaced_by: null
upstream: https://github.com/ethereum/anon-rpc/blob/main/SPEC.md
index_reason: moved
---

> **The text of this spec lives in [`ethereum/anon-rpc`](https://github.com/ethereum/anon-rpc/blob/main/SPEC.md).** It is written and maintained there, currently at version 0.3.1, alongside its [changelog](https://github.com/ethereum/anon-rpc/blob/main/CHANGELOG.md). Read it upstream. This entry exists so the registry names it and so other specs here can cite it by number.

A wallet that reads from or writes to a chain has to reach an RPC endpoint, and a fixed gateway concentrates observation: it learns who asked for what, and when. anon-rpc specifies how a host runs a pluggable anon-client instead, identified by the hash of its bundle rather than by where the bundle was downloaded from, inside a sandbox that denies it the DOM, storage, cookies and signing keys, and reachable only through a small explicit capability API. What the host gets back is an ordinary `fetch`.

The spec covers the on-chain specifier contract that names a client bundle by `keccak256` hash and advertises where it may be obtained, how a harness retrieves and integrity-checks those bytes, the isolation a worker runs under, the host-facing and worker-facing API surfaces, and the error model. It deliberately says nothing about which anonymity network a client implements: the capability API hands the worker byte streams, and the routing above them is the client's own business. Those streams are Key Pinned Streams, specified separately in [`0000-kps`](../0000-kps/README.md).
