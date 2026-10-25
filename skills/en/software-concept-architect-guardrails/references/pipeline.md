# Data Quality Specification

Use `pipeline` for a data flow with sources, stages, outputs, invariants, triggers, and a data
boundary. A PIPELINE supplements rather than replaces concept behavior or synchronization.

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

Backfill from actual commands, workflow files, schemas, and checks. Mark missing quality controls
rather than inventing them. Keep a concept-owned pipeline beside its CONCEPT; place cross-concept
pipelines in the composition layer. Completion requires every stage's inputs/outputs, failure
behavior, ownership, and invariants to resolve, with project-native validation commands when
available.
