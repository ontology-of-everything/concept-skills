# 审计依据

| 一手来源 | 采用的知识 |
| --- | --- |
| [Jackson：Concept Purposes / Concept Synchronization](https://essenceofsoftware.com/posts/distillation/) | 应用可有多个目的，每个概念仍有自身目的；同步使概念协作实现应用目标。这里只采用目的关系，规则语义采用下述新版 |
| [Jackson 2015，摘要、§8–9、讨论](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | 审 purpose + OP 论证；负场景揭示目的落空；需同时了解设计与论证，论证差不自动证明系统无用 |
| [资格](https://essenceofsoftware.com/tutorials/concept-basics/criteria/) / [组合](https://essenceofsoftware.com/tutorials/concept-basics/sync/) / [依赖](https://essenceofsoftware.com/tutorials/concept-basics/dependency/) | API 程序员也属用户；欠/过同步；概念依赖与产品子集 |
| [Beyond Objects v1](https://arxiv.org/abs/2606.27258) / [WYSIWID v2](https://arxiv.org/abs/2508.14511) | 概念与因果规则语义；部分扩展可只改 sync，也可能需改概念 |
| [wyx](https://github.com/jlifyio/wyx) | 漂移检查表与扫描机制的上游，已按本仓语义调整 |

定义独立性、目的适切性与工程互不引用分别审查。query API、Markdown 记法、五维报告及严重度为本仓约定；公开抽象状态的合法读取不误报为理论违规。持续 CI 与按需审计互补，测试通过不替代目的论证。

本轮格式基线：[WYSIWID v1 §4–6](https://arxiv.org/html/2508.14511v1#S4)（核验 2026-09-14）；具名记录、输出 case、状态读取及同步语义见 [统一规格契约](spec-format.md)。旧资料的 queries/Requesting 作为标明的扩展，不能回写为 v1 原文要求。
