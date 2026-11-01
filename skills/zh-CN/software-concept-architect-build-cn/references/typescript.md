# TypeScript

将[工程架构](architecture.md)映射为 pnpm workspace。每个 concept、composition、api、shared 包独立构建和测试，由 server 装配。

## 包与导出

```text
pnpm-workspace.yaml
apps/server/                        # package.json、tsconfig.json、src/main.ts
modules/
  concepts/reservation/              # package.json、tsconfig.json、CONCEPT.md
  concepts/payment/                 # 同上
  composition/                        # package.json、tsconfig.json、SYNCS.md
    src/syncs/                      # 具名同步规则，非独立构建单元
  api/                                # package.json、tsconfig.json、HTTP/DTO
  shared/                             # package.json、tsconfig.json、基础类型
```

workspace 纳入 `apps/*`、`modules/concepts/*` 和 `modules/*` 的实际包，分组后更新 glob。
各包声明依赖和脚本，`src/index.ts` 只导出公开契约与受限工厂。设施使用端口，按需增加 domain/application。

ESM 包示例：

```json
{
  "name": "@app/api",
  "type": "module",
  "exports": {".": {"types": "./dist/index.d.ts", "import": "./dist/index.js"}},
  "dependencies": {"@app/composition": "workspace:*"},
  "scripts": {"build": "tsc -b"}
}
```

用 project references、`composite` 和声明输出构建依赖图。仅列入 workspace 不足以证明独立编译。
exports 限制消费入口，源码检查还须阻止相对路径和 tsconfig alias 穿透内部实现。

## 接口与装配

内层声明端口 interface，adapter 实现，server 经公开工厂注入。
外部身份用泛型或 branded 类型，不引入另一概念。composition 定义应用 DTO，api 映射协议与 JSON 并调用 composition。
具名规则函数或对象遵循[执行契约](execution.md)，监听器与 Promise 链本身不保证匹配和恢复。

## 检查

```bash
pnpm --filter '@app/reservation...' build
pnpm --filter @app/reservation test
pnpm --filter @app/composition test
pnpm -r build
pnpm -r test
```

包名和脚本按清单替换，定向构建包含依赖。
用 dependency-cruiser 等检查包依赖、源码层次、公开入口、概念独立性、api 只访问 composition/shared，以及 server 的装配访问。
类型检查与 exports 本身不能证明全部边界。

依据：[pnpm workspace](https://pnpm.io/workspaces)、[依赖筛选](https://pnpm.io/filtering)、
[TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html)、
[Node exports](https://nodejs.org/api/packages.html#package-entry-points)。
