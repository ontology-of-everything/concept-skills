# Phase 3: Repository YAML and shared field semantics

Repository YAML is a local semantic profile, not a universal ontology schema. Use the project's
existing schema when supplied and record its version. Otherwise use this compact record shape:

```yaml
name: Sales
schema_version: "1"
type: semantic_ontology
facts:
  - name: Order
    grain: one confirmed order at creation
    source_operations: [ListOrders]
    identity: {key: order_id, scope: tenant}
    time: {field: placed_at, meaning: creation, timezone: UTC}
    dimensions: [Store]
    measures:
      - name: order_amount
        source_field: amount
        unit: USD
        basis: gross order amount before refunds
        additivity: additive
        aggregation_scope: unique orders in one currency
    evidence: [contract-v1#ListOrders, business-definitions#order]
evidence_boundary: [No refund or recognized-revenue inference]
```

This is illustrative approved input, not evidence for fields in another source.

A bundle has one `semantic_catalog`: name, purpose, evidence boundary, required context, and
`entry_points` mapping supported questions to model files and source operations. It links models;
it does not repeat their definitions. Two or more bundles may have a thin parent index.

A fact defines source operations, business grain, identity/scope, temporal meaning, dimensions,
measures, and evidence. `primary|child` and parent references are optional local organization,
not required semantic kinds. At different grains, aggregate before joining or specify an evidenced
allocation; a one-to-many join must not duplicate header measures.

A dimension defines name, key with scope, attributes, source, join cardinality, and historical
interpretation where needed. Use `dimension` for a local dimension, `conformed_dimension` for
semantically consistent cross-fact reuse, and `snowflake_dimension` for a normalized hierarchy
with declared parent and cardinality. A degenerate key stays on the fact. A matching field name
is insufficient for conformance: compare meaning, key domain, tenant, time/version, and attributes.

A measure is a quantity at the declared fact grain. It declares source/calculation, unit, relevant
currency or basis, additivity by axis, and allowed aggregation scope. A metric is a named business
calculation over measures. Record its formula, source measures, filters, time/window, and aggregation
scope in an optional `metrics` list; distinguish this from the fact-level `measures` list. Counts need a deduplication identity; ratios/averages need
valid components; snapshots generally cannot be summed across time. State null, empty, correction,
and deleted-record behavior when it affects the answer. Mark missing meaning open.

Keep source-field mappings in the model and link executable enum/value/command catalogs instead
of duplicating them. Every choice must trace to evidence and an approved decision or explicit
scope exclusion. The same semantics govern OKF output.
