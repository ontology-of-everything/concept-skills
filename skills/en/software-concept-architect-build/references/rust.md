# Rust / Axum

Map [the architecture](architecture.md) to Cargo packages. Business modules are libraries; server is
the sole startup binary. A package build includes its dependencies.

## Workspace

```text
Cargo.toml
Cargo.lock
apps/server/                         # Cargo.toml + src/main.rs; sole binary
modules/
  concepts/reservation/               # Cargo.toml + CONCEPT.md + src/lib.rs
  concepts/payment/                   # same; one library crate each
  composition/                        # Cargo.toml + SYNCS.md + src/lib.rs
    src/syncs/                      # named synchronization rules; not a build unit
  api/                                # Cargo.toml + src/lib.rs; Axum
  shared/                             # Cargo.toml + src/lib.rs
```

Choose the project's edition/MSRV and a compatible resolver:

```toml
[workspace]
members = ["apps/server", "modules/concepts/*", "modules/composition", "modules/api", "modules/shared"]
resolver = "3" # Rust 2024 project
```

Each member declares `[package]` and its dependencies. Concepts need only shared types and technical
facilities; composition depends on concept interfaces; api depends on composition, shared, and axum.
Server declares assembly dependencies. Workspace dependency entries centralize versions without
adding member dependencies automatically. Update globs when grouping concepts.

## Interfaces and internals

This optional Clean layout separates domain and application responsibilities. Omit unused layers.

```text
src/
  lib.rs                    # limited re-exports and assembly entry
  api.rs                    # action/query traits, input/output cases, necessary events
  domain/                   # models, invariants, inner port traits
  application/              # API implementation using domain and ports
  adapter/                  # sqlx/in-memory/external implementations
```

Expose contracts and restricted factories, keeping implementations private or `pub(crate)`:

```rust
mod api;
mod domain;
mod application;
mod adapter;

pub use api::{ReservationApi, HoldResult, ReservationId};
// Expose a restricted factory/configuration returning an API implementation when server needs it.
```

Factories return public interfaces without exposing adapters. External identities use generic or
opaque types, not another concept's types. Composition defines its own request/result types so api
needs no concept dependency.

Inner code declares port traits. Prefer generics; use `Arc<dyn Trait>` for shared runtime substitution.
For async trait objects, use object-safe boxed futures or a verified transformation. Do not assume
native `async fn` traits are dyn-compatible. Check `Send`/`Sync` for actual Axum/Tokio task crossings.

## Assembly and HTTP

Server constructs concepts, injects them into composition, then supplies composition interfaces to
api state and starts Axum. Api owns routes, middleware, HTTP and JSON mapping, not concept storage.
A fully supplied route factory may return `Router<()>`; otherwise return `Router<AppState>` and let
server provide state with `with_state`.

Implement rule completion, correlation, and failure behavior under [execution and recovery](execution.md).
Propagating `?` alone is not cross-action recovery.

## Checks

```bash
cargo build -p concept-reservation
cargo test -p concept-reservation
cargo test -p composition
cargo check --workspace
cargo test --workspace
```

Use manifest package names. Check the `cargo metadata` graph under supported features, source access,
and public interfaces. Cargo and cargo-deny do not check layers inside a crate. Test server startup
and application scenarios separately from library builds.

Sources: [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html),
[build selection](https://doc.rust-lang.org/cargo/commands/cargo-build.html),
[dyn compatibility](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility),
[Axum state](https://docs.rs/axum/latest/axum/struct.Router.html#method.with_state).
