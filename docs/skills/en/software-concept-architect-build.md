# Software Concept Architect · Build

> Turn Models into Independent Modules

`software-concept-architect-build` maps a confirmed concept model to independent modules and named, granular
synchronization rules, with colocated specifications and behavioral and dependency tests.

Default to a modular monolith: independent build/test units, Clean Architecture internally, a syncs
module, and one gateway, assembled in one process. Read the
[architecture example](../../../skills/en/software-concept-architect-build/references/architecture.md)
when defining structure, then only the selected Rust/Axum, Java/Spring, or TypeScript reference.

- Skill: [SKILL.md](../../../skills/en/software-concept-architect-build/SKILL.md)
- Chinese: [`software-concept-architect-build-cn`](../cn/software-concept-architect-build-cn.md)

```bash
npx skills add ontology-of-everything/concept-skills --skill software-concept-architect-build
```

## 1.1.0 - 2026-10-08

Default to independently built Clean Architecture modules in one process, with a separate synchronization module and unified gateway.

## 2026-09-25 Revision

Synchronization rules remain independently identifiable and verifiable. Composition guidance now
lives in SKILL.md, with action/query/request distinctions and engineering choices checked against
Jackson’s 2026 papers.

## 2026-09-19 Revision

Synchronization may restrict behavior, never extend a concept contract. Check each concept’s actions,
state changes, and outputs in composed executions; assess purpose failure separately. Condensed
repeated definitions and guidance.

## ClawHub

[Software Concept Architect · Build — Turn Models into Independent Modules](https://clawhub.ai/agenticweb4/skills/en/software-concept-architect-build)
