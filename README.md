# Access Layer Specs

Specifications for the Access Layer, meaning the paths through which people and their agents read from Ethereum, write to it, prove things about themselves, delegate authority, and exit when a provider fails.

The repository defines rules, interfaces, profiles, lifecycle status, and where each spec originally comes from. It does not list tools or implementations. It does not compete with [EIPs and ERCs](https://eips.ethereum.org), [W3C specs](https://www.w3.org/TR/) or the [Tor protocol specs](https://spec.torproject.org/), it links to them, depends on them, or defines Access Layer profiles on top of them.

Renamed from `zkspecs` on 14 September 2026, following [#29](https://github.com/ethereum/access-layer-specs/issues/29). Old links redirect.

Start with [process/](process/README.md) to see how the repository works and where a new spec should go.

## Specifications

| # | Name | Type | Status | Domains | Description |
|---|------|------|--------|---------|-------------|
| 1 | [1/COSS](specs/1-coss/README.md) | process | deprecated | — | Specification framework and editorial process, superseded by process/ |
| 2 | [2/ANON-AADHAAR-V2](specs/2-anon-aadhaar-v2/README.md) | protocol | draft | prove | Privacy-preserving verification of Aadhaar identity cards using ZK proofs |
| 3 | [3/SEMAPHORE-V4](specs/3-semaphore-v4/README.md) | protocol | draft | read, write, prove | Anonymous group membership and signaling protocol |
| 4 | [4/EXCUBIAE](specs/4-excubiae/README.md) | protocol | draft | prove, delegate | Composable attribute-based access control framework for EVM |
| 5 | [5/ZK-PROOF-OF-PERSONHOOD](specs/5-zk-proof-of-personhood/README.md) | protocol | draft | prove | ZK-based proof of personhood for online forums, text currently in zkID |

## Why these live in their own repository

- Specs change slowly. The guides and tool lists around them change weekly. Kept together, every small update to a guide would show up as a change to the specs.
- Specs need a stricter review, approval and versioning process than the material around them.

## Scope

Every spec here is `hosted`, `mirrored` or `indexed`, and carries a `type` and a lifecycle `status`. The [front matter reference](process/front-matter.md) defines all three, and [lifecycle.md](process/lifecycle.md) defines what each status promises.

Specs may be tagged with the Access Layer verbs they serve, any of `read`, `write`, `prove`, `delegate` and `exit`. A spec routinely serves several. Semaphore covers reading a leaf position, writing an identity into a group, and proving membership, so it carries all three of those tags rather than being filed under one.

## Contributing

Read [process/intake.md](process/intake.md). New specs start as an issue, small changes start as a pull request.

## License

[CC0](LICENSE), the same as the EIP repository. Every spec ends with a copyright waiver, see [process/governance.md](process/governance.md).
