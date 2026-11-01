# Synchronization specification

Create or backfill causal rules under [the contract](spec-format.md). Match completed actions,
query public state, and call declared actions with bound values. Documentation groups are not
runtime flow identity; each request, timer, or message needs an explicit entry contract.

## Establish the rule

Start from application purpose and scenarios. Identify entry completions, success/error cases,
bindings, outputs, response obligations, object/request correlation, partial completion, replay,
and loops. One rule states one explainable decision. Actions enforce invariants atomically;
a query cannot replace a write-time check.

For backfill, trace handlers, registration, mediators, and adapters to public actions. Mark inferred
intent and defects. Direct concept calls or private SQL access cannot become valid syncs merely by
transcription. Pure data transformation belongs in PIPELINE; difficult model choices go to design.

## Check completion

Use one SYNCS per composition module, grouping by entry/responsibility with unique rule identities.
Resolve includes, instances, action/query signatures, and call parameters. Preserve zero/many-result
behavior, request isolation, and all reachable response/retry/compensation/ignore decisions.
Loops need termination or controlled continuation; depth limits are optional safeguards.

Report rule count, scenario coverage, boundary findings, and unknowns. Missing application purpose
stays open. Preserve conjunctive triggers, multiple targets, and query edges in diagrams, and retain
behavior when migrating. Hooks list SYNCS but do not check its semantics.
