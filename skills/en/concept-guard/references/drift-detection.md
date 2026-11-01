# Drift detection

Default to read-only comparison of confirmed contracts and current implementation. History is an
explicit opt-in; drift never repairs specifications or code.

## Evidence and boundaries

Read specifications, PRD/staged indexes, related rules, code, migrations/schema, and tests.
Inspect definitions after searching. Read ancestor content before assuming coverage. Missing or
unscanned implementation stays unverified.

Check confirmed architecture separately from semantic drift. Under the default, verify independent
builds, one-process assembly, api/composition/concept boundaries, concept independence, ports/adapters,
and Clean layers where used. Server may use public factories. Do not impose defaults on an existing
project or treat folders/acyclicity as boundary proof.

## Categories

| Contract | Difference | Default severity |
| --- | --- | --- |
| CONCEPT | Undeclared public action, changed signature/result, observable new state, or undocumented contract parameter | Medium |
| CONCEPT | Declared action absent from all relevant implementations | High |
| CONCEPT | Private access, direct concept calls, shared mutable state, or excluded action still reachable | High |
| CONCEPT | Core definition depends on another concept or contains legacy boundary sections | Medium |
| CONCEPT | OP lacks a representative test | Medium, verification gap |
| CONCEPT | Recorded gap resolved by current implementation | Low |
| PIPELINE | Missing stage/source or changed data contract | Medium |
| PIPELINE | Contradictory invariant or cross-concept private access | High |
| SYNCS | Missing rule or changed trigger | Medium |
| SYNCS | Removed rule, undeclared participant, or changed binding/effect | High |
| Maps | Existing diagram contradicts its rules | Medium |
| References | Missing action/query, wrong signature/result, or invalid type binding | High |
| References | Internal concept has neither specification nor index explanation | Medium |

Check pipeline order, data contracts, triggers, quality, and public interfaces. For syncs, check cases,
query cardinality, calls, correlation, failure, replay, and loops. Resolve external-entry signatures;
Requesting needs no synthetic CONCEPT. Product dependencies come from PRD requirements; a sync diagram
may live there alone.

## Calibrate findings

Critical needs evidence of authorization bypass, data destruction, or core unavailability. High is a clear
violation; Medium an impactful omission; Low local maintenance. Explain adjustments to defaults.
Medium-or-higher findings need current locations; merge one root cause across affected paths.

Silence does not prove prohibition. Private helpers/caches, naming maps, and behavior-preserving
Result/async wrappers are not drift by themselves. Public state reads are allowed. A missing OP test
is a verification gap; failed purpose fulfillment needs a separate counterexample. Documenting a
concept call does not restore independence. Accept legacy notation under [the contract](spec-format.md).

## Report and optional history

Report scope/versions, counts, each category as passed/found/unverified, contract/code locations,
impact, and repair steps. Reconcile cross-spec references after batching. Route model defects to
design, stale documents to PRD/spec maintenance, and code violations to build. Present unresolved
behavioral choices rather than following code by default. Repairs use the appropriate writing mode.

Only on request, append `.claude/wyx-drift-history.jsonl`:

```json
{"ts":"<ISO-8601>","action":"detect","specs_scanned":0,"specs_with_drift":0,"critical":0,"high":0,"medium":0,"low":0,"low_by_spec":{},"path":"<scope>"}
{"ts":"<ISO-8601>","action":"fix","specs_fixed":0,"specs_remaining":0,"ref_ts":"<detect timestamp>"}
```

Use measured counts. Count a specification fixed only when no findings remain; link fix to detect
without rewriting history. Records without action mean detect. The runtime reads the last snapshot;
a scoped result does not establish whole-project status. Only rescanning clears stale warnings.
Never fabricate zero drift or escalate from Low counts alone.
