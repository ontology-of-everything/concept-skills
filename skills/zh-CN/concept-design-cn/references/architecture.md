# 工程架构

本结构是仓库约定，不是 Jackson 指定的实现。
新项目 SHOULD 使用多模块单体。
概念独立构建与测试；组合和协议适配器随 server 构建，分别测试行为。
同进程装配。
既有项目的确认约定优先。

## 架构要求

1. **概念自足。** 每个概念围绕一个目的定义自己的状态和动作，并拥有其业务状态。见[概念规格](spec-notation.md#concept)。
2. **概念独立。** 禁止概念之间的源码依赖、动作或查询调用，以及状态读取。
3. **同步组合概念。** 在概念之外用一条具名同步表达一个应用决定。通过公开动作和查询访问概念。见[同步规格](spec-notation.md#syncs)。
4. **同步连接外部入口。** 将外部请求接入根动作。由同步发起概念动作并触发对原请求的响应。
5. **保持因果边界。** 只匹配同一 flow 的完成记录。后续调用沿用该 flow 并保留触发来源。
6. **明确失败与前置条件。** 声明相关失败分支。前置条件满足后才发起依赖动作。
7. **一次匹配只触发一次。** 分发前按规则身份、匹配的完成记录和绑定行原子认领触发。见[规则执行](execution.md#规则执行)。

## 归属与形状

**Composition（组合）**表达架构职责：通过独立概念组合出业务能力，组合层目录用 `composition/`。**Synchronization（同步）**表达组合规则：匹配动作完成记录，在条件满足时触发后续动作。

```text
apps/server/
  src/
    bootstrap/                    # 构造与最终装配
    adapters/http/                # 协议转换
    composition/booking/
      reserve/
        MakeReservationUseCase
        SYNCS.md
        ReserveMediator          # sync reserve
        SuccessReplyMediator     # sync accepted
        ConflictReplyMediator    # sync rejected
  tests/                          # 架构、组合、协议
modules/<context>/concepts/<concept>/
  CONCEPT.md
  <build manifest>
  src/
    <business exports>
    <assembly entry>
    domain/                       # 状态与不变量
    application/                  # 动作与查询
      ports/                      # 内部代码所需契约
    adapters/                     # 端口实现
  tests/
libraries/<technical capability>/ # 按需独立构建与测试
deploy/                           # 环境与部署
```

上下文目录划分模型与语言；概念不等于 DDD 聚合。
源码根目录采用[语言映射](language-mapping.md)。
小概念 MAY 平铺。
不建空层，不为每条规则拆构建模块，不在每个组合分组内再套 domain/application/adapters。

| 归属 | 约束 |
| --- | --- |
| 概念 | 外部身份用类型参数或不透明 ID。 |
| domain | MUST 维护不变量，且不依赖 application、adapters、HTTP 或 ORM。 |
| application | 使用 domain，声明所需端口。领域专用端口可归 domain。 |
| adapter | 实现内部端口。同一职责不重复建 repository/reader。 |
| composition | MAY 拥有执行记录；MUST NOT 复制概念业务事实。 |
| 协议适配器 | 通过组合入口转换输入输出；MUST NOT 引入概念实现。 |
| bootstrap | 生产构造与装配入口。受限测试 fixture/测试装配 MAY 构造概念和假端口。 |
| 技术库 | MUST NOT 依赖概念或组合，也不得隐藏业务状态或协调。 |

业务代码 MUST NOT 从容器查找依赖。
业务导出与构造入口分开，生产构造访问限制在 bootstrap。
值类型留在所属模型，直到共享语义、约束、归属和变更责任明确。
共享数据库设施与迁移 MUST 保持状态归属。

## 规格归属

以下为文件组织约定，沿用项目源码根目录和已有分组。

| 内容 | 权威位置 |
| --- | --- |
| 概念 | 模块旁 `CONCEPT.md`；模块未建时 `docs/prd/concepts/<name>/CONCEPT.md`。 |
| 同步 | `apps/<app>/src/composition/<group>/` 规则旁 `SYNCS.md`；模块未建时 `docs/prd/composition/<group>/SYNCS.md`。 |
| 验收 | 总体 PRD 或已有验收文件，关联所检查的契约或场景。 |

总体 PRD 索引全部 CONCEPT 与 SYNCS。
未授权迁移时保留已确认旧位置，包括 `docs/prd/SYNCS.md`。
文件及 `// flow:` 分组不创建运行时 flow 身份，也不要求独立构建。
实例、绑定、入口契约与规则身份遵循下述约定。

## 组合分组与身份

按业务职责分组。分组可跨上下文，粒度独立于概念、接口和 flow。
每组共置一份 [SYNCS.md](spec-notation.md#syncs)。索引列全分组，每条规则只定义一次。
应用实例身份、类型绑定和共用入口契约各声明一次。各组引用声明。
重复 include MUST 指向同一声明实例，bootstrap MUST 保持该映射。
单个操作 MAY 用 `<Operation>UseCase` 作为入口。多个操作 MAY 共用 `<BusinessScope>Facade`。

新实现 SHOULD 用 `<BusinessEffect>Mediator`，如 `ReserveMediator`。触发条件有助于理解或区分规则时，可写进名称。
保留已确认的名称，明确原生代码名的映射。
规则身份 MUST 在应用内唯一，并在规格、测试和运行记录中保持稳定。移动文件 MUST NOT 改变持久规则身份。
默认一条规则一个文件。相关小规则 MAY 同文件，各自保留身份。

### 拆分同步

- 触发条件、业务效果或失败策略可独立变化时，拆成具名同步。
- 同一效果依赖多个前置结果时，在同一条 `when` 中匹配同一 flow 的所有所需结果。
- 仅实现变复杂时，在规则内提取辅助函数，保留规则身份和触发边界。多条规则形成独立业务职责时，可单独成组。

用动作完成记录衔接规则。规则 MUST NOT 直接互调。
长期等待、超时和补偿须明确所需过程状态。该状态出现独立业务目的与生命周期时，重新评估概念边界。

## 审查与验证

必要迁移见[执行与恢复](execution.md)。
指定产品子集须检查目的、依赖、入口、规则、资源、构建开关和发布归属。

架构检查 MUST 检查所有相关源码/构建单元及支持配置中的实际依赖。
覆盖概念独立、公开业务 API 访问、依赖向内、协议入口、构造访问、技术库、环、规格归属和规则身份唯一。
受影响的边界检查接入常规检查或 CI。
空匹配、漏模块、未解析依赖是缺口，不是通过。
每条违规报告规则、来源、目标和位置，并使检查失败。
用隔离违规验证相应检查确实失败。
报告反射、动态查找和跨归属 SQL 等限制，按需补定向检查。

## 工程依据

[DDD](https://www.domainlanguage.com/ddd/reference/)用于模型边界。
[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)与
[Ports and Adapters](https://alistair.cockburn.us/hexagonal-architecture)用于依赖方向。
