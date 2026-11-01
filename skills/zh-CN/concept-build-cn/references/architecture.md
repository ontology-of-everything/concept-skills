# 工程架构

本页说明模块职责，构建配置只读目标语言映射。

## 依赖与状态

```text
api → composition → concepts
server 通过公开工厂装配所有模块
```

第一行表示业务调用。概念之间不互调、不互引，server 经公开工厂装配，协调留在 composition。

| 模块 | 允许的业务依赖 | 公开接口 |
| --- | --- | --- |
| concept | 按需依赖 shared | 动作、查询、结果类型、必要完成事件 |
| composition | 概念接口、shared | 应用请求与结果，使用自身或 shared 类型 |
| api | composition 接口、shared | 协议映射与路由配置工厂 |
| shared | 无 | 身份、时间等被动类型 |
| server | 公开装配入口 | 启动与配置 |

概念拥有自己的业务状态和存储访问。可共享数据库设施，读写仍经过拥有者，迁移须标明归属。
composition 可以保存执行记录，不持有独立业务状态。

## 构建结构

```text
apps/server/                 # 唯一启动应用
modules/
  concepts/<名称>/           # 每个概念一个构建单元
    CONCEPT.md
    src/
  composition/               # 应用接口与协调
    SYNCS.md
    src/
      syncs/                 # 具名规则，不另成构建单元
  api/                       # 协议、DTO 与错误映射
  shared/                    # 被动类型
```

composition 是模块，syncs 是规则集合，sync 是单条规则。模块根目录一份 SYNCS，按入口或职责分组。
源码路径按语言映射，例如 Java 的 composition.syncs 包。

每个模块有清单、公开接口和构建测试入口。定向构建包含依赖，独立构建不表示单独启动或部署。
分组只用于导航，不自动成为构建单元。单模块任务不补齐无关工程结构。

## 端口与分层

需要设施的内层代码声明契约，adapter 实现，server 经受限工厂注入。
核心策略应能脱离 HTTP、SQL 或具体调度器测试。

| 模块 | 内部组织 |
| --- | --- |
| composition | 具名规则与应用接口，按需增加执行端口、恢复适配器 |
| concept | 简单行为集中实现，职责不同再采用 domain/application/adapter |
| api | 入站适配，无领域职责就不加领域层 |

采用 Clean 时，domain 保存模型和不变量，application 实现动作与查询，adapter 接入设施，依赖指向内层。
不建空层、纯转发层，不给既有接口再包相同端口。内部层次用包或目录，不另拆构建单元。
已有确认约定优先，本基线不自动授权迁移。

## 示例与检查

已确认预约与支付契约时：

```text
请求完成         → Reservation.hold
hold[Held]       → Payment.charge
charge[Paid]     → Reservation.confirm
charge[Declined] → Reservation.cancel
```

匹配 flow 与预约身份，相关动作完成后响应，取消失败则保留待办。详细要求见[执行与恢复](execution.md)。

| 正例 | 反例 |
| --- | --- |
| 同查构建清单和源码访问。 | 只凭目录或无环图证明全部边界。 |
| 通过具名规则协调。 | Controller 编排概念，或概念互调。 |
| 公开受限装配工厂。 | 为方便装配而开放全部实现。 |
| 验证拒绝、部分完成与重试。 | 把异常传播当作恢复。 |

核对构建、公开接口、适用分层、概念不变量与运作原理、规则和应用场景。静态检查不证明运行行为。
