# 工程架构

本结构是仓库约定，不是 Jackson 指定的实现。
新项目 SHOULD 使用多模块单体。
概念独立构建与测试；组合和协议适配器随 server 构建，分别测试行为。
同进程装配。
既有项目的确认约定优先。

## 归属与形状

```text
apps/server/
  src/
    bootstrap/                    # 构造与最终装配
    adapters/http/                # 协议转换
    compositions/booking/
      BookingFacade               # 可选入口
      make_reservation/
        SYNCS.md
        CreateReservationSync
        ConfirmReservationSync
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
源码根目录采用[语言映射](languages.md)。
小概念 MAY 平铺。
不建空层，不为每条规则拆构建模块，不在每个组合分组内再套 domain/application/adapters。

| 归属 | 约束 |
| --- | --- |
| 概念 | MUST 拥有业务状态。MUST NOT 引入另一概念、调用其动作/查询或读取其状态。外部身份用类型参数或不透明 ID。 |
| domain | MUST 维护不变量，且不依赖 application、adapters、HTTP 或 ORM。 |
| application | 使用 domain，声明所需端口。领域专用端口可归 domain。 |
| adapter | 实现内部端口。同一职责不重复建 repository/reader。 |
| composition | 使用概念公开动作与查询。MAY 拥有执行记录；MUST NOT 复制概念业务事实。 |
| 协议适配器 | 通过组合入口转换输入输出；MUST NOT 引入概念实现。 |
| bootstrap | 生产构造与装配入口。受限测试 fixture/测试装配 MAY 构造概念和假端口。 |
| 技术库 | MUST NOT 依赖概念或组合，也不得隐藏业务状态或协调。 |

业务代码 MUST NOT 从容器查找依赖。
业务导出与构造入口分开，生产构造访问限制在 bootstrap。
值类型留在所属模型，直到共享语义、约束、归属和变更责任明确。
共享数据库设施与迁移 MUST 保持状态归属。

## 组合分组与身份

按业务职责分组；分组可跨上下文。
每组共置一份 SYNCS.md，索引全部分组且不重复定义。
分组数不必对应概念、接口或运行时 flow。
应用实例身份、类型绑定和共用入口契约声明一次，各组引用。
重复 include MUST 指向同一声明实例，bootstrap MUST 保持该映射。

新实现 SHOULD 使用 `<BusinessEffect>Sync`，如 `CreateReservationSync`。
只有效果名称重合时才补触发条件。
保留确认名称，明确原生代码名称映射。
规格、测试和运行记录中的规则身份 MUST 稳定且应用内唯一。
移动文件 MUST NOT 改变持久规则身份。
默认一条规则一个文件；相关小规则 MAY 同文件，但各自保留身份。

规则通过概念动作协调，MUST NOT 直接互调。
可选 `<BusinessScope>Facade` 提供稳定入口；协调留在具名规则中。
长期等待、超时和补偿须明确所需过程状态。
该状态出现独立业务目的与生命周期时，重新评估概念边界。

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
