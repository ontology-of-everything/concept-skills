---
name: simplify-java
description: Simplify Java / Spring Boot code without changing behavior. Use for cleanup of working code, reduced nesting, clearer naming, and unnecessary complexity; use responsibility ownership, replaceable seams, and encapsulation value to guide decisions. Covers Java 21 and Spring Boot 4 without version migrations or full architecture redesign.
metadata:
  language: en
  translation_of: simplify-java-cn
  version: 0.1.0
---

# Java Code Simplification

Inspiration: [Addy Osmani](https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification).

## Overview

Reduce complexity while preserving behavior exactly. The goal is not fewer lines, but code that is easier to read, understand, modify, and debug.

Every simplification should answer: would a new teammate understand this code faster than before?

If existing code is clear and local, leave it.

## When to Use

- Functionality works and tests pass, but the implementation is more complex than necessary.
- Code review identifies readability or complexity problems.
- There is deep nesting, a long method, or unclear naming.
- Cleaning up an implementation written under time pressure.
- Consolidating scattered logic that belongs to the same responsibility.
- Merged changes introduced duplication or inconsistency.
- The user provides a code snippet and asks to simplify it or reduce nesting.

When not to use:

- Code is already clear; do not change it merely to simplify.
- Behavior is not yet understood; gather context first.
- A simpler implementation would cause a known, unacceptable performance regression.
- The module will be rewritten entirely; do not clean up code about to be deleted.
- The main problem is a functional defect, version migration, or architecture redesign; handle it separately.

## The Five Principles

### 1. Preserve Behavior Exactly

Change how the code expresses its work, not what it does.

Preserve inputs, outputs, side effects, execution order, exceptions, and edge cases. Behavior also includes caller-dependent mutability, object identity, serialization, transactions, and concurrency constraints.

Before every change, check:

- Does the same input produce the same result?
- Are failure conditions and error behavior unchanged?
- Are side effects, evaluation order, and short-circuit behavior unchanged?
- Do existing tests pass without modification?

Pin existing behavior, change the structure, then verify that behavior has not changed.

If equivalence is uncertain, gather evidence; retain the original when it remains uncertain. Do not use simplification to change defaults, add fault tolerance, or fix business defects.

### 2. Follow Project Conventions

Simplification should make code fit the project, not introduce personal preferences.

Before changing code:

1. Read applicable AGENTS.md, CLAUDE.md, and project conventions.
2. Study how neighboring code handles similar problems.
3. Confirm the Java toolchain, compilation release, Spring Boot, and related framework versions.
4. Follow existing domain terms, package structure, import ordering, and naming.
5. Follow existing method organization, exception, null, Optional, bean wiring, and annotation conventions.
6. Use existing build, test, static analysis, and formatting tools.

Select features for the project's actual versions. Do not upgrade versions, enable preview features, or replace the technology stack during simplification.

### 3. Prefer Clarity Over Cleverness

Examine data shape before control flow. Prefer existing types that express valid states and make branch coverage and results visible.

Clarity does not mean expanding everything into more statements:

- For discrete, mutually exclusive branches over existing types, consider an exhaustive switch.
- For ordered validation and early exits, consider guard clauses.
- Keep a ternary expression for a simple choice between two values.
- Explain complex conditions and calculations with accurately named intermediate values.

This example already has an OrderStatus enum. The public entry point, label, rejects null by contract; the status-to-label decision lives in one place.

Before:

```java
import java.util.Objects;

public final class StatusLabels {
    public enum OrderStatus {
        PENDING, PAID, CANCELLED
    }

    public static String label(OrderStatus status) {
        Objects.requireNonNull(status, "status");

        return status == OrderStatus.PENDING ? "Pending"
                : status == OrderStatus.PAID ? "Paid"
                : "Cancelled";
    }
}
```

After:

```java
import java.util.Objects;

public final class StatusLabels {
    public enum OrderStatus {
        PENDING, PAID, CANCELLED
    }

    public static String label(OrderStatus status) {
        Objects.requireNonNull(status, "status");

        return switch (status) {
            case PENDING -> "Pending";
            case PAID -> "Paid";
            case CANCELLED -> "Cancelled";
        };
    }
}
```

Results for all three existing states are unchanged. A null input still throws NullPointerException with the message "status".

Each state now explicitly maps to its result. Adding an enum constant later requires completing the branches on recompilation, rather than silently mapping the new state to "Cancelled" (cancelled).

This example does not require converting existing boolean parameters into an enum. Evaluate data-model or caller-contract changes separately, outside local simplification.

### 4. Maintain Balance

Watch for over-simplification:

- Aggressive inlining can remove names that express business concepts.
- Combining unrelated logic can turn two simple methods into one complex method.
- A short wrapper may support testing, replacement, or framework interception.
- Fewer lines do not necessarily mean lower comprehension cost.

Use the following judgments only when extracting, merging, or deleting boundaries:

- **Responsibility ownership:** Keep state and the rules maintaining its invariants within the same responsibility. Concentrate each business decision; do not merge distinct business purposes because the code looks similar.
- **Seam:** Identify where a dependency can be replaced without changing consumer logic. An existing injection point may suffice; another Java interface is not required.
- **Deep module:** Hide complex implementation behind a simple caller contract, so callers need fewer internal details. A module may be a method, class, or package.
- **Complete contract:** Consider preconditions, invariants, ordering, failure modes, and required configuration, not just method signatures.
- **Deletion test:** Consider deletion if removing a wrapper makes complexity disappear. Keep valuable encapsulation if details instead spread across callers. Also check framework behavior and actual replacement uses.
- **Locality:** Keep a rule's implementation, changes, and verification together where practical; reduce cross-file navigation needed to understand one behavior.
- **Current use:** Subtract complexity before adding structure. Add abstractions only when real variation, replacement, or testing needs within the current scope justify them.
- **Contract tests:** Verify through the existing caller contract; do not expand the public interface to test private steps.

Inspect existing data entry points and internal invariants. Parse and validate external data at entry, and use established contracts inside. This principle alone does not justify deleting validation: first prove it is redundant and that error behavior stays unchanged.

Preserve existing concept and synchronization contracts, responsibility ownership, and collaboration rules. Do not migrate an ordinary Spring application to a concept-and-synchronization architecture.

If improvement requires redesigning public contracts or moving responsibilities across concepts, report it separately instead of expanding this simplification pass.

### 5. Scope to What Changed

Prioritize code specified by the user; otherwise default to recently changed code.

Choose the smallest edit that solves the current readability problem. Avoid drive-by refactoring of unrelated code.

Read only the related context needed to understand and verify the change. Do not expand into a codebase-wide architecture scan.

## The Simplification Process

### Step 1: Understand Before Touching

Understand why a structure exists before removing it.

Answer:

- What responsibility does the code have? What data does it operate on?
- Which inputs are valid? Where is data parsed and validated?
- What calls it, and what does it call?
- What are the edge cases and error paths?
- Which tests define current behavior?
- Does a method, wrapper, or annotation carry framework runtime responsibilities?
- Does the structure address performance, platform limits, or historical compatibility?
- When necessary, can git blame and commit history explain the reason?

If a snippet lacks repository context, state what can be established. Do not invent conventions or verification results.

### Step 2: Identify Concrete Opportunities

These are inspection signals, not mandatory change thresholds.

| Pattern | Signal | Possible simplification |
| --- | --- | --- |
| Deep nesting | Multiple control-flow levels are hard to follow | Guard clauses or named helpers |
| Long method | Contains multiple independent intentions | Split by complete intention, not line count |
| Nested ternaries | Branch coverage or priority is unclear | if/else or an appropriate switch |
| Boolean parameter strings | Caller intent is unclear | Inspect data shape; use named methods or existing types only when contracts permit |
| Repeated conditions | One business decision is scattered | Extract a named predicate within the same responsibility |
| Generic or misleading names | Names do not explain contents or side effects | Use project domain language |
| Comments explaining what | Repeat clear code | Remove redundant comments |
| Comments explaining why | Record constraints or tradeoffs | Keep them |
| Duplicate logic | Multiple implementations of one rule | Extract after confirming shared responsibility |
| Dead code | Unreachable branches, unused variables, old commented code | Remove after checking framework, reflection, and configuration uses |
| Valueless wrappers | Forward without a contract or runtime behavior | Inline or call directly |
| Over-engineering | Layered factories or strategies without actual use | Replace with a direct expression meeting current needs |
| Redundant casts | A cast appears unnecessary | Remove only if overload resolution, runtime checks, and behavior stay unchanged |

Do not hide type mismatches with default branches, casts, or warning suppression. If the data model is the problem, identify it rather than silently redesigning it during local simplification.

### Step 3: Apply Changes Incrementally

Complete one independently understandable and verifiable simplification at a time.

1. Run existing relevant tests to establish the baseline.
2. Add characterization tests when needed and confirm results on the original implementation.
3. Make the smallest structural change.
4. Run relevant tests and checks.
5. Continue if they pass; otherwise undo this change or reconsider its cause.

Test caller-observable inputs, results, side effects, and errors. Do not lock tests to private method decomposition or internal call shapes.

Tests for behavior-preserving refactoring should normally pass on the original implementation. Do not rewrite expectations or deliberately break production code to manufacture a red-green cycle. If test effectiveness needs checking, use a controlled faulty implementation or mutation check in isolation.

If honest testing is impractical, report the gap. Do not substitute tests that only inspect code shape.

Separate simplification from new features and bug fixes to keep diffs reviewable. Commit or publish only when authorized.

If a refactoring touches more than 500 lines, first evaluate IDE refactoring, AST tools, or other previewable automation. Scale does not authorize broader scope or skipping incremental verification.

### Step 4: Verify the Overall Result

Compare before and after:

- Is the result easier to understand?
- Were patterns introduced that conflict with project conventions?
- Does each decision still live in one place?
- Must callers understand more implementation details?
- Is the diff focused, clear, and reviewable?
- Would a teammate consider it a net improvement?

Undo the simplification if the result is harder to understand or review.

Briefly record and report what changed, why it is clearer, what was verified, and what remains uncertain.

## Language and Framework Guidance

### Java 21

Consider stable features that reduce repeated decisions, casts, or boilerplate. Decide by comprehension cost and behavioral equivalence.

- **Pattern matching for switch:** Simplify repeated type checks and casts where useful. Preserve null handling, branch priority, guards, fallback results, and exceptions. Do not redesign type hierarchies for exhaustiveness.
- **Record patterns:** Simplify destructuring of existing records where useful. Check nested nulls and accessor invocation counts, order, and exceptions. Keep named access when the pattern is harder to read.
- **Record data carriers:** Consider records for genuinely value-semantic data. Check mutability, equality, constructor validation, public access, and serialization compatibility first. Do not mechanically convert entities, inheritance-based objects, or proxy beans.
- **Sequenced collections:** Express first/last access and reverse traversal with appropriate APIs. Check empty-collection exceptions, ordering, mutability, and aliasing. A reversed() view does not replace an independent reversed copy.
- **Stream and Optional:** Do not mechanically replace loops and conditionals. Preserve evaluation timing, side effects, ordering, and result-collection mutability. orElse and orElseGet are not automatically equivalent.
- **Virtual threads:** Understand and preserve the execution model. Do not automatically replace thread pools, asynchronous chains, or reactive chains. Handle changes to concurrency limits, timeouts, cancellation, context propagation, and resource lifecycles separately.

Do not introduce shared mutable state to reduce parameters or local variables.

### Spring Boot 4

Short methods and declarative configuration can carry important behavior.

- **Proxies and transactions:** Inspect annotations, call paths, and interception before deleting or moving methods. Preserve transaction boundaries, rollback, authorization, validation, caching, and asynchronous behavior. Proxy calls and self-invocation are not automatically equivalent.
- **HTTP and persistence:** Preserve status codes, response fields, exception mapping, validation order, persistence side effects, lazy-loading access, and meaningful query order.
- **HTTP Service Clients:** Where declarative clients are already used, check whether registration and group configuration can replace repeated wiring. Preserve requests, authorization, timeouts, error mapping, serialization, and observability configuration. Declarative interfaces may carry real remote-call contracts; do not delete them for lacking handwritten implementations or migrate all clients for stylistic consistency.
- **JSpecify:** Follow existing nullness conventions and distinguish nullable containers from nullable elements. Non-null annotations do not replace runtime validation. Remove null checks only when implementation and call paths prove redundancy.
- **Jackson:** Confirm the version, mapper, and modules actually in use. Remove duplicate construction or registration only when auto-configuration is equivalent. Verify fields, dates, enums, and null behavior; do not mix in a Jackson version migration.
- **Modules and auto-configuration:** Before removing dependencies or configuration, inspect modules, conditional wiring, runtime discovery, and test support. No explicit import does not mean no use.
- **Framework verification:** Verify touched runtime boundaries with existing integration tests or focused behavioral tests. Ordinary unit tests may bypass proxies and auto-configuration. Do not broaden the test context to conceal wiring problems.

## Common Rationalizations

| Rationalization | Judgment |
| --- | --- |
| Working code needs no changes | Hard-to-understand code within scope merits simplification; clear code can stay |
| Fewer lines are simpler | Compare comprehension cost, not line count |
| I will clean up nearby code too | Unrelated edits add review noise and regression risk |
| Types explain everything | Types do not fully express side effects or runtime calling constraints |
| This abstraction may be useful later | Justify complexity with current uses, not hypothetical needs |
| The original author must have had a reason | Investigate first; historical reasons may still apply or may have expired |
| New features are always more modern | A change is simplification only when clarity improves and behavior stays equivalent |
| More checks mean more safety | Establish contracts at real boundaries; repeated defenses can hide incorrect data flow |
| Refactoring while adding a feature saves time | Separate changes for review, verification, and rollback |

## Red Flags

- Test expectations must change for the simplification to pass.
- Code is shorter but requires more navigation or framework knowledge.
- Renaming follows personal preferences instead of project conventions.
- Error handling, entry validation, or framework annotations are removed for neatness.
- New defaults hide existing exceptions or illegal states.
- Interfaces, adapters, and forwarding layers are added merely for layering.
- Wrappers or configuration are deleted before they are understood.
- Public interfaces are expanded to test internal implementation.
- Execution-model, dependency-upgrade, or public-contract changes are mixed into cleanup.
- Many simplifications are made without independent verification.
- Code outside the task's scope is changed without being asked.

## Verification

- [ ] Existing tests pass without modification.
- [ ] Necessary behavioral tests pass on both original and changed implementations.
- [ ] The project builds with its actual Java release and no new warnings.
- [ ] Existing static analysis and formatting checks pass.
- [ ] Each simplification is independently understandable and reviewable.
- [ ] The diff contains no unrelated changes.
- [ ] Naming, structure, and usage follow project conventions.
- [ ] Error handling and necessary runtime validation were not removed or weakened.
- [ ] Touched null, exception, collection, evaluation, and serialization semantics are unchanged.
- [ ] Touched proxy, transaction, auto-configuration, and client boundaries were verified.
- [ ] No unused imports, variables, or unreachable branches remain.
- [ ] Simplification did not transfer internal complexity to callers.
- [ ] Unperformed checks and unconfirmed behavior were explicitly reported.

Check only what was actually completed. Passing tests are evidence, not proof of equivalence for every behavior.
