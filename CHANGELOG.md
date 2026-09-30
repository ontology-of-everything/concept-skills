# Changelog

## 2.0.0 - 2026-10-01

### Breaking Changes

- Rename the six `concept-*` installation names to `software-concept-architect-*`, and rename `semantic-km-creator`
  and `semantic-pkm-creator` to `data-knowledge-architect` and `personal-knowledge-architect`. GitHub installs
  using the old names must switch to the new names.

### Features

- Add and refine the Read It. Reframe It. Own It. learning skill, including a goal-led knowledge tree.
- Classify the nine skill pairs by concept design, semantic modeling, knowledge management, and learning methods; sync ClawHub categories and topics for the eight published English skills.

### Documentation

- Add 27 graduated usage examples in each README and an illustrated study note for *The Essence of Software*.
- Align localized skill descriptions, QA, catalog entries, and installation guidance with the new names.

## Skill classification - 2026-09-30

- Classify skills into concept design, semantic modeling, knowledge management, and learning methods. Synchronize
  eight English ClawHub listings with explicit categories and topics without changing their versions. Generate
  README/skills.sh classification views and publish metadata from the catalog; defer the learning listing at the
  owner’s request because its slug redirects to Refine.

## Knowledge Architects - 2026-09-30

- Rename `semantic-km-creator` to `data-knowledge-architect` (1.1.0) and `semantic-pkm-creator` to
  `personal-knowledge-architect` (0.4.0). Add benefit-focused titles and synchronize English/Chinese metadata, QA,
  and documentation; preserve existing workflows.

## Read It. Reframe It. Own It. 0.2.0 - 2026-09-30

- Define learning goals in qualitative terms and choose framework dimensions around those goals.
- Clarify the sales example and revise the framework when new knowledge reveals gaps or contradictions.
- Attribute “the Six Classics annotate me” to Lu Jiuyuan and synchronize the English and Chinese editions.
- Publish the renamed knowledge-tree skill and its localized documentation.

## Unreleased

- Rename the six concept skills to Software Concept Architect, with localized display names and benefit-focused
  marketplace titles. Publish the family as 1.0.0; preserve current local skill behavior.

## 1.3.0 - 2026-09-22

### Features

- Add a restaurant reserve comparison: one scenario across concept design, naive DDD, split packages, and modular DDD, with the measured complexity counts (by @AgenticWeb4).

## 1.2.0 - 2026-09-22

### Features

- Concept design confirms an alignment with the user before the design record is written.
- The concept family states that synchronization may restrict behavior but must not extend a concept contract, and checks purpose fulfillment separately.
- Office-focused skills now live in the sibling `myoffice-skills` repository.

### Fixes

- Keep one specification contract across concept design, PRD, implementation, audit, and guardrails.

## 1.1.0 - 2026-09-15

- Make English the default skill name and add a `-cn` Simplified-Chinese companion for every capability.
- Add localization metadata, paired QA/catalog/docs entries, and an executable parity gate.

## 1.0.0 - 2026-09-15

- Establish the repository baseline for ontology, semantic-layer, concept-design, and presentation skills.
- Publish eight independently installable skills with colocated QA and documentation.
