# Language mapping

Apply [architecture constraints](architecture.md); these paths map ownership rather than add layers.

## Rust

```text
Cargo.toml                          # workspace members
apps/server/
  Cargo.toml
  src/{main.rs,lib.rs,bootstrap.rs}
  src/adapters/http.rs
  src/compositions/booking/make_reservation/
    SYNCS.md
    create_reservation_sync.rs
  tests/{architecture.rs,booking_scenarios.rs,http_contract.rs}
modules/booking/concepts/reserving/
  CONCEPT.md
  Cargo.toml                        # package booking-reserving
  src/{lib.rs,assembly.rs}
  src/domain/mod.rs
  src/application/{mod.rs,ports.rs}
  src/adapters/{mod.rs,postgres.rs}
  tests/reserving_contract.rs
```

Each concept is a Cargo package; composition and HTTP default to server modules.
Declare member dependencies explicitly; `workspace.dependencies` does not add them.
Targeted builds include dependencies.
Limit `lib.rs` exports to business APIs and construction entry.
Keep other internals private or `pub(crate)`.
Source checks enforce construction access and layers inside crates.
Inspect `cargo metadata --format-version 1` for package dependencies/cycles under supported targets/features.
A Cargo graph alone does not inspect internal layers.
Ports are inner traits; prefer generics.
Check dyn compatibility before dynamic dispatch and Send/Sync at task boundaries.
Native `async fn` traits do not guarantee dyn compatibility.

References: [workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html),
[metadata](https://doc.rust-lang.org/cargo/commands/cargo-metadata.html),
[visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html),
[dyn compatibility](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility).

## Java

```text
settings.gradle.kts                 # project names and directories
apps/server/
  build.gradle.kts
  src/main/java/com/example/server/
    ServerApplication.java
    bootstrap/ServerConfiguration.java
    adapters/http/BookingController.java
    compositions/booking/makereservation/
      SYNCS.md
      CreateReservationSync.java
  src/test/java/com/example/server/{architecture,compositions,adapters}/
modules/booking/concepts/reserving/
  CONCEPT.md
  build.gradle.kts                  # project :booking-reserving
  src/main/java/com/example/booking/reserving/
    domain/Reservation.java
    application/Reserving.java
    application/ports/ReservationRepository.java
    adapters/persistence/PostgresReservationRepository.java
    assembly/ReservingFactory.java
  src/test/java/com/example/booking/reserving/ReservingContractTest.java
```

Each concept is a Gradle project or Maven module; composition/protocol default to server packages.
Declare projects and dependencies explicitly.
Use Gradle `api` only when public signatures expose dependency types; otherwise use `implementation`.
Use constructor injection.
Java subpackages do not inherit package-private access.
Architecture checks MUST restrict external access to necessarily public internal types.
Run ArchUnit or equivalent over all relevant class outputs in test/check.
With Spring Modulith, include concept packages outside the application root through `additionalPackages` or explicit module sources.
Verify the discovered leaf modules and configure named interfaces/allowed dependencies.
Modulith `verify` does not forbid concept-to-concept public API calls by default.

References: [Gradle](https://docs.gradle.org/current/userguide/multi_project_builds.html),
[Maven](https://maven.apache.org/guides/mini/guide-multiple-modules.html),
[ArchUnit](https://www.archunit.org/userguide/html/000_Index.html),
[Spring Modulith](https://docs.spring.io/spring-modulith/reference/fundamentals.html).

## TypeScript

```text
package.json
pnpm-workspace.yaml
tsconfig.json                       # references for tsc --build
apps/server/
  package.json
  tsconfig.json
  src/{main.ts,bootstrap.ts}
  src/adapters/http/booking.routes.ts
  src/compositions/booking/make-reservation/
    SYNCS.md
    create-reservation.sync.ts
  tests/{architecture,compositions,adapters}/
modules/booking/concepts/reserving/
  CONCEPT.md
  package.json                      # @booking/reserving
  tsconfig.json
  src/{index.ts,assembly.ts}
  src/domain/reservation.ts
  src/application/reserving.ts
  src/application/ports/reservation-repository.ts
  src/adapters/persistence/postgres-reservation-repository.ts
  tests/reserving.contract.test.ts
```

Each concept is a workspace package with explicit dependencies and build/test scripts.
Composition and HTTP default to server.
Directories, aliases, and workspace membership alone do not establish build units.
For `tsc --build`, configure project references, `composite`, and declaration output.
Export business APIs from the main entry and construction through an explicit `./assembly` subpath when needed.
Package exports do not prevent relative/alias access to source internals; checks MUST cover both.
Use dependency-cruiser or equivalent on resolved source dependencies, including aliases, re-exports, and type imports.
Set `tsPreCompilationDeps: true` for erased imports, or `"specify"` when rules distinguish `preCompilationOnly`.
Forbidden dependencies MUST fail check/test/CI; report unresolved paths.
A compiled-JavaScript scan misses erased types.
Use generic or branded external identities.
Composition results MUST NOT expose concept implementations.
EventEmitter, Promise chains, and type checking do not guarantee synchronization or recovery semantics.

References: [pnpm](https://pnpm.io/workspaces),
[project references](https://www.typescriptlang.org/docs/handbook/project-references.html),
[Node exports](https://nodejs.org/api/packages.html#package-entry-points),
[dependency-cruiser rules](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md),
[options](https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md).
