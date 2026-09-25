# TypeScript Implementation

These are optional engineering mappings. Separate packages, ports/adapters, layers, and protocol placement are not concept-theory requirements. Requesting may encapsulate protocols in its implementation.

Use a pnpm workspace with one package per concept:

```text
packages/
  concepts/user/      # domain.ts, actions.ts, ports.ts, adapters/
  concepts/password/
  syncs/              # named rules grouped by flow responsibility
  app/                # wiring and DTO/protocol adapters
  shared-kernel/      # foundational types only
```

Ports are interfaces, adapters implement them, and the composition root injects them. A concept
package declares no other concept package dependency. Use generics or branded IDs for concept type
parameters. Nested groups update workspace globs without weakening package rules.

For procedural synchronization, preserve named rule boundaries as functions or rule objects, optionally
grouped by flow. The async mediator connects rules according to [the skill entrypoint](../SKILL.md) while
preserving causal dependencies and allowed concurrency. For a declarative engine such as
[LegibleSync](https://github.com/mastepanoski/legiblesync), verify the installed version's
completion matching, conjunctive triggers, bindings, flow isolation, and persistence rather than
trusting examples.

Use dependency-cruiser in CI to prohibit concept-to-concept dependencies, allow only sync/app to
reference several concepts, and keep protocol libraries out of domain code. eslint-plugin-boundaries
may provide the same feedback in the editor.
