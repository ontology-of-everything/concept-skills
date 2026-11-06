# Rule collaboration diagrams

Apply the light or dark theme from the [shared diagram design](diagram-design.md).

Rule defines the conditions and order of collaboration, state changes, and failure handling. Choose a sequence, conditional flowchart, or state diagram for the question being explained. One R may need several diagrams.

| Diagram | Main concern |
|---|---|
| Business scenario sequence | Who interacts first, how messages return, and where retries or concurrency occur. |
| Conditional flowchart | Which conditions choose the next step and end branches or loops. |
| State diagram | Which states an object owned by a role can occupy and which events permit transitions. |

## Business scenario sequence

The example begins with a provider result callback. The payment service checks its signature, ownership, amount, and currency. It acknowledges the callback after committing terminal state and a unique delivery task together. The merchant atomically deduplicates eventId and updates its order. Delivery timeouts retry with the same eventId.

```mermaid
sequenceDiagram
    autonumber
    participant Channel as External payment provider
    participant Pay as Payment service
    participant PayDB as Payment store
    participant Order as Merchant order system
    Channel-)Pay: Callback with paymentId and result
    Pay->>Pay: Verify signature, owner, amount, currency
    Pay->>Pay: Check existing terminal-state constraints
    alt Validation passes and terminal state compatible
        Pay->>PayDB: One transaction: conditional terminal state + unique task
        PayDB-->>Pay: Committed or result already handled
        Pay-->>Channel: Acknowledge after durable commit
        loop Task incomplete and within bounded delivery window
            Pay-)Order: Terminal result with eventId
            Order->>Order: Atomically deduplicate eventId and update order
            alt Receipt confirmed
                Order-->>Pay: Acknowledge handled result
                Pay->>PayDB: Record successful delivery
            else Notification timeout or failure
                Pay->>PayDB: Save next retry schedule
            end
        end
    else Validation fails or result conflicts
        Pay-->>Channel: Reject result and record reason
    end
```

## Conditional flowchart

The payment service executes this result confirmation flow. Provider queries need an executor, backoff, and a query window. Keep unknown outcomes pending after the window ends and use reconciliation or manual verification.

```mermaid
flowchart TB
    Start(["Confirm payment result"]) --> Trusted{"Trusted terminal result available?"}
    Trusted -->|"Yes"| Apply["Conditionally update terminal state<br/>and atomically create delivery task"]
    Apply --> Done(["Proceed to result delivery"])
    Trusted -->|"No"| Window{"Query window still open?"}
    Window -->|"Yes"| Query["Query provider by paymentId"]
    Query --> Trusted
    Window -->|"No"| Pending["Keep pending<br/>Reconcile or verify manually"]
    Pending --> Stop(["Pause automatic queries"])
    class Apply,Query service
    class Pending worker
```

## State diagram

The payment service owns these states. Transition labels name the triggering conditions. Repeated terminal results cause only one effective change. Investigate conflicting results while retaining the confirmed terminal state. Track notification progress separately. Delivery failure does not change terminal payment state.

```mermaid
stateDiagram-v2
    direction LR
    state "Pending confirmation" as Pending
    state "Succeeded" as Succeeded
    state "Failed" as Failed
    [*] --> Pending: Accepted and persisted
    Pending --> Pending: Timeout or result still unknown
    Pending --> Succeeded: Success verified
    Pending --> Failed: Failure verified
    Succeeded --> Succeeded: Repeated success result
    Failed --> Failed: Repeated failure result
    note right of Pending
        Payment service owns these states
        Track delivery progress separately
    end note
```

## Checks

- Are the trigger, participants, and completion conditions clear? Can participants map to Role?
- Do branches, loops, and transitions name their conditions? Does each failure response have an owner?
- Does timeout preserve uncertainty? Do retries state an executor, bounds, and an exhaustion response?
- Are state updates, atomic commits, duplicates, and reordering clear? Do notes cover idempotency, validation, and terminal-state constraints?
