# 实现依据

日期标识所参考版本，工程约定更新于 2026-11-01。

| 来源 | 用途 |
| --- | --- |
| [Beyond Objects v1，2026-06-25，第 12、13 节](https://arxiv.org/html/2606.27258v1) | 独立概念共享身份、关系查询、请求与目标动作分离。 |
| [Making Software Meaningful v1，2026-06-09，第 4.4、4.5、5.2 节](https://arxiv.org/html/2606.11051v1) | 规格/代码/日志共享含义、细粒度规则、Requesting 的 HTTP/路由示例。 |
| [WYSIWID v2，2025-08-27，第 3、5、6 节](https://arxiv.org/html/2508.14511v2) | 完成匹配、绑定、flow 关联与触发恢复。 |
| [Jackson 2015，第 8 节](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | 区分目的/OP 论证与实现符合性。 |

[本仓契约](spec-format.md)采用改写的 WYSIWID v1 记录记法并扩展查询。
保留已确认方言，不把论文语法视为可互换的引擎 API。

## 工程选择

默认模块独立构建、server 同进程装配。composition 保存具名规则，api 映射协议。
[端口与适配器](https://alistair.cockburn.us/hexagonal-architecture)隔离设施，领域与应用职责不同时再采用 [Clean 分层](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)。
论文不要求这两种风格，也允许 Requesting 封装 HTTP/路由。

按契约选择 mediator/引擎、事务、outbox、幂等、响应与循环控制，用持久记录核验恢复。
公开状态不开放私有存储或绕过权限。这些是工程决策，不是 Jackson 规定的统一技术栈。
