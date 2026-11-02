# Composition

Use the [specification format](spec-format.md) for notation and execution semantics.

| Scenario evidence | Candidate change |
| --- | --- |
| Required coordination is missing | Tighten synchronization. |
| Automation removes needed manual control | Loosen synchronization or make it configurable. |
| Combined behavior changes a concept's purpose | Recheck its boundary and contract. |

Coordination actions such as access or notify still need contracts.
Logs and queues qualify only with independent purposes and complete behavior.

## Diagram

Keep one node per rule, all conjunctive `when` inputs, all `then` targets, and separate `where` reads.
Simplified arrows MUST retain the rule name and conjunction.
Loops need termination or controlled continuation.
Engineering cutoffs MUST be observable.

## Product subsets

An intrinsic dependency embeds another concept's definition; replace it with a type parameter or external coordination.
An extrinsic dependency comes from product requirements: `A → B` means retaining A requires B in this product.
Code coupling or type instantiation alone does not prove it.
Keep product dependencies separate from the synchronization diagram.

Each subset MUST have a purpose, dependency closure, entries, valid remaining rules, and resources.
Include or exclude a product-dependency cycle together.
