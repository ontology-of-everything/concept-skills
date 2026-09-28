# Learning with Conceptual Frameworks

Purpose: turn the learner's goal into a testable key framework so new material
can be placed by concept, challenge the model, and build a reusable knowledge tree.
Goal qualification establishes that framework. Supports automatic discovery
and explicit invocation.

```text
$learning-concept-framework I want to test whether a fertilizer improves seedling growth; organize these materials as a model tree.
```

[SKILL.md](../../../skills/en/learning-concept-framework/SKILL.md) · [QA](../../../qa/en/learning-concept-framework/README.md)

## Selection

Select by the requested outcome, not the word “concept”:

| Requested outcome | Route |
| --- | --- |
| Learn a new domain by clarifying the goal and key framework | This skill: establish a provisional framework |
| Integrate books, courses, or articles into a knowledge system | This skill: absorb knowledge by concept |
| Rebuild notes copied from authors' outlines into a knowledge tree | This skill: reorganize around the learning goal |
| Summarize a source in its original structure | Ordinary summarization |
| Extract source-grounded scenes, concepts, and entities into YAML | `semantic-pkm-creator` |
| Design software concepts, state, actions, and synchronizations | `concept-design` |

## Deliverable

Deliver `learning-framework-<topic>.md` with four traceable levels and cases when sources allow:

| Part | Required answers |
| --- | --- |
| Goal | What problem must be solved, and what counts as success? |
| Goal qualification / key framework | Which factors and relationships achieve the goal? Why this framework? How do supplied sources support or challenge it, and does it cover the goal? |
| Concepts and relations | What role does each concept play, and how do they affect each other? Cite source support or mark inference. |
| Sourced knowledge | Which concept receives each method, pitfall, or case, why, and from which source? |
| Classic positive and negative cases, when available | Which case succeeded or failed, through which mechanism, under which concept and limits? Cite sources; list missing cases to find. |

Reuse a source framework when it fits the goal, explaining how it helps. Source
headings do not automatically become branches. Check each framework branch against
the supplied material; mark support, counterevidence, or gaps. Judge completeness
against the goal and correctness against evidence and counterexamples. Prefer
classic positive and negative cases with verifiable sources and comparable goals
and conditions; explain material differences before drawing a comparison.

## Classic framework example: controlled experiment

“Learn plant growth” names a topic; “test whether a fertilizer increases
seedling growth” is a testable goal. This is a causal question, so a
**controlled experiment** is a candidate framework: compare treated and
control plants while keeping other conditions as similar as possible and
measuring the same outcome. This illustrates model choice; without results,
it makes no claim that the fertilizer works.

```text
Goal: test whether a fertilizer affects seedling growth
└─ Qualification / key framework: causal question; compare treated and
   control plants [controlled experiment]
   ├─ Concept: treatment — apply the fertilizer or not
   │  └─ Application advice from sources [source, placement reason]
   ├─ Concept: controlled conditions — similar light, water, and soil
   │  └─ Environment advice from sources [source, placement reason]
   ├─ Concept: outcome — growth over a fixed interval
   │  └─ Actual measurements [source, measurement method]
   └─ Relation: compare outcomes to test the fertilizer's effect [needs data]
```

## User example: sales

The user's source idea contrasts a model tree with copying an author's “three
key pitfalls” as headings. If the goal is to explain why customers buy or
decline, value, trust, and competition can be **candidate** concepts. Their
coverage and relationships still need evidence and counterexamples.

```text
Goal: explain buying or declining and choose a next action
└─ Qualification / key framework: value, trust, and competition affect choice
   [candidate]
   ├─ Value: what the customer gains and gives up
   │  └─ Place a source pitfall here if it concerns value [source, reason]
   ├─ Trust: judgments about promises
   │  └─ Place a source pitfall here if it concerns trust [source, reason]
   ├─ Competition: considered alternatives
   │  └─ Place a source pitfall here if it concerns alternatives [source, reason]
   └─ Relations: compare value with alternatives; trust affects acceptance
      of promises [needs verification]
```

The three actual pitfalls were not supplied; these leaves show placement
rules, not fabricated source claims.

## Positive and negative judgments

This table contrasts methods for building the tree; it is not evidence that
the fertilizer works.

| Check | Positive | Negative |
| --- | --- | --- |
| Where the trunk comes from | Derive treatment, control, controlled conditions, and outcome from the causal goal. | Use planting steps as top-level branches without a way to test the fertilizer. |
| Whether a model fits | Explain why each factor enables comparison and check supplied material for support. | Apply a familiar model without comparable groups or an outcome measure. |
| Handling new knowledge | Place advice and measurements by role; revise the design or conclusion when light differs between groups. | Claim an effect without data or ignore counterexamples. |

The sales example adds a second check: placing sourced pitfalls under value,
trust, or competition is positive; using “three key pitfalls” as the trunk
repeats the source outline.
