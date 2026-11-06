# Phase 3：仓库 YAML 与共享字段语义

仓库 YAML 是本地语义配置，不是通用本体标准。用户提供项目 schema 时沿用并记录版本；
否则可使用下面的紧凑记录结构：

```yaml
name: Sales
schema_version: "1"
type: semantic_ontology
facts:
  - name: Order
    grain: one confirmed order at creation
    source_operations: [ListOrders]
    identity: {key: order_id, scope: tenant}
    time: {field: placed_at, meaning: creation, timezone: UTC}
    dimensions: [Store]
    measures:
      - name: order_amount
        source_field: amount
        unit: USD
        basis: gross order amount before refunds
        additivity: additive
        aggregation_scope: unique orders in one currency
    evidence: [contract-v1#ListOrders, business-definitions#order]
evidence_boundary: [No refund or recognized-revenue inference]
```

这是示意的已批准输入，不是其他来源存在这些字段的证据。

每 bundle 一个 `semantic_catalog`：名称、目的、证据边界、所需上下文，以及将支持的问题映射到
模型文件和来源操作的 `entry_points`。目录链接模型，不重复定义。两个以上 bundle 可有薄父索引。

事实声明来源操作、业务粒度、身份/范围、时间含义、维度、度量和证据。
`primary|child` 与父引用是可选的本地组织方式，不是必需语义种类。
不同粒度先聚合再连接，或明确有证据的分摊；一对多连接不能重复计入头级度量。

维度声明名称、带范围的键、属性、来源、连接基数，以及必要的历史解释。
本地维度用 `dimension`，跨事实含义一致的复用用 `conformed_dimension`，
有父关系和基数的规范化层级用 `snowflake_dimension`；退化键留在事实。
字段同名不能证明一致性：比较业务含义、键域、租户、时间/版本和属性。

度量是声明事实粒度上的数量，需声明来源或计算、单位、相关币种/口径、分轴可加性与聚合范围。
指标是基于度量的具名业务计算；在可选 `metrics` 清单记录公式、来源度量、筛选、时间/窗口与
聚合范围，和事实内的 `measures` 清单区分。
计数需去重身份；比率和均值需有效组成量；快照通常不能跨时间相加。
空值、空集、修订与删除会影响回答时须说明，缺失含义保留为未决。

来源字段映射留在模型，引用可执行枚举/取值/命令目录，避免复制。
每项选择追溯到证据与已批准决定或明确范围排除；这些语义同样适用于 OKF。
