# Implementation Sources

Verified 2026-09-25. These are the latest relevant public versions found and checked in this review;
syntax across papers is not a single engine API.

| Source | Adopted knowledge and limits |
| --- | --- |
| [Beyond Objects v1, 2026-06-25, §§12–13](https://arxiv.org/html/2606.27258v1) | Partition actions/relations while sharing identities; no cross-concept references; queries return bindings and are not actions; separate requests from requested actions |
| [Making Software Meaningful v1, 2026-06-09, §§4.4–4.5, 5.2](https://arxiv.org/html/2606.11051v1) | Align action meanings across specifications, code, and logs; independent granular syncs; Requesting can encapsulate HTTP/routing without extra layers. TypeScript classes, DSL, and folders are example choices |
| [WYSIWID v2, 2025-08-27, §§3, 5–6](https://arxiv.org/html/2508.14511v2) | Completion matching, bindings, same-flow correlation, and engine firing recovery; the execution model adopted here, not the only possible concept implementation |
| [Jackson 2015, §8](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | OPs explain purpose fulfillment; conformance and model fitness remain distinct |

[The shared specification contract](spec-format.md) retains named-record notation adapted from
WYSIWID v1 as a repository format baseline, not a claim that theory stops at v1. Its query extension
aligns with Beyond Objects; Requesting appears in both 2026 papers and is not merely legacy material.
Preserve confirmed dialects and signatures rather than mechanically migrating them.

Repository choices include modular-monolith scope, verifiable named rule boundaries, and avoiding
hidden causality through sync-to-sync calls. Choose packages/files, ports/adapters, mediators, or engines
as needed. Public abstract state does not expose physical storage or bypass authorization. Transactions,
outboxes, external-effect idempotency, response handling, and cycle controls are engineering measures,
not a mandatory Jackson technology stack. Verify recovery claims against durable firing records.
