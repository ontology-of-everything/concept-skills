# CONCEPT 与 SYNCS 格式

本文件是按[来源](sources.md)改写的本地 Markdown 约定，不是引擎语法。

## CONCEPT

新文件 MUST 按以下顺序，每个核心节 MUST 有声明内容。
`coverage: complete|partial` 是声明覆盖范围的本地元数据，不是引擎语法。

```markdown
# concept Name [T]
coverage: partial

## purpose
<一个可评价的需要>

## state
items: set Item
owner: Item -> T
<局部类型、基数、初态、不变量>

## actions
act [item: Item; owner: T] => [item: Item]
  requires <成功条件>
  ensures <效果、输出、不变状态>
act [item: Item; owner: T] => [error: E]
  requires <拒绝条件>
  ensures <错误含义与状态后果>

## operational principle
after <已声明动作及结果>
then <兑现目的的后续动作或观察>
```

`requires` 是分支启用条件。
`ensures` 关联前后状态与输出。

- `A -> B` 本身不表示总函数或唯一性。
- 动作 MUST 具名声明输入输出，并说明每个分支的条件、效果与不变状态。
  无输入用 `[]`，无返回用 `=> []`。
- 某分支的 `requires` 不成立，本身不会产生完成记录或错误。
  无效请求须有已声明拒绝分支或入口策略。
- 不同效果 MUST 有可区分的分支或选择规则。
  成功不默认改状态，失败不默认保持状态。
  只读动作仍产生完成记录。
- 转移 MUST 原子保持不变量。
  影响行为的歧义须在相关实现前解决。

可选 `## queries` 将公开关系映射为查询 API：

```text
_owners [item: Item] => [owner: T]
  returns 匹配的 owner 绑定；无匹配为零行
```

声明签名、基数与对应关系。
查询 MUST 只读，不产生完成记录。
SYNCS 中的 `Name/_query: [输入] => [输出]` 只能用于 `where`。
不把空查询结果改成未声明错误。

按需在 `state` 附一条符合类型、基数与不变量的示例，注明粒度、身份、观察时点及对应关系。
可附注明确认状态的表或接口映射，分别引用状态约束或动作/查询契约；分析型事实表另需明确粒度、时间、适用的度量与历史来源。

## SYNCS

include MUST 指向概念或外部入口契约。
声明别名、具体类型及请求、定时、消息的根动作签名。

```text
# app AppName
include Source [Id]
include Target [Id]

sync Transfer
when { Source/finish: [] => [item: ?item] }
where { Source: { ?item owner: ?owner } }
then { Target/accept: [item: ?item; owner: ?owner] }
```

| 部分 | 约束 |
| --- | --- |
| `sync` | 一个决定对应一个稳定、应用内唯一的名称。 |
| `when` | 必需且非空。全部完成模式 MUST 在同一运行时 flow 中匹配。 |
| 模式 | 省略字段为通配，`[]` 不代表成功。分支影响后续效果时 MUST 区分。 |
| `where` | 可选。读取、过滤、计算、绑定行；省略时保留输入绑定。 |
| `then` | 必需且非空。MUST 逐行调用，填全所需具名输入，不写输出。 |
| `?name` | 同名同值；调用只用常量或已绑定值。 |

同一 `then` 的调用没有隐含顺序。
顺序通过后续结果建立。
`where` 读取求值时状态。
不默认存在快照、锁或后续状态变化时的重求值。
所需一致性 MUST 明确。

## 执行检查

- 调用请求执行，完成记录保存结果。
  发生记录身份关联两者，参数相同不代表同一次执行。
- flow 包含根发生记录及其因果后续。
  重复动作除业务或请求身份外，还须关联发生记录或因果。
  明确匹配全部记录还是某次尝试。
  `// flow:` 只作文档标签。
- 其他独立 flow 的旧完成记录 MUST NOT 满足 `when`。
  持久事实从 `where` 读取，延迟回调用入口与关联协议衔接。
- 错误与 `valid: false` 等值分别匹配。
  必要权限检查 MUST 先于受保护效果。
  事后拒绝不会撤销写入。
- 零行不调用，多行展开调用。
  声明所需零匹配响应与候选选择规则。
- 后续失败 MUST NOT 抹去已有完成记录。
  明确响应、重试、补偿或有意忽略及其效果。
- 核对发生记录组合与绑定行的触发身份和原子去重。
  重求值 MUST 保留合法重复，并防止禁止的重复。
- 无重启恢复要求时 MAY 只保留内存记录。
  需要恢复时 MUST 一致持久化发生记录、flow、规则及版本、因果、绑定与发出调用。
  外部效果另需幂等保障。

## 兼容

语法差异本身不是漂移。
兼容 `principle`、旧节顺序、`act (arg: T) : (result: R)`、`Concept.act (...) : (...)` 与动作内 `_` 查询。
局部修改 SHOULD 保留方言。
迁移 MUST 保留签名、结果分支、关联与未决。
省略的输出不能改成也匹配错误的 `=> []`。
区分事务同步与因果规则。
引用方和图须一并更新。

## concept-lint

```sh
python3 scripts/concept_lint.py CONCEPT.md SYNCS.md --json
```

CLI 仅用标准库，只读检查声明、coverage、核心节唯一性与非空、规则块及其内部括号。
对已闭合的 `when`/`then` 块，检查动作输入记录、`when` 的完成输出，以及 `then` 不含输出。
输入输出记录的顶层字段必须具名、有值，且在同一记录内不重名。
本次输入中同名 `# app Name` 的文件按同一应用检查规则名唯一性；不同应用允许重名。
结构匹配排除注释、字符串内容和围栏说明，保留诊断行号。
未知调用记法返回 `not_checked`，包含套在花括号内的旧点式调用。
嵌套记录值与 `where` 表达式不解析；不解析 include 指向、动作签名、类型或变量绑定。
概念独立性、目的、契约符合性与运行行为须由代码审查、架构检查或执行证据验证。

| 退出码 | 状态 | 含义 |
| --- | --- | --- |
| 0 | `format_checked` | 全部输入通过所列结构检查。 |
| 1 | `format_error` | 至少一个已确定的结构错误。 |
| 2 | `read_error` | 用法、文件访问或编码错误。 |
| 3 | `not_checked` | 旧方言、未知或未闭合记法，或缺 coverage。 |

读取错误优先于格式错误；格式错误优先于未检查部分。
未闭合注释、字符串或围栏遮住的内容，不推断为缺失章节。
已完整闭合的节或块存在错误时仍报错。
有意不含状态或动作时，明确写出该声明，不留空节。
`format_checked` 不表示语义验证。
