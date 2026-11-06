# Phase 2: Decision review

Establish brief (goal, deliverable, scope, evidence boundary), global constraints, and atomic
questions. Collect grain, dimensions, measures, metrics, then routing. Each decision separates source basis
(`explicit|inferred|missing`), recommendation confidence, and user feedback. Approval changes the
feedback state, not evidence quality. Missing evidence requires supplementation or an explicit
scope exclusion; it cannot be made true by selecting a plausible option.

## Build the workbench

Use `assets/review-template.html` with model JSON replacing `/*__MODEL_JSON__*/`. Serialize JSON;
escape `<` as `\u003c` before embedding so source text cannot close its script element. Never
interpolate source text into executable HTML/JavaScript. Save the model JSON beside the report as
its authoritative input. Choose a user-accessible output directory; temporary paths are optional.
The template runs offline and has no callback: return exported feedback in chat or as a file.

```json
{"meta":{"review_id":"sales-model","revision":1,"iteration":1,"title":"Sales review"},
 "brief":{"goal":"Compare gross orders","deliverable":"OKF v0.1","scope":"Orders","boundary":"No refunds"},
 "constraints":["Evidence before approval"],
 "objects":[{"id":"fact/order","kind":"fact","title":"Order",
 "evidence":[{"id":"e1","source":"contract-v1#ListOrders: one completed order per row"}],
 "decisions":[{"id":"grain","question":"What does an Order row represent?",
 "value":"One completed order","basis":"explicit","confidence":"high","status":"pending",
 "priority":"blocking","impact":"Prevents double counting","risk":"Wrong totals",
 "options":[],"relations":[]}]}]}
```

Object kinds are `fact|dimension|measure|metric|routing`; each owns evidence and decisions. A decision
needs ID, question, impact, risk, basis, confidence, priority, and a proposed value or options.
New decisions start pending. Explicit/high-confidence evidence can use a value-only confirmation;
supported but uncertain proposals provide two to four mutually exclusive options. Missing evidence
may have no proposed value/options: offer supplement or scope revision instead of inventing choices.
Each option has `id,label,when,benefit,cost,risk,reason,evidence,recommended`; evidence refers to
object-local IDs and exactly one supported option is recommended.

## Relations and feedback

Relations are `{type,target,note}` with targets `<object-id>#<decision-id>`.
`depends_on` blocks until prerequisites are resolved; cycles/self/missing references are errors.
`conflicts_with` means accepting both current proposals is invalid and blocks approval; show it
both ways. If only specific option combinations conflict, split/reframe decisions so the conflict
has an unambiguous scope. `tradeoff_with` is informational and bidirectional.
Changing a prerequisite choice clears dependent feedback, since it may need reconsideration.

The user can confirm a value, select an option, correct a value, supplement evidence, or reject
the question. Corrections/rejections/supplements create another revision; rejection does not
implicitly delete an object. A missing-evidence item cannot be approved. Draft export is always
available; approval export requires all decisions resolved with no conflicts, blocked dependencies,
or model errors. Exporting with `approved:true` requires an explicit user action.

## Revisions and completion

Keep `meta.review_id` stable for one review and increment `revision` when its proposal changes.
The export names `review_id`, `revision`, and `model_fingerprint`; each `decisions` entry
names `id`, `proposal_fingerprint`, and `action`.
Fingerprints detect accidental stale feedback; they are not authentication. Import validates actions
and option IDs, retains matching decisions, and reports changed proposals rather than restoring
stale approvals. Dependency/evidence/context changes also invalidate affected decision fingerprints.
Older unversioned feedback needs comparison against the original model; never blindly import it.

Record amendments with date, decision ID, prior/new value, reason, and source. Regenerate the model
and report after semantic changes. Reuse unchanged confirmed choices, including explicit approval
already given in chat; the workbench is a collection aid, not a second mandatory approval ceremony.
If confirmation is required, finish independent work and present the concrete unresolved choices.
Before emission, reconcile approved feedback with the current model and source evidence. Test draft
export, approval gating, changed prerequisites, stale import, and round-trip feedback; do not infer
that browser clicks have reached the agent.
