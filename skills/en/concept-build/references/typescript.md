# TypeScript

Map [the architecture](architecture.md) to pnpm workspace packages. Each concept, composition, api,
and shared package has its own build/test entry; server assembles them.

## Packages and exports

```text
pnpm-workspace.yaml
apps/server/                        # package.json, tsconfig.json, src/main.ts
modules/
  concepts/reservation/              # package.json, tsconfig.json, CONCEPT.md
  concepts/payment/                 # same
  composition/                        # package.json, tsconfig.json, SYNCS.md
    src/syncs/                      # named synchronization rules; not a build unit
  api/                                # package.json, tsconfig.json, HTTP/DTO
  shared/                             # package.json, tsconfig.json, foundational types
```

Include actual packages under `apps/*`, `modules/concepts/*`, and `modules/*`; update globs for groups.
Declare dependencies and scripts in each package. Export public contracts and restricted factories
from `src/index.ts`. Use ports for facilities and add domain/application layers only when needed.

ESM package example:

```json
{
  "name": "@app/api",
  "type": "module",
  "exports": {".": {"types": "./dist/index.d.ts", "import": "./dist/index.js"}},
  "dependencies": {"@app/composition": "workspace:*"},
  "scripts": {"build": "tsc -b"}
}
```

Use project references, `composite`, and declaration output to build the dependency graph.
Workspace membership alone is insufficient. Package exports restrict consumers; source checks must
also prevent relative-path and tsconfig-alias access to another package's internals.

## Interfaces and assembly

Inner code declares port interfaces; adapters implement them and server injects them through public
factories. External identities use generic or branded types without concept-to-concept imports.
Composition owns its application DTOs; api maps protocol/JSON data and calls composition.
Implement named rule functions or objects under [the execution contract](execution.md).
Listeners and Promise chains alone do not establish matching or recovery guarantees.

## Checks

```bash
pnpm --filter '@app/reservation...' build
pnpm --filter @app/reservation test
pnpm --filter @app/composition test
pnpm -r build
pnpm -r test
```

Use actual package names and scripts. Targeted builds include dependencies. Check package dependencies,
source layers, public entries, concept independence, api access to composition/shared, and server's
assembly access with dependency-cruiser or equivalent rules. Type checking and exports alone do not
prove these boundaries.

Sources: [pnpm workspaces](https://pnpm.io/workspaces), [filtering](https://pnpm.io/filtering),
[TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html),
[Node exports](https://nodejs.org/api/packages.html#package-entry-points).
