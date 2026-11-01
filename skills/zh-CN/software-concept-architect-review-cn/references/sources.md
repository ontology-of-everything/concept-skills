# 审查依据

| 来源 | 用途 |
| --- | --- |
| [概念目的](https://essenceofsoftware.com/posts/distillation/) | 区分应用目的与概念目的。 |
| [Jackson 2015，第 8、9 节](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | 检查目的/OP 论证与反例，论证薄弱本身不证明软件无用。 |
| [资格](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)、[组合](https://essenceofsoftware.com/tutorials/concept-basics/sync/)、[依赖](https://essenceofsoftware.com/tutorials/concept-basics/dependency/) | API 用户、协调缺陷与产品子集。 |
| [Beyond Objects](https://arxiv.org/abs/2606.27258) 与 [WYSIWID](https://arxiv.org/abs/2508.14511) | 概念契约与因果规则。 |
| [wyx](https://github.com/jlifyio/wyx) | 按本仓语义调整的漂移扫描机制。 |

定义独立性、目的兑现与工程依赖分别审查。query API、Markdown、报告维度和严重度是本仓约定。
公开抽象状态允许读取，测试不代替目的审查。

[规格契约](spec-format.md)改写自 [WYSIWID v1 第 4 至 6 节](https://arxiv.org/html/2508.14511v1#S4)，标明查询与入口扩展。
该格式基线核验于 2026-09-14。
