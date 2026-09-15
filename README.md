# Access Layer Specs

Specifications for the Access Layer, meaning the paths through which people and their agents read from Ethereum, write to it, prove things about themselves, delegate authority, and exit when a provider fails.

The repository defines rules, interfaces, profiles, lifecycle status, and where each spec originally comes from. It does not list tools or implementations. It does not compete with [EIPs and ERCs](https://eips.ethereum.org), [W3C specs](https://www.w3.org/TR/) or the [Tor protocol specs](https://spec.torproject.org/), it links to them, depends on them, or defines Access Layer profiles on top of them.

Renamed from `zkspecs` on 14 September 2026, following [#29](https://github.com/ethereum/access-layer-specs/issues/29). Old links redirect.

Start with [process/](process/README.md) to see how the repository works and where a new spec should go.

## Specifications

| # | Name | Status | Description |
|---|------|--------|-------------|
| 1 | [1/COSS](specs/1/README.md) | draft | Specification framework and editorial process |
| 2 | [2/ANON-AADHAAR-V2](specs/2/README.md) | draft | Privacy-preserving verification of Aadhaar identity cards using ZK proofs |
| 3 | [3/SEMAPHORE-V4](specs/3/README.md) | draft | Anonymous group membership and signaling protocol |
| 4 | [4/EXCUBIAE](specs/4/README.md) | draft | Composable attribute-based access control framework for EVM |
| 5 | [5/ZK-PROOF-OF-PERSONHOOD](specs/5/README.md) | idea | ZK-based proof of personhood for online forums |

## Why these live in their own repository

- Canonical rules are long-lived, while guidance, primitive mappings and tooling information change constantly. Keeping them apart stops one from churning the other.
- Specs need a stricter review, approval and versioning process than the material around them.

## Scope

Every spec here is `hosted`, `mirrored` or `indexed`, and carries a `type` and a lifecycle `status`. The [front matter reference](process/front-matter.md) defines all three, and [lifecycle.md](process/lifecycle.md) defines what each status promises.

Specs may be tagged with the Access Layer verbs they serve, any of `read`, `write`, `prove`, `delegate` and `exit`. A spec routinely serves several. Semaphore covers reading a leaf position, writing an identity into a group, and proving membership, so it carries all three of those tags rather than being filed under one.

## Access Layer Spec Map

Spec and spec-like work that currently lives elsewhere and may move here over time.

| Area | Work | Location | Context here | Notes |
|------|------|----------|--------------|-------|
| Personhood | ZK Proof of Personhood | [`privacy-ethereum/zkID/specs/2-zk-proof-of-personhood`](https://github.com/privacy-ethereum/zkID/blob/main/specs/2-zk-proof-of-personhood/README.md) | Indexed as [`5/ZK-PROOF-OF-PERSONHOOD`](specs/5/README.md) | Adjacent Access Layer spec work |
| Credentials | OpenAC Core | [`privacy-ethereum/zkID/specs/1-openac`](https://github.com/privacy-ethereum/zkID/blob/main/specs/1-openac/README.md) | Drafted in [#21](https://github.com/ethereum/access-layer-specs/pull/21) and [#23](https://github.com/ethereum/access-layer-specs/pull/23) | Protocol material alongside implementation work |
| Age verification | ZK Age Verification | [`privacy-ethereum/zkID/specs/3-zk-age-verification`](https://github.com/privacy-ethereum/zkID/blob/main/specs/3-zk-age-verification/README.md) | Drafted as `6/ZK-AGE-ELIGIBILITY` in [#19](https://github.com/ethereum/access-layer-specs/pull/19) | Adjacent Access Layer spec work |

## Contributing

Read [process/intake.md](process/intake.md). New specs start as an issue, small changes start as a pull request.

## License

[CC0](LICENSE), the same as the EIP repository. Every spec ends with a copyright waiver, see [process/governance.md](process/governance.md).
