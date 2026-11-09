# Write the PRD and specifications

Transcribe confirmed behavior without redesign.
Preserve assumptions, human notes, rejected options, confirmation sources, and the arguments connecting purpose, OP, and contract with their gaps.
Code inspection may verify locations and index facts; code differences MUST NOT create requirements.

1. Read the confirmed model and requirement sources.
2. Assign one authoritative location per model element using the table below.
3. Write contracts and rules in the [specification format](../../shared/model/spec-format.md).
   Preserve signatures, state effects, result cases, and correlation.
   Include the default [execution constraints](../../shared/model/spec-format.md#execution-constraints); retain unresolved policies as open.
4. Derive acceptance from requirements, OPs, scenarios, and contracts.
   Record source, setup, stimulus, observable result, and required failure or timing bounds.
   Resolve links, types, and signatures; update indexes and diagrams.

| Element | Authoritative location |
| --- | --- |
| Application purpose, scenarios, diagram, dependencies, viable subsets, assumptions, exclusions, open decisions | Overall PRD |
| One concept | `CONCEPT.md` beside its module; before modules exist, `docs/prd/concepts/<name>/CONCEPT.md` |
| Cohesive composition group | `SYNCS.md` beside its rules under `apps/<app>/src/compositions/<group>/`; before modules exist, `docs/prd/compositions/<group>/SYNCS.md` |
| Acceptance | Overall PRD or existing acceptance file, linked to its checked contract or scenario |

Paths are logical examples; use the language's source root and existing groups.
Preserve confirmed legacy locations, including `docs/prd/SYNCS.md`, unless a move is authorized.
Index all CONCEPT and SYNCS files.
Each rule MUST have one definition and a stable application-wide identity.
Declare application instances, bindings, and shared entry contracts once; groups reference them.
Repeated includes refer to the same instances.
Files and `// flow:` groups do not create runtime flow identities or require separate builds.

A missing model decision stays open; return it to design rather than inventing a result.
Keep specified acceptance separate from executed test evidence.
Use the [scenario index](../../shared/learning/examples.md#scenario-index) to find worked models and counterexamples.
