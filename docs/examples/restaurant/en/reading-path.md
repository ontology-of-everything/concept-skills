# Files to open

Read in this order. The trees sit beside each other as `concept/`, `ddd-clean/`, `oop-packages/`, and `ddd-modular/`.

1. `concept/syncs/src/lib.rs`, `RestaurantSyncs::reserve`. It asks Authenticating, Karma, and Availability, then calls Reserving.
2. `concept/concepts/reserving/src/actions.rs`, `Reserving::reserve`. The success path inserts one reservation.
3. `ddd-clean/src/domain/booking.rs`, `BookingService::reserve`. One function updates the user, the slot, and the reservation.
4. `oop-packages/booking/src/lib.rs`. The same function, with those types imported from other crates.
5. `oop-packages/reservation/Cargo.toml`. The reservation crate depends on the user and restaurant crates.
6. `ddd-modular/app/src/orchestration.rs`, `reserve`. The call order looks like syncs.
7. `ddd-modular/booking/src/booking_service.rs`. The write is Guest, slot occupancy, and Reservation.

The behavior those files produce is the table in the [comparison](comparison.md).
