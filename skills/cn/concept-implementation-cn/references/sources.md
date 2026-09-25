# 实现依据

核验日期：2026-09-25。下列为本次找到并核对的最新相关公开版本，不把不同论文的语法视为同一套引擎接口。

| 来源 | 采用的知识与边界 |
| --- | --- |
| [Beyond Objects v1，2026-06-25，§12–13](https://arxiv.org/html/2606.27258v1) | 按动作和关系分概念，共享身份；概念不互相引用；query 返回绑定集且不是 action；请求与目标动作分离 |
| [Making Software Meaningful v1，2026-06-09，§4.4–4.5、§5.2](https://arxiv.org/html/2606.11051v1) | 规格、代码与日志共享动作含义；sync 是独立细粒度规则；Requesting 可封装 HTTP/路由，额外分层不是必需。TypeScript 类、DSL 和目录是示例实现 |
| [WYSIWID v2，2025-08-27，§3、§5–6](https://arxiv.org/html/2508.14511v2) | 完成记录匹配、绑定、同 flow 关联及引擎触发恢复；这是本技能采用的执行模型，不代表所有概念实现的唯一选择 |
| [Jackson 2015，§8](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | OP 解释目的兑现，实现符合规格与模型适切性分别判断 |

[统一规格契约](spec-format.md) 仍使用改写自 WYSIWID v1 的具名记录格式；这是仓库格式基线，不代表理论停留在 v1。其 query 扩展与后来的 Beyond Objects 一致，Requesting 也出现在两篇 2026 年论文中，不能统称为旧资料。保留已确认规格方言与签名，不机械迁移。

本仓选择模块单体、可验证的具名规则边界及不以 sync 互调隐藏因果；具体包/文件、port/adapter、mediator 或引擎按需求选择。公开抽象状态不等于开放物理存储或绕过权限。事务、outbox、外部效果幂等、响应及循环控制是实现契约的工程措施，不是 Jackson 的统一技术栈要求；故障恢复能力须以持久触发记录验证。
