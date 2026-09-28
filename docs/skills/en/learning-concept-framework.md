# Learning with Conceptual Frameworks

Build a reusable knowledge system around the learner's goal. Qualify the problem,
establish its key framework, then absorb methods, pitfalls, and examples from
different sources under concepts. Supports automatic discovery and explicit invocation.

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

Deliver `learning-framework-<topic>.md` with four parts:

| Part | Required answers |
| --- | --- |
| Goal and qualification | What problem will learning solve? What counts as success? What kind of problem is it, and which concepts and relationships determine the outcome? |
| Key framework | What do concepts mean and how do they connect to the goal? Which framework was reused or adapted, and why? Is goal coverage complete and supported by evidence? |
| Knowledge tree | Goal as root, core concepts as branches, knowledge as leaves; attach sources and placement reasons, distinguishing evidence from inference. |
| Gaps | Which relationships or claims need validation? What must be learned next? |

Without material, deliver a provisional framework with empty branches; with material,
populate it with sourced knowledge. Completeness is relative to the goal, not the
entire domain; correctness remains subject to evidence and counterexamples.

## Goal qualification example

“Learn sales” names a topic. For a goal such as “explain why customers buy or decline
and choose a next action,” evaluate value, trust, and competition as a candidate
framework. Its fit still depends on the actual goal and material.

```text
Explain buying or declining; choose a next action
├─ Value: what the customer gains and gives up
│  └─ Source methods or pitfalls about needs and benefits [source, placement reason]
├─ Trust: judgments about promises and fulfillment
│  └─ Source methods or pitfalls about promises and evidence [source, placement reason]
└─ Competition: alternatives the customer considers
   └─ Source methods or pitfalls about alternatives [source, placement reason]
```

“Three pitfalls” is an author's presentation structure, not automatically a branch
of the knowledge tree. Reading sources through one's own questions organizes learning;
counterevidence may still change the framework, and source meaning must remain intact.
