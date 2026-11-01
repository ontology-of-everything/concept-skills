# Architecture map

Derive navigation from CONCEPT, SYNCS, PIPELINE, the overall PRD, and staged indexes. No specifications
means a coverage gap, not an empty diagram. Maps are not authoritative contracts or proof of correct code.

| View | Source and meaning |
| --- | --- |
| Concept index | Purpose and link to the current specification. |
| Sync graph | One node per rule, all conjunctive when inputs, then targets, and separate where reads; preserve cases and object correlation. |
| Product dependencies | Requirements in the overall PRD, never inferred from sync/code edges. |
| Data flow | PIPELINE owners, sources, outputs, stages, and public read/write interfaces. |
| Coverage | Every node's source, missing internal specifications, external references, and unverified material. |

Count each authoritative source once. Keep unresolved and cross-scope references visible; a missing
internal specification is not an external participant. Rebuild from content, write only changes,
and preserve human notes. Timestamps alone cannot justify skipping a rebuild; that needs a complete
source set and content fingerprints.

Use stable ASCII IDs, escaped labels, and deterministic name/path order. Visual groups do not create
architecture layers. Preserve all members of dependency groups, excluded actions, and cross-scope
edges. Mark loop control. Report node/rule counts, changed relations, and gaps; without a code census,
report specification counts only. Every relation must claim no more than its source supports.
