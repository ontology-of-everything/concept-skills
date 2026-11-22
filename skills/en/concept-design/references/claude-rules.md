# Align CLAUDE.md

Compare confirmed contracts, actual code, and [engineering architecture](architecture.md); report conflicts before updating relevant rules. Do not treat existing code as the contract or change contracts to conceal defects.
Replace repetition with the short principles below; preserve unrelated rules and open decisions. Link each rule to its project authority and actual check without copying specification bodies.

```markdown
1. Use entry/<group>, usecases/<group>, modules/<business name>, and bootstrap, adding application-level adapters/contracts/infrastructure as needed. Use lowercase singular business directories and api/application/domain/adapters within business modules. Retain concept and synchronization terms in design; explicitly map concepts to modules, and compositions and rules to use case implementations. Record naming exceptions within confirmed scope.
2. Inbound adapters establish or pass the declared root action completion and its flow, then call the public <Action>UseCase directly. The use case executes one entry synchronization rule through business module APIs according to when/where/then. Fold forwarding-only Facades into the use case. Independent rules connect through action completions. Helpers supply computations or execution mechanisms only.
3. Business modules implement independent concepts and own their state and invariants; forbid dependencies, calls, and state reads between business modules. Business access uses api only; assembly uses dedicated entries. application depends on api/domain and inner ports; adapters implement ports. api/domain do not depend on other module layers; keep these business layers framework-free.
4. Implement CONCEPT.md/SYNCS.md; confirm contracts before behavior changes. Give each synchronization rule one named implementation. Follow-up rules fire on their own matching completions. Pluralize lists and collections by meaning. Preserve rule-to-implementation mappings, persisted identities, and existing failure and retry semantics.
5. Architecture checks distinguish design and source paths and cover directories, naming, dependencies, visibility, and rule mappings. For engineering renames, check tests, module discovery, wiring configuration, documentation references, and persistent event types; define migration scope from stored data and release status. Behavior tests cover contracts and execution boundaries. Fix code on failure; never report unverified work as passed.
```

Adapt names and check entry points to the project language and confirmed exceptions. Verify alignment with all three sources; report unresolved conflicts and unexecuted checks.
