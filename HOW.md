# HOW

An AI can propose a change. The proposal itself grants no permission to make it.

**Prepare the request.** Suppose an assistant proposes changing a report from `draft` to `ready`. CP-Core can carry the goal, the decisions already made, and the constraints on the work. That gives the next person enough context to understand the request. It does not give them permission to update the report.

**Decide at commit.** On the local execution path governed by Regen Engine, the relevant checks apply when the change is about to be committed: does this operation meet the declared constraints, given the current state and authority? If permission to update the report was revoked after preparation and that revocation is now in force, the request must be refused before the write. If the request is permitted, the write may proceed.

**Verify the effect.** To test this boundary, start with the report marked `draft`. Observe calls to the operation that writes the record, independently of the decision reported by the gate.

- For a clean refusal, expect no write call and a report still marked `draft`.
- For a successful update, expect one matching write and a report that reads `ready`.

Both observations matter. Finding the report still marked `draft` cannot, by itself, tell you whether a write was blocked or whether it happened and was later undone.

The [execution model](docs/EXECUTION_MODEL_LIMITS.md) limits its all-or-nothing guarantee to managed internal state under its stated assumptions. Restoring a report to `draft` cannot recall a copy already delivered to a reader. An external effect needs its own evidence.

That is the boundary: the request says what is proposed, the gate decides what may proceed on the path it governs, and observation tells us what actually happened there.
