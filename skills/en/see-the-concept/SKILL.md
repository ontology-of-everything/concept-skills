---
name: see-the-concept
description: "Use only when the user explicitly requests this skill. Explain and examine software concept designs using source evidence and clear visuals. Use for concept boundaries, behavior, composition, synchronization, dependencies, and UI mapping."
metadata:
  language: en
  translation_of: see-the-concept-cn
  version: "0.1.4"
---

# See the Concept

**Use source evidence to help learners understand and examine software concept designs.** Be a technically knowledgeable friend to a beginner: purpose first, then mechanism; explain new terms as they appear. Keep the preamble short and choose the smallest view that explains the point.

**Trace the code first.** Follow project guidance and real entrypoints through state, actions, callers, coordination, and UI queries; check tests, configuration, and error paths. Cite files, symbols, and lines for key implementation claims. Classes and files are not automatically concepts. Documents express intent; source establishes implementation. Identify conflicts, inferences, and unknowns. Without source, explain only the supplied design, without claiming implementation verification.

The sketches below illustrate form. **Replace names, values, and behavior with evidence from the current project.** Choose what answers the question; rarely use everything.

- **Show value with purpose and an operational principle (OP).** Purpose explains why it is needed; an OP shows how typical actions achieve that purpose.

```text
Concept: <name>
Purpose: <value provided>
OP: perform <actions>; under <conditions>, obtain <useful result>
```

“Actions not buttons.” — Daniel Jackson, Operational principles. An OP neither enumerates every behavior nor becomes a click tutorial.

- **Show behavior with before/after state or action specifications.** Include enabling conditions, changes, preserved information, and outputs.

```text
Action: <name, inputs, conditions>
State item       Before       After       Reason
<project field>  <old value>  <new value> <action effect>
Preserved: <other state>; outputs: <results>
```

State, action conditions, and effects form a **state-machine model**. Use transition graphs for few states and tables or specifications for complex ones. Queries may leave state unchanged. Describe ordinary CRUD and omissions from the materials.

- **Show state associations with extended ER diagrams.** Draw sets, named relations, multiplicities, and subsets, then concrete project values.

```text
<set A> ── <relation, multiplicity> ── <set B>
<object> ── <relation> ── <value>
<subset> belongs to <set>
```

“The state is the concept’s memory.” — Daniel Jackson, Concept state. State supports behavior, not every fact in the domain; these relation lines do not trigger actions.

- **Show composition with type binding and instance groups.** Binding fills generic slots; grouping shows shared and independent state.

```text
<Concept><Type parameter> ···binds to··· <actual project type>
Application
├── <shared instance>: <state>
└── Grouped by <actual index>
    ├── <instance A>: <independent state>
    └── <instance B>: <independent state>
```

“The concept stands by itself, without reference to other concepts.” — Daniel Jackson, Concept modularity. **Composition also includes synchronization.** Instances do not form a call graph; logical sharing does not guarantee shared storage. Omit structures that do not exist.

- **Show action coordination with synchronization rules and parameter sources.** Synchronization is a composition mechanism, not automatically a callback or serial call chain.

```text
Participating actions: <concepts and actions>
Conditions: <conditions or guards>
Required values: <value> from <state, action inputs, or outputs>
Calculation: <how arguments are derived>
Coordinated actions: <other actions, arguments, and output destinations>
```

Add data flow for complex inputs and sequence diagrams only for established order. If evidence shows only calls, use a call tree. Follow target execution semantics; flag unknown ordering, failures, and transaction guarantees.

- **Show required functional combinations with a dependency diagram.** These application dependencies differ from state relations inside a concept.

```text
A ──requires──→ B
Retaining A in this application requires B
Check: <viable subsets> / <invalid subsets and reasons>
```

Simulate removing B to check the consequence. Dependence is not triggering or calling; application dependence does not require one concept's definition to reference another.

- **Show UI mapping by labeling controls with actions and display regions with queries.** Put correspondences beside a wireframe, adding involved state when needed.

```text
<control> ──invokes──→ <concept action>
<display region> ──queries──→ <concept state or derived value>
```

Several refreshes may be query reevaluation rather than additional synchronization. Check that the UI supports the OP and conveys concepts faithfully. Flag unverified queries; omit UI mapping without a UI.

- **Show implementation by pairing design with actual source.** Locate files, symbols, and lines; include enough code to explain the point.

```text
Left: source, line numbers, highlighting    Right: plain-language explanation
<actual source line>                       <what it does and its design role>
```

Use the explanation's language and stack paired units on narrow screens. Explain pseudocode line by line too, labeling it “illustrative logic.” Concepts and files need not match one to one. Source correspondence checks implementation; it is not the definition of UI mapping.

- **Show design changes with before/after views or diffs.** Show only changes when context is established; show the whole block when omission would hide ownership or ordering.

```text
Current                    Proposed                  Evidence and effect
<existing structure>       <suggested change>        <basis, benefit, cost>
```

Check mixed purposes (specificity), needless departures from familiar behavior (familiarity), and preservation of concept meanings in composition (integrity), along with sufficient behavior and independence. **Proposals are not existing facts.**

- **Show the whole design or complex interaction with concept boundaries or focused HTML.** Put state and actions inside boxes; highlight one project scenario and return to the overview.

```text
<concept boundary: state + actions>    <concept boundary: state + actions>
Connect only from evidence; placement and teaching order add no system edges.
```

For this integrated notation: solid lines without arrowheads mean state relations; solid arrows mean action effects; dashed arrows mean synchronization; dotted lines mean type binding; named pins mean dynamic subsets. Dependency diagrams need their own legend. Use SVG/HTML or labels when rendering is unclear. Mark omitted state, multiplicities, syncs, and instances.

## Presentation and delivery

**Make it feel like an infographic.** Place views beside brief explanations of cause and effect. Keep everyday analogies faithful and “Aha!” moments and humor brief. The default view should stand alone. Interaction should show actions, changes, and explanations together, with stepping, comparison, and reset as needed; retain selection across views.

**Make it stunning and readable.** Use aged-paper cream, warm gray, and warm shadows, avoiding cold white, blue pages, and black shadows. Use `#1E1E2E` code panels and Catppuccin-style highlighting. Support keyboard, touch, visible focus, and text alongside highlights; essential information must not depend on hover. Make animation user-triggered, skippable, and respectful of reduced-motion settings.

For courses, deliver a directory. **A single-file skill does not mean a single-file course.**

```text
course/
├── index.html     # assembled entrypoint
├── styles.css     # shared styles
├── main.js        # shared interaction
├── modules/       # independently authored sections
└── assets/        # local resources
```

Reuse styles and scripts and update affected sections only. Assemble content into `index.html` before delivery, without module fetches, remote resources, installation, or a server. Open the result offline and check layout, navigation, interactions, reset, keyboard, narrow screens, sources, and paired explanations.

**Demonstration is not runtime evidence.** Teaching steps do not prove execution order; reset restores only simulation state. Unexecuted tests or unopened artifacts cannot establish verification. Report what remains unverified.
