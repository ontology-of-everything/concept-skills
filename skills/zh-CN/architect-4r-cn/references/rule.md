# Rule 的协作规则图

画图时应用[共享图示设计](diagram-design.md)中的明暗主题。

Rule 说明角色按什么条件和顺序协作，怎样改变状态、处理异常。按所表达的问题选择时序图、条件流程图或状态图，一个 R 可以使用多张图。

| 图法 | 主要表达 |
|---|---|
| 业务场景时序图 | 谁先与谁交互，消息如何返回、重试或并发。 |
| 条件流程图 | 什么条件决定下一步，分支和循环何时结束。 |
| 状态图 | 某个角色持有的对象可以处于什么状态，什么事件允许迁移。 |

## 业务场景时序图

本例从渠道结果回调开始。支付服务验签，并核对支付归属、金额与币种。终态与唯一投递任务同事务提交后才确认回调。商家按 eventId 原子去重并更新订单，通知超时继续使用同一 eventId 重投。

```mermaid
sequenceDiagram
    autonumber
    participant Channel as 外部支付渠道
    participant Pay as 支付服务
    participant PayDB as 支付库
    participant Order as 商家订单系统
    Channel-)Pay: 回调 paymentId 与支付结果
    Pay->>Pay: 验签并核对归属、金额、币种
    Pay->>Pay: 检查已有终态约束
    alt 校验通过且终态相容
        Pay->>PayDB: 同事务：条件更新终态与唯一投递任务
        PayDB-->>Pay: 已提交或该结果已处理
        Pay-->>Channel: 持久化后确认接收
        loop 任务未完成且仍在有界投递窗口内
            Pay-)Order: 终态通知 eventId
            Order->>Order: 原子去重 eventId 并更新订单
            alt 收到接收确认
                Order-->>Pay: 确认已处理
                Pay->>PayDB: 记录投递成功
            else 通知超时或失败
                Pay->>PayDB: 保存下次重试计划
            end
        end
    else 校验失败或结果冲突
        Pay-->>Channel: 拒绝结果并记录原因
    end
```

## 条件流程图

支付服务执行此结果确认流程。渠道查询需有执行方、退避和查询窗口。窗口耗尽后保留待确认，并转入对账或人工核实。

```mermaid
flowchart TB
    Start(["确认支付结果"]) --> Trusted{"已取得可信终态？"}
    Trusted -->|"是"| Apply["条件更新终态<br/>并原子写入投递任务"]
    Apply --> Done(["进入结果投递"])
    Trusted -->|"否"| Window{"查询窗口仍有效？"}
    Window -->|"是"| Query["按 paymentId 查询渠道"]
    Query --> Trusted
    Window -->|"否"| Pending["保留待确认<br/>转对账或人工核实"]
    Pending --> Stop(["暂停自动查询"])
    class Apply,Query service
    class Pending worker
```

## 状态图

这些状态由支付服务持有。图中的迁移标签说明触发条件，重复终态只产生一次有效变更。冲突结果进入核查，已确认终态保持不变。通知进度另行记录，投递失败不修改支付终态。

```mermaid
stateDiagram-v2
    direction LR
    state "待确认" as Pending
    state "成功" as Succeeded
    state "失败" as Failed
    [*] --> Pending: 已受理并持久化
    Pending --> Pending: 超时或结果仍未知
    Pending --> Succeeded: 核实成功
    Pending --> Failed: 核实失败
    Succeeded --> Succeeded: 重复成功结果
    Failed --> Failed: 重复失败结果
    note right of Pending
        支付服务持有这些状态
        通知进度另行记录
    end note
```

## 检查

- 场景的触发条件、参与者、结束条件是否明确？参与者能否对应 Role？
- 分支、循环、状态迁移是否写明条件？失败处理是否有负责角色？
- 超时是否保留未知结果？重试是否说明执行方、边界和耗尽后的处理？
- 状态更新、原子提交、重复与乱序处理是否清楚？图下是否补足幂等、校验和不可倒退等约束？
