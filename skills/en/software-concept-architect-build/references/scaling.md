# Scaling Groups and Packages

Scale only to solve observed navigation, build, or ownership pain.

| Decision       | Rule                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Groups         | combine product-dependency clusters, shared flow participation, and team ownership; validate independent delivery separately          |
| Build seams    | default to `concepts/<group>/<concept>/`; split workspaces or parent builds only for real build/team needs and update boundary checks |
| Sync packages  | split by flow responsibility; keep rule identity unique; place cross-group flows with the owning external entry                       |
| Specifications | keep CONCEPT with modules and one SYNCS per sync package; update PRD index and diagrams; product dependencies stay in the overall PRD |

After grouping, re-check dependency closure, entry points, remaining rules, external resources,
build flags, and release ownership. Directory nesting alone neither creates a module nor proves a
deliverable subset.
