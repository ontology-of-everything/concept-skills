# Implementation sources

Publication dates identify consulted versions. Engineering choices were updated on 2026-11-01.

| Source | Used for |
| --- | --- |
| [Beyond Objects v1, 2026-06-25, sections 12 and 13](https://arxiv.org/html/2606.27258v1) | Independent concepts sharing identities; relation queries; requests distinct from requested actions. |
| [Making Software Meaningful v1, 2026-06-09, sections 4.4, 4.5, 5.2](https://arxiv.org/html/2606.11051v1) | Shared meanings across specifications/code/logs, granular rules, and Requesting's HTTP/routing example. |
| [WYSIWID v2, 2025-08-27, sections 3, 5, 6](https://arxiv.org/html/2508.14511v2) | Completion matching, binding, flow correlation, and firing recovery. |
| [Jackson 2015, section 8](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | Purpose/OP arguments, distinct from implementation conformance. |

[The local contract](spec-format.md) uses adapted WYSIWID v1 record notation with query extensions.
Preserve confirmed dialects; the papers do not define one interchangeable engine API.

## Engineering choices

This repository defaults to independently built modules in one server process. Composition owns
named rules; api maps protocols. [Ports and adapters](https://alistair.cockburn.us/hexagonal-architecture)
isolate facilities. Add [Clean layers](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
when domain and application responsibilities differ. The papers require neither style and allow
Requesting to encapsulate HTTP/routing.

Choose mediator/engine, transactions, outbox, idempotency, responses, and loop controls to meet the
contract. Verify recovery with durable records. Public state access opens neither private storage
nor permissions. These are engineering decisions, not a mandatory Jackson stack.
