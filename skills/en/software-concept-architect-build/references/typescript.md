# TypeScript

Read for TypeScript targets. [Architecture](architecture.md) owns module relationships and examples.
Use a pnpm workspace with independently buildable/testable packages for each concept, syncs, gateway,
and shared; server assembles and starts them.

## Project skeleton

```text
pnpm-workspace.yaml
apps/server/                        # package.json, tsconfig.json, src/main.ts
modules/
  concepts/reservation/              # package.json, tsconfig.json, CONCEPT.md
  concepts/payment/                 # same
  syncs/                            # package.json, tsconfig.json, SYNCS.md
  gateway/                          # package.json, tsconfig.json, HTTP/DTO
  shared/                           # package.json, tsconfig.json, foundational types
```

Include actual packages under `apps/*`, `modules/concepts/*`, and `modules/*`; update globs when adding
groups. Each package declares dependencies and build/test scripts. Use `src/index.ts`, `api.ts`,
`domain/`, `application/`, and `adapter/` internally. Export only business APIs, result types, and
necessary assembly entries from `index.ts`.

Manifest fragment for a project using ESM and declarations:

```json
{
  "name": "@app/gateway",
  "type": "module",
  "exports": {".": {"types": "./dist/index.d.ts", "import": "./dist/index.js"}},
  "dependencies": {"@app/syncs": "workspace:*"},
  "scripts": {"build": "tsc -b"}
}
```

Configure TypeScript project references, `composite`, and declaration output so builds follow the
dependency graph. Workspace membership alone does not prove independent compilation. Package
`exports` limits consumer entry points; source checks also prohibit relative-path or tsconfig-alias
access into another package.

## Interfaces and assembly

Inner ports are interfaces, implemented by adapters and injected through restricted public factories
by server. Concepts never depend on other concepts; use generic/branded external identities. Syncs
exports application DTOs; gateway invokes syncs and owns external protocol/JSON mapping.

Implement named rule functions/objects preserving output cases, flow correlation, and object
bindings. Async mediators and engines follow the entrypoint's matching/recovery contract. Verify an
engine's installed capabilities; event listeners or Promise chains do not imply full synchronization semantics.

## Verification

```bash
pnpm --filter '@app/reservation...' build
pnpm --filter @app/reservation test
pnpm --filter @app/syncs test
pnpm -r build
pnpm -r test
```

Substitute actual package names/scripts; targeted builds include dependency closure. Use
dependency-cruiser or equivalent checks for zero concept dependencies, gateway access limited to
syncs/shared, source layers, and public entries. Allow server's multi-module assembly separately.
Type checking does not establish permitted access; exports alone does not stop every source-level bypass.

Sources: [pnpm workspaces](https://pnpm.io/workspaces), [dependency filtering](https://pnpm.io/filtering),
[TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html),
[Node package exports](https://nodejs.org/api/packages.html#package-entry-points).
