# Specification Drift and Severity

Read each specification with current implementation, schema/migrations, tests, and staged files
linked by the overall PRD. Accept `principle` and `operational principle` and label legacy format
rather than reporting syntax alone as drift. Check query signatures like actions, while remembering
queries emit no completion.

Separate a missing OP test (verification gap) from a counterexample to contract → OP → purpose.
Without code, skip implementation and test-coverage conclusions.

| Object/category         | Decision rule                                                         | Default     |
| ----------------------- | --------------------------------------------------------------------- | ----------- |
| Missing action          | public action is undeclared                                           | Medium      |
| Removed action          | declared action is absent from all relevant implementations           | High        |
| Changed signature       | inputs, real outputs, or error cases changed                          | Medium      |
| New state               | undeclared state changes observable behavior                          | Medium      |
| Naming violation        | a core concept section depends on another concept definition          | Medium      |
| Seam violation          | code bypasses another concept's public interface for private state    | High        |
| Intrinsic coupling      | a concept directly calls another concept                              | High        |
| Cross-cutting parameter | a contract-relevant common parameter is undocumented                  | Medium      |
| OP without test         | no behavior test covers the representative story                      | Medium      |
| Excluded action used    | an application-excluded action is reachable                           | High        |
| Missing/removed sync    | coordination is undocumented or a declared rule has no implementation | Medium/High |
| Changed trigger         | actual completion differs from `when`                                 | Medium      |
| Changed binding/effect  | `where` qualification/binding or `then` target/arguments changed      | High        |
| New participant         | actual participating concept is undeclared                            | High        |
| Graph inconsistency     | a derived graph differs from its rules                                | Medium      |
| Missing reference       | sync action/query, signature, or instantiation does not resolve       | High        |
| Missing participant     | internal concept has no specification or index entry                  | Medium      |

External entries such as Requesting need no CONCEPT but their parameters, results, and correlation
must be verified. A synchronization graph may live only in the overall PRD. For PIPELINE, check
missing stage/source (Medium), contradictory invariant, and cross-concept access (High). Product
dependencies come from requirements, never code coupling alone.

Severity is repository policy: Critical requires evidenced authorization bypass, data destruction,
or core unavailability; High is a clear contract/seam violation; Medium is an impactful omission;
Low is local maintenance. Specification silence does not imply prohibition. Private helpers, derived
caches, semantics-preserving wrappers, and documented naming maps are not drift. Evidence every
Medium-or-higher finding with current locations; incomplete scans remain unverified. Merge findings
by root cause.

For large sets, review adjacent groups of two or three specifications, returning
passed/found/unverified for every category, then reconcile cross-spec references centrally. Use
`spec-format.md` for fields, cardinality, initial state, outputs, abstract-state reads, and
reachable matching behavior.
