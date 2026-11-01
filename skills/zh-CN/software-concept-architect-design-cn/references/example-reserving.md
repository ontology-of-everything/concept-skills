# 订位设计例

本教学片段按[规格契约](spec-format.md)编写，不是完整产品。未决行为须先定义，再实现相关部分。

## 独立概念

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

grant 的到场输入/时间，以及 cancel/grant 前置不满足时的处理仍未决，不补造错误。
目的能否兑现取决于到场行为的定义与检查。

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

查询读取 venue/offered，不产生完成事件，Availability 不读 Reserving。未知 Slot 的处理仍未决。

## 应用场景

用户选定一个时段后得到预约或冲突，到场不在本片段。应用提供 UserId、VenueId、RequestId：

```text
Requesting/reserve: [user: UserId; slot: Availability.Slot] => [request: RequestId]
Requesting/respond: [request: RequestId; reservation: Reserving.Reservation] => []
Requesting/respond: [request: RequestId; error: Conflict] => []
```

RequestId 标识本次请求，Conflict 是 Reserving 的已声明错误。请求完成开启一个 flow，后续调用沿用。

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

accepted/rejected 按输出字段判别，并匹配同请求的用户与时段，不等待 _find。
空查询不是错误，多候选不表示全部预约。offered 可能在写入前变化，撤下与预约的并发仍未决。

## 图与子集

reserve 连接请求完成与 Reserving.reserve，accepted/rejected 各须两个完成共同匹配后响应。查询读取与触发分开画。

已知时段身份可直接预约时，产品可能只需 Reserving；必须发现时段时才有对 Availability 的产品依赖，类型实例化本身不是依据。

认证、场所检查、并发撤下、显示、到场、取消入口与故障处理均未决。规则只覆盖选定时段后的成功或冲突。
