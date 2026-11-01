# Design moves

Choose a move from a demonstrated scenario, not size, names, or shared fields alone.

| Move | Decision and tradeoff |
| --- | --- |
| Split / merge | Separate responsibilities or compose distinct concepts; weigh simplicity, control, and capability. |
| Unify / specialize | Combine variants or keep a specialized fit; weigh generality against the actual need. |
| Tighten / loosen | Add or relax synchronization; weigh automation against user control. |

A narrow concept is a problem when it excludes needed behavior; specialization may be appropriate.
Choose scope by root cause, not changed-line count. Keep no change as an option and reuse prior
authorization. Review-only work produces a proposal, not edits.

For a chosen change, record evidence, alternatives, behavioral differences, affected contracts/rules,
and checks. Preserve invariants and verify application needs. Separate design reasoning from tests
actually run, and intentional redesign from behavior-preserving refactoring.

## Sources

- Daniel Jackson, [Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/), 2022-04-18. Move pairs and tradeoffs.
- Daniel Jackson, [Beyond Objects](https://arxiv.org/abs/2606.27258), 2026-06-25. Conflation and fragmentation from object-based partitioning.
- Eagon Meng et al., [Making Software Meaningful](https://arxiv.org/abs/2606.11051), 2026-06-09. Shared meanings grounded in observable behavior.
- [What You See Is What It Does](https://arxiv.org/abs/2508.14511), 2025. Independent concepts and explicit synchronization.

The workflow adapts these publications. Dates identify consulted versions.
