# Synchronization Specification

Use `sync` to create or backfill causal application rules after reading `spec-format.md`.

- `when` matches completed actions and selected inputs/outputs. Multiple patterns are conjunctive
  within one causal flow.
- `where` reads public abstract state or declared queries and produces zero, one, or many binding
  sets. Zero emits nothing and does not imply an error or response.
- `then` invokes declared actions once per binding set using only constants or bound values. Split
  dependencies on future outputs into another rule.
- Runtime flow is one causal instance rooted in an external event. `// flow:` is documentation
  grouping, not a token. Requesting, timers, and messages each need explicit entry contracts.

## Work

Starting from application purpose and end-to-end scenarios, identify entry completions, required
coordination, success/error discrimination, bindings, outputs, correlation IDs, response
obligations, concurrency, replay, partial completion, and loops. One rule expresses one explainable
decision.

For backfill, trace the mediator/engine and interface adapters to actual public actions. Preserve
observed defects and mark inferred intent. Never translate direct concept calls into acceptable
synchronization without reporting the independence violation.

Completion requires resolvable includes and instances, real action/query signatures, bound `then`
inputs, explicit zero/many-match behavior where relevant, success/refusal/failure response coverage,
request correlation, replay strategy, and a diagram that preserves conjunction and query edges.
