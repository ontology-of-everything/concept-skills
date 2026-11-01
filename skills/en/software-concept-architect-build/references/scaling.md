# Groups and packages

Group only to solve observed navigation, build, or ownership problems. Follow [the architecture](architecture.md);
grouping never permits concept-to-concept references.

| Decision | Rule |
| --- | --- |
| Groups | Use product dependencies, shared scenarios, or team ownership; verify delivery separately. |
| Build units | When useful, use modules/concepts/group/concept with one unit per concept. Split workspaces/parent builds only for actual needs; update dependency checks. |
| Composition | Default to one module with rule groups. Split only for distinct responsibilities; keep rule identity unique. Cross-group flows follow their external entry's owner. |
| Specifications | Colocate CONCEPT and one SYNCS per composition module; update PRD indexes and diagrams. Keep product dependencies in the overall PRD. |

After grouping, verify purpose, dependencies, entries, rules, resources, build flags, and release
ownership. Keep cross-concept policy in composition and server assembly unified. Directory nesting
alone establishes neither a module nor a deliverable subset.
