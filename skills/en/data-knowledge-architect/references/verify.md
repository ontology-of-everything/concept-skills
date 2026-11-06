# Phase 4: Verify

Report `passed`, `failed`, or `unverified`, with tool or reasoning evidence. Parsing is not proof
of semantic correctness, and user approval is not proof of source truth.

## Structural checks

Parse YAML/frontmatter. Resolve expected files, unique paths/IDs, entry points, links, and source
locators; check against the selected project schema. For OKF, distinguish its extensible format
rules from this skill's stronger profile. Interpret leading `/` relative to the bundle root.
Do not fail unknown types or require `id`, `name`, or citations as OKF standard fields.

## Semantic checks

- Grain is a business statement backed by field and business evidence; keys, scope, time, pagination,
  and correction behavior support that statement.
- Dimensions and joins preserve fact grain. Check actual supported cardinality and one-to-many
  duplication, historical matching, and multi-tenant keys. Reuse only semantically conformed dimensions;
  a shared key spelling alone proves nothing.
- Measures have supported units/basis and aggregation rules by axis. Test a small counterexample:
  two lines must not double a header amount; two dates must not sum a balance; currencies require
  an evidenced conversion policy.
- Metrics cite source measures and define their formula, filters, time window, and aggregation scope.
  Do not rename gross order amounts as recognized revenue.
- Routes request sufficient source context and respect read/write and evidence boundaries. Names,
  source enums, joins, and calculations are not invented.
- Decisions, exclusions, and evidence match current feedback. Missing evidence stays unresolved or
  out of scope; a stale approval cannot settle a changed proposal.

Repair mechanical formatting and recheck. For semantic failures, identify the affected decisions;
reuse unchanged approvals and return only consequential changes to review. Ask when the needed
business meaning cannot be established from available evidence. Report remaining gaps and do not
claim runtime/source-data validation unless it was actually performed.
