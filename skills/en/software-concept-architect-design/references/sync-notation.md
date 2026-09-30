# Composition Checks

How to write a sync, including flow, failure, and replay, is in `spec-format.md`. This file only
judges design choices. See `example-reserving.md` for splitting rules by data dependency.

## Whether to synchronize

- **Under-synchronization:** a coordination that should happen does not. Tighten by adding the rule.
- **Over-synchronization:** automation removes manual control the user needs. Loosen it, or make it
  configurable.
- Decide from the application purpose and a concrete scenario.
- A **placeholder action**, such as access or notify, exists so another action can synchronize with
  it. It still needs its own contract.
- **Synergy** is value the composition adds beyond either concept alone. If that rewrites a
  concept's original purpose, review the seam against the qualification standard.
- Many participants or a long flow only mean the scenario is complex. Revisit a concept boundary
  only when there is an independent purpose and business state of its own. Logs and queues are not
  concepts.

## Synchronization diagram

Each sync is one rule node: multiple `when` edges in, multiple `then` edges out, and `where` marked
as a read. A simplified A→B arrow keeps the rule name and states whether the `when` patterns must
all hold. This diagram is not the product dependency.

A loop needs a termination condition, or a reason it continues under control. If an engineering cap
cuts it off, that cutoff must be visible.

## Dependencies and subsets

- **Intrinsic:** the concept's own definition depends on another concept. Use a type parameter, or
  move the link into a sync. Do not leave it in the concept definition.
- **Extrinsic:** in this application, including A makes sense only together with B. Record `A → B`
  in the alignment's dependencies and subsets. The PRD transcription puts it in the overall PRD.
- Code coupling does not prove a product dependency. Besides the dependency closure, check purpose,
  entry, remaining syncs, and external resources.
- Concepts in one dependency cycle are included together or excluded together. Grouping them is not
  itself a deliverable subset.
