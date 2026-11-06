# Phase 1: Inventory and grain

Inventory each supplied operation or table once: identifier, source/version/locator, inputs, outputs,
read/write/unknown status, pagination, errors, temporal fields, keys, and evidence gaps. Inspect the
actual contract; a method name such as `get` or an HTTP verb is only a clue to effects.

| Evidence | What it can establish | What it cannot establish alone |
| --- | --- | --- |
| API/CLI response array | Candidate record shape and pagination boundary | Business event, uniqueness, history, or additivity |
| Table key/DDL | Declared uniqueness and structural relations | Measurement grain or business meaning of identity |
| Business definition | Event/snapshot meaning and intended analysis | Undocumented available fields or source guarantees |

Classify supported roles as fact candidate, dimension/source lookup, command/utility, mixed, or
out of analytical scope; otherwise mark unresolved. A fact may represent an event, periodic or
accumulating snapshot, or factless occurrence. A dimension provides descriptive context, not merely
code translation. Split mixed responses only when their independent meanings are evidenced.

Declare grain in business terms, including relevant event/snapshot time and uniqueness scope.
Distinguish one order, one order line, and one observed order version. Investigate null/duplicate
keys and corrections; do not infer a historical series from a current-state endpoint. A query
needing unsupported history remains outside the evidence boundary.

Exit when the inventory covers all supplied material and every unresolved role/effect has an
explicit gap. A gap blocks dependent decisions, not unrelated inventory work. Modeling does not
require executing writes or fetching production data.

Source: [Kimball grain](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/).
The inventory roles and evidence records are this repository's conventions.
