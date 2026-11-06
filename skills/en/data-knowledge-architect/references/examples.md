# Worked example

Assume the supplied v1 contract explicitly defines `ListOrders` rows with `order_id`, `tenant_id`,
`store_id`, `placed_at`, `amount_usd`, and one row per completed order. A supplied business definition
says `amount_usd` is gross order amount before refunds. `ListStores` declares unique
`(tenant_id, store_id)` and store attributes. These are example premises, not inferred fields.

Ingest inventories both read operations. Review proposes Order grain and tenant-scoped identity,
Store's many-orders-to-one-store join, creation time, and a gross-order-amount measure. Every choice
cites its contract or business-definition locator. If amount basis were absent, the measure remains
missing and cannot be approved merely by clicking a plausible option.

The user confirms this model. Reuse that approval; the workbench is another way to collect decisions,
not a requirement to click again. Emit either repository YAML or an OKF v0.1 bundle with Order,
Store, optional gross amount metric, and source-operation references. No "Revenue" metric is inferred:
recognized revenue and gross order amount need different definitions.

Check two distinct orders total correctly and Store joins do not duplicate them. If a later source
adds multiple order lines, do not sum the repeated order amount at line grain. If the source is a
current-status list with no historical guarantees, do not emit an order-event time series. Verify
format, references, and semantic counterexamples separately; report unexecuted data checks.
