# 餐厅预约

同一家餐厅，同一对客人，四套结构。出处是 Daniel Jackson，*Beyond Objects*，[arXiv:2606.27258](https://arxiv.org/abs/2606.27258)，§5–13。

Alice 订下一个时段。Bob 再订同一个时段。

| 切法 | Alice 订完再搜索 | Bob |
| --- | --- | --- |
| 概念设计 | 该时段仍列出 | `Conflict` |
| 朴素 DDD，以及同一套对象拆进多个 crate | 搜索为空 | `NoSlot` |
| 模块化 DDD | 该时段仍列出 | `Conflict` |

概念设计的 `Conflict` 来自 Reserving。这次写入只插入一条预约，Availability 保持原样。模块化 DDD 的 `Conflict` 来自 `BookingService`：一次服务里写入客人、时段占用和预约。

- [对照与复杂性计数](comparison.md)
- [建议打开的文件](reading-path.md)
