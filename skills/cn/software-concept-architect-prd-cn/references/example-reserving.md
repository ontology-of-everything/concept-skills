# 订位转录例：权威文件与追溯

展示 Reserving/Availability 已确认片段的落盘与追溯，非论文原文或完整预约产品。

## 已确认输入

- Reserving [U, S] 维护预约承诺；Availability [V] 提供时段。
- Reserving.reserve 成功返回 reservation；冲突返回 Conflict 且不改状态。
- Availability._find 返回该 venue 全部 offered 时段，空集合表示无候选。
- 用户选择单一 slot 后，Requesting/reserve 的具名输入为 user/slot，完成输出为 request；Requesting/respond 接受 request 加 reservation 或 error，完成输出为空。
  应用提供 UserId/VenueId/RequestId；Conflict 对应 Reserving 的错误类型。响应按同一 flow/request 及 user/slot 关联。

## 转录落点

| 模型内容 | 模块已存在 | 尚无模块 |
| --- | --- | --- |
| Reserving 的完整四节 | `reserving/CONCEPT.md` | `docs/prd/concepts/Reserving.md` |
| Availability 的完整四节 | `availability/CONCEPT.md` | `docs/prd/concepts/Availability.md` |
| 应用实例化与规则 | `syncs/SYNCS.md` | `docs/prd/SYNCS.md` |
| 用户需要、依赖、图及未决项 | `docs/prd/README.md` | 同左 |

四节从确认模型逐项转录；本例未提供的字段不得推断。CONCEPT.md 内仍使用局部类型参数，实际实例化只进入 SYNCS.md。

## syncs/SYNCS.md 片段

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

将“成功预约后可兑现承诺”的 principle 编为代表性验收场景，链接 reserve/grant 契约并保留到场等前提；grant 或到场契约缺失时标为待补充，不能声称验收已可执行。冲突且状态不变的边界场景追溯到 reserve 的错误 case。两者均源于模型，不发明新要求。

`_find` 的空集合不能转录成 `[error: E]`，多候选也不能变成预约全部。若上游尚未说明身份、并发、到场条件或取消入口，把这些保留为未决；只有用户确认后才更新对应规格及派生图。

核对：确认元素落点唯一，索引有效；同步图保留 accepted/rejected 合取输入，query 不画为完成事件。
