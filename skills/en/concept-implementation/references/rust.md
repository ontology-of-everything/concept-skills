# Rust Implementation

These are optional engineering mappings. Separate packages, ports/adapters, layers, and protocol placement are not concept-theory requirements. Requesting may encapsulate protocols in its implementation.

Use a Cargo workspace with one crate per concept:

```text
app/              # composition root and protocol adapters
syncs/            # named composition rules, optionally grouped by flow
concepts/user/    # one independent crate per concept
concepts/session/
shared-kernel/    # identifiers and time only; no business behavior
```

Dependencies flow `app → syncs → concepts/*`; app also selects adapters. Concept crates never depend
on one another. Grouping may add directories and workspace globs without changing crate names or
dependency rules.

Inside a concept crate, keep invariants/pure logic in `domain.rs`, actions in `actions.rs`, port
traits in `ports.rs`, and SQL/in-memory implementations in `adapters/`. Use generics for static
dispatch and `Arc<dyn Trait>` only for runtime substitution.

`Password<U>` uses a generic identity rather than a User concept type. `Result` may encode declared
cases, but sequential `?` across concepts can leave partial completion; implement the confirmed
partial-completion policy (response, retry, compensation, or intentional retention), or an applicable transaction.

When using edge adapters, keep axum/tonic routes, serde DTOs, and OpenAPI/protobuf contracts in app or an interfaces crate.
Routes call synchronizations, never concept internals. In CI, inspect `cargo metadata` across
supported features to assert no concept-to-concept dependency. `cargo-deny` handles package policy
but cannot separate domain and adapter code inside one crate.

Sources: [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html) and
[cargo-deny bans](https://embarkstudios.github.io/cargo-deny/checks/bans/cfg.html).
