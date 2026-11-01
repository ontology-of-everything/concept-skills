# 订位转录例

转录以下确认片段，不视为完整产品，也不补造缺失字段。

## 确认输入与位置

Reserving 维护时段承诺，Availability 提供时段。reserve 成功返回 reservation，冲突返回 Conflict 且不改状态。
_find 返回场所全部 offered 时段，空集表示没有候选。

用户选一个时段。Requesting/reserve 输入 user/slot、输出 request；respond 输入 request 加 reservation 或 error，输出为空。
应用提供 UserId、VenueId、RequestId，Conflict 对应 Reserving 错误。按 flow/request 和 user/slot 关联响应。

| 内容 | 模块已建 | 模块未建 |
| --- | --- | --- |
| 概念四节 | 模块的 CONCEPT.md | docs/prd/concepts/ |
| 实例与规则 | composition/SYNCS.md | docs/prd/SYNCS.md |
| 需要、依赖、图与未决 | docs/prd/README.md | 同左 |

局部类型参数留在 CONCEPT，实际类型实例化归 SYNCS。

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

## 验收与缺口

预约承诺验收关联 reserve/grant，保留到场前提。缺 grant 或到场契约时，验收仍不完整。
冲突且状态不变关联 reserve 的错误分支。

不把 _find 空集转成未声明错误，也不将多候选转成全部预约。身份、并发、到场和取消缺口须保留到确认。
核对唯一文件归属、有效索引、accepted/rejected 的合取输入，并将查询读取与完成事件分开。
