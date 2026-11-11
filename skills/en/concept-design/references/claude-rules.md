# Align CLAUDE.md

1. Compare confirmed design contracts, actual implementation, and applicable engineering conventions.
2. Report conflicts before writing rules. MUST NOT treat implementation as the contract or change the contract to excuse defects.
3. Use the five-rule template below in `CLAUDE.md`. Each MUST identify its source and check; reference authoritative definitions instead of copying them.
4. Update only relevant rules; preserve unrelated content. Unresolved decisions remain open.
5. Check the resulting rules against all three sources. Report unresolved conflicts and unexecuted checks; claim alignment only when supported by evidence.

## Output template

```markdown
1. Before development, check confirmed design, existing implementation, and engineering conventions; report conflicts first.
2. Implement state, actions, and invariants according to CONCEPT.md; concepts must not invoke one another or read one another's state.
3. Implement cross-concept coordination according to SYNCS.md; inputs, conditions, and results must agree between code and specifications.
4. For behavior changes, confirm and update the contract before changing code and tests; never change the contract to conceal defects.
5. Link each constraint to its authoritative definition and check; verify design, implementation, and engineering conventions before completion. Never report unverified work as passed.
```
