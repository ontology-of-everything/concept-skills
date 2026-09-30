# Design moves and evidence

Read this before selecting a move or interpreting a suspected smell.

| Move | Target and tradeoff |
| --- | --- |
| Split / merge | Separate responsibilities or compose distinct concepts; weigh simplicity against control and capability. |
| Unify / specialize | Unify variants of a theme or introduce specialized variants; weigh generality against fit. |
| Tighten / loosen | Strengthen or weaken synchronization between concepts; weigh automation against user flexibility. |

A smell is a hypothesis, not a verdict. Size, names, and shared fields alone do not establish
conceptual overload or redundancy. Narrowness matters when needed behavior is excluded;
specialization can be appropriate. Judge the smallest sufficient scope by the root cause,
not the number of changed lines. Preserve settled authorization; ask only about unresolved
consequential choices. Review-only requests produce proposals, not edits.

For each chosen change, show the scenario and evidence, alternatives including no change,
expected behavioral differences, affected contracts/synchronizations, and verification results.
Distinguish reasoning over a design from executed tests. Keep concept invariants valid and
check application-level requirements too; passing local tests alone does not establish fit.
An intentional behavior change is redesign, not a claim of behavior-preserving code refactoring.

## Sources

These instructions adapt the sources below; the workflow is not a quoted or endorsed method.

- Daniel Jackson, [Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/),
  2022-04-18: the three pairs of moves and their tradeoffs.
- Daniel Jackson, [Beyond Objects](https://arxiv.org/abs/2606.27258), 2026-06-25 preprint:
  functionality conflation and fragmentation caused by partitioning around domain individuals.
- Eagon Meng et al., including Daniel Jackson,
  [Making Software Meaningful](https://arxiv.org/abs/2606.11051), 2026-06-09 preprint:
  explicit, shared meaning grounded in observable behavior.
- [What You See Is What It Does](https://arxiv.org/abs/2508.14511), 2025:
  independent concepts and explicit synchronizations; local guarantees and application composition.

Dates identify consulted publications, not an ongoing claim that they are the latest research.
