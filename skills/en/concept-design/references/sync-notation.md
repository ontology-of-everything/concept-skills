# Composition checks

Use [the specification contract](spec-format.md) for notation, correlation, and failure semantics.
This page checks design choices; [the reservation example](example-reserving.md) shows rule splitting.

## Choose coordination

| Observation | Decision |
| --- | --- |
| Required coordination never occurs | Tighten synchronization by adding the missing rule. |
| Automation removes needed manual control | Loosen synchronization or make it configurable. |
| Combined behavior changes a concept's purpose | Recheck its boundary and contract. |
| A flow has many participants | Inspect the scenario; length alone does not justify a new concept. |

Base each decision on application purpose and a concrete scenario. An action reserved for
coordination, such as access or notify, still needs its own contract. Logs and queues qualify as
concepts only with an independent purpose and complete behavior of their own.

## Draw and check rules

Keep one node per rule, all required when inputs, all then targets, and separate where reads.
Simplified arrows retain the rule name and conjunction. They do not express product dependencies.
A loop needs termination or controlled continuation; make any engineering cutoff observable.

## Dependencies and subsets

An intrinsic dependency puts another concept's definition inside this one. Replace it with a type
parameter or move the coordination into syncs. An extrinsic dependency is product-specific:
`A → B` means this application needs B when retaining A. Record it in alignment and the overall PRD.

Code coupling does not prove product dependency. Check each subset's purpose, dependency closure,
entries, remaining rules, and resources. Include or exclude a product-dependency cycle together;
grouping a cycle alone does not make it deliverable.
