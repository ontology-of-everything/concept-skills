---
name: software-concept-architect-build-cn
description: "Generates confirmed concept implementations. Use when explicitly invoked. 将确认模型落实为模块与同步规则。"
metadata:
  language: zh-CN
  translation_of: software-concept-architect-build
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# 软件概念架构师 · 实现

## 目标

实现已确认的概念模型，或交付用户要求的实现方案。仅在显式调用 `$software-concept-architect-build-cn` 时运行。
输入包括规格、应用目的、场景和已确认的工程约定。

## 原则

默认模块单体，模块独立构建和测试，由 server 同进程装配。
业务调用依次经过 api、composition 和概念接口，公开装配工厂与业务接口分开。

默认端口与适配器，需要区分领域与应用职责时采用 Clean 分层。不建空层或纯转发层。
已有工程沿用确认约定，迁移限于任务范围。

保留概念契约、权限、关联、失败和排除决定。规格、代码与日志中的概念、动作和参数含义一致。模型缺口保持未决。

## 概念

| 模块 | 职责 |
| --- | --- |
| concept | 拥有业务状态，公开动作与查询；外部身份用类型参数或不透明 ID，概念之间不互引。 |
| composition | 公开应用接口，通过具名 syncs 协调概念，规格保存在 SYNCS。 |
| api | 将外部协议与数据映射到 composition 接口。 |
| server / shared | 统一装配 / 提供不依赖业务模块的被动类型。 |

动作是可观察的发生，也可以只读。查询返回绑定，不产生完成事件。请求可以发生，目标动作未必发生。

## 流程

1. 读[规格契约](references/spec-format.md)、确认模型、工程约定及相关代码和测试，继续不依赖未决项的工作。
2. 定义边界时读[工程架构](references/architecture.md)，再只读目标语言：
   [Rust / Axum](references/rust.md)、[Java / Spring](references/java-spring.md)或[TypeScript](references/typescript.md)。
   明确构建单元、接口、状态拥有者和装配入口。
3. 写规则前读[执行与恢复](references/execution.md)。保留具名边界，按匹配和恢复需求选择 mediator 或引擎。
4. CONCEPT 与概念共置，SYNCS 与 composition 共置，文件内按入口或职责分组并更新 PRD 索引。
   有实际分组需要时再读[分组与扩展](references/scaling.md)。
5. 构建和测试受影响模块与装配。检查运作原理、不变量、规则分支、应用场景、并发、所需恢复，以及构建和源码访问边界。

区分论文与工程约定时读[实现依据](references/sources.md)。

## 正反例

| 正例 | 反例 |
| --- | --- |
| 支付和预约各自独立，具名规则在支付完成后发起预约确认。 | 预约概念内部直接调用支付概念。 |
| 需要重启后恢复时，通过端口接入执行记录存储。 | 仅凭内存监听器就声称支持持久恢复。 |

## 完成条件

规格代码一致，执行可追溯，排除动作不可达。交付子集时核对目的、依赖、入口、规则、资源与构建开关。
报告测试与缺口，模型问题交设计，转录错误交 PRD。符合规格不等于兑现目的。
