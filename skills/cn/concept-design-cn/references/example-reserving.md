# 订位例：多类型参数与组合边界

教学片段，按 [规格契约](spec-format.md) 改写，不是论文原文，也不是完整餐厅产品。未决留着，不能据此生成实现。

## 两个概念

```text
# concept Reserving [U, S]
## purpose
为用户保留未来使用某资源时段的承诺。
## state
reservations: set Reservation
user: Reservation -> U
slot: Reservation -> S
status: Reservation -> Status
Reservation 是本概念创建的身份；Status = booked | canceled | granted。
初态 reservations 为空；每项预约恰有一个 user、slot、status。
每个 S 最多对应一个 booked 预约；S 无字段假设。
## actions
reserve [user: U; slot: S] => [reservation: Reservation]
  requires slot 无 booked 预约
  ensures 原子创建 booked 预约并返回其身份，其他预约不变
reserve [user: U; slot: S] => [error: Conflict]
  requires slot 已有 booked 预约
  ensures 返回 Conflict（时段已占用），状态不变
cancel [reservation: Reservation] => []
  requires 预约为 booked
  ensures 仅将该预约改为 canceled
grant [reservation: Reservation] => []
  requires 预约为 booked；到场条件待定义
  ensures 仅将该预约改为 granted
## operational principle
after reserve [user: u; slot: s] => [reservation: r]
then 在预约未取消、满足到场条件时 grant [reservation: r] => []，兑现承诺。
```

论证缺口：grant 的到场输入/时间契约尚未定义；cancel/grant 在前置不满足时的调用处理未确定，不能补造错误输出。目的性：届时兑现预订承诺。独立：只用身份。熟悉：预约。端到端要等到场前提写明并检验兑现行为后才能判断。

```text
# concept Availability [V]
## purpose
让使用者找到指定场所当前提供的资源时段。
## state
slots: set Slot
venue: Slot -> V
offered: set Slot
Slot 是本概念创建的身份；初态 slots/offered 为空。
每个 Slot 恰属于一个 V；offered 是 slots 的子集。
## actions
publish [venue: V] => [slot: Slot]
  requires true
  ensures 创建新 Slot，关联 venue 并加入 offered，其他状态不变
withdraw [slot: Slot] => []
  requires slot 属于 slots
  ensures 从 offered 移除 slot，其他状态不变
## operational principle
after publish [venue: v] => [slot: s]
then s 在 offered 中且 venue(s)=v；withdraw [slot: s] => [] 后不再被可用时段查询返回。
## queries
_find [venue: V] => [slot: Slot]
  returns 该 venue 下全部 offered 时段，每项一行；无结果为空集合
```

`_find` 是可选的 query 映射，不产生完成事件；也可以直接读 venue 与 offered。Availability 不读取 Reserving。不存在的 Slot 如何处理仍未决。

## 应用目的与预约片段

应用目的：用户选定时段后，得到预约承诺或明确的冲突。到场兑现不在本片段。UserId 与 VenueId 由应用边界提供，不另建概念。入口契约：

```text
Requesting/reserve: [user: UserId; slot: Availability.Slot] => [request: RequestId]
Requesting/respond: [request: RequestId; reservation: Reserving.Reservation] => []
Requesting/respond: [request: RequestId; error: Conflict] => []
```

RequestId 标识这一次请求。Conflict 就是 Reserving 的 Conflict。每个请求只选一个 slot。这次请求的完成开启一个 flow，后面的调用沿用它。

```text
# app Reservations
include Availability [VenueId]
include Reserving [UserId, Availability.Slot]
include Requesting

// flow: reserve
sync reserve
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
}
then {
  Reserving/reserve: [user: ?user; slot: ?slot]
}

sync accepted
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [reservation: ?reservation]
}
then {
  Requesting/respond: [request: ?request; reservation: ?reservation]
}

sync rejected
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [error: ?error]
}
then {
  Requesting/respond: [request: ?request; error: ?error]
}
```

accepted 与 rejected 用输出字段区分结果，并且必须同时匹配同一次请求里的用户和时段。本例不等待 `_find`。空集不是 error，多个时段也不能展开成多次预约。查询到的 offered 在写入时可能已变，撤下与预约的竞态另定。

## 图、子集与未决

同步图：Requesting/reserve → reserve → Reserving/reserve。accepted 与 rejected 各有两个必须同时成立的 when，然后调用 Requesting/respond。查询标成读取，不是完成。

已知时段可以直接预约时，产品只需 Reserving。必须先发现时段时，写 Reserving → Availability。include 里的类型参数不是这条依赖的证据。

未决：认证、时段属于哪个场所、撤下与预约的竞态、预约如何显示、到场条件、取消和兑现的入口、故障后怎么处理。这三条规则只覆盖选定一个时段后的成功或冲突。
