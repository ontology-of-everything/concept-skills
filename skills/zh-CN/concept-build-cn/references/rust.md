# Rust / Axum

将[工程架构](architecture.md)映射为 Cargo package。业务模块是 library，server 是唯一启动 binary。构建包时包含其依赖。

## Workspace

```text
Cargo.toml
Cargo.lock
apps/server/                         # Cargo.toml + src/main.rs，唯一 binary
modules/
  concepts/reservation/               # Cargo.toml + CONCEPT.md + src/lib.rs
  concepts/payment/                   # 同上，各自一个 library crate
  composition/                        # Cargo.toml + SYNCS.md + src/lib.rs
    src/syncs/                      # 具名同步规则，非独立构建单元
  api/                                # Cargo.toml + src/lib.rs，Axum
  shared/                             # Cargo.toml + src/lib.rs
```

按项目选择 edition/MSRV 和兼容的 resolver：

```toml
[workspace]
members = ["apps/server", "modules/concepts/*", "modules/composition", "modules/api", "modules/shared"]
resolver = "3" # Rust 2024 工程
```

每个成员声明 package 与依赖。概念只依赖必要 shared 类型和技术设施，composition 依赖概念接口，api 依赖 composition、shared、axum。
server 声明装配依赖。workspace.dependencies 只管理版本，不自动给成员添加依赖。概念分组后更新 glob。

## 接口与内部实现

需要区分领域和应用职责时，可采用以下 Clean 分层，省略未用层次。

```text
src/
  lib.rs                    # 有限 re-export 与装配入口
  api.rs                    # 动作/query trait、输入输出 case、必要事件
  domain/                   # 模型、不变量、内层端口 trait
  application/              # 实现 API，依赖 domain 与端口
  adapter/                  # sqlx/内存/外部设施实现
```

公开契约与受限工厂，实现保持私有或 `pub(crate)`：

```rust
mod api;
mod domain;
mod application;
mod adapter;

pub use api::{ReservationApi, HoldResult, ReservationId};
// 需要 server 装配时，只公开受限工厂/配置，返回 API 实现。
```

工厂返回公开接口，不暴露 adapter。外部身份用泛型或不透明类型，不引用另一概念。
composition 定义自己的请求与结果类型，避免 api 因类型泄漏依赖概念。

内层定义端口 trait。优先用泛型，需要共享运行时替换才用 `Arc<dyn Trait>`。
异步 trait object 使用对象安全的 boxed future 或核验过的转换，不能假定原生 async fn trait 支持 dyn。
按实际 Axum/Tokio 任务边界检查 `Send`/`Sync`。

## 装配与 HTTP

server 构造概念，注入 composition，再将组合接口注入 api state 并启动 Axum。
api 负责路由、中间件、HTTP 与 JSON 映射，不装配概念存储。
状态齐备的路由工厂可返回 `Router<()>`，否则返回 `Router<AppState>`，由 server 调用 with_state。

规则完成、关联与失败行为遵循[执行与恢复](execution.md)，单纯传播 `?` 不能代替跨动作恢复。

## 检查

```bash
cargo build -p concept-reservation
cargo test -p concept-reservation
cargo test -p composition
cargo check --workspace
cargo test --workspace
```

使用清单中的包名。检查支持 features 下的 cargo metadata 依赖图、源码访问与公开接口。
Cargo 和 cargo-deny 不检查 crate 内分层。另测 server 启动及应用场景，不以 library 构建代替装配验证。

依据：[Cargo workspace](https://doc.rust-lang.org/cargo/reference/workspaces.html)、
[构建选择](https://doc.rust-lang.org/cargo/commands/cargo-build.html)、
[dyn 兼容性](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility)、
[Axum state](https://docs.rs/axum/latest/axum/struct.Router.html#method.with_state)。
