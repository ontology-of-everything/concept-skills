---
name: concept-model
description: Guide new development and maintenance with concise concept principles.
  Use for state and behavior ownership, concept boundaries, or cross-concept collaboration;
  complements ub-mode.
metadata:
  language: en
  translation_of: concept-model-cn
  version: 1.0.0
---

# Concept modeling principles

Follow these principles when developing and maintaining software.

## Purpose

- One concept, one clear purpose.
- Fulfill the purpose with complete behavior.
- Explain value through a representative history; define behavior through contracts.

## Independence

- State belongs to its concept; rules stay with the state.
- Concepts are independently understandable; they neither call one another nor read one another’s state.
- Refer to external objects only by identity.

## Composition

- Concepts define behavior; synchronizations define collaboration.
- Make synchronization triggers, conditions, and actions explicit.
- Composition may restrict behavior, but must preserve contracts.

## Implementation

- Actions uphold preconditions, outcomes, and invariants.
- Make the observable outcomes of failure, retries, and concurrency explicit.
- Verify concept contracts and composition purposes separately.

## Maintenance

- Determine responsibility before adding structure.
- Preserve behavior when refactoring; make intentional changes explicit.
- Limit changes to what is needed; retain clear code.
