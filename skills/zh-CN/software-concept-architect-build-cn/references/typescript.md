# TypeScript

目标为 TypeScript 时读取。模块关系与案例见 [工程架构](architecture.md)。采用 pnpm workspace，每个 concept、syncs、gateway、shared 一个可独立构建/测试的 package，server 统一装配与启动。

## 工程骨架

```text
pnpm-workspace.yaml
apps/server/                        # package.json、tsconfig.json、src/main.ts
modules/
  concepts/reservation/              # package.json、tsconfig.json、CONCEPT.md
  concepts/payment/                 # 同上
  syncs/                            # package.json、tsconfig.json、SYNCS.md
  gateway/                          # package.json、tsconfig.json、HTTP/DTO
  shared/                           # package.json、tsconfig.json、基础类型
```

workspace 包含 `apps/*`、`modules/concepts/*` 和 `modules/*` 的实际包；增加组目录时更新 glob。每包声明自己的依赖与 build/test 脚本。内部组织为 `src/index.ts`、`api.ts`、`domain/`、`application/`、`adapter/`；`index.ts` 仅导出业务接口、结果类型与必要装配入口。

包清单片段（使用 ESM 与声明文件的工程）：

```json
{
  "name": "@app/gateway",
  "type": "module",
  "exports": {".": {"types": "./dist/index.d.ts", "import": "./dist/index.js"}},
  "dependencies": {"@app/syncs": "workspace:*"},
  "scripts": {"build": "tsc -b"}
}
```

配置 TypeScript project references 与 `composite`/声明输出，使构建顺序遵循依赖；不能仅写 workspace 清单就宣称可独立编译。`exports` 限制消费入口，源码边界检查另阻止相对路径或 tsconfig alias 穿透其他包。

## 接口与装配

端口用 `interface`，adapter 实现，由 server 经受限公开工厂注入。概念不依赖其他概念，外部身份用泛型或 branded ID。syncs 公开应用 DTO；gateway 仅调用 syncs，外部协议与 JSON 映射留在 gateway。

规则实现为具名函数/对象，保留输出 case、flow 与对象绑定。async mediator 或规则引擎均按正文兑现匹配和恢复；选引擎时核验实际版本能力，不能由事件监听或 Promise 链推定完整同步语义。

## 验证

```bash
pnpm --filter '@app/reservation...' build
pnpm --filter @app/reservation test
pnpm --filter @app/syncs test
pnpm -r build
pnpm -r test
```

名称与脚本按包清单替换；定向构建含依赖闭包。用 dependency-cruiser 或等价工具检查概念零互引、gateway 仅依赖 syncs/shared、源码层次与公开入口；server 的多模块装配单独允许。类型检查通过不证明访问合法，包 exports 也不阻止所有源码级绕过。

依据：[pnpm workspace](https://pnpm.io/workspaces)、
[筛选依赖闭包](https://pnpm.io/filtering)、
[TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html)、
[Node package exports](https://nodejs.org/api/packages.html#package-entry-points)。
