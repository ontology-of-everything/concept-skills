# Audit Sources

| Primary source                                                                                                                                                                                                                                       | Adopted knowledge                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [Concept Purposes and Synchronization](https://essenceofsoftware.com/posts/distillation/)                                                                                                                                                            | applications may have several purposes; each concept has its own; synchronization composes them                        |
| [Jackson 2015, abstract and sections 8–9](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)                                                                                                                                              | audit the purpose/OP argument; negative scenarios expose misfit; a weak argument alone does not prove a system useless |
| [Qualification](https://essenceofsoftware.com/tutorials/concept-basics/criteria/), [composition](https://essenceofsoftware.com/tutorials/concept-basics/sync/), and [dependency](https://essenceofsoftware.com/tutorials/concept-basics/dependency/) | API programmers are users; under/over-synchronization; concept dependencies and product subsets                        |
| [Beyond Objects](https://arxiv.org/abs/2606.27258) and [WYSIWID](https://arxiv.org/abs/2508.14511)                                                                                                                                                   | concept and causal-rule semantics                                                                                      |
| [wyx](https://github.com/jlifyio/wyx)                                                                                                                                                                                                                | upstream drift scanning mechanics adapted to this repository's semantics                                               |

Audit definition independence, fitness for purpose, and the repository's no-module-reference rule
separately. Query interfaces, Markdown notation, the five-dimension report, and severity calibration
are local conventions. Reading public abstract state is not a theoretical violation. Continuous CI
complements, rather than replaces, purpose review.

The format baseline is WYSIWID v1 sections 4–6, verified 2026-09-14. Named records, result cases,
state reads, and synchronization semantics are consolidated in `spec-format.md`; legacy queries and
Requesting remain labeled extensions.
