# Java / Spring

Read for Java targets. [Architecture](architecture.md) owns module relationships and examples.
Use Gradle multi-project or Maven multi-module builds: one library JAR per module and server as the
sole Spring Boot startup application.

## Build skeleton

```text
settings.gradle.kts
build.gradle.kts                      # shared build conventions
apps/server/                          # build.gradle.kts + startup/assembly
modules/
  concepts/reservation/               # build.gradle.kts + CONCEPT.md
  concepts/payment/                   # separate src/main/java and src/test/java
  syncs/                              # build.gradle.kts + SYNCS.md
  gateway/                            # build.gradle.kts + Controller/DTO
  shared/                             # build.gradle.kts + foundational types
```

Example `settings.gradle.kts`:

```kotlin
include(":apps:server", ":modules:concepts:reservation", ":modules:concepts:payment",
        ":modules:syncs", ":modules:gateway", ":modules:shared")
```

Library projects use `java-library`; only server produces an executable Boot JAR. Gateway dependency fragment:

```kotlin
dependencies {
    implementation(project(":modules:syncs"))
    implementation(project(":modules:shared"))
    // Web framework dependencies follow the project's version conventions.
}
```

Syncs depends on concept projects; server assembles modules. Use Gradle `api` only when a public
signature exposes a dependency type; otherwise use `implementation`. Syncs application DTOs keep concept types out of their public signatures so gateway needs no concept
dependency. Maven uses parent aggregation and
explicit module dependencies for the same boundaries. Java packages alone do not establish
independent builds.

## Module internals and assembly

```text
io.example.concept.reservation/
  package-info.java                  # explicit module and allowed dependencies
  ReservationApi.java                # actions, queries, result cases
  ReservationEvents.java             # when needed
  domain/                            # pure Java models, invariants, ports
  application/ReservationService.java # implements ReservationApi
  adapter/persistence/               # repository implementations
```

Inner layers declare storage ports; application code depends on them and adapters implement them.
Keep implementations package-private where possible. Assemble with module-local Bean configuration
or a restricted public configuration entry, rather than server importing internals. Concept
signatures contain no HTTP/JSON types. Syncs implements application APIs using named methods/rule
objects; gateway controllers invoke those APIs and translate protocols.

## Boundary and behavior verification

Build units and Spring Modulith application modules are distinct boundaries; verify both. Configure
explicit discovery for the project version so every concept leaf package, syncs, gateway, and shared
is checked. Group directories and multiple JARs do not automatically guarantee correct discovery.

- `ApplicationModules.of(App.class).verify()` checks cycles and internal access. Also declare allowed
  dependencies, restricting concepts to necessary shared types. Default verification permits concept API dependencies.
- Use ArchUnit for source layers, gateway access limited to syncs/shared, and server's assembly-only
  access. Check that build manifests and source boundaries agree.
- `@ApplicationModuleTest`/module tests check OPs and invariants; composition tests cover application
  scenarios, concurrent correlation, and recovery.
- `@Transactional`, `@ApplicationModuleListener`, and event publication records do not automatically
  provide conjunctive matching, flow bindings, or effect idempotency. Follow the entrypoint's commit/completion contract.

```bash
./gradlew :modules:concepts:reservation:build
./gradlew :modules:syncs:test
./gradlew :apps:server:check :apps:server:bootJar
# Equivalent targeted Maven build; substitute the actual artifactId.
./mvnw -pl concept-reservation -am verify
```

A module build includes required dependencies. Separately run all module checks and application
assembly tests. Ensure server's architecture tests scan every module on the multi-module classpath.

Sources: [Gradle multi-project builds](https://docs.gradle.org/current/userguide/multi_project_builds.html),
[Maven reactor](https://maven.apache.org/guides/mini/guide-multiple-modules.html),
[Modulith model](https://docs.spring.io/spring-modulith/reference/fundamentals.html),
[verification](https://docs.spring.io/spring-modulith/reference/verification.html).
