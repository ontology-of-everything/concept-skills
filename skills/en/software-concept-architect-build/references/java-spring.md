# Java / Spring

Map [the architecture](architecture.md) to Gradle projects or Maven modules. Each module produces a
library JAR; server is the only Spring Boot application.

## Build layout

```text
settings.gradle.kts
build.gradle.kts                      # shared build conventions
apps/server/                          # build.gradle.kts + startup/assembly
modules/
  concepts/reservation/               # build.gradle.kts + CONCEPT.md
  concepts/payment/                   # separate src/main/java and src/test/java
  composition/                        # build.gradle.kts + SYNCS.md
    src/main/java/<base>/composition/syncs/  # named rules; not a build unit
  api/                                # build.gradle.kts + Controller/DTO
  shared/                             # build.gradle.kts + foundational types
```

Declare the projects:

```kotlin
include(":apps:server", ":modules:concepts:reservation", ":modules:concepts:payment",
        ":modules:composition", ":modules:api", ":modules:shared")
```

Use `java-library` for libraries; only server builds an executable Boot JAR. Api depends on composition:

```kotlin
dependencies {
    implementation(project(":modules:composition"))
    implementation(project(":modules:shared"))
    // Web framework dependencies follow the project's version conventions.
}
```

Composition depends on concept projects. Use Gradle `api` only when a public signature exposes a
dependency type, otherwise `implementation`. Composition DTOs must not force api to import concepts.
Maven expresses the same boundaries through parent aggregation and explicit dependencies.

## Interfaces and assembly

Use this Clean layout only when domain and application responsibilities need separation:

```text
io.example.concept.reservation/
  package-info.java                  # explicit module and allowed dependencies
  ReservationApi.java                # actions, queries, result cases
  ReservationEvents.java             # when needed
  domain/                            # pure Java models, invariants, ports
  application/ReservationService.java # implements ReservationApi
  adapter/persistence/               # repository implementations
```

Inner code declares ports; adapters implement them. Keep implementations package-private where
possible. Assemble through module-local Bean configuration or restricted public factories.
Concept interfaces contain no HTTP/JSON types. Composition implements named rules and application
interfaces; controllers call those interfaces and map protocols.

## Checks

Verify both build units and Spring Modulith modules. Configure discovery for the project version so
all concept leaves, composition, api, and shared are checked; directories and JARs alone do not prove this.

- `ApplicationModules.of(App.class).verify()` checks cycles and internal access. Declare allowed
  dependencies too, since it permits concept-to-concept public API dependencies by default.
- Use ArchUnit to check internal layers, api access to composition/shared, server assembly access,
  and agreement between source dependencies and build manifests.
- Use `@ApplicationModuleTest` or module tests for operational principles/invariants and composition tests for scenarios,
  concurrent correlation, and recovery.
- Transactions, application-module listeners, and publication records do not alone provide joint
  matching, flow bindings, or idempotency. Follow [execution and recovery](execution.md).

```bash
./gradlew :modules:concepts:reservation:build
./gradlew :modules:composition:test
./gradlew :apps:server:check :apps:server:bootJar
# Equivalent targeted Maven build; substitute the actual artifactId.
./mvnw -pl concept-reservation -am verify
```

Use actual project names. Targeted builds include dependencies. Run all module and assembly checks;
ensure server's architecture tests scan every module on the classpath.

Sources: [Gradle projects](https://docs.gradle.org/current/userguide/multi_project_builds.html),
[Maven reactor](https://maven.apache.org/guides/mini/guide-multiple-modules.html),
[Modulith model](https://docs.spring.io/spring-modulith/reference/fundamentals.html),
[verification](https://docs.spring.io/spring-modulith/reference/verification.html).
