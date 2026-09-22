# Comparison

Same scenario as the [overview](README.md). The Rust trees are `concept/`, `ddd-clean/`, `oop-packages/`, and `ddd-modular/`.

| | Concept design | Naive DDD | Modular DDD |
| --- | --- | --- | --- |
| Modules | Authenticating, Availability, Reserving, Karma, plus syncs | User, Restaurant, Reservation, plus `BookingService` | Identity, Availability, Booking, Reputation, plus orchestration |
| Who commits a reserve | `Reserving::reserve` inserts one reservation | `BookingService::reserve` updates the user, marks the slot reserved, and builds a reservation | `BookingService::reserve` updates the guest, occupies the slot, and builds a reservation |
| Database | One SQLite file per concept, no cross-concept foreign key | One SQLite file, foreign keys between the tables | One SQLite file per bounded context |
| After Alice | Availability still lists the slot | `Slot.reserved` hides it | Availability still lists the slot; occupancy lives in Booking |
| Bob | `Conflict` | `NoSlot` | `Conflict` |

`oop-packages/` is the naive model with one crate per noun. `reservation` depends on `user` and `restaurant`. The search still goes empty, and Bob still gets `NoSlot`.

## Complexity metrics

These are the measures with a published definition that apply to a module cut. Each one was checked on these four trees, or marked as not run.

| Metric | Definition | What the check showed |
| --- | --- | --- |
| Cyclomatic complexity | McCabe, 1976. Independent paths through a function. | [lizard](https://github.com/terryyin/lizard) 1.24.0. Domain functions stay at or below 10. The CLI command loop is the outlier, at 31 or 33, in every tree. Plotted: no. |
| Efferent coupling, Ce | Martin, 1994. Modules this module depends on. | Peer edges among behavior modules: concept 0, naive DDD 3, split packages 5, modular DDD 0. Black bars below. |
| Cumulative component dependency | Lakos, 1996. For each component, count itself plus every component it depends on, directly or indirectly; sum those counts. | With the composer included and the shared kernel excluded, concept and modular DDD are the same star: CCD 9 over 5 components. Split packages: CCD 9 over 4. Naive DDD, composer excluded: CCD 7 over 4. Plotted: no. The star and the object graph land on the same CCD. |
| Coupling between objects | Chidamber and Kemerer, 1994. Classes a class uses. | Not plotted as CBO. The red bars count a narrower set: domain structs the reserve success path writes. |
| Information flow | Henry and Kafura, 1981. Length × (fan-in × fan-out)². | Not used. Fan-out would mix queries and writes. |
| Cognitive complexity | Sonar's increment for nested control flow. | Not run. No Sonar scan of these trees. |
| Halstead volume | Operators and operands. | Not run. |
| Lines of code | Size. tokei, Rust code column. | Concept 1473, naive DDD 1096, split packages 1088, modular DDD 1564. Size, not complexity. |

![Two counts for one reserve. Peer dependencies: concept 0, naive DDD 3, split packages 5, modular DDD 0. State holders written: concept 1, naive DDD 3, split packages 3, modular DDD 3.](../reserve-complexity.png)

### How the two bars were counted

**Peer dependencies** (black). A behavior module is a crate that owns domain state or the booking service. In the single-crate tree it is a file under `domain/`. An edge is a `use` of another behavior module. The shared kernel, identifier types, SQLite adapters, and the composer are excluded. The composer is `syncs`, modular orchestration, and the naive application service: each one is supposed to call the modules it composes.

| Tree | Edges |
| --- | --- |
| Concept | None among Authenticating, Availability, Reserving, Karma. `syncs` depends on all four, and that star is the composer, so it is not in the black bar. |
| Naive DDD | `domain/booking.rs` uses `user`, `restaurant`, and `reservation`. Those three do not use each other. |
| Split packages | `booking` uses `user`, `restaurant`, and `reservation`. `reservation` uses `user` and `restaurant`. |
| Modular DDD | None among Identity, Availability, Booking, and Reputation. Orchestration depends on all four and is excluded, same rule as `syncs`. |

**State holders written** (red). On the success path of reserve, count the domain structs whose fields change, plus a reservation inserted by that path.

| Tree | Success path | Count |
| --- | --- | --- |
| Concept | `Reserving::reserve` inserts a `Reservation`. `RestaurantSyncs::reserve` reads the other three concepts and writes only through that call. | 1 |
| Naive DDD | `BookingService::reserve` calls `User.note_booked`, sets `Slot.reserved`, and constructs a `Reservation`. The application service saves all three. | 3 |
| Split packages | The same function, with the three structs in separate crates. | 3 |
| Modular DDD | `BookingService::reserve` calls `Guest.note_booked` and `SlotOccupancy.occupy`, and constructs a `Reservation`. The booking facade saves all three. Orchestration does not write Availability or Reputation on this path. | 3 |

Cyclomatic complexity, read with lizard 1.24.0, excluding `target/` and `main.rs`:

| Tree | Functions | Mean CCN | Highest domain CCN | CLI `run` |
| --- | --- | --- | --- | --- |
| Concept | 79 | 1.84 | 9, an Availability SQLite read | 33 |
| Naive DDD | 51 | 2.45 | 10, `get_restaurant` | 31 |
| Split packages | 50 | 2.58 | 10, `get_restaurant` | 31 |
| Modular DDD | 88 | 1.90 | 9, an Availability SQLite read | 33 |

The highest domain scores are row mappers. They do not separate the cuts. The black bars separate the object graph from the two cuts whose behavior modules do not import each other. The red bars separate Reserving, which writes one struct, from both DDD services, which write three.
