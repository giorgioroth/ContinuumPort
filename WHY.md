# WHY

A system can drift without breaking.

You edit a file and press **Commit changes**. The connection drops before a reply reaches you.

The server may have saved your edit. It may never have received it. From your side, both cases look the same.

“No confirmation arrived” is an accurate record. “Nothing changed” says more than you know. So does “the edit is live.”

The missing reply is not yet drift. Drift begins when someone treats a guess as settled and builds the next step on it.

---

More memory can preserve the request, the discussion, and the reasons for the edit. Reading them again will not tell you whether the commit landed. Checking the repository can.

Until then, other work can continue. The step that depends on the edit being live should wait for evidence that it is.

---

ContinuumPort separates two things that are easy to confuse when work passes from one session or person to another.

**CP-Core carries the state of the work:** the goal, the decisions already made, the constraints that still apply, and the questions left open. A successor can pick up the task without having to impersonate the person who left it.

**Regen Engine checks whether a proposed action may proceed** on the execution paths it governs, under the declared constraints and current authority. A handoff can record that publication was approved yesterday. That record alone does not authorize publication today.

The [execution model](docs/EXECUTION_MODEL_LIMITS.md) draws a specific boundary: under its stated assumptions, a failed sequence leaves no partially committed change in the internal state it governs. Restoring that state cannot take back a message that has already reached its recipient.

A permitted step can still serve the wrong goal. A project can follow every rule and never finish.

---

**What did the last step actually change?**

**What gives us permission to take the next one?**

A system can remember the whole conversation and still owe us both answers.
