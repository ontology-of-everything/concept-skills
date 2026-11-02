# 完整概念与局部组合

以下为教学选择，不是其他产品的需求。
采用[规格格式](spec-format.md)。

## 完整待办

本地可信调用者用它记住未完成工作。
Text 是任意字符串，允许空文本。
Task 身份新鲜生成且不复用。
删除、排序、授权和持久化不在本例范围。

```text
# concept Todo
coverage: complete
## purpose
记住未完成工作，并区分已完成工作。
## state
tasks: set Task
text: Task -> Text
done: set Task
Task 是局部身份；Text 是字符串。
初始 tasks 与 done 为空。
text 定义域恰为 tasks，每任务恰有一个 Text；done 是 tasks 的子集。
Missing 是表示未知任务的单例错误。
## actions
add [text: Text] => [task: Task]
  requires true
  ensures 创建并返回一个新鲜 t；tasks = 旧 tasks union {t}；
          text = 旧 text 加 (t, 输入 text)；done 不变
complete [task: Task] => []
  requires task 属于 tasks
  ensures done = 旧 done union {task}；其余状态不变
complete [task: Task] => [error: Missing]
  requires task 不属于 tasks
  ensures 返回 Missing；状态不变
reopen [task: Task] => []
  requires task 属于 tasks
  ensures done = 旧 done minus {task}；其余状态不变
reopen [task: Task] => [error: Missing]
  requires task 不属于 tasks
  ensures 返回 Missing；状态不变
## operational principle
after add [text: "报告"] => [task: t]，待办包含 t；
then complete [task: t] => [] 后待办不含 t；
then reopen [task: t] => [] 后恢复同一 t 与文本。
## queries
_pending [] => [task: Task; text: Text]
  恰返回 tasks minus done，每任务一行并附文本；
  空状态返回零行；无顺序；不产生完成记录
```

| 从全新状态验收 | 可观察结果 |
| --- | --- |
| add("报告") 后 _pending | 恰含返回的任务与输入文本。 |
| add 得到 t；complete(t) 后 reopen(t)，每次均查询 | t 先消失，再以原文本出现。 |
| complete(t) 两次，再 reopen(t) 两次 | 重复调用成功，不增加重复任务或其他变化。 |
| complete(unknown) 或 reopen(unknown) | Missing，状态不变。 |
| add 前 _pending | 零行，无错误。 |

以上为规定的检查，不是实测结果。
complete 时删除文本会破坏重新打开，即使只测 complete 的用例通过。
界面、外部入口与持久化行为另需契约。
Todo 只需一份 CONCEPT，无需 SYNCS。

## 局部订位模型

本片段仅覆盖选定时段的成功或冲突。

```text
# concept Reserving [U, S]
coverage: partial
## purpose
为用户保留未来使用资源时段的承诺。
## state
reservations: set Reservation
user: Reservation -> U
slot: Reservation -> S
status: Reservation -> Status
Reservation 是局部身份；Status = booked | canceled | granted。
Conflict 是表示时段已有 booked 预约的单例错误。
初始 reservations 为空。
每项预约恰有一个 user、slot 和 status。
每个 S 最多有一个 booked 预约；不假定 S 的字段。
示例（仅说明）：从空状态 reserve [user: u1; slot: s1] => [reservation: r1] 后，一条当前预约记录为 { reservation: r1, user: u1, slot: s1, status: booked }，以 reservation 为身份，其余字段对应同名关系。
## actions
reserve [user: U; slot: S] => [reservation: Reservation]
  requires slot 无 booked 预约
  ensures 原子创建并返回新鲜 r，设为输入 user/slot 和 booked；
          r 加入 reservations；已有事实不变
reserve [user: U; slot: S] => [error: Conflict]
  requires slot 有 booked 预约
  ensures 返回 Conflict；状态不变
cancel [reservation: Reservation] => []
  requires 预约为 booked
  ensures 仅将状态改为 canceled
grant [reservation: Reservation] => []
  requires 预约为 booked；到场条件未决
  ensures 仅将状态改为 granted
## operational principle
after reserve [user: u; slot: s] => [reservation: r]，
then 未取消且满足到场条件时 grant [reservation: r] => []，兑现承诺。
```

Availability[V] 独立提供场所当前可选时段。
所需接口片段声明局部 Slot 身份、每时段恰一个场所的 `venue: Slot -> V`，
以及现有时段子集 `offered: set Slot`。
查询 `_find [venue: V] => [slot: Slot]` 返回全部匹配 offered 时段，每项一行。
无匹配返回零行，不产生完成记录。
Availability 不读 Reserving。

应用入口契约：

```text
Requesting/reserve: [user: UserId; slot: Availability.Slot] => [request: RequestId]
Requesting/respond: [request: RequestId; reservation: Reserving.Reservation] => []
Requesting/respond: [request: RequestId; error: Conflict] => []
```

每个请求开启一个运行时 flow，响应沿用其 RequestId。

```text
# app Reservations
include Availability [VenueId]
include Reserving [UserId, Availability.Slot]
include Requesting

// flow: reserve
sync reserve
when { Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request] }
then { Reserving/reserve: [user: ?user; slot: ?slot] }

sync accepted
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [reservation: ?reservation]
}
then { Requesting/respond: [request: ?request; reservation: ?reservation] }

sync rejected
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [error: ?error]
}
then { Requesting/respond: [request: ?request; error: ?error] }
```

响应规则须在同一 flow 匹配两个完成记录，并关联相同 user/slot。
输出字段区分成功与错误。
本片段每请求 flow 只有一次预约尝试。
重复尝试还须按发生记录关联。
规则不等待 _find；查询是读取，不是完成记录。
多候选不授权全部预约。

已知时段产品可能只需 Reserving。
发现时段的需求才支持纳入 Availability，类型绑定本身不够。
移除它须将 S 改绑为独立提供的 SlotId 并更新入口/规则。
悬空 Availability.Slot 不构成可用子集。

到场输入/时限、cancel/grant 前置不满足、认证、场所检查、并发撤下、
显示、取消入口和故障处理仍未决。
offered 可在 reserve 前变化，不能代替写入时检查不变量。
到场与 grant 未定义及检查前，目的达成仍有缺口。
