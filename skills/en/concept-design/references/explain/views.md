# Views and evidence

| Question | Evidence to retain |
| --- | --- |
| Why is this needed? | Purpose, scenario, OP assumptions, and result |
| How does state change? | Inputs, conditions, before/after state, unchanged information, and outputs |
| How is data related? | Named relations, types, cardinalities, and instances |
| How do concepts work together? | Instances, type bindings, and synchronization relations from the [map format](../map-format.md) |
| Why are actions ordered? | Source-backed order; show only calls when only calls are established |
| What can be removed? | Requirement-backed purpose dependencies and viable subsets |
| What does the UI do? | Controls to actions, display regions to queries |
| How do implementations or proposals differ? | Source locations, evidence, and behavioral impact |

Use relation and action tables for complex state.
Returned errors are not automatically states.
Concepts and files need not correspond one-to-one; shared instances do not establish shared storage.
Omit UI views when no UI exists; label unverified queries.
Source excerpts MUST preserve actual text and line numbers; label pseudocode illustrative.
