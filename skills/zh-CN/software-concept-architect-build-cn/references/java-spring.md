# Java / Spring

目标为 Java 时读取。模块关系与案例见 [工程架构](architecture.md)。使用 Gradle 多项目或 Maven 多模块，每个模块独立 library JAR，server 是唯一 Spring Boot 启动应用。

## 构建骨架

```text
settings.gradle.kts
build.gradle.kts                      # 共用构建约定
apps/server/                          # build.gradle.kts + 启动/装配
modules/
  concepts/reservation/               # build.gradle.kts + CONCEPT.md
  concepts/payment/                   # 各自 src/main/java、src/test/java
  syncs/                              # build.gradle.kts + SYNCS.md
  gateway/                            # build.gradle.kts + Controller/DTO
  shared/                             # build.gradle.kts + 基础类型
```

`settings.gradle.kts` 示例：

```kotlin
include(":apps:server", ":modules:concepts:reservation", ":modules:concepts:payment",
        ":modules:syncs", ":modules:gateway", ":modules:shared")
```

library 子项目采用 `java-library`；仅 server 生成可执行 Boot JAR。gateway 的依赖片段：

```kotlin
dependencies {
    implementation(project(":modules:syncs"))
    implementation(project(":modules:shared"))
    // Web 框架依赖由项目统一版本约定提供。
}
```

syncs 依赖概念项目；server 装配所有模块。仅当公开签名确实暴露某依赖类型时使用 Gradle `api`，否则用 `implementation`。syncs 的应用 DTO 不暴露概念类型，避免迫使 gateway 引入概念。Maven 用父 POM 聚合和显式模块依赖表达同样的边界；仅分 Java 包不满足独立构建要求。

## 模块内部与装配

```text
io.example.concept.reservation/
  package-info.java                  # 显式模块与允许依赖
  ReservationApi.java                # 动作、query、结果 case
  ReservationEvents.java             # 按需
  domain/                            # 纯 Java 模型、不变量、端口
  application/ReservationService.java # implements ReservationApi
  adapter/persistence/               # repository 实现
```

存储端口由内层声明，应用层依赖端口，适配器实现端口。实现类尽量保持包内可见；由模块内 Bean 配置或受限公开配置入口装配，避免 server 引用内部实现。概念签名不含 HTTP/JSON 类型。syncs 以具名方法/规则对象实现应用接口，gateway Controller 只调用该接口并做协议映射。

## 边界与行为验证

构建单元与 Spring Modulith application module 是两种边界，须同时核实。按项目版本配置显式模块发现，使每个概念叶包、syncs、gateway、shared 都受检查；目录分组和多个 JAR 不自动保证发现正确。

- `ApplicationModules.of(App.class).verify()` 检查无环与内部访问；另声明允许依赖集合，概念只允许必要 shared。默认 verify 不禁止概念间公开 API 依赖。
- 用 ArchUnit 检查源码层次、gateway 仅引用 syncs/shared、server 仅经装配入口接入；验证构建清单依赖与源码边界一致。
- `@ApplicationModuleTest`/模块测试验证 OP 与不变量；组合测试验证应用场景、并发关联与失败恢复。
- `@Transactional`、`@ApplicationModuleListener` 和事件发布记录不自动提供多事件合取、flow 绑定或副作用幂等；遵守正文的提交/完成事件契约。

```bash
./gradlew :modules:concepts:reservation:build
./gradlew :modules:syncs:test
./gradlew :apps:server:check :apps:server:bootJar
# Maven 等价定向构建（artifactId 按项目替换）
./mvnw -pl concept-reservation -am verify
```

单模块构建包含其所需依赖；整体另执行各模块检查及应用装配测试。多模块环境下，确认 server 的架构测试扫描到全部模块。

依据：[Gradle 多项目](https://docs.gradle.org/current/userguide/multi_project_builds.html)、[Maven reactor](https://maven.apache.org/guides/mini/guide-multiple-modules.html)、[Modulith 模块模型](https://docs.spring.io/spring-modulith/reference/fundamentals.html)、[验证规则](https://docs.spring.io/spring-modulith/reference/verification.html)。
