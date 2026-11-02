# Sources and local choices

| Basis | Use |
| --- | --- |
| [Jackson, Towards a Theory of Conceptual Design for Software (2015), §§8–9](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | Purpose, operational principles, and the distinction between purpose arguments and implementation conformance |
| [The Essence of Software: qualification](https://essenceofsoftware.com/tutorials/concept-basics/criteria/) | Eight criteria for a software concept |
| Meng & Jackson (MIT), WYSIWID v1, §§4–6 (arXiv:2508.14511v1) | Named action inputs/results, causal synchronization, public-state queries, flows, and firing consistency |
| [Beyond Objects v1, §§12–13](https://arxiv.org/html/2606.27258v1#S12) | Behavioral module boundaries and causal composition |
| [Jackson, Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/) | Split/merge, unify/specialize, tighten/loosen |
| [ub-mode](https://github.com/unclebob/ub-mode/blob/master/SKILL.md) | A writing reference for short rules, checking premises, subtracting complexity, and verifiable work |

Markdown sections, `coverage`, `app`/`include`, query APIs, case interpretation, prompt selectors, and decision-record YAML are local conventions.
The directory layout and Sync/Facade naming are engineering choices.

The [Concept and Synchronization Diagram](map-format.md) is a local projection of CONCEPT/SYNCS references.
Its parser, hashed identities, and ARCHITECTURE.md layout are repository choices, not Jackson's purpose-dependency graph.

Specification-maintenance workflows adapt [wyx v0.26.0](https://github.com/jlifyio/wyx); retain its [MIT notice](#wyx-mit).

## wyx (MIT)

```text
MIT License

Copyright (c) 2026 jlifyio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
