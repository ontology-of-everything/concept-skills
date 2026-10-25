# Scaling Groups and Packages

Scale only to solve observed navigation, build, or ownership pain. Baseline: [architecture](architecture.md).

| Decision | Rule |
| --- | --- |
| Groups | combine product-dependency clusters, shared flow participation, and team ownership; validate independent delivery separately |
| Build seams | default to `modules/concepts/<group>/<concept>/`, one build unit per concept; split workspaces or parent builds only for real build/team needs and update boundary checks |
| Sync packages | default to one independent syncs module with flow groups; split build units only for an observed need; keep rule identity unique; place cross-group flows with the owning external entry |
| Specifications | keep CONCEPT with modules and one SYNCS per sync package; update PRD index and diagrams; product dependencies stay in the overall PRD |

After grouping, re-check dependency closure, entry points, remaining rules, external resources,
build flags, and release ownership. Directory nesting alone neither creates a module nor proves a
deliverable subset.
