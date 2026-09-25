---
id: 6
title: Key Pinned Streams
description: Authenticated multiplexed byte streams to a peer pinned by certificate hash, over WebRTC or QUIC
shortname: KPS
role: indexed
type: protocol
status: draft
domains: [read, write]
tags: [transport, key-pinning, streams, datagrams, webrtc, quic]
editor: Andrew Morris <andrew.morris@ethereum.org>
contributors: []
depends_on: []
replaces: []
replaced_by: null
upstream: https://github.com/ethereum/kps/blob/main/SPEC.md
index_reason: moved
---

> **The text of this spec lives in [`ethereum/kps`](https://github.com/ethereum/kps/blob/main/SPEC.md).** It is written and maintained there, currently at draft version 0.2.1. Read it upstream. This entry exists so the registry names it and so other specs here can cite it by number.

A KPS endpoint is identified by a hash of its self-signed certificate rather than by a CA-signed domain name, so anyone who can pass along an address — a UDP endpoint plus that hash — can also authenticate the peer at the other end. No certificate authority, no DNS, and no ambient trust in whoever distributed the address.

On top of that identity the spec defines an encrypted, multiplexed connection carrying unnamed reliable ordered bidirectional byte streams, plus unreliable connection-level datagrams. Two transports are defined, WebRTC so a browser can dial, and QUIC for native peers, and which one carries a connection is hidden from the caller: the same peer can serve both. Message framing, routing and request/response semantics are left to whatever is layered on top.

Pinning a peer by key rather than by name takes the certificate authority and the DNS root out of the path a client uses to reach anything at all, which is what earns the entry its own number here rather than a mention inside whatever is layered on top. [7/ANON-RPC](../7-anon-rpc/README.md) is the first of those in this repository: its workers reach the network over KPS streams, and its harnesses fetch client bundles over them.
