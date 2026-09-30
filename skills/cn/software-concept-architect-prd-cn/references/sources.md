# 转录依据

| 来源 | 采用的知识 |
| --- | --- |
| [Jackson：Concept Purposes / Concept Synchronization](https://essenceofsoftware.com/posts/distillation/) | 应用可有多个目的，每个概念仍有自身目的；同步使概念协作实现应用目标。这里只采用目的关系，规则语义采用下述新版 |
| [Jackson 2015，摘要、§8](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | purpose + OP 解释设计为何满足需要，OP 不等于完整行为规格 |
| [WYSIWID v2](https://arxiv.org/abs/2508.14511) / [Beyond Objects v1](https://arxiv.org/abs/2606.27258) | 规格可指导代码/测试，采用因果组合；扩展可能改 sync，也可能改概念 |
| [conceptbox](https://github.com/61040-fa25/conceptbox) / [课程 rubric](https://61040-fa25.github.io/resources/concept-rubric) | 规格与代码共存；notes 记录应用背景 |

固定 Markdown 标题、query API、唯一落点与场景追溯是本仓约定。独立包所需记法已在模板中，不依赖伴生技能；

本轮格式基线：[WYSIWID v1 §4–6](https://arxiv.org/html/2508.14511v1#S4)（核验 2026-09-14）；具名记录、输出 case、状态读取及同步语义见 [统一规格契约](spec-format.md)。旧资料的 queries/Requesting 作为标明的扩展，不能回写为 v1 原文要求。
