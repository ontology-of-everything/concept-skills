# Rust / Axum

目标为 Rust 时读取。模块关系与案例见 [工程架构](architecture.md)；以下是该基线的 Cargo 映射。

## Workspace

```text
Cargo.toml
Cargo.lock
apps/server/                         # Cargo.toml + src/main.rs，唯一 binary
modules/
  concepts/reservation/               # Cargo.toml + CONCEPT.md + src/lib.rs
  concepts/payment/                   # 同上，各自一个 library crate
  syncs/                              # Cargo.toml + SYNCS.md + src/lib.rs
  gateway/                            # Cargo.toml + src/lib.rs，Axum
  shared/                             # Cargo.toml + src/lib.rs
```

根清单示例（edition/MSRV 按项目选择，resolver 与其兼容）：

```toml
[workspace]
members = ["apps/server", "modules/concepts/*", "modules/syncs", "modules/gateway", "modules/shared"]
resolver = "3" # Rust 2024 工程
```

每个成员有自己的 `[package]`。例如 `concept-reservation` 只按需声明 shared 和技术依赖；syncs 声明各概念依赖，gateway 声明 syncs、shared、axum，server 声明公开装配所需模块。`[workspace.dependencies]` 只集中管理版本，成员仍须声明所用依赖。增加组目录时更新 members glob。

独立构建以 package 为选择单位，构建其依赖；各业务模块默认只有 library target，server 链接它们并启动一个进程。

## 公开接口与内部分层

```text
src/
  lib.rs                    # 有限 re-export 与装配入口
  api.rs                    # 动作/query trait、输入输出 case、必要事件
  domain/                   # 模型、不变量、内层端口 trait
  application/              # 实现 API，依赖 domain 与端口
  adapter/                  # sqlx/内存/外部设施实现
```

`lib.rs` 的可见性骨架：

```rust
mod api;
mod domain;
mod application;
mod adapter;

pub use api::{ReservationApi, HoldResult, ReservationId};
// 需要 server 装配时，只公开受限工厂/配置，返回 API 实现。
```

内部层默认私有或 `pub(crate)`，不 `pub mod adapter` 来方便业务调用。工厂签名只暴露必要配置和公开契约。外部身份用泛型或不透明 ID，概念 API 不引用另一概念的类型。syncs 公开自己的应用请求/结果类型，gateway 不因类型泄漏而依赖概念。

端口 trait 由内层定义，adapter 实现；用泛型做静态分发，需要共享运行期实现时才用 `Arc<dyn Trait>`。
异步 trait 若要作 `dyn`，必须使用对象安全的 boxed-future 签名或已核验的转换方案；不能假定原生 `async fn` trait 可直接作 trait object。跨 Axum/Tokio 任务的接口和 future 按实际调用满足 `Send`/`Sync` 要求。

## 装配与 HTTP

server 构造概念实现 → 注入 syncs → 将 syncs 接口注入 gateway state → 启动 Axum。gateway 仅装配路由、中间件和 DTO 映射，不装配概念存储。
其公开路由入口可返回已注入状态的 `Router<()>`；仍缺状态时才返回 `Router<AppState>`，由 server 调用 `with_state`。

Axum、HTTP 请求/响应及外部 JSON DTO 留在 gateway。概念动作通过进程内 API 调用。async mediator 或规则引擎均须兑现正文中的完成事件、关联和失败契约；`?` 传播错误不能代替跨动作恢复策略。

## 验证

```bash
cargo build -p concept-reservation
cargo test -p concept-reservation
cargo test -p syncs
cargo check --workspace
cargo test --workspace
```

包名以清单为准。CI 从 `cargo metadata` 的解析图检查受支持 features 下的模块依赖，再检查源码层次与公开面；可编译不等于架构合法。Cargo 与 cargo-deny 都不能检查同一 crate 内的 domain/adapter 分层。验证 server 启动和应用场景，不以 library 构建成功代替整体装配。

依据：[Cargo workspace](https://doc.rust-lang.org/cargo/reference/workspaces.html)、
[构建选择](https://doc.rust-lang.org/cargo/commands/cargo-build.html)、
[trait object 兼容性](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility)、
[Axum Router 状态](https://docs.rs/axum/latest/axum/struct.Router.html#method.with_state)。
