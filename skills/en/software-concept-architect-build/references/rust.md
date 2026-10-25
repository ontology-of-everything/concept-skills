# Rust / Axum

Read for Rust targets. [Architecture](architecture.md) owns module relationships and examples;
this reference maps that baseline to Cargo.

## Workspace

```text
Cargo.toml
Cargo.lock
apps/server/                         # Cargo.toml + src/main.rs; sole binary
modules/
  concepts/reservation/               # Cargo.toml + CONCEPT.md + src/lib.rs
  concepts/payment/                   # same; one library crate each
  syncs/                              # Cargo.toml + SYNCS.md + src/lib.rs
  gateway/                            # Cargo.toml + src/lib.rs; Axum
  shared/                             # Cargo.toml + src/lib.rs
```

Root manifest example; select edition/MSRV for the project and a compatible resolver:

```toml
[workspace]
members = ["apps/server", "modules/concepts/*", "modules/syncs", "modules/gateway", "modules/shared"]
resolver = "3" # Rust 2024 project
```

Each member has its own `[package]`. For example, `concept-reservation` declares only necessary shared
and technical dependencies. Syncs declares concept dependencies; gateway declares syncs, shared, and
axum; server declares modules needed for public assembly. `[workspace.dependencies]` centralizes
versions but members still declare dependencies they use. Update member globs when adding groups.

Select packages for independent builds, including their dependencies. Business modules default to
library targets; server links them and starts one process.

## Public API and internal layers

```text
src/
  lib.rs                    # limited re-exports and assembly entry
  api.rs                    # action/query traits, input/output cases, necessary events
  domain/                   # models, invariants, inner port traits
  application/              # API implementation using domain and ports
  adapter/                  # sqlx/in-memory/external implementations
```

Visibility skeleton for `lib.rs`:

```rust
mod api;
mod domain;
mod application;
mod adapter;

pub use api::{ReservationApi, HoldResult, ReservationId};
// Expose a restricted factory/configuration returning an API implementation when server needs it.
```

Keep internals private or `pub(crate)`; do not expose `pub mod adapter` for business callers.
Factories expose only necessary configuration and public contracts. Use generic/opaque external
identities without importing another concept's types. Syncs exports its own application requests
and results so gateway does not acquire concept dependencies through leaked types.

Inner layers define port traits; adapters implement them. Prefer generic static dispatch; use
`Arc<dyn Trait>` when shared runtime substitution is needed. Async traits used through `dyn` need
object-safe boxed-future signatures or a verified transformation; native `async fn` traits cannot
be assumed usable as trait objects. Satisfy the actual `Send`/`Sync` requirements of interfaces and
futures crossing Axum/Tokio tasks.

## Assembly and HTTP

Server constructs concepts → injects them into syncs → injects syncs APIs into gateway state →
starts Axum. Gateway assembles routes, middleware, and DTO mapping, not concept storage. A route
factory with state already supplied may return `Router<()>`; return `Router<AppState>` only while
state is missing and let server call `with_state`.

Keep Axum, HTTP requests/responses, and external JSON DTOs in gateway. Invoke concept actions through
in-process APIs. Async mediators and engines must satisfy the entrypoint's completion, correlation,
and failure contracts; `?` propagation does not replace recovery across actions.

## Verification

```bash
cargo build -p concept-reservation
cargo test -p concept-reservation
cargo test -p syncs
cargo check --workspace
cargo test --workspace
```

Use actual manifest package names. In CI inspect the `cargo metadata` resolved graph under supported
features, then source-layer/public-surface boundaries. Compilation alone does not establish valid
architecture. Neither Cargo nor cargo-deny checks domain/adapter layers inside one crate. Verify
server startup and application scenarios separately from library builds.

Sources: [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html),
[build selection](https://doc.rust-lang.org/cargo/commands/cargo-build.html),
[dyn compatibility](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility),
[Axum Router state](https://docs.rs/axum/latest/axum/struct.Router.html#method.with_state).
