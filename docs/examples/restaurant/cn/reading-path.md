# 建议打开的文件

按这个顺序读。四套树并排放着：`concept/`、`ddd-clean/`、`oop-packages/`、`ddd-modular/`。

1. `concept/syncs/src/lib.rs` 里的 `RestaurantSyncs::reserve`。它先问 Authenticating、Karma、Availability，再调用 Reserving。
2. `concept/concepts/reserving/src/actions.rs` 里的 `Reserving::reserve`。成功路径插入一条预约。
3. `ddd-clean/src/domain/booking.rs` 里的 `BookingService::reserve`。一个函数改用户、时段和预约。
4. `oop-packages/booking/src/lib.rs`。同一个函数，这三个类型从别的 crate 引进来。
5. `oop-packages/reservation/Cargo.toml`。预约 crate 依赖用户 crate 和餐厅 crate。
6. `ddd-modular/app/src/orchestration.rs` 里的 `reserve`。调用顺序看起来像 syncs。
7. `ddd-modular/booking/src/booking_service.rs`。写入的是客人、时段占用和 Reservation。

这些文件跑出来的行为见[对照](comparison.md)里的表。
