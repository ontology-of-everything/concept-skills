# Learning with Conceptual Frameworks

Build a model tree around the learner's goal. Qualifying the goal establishes the
key framework: the factors and relationships needed to achieve it. Place methods,
pitfalls, and cases from sources beneath that framework. Supports automatic discovery
and explicit invocation.

```text
$learning-concept-framework Help me learn sales through an established framework and integrate these notes.
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

Deliver `learning-framework-<topic>.md` with four traceable levels:

| Part | Required answers |
| --- | --- |
| Goal | What problem must be solved, and what counts as success? |
| Goal qualification / key framework | Which factors and relationships achieve the goal? Why this framework? How do supplied sources support or challenge it, and does it cover the goal? |
| Concepts and relations | What role does each concept play, and how do they affect each other? Cite source support or mark inference. |
| Sourced knowledge | Which concept receives each method, pitfall, or case, why, and from which source? |

Reuse a source framework when it fits the goal, explaining how it helps. Source
headings do not automatically become branches. Check each framework branch against
the supplied material; mark support, counterevidence, or gaps. Judge completeness
against the goal and correctness against evidence and counterexamples.

## Goal qualification example

“Learn sales” names a topic. For a goal such as “explain why customers buy or decline
and choose a next action,” evaluate value, trust, and competition as a candidate
framework. Its fit still depends on the actual goal and material.

```text
Goal: explain buying or declining; choose a next action
└─ Qualification / key framework: buying is a multifactor choice; value,
   trust, and competition explain it [candidate; check against sources]
   ├─ Concept: value — what the customer gains and gives up
   │  └─ Relevant methods or pitfalls [source, placement reason]
   ├─ Concept: trust — judgments about promise fulfillment
   │  └─ Relevant methods or pitfalls [source, placement reason]
   ├─ Concept: competition — considered alternatives
   │  └─ Relevant methods or pitfalls [source, placement reason]
   └─ Relations: compare value with alternatives; trust affects acceptance
      of promised value [check against sources]
```

“Three pitfalls” is an author's presentation structure, not automatically a branch
of the knowledge tree. Reading sources through one's own questions organizes learning;
counterevidence may still change the framework, and source meaning must remain intact.
