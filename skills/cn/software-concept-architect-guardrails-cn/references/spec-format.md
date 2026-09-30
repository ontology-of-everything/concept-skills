# 概念与同步规格契约

编写、转录、实现或核对 CONCEPT/SYNCS 时读。格式改写自 [WYSIWID v1 §4–6](https://arxiv.org/html/2508.14511v1#S4)，不是引擎语法。

## 同步原则

同步可以排除概念的部分行为，不能让它做出自身规格不允许的行为。逐个概念看动作、状态变化和输出的序列，不能只对动作名。限制写在 SYNCS；前置条件、不变量、效果和输出 case 仍由概念自己的契约决定。要超出契约，先改并确认概念规格。

收窄行为不算违约。还要看剩下的场景能否兑现 purpose：合法组合也可能使目的落空。

## CONCEPT：独立的行为接口

新写按 purpose → state → actions → operational principle 排列。概念名和类型参数在标题。requires/ensures、notes、queries 是本仓写法。占位只示意字段；未确认的标未决。

```markdown
# concept Name [T]

## purpose
<一个可评价的需要>

## state
items: set Item
owner: Item -> T
<声明 Item 为本概念的身份类型；说明关系的基数、初态及必要不变量>

## actions
act [item: Item; owner: T] => [item: Item]
  requires <该成功 case 的适用条件>
  ensures <状态变化、输出值与未改变部分>
act [item: Item; owner: T] => [error: E]
  requires <该错误 case 的适用条件；声明 E 的含义>
  ensures <错误值及状态后果>

## operational principle
after <条件及已声明动作的输入 => 输出>
then <后续动作/观察及可观察结果；如何兑现 purpose>
```

| 要素 | 核对标准 |
| --- | --- |
| 名称/类型 | 外部身份是无字段的类型参数。局部类型有定义。具体类型只在 SYNCS 实例化 |
| purpose | 一个需要，不是功能清单 |
| state | 写明基数、初态、不变量。`A -> B` 只表示类型之间有关联，不表示总函数或唯一 |
| actions | 输入输出具名。无参数写 `[]`，无返回值写 `=> []`。每个 case 写条件、效果和输出 |
| OP | 用真实动作名演示如何兑现 purpose，不穷举行为 |

同一动作可以有多个 case。字段名参与匹配。成功与拒绝的条件必须分得开；重叠且效果不同时，写明选择规则或标未决。失败不默认保持状态，成功也不默认改状态。只读动作，例如校验凭据，仍然产生 completion。

可以省略与当前设计无关的细节。影响同步的签名、分支和状态含义必须写明。实现前补齐会改变可观察行为的歧义。不为填模板而发明错误、权限或功能。

## 状态读取与可选 query 接口

概念拥有自己的状态。应用可以查询它公开的抽象状态，包括跨概念 join。物理表、私有存储和其他概念的内部实现不因此开放。概念之间不互相读取或调用。

where 默认读已声明的关系。项目要用 query API 时，在可选的 `## queries` 写 `_` 查询：具名参数、结果、零/一/多行，以及对应哪段抽象状态。查询只读，不产生 completion。这不是第五个核心节，也不为每个字段造 getter。

```text
_owners [item: Item] => [owner: T]
  returns owner 关系中匹配 item 的绑定；无匹配为零行
```

where 可写 `Name/_owners: [item: ?item] => [owner: ?owner]`。这是 query 扩展，不能放入 when 或 then。初态、基数或查询能力不明就留缺口。空集不是未声明的 error。

## SYNCS：应用的因果规则

`app`、`include`、类型实例化和 `// flow:` 是本仓的外层组织。`sync/when/where/then` 用论文的记录模式。每个 include 指向一份找得到的概念规格，或一份写明的外部入口契约。别名和实际类型要有定义。Web 只是入口例子。已有的 Requesting 可以保留名称，但要写明签名。定时和消息同样声明自己的根事件。

```text
# app AppName
include Source [Id]
include Target [Id]
include Web

// flow: transfer
sync Transfer
when {
  Web/request: [method: "transfer"] => [request: ?request]
  Source/finish: [] => [item: ?item]
}
where {
  Source: { ?item owner: ?owner }
}
then {
  Target/accept: [item: ?item; owner: ?owner]
}
```

上面是语法槽位，不是一个已定义的产品。item、Source.owner 和目标输入都要对照真实规格。要不要响应，由入口契约决定。

| 部分 | 精确语义 |
| --- | --- |
| sync | 应用内唯一且稳定的规则名，对应一条说得清的设计决策 |
| when | 必填。匹配动作的完成：`Concept/action: [输入] => [输出]`。多个模式必须同时成立，且属于同一个运行时 flow |
| 部分匹配 | 只约束写出的字段，没写的字段是通配。`[]` 是空模式，不是成功。动作可能返回 error 时，成功路径要匹配成功字段或其他已证实的判别条件 |
| where | 可省略。用 when 的绑定去读抽象状态、过滤或计算，得到零组、一组或多组绑定。省略时沿用原来的绑定 |
| then | 必填。每一组绑定发出所列调用，只有具名输入，不写 `=>`。参数按真实签名填全；when 里可以省略的字段，在 then 里不能漏 |
| 变量 | `?name` 在整条规则里同名同值。then 只用常量，或 when/where 已经绑定的变量。同一次 then 里的调用没有隐含先后。以后的输出用下一条 sync 的 when 来匹配 |

### 失败、关联与执行

- `=> [error: ?error]` 匹配已声明的错误。`=> [valid: false]` 是普通的否定结果。两者不要混用。授权或校验要先得到允许，再发写动作。事后拒绝不会撤销已经完成的写入。
- where 零行就是不调用。多行展开成多组调用。需要响应的入口要写明零行时怎么办。多个候选不默认取第一个，也不默认全部执行。重复投递是否幂等，另写契约。
- 一个 flow 对应一个根事件。同一 flow 里有多个同类动作时，用业务 ID 配对，不能只靠 flow token。`request` 用来找到响应。`// flow:` 只给规则分组，不是运行时 token。
- 后面的失败抹不掉已经完成的事件。部分完成后要写明响应、重试、补偿，或有意不再处理。动作自己维护不变量。where 读到的状态不能代替写入时的原子检查。
- 记录动作身份、flow、触发规则、因果来源，以及发出的调用，避免重放时再次发出。去重键按引擎语义核验。这不保证外部副作用恰好一次。

## 旧规格兼容与交付核对

读到 `principle`、旧的四节顺序、`act (arg: T) : (result: R)`、`Concept.act (...) : (...)`，以及写在 actions 里的 `_` 查询，语法本身不算漂移。新写用本契约。局部修改保留原来的方言。整份迁移要经用户授权，并改到所有引用它的文档和图。

迁移前先找回旧规则的输入、输出、成功/错误判别和隐含关联。旧 when 省略了输出时，不要改成 `=> []`，否则会把错误也匹配进去。wyx 边界段和旧书版事务同步单独辨认，保留原来的行为和未决，不要按字符替换。

交付时按这个顺序核对：类型实例化 → 状态或查询 → 动作的输入和相关结果 → when 的 case → where 的行数 → then 的参数 → 入口的结果和关联。OP 与应用场景分开追溯。跨概念的策略只写在 SYNCS。目的、依赖、排除和未决留在总体 PRD。实现时再查并发、故障恢复和可观察行为。
