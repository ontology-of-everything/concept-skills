# 工程架构

确定或核对工程结构时读取；原则见 [技能正文](../SKILL.md)，构建配置只读目标语言参考。

## 构建与运行边界

```text
apps/server/                     # 唯一启动应用，配置与装配
modules/
  concepts/<组>/<概念>/           # 每个叶目录一个构建单元
    CONCEPT.md
    src/                         # 公开 API + domain/application/adapter
  syncs/                         # 独立构建单元，公开应用接口
    SYNCS.md                     # 按 flow 分组的具名规则
    src/                         # 规则实现；执行端口/适配器按需
  gateway/                       # 独立构建单元，协议/DTO/错误映射
  shared/                        # 独立构建单元，被动基础类型
```

组和 flow 是导航，不自动成为模块。独立构建会构建声明的依赖闭包；模块最终装配到同一进程，单独构建不意味着单独启动或部署。单模块任务只交付所需范围，不补齐无关骨架。

| 模块 | 业务依赖 | 公开面 |
| --- | --- | --- |
| concept | shared（按需） | 动作、查询、结果类型、必要完成事件 |
| syncs | concept 公开接口、shared | 应用动作与结果；公开签名使用 syncs/shared 类型 |
| gateway | syncs 公开接口、shared | 对外协议；对 server 提供路由/配置入口 |
| shared | 无业务模块 | 身份、时间等被动基础类型 |
| server | 各模块公开装配入口 | 启动应用；装配多模块不是业务协调 |

公开面分业务接口和装配接口；syncs 只使用概念业务接口。每个概念封装自己的存储，可共享数据库设施，但读写仍经所属概念。迁移标明状态所有者。

## 模块内依赖

- `domain`：模型、不变量与纯规则；存储端口由需要它的内层声明。
- `application`：实现公开动作/查询，调用领域逻辑与端口，处理用例事务边界。
- `adapter`：实现端口，接入数据库或外部设施；技术细节依赖内层契约。
- 装配入口：构造具体实现并返回公开接口；内部实现保持隐藏。

syncs 的应用层承载具名规则，需要恢复时增加执行端口与适配器；业务状态留在概念。gateway 本身承担入站适配，不为目录对称添加领域层。Rust 的 crate 内模块、Java 的包、TypeScript 的目录承载层次，默认不每层再拆构建单元。

## 一条请求的正常与失败路径

例：已确认 Reservation 可产生 Held、Confirmed、Cancelled，Payment 可产生 Paid、Declined；拒付后必须最终释放预约。以下是因果路径，具体字段与 case 以规格为准。

```text
gateway：HTTP 请求 → syncs.reserve（建立请求/flow 关联）
syncs：请求完成 → Reservation.hold
syncs：hold[Held] → Payment.charge
syncs：charge[Paid] → Reservation.confirm
syncs：confirm[Confirmed] → 响应成功
syncs：charge[Declined] → Reservation.cancel
syncs：cancel[Cancelled] → 响应拒付
gateway：应用结果 → HTTP 响应
```

每条边是具名规则，后续调用由前一动作完成结果绑定；flow 与预约身份贯穿匹配。若取消暂时失败，已完成的 hold/charge 仍成立：持久记录待恢复执行，按确认的入口契约响应，重试取消并避免重复扣款。重试耗尽须可观察，不能提前声称已释放；补偿也不自动抹去历史。普通连续调用必须实现同样的关联、分支和恢复语义。

## 关键正反例

| 正例 | 反例与后果 |
| --- | --- |
| 模块有自己的构建清单、接口与测试入口 | 仅分文件夹却宣称独立编译，无法验证构建边界 |
| gateway → syncs → concept API | Controller 编排概念或概念互调，应用策略散落 |
| 内层声明端口，adapter 实现 | domain 导入 HTTP/SQL 实现，领域规则绑定设施 |
| server 使用受限公开工厂/配置 | 为装配公开所有内部包，业务调用可绕过边界 |
| 具名规则匹配输出 case 和关联 | 连续 `?`/异常冒泡代替失败策略，留下未处理状态 |
| 同时检查构建图和源码/API 边界 | 只检查无环，漏掉合法编译却违规的概念依赖 |

验证分别覆盖模块构建、公开面/层次、概念 OP 与不变量、同步分支及整条请求的失败恢复；静态边界通过不能证明行为正确。
