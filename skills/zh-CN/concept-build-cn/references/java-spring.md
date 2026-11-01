# Java / Spring

将[工程架构](architecture.md)映射为 Gradle 项目或 Maven 模块。每个模块产出 library JAR，server 是唯一 Spring Boot 应用。

## 构建结构

```text
settings.gradle.kts
build.gradle.kts                      # 共用构建约定
apps/server/                          # build.gradle.kts + 启动/装配
modules/
  concepts/reservation/               # build.gradle.kts + CONCEPT.md
  concepts/payment/                   # 各自 src/main/java、src/test/java
  composition/                        # build.gradle.kts + SYNCS.md
    src/main/java/<base>/composition/syncs/  # 具名规则，非独立构建单元
  api/                                # build.gradle.kts + Controller/DTO
  shared/                             # build.gradle.kts + 基础类型
```

声明项目：

```kotlin
include(":apps:server", ":modules:concepts:reservation", ":modules:concepts:payment",
        ":modules:composition", ":modules:api", ":modules:shared")
```

library 使用 java-library，只有 server 构建可执行 Boot JAR。api 依赖 composition：

```kotlin
dependencies {
    implementation(project(":modules:composition"))
    implementation(project(":modules:shared"))
    // Web 框架依赖由项目统一版本约定提供。
}
```

composition 依赖概念项目。公开签名暴露依赖类型时才用 Gradle api，否则用 implementation。
组合 DTO 不应迫使 api 引入概念类型。Maven 通过父 POM 聚合与显式依赖表达相同边界。

## 接口与装配

需要区分领域与应用职责时，采用以下 Clean 分层：

```text
io.example.concept.reservation/
  package-info.java                  # 显式模块与允许依赖
  ReservationApi.java                # 动作、query、结果 case
  ReservationEvents.java             # 按需
  domain/                            # 纯 Java 模型、不变量、端口
  application/ReservationService.java # implements ReservationApi
  adapter/persistence/               # repository 实现
```

内层声明端口，adapter 实现。实现类尽量保持包内可见，通过模块内 Bean 配置或受限公开工厂装配。
概念接口不包含 HTTP/JSON 类型。composition 实现具名规则与应用接口，Controller 调用接口并映射协议。

## 检查

同时核对构建单元与 Spring Modulith 模块。按项目版本配置发现规则，覆盖全部概念叶包、composition、api 和 shared。
目录和多个 JAR 不能证明发现完整。

- verify 检查无环和内部访问，另须声明允许依赖，因为它默认允许概念间公开 API 依赖。
- 用 ArchUnit 核对内部分层、api 访问 composition/shared、server 装配访问，以及源码与构建清单的一致性。
- 用 `@ApplicationModuleTest` 或模块测试覆盖运作原理与不变量，组合测试覆盖应用场景、并发关联与恢复。
- 事务、模块监听器与发布记录不自动提供合取匹配、flow 绑定或幂等，须遵循[执行与恢复](execution.md)。

```bash
./gradlew :modules:concepts:reservation:build
./gradlew :modules:composition:test
./gradlew :apps:server:check :apps:server:bootJar
# Maven 等价定向构建（artifactId 按项目替换）
./mvnw -pl concept-reservation -am verify
```

使用实际项目名，定向构建包含依赖。另跑全部模块与装配检查，确认 server 的架构测试扫描全部模块。

依据：[Gradle 多项目](https://docs.gradle.org/current/userguide/multi_project_builds.html)、
[Maven reactor](https://maven.apache.org/guides/mini/guide-multiple-modules.html)、
[Modulith 模块模型](https://docs.spring.io/spring-modulith/reference/fundamentals.html)、
[验证](https://docs.spring.io/spring-modulith/reference/verification.html)。
