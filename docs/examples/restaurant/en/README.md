# Restaurant reserve

One restaurant, one pair of guests, four structures. The source is Daniel Jackson, *Beyond Objects*, [arXiv:2606.27258](https://arxiv.org/abs/2606.27258), §5–13.

Alice reserves a slot. Bob asks for the same slot.

| Cut | Search after Alice | Bob |
| --- | --- | --- |
| Concept design | The slot stays listed | `Conflict` |
| Naive DDD, and the same objects split into crates | The search is empty | `NoSlot` |
| Modular DDD | The slot stays listed | `Conflict` |

Concept design returns `Conflict` from Reserving. That write inserts a reservation and leaves Availability as it was. Modular DDD returns `Conflict` from `BookingService`, which writes a guest, a slot occupancy, and a reservation in one service.

- [Comparison and the complexity counts](comparison.md)
- [Files to open](reading-path.md)

中文：[餐厅预约](../cn/README.md)。
