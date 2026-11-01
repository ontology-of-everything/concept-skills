# Data quality specification

Use PIPELINE to describe sources, transformations, outputs, checkable quality, triggers, and public
read/write boundaries. Cross-concept coordination still belongs in SYNCS.

```markdown
# pipeline: <name>

## purpose

<quality or transformation outcome>
## sources
<source, ownership, grain, contract>
## stages
### <stage> [tool: <project tool>]
<input → transform → output; failure behavior>
## outputs
<artifact, schema, owner, consumer>
## invariants
<checkable quality rules>
## triggers
<event/schedule/manual entry>
## data boundary
<allowed reads/writes and prohibited crossings>
```

Backfill from actual commands, workflow files, schemas, queries/joins, and checks. Name data owners
or external sources and the public interfaces used. Cross-concept work stays in composition;
a concept's storage adapter may use SQL, but a pipeline gains no private cross-concept access.

A rule such as `score in [-1, 1]` is checkable; "clean data" is not. Use a row-count bound only when
the contract requires it. Choose meaningful stages and actual tools, not one stage per small operation.
Record each stage's inputs, outputs, failure behavior, and checks. New flows also need append/refresh
and idempotency behavior. Mark missing controls open rather than inventing them.

Colocate a concept-owned PIPELINE with CONCEPT; place cross-concept pipelines in composition.
Sources, stages, outputs, and invariants must resolve to code or an explicit intended contract.
Discovery lists candidates only; pure coordination belongs in sync mode.
