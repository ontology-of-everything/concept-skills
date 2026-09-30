# Rust 落地

以下为按需采用的工程映射；独立包、port/adapter、分层与协议位置不是概念理论的硬性要求。Requesting 可在自身实现中封装协议。

## 工程骨架

cargo workspace，一个 concept 一个 crate：

```text
app/                # 组合根：唯一命名具体 adapter 的地方，装配后接路由
syncs/              # 组合层：具名规则，可按 flow 分组
concepts/
  user/             # 一个 concept 一个 crate
  password/
  session/
shared-kernel/      # 仅通用基础类型（Id、时间），无业务
```

声明依赖为 `app → syncs → concepts/*`，app 另装配具体 adapters；概念 crate 互不声明依赖。

分组目录如 `concepts/billing/invoice/`，members glob 随层次更新，crate 名及依赖规则保持；syncs 可每组一个 crate。成员只能属于一个 workspace，多层目录不等于嵌套 workspace。

## 概念 crate 内部

```text
concepts/password/src/
  domain.rs      # 不变量与纯逻辑，不依赖其他概念/协议
  actions.rs     # 概念 actions，依赖 port trait
  ports.rs       # 如 trait PasswordStore
  adapters/      # sqlx / 内存实现，供组合根选用
```

port 即 trait、adapter 实现 trait、依赖只指向 domain；用泛型做零开销静态分发，需要运行期换实现时用 `Arc<dyn Trait>`。

## 错误与身份

`Password<U>` 的 U 是泛型身份，不引用 User 概念类型。公开方法可用 `Result` 表达已声明输出，但 mediator 中 `users.register(...)?; passwords.set(...)?` 可能留下只注册用户的部分状态：须按已确认契约处理部分完成（响应、重试、补偿或有意保留），或采用适用事务，不能用 `?` 当作完整注册流程。

## 接口层落点

采用边缘适配器时，app 内 `api` 模块（或独立 interfaces crate）：axum/tonic 路由只调 syncs 函数；serde DTO、OpenAPI/proto 契约只存在于此层，概念 crate 不依赖任何协议库。

## 架构看护

- Cargo 只允许引用显式依赖的 crate；新增依赖仍须由 CI 检查其合法性。
- **cargo-deny** 检查包级依赖政策，不能区分同一 crate 内 domain 与 adapter；层级约束需拆 crate 或源码边界检查。
- CI 用 `cargo metadata` 的解析图断言概念间无依赖（包含项目支持的 features）；`cargo tree -i` 仅供人工诊断，不是自动断言。

依据：[Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html)、[cargo-deny bans](https://embarkstudios.github.io/cargo-deny/checks/bans/cfg.html)。
