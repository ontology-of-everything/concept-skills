# Review sources

| Source | Used for |
| --- | --- |
| [Concept purposes](https://essenceofsoftware.com/posts/distillation/) | Separate application and concept purposes. |
| [Jackson 2015, sections 8 and 9](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | Review purpose/OP arguments and counterexamples. A weak argument alone does not prove useless software. |
| [Qualification](https://essenceofsoftware.com/tutorials/concept-basics/criteria/), [composition](https://essenceofsoftware.com/tutorials/concept-basics/sync/), [dependency](https://essenceofsoftware.com/tutorials/concept-basics/dependency/) | API users, coordination defects, and product subsets. |
| [Beyond Objects](https://arxiv.org/abs/2606.27258) and [WYSIWID](https://arxiv.org/abs/2508.14511) | Concept contracts and causal rules. |
| [wyx](https://github.com/jlifyio/wyx) | Drift-scanning mechanics adapted to this repository. |

Review definition independence, purpose fulfillment, and engineering dependencies separately.
Query APIs, Markdown, report dimensions, and severity are local conventions; public abstract-state
reads are allowed. Tests do not replace purpose review.

[The contract](spec-format.md) adapts [WYSIWID v1 sections 4 to 6](https://arxiv.org/html/2508.14511v1#S4)
and labels query/entry extensions. The format baseline was checked on 2026-09-14.
