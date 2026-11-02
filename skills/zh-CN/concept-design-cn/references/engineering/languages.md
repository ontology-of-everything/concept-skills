# 语言映射

应用[架构约束](architecture.md)；以下路径映射归属，不增加层。

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

每个概念是 Cargo package；组合和 HTTP 默认是 server 模块。
显式声明成员依赖；`workspace.dependencies` 不自动添加依赖。
定向构建包含依赖。
`lib.rs` 只导出业务 API 与构造入口。
其余内部保持私有或 `pub(crate)`。
源码检查限制构造访问及 crate 内部分层。
用 `cargo metadata --format-version 1` 检查支持 target/feature 下的包依赖与环。
Cargo 图本身不检查内部分层。
端口用内部 trait，优先泛型。
动态分派前检查 dyn compatibility，任务边界检查 Send/Sync。
原生 `async fn` trait 不保证 dyn compatibility。

参考：[workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html)、
[metadata](https://doc.rust-lang.org/cargo/commands/cargo-metadata.html)、
[可见性](https://doc.rust-lang.org/reference/visibility-and-privacy.html)、
[dyn compatibility](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility)。

## Java

```text
settings.gradle.kts                 # 项目名称与目录
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

每个概念是 Gradle 项目或 Maven 模块；组合和协议默认是 server 内的包。
显式声明项目与依赖。
公开签名暴露依赖类型时才用 Gradle `api`，否则用 `implementation`。
使用构造器注入。
Java 子包不继承 package-private 权限。
架构检查 MUST 限制外部使用必须公开的内部类型。
在 test/check 中用 ArchUnit 或等价工具扫描全部相关类输出。
使用 Spring Modulith 时，通过 `additionalPackages` 或显式模块来源纳入应用根包外的概念包。
核对实际发现的叶模块，配置命名接口与允许依赖。
Modulith `verify` 默认不禁止概念间调用公开 API。

参考：[Gradle](https://docs.gradle.org/current/userguide/multi_project_builds.html)、
[Maven](https://maven.apache.org/guides/mini/guide-multiple-modules.html)、
[ArchUnit](https://www.archunit.org/userguide/html/000_Index.html)、
[Spring Modulith](https://docs.spring.io/spring-modulith/reference/fundamentals.html)。

## TypeScript

```text
package.json
pnpm-workspace.yaml
tsconfig.json                       # tsc --build 的项目引用
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

每个概念是 workspace package，显式声明依赖和构建/测试脚本。
组合和 HTTP 默认归 server。
目录、别名和 workspace 成员身份本身不构成构建单元。
`tsc --build` 须配置项目引用、`composite` 和声明输出。
主入口导出业务 API，按需通过显式 `./assembly` 子路径导出构造能力。
package exports 不阻止相对路径或别名访问内部源码；检查 MUST 覆盖两者。
用 dependency-cruiser 或等价工具检查已解析源码依赖，包含别名、再导出和类型导入。
设置 `tsPreCompilationDeps: true` 纳入已擦除导入；区分 `preCompilationOnly` 时用 `"specify"`。
禁止依赖 MUST 使 check/test/CI 失败；报告未解析路径。
只扫描编译后 JavaScript 会遗漏已擦除类型。
外部身份用泛型或品牌类型。
组合结果 MUST NOT 暴露概念实现。
EventEmitter、Promise 链和类型检查不保证同步或恢复语义。

参考：[pnpm](https://pnpm.io/workspaces)、
[项目引用](https://www.typescriptlang.org/docs/handbook/project-references.html)、
[Node exports](https://nodejs.org/api/packages.html#package-entry-points)、
[dependency-cruiser 规则](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md)、
[配置](https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md)。
