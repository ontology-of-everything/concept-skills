# Architecture Map

Use `map` to derive navigation artifacts from authoritative CONCEPT, SYNCS, PIPELINE, and overall
PRD files. Maps never become the source of truth.

Include a concept index with purpose and specification link; a synchronization graph with rule
nodes, conjunctive `when` edges, `where` query edges, and `then` calls; a product-dependency matrix
sourced only from the overall PRD; data-flow paths sourced from PIPELINE; and coverage linking every
node back to its source.

Do not infer product dependencies from synchronization or code edges. Preserve multi-source and
multi-target rules rather than flattening them into misleading pairwise arrows. Mark unresolved
references and excluded actions. Rebuild from content after specification changes; timestamps alone
never prove freshness.

Completion requires every map node and edge to resolve to a current source, every
concept/sync/pipeline to be represented or explicitly excluded, and no relation to claim stronger
semantics than its source.
