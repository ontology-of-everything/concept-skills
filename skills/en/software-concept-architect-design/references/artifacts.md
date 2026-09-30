# Design artifacts

Confirm the three alignment sections with the user, then write the design record from those same
facts. Pending concepts, scenarios, and subsets do not enter confirmed Concepts or Synchronizations.

## Alignment

### Concept inventory

| Concept | Purpose | OP | Familiar or new | User-visible state | Confirmation |
| --- | --- | --- | --- | --- | --- |
| <name> | <one need> | <archetypal scenario: what the user sees after the actions> | familiar / variant / new | <state a user can explain> | confirmed / pending |

### Application purpose and scenarios

<beneficiaries, application purpose, current state, desired outcome, constraints; source / inference / open; confirmed / pending>

<If <observable condition>, then <observable result>. Concepts: <names>. Synchronizations: <rule names>. Misfit: <counterexample, or leave empty>. Confirmation: confirmed / pending>

### Dependencies and subsets

Explanation order: <concepts explained before those that depend on them>

<A → B means including A requires B>

Viable subsets: <concepts in each subset>

MVP: <subset, and whether its entry, remaining rules, and external resources are satisfied>

Confirmation: confirmed / pending

## Design record

### Concepts

<purpose, state, actions, OP, and optional queries/notes per spec-format.md, for each confirmed concept>

Argument: <why the contract supports the OP and the result fulfills the purpose; counterexamples or open points>

Seam: <decision and reasons for each of the eight criteria>

### Synchronizations

<app / include / sync, grouped by entry or rule responsibility, tied to a confirmed application scenario and purpose>

### Synchronization diagram

<when → rule node → then; where reads marked separately>

<Checks composition only. Keep multi-source conjunctions, multiple targets, and query edges here; this is not the product dependency graph>

### Exclusions and open decisions

<candidate / action / assumption, conclusion, source, and impact. Pending items belong here>
