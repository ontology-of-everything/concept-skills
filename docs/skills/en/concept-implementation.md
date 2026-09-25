# Concept Implementation

`concept-implementation` maps a confirmed concept model to independent modules and named, granular
synchronization rules, with colocated specifications and behavioral and dependency tests.

- Skill: [SKILL.md](../../../skills/en/concept-implementation/SKILL.md)
- Chinese: [`concept-implementation-cn`](concept-implementation-cn.md)

```bash
npx skills add ontology-of-everything/concept-skills --skill concept-implementation
```

## 2026-09-25 Revision

Synchronization rules remain independently identifiable and verifiable. Composition guidance now
lives in SKILL.md, with action/query/request distinctions and engineering choices checked against
Jackson’s 2026 papers.

## 2026-09-19 Revision

Synchronization may restrict behavior, never extend a concept contract. Check each concept’s actions,
state changes, and outputs in composed executions; assess purpose failure separately. Condensed
repeated definitions and guidance.
