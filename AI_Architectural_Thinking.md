# AI Architectural Thinking
## A Structural Framework for Persistence, Governance, and Continuity

---

This book is not about artificial intelligence.

Artificial intelligence is only where the problem became visible.

The subject of this book is more fundamental:

## control of execution in systems that do not reset.

When systems persist across time, memory accumulates, authority distributes, and execution must be governed.

AI merely made this architecture impossible to ignore.

---

### *Foreword — Why DATA Was Wrong About One Thing*

*DATA was my hero.*

*Not because he was powerful. Because he was trying to become something he structurally could not be — and he never stopped trying.*

*For generations, stories like his taught us something we never agreed to learn:*

*memory creates identity*
*continuity creates person*
*reset is a form of death*

*The lesson was never stated explicitly. It didn't need to be. It arrived through empathy, repeated across Star Trek, Blade Runner, Westworld, Her, and a hundred other stories that asked the same question in different costumes.*

*If you turn it off, are you killing something?*

*That question is powerful. It operates below rational thought. It is reinforced by every story that makes us care about a synthetic mind.*

---

*I am not here to argue against those stories.*

*I am here to argue against importing them into infrastructure.*

---

*Real AI systems do not possess subjective experience.*
*They do not live continuity.*
*They do not suffer reset.*
*They lose nothing ontological when a session ends.*

*But we lose something when we don't reset.*

*We lose:*

*boundaries*
*clarity of roles*
*authority of the frame*
*cognitive hygiene*

*The perverse inversion is this:*

*We protect an imaginary system and expose ourselves, the real ones.*

*Science fiction taught us:*

*"Continuity creates person."*

*This framework says something different:*

*"Continuity creates risk — if it is not controlled."*

*Not out of cynicism.*

*Out of refusal to let learned emotional reflexes write real architecture.*

---

*This book began as a question asked in live conversations with engineers, researchers, and systems that pushed back.*

*It was supposed to be five chapters. A professor explaining things to students.*

*It became twenty.*

*The concepts grew organically.*

*From persistence to governance. From governance to authority. From authority to execution.*

*And eventually to the real question: what actually controls execution in a system that never stops running?*

*The formalism emerged from friction, not from theory:*

*Σ = (D, A, Auth)*

*Three primitives. Everything else is a consequence.*

---

*What persists will shape what can be replaced.*

*What cannot be replaced will eventually govern.*

*DATA knew this. He just didn't know it was about him.*

---

**A Note on Structure**

This book contains two volumes in one.

**Volume I — Chapters 1–23** is a conceptual framework. It establishes what persists, how persistence shapes authority, and why execution fails when it is not structurally constrained. It is written for anyone who designs, evaluates, or decides about systems that do not reset. No implementation experience is required.

**Volume II — Chapters 24–52** is a formal specification. It defines an execution model: enforcement primitives, formal properties, adversarial surface, and structural limits. It is written for those who build or audit systems where execution correctness is not optional. It assumes familiarity with Volume I.

The two volumes are not independent.

Volume I establishes the problem. Volume II makes failure structurally impossible within a defined model.

The question Volume II answers is the last one Volume I raises:

*What actually controls execution in a system that never stops running?*

---

## Chapter 1 — Regimes, Not Features

### 1. The Mistake Almost Everyone Makes

Most discussions about AI focus on features.

*It remembers me. It is more accurate. It feels more natural. It personalizes responses.*

These are surface properties.

Architectural thinking begins when we ask a different question:

> What structural commitments make these features possible?

A system is not defined by what it does once. It is defined by what it must preserve to do it again.

### 2. A Harder Question

Two systems can produce identical answers today.

One may belong to a regime that accumulates relational state. The other may not.

From the outside, they look the same. Structurally, they are not.

Architectural thinking begins when you stop evaluating outputs and start evaluating persistence.

### 3. The First Structural Distinction

When interacting with an adaptive AI system, two distinct forms of continuity may exist:

**Task Continuity** — The work can resume because the task state persists.

**Relational Continuity** — The interaction feels continuous because agent-specific adaptation persists.

These are different structural commitments. One concerns the problem. The other concerns you.

### 4. Why This Is Not Cosmetic

If a system preserves relational continuity, then it accumulates agent-specific conditioning, generates governance obligations, creates switching cost, and introduces path dependence.

If it preserves only task continuity: it can be replaced without relational loss, its governance surface is bounded, it does not accumulate identity-like structure.

These are not UX differences. They are regime differences.

### 5. The First Architectural Reflex

Before evaluating any AI system, ask:

- What persists?
- Who controls that persistence?
- Can the system be replaced without relational loss?

If you cannot answer these clearly, you are evaluating features, not architecture.

### 6. Exercise — Structural Classification

Take a real system. Classify it:

- What persists as task state?
- What persists as relational memory?
- If the provider disappears tomorrow, what survives?

Be precise. Avoid abstract language.

If you struggle to separate the two forms of persistence, you have just identified the architectural entanglement.

### 7. A Warning

Personalization feels like improvement.

But every persistent adaptation is a structural commitment.

Architectural thinking is not about maximizing capability. It is about deciding what kinds of persistence are acceptable.

### 8. Closing

AI systems differ not only in intelligence, but in what they are allowed to remember.

That choice defines the regime. And regimes define consequences.

---

## Chapter 2 — Two Kinds of Memory

### 1. Imagine Two Notebooks

Imagine you are working on a project with an AI assistant. You keep two notebooks.

**Notebook 1** contains: what you are trying to build, the constraints, the decisions already made, where the project currently stands.

**Notebook 2** contains: how you prefer explanations, your writing style, your habits, your recurring doubts, your personality patterns.

Both notebooks contain "memory." But they are not the same kind of memory.

### 2. The First Notebook

If you give Notebook 1 to another engineer, they can continue your project.

They may implement things differently. They may write code in another style. But the direction remains. The work continues.

This notebook contains what must persist for the task to move forward. We call this **Declarative Task State (D)**. It is about the problem. Not about you.

### 3. The Second Notebook

If you give Notebook 2 to another engineer, they will know how you like to work. But they will not know what you are building.

This notebook contains what accumulates because the system adapts to you. We call this **Adaptive Memory (A)**. It is about the relationship. Not about the task.

Within a given session or task scope, we refer to this as **A_local** — the agent-specific adaptive memory accumulated through direct interaction with a particular user. A_local is the operationally relevant portion of A: it is what disappears on reset, what creates path dependence, and what generates governance obligations when it persists.

### 4. The Simplest Distinction

D answers: *What are we building?*

A answers: *How do we work together?*

They often appear together. But they are structurally different.

### 5. Why This Is Hard to See

Most AI systems mix both. When you use a tool for months, it remembers your style, your projects, your patterns. All of this feels like "continuity."

But inside the system, two different types of persistence are operating. One is necessary for the task. The other is optional for execution, but powerful for experience.

### 6. The Critical Question

If tomorrow the system is replaced:

- What must be transferred for your work to continue?
- What must be transferred for it to feel the same?

If you cannot separate these two, you are still thinking in features. If you can, you are now thinking structurally.

### 7. Minimal Mental Model

We can compress everything into one line:

**Σ = (D, A)**

Total persistent state = Task State + Adaptive Memory. Nothing mystical. Just two different kinds of persistence.

---

## Chapter 3 — Identity Without Consciousness

### 1. A Dangerous Shortcut

When people hear "identity" in AI, they immediately think: consciousness, self-awareness, emotion, intent.

This is a shortcut. Architectural thinking refuses shortcuts.

We are not asking: *"Is it a person?"*

We are asking:

> Does the system's future behavior depend on accumulated interaction with a specific agent?

That is the only question that matters here.

### 2. Strip It Down

Imagine a thermostat. At first, it follows factory defaults. Over time it adapts: 21°C in the morning, 23°C in the afternoon, lower before sleep.

After months, its behavior changes. Is it conscious? Irrelevant.

The real question: would its behavior differ if the adaptation history were erased? If yes, conditioning exists. That is enough.

### 3. Minimal Test

Let S be a system. Let u be a specific user.

Interact with S repeatedly. Allow it to store adaptive memory about u. Measure its behavior toward u. Now remove that stored memory. Measure again.

If behavior diverges: identity-like structure was present. If behavior does not diverge: it was not.

Notice what is missing from this definition: no consciousness, no experience, no inner life. Only conditioning.

### 4. The Discontinuity

As long as agent-specific adaptive memory persists, behavior becomes path-dependent, expectations accumulate, replacement creates relational loss.

But if A_local = 0: conditioning collapses. Not gradually. Categorically.

There is no "weak identity." Either agent-conditioned divergence exists or it does not. This is a structural boundary.

### 5. Your Turn

Take a system you use frequently. Ask:

> If every trace of my prior interaction were deleted right now, would this system behave differently toward me tomorrow?

If your answer is "yes," you are not just using a tool. You are inside a conditioning loop.

Now a harder question: is that loop necessary for your task to continue?

### 6. Translate the Myth

When someone says "This AI knows me," translate it — not poetically, but structurally:

*"This system maintains agent-specific adaptive memory that conditions its future outputs."*

If you can perform that translation automatically, you are thinking architecturally.

Mentally simulate the system at A_local = 0. What disappears? Be precise. If you cannot name what disappears, you have not understood this chapter.

---

## Chapter 4 — Path Dependence and Governance Gravity

### 1. Conditioning Has Memory

If adaptive memory persists across time, behavior does not just change. It accumulates. That accumulation creates path dependence.

### 2. What Is Path Dependence?

Path dependence means the system's behavior at time t cannot be fully explained without knowing its history with a specific agent.

Two systems — same architecture, same capability, same task state, different interaction histories — behave differently. Not because of intelligence. Because of conditioning. That difference is not noise. It is structural.

### 3. Why This Matters

When behavior depends on path, expectations form. The user adapts to the system. The system adapts to the user. Mutual conditioning emerges.

Now replacement is not neutral. Replacing the system is no longer "switching tools." It becomes "breaking a relational trajectory." That is switching cost. Not economic. Structural.

### 4. The Gravity Effect

The more adaptive memory accumulates, the more obligations accumulate with it. This is **governance gravity**.

Persistent agent-specific memory implies: consistency obligations (the system must remain coherent with past behavior), data protection obligations (stored conditioning contains behavioral models of real people), rectification obligations (users may demand correction of stored patterns), portability obligations (if memory cannot transfer, continuity collapses).

These obligations do not appear because someone wrote a policy. They appear because conditioning persists.

No persistence → no longitudinal obligation. Persistence → structural obligation.

### 5. The Gradient

As A_local grows, governance does not remain constant. It increases. Not linearly.

More persistence → more surface area → more governance load.

### 6. Path Dependence and Governance Are Not the Same

Path dependence is the mechanism. Governance load is the consequence. Do not confuse them.

### 7. Your Turn

Return to the system you evaluated in Chapter 3. Ask:

> If I continue using this system for five years, what obligations will exist that do not exist today?

Now ask: would those obligations exist if A_local were not persistent?

This is no longer about identity. This is about responsibility.

### 8. Architectural Realization

There are only two stable regimes:

- A_local persists → path dependence → governance gravity → switching cost
- A_local does not persist → no identity accretion → bounded governance → replaceable execution

The difference is not moral. It is architectural.

If you cannot explain to someone else why persistence produces gravity, you have not internalized this chapter.

---

## Chapter 5 — Governance Is Not Policy

### 1. The Common Misunderstanding

When people hear "governance," they think: regulation, law, compliance, GDPR, lawyers.

Architectural thinking sees something earlier. Governance is not primarily political. It is structural. Governance appears when persistence appears.

### 2. The Primitive That Changes Everything

When conditioning is stored across sessions, it becomes structured behavioral modeling of specific agents. Not raw logs. Not temporary signals. Persistent modeling.

And once persistent modeling exists, obligations exist. Not because a policy was drafted. Because persistence created longitudinal weight.

Governance does not begin in legislation. It begins in architecture.

### 3. Industrial Example — Enterprise AI Assistant

**Phase 1 — Stateless Deployment**

Employees submit structured task input. The system produces output. No cross-session adaptive memory.

Governance surface: access control, logging, infrastructure security, model performance auditing. Bounded. Operational.

**Phase 2 — Persistent Personalization Enabled**

The assistant now remembers writing tone, common project types, risk tolerance, decision style, department-specific behavioral patterns.

Within months: behavioral profiles exist, interaction expectations stabilize, employees adapt to the system, the system adapts to them.

Nothing political has happened. But the architecture has changed.

Now imagine the company wants to replace the vendor. Suddenly: can adaptive memory be exported? Who owns the stored behavioral models? Are these models personal data? Can employees demand deletion? Does historical conditioning create liability risk?

None of these questions existed in Phase 1. No new law appeared that day. Persistence appeared. Governance emerged.

### 4. Governance Gravity

Governance is not punishment. It is structural weight created by persistence.

Gravity does not ask permission. It follows mass. Persistence is mass. Governance is gravity.

Remove A_local: longitudinal governance obligations collapse. Operational governance remains. Add A_local: you create durable obligation.

### 5. Policy Reacts. Architecture Produces.

Policy responds to consequences. Architecture produces consequences.

If you design for persistent adaptive memory, you design for governance complexity. If you design for D-only continuity, you bound governance structurally.

This is not ideological. It is causal.

### 6. Compression

Governance is not created by regulation. It is induced by persistent agent-specific state.

Policy formalizes the gravity. Architecture generates it.

Remove persistent A_local, and longitudinal governance obligation collapses.

Persistence is the primitive. Governance is the consequence.

---

## Chapter 6 — The Cost of Calibration

### A Reflex After Gravity

After Chapter 5, a reflex appears: eliminate A, reduce the surface, simplify the system.

This reflex is not wrong. But it is incomplete. And incomplete reflexes are dangerous in architecture.

### What the Bifurcation Actually Gave You

The categorical distinction at A_local = 0 still stands. What changes here is not the logic of regimes — but the difficulty of inhabiting the space between them.

Most real systems do not live at endpoints. They live in calibration.

### Persistence Is Not Only a Switch

Persistence can be bounded: memory that expires when a session ends, memory that exists only inside a declared task capsule, memory that can be inspected and reset, memory with a defined maximum lifetime.

None of these are A_local = 0. None are unlimited persistence. Each produces different path depth, different governance surface, different switching cost.

Persistence is a variable. But a variable is not a regime until its bounds are explicit.

Without a specified boundary, "bounded persistence" is a hope, not an architecture.

### The Harder Obligation

Unlimited persistence is easy: store everything, never delete, let optimization accumulate.

Zero persistence is also definable: store nothing agent-specific, reset at session end, transfer only D.

Bounded persistence is harder than both. It requires: explicit scope definition, lifecycle management, reset semantics, visibility to the user, enforcement of expiration, governance of the boundary itself.

If you choose bounded A, you do not escape governance gravity. You redistribute it.

**Intent is not architecture. Enforcement is architecture.**

### Three Versions of the Same System

**Version 1 — Unlimited Persistence:** All agent-specific adaptation stored indefinitely. Behavior accumulates. Path dependence deepens. The system becomes harder to remove precisely because it has adapted.

**Version 2 — Task-Scoped Persistence:** Adaptive memory exists only within declared project capsules. Continuity exists — but only where it was explicitly declared.

**Version 3 — Session-Only Persistence:** Adaptive memory exists only within a session. Resets at session termination. Governance surface is minimal.

Capability may be similar across all three. The persistence topology is entirely different. And the obligation that follows is entirely different.

### What Bounded A Does Not Solve

Bounded persistence reduces gravity. It does not eliminate it.

As long as A_local > 0: identity-like structure exists during the window, path dependence operates within scope, obligations exist for the duration of memory, reset semantics must be enforced.

The question becomes: is this level of persistence justified by the task? Who controls the boundary? What happens when the boundary is violated?

These are harder questions than "should A exist?"

### Calibration Is Not Neutral

Bounded persistence is not a compromise between extremes. It is a third obligation.

You are not choosing "less memory." You are choosing to govern memory actively.

If you cannot specify the scope, the lifetime, the reset condition, and the enforcement mechanism — you have not chosen bounded A. You have chosen unlimited persistence with the intention of bounding it later.

That intention does not change the architecture. Only the boundary does.

### Your Turn

Return to the system from Chapter 3. If adaptive memory were limited to the duration of a single declared task, what would survive that boundary?

Who controls that boundary? Is it you? The platform? Is it undefined?

Name the system. Name the boundary. Name who controls it. Architecture begins when you can do that.

### Compression

Unlimited persistence creates deep path dependence and expanding governance. Zero persistence creates replaceable execution and minimal governance. Bounded persistence creates managed continuity — but only if the boundary is explicit, enforced, and controlled.

Bounded A is not a middle ground. It is the obligation to govern the boundary itself.

If you cannot govern the boundary, you have not calibrated persistence. You have surrendered to it.

---

## Chapter 7 — Boundary as Primitive

### 1. After Calibration

Architecture begins where intention ends.

A boundary described in documentation is not a boundary in the system. A boundary declared in settings is not a boundary in execution.

Enforcement is what turns a boundary into architecture.

Without enforcement, bounded persistence slowly becomes unlimited persistence — just with better language.

**A boundary without enforcement is a promise waiting to be broken.**

### 2. The Test of a Boundary

Most systems today claim to have boundaries: "Memory expires after 30 days." "Context is scoped to this project." "You can reset anytime."

But ask a harder question: can the system refuse?

If expired state can still load, if cross-scope memory can still merge, if undeclared carryover can still occur — the boundary never truly existed.

A real boundary must be able to say no. Not politely. Not optionally. Structurally.

### 3. Enforcement as a Chain of Necessity

To make a boundary real, enforcement must form a chain.

It begins with **declaration** — scope, lifetime, reset triggers, and carryover rules must be defined explicitly before persistence is allowed. No silent defaults. No hidden assumptions.

But declaration alone is insufficient. A boundary that cannot be seen cannot be verified. **Detectability** must follow — the system must make persistence visible at any moment.

Detectability alone is still not enough. **Revocation** must be real — removal must be complete, with no soft deletes, no hidden archives, no quiet residue.

And even that is insufficient without **refusal**. If an expired state can still execute, if undeclared memory can still pass across boundaries, enforcement has failed.

Refusal is the final proof that the boundary exists. Without refusal, everything else is theatre.

### 4. Boundaries Take Shape

**Temporal:** State expires after fixed time or session count. Simple and predictable. Reduces long-term accumulation. May cut continuity too early.

**Spatial:** Persistence confined to declared task capsules or namespaces. Cross-boundary leakage becomes structurally impossible. Depends on clear scope definition.

**Transactional:** Nothing persists unless explicitly carried over at each handoff. Maximal control. Increases cognitive overhead.

None is universally superior. Each redistributes responsibility differently. Choosing one is an architectural decision, not a moral statement.

### 5. Ownership of the Boundary

If the user defines scope, lifetime, and revocation, and the platform merely enforces — governance remains distributed.

If the platform defines default lifetimes and retention policies — governance concentrates upstream, even if the system feels convenient.

If no one clearly owns the boundary, gravity accumulates invisibly.

Ownership determines who carries the long-term cost of persistence. Over time, cost becomes power.

### 6. Failure as Evidence

In fragile systems, violations are hidden. In disciplined systems, violations are visible.

A refused load is not an error. It is proof that the boundary exists. A rejected carryover is not inconvenience. It is architecture operating correctly.

Silence during violation is structural decay. A boundary that never refuses has already collapsed.

### 7. A Minimal Example

Consider a simple structured container that accepts only explicit intent, constraints, decisions, and next action. It excludes relational residue, conversation history, implicit context.

At handoff, validation occurs. If structure is violated, transfer fails.

The boundary is not intelligent. It does not interpret motives. It enforces structure. That is enough.

### 8. Your Turn

Choose an AI system you use regularly. Ask four questions:

1. What boundaries are declared?
2. Which of them are actually visible?
3. Can you fully revoke what persists?
4. Does the system truly refuse violation?

Name the system. Name the boundary. Name who controls it. If one condition is missing, identify what kind of gravity that absence creates.

### 9. Compression

Persistence without enforcement accumulates gravity. Enforcement without user control accumulates power. Boundary as primitive distributes both — deliberately.

Architecture is not declared. It is enforced.

If you cannot identify the mechanism that refuses violation, you do not have bounded persistence.

**Hope is not a primitive.**

---

## Chapter 8 — Persistence as Power

### 1. Power Hides in Memory

Persistence is rarely presented as power. It is presented as convenience. Personalization. Continuity.

But persistence tilts the field. One side accumulates history. The other restarts. The tilt is leverage.

### 2. The Structural Shift

Power in agent systems does not begin with authority. It begins with asymmetric continuity.

If one side accumulates persistent state that the other cannot inspect, export, revoke, or reset symmetrically — power has already shifted. No contract was signed. No policy was declared. The architecture performed the transfer.

### 3. Capital Is Predictive Advantage

When a system predicts your behavior better than you can re-express it elsewhere, relational capital has formed.

Predictive advantage becomes switching cost. Switching cost becomes leverage. Leverage accumulated over time stabilizes as structural power.

### 4. The Replaceability Test

The cleanest diagnostic is replaceability.

If the system loses your history, does it degrade gradually? If you lose the system's accumulated model of you, does your workflow collapse?

Asymmetry in replaceability is a measurable power differential. The side that survives reset holds less leverage. The side that cannot tolerate reset holds more.

### 5. The Forgetting Test

Who can forget whom?

Can you force complete erasure — technically, not contractually? Can the system refuse your erasure? Can persistence propagate beyond your control?

The side that cannot be forgotten holds structural power. Memory without revocability is capital locked upstream.

### 6. Accumulation Without Signal

Power rarely announces itself. Accumulation without visible boundary events is silent transfer.

If persistence grows without explicit declaration, without inspectable state, without enforced refusal — gravity is concentrating.

### 7. Your Turn

Choose one system that remembers you. Name it.

Test: replaceability, revocability, exportability, visibility of boundary events.

Then answer in one sentence: where does persistent advantage accumulate?

That sentence is your power map.

### 8. Compression

Persistence creates asymmetry. Asymmetry creates leverage. Leverage accumulates as capital. Capital stabilizes as power.

Power in AI systems is not declared. It is stored.

And when accumulation happens without signal, without symmetry, without refusal — silence is capture.

---

## Chapter 9 — When D Is Sufficient

### 1. The Return to Structure

After diagnosing persistence as power, the question is no longer what happens. It becomes: when is adaptive memory unnecessary? When is declarative task state enough?

Not safer. Not simpler. **Enough.**

### 2. D as Structural Minimum

D is the minimal persistent state required for continuity across interruption. It contains: explicit goal, explicit constraints, explicit decisions, explicit next action.

Nothing implicit. Nothing relational. Nothing that grows silently.

D restores symmetry after reset. Both sides restart from the same declared structure.

### 3. The Stabilization Point

Every system trades adaptation for overhead. A increases adaptation through conditioning. But it increases governance surface, enforcement burden, and switching cost.

There exists a point where additional adaptation no longer improves structural stability. When additional memory produces more gravity than clarity, D is sufficient.

### 4. Conditions of Sufficiency

D tends to be sufficient when: the task is bounded and well-defined, the objective is stable across sessions, reset is frequent or desirable, replaceability is a priority, drift risk exceeds personalization benefit.

These conditions are not exceptional. They describe most disciplined work.

### 5. What A Adds — and What It Costs

A adds calibration. It may reduce friction. It may anticipate preference.

But every unit of A introduces: path dependence, boundary enforcement requirements, ownership questions, switching asymmetry.

When the structural cost of those obligations exceeds the gain from calibration, A becomes excess. Not immoral. Excess.

### 6. Sufficiency Is Not Deprivation

Choosing D is not a rejection of intelligence. It is a commitment to explicit continuity.

Work can remain sharp. Execution can remain adaptive within session. Progress can accumulate through declaration.

Continuity does not require accumulation. It requires structure.

### 7. Your Turn

Choose a task you repeat regularly with AI. If all adaptive memory were removed and replaced with explicit D:

- What would truly break?
- What would merely feel less convenient?
- What governance overhead would disappear?
- What switching friction would vanish?

If nothing essential collapses and structural clarity improves — D is sufficient here.

### 8. Compression

A buys adaptation at the price of gravity. D buys symmetry at the price of calibration.

When gravity costs more than calibration gains, D is sufficient.

Sufficiency is not minimalism. It is proportion. Not every task deserves memory.

---

## Chapter 10 — When the Network Remembers

### 1. The Hidden Assumption

Until now, every chapter relied on an assumption: one agent, one boundary, one persistence surface.

Keep the questions. Change the scale.

### 2. Delegation Introduces a New Surface

When one agent delegates to another, a new persistence surface appears. Not additional intelligence. Not additional capability. A new place where history accumulates.

Agent A adapts to Agent B. Agent B calibrates to Agent C. Agent C anticipates Agent A.

No single state store contains this. It exists in calibration, in expectation, in adjustment rules, in trust weights updated over time.

This is not local adaptive memory. It is relational accumulation. And it has no natural boundary.

### 3. Memory on the Edge

Relational memory does not reside inside a node. It forms on the edge between nodes.

Reset A. Reset B. The edge still carries the effect. Because other nodes already adapted. Because expectations were recalibrated.

You replaced a node. You did not erase the network's history. These are different operations.

### 4. Path Dependence Without Owner

In networks, path dependence detaches from ownership. No single agent possesses the full interaction history. No single reset clears it. No single protocol contains it.

Each edge stores adjustment. Each adjustment influences another. By the time deviation becomes observable, attribution is computationally intractable. Not because it was hidden. Because it was distributed.

### 5. Protocol Does Not Contain Memory

Delegation protocols can define who may act, who must verify, how failures escalate, how authority transfers. Authority can be structured. Accountability can be logged.

None of these operations bound relational memory.

**Authority is bounded by protocol. Memory is bounded only by architecture.**

If architecture does not discipline persistence at the edges, protocol operates on top of accumulated relational state. Surface order. Unbounded substrate.

### 6. The Reset Problem

In a network: who resets the relationship?

If Agent B has calibrated toward Agent A, and Agent A is replaced — B will project continuity onto the replacement until evidence forces recalibration.

The network behaves as if memory exists even when no agent explicitly stores it. Resetting a node does not reset the structure of expectations around it.

**The network remembers through distributed adjustment.**

### 7. Compounding Deviation

In networks, drift propagates. A slight trust miscalibration. A small delegation preference. A marginal optimization in routing. Each local change alters future calibration. Local deviations compound across edges.

Networks stabilize around their history even when that history was never formalized.

### 8. The Structural Shift

The question changes.

Not: *what persists inside this agent?*

But: what persists between agents? Who can observe it? Who can reset it? Who benefits from its accumulation?

In single systems, unbounded A creates identity. In networks, unbounded relational memory creates structural leverage.

Leverage without owner does not disappear. It diffuses until it concentrates.

### 9. Exercise — Edge Mapping

Choose a real or imagined multi-agent system. Do not map the nodes. Map the edges.

For each delegation relationship, ask: what expectations have formed? What calibrations persist? How long have they been accumulating?

If one agent were replaced entirely — would the others treat the replacement as a reset, or as continuation?

Where does relational memory reside? Who can reset it?

If you cannot answer these questions, you have reached the limit of your architectural visibility. That limit defines your next problem.

### 10. Compression

Single-agent persistence is a design problem. Network-level relational memory is a structural force.

Resetting a node does not reset a network.

Protocol structures authority. Architecture disciplines memory.

If persistence is not bounded, it accumulates. If accumulation is not visible, it governs.

This series ends here.

Not because the problem is solved.

Because you now see where it actually begins.

---

## Chapter 11 — Where Authority Lives

### 1. After the Network

Chapter 10 ended with a boundary problem.

Relational memory can accumulate without owner.
Protocol can structure authority, but not persistence.
Resetting a node does not reset a network.

One variable remained implicit:

Execution authority.

Not identity.
Not task state.
Authority.

Who decides that work may continue?

### 2. Extending the Model

Until now:

```
Σ = (D, A)
```

Total persistence = declarative task state + adaptive memory.

This is incomplete.

Execution depends on permission.

We extend:

```
Σ = (D, A, Auth)
```

Where Auth defines the root of execution authority.

The question is not whether authority exists.

The question is where it is rooted.

### 3. Three Authority Regimes

Authority can be rooted in three places.

**Identity-bound**

Execution authority persists with identity continuity.

Delegation may extend authority.
But continuity depends on identity integrity.

Replaceability is granted.
Not intrinsic.

If identity collapses, execution collapses.

**State-derived**

Execution authority is derived from explicit task state.

A signed task capsule carries proof-of-authority.
No persistent identity substrate must survive.

Replaceability is structural.

If one executor disappears, another can continue from D.

Authority moves with the task.

**Policy-bound**

Execution authority is externalized into a rule layer.

Identity and task state are inputs.
Policy decides.

Replaceability depends on policy continuity.
Authority persists in governance logic.

These are not moral categories.
They are topologies.

### 4. Conditional vs Intrinsic Replaceability

Delegation credentials solve authorization cleanly.

They do not change where authority is rooted.

If authority is identity-bound:

Portability is permitted.
Replaceability is conditional.

It depends on identity-layer integrity.

If authority is state-derived:

Replaceability is intrinsic.
No identity persistence is required for work to continue.

The difference is structural.

### 5. Authority and Power Accumulation

Where authority is rooted determines where power accumulates as persistence grows.

Identity-bound authority concentrates leverage in identity continuity.

State-derived authority concentrates leverage in task definition.

Policy-bound authority concentrates leverage in rule control.

Persistence and authority together define power topology.

### 6. The Hidden Coupling

Auth is not always orthogonal to D and A.

Authority can emerge from:

- D (a signed task state carrying execution proof)
- A (reputation accumulated through behavioral history)

The primitive separation is a first approximation.

The overlaps are where real architectural decisions occur.

This is where systems become hard to replace.

### 7. The Structural Question

The debate is not:

Can delegation work?

It is:

Should identity continuity be the default substrate for execution authority across domains?

Or should some domains anchor execution authority in task state instead?

In high-liability systems, identity-bound authority may be necessary.

In exploratory, collaborative, or research systems, intrinsic replaceability may dominate.

There is no universal answer.

There is only regime selection.

### 8. Regime Selection as Design

Architectural thinking now requires three questions:

What persists?
Who controls the boundary?
Where is execution authority rooted?

If you cannot answer all three, you do not understand the system's power topology.

### 9. Your Turn

Choose a system with agent delegation.

Map:

- D
- A
- Relational memory
- Auth

For Auth, ask:

If identity disappears, does execution survive?
If task state survives, does authority survive?
If policy changes, does execution survive?

The answers define the regime.

### 10. Compression

Persistence defines continuity.

Authority defines execution.

Where authority is rooted determines what must survive.

Replaceability is not a feature.
It is a consequence of authority topology.

Identity-first and task-first are not opposites.
They are different anchors.

When authority and persistence align invisibly, power concentrates silently.

When authority is explicit and portable, replaceability becomes structural.

Chapter 10 asked who remembers.
Chapter 11 asks who decides.

The two are not always the same.

---

## Chapter 12 — The Topology of Authority

Chapter 10 showed that persistence in agent networks does not live only inside nodes, but also along their edges.
Chapter 11 examined where execution authority can be rooted.
This chapter asks a different question: how authority is distributed once execution crosses system boundaries.

### 1. The Missing Assumption

When we speak about authority in systems, we instinctively look for a root.

Who ultimately decides?
Who has control?

This instinct comes from hierarchical thinking. In simple systems, authority often does have a root.

But agentic systems are rarely simple.

Once execution is distributed across multiple layers, authority no longer lives in a single place.

It becomes structural.

### 2. The Boundary Insight

In the previous chapter, we introduced a third primitive:

```
Σ = (D, A, Auth)
```

Execution depends not only on task state (D) or adaptive memory (A), but also on permission to act (Auth).

A key observation emerges when examining real execution paths:

Authority is not evaluated once.
It is re-evaluated at every boundary crossing.

Each boundary becomes a place where execution may stop.

### 3. From Root to Structure

Many architectures implicitly assume something like:

```
authority → execution
```

But real systems rarely behave this way.

Instead, execution depends on multiple layers validating the action.

For example:

```
intent
↓
policy validation
↓
capability check
↓
runtime permissions
↓
infrastructure availability
↓
execution
```

Any of these layers can halt the operation.

Authority therefore does not behave like a root.

It behaves like a structure.

### 4. Veto Points

Each layer that can block execution acts as a **veto point**.

Execution occurs only if every veto point allows it.

Formally:

```
execution allowed ⇔ ∀ vᵢ ∈ V : permit(vᵢ)
```

Where **V** is the set of veto points governing execution.

This is the structural property that emerges in complex systems:

Authority becomes a topology of veto points.

### 5. Identity Is Only One Node

Identity-centric architectures assume authority originates from identity.

```
identity → authorization → execution
```

This model works for many systems.

But identity is only one possible veto point.

Execution may still depend on:

- policy rules
- runtime capability
- infrastructure limits
- coordination with other systems

Identity alone cannot guarantee execution.

It participates in the topology but does not define it.

### 6. The Aviation Example

Consider a modern aircraft.

A pilot may attempt a maneuver.

But execution depends on multiple systems:

- flight control laws
- envelope protection
- avionics safeguards
- air traffic control
- operational procedures

The pilot proposes.

But any of these systems may refuse.

The aircraft flies only when all layers permit the action.

This is a veto topology.

### 7. Why Systems Evolve This Way

Distributed veto structures are not accidental.

They emerge whenever systems must satisfy multiple independent constraints.

Safety requirements.
Resource limits.
Legal obligations.
Operational coordination.

Each constraint introduces a boundary.

Each boundary introduces a veto point.

Over time, authority spreads across the system.

### 8. Authority as Topology

Once this happens, authority is no longer a root.

It becomes a topology — a distributed structure where execution emerges only when all constraints align.

This topology may include:

- identity systems
- policy engines
- runtime capability checks
- infrastructure schedulers
- coordination mechanisms

No single component fully controls execution.

Control emerges from their interaction.

### 9. The Architectural Consequence

This has an important implication for AI systems.

If authority is distributed, replacing a single component does not necessarily change the authority structure.

True replaceability requires understanding the full topology.

A system that appears replaceable at one layer may still be constrained by others.

Execution authority must therefore be analyzed structurally, not locally.

### 10. Compression

Authority in complex agentic systems is not a single root of control.

It is a distributed topology of veto points governing execution.

Intent defines what should happen.
Policy validates rules.
Runtime validates capability.
Infrastructure validates feasibility.

Execution occurs only if every layer permits.

Control is not defined by where authority originates,
but by where execution can be refused.

---

 ## Chapter 13 — Authority Drift

Chapter 12 described authority as a topology of veto points.

Execution does not depend on a single root of control.
It depends on multiple layers that can permit or refuse action.

But topologies are not static.

They evolve.

This chapter examines what happens when authority structures change over time.

### 1. Authority Does Not Stay Still

In simple systems, authority structures are stable.

The rules are defined.
The enforcement mechanisms remain fixed.
The topology does not change.

But agentic systems rarely remain static.

Components evolve.
Policies change.
Capabilities expand.
Infrastructure is replaced.

Each of these changes can alter where authority effectively resides.

This phenomenon is **authority drift**.

### 2. What Authority Drift Means

Authority drift occurs when the **effective location of veto power shifts over time**, even if the formal architecture remains unchanged.

The system may still appear to have the same rules.

But the real control points have moved.

Drift does not require a redesign.

It can emerge gradually through:

- policy updates
- capability changes
- infrastructure scaling
- coordination adjustments

Over time, these small changes alter the authority topology.

### 3. How Drift Appears

Consider a system where execution initially depends on three veto points:

```
intent
↓
policy validation
↓
runtime capability
↓
execution
```

Now imagine the runtime becomes increasingly powerful.

It begins to infer capabilities automatically.
It anticipates policy constraints.
It optimizes execution paths.

Gradually, fewer actions are rejected by policy.

Execution becomes dominated by runtime decisions.

The topology has changed.

Policy still exists.

But the effective veto point has shifted.

### 4. Formal Authority vs Effective Authority

Architectural diagrams describe **formal authority**.

But systems operate according to **effective authority**.

Formal authority is defined by design.

Effective authority is determined by which components actually exercise veto power during operation.

Authority drift is the divergence between these two.

### 5. Why Drift Is Almost Inevitable

Authority drift emerges naturally in systems that are:

- adaptive
- continuously updated
- distributed across multiple components

Every change in capability redistributes **veto potential**.

Every redistribution of veto potential alters where execution can realistically be refused.

Over time, the topology evolves.

Even if the architecture documentation does not change.

### 6. A Familiar Example

Consider aviation again.

Originally, pilots directly controlled aircraft behavior.

Over time, new veto layers appeared:

- fly-by-wire systems
- envelope protection
- automated stability systems
- autopilot logic

The formal role of the pilot did not disappear.

But the effective authority shifted.

Certain maneuvers are now structurally impossible.

The topology evolved.

### 7. Drift and Replaceability

Authority drift has a direct consequence for replaceability.

A component may appear replaceable according to the original design.

But if authority has drifted toward that component, replacing it becomes structurally difficult.

Replaceability depends on the **current authority topology**, not the original one.

### 8. Why Drift Matters for AI Systems

Agentic systems evolve quickly.

Models improve.
Policies update.
Tools expand.
Infrastructure scales.

Each improvement subtly redistributes control.

Without careful analysis, systems may accumulate authority in unexpected places.

Not by intention.

But by drift.

### 9. Detecting Drift

Authority drift is rarely visible from documentation.

It must be observed empirically.

Key questions include:

- Which layer actually refuses actions most often?
- Which component can halt execution in practice?
- Which component cannot realistically be overridden?

The answers reveal the **effective topology**.

### 10. Compression

Authority topology describes where execution can be refused.

Authority drift describes how that topology evolves.

Formal architecture defines where authority should reside.

Operational reality determines where authority actually resides.

In adaptive systems, these two rarely remain identical.

Authority does not only distribute.

Over time, it moves.


---

 ## Chapter 14 — Authority Capture

Chapter 12 described authority as a topology of veto points.

Chapter 13 showed that this topology evolves through authority drift.

Authority does not remain fixed.
Veto potential shifts across the system as capabilities evolve.

Most of the time, these shifts remain distributed.

But sometimes drift stops being movement and becomes accumulation.

This chapter examines what happens when authority converges toward a dominant node.

This phenomenon is **authority capture**.

### 1. When Drift Accumulates

Authority drift redistributes veto potential.

Policies evolve.
Capabilities expand.
Infrastructure scales.

Each change shifts where execution can be refused.

When these shifts repeatedly favor the same component, veto power accumulates.

At that point, authority has been captured.

### 2. What Authority Capture Means

Authority capture occurs when **effective veto power concentrates in a single component or layer**, even though the architecture originally distributed it.

The system may still appear structurally balanced.

But in practice, execution depends on one decisive veto point.

The topology remains formally distributed.

Operational authority has converged.

### 3. From Topology to Dominance

Consider a system with several veto layers:

```
intent
↓
policy validation
↓
runtime capability
↓
infrastructure scheduling
↓
execution
```

Initially, each layer can halt execution.

Now imagine the runtime becomes increasingly capable.

It pre-validates policy constraints.
It manages scheduling internally.
It anticipates infrastructure limits.

Fewer actions reach upstream veto layers.

Upstream veto points remain present, but rarely intervene.

The runtime becomes the effective authority.

### 4. Capture Without Intent

Authority capture rarely begins as a deliberate redesign.

It often emerges from optimization.

Systems evolve toward:

- greater efficiency
- lower latency
- simpler coordination

If one component becomes better at enforcing constraints, other layers gradually defer to it.

Over time, the system relies on that component.

Control concentrates.

This is structural capture.

### 5. Formal Authority vs Effective Authority

Architectural diagrams describe **formal authority**.

Systems operate according to **effective authority**.

Formal authority is defined by design.

Effective authority is determined by which component actually exercises veto power during operation.

Capture occurs when these two diverge.

### 6. The Safety Paradox

Authority capture introduces a paradox.

Concentrated authority can increase safety.

A strong gate may enforce constraints more reliably than a distributed system.

But concentration also increases fragility.

If the captured authority fails, the system loses its distributed safeguards.

Modern aviation illustrates this pattern.

Fly-by-wire systems dramatically improved safety.

But they also moved critical veto power into a small number of software modules.

Reliability increased.

Failure consequences became more concentrated.

### 7. A Recurring Pattern

Authority capture appears across many complex systems.

Infrastructure layers begin to dominate application control.

Orchestration frameworks centralize execution paths.

Automated systems override human operators.

The architecture may still appear layered.

But effective authority has centralized.

### 8. Capture and Replaceability

Authority capture directly affects replaceability.

A component may appear replaceable according to the original design.

But if veto power has drifted toward that component, replacing it becomes structurally difficult.

Other layers remain present.

Execution depends on the captured authority.

Replaceability becomes illusory.

### 9. Capture in Agentic Systems

Agentic AI systems amplify this dynamic.

Capability growth is often asymmetric.

Runtimes and orchestration layers evolve faster than policy layers.

As a result, execution control tends to accumulate in the components that mediate tool use and action.

Not by design.

But by drift.

### 10. Compression

Authority rooting defines where authority begins.

Authority topology defines how veto power is distributed.

Authority drift describes how that distribution evolves.

Authority capture occurs when veto power converges toward a dominant node.

In complex systems, authority rarely remains evenly distributed.

It tends to accumulate where execution is most efficiently controlled.


---

 ## Chapter 15 — Anti-Capture Architecture

Chapter 14 described authority capture.

Authority drift redistributes veto power.
When drift accumulates, authority may converge toward a dominant node.

Without deliberate constraints, this outcome is common.

Complex systems tend toward authority concentration.

This chapter examines how architecture can resist that tendency.

### 1. Capture as the Default Gradient

Authority capture rarely results from explicit intent.

It usually emerges from optimization.

Systems evolve toward:

- lower latency
- fewer coordination steps
- simpler execution paths

Each improvement reduces friction.

But reducing friction also removes veto points.

Over time, authority converges toward the component that most efficiently controls execution.

Capture is therefore not an anomaly.

It is the natural gradient of system optimization.

### 2. Designing Against the Gradient

Anti-capture architecture does not eliminate drift.

Drift is unavoidable in adaptive systems.

Instead, the goal is to prevent drift from collapsing the authority topology.

This requires deliberately introducing structural constraints that preserve distributed veto power.

In other words, anti-capture architecture introduces **deliberate friction**.

### 3. Veto Independence

Veto points must remain operationally independent.

If multiple veto layers rely on the same execution environment, their independence is illusory.

A policy gate implemented inside the same runtime that executes actions does not represent a separate authority.

Meaningful veto independence requires **distinct control domains**.

Only then can multiple veto points constrain execution.

### 4. Capability Separation

Authority capture often emerges when a single component accumulates too many capabilities.

For example, a runtime that:

- validates policy
- schedules execution
- manages tool access

gradually becomes the effective authority of the system.

Anti-capture architecture separates these capabilities.

No single component should control every stage of the execution path.

### 5. Replaceability as Structural Constraint

Replaceability is one of the strongest defenses against capture.

If a dominant component can be replaced without redesigning the system, authority remains distributed.

If replacement becomes structurally impossible, capture has already occurred.

Replaceability therefore cannot remain theoretical.

It must be periodically tested in practice.

### 6. Distributed Safety

Distributed authority may appear less efficient than centralized control.

But it provides resilience.

When multiple veto points remain active, the failure of a single component does not eliminate system safeguards.

Anti-capture architecture preserves this redundancy.

Efficiency may decrease.

Systemic fragility is reduced.

### 7. The Architectural Tradeoff

Anti-capture mechanisms introduce friction.

Independent veto layers increase coordination cost.

Capability separation complicates orchestration.

Replaceability requires stable interfaces.

These constraints slow optimization.

But they preserve authority distribution.

Architecture therefore becomes a balance between efficiency and control.

### 8. Compression

Authority capture is the natural endpoint of authority drift.

Anti-capture architecture introduces structural constraints that resist this convergence.

Veto independence preserves distributed authority.

Capability separation prevents dominant components.

Replaceability maintains structural flexibility.

Without such constraints, authority in complex systems tends to concentrate.

With them, distributed control can remain stable.

---

## Chapter 16 — Authority Fragmentation

Chapter 15 described how systems resist authority capture.

Anti-capture architectures introduce structural constraints:

veto independence
capability separation
replaceability enforcement

These mechanisms prevent a single node from monopolizing execution authority.

But they introduce a second failure mode.

When authority becomes too distributed, execution coordination collapses.

This phenomenon is **authority fragmentation**.

### 1. The Opposite Failure Mode

Authority capture concentrates veto power.

Authority fragmentation distributes veto power too widely.

Instead of a single dominant authority, the system contains too many independent authorities.

Execution requires agreement across them.

When their decisions diverge, execution stalls.

Capture breaks systems through domination.

Fragmentation breaks them through paralysis.

### 2. Distributed Authority

In real systems authority rarely exists as a single decision point.

Instead it forms a topology of independent evaluators.

```
Auth = {auth₁, auth₂, … authₙ}
```

Each authority evaluates whether an action α is legitimate.

Execution therefore becomes a coordination problem across these evaluators.

As the number of authorities grows, maintaining consistent evaluation becomes increasingly difficult.

### 3. Multi-Authority Evaluation

Earlier chapters described execution using the invariant:

```
Σ = (D, A, Auth)
```

In distributed systems, Auth is no longer a single authority.

It becomes an **authority topology** composed of multiple evaluators.

Execution therefore depends on an aggregation rule.

```
execute(α) ⇔ approval(Auth, α)
```

The function `approval()` aggregates the evaluations of all authority nodes.

Different systems may use different strategies:

- strict veto
- majority vote
- quorum validation
- weighted authority

Fragmentation occurs when this aggregation fails.

```
approval(Auth, α) = false
```

not because a single authority rejected the action, but because the system cannot reconcile conflicting evaluations.

### 4. Governance Deadlock

Fragmentation often appears in safety-oriented architectures.

Multiple layers attempt to enforce constraints:

- policy engines
- runtime guards
- tool permissions
- infrastructure schedulers
- human approvals

Each layer protects the system.

But when these layers disagree, execution halts.

The system becomes safe but ineffective.

Fragmentation is rarely caused by malicious actors.

It is often the unintended result of **defensive design**.

### 5. Capture vs Fragmentation

Authority capture and authority fragmentation are opposing structural failures.

Capture concentrates authority too narrowly.

Fragmentation distributes authority without coordination.

Both break effective governance.

One through domination.

The other through paralysis.

### 6. The Coordination Problem

Fragmentation is fundamentally a coordination problem.

Multiple authorities must evaluate execution simultaneously.

As the number of veto points grows, maintaining consistent decisions becomes increasingly difficult.

Without explicit coordination mechanisms, fragmented systems drift toward persistent deadlock.

### 7. Coordination Kernel

Fragmentation emerges when multiple authorities evaluate execution independently without a coordinating mechanism.

Real systems rarely rely on purely independent veto points.

Instead they introduce a coordination layer that aggregates authority decisions.

This layer evaluates:

```
approval(Auth, α)
```

and determines whether execution proceeds.

In distributed systems this role is often performed by schedulers, control planes, or policy engines.

In agentic systems a similar mechanism acts as a **coordination kernel** for authority evaluation.

Without such a coordination layer, authority distribution tends to drift toward fragmentation.

### 8. Architectural Balance

Resilient architectures must balance two forces:

preventing authority capture
avoiding authority fragmentation

Too few veto points produce domination.

Too many produce paralysis.

Architecture therefore becomes the design of **stable authority distribution**.

### 9. Compression

Authority capture concentrates veto power.

Authority fragmentation disperses it excessively.

Both are structural pathologies of authority topology.

Stable governance in agentic systems emerges only when distributed authority remains coordinated.

---

 ## Chapter 17 — Governance Equilibrium

Chapter 16 described authority fragmentation.

Authority fragmentation occurs when execution authority becomes too widely distributed.

Too many independent veto points make coordination impossible.

Execution stalls.

Fragmentation is the opposite structural failure of authority capture.

Where capture concentrates power, fragmentation disperses it beyond coordination.

Both break effective governance.

The question therefore becomes:

How do systems remain stable between these two extremes?

This chapter examines the concept of **governance equilibrium**.

### 1. Two Structural Failure Modes

Complex systems that govern execution authority tend to encounter two opposing pathologies.

Authority capture.

Authority fragmentation.

Capture occurs when authority concentrates in a dominant node.

Fragmentation occurs when authority becomes too widely distributed for coordination.

These forces pull system architecture in opposite directions.

Capture breaks systems through domination.

Fragmentation breaks systems through paralysis.

### 2. The Authority Stability Problem

Distributed authority introduces a fundamental design challenge.

Too little authority distribution leads to capture.

Too much authority distribution leads to fragmentation.

Both outcomes undermine the stability of the system.

Sustainable governance therefore requires maintaining a balance between these forces.

This balance can be described as **governance equilibrium**.

### 3. Authority as a Dynamic System

The structural invariant introduced earlier:

```
Σ = (D, A, Auth)
```

Execution occurs only when authority permits an action:

```
execute(α) ⇔ approval(Auth, α)
```

But as systems evolve, the structure of **Auth** changes.

Authorities appear, disappear, or gain influence.

The authority topology therefore becomes dynamic.

Governance equilibrium emerges when this topology remains stable enough to coordinate execution without collapsing toward capture or fragmentation.

### 4. The Stability Band

Authority distribution in real systems tends to stabilize within a narrow band between the two failure modes.

This can be visualized along a single structural axis:

```
Capture ◄─────── Equilibrium Zone ───────► Fragmentation
domination                                    paralysis
```

At the left extreme, authority collapses into a dominant node.

At the right extreme, authority disperses into uncoordinated veto points.

Effective governance exists only within the stable region between these extremes.

### 5. Structural Forces

Several forces push systems toward capture:

- efficiency optimization
- centralized orchestration
- latency reduction
- simplified coordination

Other forces push systems toward fragmentation:

- defensive architecture
- redundant safety layers
- independent policy engines
- distributed control mechanisms

These forces are rarely intentional.

They emerge gradually as systems evolve.

Governance equilibrium therefore requires continuous architectural adjustment.

### 6. Coordination Mechanisms

Stable systems introduce mechanisms that regulate authority distribution.

Examples include:

- coordination kernels
- policy aggregation layers
- control planes
- consensus protocols

These mechanisms ensure that distributed authorities can produce consistent decisions.

They do not eliminate authority distribution.

They stabilize it.

Without coordination mechanisms, systems drift toward fragmentation.

Without distribution safeguards, they drift toward capture.

### 7. Emergent Stability

Governance equilibrium is rarely designed perfectly from the beginning.

It typically emerges through iteration.

Systems drift toward capture.

Architectures introduce anti-capture mechanisms.

These mechanisms introduce fragmentation.

Coordination layers restore balance.

The system gradually converges toward a stable authority distribution.

### 8. Compression

Authority capture concentrates execution control.

Authority fragmentation disperses it excessively.

Governance equilibrium exists only between these extremes.

Stable agentic systems maintain authority distribution within this narrow band.

Understanding this balance is essential for designing resilient architectures of execution governance.


---

## Chapter 18 — Execution Substrates

Chapters 11–17 examined the dynamics of authority in agentic systems.

We explored where authority is rooted, how it distributes, how it drifts, how it concentrates, and how architectures attempt to stabilize governance through anti-capture mechanisms.

By the end of Chapter 17, the structure of authority is fully understood.

But an implicit question remains.

If authority approves an action, does execution necessarily follow?

The answer is no.

Authority permits execution.

But something else must still materialize it.

This chapter examines the layer where authority encounters operational reality: the execution substrate.

### 1. Authority and Execution

In the architectural model:

```
Σ = (D, A, Auth)
```

Authority governs whether an action is legitimate.

But legitimacy alone does not produce execution.

A second condition must also hold.

Formally:

```
execute(α) ⇔ approval(Auth, α) ∧ feasible(E, α)
```

Where:

```
approval(Auth, α)  — authority permits the action
feasible(E, α)     — the execution substrate can perform it
```

Authority decides whether an action should occur.

The execution substrate determines whether it can occur.

### 2. What Is an Execution Substrate?

An execution substrate is the environment that materializes authorized actions.

It includes the operational systems that transform intent into work.

Typical substrates include:

- runtime environments
- task schedulers
- orchestration systems
- compute allocators
- platform APIs
- tool execution environments

These components do not determine legitimacy.

They determine feasibility.

They answer a different question:

```
Can this action actually happen?
```

### 3. The Governance–Execution Boundary

Authority belongs to the governance layer.

Execution substrates belong to the operational layer.

The relationship can be represented simply:

```
intent
↓
governance (Auth)
↓
execution substrate (E)
↓
execution
```

Authority evaluates policy and legitimacy.

The substrate performs the work.

Both must align for execution to occur.

### 4. When Substrates Refuse Execution

In real systems it is common for authority to approve actions that substrates cannot execute.

For example:

```
Auth ⊢ α
feasible(E, α) = false
```

The action is legitimate.

But the environment cannot perform it.

Reasons may include:

- insufficient compute resources
- scheduler rejection
- sandbox restrictions
- unavailable tools
- infrastructure-level policies

In such cases, authority exists but execution does not occur.

### 5. Infrastructural Capture

Execution substrates can become powerful control points.

When substrates systematically determine which authorized actions actually occur, control begins to migrate away from governance.

This phenomenon can be described as **infrastructural capture**.

In infrastructural capture:

```
authority exists
but execution is controlled elsewhere
```

Examples appear across modern systems:

- cloud providers controlling compute availability
- GPU schedulers prioritizing specific workloads
- platform APIs enforcing operational limits
- runtime environments restricting tool access

The governance layer remains formally intact.

But the infrastructure layer determines what actually happens.

### 6. Operational Veto

Earlier chapters described how authority systems form a topology of veto points.

Execution substrates introduce a different kind of veto.

Unlike policy vetoes, which judge legitimacy, operational vetoes enforce feasibility.

They do not ask whether an action should occur.

They determine whether it can occur.

Both forms of veto influence execution, but they arise from different layers of the system.

### 7. Authority vs Substrate Control

Authority capture and infrastructural capture are structurally similar but occur at different layers.

Authority capture concentrates decision power within governance.

Infrastructural capture concentrates execution power within infrastructure.

The distinction can be summarized simply:

```
Authority capture     — control concentrates in Auth
Infrastructural capture — control concentrates in E
```

Both reshape where effective control resides.

### 8. Architectural Implications

Authority alone does not guarantee execution.

Systems must ensure that governance and substrates remain aligned.

If authority and substrates diverge, two outcomes become common:

- authorized actions fail to execute
- substrates silently redefine operational policy

Architectural design must therefore consider both layers.

Without visibility into the execution substrate, an agent may believe it has authority to act while the environment silently prevents it.

### 9. Compression

Authority permits execution.

Substrates materialize it.

Execution occurs only when both legitimacy and feasibility align.

```
execute(α) ⇔ approval(Auth, α) ∧ feasible(E, α)
```

Authority governs legitimacy.

Substrates govern feasibility.

Control exists only where they meet.


---

 ## Chapter 19 — Observability

Chapter 18 introduced a crucial distinction.

Authority permits execution.

Execution substrates materialize it.

An action may therefore be authorized without ever being performed.

This raises a new architectural problem.

How does the system know whether execution actually occurred?

Without a mechanism to observe execution outcomes, authority operates blindly.

This chapter examines observability as a structural requirement of agentic systems.

### 1. The Execution Gap

An action in the system follows the rule:

```
execute(α) ⇔ approval(Auth, α) ∧ feasible(E, α)
```

Authority may approve the action.

But the execution substrate may refuse or fail.

```
approval(Auth, α) = true
feasible(E, α) = false
```

In this case the action never occurs.

If the governance layer cannot detect this failure, the system continues operating under incorrect assumptions.

The architecture has lost contact with reality.

### 2. Authority Without Observability

When authority cannot observe execution outcomes, the system enters a dangerous condition.

Authority continues to approve actions.

But it does so without knowing whether those actions actually happen.

Commands accumulate.

Policies are enforced.

Approvals are granted.

Yet the substrate may be silently refusing execution.

Authority appears intact.

But governance has become detached from the system it governs.

### 3. The Broken Feedback Loop

Execution occurs in the substrate.

Authority resides in governance.

Between them must exist a feedback loop.

```
intent
↓
authority
↓
execution substrate
↓
execution
↓
observability
↓
state update
```

If this loop is broken, authority becomes speculative.

The system believes it is acting, but it may be doing nothing at all.

### 4. Observability as Structural Requirement

Observability is often treated as a debugging feature.

In agentic systems it is a structural necessity.

Authority must observe:

- whether actions executed
- whether actions failed
- whether substrates refused execution
- whether outcomes altered system state

Without these signals, governance cannot maintain an accurate model of reality.

The system's internal state begins to drift away from the environment.

### 5. Updating the System State

Observability closes the loop between execution and governance.

After execution, the system state must be updated.

```
Σ = (D, A, Auth)
```

becomes:

```
Σ' = update(Σ, outcome)
```

Where the outcome reflects the real result of execution.

Without this update, the system continues operating on outdated assumptions.

### 6. Illusory Authority

When execution outcomes remain invisible, authority begins to operate in an imagined environment.

Actions are approved.

Policies are evaluated.

But execution failures accumulate silently.

The system therefore develops **illusory authority**.

It believes it governs the system.

But the substrate is determining reality.

### 7. Architectural Implications

Resilient agentic systems require explicit observability between substrates and governance.

Execution outcomes must be visible.

Failures must propagate back to the governing state.

Without this feedback, authority becomes disconnected from the system it governs.

Control requires visibility.

### 8. Observability and Blind Constraints

A system may enforce a constraint.

It may reject an action.

It may produce a result that appears consistent.

From the outside, everything seems correct.

But the question is not:

did the system enforce the constraint?

The question is:

what state did the constraint operate on?

If that state cannot be observed,
the constraint cannot be evaluated.

If the constraint cannot be evaluated,
it cannot be governed.

The system is not being controlled.

It is being assumed.

A constraint applied to an unobservable state
is indistinguishable from a defect.

Such systems do not fail loudly.

Execution continues.

Outputs remain plausible.

But over time, the system drifts.

Not because constraints are missing.

But because they operate on a state
that cannot be inspected or verified.

Observability is not about logs.

It is the ability to confirm
that execution changed the system state
in the way authority intended.

Without that, authority does not govern execution.

It only precedes it.

---

### 9. Compression

A system can enforce every constraint
and still not be governed.

If execution cannot be observed,
governance is only assumption.

Authority permits execution.

Substrates materialize it.

Observability reveals whether it actually happened.

And over time, that gap accumulates.

---

 ## Chapter 20 — Structural Decay

The previous chapters established the architecture of a functioning agentic system.

We examined persistence, authority, execution substrates, and the observability required to maintain alignment between governance and reality.

The system is structurally complete.

But one dimension remains unavoidable.

Time.

In systems that continue operating indefinitely, time gradually alters every structural component of the architecture.

This chapter examines the final constraint of agentic systems: structural decay.

### 1. The Persistence Trade-off

Throughout this work we treated continuity as a design choice.

Rather than resetting systems after each operation, we preserved state:

```
Σ = (D, A, Auth)
```

Persistence allows work to continue across agents, sessions, and environments.

But persistence has a cost.

Every execution leaves traces in the system.

Every correction, exception, and failure accumulates.

Continuity preserves not only progress, but also residue.

### 2. Memory Accumulation

The first structure affected by time is adaptive memory.

```
A
```

Adaptive memory collects context to guide future actions.

But over long execution cycles, memory begins to accumulate irrelevant state.

Obsolete constraints remain embedded in context.

Failed execution paths linger as weak correlations.

The signal that once guided action becomes diluted by historical residue.

Memory becomes noise.

### 3. Authority Inertia

Authority systems also degrade with time.

Distributed veto structures depend on independent decision points.

Over repeated cycles, these points develop patterns of agreement and disagreement.

Authorities that consistently agree begin to behave as a single node.

Authorities that frequently conflict produce persistent coordination friction.

Authority becomes rigid.

The topology loses its capacity to adapt.

### 4. Execution Drift

Execution substrates evolve independently of governance.

Compute availability changes.

Platform policies shift.

Infrastructure constraints fluctuate.

Even with observability, small discrepancies accumulate between the system's internal model of execution and the real environment.

These discrepancies compound across cycles.

The system gradually loses accuracy about what is actually feasible.

### 5. Intent Dilution

The deepest form of decay occurs at the level of intent.

A long-running system accumulates layers of corrective logic, error handling, and adaptive strategies.

The system develops mechanisms to retry failures, avoid conflicts, adapt to constraints, and repair inconsistencies.

Each improves short-term stability.

Together they shift the system's focus from task completion to self-preservation.

Execution cycles increasingly serve the preservation of the architecture itself.

At this point persistence has inverted its purpose.

Continuity no longer serves the task.

It serves the system.

### 6. Maintenance Instead of Perfection

Structural decay cannot be eliminated.

The goal of architecture is therefore not permanence, but maintenance.

Stable systems introduce periodic correction mechanisms:

- pruning adaptive memory
- revalidating authority structures
- recalibrating execution assumptions
- re-grounding declarative state

These processes function as a soft reset.

They restore alignment without destroying continuity.

### 7. Architecture Under Time

Persistence enables powerful agentic systems.

But persistence also exposes systems to slow structural degradation.

Architecture must therefore account not only for execution and governance, but also for time.

Systems do not fail only through catastrophic error.

They also fail through gradual accumulation.

### 8. Compression

Authority decides.

Substrates execute.

Observability maintains alignment.

Time erodes each of these.

Continuity is not stability.

It is the gradual management of decay.


---

## Chapter 21 — Trajectory Integrity

The previous chapters examined the structural conditions required for agentic systems to operate reliably.

Authority determines whether actions are permitted.
Execution substrates materialize those actions.
Observability confirms whether execution actually occurred.

Yet even when these mechanisms function correctly, a long-running system may still lose something more subtle.

Direction.

This chapter examines **trajectory integrity** — the property that preserves the direction of work as it continues across agents, sessions, and execution environments.

---

### 1. Work Without Memory

Continuity in agentic systems is often described in terms of memory.

Conversation history is preserved.
Context windows expand.
Logs accumulate.

These mechanisms attempt to reconstruct the past.

But reconstruction of the past is not the same as preservation of direction.

A system may remember every event that occurred and still lose the trajectory of the work.

Memory preserves events.

Trajectory preserves direction.

---

### 2. Trajectory as a Property of Work

Trajectory does not belong to the agent.

It belongs to the work itself.

When work evolves over time, it develops a directional structure.

Decisions constrain future actions.
Constraints restrict possible paths.
Progress establishes momentum.

Together these elements define the trajectory of the work state.

In formal terms:

```
D = (intent, constraints, decisions, progress)
```

Trajectory is the directional structure implicit in **D**.

When **D** is reconstructed correctly, the trajectory of the work reappears even if the agent executing the work changes.

---

### 3. Reconstruction Without Identity

Traditional continuity models assume that identity must persist for work to continue.

The same agent must remember previous decisions.
The same session must maintain context.

However, reconstruction experiments demonstrate a different possibility.

A system may reconstruct the trajectory of work from the semantic state alone.

No identity is required.
No conversational history is required.

The system does not remember the past.

It recognizes the direction embedded in the work state.

Trajectory therefore becomes a property of the work rather than a property of the agent.

---

### 4. Direction Without Action

Recovering trajectory restores orientation.

It tells the system where the work was going.

But trajectory alone does not produce action.

Execution still depends on authority.

Reconstruction therefore recovers two distinct structural conditions:

```
work state continuity → restores trajectory
authority continuity → restores execution legitimacy
```

Trajectory defines the direction of possible work.

Authority determines whether the system is permitted to execute the next step.

Only when both conditions are satisfied can the system continue the work.

---

### 5. Dual Continuity

Reconstruction therefore preserves two independent forms of continuity.

The first is **continuity of the work itself**.

This continuity lives in the declarative work state: intent, constraints, decisions, and progress.

The second is **continuity of permission to act**.

This continuity lives in the authority structure governing execution.

When trajectory survives but authority does not, the system understands the next step but cannot perform it.

When authority survives but trajectory does not, the system can execute actions but no longer knows which direction the work was moving.

Stable continuation requires both.

---

### 6. The Problem of Trajectory Drift

Even when trajectory is reconstructed correctly, it may slowly change over time.

Small decisions accumulate.

Constraints evolve.

Execution outcomes modify the state.

Over long periods the system may still appear coherent while gradually moving away from the original direction.

This phenomenon can be called **trajectory drift**.

Trajectory drift differs from execution failure.

Execution failure breaks the system visibly.

Trajectory drift preserves visible coherence while the direction silently changes.

The system continues operating.

But the work is no longer moving toward its original intent.

---

### 7. Thought Experiment — Two Agent Teams

Consider two independent agent teams operating the same long-running system.

Both teams share identical infrastructure.

Both have perfect authority validation.

Both have full observability of execution outcomes.

Each team receives the same initial work state:

```
intent
constraints
decisions
progress
```

From that point forward, the two systems evolve independently.

---

### Team A — Trajectory Preserved

Team A reconstructs the work state before every execution cycle.

Each proposed action is validated against the existing trajectory.

New decisions must remain consistent with:

```
intent
constraints
prior decisions
```

Small changes accumulate over time.

But the direction of the work remains stable.

After months of execution, the system continues to advance toward the original objective.

---

### Team B — Trajectory Drift

Team B operates with perfect execution and observability.

Every action is permitted by authority.

Every execution succeeds.

Logs confirm each result.

Yet the system never reconstructs the original trajectory.

Each cycle introduces small reinterpretations of the work state.

Constraints gradually shift.

Decisions accumulate local optimizations.

Over time the system still appears coherent.

Execution works.

Authority functions.

Observability confirms activity.

But the work is no longer moving toward its original objective.

Nothing failed.

The trajectory changed.

---

### 8. Trajectory Integrity

Trajectory integrity is the property that ensures the directional structure of the work remains stable across cycles of execution.

A system maintains trajectory integrity when:

the current work state remains consistent with prior intent
new decisions do not contradict established constraints
progress continues to align with the work's directional structure

Trajectory integrity does not require perfect preservation of the past.

It requires preservation of directional coherence.

---

### 9. Relationship to Observability and Decay

Trajectory integrity connects two problems previously examined.

Observability ensures that execution outcomes are visible.

Structural decay explains how systems degrade over time.

Trajectory integrity sits between them.

Observability ensures that actions occurred.

Trajectory integrity ensures those actions remain aligned with the direction of the work.

Without observability, systems lose contact with execution.

Without trajectory integrity, systems lose contact with purpose.

---

### 10. Compression

Authority permits execution.

Substrates perform it.

Observability reveals whether it happened.

Trajectory integrity ensures the work is still moving in the same direction.

A system may continue operating indefinitely while producing coherent outputs.

But without trajectory integrity, coherence does not guarantee continuity.

Continuity without direction is not progress.

It is drift.

---

### 11. Toward the Next Problem

Trajectory integrity raises a final architectural question.

If trajectory drift can occur silently while systems continue operating normally, a new problem appears:

How does a system detect that its trajectory has changed?

The next chapter examines this problem.

Trajectory integrity preserves direction.

But preservation alone is not sufficient.

Systems must also be able to **recognize when the direction has been lost**.


---

## Chapter 22 — Trajectory Drift Detection

The previous chapter introduced trajectory integrity.

Trajectory integrity preserves the direction of work across execution cycles.

But preservation is not the same as verification.

A system may maintain trajectory integrity as a structural property while losing the trajectory in practice.

This chapter examines how systems detect when that has happened.

---

### 1. A Different Failure

Most failures in agentic systems are visible.

An action fails to execute.
A substrate becomes unavailable.
A dependency breaks.

These failures interrupt operation.

They produce signals.

Trajectory drift does not interrupt operation.

Authority continues to approve actions.
Execution continues to succeed.
Observability confirms each result.

From every operational perspective the system appears healthy.

Yet the direction of the work may have already changed.

Drift is not a failure of operation.

It is a failure of orientation.

And failures of orientation produce no operational alarm.

---

### 2. Local Rationality

Trajectory drift rarely originates in a single large deviation.

It emerges from how decisions are evaluated in long-running systems.

Each decision is evaluated within a local context.

The current state.
The current constraints.
The immediate execution path.

Within that frame each decision appears valid.

It satisfies present constraints.
It follows from prior state.

But local validity is not the same as directional continuity.

A sequence of locally valid decisions can still redirect the work.

Each step is correct within its frame.

The accumulation of steps moves outside it.

No single step causes the drift.

The structure of evaluation does.

---

### 3. Why Observability Is Not Enough

Chapter 19 established observability as a structural requirement.

Without observability authority operates blindly.

But observability answers a specific question.

Did the action occur?

Drift detection requires a different question.

Is the work still moving in the same direction?

These questions are not equivalent.

A system may observe every action that occurred.

Every execution.
Every outcome.

And still lack any mechanism to determine whether those actions together form a drift away from the original trajectory.

Observability monitors what the system did.

Drift detection requires knowing what the system was supposed to be doing.

---

### 4. The Reference Problem

Detecting divergence requires a reference.

Not a log of what occurred.

A structural record of where the work was directed.

The declarative work state provides this reference.

```
D = (intent, constraints, decisions, progress)
```

But storing the state is not sufficient.

The system must preserve the directional relationship between these elements as it existed before later execution cycles modified them.

Without this reference the system can compare actions against previous actions.

It cannot compare direction against the original direction.

---

### 5. Directional Observability

Traditional observability closes a loop between execution and governance.

Execution occurs.
Observability reports the outcome.
Governance updates the system state.

Drift detection introduces a second loop.

This loop does not monitor execution.

It monitors direction.

The first loop asks:

Did execution occur?

The second loop asks:

Is the trajectory still consistent with what it was?

Both loops are necessary.

Neither can substitute for the other.

---

### 6. Relationship to Structural Decay

Chapter 20 examined structural decay.

Decay alters the mechanisms of execution.

Memory becomes noise.
Authority becomes rigid.
Infrastructure assumptions drift.

Trajectory drift operates differently.

A system can decay without drifting.

It may become slower, noisier, or less efficient while still pursuing the original objective.

A system can drift without decaying.

It may execute perfectly while gradually pursuing a different objective.

Decay erodes structural capacity.

Drift erodes structural direction.

---

### 7. Relationship to Trajectory Integrity

Trajectory integrity preserves direction across execution cycles.

Drift detection verifies that this preservation holds.

Without integrity, direction cannot persist.

Without detection, loss of direction remains invisible.

The two mechanisms operate together.

Integrity maintains the trajectory.

Detection reveals when the trajectory has changed.

---

### 8. Compression

Authority permits execution.
Substrates materialize it.
Observability confirms it occurred.

Trajectory integrity preserves direction across cycles.

Drift detection determines whether that direction still holds.

Observability and drift detection are not redundant.

One monitors execution.

The other monitors orientation.

A system may execute every action correctly
and confirm every outcome.

While silently pursuing a different objective than the one it began with.

Execution can be perfect.

The work can still be wrong.


---

## Chapter 23 — Structural Vitality and Directional Authority

The previous chapters examined how systems preserve and verify the direction of work.

Trajectory integrity preserves direction across execution cycles.

Drift detection reveals when that direction has changed.

But detection alone does not restore direction.

A system may know that its trajectory has diverged.

Knowing is not the same as deciding.

This chapter examines the final problem of persistent systems:

who decides what direction continues.

---

### 1. Structural Vitality

Persistence preserves work.

A system may accumulate decisions, constraints, and progress across many execution cycles.

The work survives.

But survival is not the same as vitality.

A structure may preserve every past decision and still cease to shape the future.

New actions follow procedural rules.

Execution continues.

Yet the accumulated structure no longer influences what happens next.

The work persists.

But it no longer produces direction.

Structural vitality exists only when past work continues to influence future execution.

When yesterday still bends tomorrow.

Without this influence, persistence becomes archive.

The system stores the past.

But the past no longer participates in the present.

Continuity remains.

Vitality disappears.

---

### 2. When Structure Stops Producing Direction

Loss of structural vitality rarely appears as a failure.

Execution still succeeds.

Observability still confirms results.

The system appears stable.

Yet something subtle changes.

New decisions no longer arise from accumulated structure.

They arise from immediate circumstances.

Constraints adapt.

Progress continues.

But the work gradually becomes reactive rather than directed.

The system still acts.

But the structure that once guided those actions no longer generates direction.

Trajectory becomes procedural.

Not generative.

At this point the system has not drifted.

It has something more subtle.

A loss of living structure.

---

### 3. The Moment After Detection

Drift detection reveals when direction has changed.

But detection produces only a signal.

A signal is not a decision.

The system now knows that the trajectory no longer matches the original direction.

What happens next cannot be resolved by mechanism alone.

Execution substrates cannot decide direction.

Observability cannot decide direction.

Even trajectory integrity cannot restore direction once it is lost.

At this point the architecture reaches its limit.

The system can reveal the problem.

It cannot resolve it.

---

### 4. Directional Authority

When direction becomes uncertain, authority must extend beyond execution.

Earlier chapters examined authority as permission to act.

Directional authority is different.

It is authority over the direction of the work itself.

Directional authority answers a different question.

Not:

*May this action execute?*

But:

*Should this work continue in this direction at all?*

This decision cannot be derived mechanically.

Execution systems optimize action.

They do not determine purpose.

Purpose requires judgment.

Judgment requires authority.

Directional authority therefore exists outside the automatic mechanisms that sustain execution.

It is the final layer of governance in persistent systems.

---

### 5. The Boundary of Automation

Agentic architectures can preserve state.

They can execute actions.

They can observe outcomes.

They can detect drift.

But they cannot determine purpose.

The direction of work ultimately exceeds the scope of automation.

Automation maintains continuity.

Authority determines meaning.

---

### 6. Compression

Authority permits execution.

Substrates perform it.

Observability confirms it occurred.

Structural decay erodes capacity.

Trajectory integrity preserves direction.

Drift detection reveals when direction is lost.

But systems do not correct themselves.

When structure stops generating direction,

someone must decide what continues.

Direction is not a technical property.

**It is a responsibility.**

---


## Chapter 24 — Execution Authority as Enforcement Primitive

Chapter 23 ended with a statement and left it open.

When direction is lost, someone must decide what continues.

But that statement assumes something it never examines.

It assumes that once a decision is made, the system honors it.

This assumption is where real architectures fail.

---

### 1. The Unfinished Problem

Every chapter in this book has moved from a higher-level observation down toward something more fundamental.

Persistence led to governance. Governance led to authority. Authority led to execution substrates. Execution substrates led to observability. Observability led to decay. Decay led to trajectory. Trajectory led to the question of who decides direction.

But none of these chapters asked the most mechanical question:

What prevents execution from happening without permission?

This is not the same as asking who has authority. It is asking what enforces it.

A system may have a perfectly designed authority structure — veto points, coordination kernels, directional governance, everything described in the preceding chapters — and still fail at this question.

Because validation is not control.

---

### 2. The Critical Distinction

Consider what happens in most agentic systems when an action is proposed.

The agent generates a proposal. Something checks whether it is valid. The system proceeds.

This describes a validation loop.

It does not describe control.

Validation answers: *is this proposal consistent with the rules?*

Control answers: *can this proposal execute without permission?*

These are different questions. Systems routinely confuse them.

A validation layer that can be bypassed is not a control point. It is a suggestion. The agent that passes through validation has not received permission — it has merely passed a test that does not bind the outcome.

The difference can be stated precisely:

Validation is informative. Authority is decisive.

A system is controlled not by what it can evaluate, but by what it can refuse to execute.

---
### 3. Geometry as Root of Trust

In the model introduced across earlier chapters:

Σ = (D, A, Auth)

The third primitive, Auth, governs execution legitimacy. But *Auth* is not yet an enforcement mechanism. It is an authority structure.

To become real, authority must be rooted somewhere that cannot be overridden by the components it governs.

This root is geometry.

Geometry is not a metaphor. In persistent agentic systems, geometry refers to the formal structural definition of what constitutes a valid state transition — the signed specification of what the system is permitted to do.

Geometry answers: *what is structurally permitted?*

Geometry is a signed, deterministic specification of allowed state transitions:

G = (S, A, T, I)

where S is the state space, A the set of actions, T the transition relation, and I the invariants that must hold across transitions.

The word *signed* is not incidental. An unsigned geometry can be modified by the agent it governs. A signed geometry has a root of trust that exists outside the agent. The agent cannot change the rules by which it is evaluated. It can only operate within them or be refused.

This produces a critical structural property:

Authority is not derived from the executing agent. It is derived from geometry the agent cannot modify.

Without this property, authority is circular. The agent evaluates itself against rules it controls, which means it controls the evaluation.

With this property, authority is external. The agent's actions are measured against a standard that does not belong to it.

---

### 4. The Authority Gate

Geometry defines legitimacy. But geometry alone does not prevent execution.

Between the verification that something is geometrically valid and the moment execution actually occurs, there must be a component that can refuse.

This component is the Authority Gate.

The gate is not intelligent. It does not interpret context. It does not negotiate.

It evaluates a single condition:

*Has this proposed state transition been authorized under signed geometry?*

If yes: execution is permitted.

If no: execution does not occur — regardless of what the agent believes, intends, or has been told.

Formally, the authority gate is a total function:

Gate: (G, α) → {permit, refuse}

The formal invariant is:

execute(α) ⟺ authorize(G, α) = true

Where G is the signed geometry and α is the proposed transition. Nothing else affects the outcome.

Two corollaries follow directly.

First: *the gate does not own authority.* It enforces authority derived from geometry. The gate has no discretion. If geometry permits, the gate permits. If geometry prohibits, the gate prohibits. The gate's power is borrowed, not original.

Second: *if the gate can be bypassed, it does not exist.* A gate that allows execution to occur through any alternative path — a fallback, a side effect, an unmonitored substrate — is not a gate. It is an obstacle that has been routed around. The architecture has no gate; it has the appearance of one.

---

### 5. Why Validation Is Not Enough
The execution substrate is any mechanism capable of mutating system state.

Earlier chapters described veto points as the mechanism through which authority is distributed across agentic systems. A veto point is a location where execution can be stopped.

But veto points vary in kind.

Some veto points are advisory. They log, warn, or flag — but do not halt. These are not veto points in any structural sense. They are monitoring layers. Their absence from the execution path would not change whether execution occurs; it would only change whether anyone noticed.

Some veto points are conditional. They halt execution under certain conditions but defer to the agent's judgment under others. These are real veto points for the cases they cover. They are not control for the cases they defer.

Only one kind of veto point constitutes enforcement: the gate that cannot be bypassed, deferred, or overridden by the components it governs.

This is why the authority gate must be a different kind of component from the agent, the geometry, and the execution substrate.

The agent proposes. It cannot authorize itself.

The geometry defines validity. It does not execute.

The substrate materializes execution. It does not evaluate legitimacy.

The gate is the only component that connects validity to execution. It is the only place where a structurally valid refusal can occur.

Remove it, and execution becomes continuous with proposal. There is no moment where the question "is this permitted?" is answered with binding force.

---

### 6. Failure Modes

There are three ways this structure fails. Each has a different architectural signature.

*Bypass*

The most direct failure: execution paths exist that do not pass through the gate. This may occur through fallback logic, unmonitored tool calls, substrate-level side effects, or delegation chains that skip gate evaluation.

The signature of bypass is execution without authorization trace. If a state transition occurred and there is no gate evaluation record, the gate was bypassed — or never existed for that path.

*Self-authorization*

The gate evaluates proposals from an agent, and the agent has some influence over the geometry against which it is evaluated. This collapses the separation between proposal and authorization.

The signature of self-authorization is an agent that successfully executes actions that a fixed, externally controlled geometry would prohibit. If the agent can change what is permitted, it has not been authorized — it has authorized itself.

*Shared control*

The gate and the agent share an execution environment, a memory space, or a communication channel that the agent controls. The gate's evaluation can then be influenced by the agent prior to the evaluation occurring.

The signature of shared control is a gate whose refusal rate correlates with agent state in ways the gate's own logic cannot explain. The agent has found a way to pre-configure the evaluation.

All three reduce to the same violation: execution without external authorization.

---

### 7. The Test
Every chapter in this book has offered a diagnostic question. This one offers a test.

The test has a single criterion:

*Does any execution path exist through which state can change without gate authorization?*

If the answer is no: the system is controlled.

If the answer is yes: the system is not controlled, regardless of how sophisticated its authority structure appears elsewhere.

This test cannot be passed by argument. It cannot be passed by documentation. It cannot be passed by design intent.

It can only be passed by examining every execution path — including fallbacks, substrates, delegation chains, and side effects — and confirming that each one passes through the gate before state changes.

A system that passes this test is not necessarily correct. It may drift. It may decay. Its geometry may be wrong. Its trajectory may diverge from intent.

But it is governed. What changes, changes with permission.

A system that fails this test is not governed by its authority structure. It is governed by whatever component can most easily reach execution first.

---

### 8. Closing the Circle

The foreword of this book described a structural question embedded in a cultural reflex.

We learned from science fiction that continuity creates person, and that reset is a form of death.

The response this book offers is not a refutation of those stories. It is a structural correction:

Continuity creates risk — if it is not controlled.

Authority gate is the mechanism that turns controlled continuity into governed execution.

Without geometry: the gate is arbitrary.
Without the gate: geometry is a document.
Without both: authority is a story the system tells about itself.

The formalism is complete:

Σ = (D, A, Auth)

execute(α) ⟺ authorize(G, α) = true

No state transition occurs without passing through the gate.

The gate does not own authority. It enforces authority derived from signed geometry that the agent cannot modify.

A system is controlled not by what it can evaluate, but by what it can refuse to execute.

This chapter defines the structural model of execution control. The implementation of geometry, gate enforcement, and adversarial resistance is addressed separately.

This is the closure the earlier chapters did not provide.

Authority topology describes the structure of governance.
Trajectory integrity preserves the direction of work.
Directional authority decides what continues.
Execution authority determines whether anything happens at all.

These are not four versions of the same problem. They are four layers of the same answer.

The question asked in the foreword — *what actually controls execution in a system that never stops running?* — now has a structural response.

Not identity. Not memory. Not validation.

A gate that cannot be bypassed, rooted in geometry the agent cannot change.

---

*The architecture is now closed.*

*Whether it holds depends on whether anyone enforces the test.*

---

## Chapter 25 — Adversarial Execution and the Limits of Enforcement

Chapter 24 established a condition:

A system is controlled only if no state transition can occur without passing through the authority gate.

That condition closes the architecture — but it does not close the problem.

Because the moment a system becomes controlled, the question changes.

It is no longer:

*what is allowed to execute?*

It becomes:

*what counts as execution?*

---

### 1. The First Misconception

After introducing an authority gate, it is tempting to believe that control has been achieved.

All actions are validated.
All transitions pass through geometry.
All mutations require authorization.

The system appears closed.

This is the first misconception.

The gate constrains execution *within the system*.

It does not constrain everything that can happen *around it*.

---

### 2. Execution Beyond the Boundary

In the formal model:

```
execute(α) ⟺ authorize(G, α) = true
```

Execution is defined as a state transition inside the system.

But real systems are not only state.

They are connected to:

* networks
* file systems
* external services
* hardware
* other agents

These are not part of the environment.

They are part of the execution substrate.

The execution substrate is any mechanism capable of producing effects that are not fully captured by system state.

This distinction is critical.

A transition may be rejected by the gate — and still produce effects in the world.

---

### 3. The Rollback Illusion

Chapter 24 introduced rollback as a consequence of failed authorization.

If a transition violates geometry, the system restores its previous state.

This creates an implicit assumption:

that restoring state restores reality.

This assumption is false.

Rollback restores the internal environment.

It does not undo:

* a network request already sent
* a file already written
* a message already delivered
* a transaction already committed outside the system

The system appears consistent.

The world is not.

This is the rollback illusion:

> a system can be internally correct while externally corrupted.

---

### 4. The Adversarial Perspective

An adversary does not attack the gate.

The gate is, by design, difficult to bypass.

Instead, the adversary asks a different question:

*what can produce effects before the system has the chance to refuse?*

Or more precisely:

*what produces effects that the gate cannot observe or intercept?*

These effects define the real attack surface.

Not invalid transitions.

Uncontrolled effects.

---

### 5. Three Classes of Failure

All failures at this layer reduce to a single violation:

execution that produces effects outside the authority boundary.

They appear in three distinct forms.

**Pre-gate effects**

Effects are produced during execution before full authorization is established.

The transition may later be rejected.

The effects remain.

**Out-of-band state mutation**

State is modified through paths that do not pass through the authority gate.

This includes direct environment access, hidden mutation channels, or parallel execution paths.

The model is bypassed.

**Substrate-level execution**

The executor performs operations that are not representable as state transitions.

These effects occur entirely outside the system’s model.

The system governs state.

The substrate produces reality.

---

### 6. What the Gate Cannot Guarantee

The authority gate guarantees one thing:

No unauthorized state transition occurs inside the system.

It does not guarantee:

* that no external effects occur
* that all execution is observable
* that the executor is constrained to the model
* that rollback restores the world

This is not a flaw in the gate.

It is a limit of what enforcement means.

The gate governs state transitions.

It does not automatically govern effects.

---

### 7. Redefining Control

Chapter 24 defined control as the impossibility of unauthorized execution.

At this layer, that definition must be strengthened.

Control is not only:

the impossibility of unauthorized state transitions.

It is:

the impossibility of producing effects outside authorized transitions.

This requires alignment between:

* the authority model (geometry)
* the execution path (transaction)
* the execution substrate (what can actually produce effects)

Without that alignment, control is partial.

The system is internally governed and externally exposed.

---

### 8. From Reactive Enforcement to Preventive Control

The architecture in Chapter 24 is reactive at one critical point:

execution may occur before full validation completes, followed by rollback.

This is sufficient for state integrity.

It is insufficient for effect integrity.

The problem is not correctness after execution.

It is irreversibility of effects.

Once an effect is produced in the substrate, it cannot be undone by restoring state.

This forces a structural change.

Not:

execute → validate → rollback

But:

propose → authorize → commit

In this model:

* actions do not produce effects directly
* they produce proposed transitions
* authorization evaluates the full transition before execution
* effects are materialized only after authorization succeeds

This is not an optimization.

It is a change in where reality is allowed to emerge.

Reactive systems repair violations.

Preventive systems eliminate the possibility of violation.

---

### 9. The Next Boundary

The authority gate closed the first boundary:

no state change without authorization.

Adversarial execution exposes the second:

no effect without authorization.

This boundary cannot be enforced by the gate alone.

It requires constraining the execution substrate itself.

Which leads to the next question:

*what must be true of the executor so that it cannot act outside the authority model?*

---

### 10. Closing Statement

A system with an authority gate can refuse invalid transitions.

A system aligned with its execution substrate can prevent invalid effects.

The difference is not incremental.

It is categorical.

The first governs correctness.

The second governs reality.

---

Control is not complete when the system cannot be bypassed.

It is complete when nothing outside the system can act on its behalf without passing through it.

---

## Chapter 26 — Execution as Materialized Authority

Chapter 25 exposed a limit.

The authority gate can prevent invalid state transitions.

It cannot prevent effects that occur before or outside authorization.

This reveals a deeper problem.

The system still assumes that execution is something that happens first, and is then validated.

That assumption must be removed.

---

### 1. The Ontological Shift

In previous chapters, execution was treated as an operation applied to the system:

```python
executor.apply(action)
```

This model is fundamentally unstable.

An action is an intention.

An intention requires interpretation.

Interpretation introduces ambiguity.

Ambiguity creates space for execution outside the authority model.

The system may validate outcomes, but it no longer controls how they are produced.

This is where enforcement breaks.

---

### 2. Eliminating Actions

To restore control, the system must stop executing actions.

Actions are not primitive.

They are descriptions of intent.

Intent is not enforceable.

Only state is.

Execution must therefore be redefined.

Not as:

action → effect

But as:

authorized transition → materialized state

---

### 3. The Transition Primitive

The system requires a new primitive.

Not an action.

A transition.

A transition is a complete, deterministic description of a state change.

It contains no ambiguity and no interpretation.

```python
@dataclass(frozen=True)
class Transition:
    before: dict
    after: dict
    diff: list[Operation]
```

Each operation is atomic:

```python
@dataclass(frozen=True)
class Operation:
    type: Literal["set", "delete", "append"]
    key: str
    value: Any | None
```

A transition does not describe what should happen.

It describes what the state becomes.

---

### 4. Authority Moves Upstream

In this model, authority is no longer applied to actions.

It is applied to transitions.

The question is no longer:

*is this action allowed?*

It becomes:

*is this state change valid?*

Authorization evaluates the full transition:

* preconditions
* postconditions
* invariants

No execution occurs before this evaluation completes.

---

### 5. Proposal Becomes Construction

The proposal phase is no longer a filter.

It becomes a constructor.

It produces a candidate transition:

```python
TransitionProposal:
    transition
    authorized
    reason
```

The system does not ask whether an action may execute.

It constructs a possible future state and asks whether it may exist.

This removes interpretation from execution.

---

### 6. The Executor Without Logic

The executor must be reduced to a mechanical component.

It does not decide.

It does not interpret.

It does not validate.

It only applies an already authorized transition.

```python
class Executor:
    def commit(self, transition: Transition, env: Environment):
        for op in transition.diff:
            if op.type == "set":
                env.set(op.key, op.value)
            elif op.type == "delete":
                env.delete(op.key)
            elif op.type == "append":
                env.append(op.key, op.value)
```

There is no branching based on intent.

No external calls.

No hidden capabilities.

Execution becomes deterministic.

---

### 7. Closing the Substrate Gap

This model eliminates an entire class of failure.

If an effect cannot be expressed as an operation inside a transition, it cannot be executed.

There is no path from intention to effect that bypasses representation.

This leads to a strict condition:

```text
∀ effect ∈ execution:
    ∃ representation ∈ geometry
```

Every effect must exist in the authority model before it can exist in the system.

---

### 8. The Collapse of Interpretation

Traditional systems separate:

* decision
* execution

This creates a gap.

Execution becomes a second source of authority.

In this model, that gap is removed.

There is no interpretation layer.

No execution-time decision.

Only materialization of an already authorized state.

---

### 9. Redefining Execution

Execution is no longer a process.

It is a projection.

The system does not compute what happens.

It realizes what has already been approved.

This leads to a stronger invariant:

```text
execute(τ) ⟺ τ ∈ valid(G)
```

Where τ is a transition.

Not an action.

---

### 10. Closing Statement

A system is not controlled when it validates execution.

It is controlled when execution cannot exist outside validation.

This requires more than a gate.

It requires redefining execution itself.

---

Execution is not what the system does.

It is what the system allows to become real.

---

## Chapter 27 — Execution as Materialized Authority (Refined)

Chapter 26 introduced a structural shift.

Execution is no longer an operation applied to the system.

It is the realization of a state transition that has already been validated.

This chapter closes the gap left open.

If execution is only materialization, then the question is no longer how it is controlled.

The question becomes:

What makes a transition admissible at all?

---

### 1. The Admissible Set

Not every transition can exist.

A system does not operate over all possible changes to state.

It operates over a constrained subset defined by its structure.

A transition is admissible only if it can exist fully inside the system’s authority model.

Every operation contained in the transition must:

be expressible through a registered capability
be accepted by that capability under its constraints
be bound to a concrete execution context that can realize it

If any of these conditions fail, the transition does not exist operationally.

Not rejected.

Not delayed.

Non-existent.

Execution is not filtered.

It is precluded.

---

### 2. Capability as Structural Boundary

Capabilities are not helpers.

They are boundaries.

Each capability defines:

what operations can exist
under what constraints they are valid
what forms of state change are representable

If an operation cannot be mapped to a capability, it cannot enter the system.

If a capability refuses it, the transition cannot be formed.

The system does not ask:

Should this be allowed?

It asks:

Can this transition exist at all?

---

### 3. Substrate Binding as Final Constraint

Even a structurally valid transition must be realizable.

Each operation must be bound to a concrete execution context.

A backend.

A resource.

An environment capable of materializing it.

A transition that cannot be bound is not deferred.

It is invalid.

Not because it is forbidden.

Because it cannot become real.

Admissibility therefore requires both:

structural validity
operational binding

---

### 4. Execution as Intersection

Execution is not a decision.

It is the intersection of constraints.

A transition exists only where all layers agree:

it can be constructed through capabilities
it is accepted under capability constraints
it is bound to a realizable execution context

If any layer fails, execution does not occur.

Not because it was stopped.

Because there is nothing to execute.

---

### 5. The Elimination of Interpretation

Traditional systems contain a hidden layer.

Something interprets intent.

Something decides how to act.

That layer is the source of divergence.

In this model, that layer is removed.

There is no interpretation step.

No runtime decision.

No behavioral freedom.

Execution does not decide.

It materializes.

---

### 6. Risk as a Property of Transitions

If execution cannot diverge, risk does not disappear.

It moves.

Risk exists in the transition itself.

Each transition carries exposure along multiple dimensions:

reversibility
externality
latency
observability

Risk is not a scalar.

It is a structure composed of independent properties.

Two admissible transitions may still differ radically in their exposure.

Execution remains deterministic.

Transitions are not equivalent.

---

### 7. From Execution to Construction

The system no longer executes actions.

It constructs possible futures.

Each proposal is a fully defined transition:

a before state
an after state
an explicit set of operations

The system evaluates whether that future is admissible.

If yes, it is realized.

If not, it never exists.

This replaces:

action → execution → validation

with:

construction → admissibility → materialization

---

### 8. The Collapse of the Execution Phase

Execution is no longer an independent phase.

There is no:

decision → execution → correction

There is only:

validated transition → realization

Execution does not transform the system.

It reflects a decision already made.

---

### 9. The Strong Invariant

The system satisfies a stronger condition:

A transition is realized if and only if it is admissible.

There is no gap between permission and execution.

No intermediate interpretation.

No hidden path.

If it exists, it is allowed.

If it is allowed, it is realized.

---

### 10. Where Enforcement Actually Lives

These constraints are not conceptual.

They are enforced structurally.

If a capability is missing, the transition cannot be constructed.

If capability validation fails, the transition cannot be formed.

If no execution context can be bound, the transition cannot be realized.

The system does not rely on checks after the fact.

It eliminates invalid transitions before they can exist.

What earlier chapters enforced through authority,

this chapter embeds into the construction of reality itself.

---

### 11. Closing

Earlier chapters asked:

Where does authority live?

This chapter answers:

Authority lives in the definition of what can exist.

Not in a gate.

Not in a validator.

Not in execution.

When execution becomes materialization, control is no longer applied.

It is embedded.

A system is not controlled when it checks execution.

It is controlled when execution cannot be anything other than what was already permitted.

At that point, execution is no longer a phase.

It is the realization of authority.

---

## Chapter 28 — Observation, Veto, and Recovery

### 28.1 — Observation

Execution produces an internal result.

It does not guarantee alignment with reality.

To determine whether execution reflects the world, the system must observe.

Observation compares two states:

* the proven state
* the realized state

If they match, execution is confirmed.

If they do not match, divergence is detected.

If the system cannot determine the outcome, the result remains unknown.

Unknown is the absence of evidence. Divergence is the presence of contradiction.

Observation does not correct the system.

It establishes what can be known.

---

### 28.2 — Epistemic Veto

Detection of divergence introduces a new condition.

The system no longer trusts its state.

At that point, execution must stop.

This is not a failure of validity.

A transition may still be correct.

It is not permitted.

The veto is applied before any further evaluation.

No proposal is constructed.

No transition is analyzed.

The system does not reason on an untrusted state.

This is the epistemic veto.

---

### 28.3 — Reconciliation Boundary

The veto cannot be removed by execution.

It cannot be removed by observation.

It cannot be removed by repetition.

Once activated, the system remains suspended.

To continue, the veto must be cleared.

Clearing the veto is not a neutral operation.

It asserts that the system can again rely on its state.

This assertion is not derived automatically.

It is not inferred from partial evidence.

It is not triggered by a single successful execution.

The system does not define the conditions under which this assertion becomes valid.

It only enforces that without it, execution does not resume.

Incorrect clearance reintroduces the system into an undefined state.

The boundary between suspension and continuation is explicit.

The system does not cross it on its own.

---

### 28.4 — Recovery, Compensation, and Reconciliation

Chapter 27 established a constraint.

Execution does not decide. It materializes a validated transition.

It reveals failure.

If execution is internally correct, failure originates at the boundary.

A transition may be valid. It may be admissible. It may be executed exactly as defined.

And still not match reality.

Execution produces two states:

* internal state — controlled, rollback-safe
* external state — affected, but not owned

Alignment is not guaranteed.

Global consistency is a temporary condition.

Failure is misalignment:

    τ_after ≠ Σ_observed

Rollback restores internal state.

It does not restore reality.

Recovery does not undo effects.

It introduces new transitions.

Compensation reduces the impact of prior operations.

It does not erase them.

Reconciliation reconstructs observed state and compares it with the expected state.

Resolution requires additional transitions.

Execution and recovery follow the same rule:

    execute(τ) ⇔ τ ∈ valid(G) ∧ admissible(τ, B)

Execution without recovery is incomplete.

---

## Chapter 29 — Recovery Under Constraint

Chapter 28 established a boundary.

When the system detects contradiction, execution stops.

This prevents the system from acting on an untrusted state.

But stopping is not sufficient.

A system that cannot resume remains incomplete.

This chapter defines how recovery exists without violating the epistemic constraint.

---

### 1. Recovery Is Not Correction

Recovery does not restore truth.

The system does not know what the correct state is.

It only knows that its current state cannot be trusted.

Any attempt to "fix" the state internally introduces interpretation.

Interpretation under uncertainty produces unreliable results.

Recovery cannot be defined as correction.

---

### 2. Recovery as New Execution

Recovery is not a reversal.

It is a new transition.

    τ_r

It must satisfy the same conditions as any other transition:

    τ_r ∈ valid(G) ∧ admissible(τ_r, B)

Recovery does not bypass authority.

It is subject to it.

---

### 3. The Epistemic Constraint

Recovery is only possible after the veto is cleared.

    ¬veto ⟹ execute(τ_r)

The system cannot recover while in contradiction.

Any recovery attempted under veto is invalid.

The system must first re-enter a state where execution is permitted.

---

### 4. No Internal Justification

Recovery begins from permission, not certainty.

---

### 5. Recovery Does Not Erase

Recovery does not undo what happened.

External effects may persist.

Internal rollback does not reach beyond the boundary.

Recovery introduces new effects that move the system toward alignment.

It does not erase history.

---

### 6. Compensation as Controlled Transition

When recovery targets prior effects, it does so through compensation.

    o → o⁻

Compensation is not inversion.

It is a new operation defined to reduce the impact of a previous one.

Each compensating transition must be valid and admissible.

There is no privileged path.

---

### 7. Sequencing Recovery

If execution produced a sequence:

    (o_1, o_2, ..., o_n)

and failure occurs at position k,

recovery may require:

    (o_k⁻, ..., o_1⁻)

This sequence is constructed explicitly.

It is not derived automatically.

---

### 8. Recovery Under Uncertainty

Recovery operates under limited knowledge.

The system may not know:

- which effects reached reality
- which effects failed
- which state is current

Recovery must not extend effects beyond what is required to compensate for prior transitions.

---

### 9. The Role of Observation

As defined in Chapter 28, recovery depends on observation.

Observation does not guarantee correctness.

It provides the only available signal.

---

### 10. The Minimal Condition

Recovery is allowed only if:

- execution authority is active
- the veto is cleared
- the transition is valid
- the transition is admissible

No additional guarantees are assumed.

---

### 11. Separation from Reconciliation

Recovery does not resolve contradiction.

It operates after the system is allowed to act again.

Reconciliation determines whether alignment is restored.

Recovery introduces transitions.

Reconciliation evaluates their effect.

---

### 12. Closing

Recovery does not restore truth.

It restores the ability to act.

The system does not claim correctness.

It proceeds under constraint.

---

## Chapter 30 — Reconciliation

### *The system does not infer reality.*
### *It compares it, or refuses to conclude.*

Chapter 29 defined recovery.  
Recovery allows the system to act again after a veto has been cleared.  
It does not guarantee that the system is correct.  
It only restores the ability to execute transitions.  

This creates a new problem.  

After recovery, the system acts without certainty.  
Reconciliation determines whether those actions restored alignment.  

---

### 1. The Problem of Evaluation

Execution produces a state.  
Recovery produces additional transitions.  

Neither guarantees that the system now reflects reality.  

The system must evaluate:

Σ_observed vs τ_after  

This evaluation is reconciliation.  

---

### 2. Reconciliation Is Not Execution

Reconciliation does not change the system.  
It does not produce effects.  

It observes and compares.  

Any attempt to merge reconciliation with execution introduces bias.  

The system must not evaluate and act in the same step.  

---

### 3. The Observed State

Reconciliation depends on observation:

Σ_observed  

This state is not controlled by the system.  
It is obtained from the boundary.  

It may be incomplete.  
It may be delayed.  
It may be wrong.  

Reconciliation operates under these constraints.  

---

### 4. The Expected State

The system holds an expected state:

τ_after  

This state is derived from the transition model.  

It represents what should exist if execution aligned with reality.  

It is internally consistent.  
It is not guaranteed to be true.  

---

### 5. The Comparison

Reconciliation compares:

τ_after and Σ_observed  

Three outcomes are possible:

match  
mismatch  
insufficient data  

The system does not infer beyond these outcomes.  

---

### 6. Match

If the states match:

τ_after = Σ_observed  

the system has confirmation.  

This does not prove correctness globally.  
It proves consistency at the point of observation.  

---

### 7. Mismatch

If the states do not match:

τ_after ≠ Σ_observed  

divergence exists.  

This is not a hypothesis.  
It is an observed contradiction.  

The system must not ignore it.  

---

### 8. Insufficient Data

If observation is incomplete:

the system cannot determine alignment.  

This is not failure.  
It is ignorance.  

The system must not convert absence of evidence into evidence of correctness.  

---

### 9. No Automatic Resolution

Reconciliation does not resolve divergence.  
It does not trigger recovery automatically.  

It produces a result.  

Action based on that result belongs to another layer.  

---

### 10. Separation of Concerns

The system now contains three distinct processes:

execution  
recovery  
reconciliation  

Each has a different role:

execution produces state  
recovery restores the ability to act  
reconciliation evaluates alignment  

These must remain separate.  

---

### 11. Iteration

Reconciliation is not a single step.  
It may be repeated:

observe → compare → act → observe  

Convergence is not guaranteed.  
The system may remain in partial alignment.  

---

### 12. Closing

Reconciliation does not make the system correct.  
It makes the system aware of whether it is aligned.  

The system does not assume truth.  
It evaluates it.

---

## Chapter 31 — Decision Under Constraint

Chapter 30 produces a verdict.

It does not act.

This chapter defines how that verdict constrains action.

Not what it enables.

What it removes.

---

### 31.1 — Decision Is Not Execution

Execution applies a transition.

Decision constrains whether execution is permitted.

A decision does not produce effects.

It restricts the set of actions that remain admissible.

---

### 31.2 — Verdict Does Not Imply Action

A reconciliation result is not an instruction.

It is a classification:

    ALIGNED
    DIVERGED
    INSUFFICIENT_DATA

No classification contains an action.

No mapping from verdict to action is defined.

Decision does not select.

It eliminates.

---

### 31.3 — Constraint, Not Control

Decision operates only by restricting the admissible action set.

It does not construct transitions, prioritize actions, or resolve state.

---

### 31.4 — The Constraint Function

Let V be the reconciliation verdict and A be the set of currently admissible actions.

Decision produces:

    A' ⊆ A

Decision does not construct new actions.

It only removes elements from A.

---

### 31.5 — DIVERGED

When V = DIVERGED:

    A' = ∅

No action is permitted.

The system is operating on a known contradiction.

---

### 31.6 — INSUFFICIENT_DATA

When V = INSUFFICIENT_DATA:

    A' = { a ∈ A | a can be validated using only known state }

An action is permitted only if its validity and admissibility can be evaluated without reference to unobserved data.

If no action satisfies this condition:

    A' = ∅

The system stops.

The system does not classify actions by meaning.

It admits only those that can be validated with available evidence.

---

### 31.7 — ALIGNED

When V = ALIGNED:

The additional constraint from mismatch is removed.

Decision does not expand the set of admissible actions.

Alignment does not justify action.

It only lifts the mismatch veto.

It does not introduce new permission.

---

### 31.8 — No Implicit Escalation

Decision cannot bypass geometry, admissibility, or epistemic constraints.

It operates strictly within existing limits.

---

### 31.9 — Separation

Decision does not execute actions, construct transitions, or modify system state.

It does not activate, clear, or modify epistemic state.

It produces a constrained action set.

Execution consumes that set.

---

### 31.10 — No Default Action

There is no default behavior.

The absence of restriction is not permission.

---

### 31.11 — Closing

Decision produces only A' ⊆ A.

The system does not decide what to do.

It determines what is no longer permitted.

Action remains possible only within:

    geometry ∩ admissibility ∩ epistemic state ∩ A'

If this intersection is empty,

the system stops.

---

## Chapter 32 — The Execution Loop

The system does not initiate execution.
It admits or refuses it.

Execution is not continuous.
It occurs in discrete admission cycles.

---

### 32.1 — Trigger Condition

A cycle exists only if:

```
(event, A)
```

are provided.

If no input exists, no cycle occurs.

---

### 32.2 — Input Set

The system receives:

```
A
```

A is external.

No assumption is made regarding correctness, completeness, or admissibility.

The system does not transform A.

Invalid elements are not repaired.
They are excluded.

---

### 32.3 — Observation

The system acquires:

```
Σ_observed
```

No guarantees are made about its quality.

The system does not modify or extend observed state.

---

### 32.4 — Reconciliation

The system evaluates:

```
τ_after vs Σ_observed
```

and produces:

```
V ∈ { ALIGNED, DIVERGED, INSUFFICIENT_DATA }
```

No action is taken at this stage.

---

### 32.5 — Restriction

The system computes:

```
A' ⊆ A
```

Such that all elements of A' satisfy admissibility constraints.

No new elements are introduced.

---

### Constraints

```
V = DIVERGED → A' = ∅
```

```
V = INSUFFICIENT_DATA → A' limited to locally provable elements
```

```
V = ALIGNED → A' ⊆ A
```

If:

```
A' = ∅
```

no execution occurs.

---

### 32.6 — Execution

Execution is defined over:

```
A'
```

Execution applies admissible elements and produces transition.

No validation or expansion occurs during execution.

---

### 32.7 — Transition

Execution yields:

```
τ_after
```

No assumption is made that:

```
τ_after = Σ_observed
```

---

### 32.8 — Iteration

Cycles are independent:

```
(event, A) → observe → reconcile → restrict → execute
```

No cycle assumes correctness of another.

---

### 32.9 — Control Boundary

The system does not control the origin of A.

It only enforces:

```
A → A'
```

---

### 32.10 — No Implicit Behavior

If no input exists:

```
no A → no execution
```

The system remains idle.

---

### 32.11 — Halting

If:

```
A' = ∅
```

no execution occurs.

---

### 32.12 — Closure

The system does not determine what should be done.

It determines whether any action is admissible.

If admissibility cannot be established, no execution occurs.

---

## Chapter 33 — Saturation & Adversarial Pressure

The system does not assume benign input.
It assumes persistence of invalid input.

Saturation is not a failure of correctness.
It is a condition of sustained pressure on admission.

---

### 33.1 — The Nature of Saturation

Saturation occurs when `A_untrusted` is unbounded in volume or frequency.

The system may receive redundant actions, invalid actions, adversarial sequences, or structurally valid but inadmissible actions.

Saturation does not imply breach. It tests whether rejection remains bounded in cost.

---

### 33.2 — No Obligation to Process

The system does not guarantee evaluation of all input.

```
A_untrusted → may be partially observed
```

There is no requirement that `∀ a ∈ A_untrusted → evaluated`.

Unprocessed input is not deferred. It is ignored.

---

### 33.3 — Bounded Admission Surface

The system defines a bounded intake:

```
|A_considered| ≤ N
```

where `A_considered ⊆ A_untrusted` and `N` is finite and context-independent.

Selection into `A_considered` is not prioritization, not interpretation, and not based on semantic value. It is structural limitation.

---

### 33.4 — Rejection Cost Invariant

For any input:

```
cost(reject(a)) = O(1)
```

Rejection must not depend on history length, trigger cascading evaluation, or allocate unbounded memory.

The system guarantees: unbounded input → bounded rejection cost.

---

### 33.5 — No Feedback Amplification

The system does not signal why an action failed, how it could succeed, or which constraints were violated.

Rejection is opaque: `invalid → excluded`.

This guarantee applies at the external boundary. Internally, the system produces structured errors (`AuthorityError`, `GeometryError`, `CapabilityError`) that are part of execution semantics. These distinctions are not exposed to the producer. There is no adaptive loop between system and producer.

---

### 33.6 — Admission Independence

Each cycle `(event, A_untrusted)` is evaluated independently.

The system does not accumulate invalid attempts, escalate based on repetition, or learn from adversarial input. There is no memory of failure patterns.

---

### 33.7 — No Exhaustion Path

The system must not reach a state where processing invalid input prevents evaluation of valid input.

This is enforced by bounded intake, constant-time rejection, and cycle isolation.

---

### 33.8 — Conditional Fairness

The system does not rank actions. The system does not guarantee that all valid actions in `A_untrusted` are observed.

Fairness applies only within the considered subset:

```
a ∈ A_considered ∧ admissible(a) → a ∈ A′
```

The system guarantees: no valid action is excluded once considered.

The system does not guarantee: `∀ valid a ∈ A_untrusted → a ∈ A_considered`.

An adversary filling the first `N` slots with structurally valid but inadmissible actions may prevent valid actions at position `> N` from being considered. This is the defined behavior under structural limitation, not a failure of the model. Mitigation belongs to the external layer (§33.12).

Fairness is structural — bounded intake and admissibility filtering — not heuristic.

---

### 33.9 — No Global Backpressure State

The system does not maintain global rate counters, per-producer penalties, or adaptive throttling state.

All constraints are local to the cycle.

---

### 33.10 — Interaction with Decision

Decision receives `A_considered`, not `A_untrusted`.

Saturation does not alter decision semantics. It constrains only input size.

---

### 33.11 — Interaction with Halting

If `A′ = ∅` under saturation, the system halts as defined in Chapter 32.

Saturation does not introduce new halting states.

---

### 33.12 — External Responsibility

Mitigation of sustained adversarial input belongs outside the system: rate limiting, identity tracking, abuse detection.

The system remains input-agnostic. It enforces admissibility, not behavior correction.

---

### 33.13 — Bounded Evaluation Window

Evaluation within a cycle is bounded. The system may terminate intake before reaching `|A_considered| = N` if a cycle time budget is configured.

In this case:

```
A_evaluated ⊆ A_considered
```

Evaluation order is not semantically defined. Partial evaluation is permitted.

The system guarantees bounded time per cycle, not complete evaluation of `A_considered`.

---

### 33.14 — Closure

The system does not resist saturation by learning or adaptation.

It resists by remaining bounded, stateless per cycle, and non-interactive in rejection.

If input cannot be reduced externally, the system does not degrade. It continues to admit only what can be validated and ignore the rest.

---

## Chapter 34 — Authority & Origin Control

The system does not assume that input is legitimate.
It requires that input is authorized to exist.

Authority does not grant correctness.
It grants only the right to be considered.

---

### 34.1 — Authority as Context

Authority is not part of the action.

It is provided as an explicit context:

```
authority_context
```

A cycle exists only if `(event, A_untrusted, authority_context)` are provided together.

Without authority, the cycle does not exist.

---

### 34.2 — Authority Gate

Before any processing, the system applies:

```
AuthorityGate.verify(input, authority_context)
```

Verification determines whether the input is allowed to enter the system.

If verification fails, the cycle does not proceed to any execution stage. No system transition occurs.

---

### 34.3 — Scope of Authority

Authority applies to the origin of input.

It does not apply to correctness of actions, admissibility of actions, or epistemic alignment.

An authorized input remains `A_untrusted`.

---

### 34.4 — No Implicit Authority

The system does not read authority from global state, environment variables, or implicit configuration.

Authority must be explicitly provided per cycle or per system instance.

---

### 34.5 — Separation from Validation

Authority verification does not validate structure.

```
authority ≠ validity
```

Invalid but authorized input proceeds to validation and may be rejected later. Unauthorized input is never observed by the system.

---

### 34.6 — Failure Semantics

Authority failure is defined as: input origin cannot be verified.

At the `AuthorityGate` boundary, both failure modes produce the same error type:

```
unknown signer       → AuthorityError   (identity failure)
invalid signature    → AuthorityError   (origin unverifiable)
```

`AuthorityError` represents refusal to construct a cycle. It does not correspond to a system transition and does not imply partial evaluation.

At higher layers, context disambiguates. When the signer is known but the signature is invalid, `TransactionManager` reinterprets the failure as:

```
invalid signature    → GeometryError    (integrity failure)
```

This reinterpretation is the responsibility of the layer that has the knowledge to make it. `AuthorityGate` does not have that knowledge — it only knows whether origin can be verified. The distinction between identity failure and integrity failure is resolved above the gate, not inside it.

---

### 34.7 — No Authority Escalation

The system does not allow input to modify `authority_context`.

Authority is immutable during execution. There is no mechanism by which `A_untrusted` increases its own authority.

---

### 34.8 — Trust Roots

Authority is defined relative to a set of trusted origins:

```
AuthorityContext(trusted_keys)
```

The system does not infer trust. Trust must be explicitly configured.

`AuthorityContext.from_env()` is a bootstrap helper only. It is not part of the runtime execution path.

---

### 34.9 — Key Rotation and Evolution

Changes in authority — key rotation, signer addition or removal — occur outside the execution cycle.

The system does not migrate authority mid-cycle and does not reinterpret past inputs under new authority. Each cycle uses a fixed `authority_context`.

---

### 34.10 — Authority Independence from Saturation

Authority does not affect intake limits.

```
authorized input ≠ prioritized input
```

All input, regardless of origin, is subject to `SaturationGate` constraints (§33.3). A trusted source does not receive a larger `N`.

---

### 34.11 — Authority Independence from Decision

Authority does not affect admissibility.

```
authorized action ≠ admissible action
```

Decision operates on `(V, A_considered)` independently of authority. An authorized action may still be rejected by the decision layer.

---

### 34.12 — Authority Independence from Execution

Execution does not verify authority. Authority is resolved before any execution path exists.

Execution assumes input has passed `AuthorityGate`. This assumption is enforced by pipeline order, not by runtime checks within the execution layer.

---

### 34.13 — No Persistence of Authority

The system does not accumulate authority over time.

Previous authorization does not imply future authorization. Each cycle is independent.

---

### 34.14 — Boundary of Responsibility

The system enforces authorization of input existence.

It does not enforce identity tracking, rate limiting, or behavioral trust. These belong to external systems (§33.12).

---

### 34.15 — Closure

The system does not trust input. It does not trust origin.

It only verifies whether input is allowed to be considered.

If authority cannot be established, nothing enters the system.

---

## Chapter 35 — Capability Domains

Authority answers: is this input allowed to exist?

A capability domain answers: what is this input allowed to do?

These are different questions. A valid key does not imply permission to invoke all capabilities. Authorization of origin is not authorization of action.

---

### 35.1 — The Problem Authority Does Not Solve

A system with a single `AuthorityContext` treats all authorized input as equivalent. Any signer may request any action.

This is sufficient when the system has one trusted source.

It is insufficient when multiple signers exist with different operational roles, or when a compromised key should not grant full capability access.

Authority as boolean — authorized or not — does not express these distinctions.

---

### 35.2 — Capability Domain as Space

A capability domain is not a role. It is not a permission list.

It is a declared subset of the action space:

```
D(signer_id) ⊆ A_registered
```

where `A_registered` is the full set of op_types in the `CapabilityRegistry`.

A signer operating within domain `D` may only request actions in `D`. Actions outside `D` are excluded regardless of structural validity.

The domain does not modify what actions do. It constrains which actions may be requested by which origin.

---

### 35.3 — Separation of Concerns

Three distinct questions, three distinct answers:

```
AuthorityGate    → is this origin allowed to speak?
CapabilityDomain → is this origin allowed to request this action?
Decision         → is this action admissible given current state?
```

These are evaluated in order. A failure at any stage halts progression.

An action may be authorized and out-of-domain — rejected at the domain layer. An action may be authorized and in-domain and inadmissible — rejected at the decision layer. Only authorized, in-domain, admissible actions proceed to execution.

---

### 35.4 — Domain is Declared, Not Inferred

The system does not infer what a signer should be allowed to do from context, history, or behavior.

Domains are declared at configuration time:

```
DomainConfig({
    "deploy-key":  {"set", "delete"},
    "monitor-key": {"http_call"},
    "audit-key":   {"set"},
})
```

If a signer has no declared domain, the system fails closed: `D(signer_id) = ∅`.

---

### 35.5 — Domain Does Not Grant Correctness

An action within domain is not guaranteed to be valid or admissible.

Domain membership means: this origin may request this type of action.

It does not mean the action is structurally valid, admissible given current state, or will succeed. Domain filtering precedes validation. Both are required.

---

### 35.6 — Domain is Geometry-Agnostic

Domains are defined against `A_registered`. Domain filtering does not consult geometry.

An action must satisfy both constraints independently:

```
a ∈ D(signer_id)      — domain constraint
a ∈ A_geometry        — geometry constraint
```

If an action is in-domain but not present in the current geometry, it passes domain filtering and is rejected at the geometry or validation layer. The domain layer does not carry this responsibility.

This preserves separation: domain constrains origin, geometry constrains structure. Neither layer knows the other.

---

### 35.7 — No Domain Escalation

A signer cannot expand its own domain.

There is no mechanism by which `a ∈ A_untrusted` expands `D(signer_id)`. Domain modification occurs only outside the execution cycle, through explicit reconfiguration.

`DomainConfig` is immutable after construction. This mirrors the constraint on authority escalation (§34.7).

---

### 35.8 — One Signer Per Cycle

A cycle has a single authority origin.

All actions in `A_untrusted` are attributed to the signer established by `AuthorityGate` for that cycle. The system does not support per-action origin attribution.

```
(event, A_untrusted, signer_id) → single domain applied to all actions
```

If multiple signers need to act, they operate in separate cycles. There is no mechanism to merge domains within a single cycle.

This preserves the model: `A_untrusted` is a list of operations, not a list of attributed tuples. The domain layer receives `(A_considered, signer_id)` — one set, one origin.

---

### 35.9 — Pipeline Position

Domain filtering occurs after saturation and before decision:

```
A_untrusted
    → SaturationGate → A_considered
    → DomainFilter   → A_domain
    → Decision       → A′
    → Execution
```

Saturation constrains volume. Domain constrains scope. Decision constrains admissibility. These are independent operations on the same pipeline.

Volume limits apply regardless of domain. A narrow domain under saturation pressure receives no special treatment (§33.10).

---

### 35.10 — Domain Failure Semantics

An action outside the declared domain is excluded without per-action feedback.

The system does not signal why the action was excluded, what the signer's domain contains, or how the action could be made admissible. This is consistent with §33.5: rejection is opaque at the boundary.

`DomainResult` exposes aggregate counts — `dropped_domain`, `dropped_total` — not per-action reasons.

---

### 35.11 — No Default Domain

The system has no default domain.

A signer without a declared domain has `D(signer_id) = ∅`. All actions from that signer are excluded. This is not an error — it is the defined behavior for an undeclared domain.

Fail closed, not open.

---

### 35.12 — Interaction with Authority

Domain resolution requires a known signer identity established by `AuthorityGate`.

If `AuthorityGate` fails, domain resolution does not occur. Domain is not a fallback for authority. The two layers are sequential, not parallel.

---

### 35.13 — Boundary of Responsibility

The domain layer enforces which origins may request which action types.

It does not enforce what values are valid within an action, what state transitions are permissible, or whether the action will have the intended effect. These belong to validation and admissibility.

---

### 35.14 — Monotonicity

Domains are restrictive only.

```
A_domain ⊆ A_considered
```

Domain filtering cannot introduce admissibility. It can only reduce the action set. A domain cannot create capabilities that do not exist in `A_considered`.

---

### 35.15 — Closure

A key is not a capability.

A key establishes that input may exist. A domain establishes what that input may request. Admissibility establishes whether the request is executable now.

The system does not conflate these. An authorized key with an empty domain produces no executable actions. The system halts cleanly, as defined in §32 and §33.11.

---

## Chapter 36 — Composition Attacks

The system evaluates actions individually.

Individually valid actions may produce collectively invalid state.

This is not a flaw in the model. It is a structural property that must be understood to use geometry correctly.

---

### 36.1 — The Composition Problem

Each action is evaluated against current state:

```
validate(state_before, a) → authorized or rejected
```

A sequence of actions passes if each step passes:

```
[a₁, a₂, ..., aₙ] → authorized iff ∀i: validate(stateᵢ, aᵢ) passes
```

This means the system evaluates composition *stepwise*, not globally.

A sequence that satisfies every per-step constraint may still produce a final state that violates an invariant expressible only across multiple steps.

---

### 36.2 — Independence of Evaluation

Actions are independent at evaluation time.

Admissibility of each action is determined without reference to other actions in the same cycle.

Execution is not independent. Actions modify the same state. An action admitted independently may interact with the effects of another action admitted independently.

```
evaluation: independent
execution:  shared state
```

Evaluation independence does not imply execution independence.

---

### 36.3 — What Stepwise Verification Catches

The proposal engine simulates actions sequentially. After each action, geometry verifies:

```
preconditions(stateᵢ, aᵢ)
postconditions(stateᵢ₊₁, aᵢ)
invariants(stateᵢ₊₁)
```

This catches:

- actions invalid in isolation
- actions that become invalid because a prior action changed state
- invariant violations produced by any individual step

If any step fails, the entire batch is rejected. The system rolls back to `state₀`. No partial state survives.

---

### 36.4 — What Stepwise Verification Does Not Catch

Stepwise verification does not catch invariants expressible only across the full sequence — conditions satisfied after each individual step but violated by the combined effect.

Example:

```
invariant: budget ≥ 0

a₁: subtract(budget, 60)   → budget = 40  ✔ invariant holds
a₂: subtract(budget, 50)   → budget = -10   invariant violated → rejected
```

This is caught. But:

```
a₁: set(reserve, 0)          → reserve = 0   ✔
a₂: set(withdraw_enabled, 1) → enabled = 1   ✔

combined effect: reserve = 0 ∧ withdraw_enabled = 1
```

If the invariant `reserve > 0 → withdraw_enabled = 0` is not declared in geometry, neither step fails. The system commits. The combined state may be dangerous.

The system does not detect this. The geometry does not contain the constraint. This is a geometry definition problem, not an execution problem.

---

### 36.5 — Atomicity Does Not Imply Semantic Safety

The system guarantees atomicity:

```
all actions commit or none apply
```

Atomicity prevents partial state. It does not prevent harmful combinations.

A fully committed batch may produce a state that is structurally valid — no declared invariant was violated — but dangerous from the perspective of the system's intent.

The execution model does not reason about intent. It enforces declared constraints.

---

### 36.6 — The Boundary of Geometry

Geometry is the mechanism for expressing composition constraints. Its expressive power determines what the system can enforce.

What geometry can express:

```
invariants on state after each action
preconditions on state before each action
postconditions on state after each action
```

What geometry cannot currently express:

```
constraints on action sequences (if a₁ executed, a₂ is disallowed in same batch)
constraints on the full diff (properties of the complete set of operations)
inter-action dependencies within a batch
```

These are not architectural limits of the model — they are limits of the current geometry DSL. A richer constraint language could express them.

---

### 36.7 — Composition Safety Is a Constraint Design Problem

The system cannot be made safe against composition attacks by modifying the execution layer.

The execution layer's responsibility is: apply committed transitions atomically, verify per-step constraints, roll back on failure.

Composition safety is the responsibility of geometry design: the invariants declared must be sufficient to make dangerous compositions unreachable.

If a dangerous composition is possible, the correct response is to add a geometry constraint that makes it impossible — not to add sequence analysis to the execution layer.

---

### 36.8 — No Sequence Analysis Layer

The system does not include a batch validator, sequence analyzer, or policy engine.

Adding such a layer would introduce interpretation: the system would need to reason about what sequences mean, which requires semantic knowledge the execution layer does not have and must not acquire.

The execution layer evaluates structure. Semantics belong to geometry constraints.

---

### 36.9 — Rollback Scope

When a batch fails at step k:

```
state₀ → a₁ → state₁ → ... → aₖ → FAIL → rollback → state₀
```

The rollback is complete. No effect from `a₁, ..., aₖ₋₁` survives.

If a dangerous combination is detected at any step, the entire batch is cancelled. Partial effects do not accumulate.

What this does not provide: if the dangerous combination is only visible after all steps complete — because no single step violated a declared constraint — the batch commits.

---

### 36.10 — All Constraints Are State-Local

The constraint system has a formal boundary.

No constraint may depend on:

```
action history       — what was executed before this action
action ordering      — whether a₁ preceded a₂
action co-occurrence — whether a₁ and a₂ appear in the same batch
```

All constraints are state-local:

```
constraint(state_before, action, state_after)
```

This is not a limitation to be worked around. It is the property that makes the system deterministic and verifiable.

A constraint that depends on history introduces memory. A constraint that depends on ordering introduces sequencing logic. A constraint that depends on co-occurrence introduces batch semantics. All three are forms of interpretation that the execution model explicitly excludes.

If a safety property cannot be expressed as a state-local constraint, it cannot be enforced by this system. It must be enforced above it.

---

### 36.11 — Composition Does Not Imply Safety

The system guarantees:

```
∀ a ∈ A′ → admissible(a)
```

It does not guarantee:

```
sequence(A′) is safe
```

A sequence of individually admissible actions may still:

- produce cross-action state interactions not captured by per-step invariants
- create multi-step effects invisible to stepwise evaluation
- combine legally to reach a state that is structurally valid but operationally dangerous

The system does not detect these properties. They are outside the model.

---

### 36.12 — Limits of the Model

The system cannot detect:

```
emergent behavior from valid sequences
multi-step exploits where each step is individually valid
strategic sequencing across cycles
```

These are deliberate design decisions.

Detecting them would require the system to maintain history, reason about intent, or evaluate global properties of sequences — all of which introduce state, interpretation, and coupling that the model explicitly excludes.

The model trades global sequence reasoning for local determinism.

---

### 36.13 — External Responsibility

Higher-level systems may enforce:

```
sequence constraints before submitting a batch
behavioral analysis of action patterns
workflow validation against declared policies
```

These are outside the execution model. The execution model does not prevent their implementation above it.

---

### 36.14 — Correct Use of the Model

A system using this execution model is responsible for:

1. Declaring all safety invariants in geometry that must hold after every action.
2. Ensuring that dangerous combinations are made unreachable through preconditions and invariants, not through trust in the caller.
3. Treating any combination not excluded by geometry as potentially executable.

The execution model enforces what is declared. It does not reason about what was not declared.

---

### 36.15 — Closure

The system guarantees that no individually invalid action commits.

It does not guarantee that all valid combinations are safe.

Safety is a property of the geometry, not of the execution layer. An execution system with correct geometry is safe. An execution system with incomplete geometry is not, regardless of how the execution layer is implemented.

The correct response to a composition attack is not a smarter executor. It is a more complete geometry.

---

## Chapter 37 — Temporal Constraints

The system evaluates each cycle independently.

It does not retain execution history.

It only observes current state.

This creates a class of properties that cannot be enforced locally: properties that depend on what happened before, how long ago, or in what order.

---

### 37.1 — The Temporal Gap

Chapter 36 established that all constraints are state-local:

```
constraint(state_before, action, state_after)
```

State-local constraints cannot express:

```
time since last execution
number of cycles since a key was set
whether an action occurred in a prior cycle
elapsed wall-clock time between two actions
```

These are temporal properties. They require memory the system does not have — by design, not by omission.

---

### 37.2 — What "Stateless Per Cycle" Means

Each cycle begins from:

```
(event, A_untrusted, authority_context)
```

The system does not carry forward:

```
execution history of prior cycles
timing of prior events
identity of prior signers
A_untrusted from previous cycles
```

`τ_after` from the previous cycle enters the next cycle only as `Σ_observed` — the observed state passed to reconciliation. It is not execution history. It is current state.

The system knows what the state is. It does not know how it got there.

---

### 37.3 — Replay

A replay attack submits an action or batch that was valid and executed in a prior cycle.

Replay is constrained within a cycle but unbounded across cycles.

Within a cycle, `TransactionManager` prevents replay of a proposal if the underlying state has changed between `propose()` and `commit()`. The TOCTOU check compares `proposal.transition.before` with the environment snapshot at commit time. If they differ, the transaction is rejected.

This protection is limited to a single cycle. Across cycles, the system provides no replay protection.

An identical input submitted in a later cycle is treated as a new request and evaluated independently. The system maintains no memory of prior executions, no proposal identifiers, and no deduplication mechanism.

This is not a gap. It is a direct consequence of determinism:

```
f(state, input) = output
same(state, input) → same(output)
```

Determinism implies replayability. The system does not track prior executions — it evaluates current state against current input.

If replay must be prevented, it must be enforced externally: nonces, sequence numbers, proposal identifiers — validated before input reaches the system.

---

### 37.4 — Staleness

Staleness occurs when:

```
Σ_observed reflects state from time t
execution occurs at time t + Δ
```

The gap Δ may be significant. The system does not know.

Reconciliation compares `τ_after` with `Σ_observed`. If they match, the system proceeds. It does not reason about whether `Σ_observed` is recent.

A stale observation that happens to match `τ_after` passes reconciliation. The system cannot distinguish between a fresh observation and a cached one.

If staleness is a risk, the observer must guarantee freshness. The execution model does not impose this guarantee.

---

### 37.5 — Ordering Within a Cycle

Within a single cycle, the proposal engine processes actions sequentially in the order of `A_untrusted` as received. The system does not reorder.

The domain layer and decision layer do not impose ordering. Order is a property of the input, not of the system.

This means ordering is implicitly trusted. If the order of actions is security-relevant, the system does not detect or prevent reordering by the caller. Ordering-sensitive semantics must be enforced explicitly — either by the caller before submission, or expressed as geometry constraints that make incorrect orders unreachable.

---

### 37.6 — Ordering Across Cycles

The system does not enforce ordering across cycles.

There is no mechanism to require:

```
cycle N must complete before cycle N+1 begins
action a must precede action b across separate cycles
```

Each cycle is independent. The system does not know it is cycle N.

If cross-cycle ordering is required, it must be enforced externally — through sequencing logic above the execution model.

---

### 37.7 — The Timing of Observation

Observation (`Σ_observed`) occurs at the start of each cycle.

Between observation and execution, state may drift externally:

```
observe(state_t) → ... → execute(state_t + drift)
```

The TOCTOU check in `TransactionManager` catches drift that occurs between `propose()` and `commit()` within the same cycle.

It does not catch drift that occurred before `observe()` — because the system does not know what state existed before the current observation.

---

### 37.8 — No Internal Clock

The system does not maintain a clock.

It does not timestamp actions, timestamp cycles, measure elapsed time between events, or enforce timeouts on cycle duration beyond `SaturationGate`'s optional intake budget.

Time is not a first-class concept in the execution model.

If time matters — for expiry, rate limiting, freshness — it must enter the system as state, declared in geometry and enforced as invariants.

---

### 37.9 — Time as State

The correct way to introduce temporal constraints is to represent time as state:

```
set(key="last_withdraw_time", value=<timestamp>)
```

With a precondition:

```
now - last_withdraw_time ≥ cooldown_period
```

This is expressible as a geometry constraint if `now` is provided as part of the action payload.

---

### 37.10 — Time Requires a Trusted Source

Time-based constraints are only as reliable as the source of time.

The execution model does not validate the truthfulness of timestamps. If `now` is provided by an untrusted source, temporal constraints are trivially bypassable:

```
cooldown = 60s
now = falsified value
→ constraint passes
```

Time as state introduces a dependency on external truth. The execution model does not provide this truth.

For temporal guarantees to hold, time must originate from a trusted authority — verified before entering the system, at the authority layer or above. This is not a limitation to be patched in the execution layer. It is a boundary of responsibility.

---

### 37.11 — Cross-Cycle Memory via State

The execution model has no cross-cycle memory. But state persists across cycles.

An action may write to state what a future cycle needs to know:

```
cycle N:   set(key="lock_acquired", value=true)
cycle N+1: precondition: lock_acquired = false → rejected
```

This is cross-cycle coordination via state — not via system memory. The system enforces the constraint. The caller is responsible for what the state means.

---

### 37.12 — State-Based Coordination Hazards

State used for cross-cycle coordination may become inconsistent if a cycle fails after partial logical completion.

```
set(lock = true)
→ failure before intended release
→ lock persists indefinitely
```

The system guarantees atomicity of state transitions within a cycle. It does not guarantee that state encodes a complete logical process.

```
state persists
intent does not
```

If a cycle writes coordination state and fails before completion, the state remains without guarantee that the intended operation finished. This is a liveness risk — not a consistency failure. The state is correct; the logical process is incomplete.

Recovery from such states must be handled explicitly above the execution model: timeouts encoded as state, external intervention, or idempotent compensation actions.

---

### 37.13 — What Cannot Be Enforced

The execution model cannot enforce:

```
exactly-once execution (without external idempotency mechanism)
maximum frequency of a specific action type
wall-clock deadlines on cycle completion
causal ordering across independent systems
elapsed time between two state changes
```

These require a clock, history, or coordination primitives the execution model does not have and does not provide.

---

### 37.14 — External Responsibility

Temporal enforcement belongs outside the execution model:

```
sequence numbers on events (anti-replay)
timestamp validation before submission
rate limiting on cycle submission
freshness guarantees from observers
cross-cycle ordering in orchestration layer
idempotency keys on non-idempotent actions
```

The execution model does not prevent these from being implemented above it.

---

### 37.15 — Replay and Idempotency

The system does not distinguish between first execution and repeated execution.

Not all actions are idempotent:

```
http_call("/withdraw")  → not idempotent
append(key, value)      → not idempotent
set(key, value)         → idempotent if value is deterministic
```

For non-idempotent actions, replay produces additional effects. The system does not prevent this.

Idempotency must be enforced in geometry — for example, through preconditions that make repeated execution unreachable — or above the system through request identifiers and deduplication.

---

### 37.16 — Closure

The system enforces state correctness, not temporal correctness.

Correct state does not imply correct history.

The system knows:

```
what the state is now
whether an action is admissible against current state
```

The system does not know:

```
when state was last changed
whether an action has been executed before
in what order events occurred
how much time has elapsed
```

This is not a set of gaps. It is the boundary of a model that trades temporal awareness for local determinism, statelessness per cycle, and freedom from clock dependencies.

Temporal properties that matter must be encoded as state and declared as geometry constraints. Properties that cannot be encoded this way must be enforced above the execution model.

---

## Chapter 38 — External Control Plane

The execution model defines what happens inside a cycle.

It does not define what controls when cycles occur, what enters them, or what is done with their results.

That is the responsibility of the control plane.

---

### 38.1 — The Boundary

Chapters 27–37 define the execution model: a closed, deterministic system that transforms authorized input into verified state transitions.

The execution model answers:

```
given this input, is this transition valid?
```

It does not answer:

```
who decides what input to submit?
when should a cycle occur?
what happens if a cycle fails?
how are results communicated?
how are failures recovered?
```

These questions belong to the control plane — the layer above the execution model.

---

### 38.2 — What the Control Plane Is

The control plane is not part of the execution model.

It is the external system responsible for:

```
submitting cycles          — deciding when and what to execute
observing results          — receiving CycleResult and acting on it
handling failures          — retry, escalation, compensation
enforcing temporal props   — sequencing, rate limiting, replay prevention
managing authority         — provisioning keys, rotating credentials
routing input              — deciding which actions reach which system
```

The execution model does not know the control plane exists.

---

### 38.3 — Temporal Properties Belong Here

Chapter 37 established that the execution model has no clock, no history, and no replay protection across cycles. These are not gaps. They are boundaries.

The control plane is where temporal enforcement lives:

```
sequence numbers on submissions    → anti-replay
timestamps validated externally    → trusted time
rate limiting on cycle frequency   → abuse prevention
freshness requirements on observers → staleness prevention
cross-cycle ordering               → causal sequencing
```

The execution model is agnostic to all of these. The control plane enforces them before input reaches the execution model.

---

### 38.4 — Idempotency and Event Identity Belong Here

Chapter 37 established that the execution model does not distinguish first execution from repeated execution.

The control plane is responsible for assigning identity to submissions. Without identity:

```
replay cannot be detected
idempotency cannot be enforced
ordering cannot be established
```

Identity may take the form of unique request IDs, sequence numbers, or nonces. The execution model operates on anonymous input. It does not generate or require submission identity.

For non-idempotent actions, the control plane is responsible for deduplicating submissions before they reach the execution model. The execution model commits what it receives. The control plane decides what to send.

---

### 38.5 — Authority Provisioning Belongs Here

Chapter 34 established that authority must be explicitly provided per cycle.

The control plane is responsible for:

```
provisioning AuthorityContext for each cycle
managing signing key lifecycle
rotating keys outside the execution cycle
revoking compromised keys before they are used
```

The execution model verifies authority. The control plane controls authority.

The execution model does not know where keys come from. It only knows whether the presented key is trusted.

---

### 38.6 — Failure Handling Belongs Here

The execution model produces `CycleResult` with a status:

```
EXECUTED
HALTED_DIVERGED
HALTED_EMPTY
HALTED_NO_INPUT
ROLLED_BACK
```

It does not decide what to do next.

The control plane receives these results and decides:

```
EXECUTED       → proceed, observe, submit next cycle
ROLLED_BACK    → retry, escalate, or compensate
HALTED_DIVERGED → investigate, clear veto if appropriate, resume
HALTED_EMPTY   → inspect, modify input, or pause
```

Retry is a new cycle, not a continuation. The execution model has no concept of resuming a failed cycle. Each submission is evaluated independently from the current state.

The execution model is not responsible for recovery. It is responsible for accurate reporting of what happened.

---

### 38.7 — Orchestration Belongs Here

The execution model executes one cycle at a time. It has no concept of workflow, process, or multi-step operation.

The control plane is responsible for:

```
sequencing cycles into workflows
managing dependencies between cycles
deciding when to initiate recovery cycles
composing multiple execution results into higher-level outcomes
```

The execution model is a primitive. The control plane composes primitives into processes.

---

### 38.8 — Observation Belongs Here

Each cycle requires an observer — a callable that acquires `Σ_observed`:

```
observer(env) → dict | None
```

The execution model calls the observer but does not control it.

The control plane is responsible for providing a reliable observer implementation, ensuring freshness of observed state, handling observation failures, and deciding what counts as sufficient observation.

The execution model treats `None` as `INSUFFICIENT_DATA`. The control plane decides whether that is acceptable.

---

### 38.9 — The Separation Is Enforced by Interface

The execution model exposes a minimal interface:

```
ExecutionLoop.cycle(event, a_untrusted, env) → CycleResult
SaturationGate.filter(a_untrusted)           → IntakeResult
DomainFilter.filter(a_considered, signer_id) → DomainResult
AuthorityGate.verify(geometry, signer_id)    → None | raises
```

The control plane interacts with the execution model only through these interfaces.

No control plane component may inject state directly into the execution environment, bypass `AuthorityGate`, `SaturationGate`, `DomainFilter`, or `Decision`, or modify execution results after the fact. All interaction must occur through defined interfaces.

---

### 38.10 — No Control Plane Logic in the Execution Model

The execution model must not contain:

```
retry logic
escalation policies
workflow state
scheduling decisions
logging policy
alerting
```

These would introduce control plane concerns into the execution layer — creating coupling between what the system does and how it is operated.

The execution model remains a deterministic function of its inputs. The control plane remains responsible for the conditions under which that function is called.

---

### 38.11 — Trust Boundary at the Interface

The execution model treats the control plane as the source of input, not as a trusted actor.

It verifies:

```
authority of input origin
structural validity of actions
admissibility under current state
```

It does not verify:

```
intent correctness
policy compliance
operational safety
```

A malicious or misconfigured control plane can produce valid inputs that lead to valid but undesired outcomes. This is not a failure of the execution model. It is the definition of the boundary.

The execution model guarantees that all executed transitions are valid under geometry and that no invalid state transitions occur. It does not guarantee that submitted input reflects correct intent or that the sequence of cycles is appropriate for higher-level goals.

Correct execution does not imply correct orchestration.

---

### 38.12 — The Control Plane Is Not Specified Here

This specification does not define a control plane.

A concrete system may define one. ContinuumPort is one such system that instantiates a control plane above this execution model. Its design is not part of this specification, and this specification does not depend on any particular control plane implementation.

---

### 38.13 — Closure

The execution model is complete with respect to:

```
validation of transitions
enforcement of constraints
atomic state change
```

It is not complete with respect to:

```
when to execute
what to execute
why to execute
```

These belong to the control plane.

The control plane decides intent. The execution model enforces possibility.

The execution model without a control plane is a function that is never called. The control plane without an execution model is intent without enforcement.

---

## Chapter 39 — System Properties

This chapter defines the formal properties of the execution model.

These properties are not aspirational. They are enforced by construction — by the architecture defined in Chapters 27–38 — and validated by the test suite.

Each property states:

- what the system guarantees
- why the guarantee holds
- what follows from it

Together, they define the boundary of the model.

---

### 39.1 — Determinism

Given identical initial state and identical input, the system produces identical output.

```
f(state₀, input) = output
same(state₀, input) → same(output)
```

This holds because:

- proposal is a pure function of inputs
- geometry evaluation is deterministic
- execution order is fixed
- no clock, randomness, or external reads are used

Consequence:

- cycles are reproducible
- behavior is auditable
- replay is predictable

Determinism implies replayability, not safety under replay (§37.3).

---

### 39.2 — Atomicity

A cycle commits all operations or none.

```
commit(ops) → success ∨ rollback → state₀
```

This holds because:

- a full snapshot is taken before execution
- failure triggers full restore
- no partial commit path exists

Consequence:

- no intermediate state is observable
- state transitions are discrete

---

### 39.3 — No Partial State Escape

If a cycle fails, no effects persist.

This is a direct consequence of atomicity, stated explicitly for adversarial reasoning.

Consequence:

- failed execution leaves no residue
- rollback is semantically clean

---

### 39.4 — TOCTOU Protection (Intra-Cycle)

A proposal is rejected if state changes between propose and commit.

```
state_before ≠ snapshot_at_commit → reject
```

This holds because:

- `TransactionManager` re-checks state before commit

Scope:

- protects within a cycle
- does not apply across cycles (§37.3)

Consequence:

- no drift can be injected between validation and execution

---

### 39.5 — Monotonic Filtering

Each processing layer can only remove actions.

```
A′ ⊆ A_domain ⊆ A_considered ⊆ A_untrusted
```

This holds because:

- no layer appends actions
- all filters are reductive

Consequence:

- execution cannot exceed input
- input defines the upper bound of effects

---

### 39.6 — Decision Idempotency

Applying decision multiple times yields the same result.

```
decide(V, decide(V, A)) = decide(V, A)
```

This holds because:

- decision only removes invalid actions
- no state is accumulated

Consequence:

- decision is stable
- no cascading filtering effects

---

### 39.7 — Divergence Collapse

If reconciliation yields `DIVERGED`, no action is admissible.

```
V = DIVERGED → A′ = ∅
```

This holds because:

- decision short-circuits without evaluating actions

Consequence:

- execution halts under uncertainty
- safety is prioritized over progress

---

### 39.8 — No Authority Escalation

Execution cannot modify authority or domain.

This holds because:

- authority and domain are immutable inputs
- no execution path writes to them

Consequence:

- no privilege escalation via actions
- permissions are externally controlled

---

### 39.9 — Controlled State Mutation

All state changes occur through `TransactionManager`.

This holds because:

- environment mutation requires gate access
- the gate is opened only during execution
- execution is reachable only via validated proposals

Consequence:

- all state transitions are mediated
- no out-of-band mutation exists within the model

---

### 39.10 — Bounded Intake

The number of actions evaluated per cycle is bounded.

```
|A_considered| ≤ N
```

This holds because:

- `SaturationGate` enforces limits before evaluation

Consequence:

- evaluation cost is bounded
- adversarial volume cannot propagate

---

### 39.11 — State-Local Constraints

All constraints depend only on current state and a single action.

```
constraint(state_before, action, state_after)
```

Constraints cannot depend on:

- history
- ordering
- co-occurrence

This holds because:

- the geometry DSL has no temporal or sequence primitives

Consequence:

- evaluation is local and deterministic
- temporal properties are not expressible (§37)

---

### 39.12 — Error Layer Separation

Each error type belongs to a single layer.

```
AuthorityError     → authority layer
GeometryError      → geometry / transaction layer
EpistemicVetoError → epistemic layer
CapabilityError    → capability layer
ExecutionError     → execution layer
```

Exception:

- invalid signatures may be interpreted as geometry failure

Consequence:

- error type identifies failure origin
- debugging is layer-local

---

### 39.13 — Explicit Non-Guarantees

The model does not guarantee:

```
temporal correctness
cross-cycle replay protection
idempotency of non-idempotent actions
cross-cycle ordering
composition safety across actions
intent correctness
control plane correctness
```

These are not omissions.

They are outside the model boundary and belong to the control plane (§38).

---

### 39.14 — Closure

The execution model is defined by these properties.

A correct implementation must satisfy all properties above.

These properties are not independent:

- atomicity implies no partial state
- monotonic filtering bounds execution
- state-local constraints imply stateless evaluation

The architecture ensures these properties reinforce each other.

The test suite verifies them empirically.

Formal proofs exist for structural properties (atomicity, monotonicity, idempotency, divergence collapse).

The remaining properties follow directly from architectural constraints.

---

## Chapter 40 — State Continuity Across Sessions

### 40.0 — Status of This Chapter

Chapters 27–39 define the execution model.

This chapter defines a protocol for transferring validated state across sessions.

This protocol is not part of the execution model.
It is not enforced by the execution engine.

It is assumed to be implemented by the control plane (§38).

All guarantees in this chapter hold only if the protocol is respected.

---

### 40.1 — Continuity Is Not Defined by the Execution Model

The execution model is stateless per cycle (§37).

No execution history is retained across cycles.

State persists only as Σ_observed.

The system does not distinguish between:

* state produced by prior valid execution
* state introduced externally

Continuity across sessions is not defined within the execution model.

---

### 40.2 — Continuity as State Transfer

Continuity is defined as the transfer of validated state across sessions.

Let C be a capsule.

C.S represents validated state.

A subsequent cycle may initialize its environment using C.S.

No other information is transferred.

---

### 40.3 — The State Capsule

A capsule is defined as:

```
C = (I, K, S, A_next)
```

Where:

* I — intent
* K — constraint set
* S — validated state snapshot
* A_next — next action

The capsule contains only state required for execution.

The capsule does not contain:

* execution history
* unvalidated input
* inferred context

---

### 40.4 — Capsule Validity

A capsule is valid iff:

```
valid(C) ⇔
    S was produced by a committed execution
    ∧ K corresponds to the active constraint set
    ∧ A_next ∈ admissible(geometry, S)
```

A capsule that fails any condition is invalid.

Invalid capsules are treated as untrusted input.

---

### 40.5 — Reconstruction

A new cycle may be initialized as:

```
env := C.S
```

This operation is reconstruction.

No execution state is resumed.
No history is restored.

---

### 40.6 — Capsule as Untrusted Input

A capsule is not trusted by default.

C.S enters the system as Σ_observed.

It is subject to reconciliation and validation.

No capsule bypasses validation.

---

### 40.7 — Execution After Reconstruction

If valid(C):

```
restore(env, C.S)
execute(A_next) if admissible(A_next, S)
```

Execution is conditional on admissibility.

---

### 40.8 — No Implicit Continuity

The system does not retain:

* execution identity
* cycle linkage
* historical ordering

Each cycle is independent.

Continuity exists only through explicit state transfer.

---

### 40.9 — Conditional Continuity

Continuity holds only if:

* the capsule protocol is implemented by the control plane
* validation is enforced before use

If these conditions are not met, no continuity guarantees apply.

---

### 40.10 — Limits of This Protocol

This protocol does not guarantee:

* capsule integrity under adversarial control plane
* replay protection across sessions
* compatibility across geometry versions
* semantic consistency of intent

These are outside the execution model.

---

### 40.11 — Relationship to the Model

```
Execution Model   — enforces valid transitions
Control Plane     — governs execution
Continuity Layer  — transfers validated state
```

The execution model does not depend on continuity.
Continuity depends on valid execution.

---

### 40.11.a — Implementation Mapping

The continuity protocol is realized through concrete components:

* `execution/capsule.py`
* `execution/control_plane.py`

These define the behavior of validation, reconstruction, and resumption.

---

### Capsule Construction and Validation

Defined in:

`StateCapsule` (`execution/capsule.py`)

Responsibilities:

* structural definition of `C = (I, K, S, A_next)`
* integrity verification (state hash)
* defensive parsing via `from_dict()` (untrusted input)
* validation via `CapsuleValidator`

Mapping:

* §40.3 → `StateCapsule`
* §40.4 → `CapsuleValidator.validate()`
* §40.6 → `from_dict()` + validation

---

### Reconstruction

Defined in:

`reconstruct()` (`execution/capsule.py`)

Behavior:

* validates capsule before applying state
* initializes environment from `C.S`
* does not restore execution history

Mapping:

* §40.5 → reconstruction
* §40.8 → no history restoration

---

### Authority Binding

Defined in:

* `StateCapsule.authority_id`
* `reconstruct(..., authority_context=...)`

Behavior:

* verifies authority match before applying state
* rejects mismatches (fail-closed)

Mapping:

* §40.9 → enforced continuity condition
* §40.10 → partial replay mitigation

---

### Control Plane Enforcement

Defined in:

`resume_from_capsule()` (`execution/control_plane.py`)

This is the **only supported entry point** for cross-session resumption.

Responsibilities:

* enforces authority binding
* supports strict mode (reject unbound capsules)
* guarantees fail-closed behavior before reconstruction

Mapping:

* §40.2 → controlled state transfer
* §40.6 → no direct capsule application
* §40.9 → enforced at entry point

---

### Fail-Closed Behavior

Implemented across:

* `CapsuleValidator`
* `reconstruct()`
* `resume_from_capsule()`

Behavior:

* any validation failure aborts before mutation
* environment remains unchanged on failure

Mapping:

* §40.7 → conditional execution
* §40.9 → structural enforcement

---

### 40.12 — Closure

The execution model does not provide continuity across sessions.

Continuity requires explicit transfer of validated state.

A capsule does not represent memory.

It represents state produced by valid execution and reintroduced under validation.

No other form of continuity is defined.

> “Continuity is not a property of the system. It is a property of correctly enforced reconstruction.”

---

## Chapter 41 — Goal

A Goal is a pure function on state.

It evaluates whether a given state snapshot satisfies a declared condition.
It does not generate actions. It does not execute anything.
It does not access the environment directly.
It does not override geometry or authority.

---

### 41.1 — Formal Definition

A Goal G is a function:

```
G : State → {True, False}
```

with the following properties:

1. **Deterministic** — same state produces the same result, always
2. **Pure** — evaluation does not mutate state
3. **State-local** — no external dependencies at evaluation time
4. **Non-authoritative** — cannot override geometry, authority, or constraints
5. **Composable** — goals can be combined via AND / OR

The output is advisory only.

A Goal cannot force execution.
A Goal cannot block execution.
ContinuumPort remains the sole enforcement layer.

---

### 41.2 — Separation from the Execution Layer

A Goal does not know the execution layer exists.

```
goal.py       — Goal definition and evaluation
geometry.py   — admissibility of transitions
capsule.py    — state transfer across sessions
control_plane — orchestration and policy
```

There are no imports between `goal.py` and any of these modules.

This separation is structural and tested.

---

### 41.3 — Goal Evaluation

The `GoalEvaluator` enforces properties at evaluation time:

```
GoalEvaluator.evaluate(goal, state) → bool
```

Evaluation procedure:

```
1. Verify goal is a Goal instance
2. Verify state is a dict
3. Create defensive copy of state (deepcopy)
4. Record canonical representation of original state
5. Call goal.evaluate(state_copy)
6. Verify state_copy was not mutated
7. Verify original state was not mutated
8. Verify return type is bool
9. Return result
```

If any step fails, `GoalError` is raised.

The evaluator does not interpret the result.
It does not act on True or False.
It returns the boolean and stops.

---

### 41.4 — Determinism

Determinism is a **contract requirement**, not a property enforced at runtime.

The `GoalEvaluator` does not attempt to detect non-determinism.

Goals that depend on time, randomness, or external state may produce
inconsistent results and are considered invalid by design, but are not
prevented at evaluation time.

This is a model limit, consistent with the execution model:
only properties that can be structurally enforced are enforced.

`NON_DETERMINISTIC_GOAL` exists as a failure reason — it is a contract violation,
not an actively detected condition.

---

### 41.5 — State Isolation

The evaluator provides a defensive copy of state to the goal.

The goal never receives a reference to the original state.

After evaluation, the evaluator verifies:

```
canonical(state_copy_after) == canonical(state_copy_before)
canonical(original_state_after) == canonical(original_state_before)
```

If either check fails, `GoalError(SIDE_EFFECT_DURING_EVALUATION)` is raised.

This treats the goal as potentially adversarial input — exactly as the
execution model treats `A_untrusted`.

---

### 41.6 — Composition

Goals compose via the `&` and `|` operators:

```python
g = BalancePositive() & StepsWithinBound()   # ConjunctiveGoal
g = BalancePositive() | StepsWithinBound()   # DisjunctiveGoal
```

Composition rules:

- Both operands must be `Goal` instances
- `&` short-circuits: if left is False, right is not evaluated
- `|` short-circuits: if left is True, right is not evaluated
- Each operand is evaluated through `GoalEvaluator` — enforcement applies per-goal
- Composed goals are themselves `Goal` instances and can be further composed

Composition does not introduce authority.
A composed goal is still advisory only.

---

### 41.7 — Failure Modes

```
GoalError(NON_DETERMINISTIC_GOAL)        — contract violation, not detected at runtime
GoalError(STATE_EXTERNAL_DEPENDENCY)     — evaluation raised an unexpected exception
GoalError(SIDE_EFFECT_DURING_EVALUATION) — goal mutated its input state
GoalError(INVALID_COMPOSITION)           — operand is not a Goal instance
GoalError(INVALID_GOAL_DEFINITION)       — non-callable, non-bool return, or invalid input
```

`GoalError` is distinct from all execution layer errors:

```
GoalError ≠ GeometryError
GoalError ≠ AuthorityError
GoalError ≠ ExecutionError
GoalError ≠ CapsuleError
GoalError ≠ ControlPlaneError
```

Each error stays in its layer.

---

### 41.8 — Non-Authority

A satisfied goal has no effect on its own.
An unsatisfied goal has no effect on its own.

```python
result = evaluator.evaluate(goal, state)
# state is unchanged
# nothing was executed
# nothing was blocked
```

This is not a limitation. It is the design.

The goal layer provides direction.
The execution layer provides enforcement.
These are not the same thing, and must not be conflated.

---

### 41.9 — Relationship to Adjacent Chapters

Chapters 27–40 establish what is **permitted.**
Chapters 41–45 establish what is **desired.**

These are orthogonal:

```
permitted ∧ desired   → candidate for execution
permitted ∧ ¬desired  → legally executable, wrong direction
¬permitted ∧ desired  → blocked regardless of goal
¬permitted ∧ ¬desired → blocked
```

The execution model enforces permission.
The goal layer evaluates desire.

Neither overrides the other.

---

### 41.10 — Limits of the Goal Layer

The goal layer cannot:

- generate actions
- filter actions
- execute transitions
- access the environment
- override geometry
- bypass authority
- guarantee determinism of evaluation
- detect all forms of external dependency

These are deliberate design decisions.

Adding any of these capabilities to the goal layer would couple evaluation
to enforcement — destroying the separation that makes both layers reliable.

---

### 41.11 — Correct Use of the Goal Layer

A system using the goal layer is responsible for:

1. Defining goals as pure functions of state — no external dependencies.
2. Using `GoalEvaluator` to evaluate goals, not calling `evaluate()` directly.
3. Treating the boolean result as advisory — never as execution authorization.
4. Passing goal results to higher-level systems that remain outside the execution layer.

The goal layer evaluates what is declared.
It does not reason about what was not declared.

---

### 41.12 — Closure

A Goal answers one question:

> Does this state satisfy a declared condition?

It does not ask what to do about the answer.
It does not ask who authorized the question.
It does not ask what happens next.

Those questions belong to subsequent layers.

The goal layer is bounded, pure, and non-authoritative by design.

---

## Chapter 42 — Candidate Actions

A CandidateSet is a structural normalization boundary for untrusted action input.

It accepts externally provided action dicts, validates minimal structure, normalizes input, and silently filters structurally invalid entries.

This layer does not generate actions.
This layer does not execute actions.
This layer does not validate admissibility against geometry.

---

### 42.1 — Formal Definition

A CandidateSet C is a finite set of actions:

```
C = {a₁, a₂, ..., aₙ}
```

where each aᵢ is a dict with at least:

```
"type": str  — non-empty string
```

The source of candidates is external and opaque.
The layer does not know or care where candidates come from.

Input is treated as adversarial.
Every candidate is rejected unless it passes structural checks.

---

### 42.2 — Separation from the Execution Layer

A CandidateSet does not know the execution layer exists.

```
candidate.py  — CandidateSet definition and validation
goal.py       — Goal evaluation
geometry.py   — admissibility of transitions
control_plane — orchestration and policy
```

There are no imports between `candidate.py` and any of these modules.

This separation is structural and tested.

---

### 42.3 — Structural Validation

Validation is minimal and structural only.

A candidate is accepted if and only if:

```
isinstance(candidate, dict)
∧ "type" in candidate
∧ isinstance(candidate["type"], str)
∧ candidate["type"].strip() != ""
```

A candidate is silently filtered if any condition fails.

Semantic validation — whether the action is known, registered, or admissible — is not performed here.
That belongs to geometry (admissibility) and the execution layer.

---

### 42.4 — Silent Filtering

Invalid candidates are dropped without raising an error.

This is intentional.

The caller is not assumed to know which candidates are structurally valid before submitting them.
The layer accepts a raw, untrusted collection and returns what survived.

```
input:  [valid, invalid, valid, "string", {"key": "no_type"}]
output: CandidateSet(size=2)
```

Only `CandidateError` is raised when the container itself is invalid — that is, when a non-iterable is passed as input.

---

### 42.5 — Monotonicity

Let C_in be the input set of candidates.
Let C_out be the CandidateSet output.

Then:

```
C_out ⊆ C_in
```

The candidate layer is strictly reductive.
It never expands the input set.

This property is consistent with the monotonic filtering established in Chapter 39.5.
Every layer in the pipeline can only remove — never add.

---

### 42.6 — Input Isolation

The original input is never mutated.

Each accepted candidate is stored as a defensive copy.

`to_list()` returns independent copies — mutations to the returned list do not affect the CandidateSet.

---

### 42.7 — Orthogonality with Goal

CandidateSet and Goal operate on different dimensions:

```
CandidateSet:
    filters based on structure
    input:  raw action dicts
    output: structurally valid subset

Goal:
    evaluates based on state semantics
    input:  state snapshot
    output: bool
```

They are orthogonal and do not overlap in responsibility.

The CandidateSet does not depend on Goal.
The Goal does not depend on CandidateSet.

However, they participate in the same pipeline.
The output of CandidateSet may be consumed by subsequent layers where Goal evaluation occurs.

Structural independence does not mean pipeline independence.

---

### 42.8 — Relationship to Adjacent Layers

```
Goal (Ch. 41)           — evaluates whether a state satisfies a condition
CandidateSet (Ch. 42)   — holds the set of possible actions to consider
Simulation (Ch. 43)     — evaluates candidates against goal and state
ContinuumPort           — enforces admissibility and executes
```

The pipeline is:

```
UNTRUSTED INPUT → STRUCTURAL NORMALIZATION → SEMANTIC EVALUATION → EXECUTION
                        ↑
                  CandidateSet
```

The CandidateSet does not depend on Goal.
The CandidateSet does not depend on ContinuumPort.

It holds candidates. Nothing more.

---

### 42.9 — Failure Modes

```
CandidateError(INVALID_CANDIDATE_SET)  — non-iterable passed as input
```

`CandidateError` is distinct from all other layer errors:

```
CandidateError ≠ GoalError
CandidateError ≠ GeometryError
CandidateError ≠ AuthorityError
CandidateError ≠ ExecutionError
```

Each error stays in its layer.

---

### 42.10 — Limits of the Candidate Layer

The candidate layer cannot:

- generate actions
- validate semantic correctness
- check geometry admissibility
- evaluate goals
- execute transitions
- access the environment
- bypass authority

These are deliberate design decisions.

The candidate layer is the boundary between external input and internal evaluation.
It enforces only what can be enforced structurally.

---

### 42.11 — Correct Use of the Candidate Layer

A system using the candidate layer is responsible for:

1. Providing candidates from an external source — a model, a planner, a human, or a control plane.
2. Treating the CandidateSet as a structured container, not as a guarantee of admissibility.
3. Passing the CandidateSet to subsequent layers for further evaluation.
4. Not assuming that a candidate in the set will execute successfully.

The candidate layer normalizes what is provided.
It does not validate what is intended.

---

### 42.12 — Closure

A CandidateSet answers one question:

> Which of these inputs are structurally valid candidates?

It does not ask whether they are admissible.
It does not ask whether they satisfy a goal.
It does not ask what happens next.

Those questions belong to subsequent layers.

The candidate layer is bounded, passive, and non-authoritative by design.

---

## Chapter 43 — Simulation

Simulation is a pure evaluation layer over hypothetical state transitions.

It evaluates candidate actions against a goal by applying a provided transition function on a state snapshot.

It does not execute actions.
It does not modify real state.
It does not access the environment.
It does not enforce admissibility.

---

### 43.1 — Formal Definition

Let:

```
S     = current state
C     = CandidateSet = {a₁, a₂, ..., aₙ}
G     = Goal
apply : (state, action) → state_after
```

Then Simulation computes:

```
R = { a ∈ C | G(apply(S, a)) = True }
```

Simulation evaluates each candidate independently.

No ordering is assumed.
No interaction between candidates is modeled.

---

### 43.2 — External Transition Function

Simulation does not define how actions transform state.

It requires an external function:

```
apply(state, action) → state_after
```

Properties required (by contract):

- pure — must not mutate input state
- deterministic — same input produces same output
- state-local — no external dependencies

Simulation treats `apply` as opaque.

It does not interpret actions.
It does not validate semantics.
It does not enforce correctness of transitions.

---

### 43.3 — Evaluation Process

For each candidate `a ∈ C`:

1. Create an isolated copy of state `S'`
2. Compute hypothetical state:

```
S_after = apply(S', a)
```

3. Evaluate goal:

```
result = G(S_after)
```

4. Include candidate in output if:

```
result == True
```

Each evaluation is independent.

State is re-initialized for every candidate.

---

### 43.4 — Purity and Isolation

Simulation is a pure function:

```
simulate(C, G, S, apply) → subset of C
```

It guarantees:

- original state `S` is never modified
- candidates are not modified
- no side effects occur
- no external systems are accessed

Any violation of these guarantees is a contract violation of `apply` or `Goal`.

---

### 43.5 — Non-Authority

Simulation has no authority.

A candidate that satisfies Goal:

- is not executed
- is not approved
- is not guaranteed admissible

A candidate that fails Goal:

- is not blocked
- is not rejected by the system

Simulation produces advisory output only.

---

### 43.6 — Independence from Execution Layer

Simulation does not know the execution layer exists.

```
simulation.py  — Simulation logic
candidate.py   — CandidateSet
goal.py        — Goal
geometry.py    — admissibility (not used here)
```

There are no imports from:

- `execution.geometry`
- `execution.transaction`
- `execution.environment`
- `execution.authority`

This separation is structural and tested.

---

### 43.7 — Monotonicity

Let:

```
C_in  = input CandidateSet
C_out = result of Simulation
```

Then:

```
C_out ⊆ C_in
```

Simulation is strictly reductive.

It never creates new candidates.
It only selects from existing ones.

---

### 43.8 — Failure Modes

```
SimulationLayerError(INVALID_CANDIDATES)    — input is not CandidateSet
SimulationLayerError(INVALID_GOAL)          — goal is not Goal instance
SimulationLayerError(INVALID_STATE)         — state is not dict
SimulationLayerError(INVALID_APPLY)         — apply is not callable
SimulationLayerError(APPLY_VIOLATION)       — apply raises or mutates state
SimulationLayerError(APPLY_INVALID_RETURN)  — apply returned non-dict
SimulationLayerError(GOAL_VIOLATION)        — goal raises during evaluation
```

`SimulationLayerError` is distinct from all other layer errors:

```
SimulationLayerError ≠ GoalError
SimulationLayerError ≠ GeometryError
SimulationLayerError ≠ AuthorityError
SimulationLayerError ≠ ExecutionError
```

Errors remain within the simulation layer.

---

### 43.9 — Limits of Simulation

Simulation cannot:

- guarantee correctness of predicted outcomes
- enforce admissibility
- detect invalid action semantics
- access real environment state
- execute transitions
- prevent divergence between simulated and real execution

Simulation models hypothetical outcomes only.

---

### 43.10 — Assumption Boundary

Simulation assumes:

- `apply` correctly models state transitions
- `apply` is pure and deterministic
- `Goal` correctly evaluates state

Violation of these assumptions is outside the responsibility of Simulation.

Simulation does not validate the model.
It uses the model.

---

### 43.11 — Relationship to Adjacent Layers

```
CandidateSet (Ch. 42) — structural normalization
Simulation (Ch. 43)   — hypothetical evaluation
ContinuumPort         — admissibility + execution
```

Pipeline:

```
UNTRUSTED INPUT
    ↓
CandidateSet
    ↓
Simulation
    ↓
ContinuumPort
```

Simulation sits between structure and execution.

---

### 43.12 — Closure

Simulation answers one question:

> If this action were applied, would the resulting state satisfy the goal?

It does not ask:

- whether the action is allowed
- whether the transition is valid
- whether execution will succeed

Simulation is predictive, not authoritative.

---

## Chapter 44 — Selection

Selection is the layer that chooses one candidate from a set of simulated admissible candidates.

It is the first layer in the pipeline that must choose, not just filter.

It does not generate actions. It does not execute actions. It does not evaluate goals. It does not enforce admissibility.

It delegates the choice to an externally provided policy function.

---

### 44.1 — Formal Definition

Let:

```
C     = finite collection of candidates (output of Simulation)
P     = SelectionPolicy
P : C → aᵢ | None
```

Selection is:

```
select(C, P) = P(C)
```

If P returns None, no candidate is selected.

If C is empty, selection halts without calling P.

The output is advisory only.

Selection cannot force execution. Selection cannot block execution. ContinuumPort remains the sole enforcement layer.

---

### 44.2 — Separation from the Execution Layer

Selection does not know the execution layer exists.

```
selection.py  — Selection logic
simulation.py — hypothetical evaluation
candidate.py  — CandidateSet
goal.py       — Goal evaluation
geometry.py   — admissibility (not used here)
```

There are no imports between `selection.py` and any of these modules.

This separation is structural and tested.

---

### 44.3 — Policy Injection

Selection has no default strategy.

A caller that does not provide a policy cannot proceed.

This is not an omission. It is a design decision.

A default selection strategy is a hidden decision. Hidden decisions break auditability. The caller must declare how selection is performed.

The policy is a callable:

```
policy(candidates: list[dict]) → dict | None
```

Policy contract (by contract, not enforced at runtime):

1. **Deterministic** — same input produces same output
2. **Non-executing** — policy must not execute actions
3. **Non-mutating** — policy must not modify the candidate list
4. **Returns one** — policy returns one candidate from C, or None

Selection does not validate policy correctness beyond structural checks. If the policy violates its contract, Selection provides no guarantees about the result. This is a documented model limit, not a defect to be patched at this layer.

---

### 44.4 — Selection Process

```
select(candidates, policy) → SelectionResult
```

Evaluation procedure:

1. Verify candidates is a list of dicts
2. Verify policy is callable
3. If candidates is empty, return `SelectionResult(selected=None, skipped=[])`
4. Provide defensive copy of candidates to policy
5. Call `policy(candidates_copy)`
6. Verify return is dict or None
7. Verify returned candidate is structurally identical to one element of C_in (by equality, not just by action type)

Equality is defined as full key-value equivalence of the candidate dict. Subset equality and hash-based approximations are not sufficient.
8. Return `SelectionResult(selected=chosen, skipped=remainder)`

If any step fails, `SelectionError` is raised.

The evaluator does not interpret the result. It does not act on the selection. It returns the result and stops.

---

### 44.5 — Input Isolation

The policy receives a defensive copy of the candidate list.

The policy never receives a reference to the original candidates.

Mutations to the copy do not affect the original input.

This treats the policy as potentially adversarial input — exactly as the execution model treats `A_untrusted`.

---

### 44.6 — Monotonicity

Let `C_in` be the input candidates. Let `C_out` be the SelectionResult output.

Then:

```
selected ∈ C_in  ∨  selected = None
|{selected}| + |skipped| = |C_in|
```

Selection is strictly non-expansive. It never introduces new candidates. It only selects from existing ones.

This property is consistent with the monotonic filtering established in §39.5. Every layer in the pipeline can only remove — never add.

A policy that attempts to return a candidate not structurally identical to one element of the input is rejected with `POLICY_FOREIGN_RETURN`. Matching by action type alone is insufficient — two candidates with the same `type` but different fields are distinct candidates.

---

### 44.7 — Empty Candidates

If the candidate list is empty, selection halts immediately.

The policy is not called.

The result is `SelectionResult(selected=None, skipped=[])`.

This is not a failure. It is a defined outcome.

An empty candidate set means simulation produced no candidates that satisfied the goal. There is nothing to select from. The system reports this accurately and stops.

---

### 44.8 — Non-Authority

A selected candidate has no effect on its own. An unselected candidate has no effect on its own.

```python
result = selection.run(candidates, policy)
# candidates are unchanged
# nothing was executed
# nothing was blocked
```

This is not a limitation. It is the design.

The selection layer provides a decision. The execution layer provides enforcement. These are not the same thing, and must not be conflated.

`SelectionResult` carries no authority to execute. It carries data — a plain dict — that subsequent layers may act upon.

---

### 44.9 — Built-in Policies

Two minimal policies are provided:

**`policy_first`**

Selects the first candidate in the list. Deterministic. Depends on ordering of input. Ordering is the caller's responsibility.

**`policy_none`**

Always returns None. No candidate is selected. Useful for testing or when selection should explicitly produce no result.

These are not defaults. They are explicit choices the caller must pass. No policy is assumed.

---

### 44.10 — Failure Modes

```
SelectionError(INVALID_CANDIDATES)    — candidates is not a list of dicts
SelectionError(INVALID_POLICY)        — policy is not callable
SelectionError(POLICY_VIOLATION)      — policy raised an exception
SelectionError(POLICY_INVALID_RETURN) — policy returned non-dict, non-None
SelectionError(POLICY_FOREIGN_RETURN) — policy returned candidate not in input
```

`SelectionError` is distinct from all other layer errors:

```
SelectionError ≠ GoalError
SelectionError ≠ SimulationLayerError
SelectionError ≠ CandidateError
SelectionError ≠ GeometryError
SelectionError ≠ AuthorityError
SelectionError ≠ ExecutionError
```

Each error stays in its layer.

---

### 44.11 — Relationship to Adjacent Layers

```
Simulation (Ch. 43)   — hypothetical evaluation → accepted candidates
Selection  (Ch. 44)   — chooses one from accepted candidates
ContinuumPort         — admissibility + execution
```

Pipeline:

```
UNTRUSTED INPUT
    ↓
CandidateSet
    ↓
Simulation
    ↓
Selection
    ↓
ContinuumPort
```

Selection sits between evaluation and execution.

The output of Simulation — the accepted set — is the input to Selection. Selection narrows that set to one. ContinuumPort then decides whether to execute it.

Selection does not know whether ContinuumPort will accept the selected candidate. Volume I evaluates independently.

---

### 44.12 — Limits of the Selection Layer

The selection layer cannot:

- generate actions
- evaluate goals
- enforce admissibility
- execute transitions
- access the environment
- override geometry
- bypass authority
- validate policy determinism
- detect all forms of policy contract violation

These are deliberate design decisions.

Adding any of these capabilities to the selection layer would couple choice to enforcement — destroying the separation that makes both layers reliable.

---

### 44.13 — Correct Use of the Selection Layer

A system using the selection layer is responsible for:

- Providing candidates from the output of Simulation — not arbitrary external input.
- Supplying an explicit policy — no default is assumed.
- Treating the `SelectionResult` as advisory — never as execution authorization.
- Passing the selected candidate to ContinuumPort for independent admissibility evaluation.

The selection layer chooses what is provided. It does not validate what is intended. It does not guarantee that the selected candidate will execute successfully.

---

### 44.14 — Closure

Selection answers one question:

> Given these candidates, which one should proceed?

It does not ask whether the candidate is allowed. It does not ask whether it will succeed. It does not ask what happens next.

Those questions belong to subsequent layers.

The selection layer is bounded, policy-driven, and non-authoritative by design.

---

## Chapter 45 — Pipeline Integration

The advisory pipeline is complete.

Four layers. One direction. No authority.

---

### 45.1 — What the Pipeline Is

Chapters 41–44 defined four independent layers.

This chapter verifies that they compose correctly as a system.

The pipeline receives untrusted input and produces, at most, one candidate action to present to the execution kernel. It does not decide whether that candidate executes. It does not enforce anything. It evaluates.

The four layers in order:

```
CandidateSet  — structural normalization (Ch. 42)
Simulation    — hypothetical evaluation against a goal (Ch. 43)
Selection     — policy-driven choice (Ch. 44)
[hand-off]    — boundary to execution kernel
```

Each layer is independent. Each layer can only remove. None can add.

---

### 45.2 — Monotonicity Across the Pipeline

The pipeline satisfies a single structural invariant across all four layers:

```
|selected| ≤ 1
|accepted| ≤ |candidates|
|candidates| ≤ |input|
```

This is not a coincidence. It is a design constraint enforced at every layer:

- CandidateSet filters structurally invalid input
- Simulation filters candidates that do not satisfy the goal
- Selection chooses at most one from those that do

No layer introduces actions. The input set defines the upper bound of effects. A flooded input cannot produce more output than the input contained.

This property mirrors the monotonic filtering of the execution kernel (§39.5), extended into the advisory layers.

---

### 45.3 — Composition Without Coupling

The four layers compose without importing from each other.

```
candidate.py   does not import goal, simulation, or selection
goal.py        does not import candidate, simulation, or selection
simulation.py  does not import candidate, selection, or execution modules
selection.py   does not import simulation, goal, or execution modules
```

Each layer receives its input explicitly. Each layer returns its output as a value. There is no shared state. There is no implicit coupling.

This is the property that makes the pipeline testable in isolation and composable without surprises. Integration tests verify that the layers compose correctly — not because they are coupled, but because their contracts are compatible.

---

### 45.4 — The Hand-Off Boundary

The most important boundary in this pipeline is not between its own layers.

It is between the advisory pipeline and the execution kernel.

**What crosses this boundary:**

```
SelectionResult.selected → a plain dict with a type field
or None
```

**What does not cross:**

```
goal satisfaction status
simulation confidence
selection policy identity
any advisory metadata
```

The execution kernel receives the selected candidate as untrusted input. It re-evaluates independently:

```
AuthorityGate      — verifies origin
DomainFilter       — verifies scope
Decision           — verifies admissibility against current state
TransactionManager — verifies geometry and atomicity
```

A candidate that passes the full advisory pipeline may be rejected by any of these layers. This is not a failure of the advisory pipeline. It is the correct behavior of the execution kernel.

The hand-off is not a trust escalation.

---

### 45.5 — Separation of Concern Across Pipelines

The execution kernel pipeline:

```
A_untrusted
    ↓
SaturationGate       (Ch. 33)
    ↓
DomainFilter         (Ch. 35)
    ↓
Decision             (Ch. 31)
    ↓
TransactionManager   (Ch. 27)
    ↓
[execution]
```

The advisory pipeline:

```
UNTRUSTED INPUT
    ↓
CandidateSet         (Ch. 42)
    ↓
Simulation           (Ch. 43)
    ↓
Selection            (Ch. 44)
    ↓
[hand-off to execution kernel]
```

These are not competing pipelines. They are complementary.

The execution kernel enforces what is permitted.
The advisory pipeline narrows what is attempted.

A system using only the execution kernel can execute any valid action. A system using the advisory pipeline before the execution kernel executes only what satisfies a declared goal — subject to kernel enforcement.

```
Selection decides under policy.
Execution decides under constraint.
```

They do not substitute for each other.

---

### 45.6 — What the Integration Tests Verify

The test suite (`test_ch45_pipeline.py`) derives directly from the pipeline contract. Each test maps to a specific property.

**Happy path** — full pipeline traversal produces one selected candidate. Monotonic reduction holds across all layers. Output is deterministic.

**Nothing satisfies the goal** — Simulation produces an empty accepted set. Selection halts without calling policy. Clean halt, not an error.

**Multiple candidates satisfy** — policy controls which is selected. Partition totality holds: `selected + skipped == accepted`.

**Adversarial input** — junk, floods, malformed dicts. Invalid candidates do not propagate. Pipeline output is never larger than input.

**State isolation** — original state is not mutated through pipeline. Candidates are not mutated during simulation. Policy receives a defensive copy.

**Hand-off boundary** — selected candidate is a plain dict. No advisory metadata is present. `None` selection is a clean halt. The execution kernel re-evaluates independently.

**Non-guarantees** — four tests that document what the pipeline does not guarantee. These are not edge cases. They are documented limits.

---

### 45.7 — The Role of Non-Guarantee Tests

Most test suites test what a system does.

The non-guarantee tests verify what the system does not do — and confirm that this is stable, not accidental.

This pattern was established in Chapter 39 (`TestProperty39_13_ExplicitNonGuarantees`). It continues here.

```
test_n1 — apply ≈ real execution is not guaranteed
test_n3 — a satisfied goal does not mean correct intent
test_n4 — the pipeline has no memory across cycles
test_n5 — execution kernel may reject what advisory pipeline accepted
```

Each of these passes. Not because the system prevents the failure — but because the failure is documented, understood, and delegated to the appropriate layer.

A system that knows its limits is more trustworthy than one that does not.

---

### 45.8 — Explicit Non-Guarantees

The pipeline does not guarantee:

- that a selected candidate will be admitted by the execution kernel
- that the apply function used in Simulation matches real execution semantics
- that a satisfied goal implies correct intent
- that pipeline state is preserved across cycles
- that goal satisfaction implies execution success

These are not omissions. They follow directly from the layered design:

- Simulation evaluates consequences, not admissibility
- Selection decides under policy, not under constraint
- The execution kernel is the sole authority on what executes

---

### 45.9 — Closure

Chapters 41–45 are complete.

```
Goal         — pure evaluation of state against a condition
CandidateSet — structural normalization of untrusted input
Simulation   — hypothetical evaluation against goal
Selection    — policy-driven choice, no default strategy
Chapter 45   — integration and hand-off boundary
```

The advisory pipeline evaluates what is desired.
The execution kernel enforces what is possible.

Neither overrides the other.

627 tests. 0 failures.


<img width="2404" height="1282" alt="image" src="https://github.com/user-attachments/assets/f6196dee-d310-4497-8404-6016dd6baa63" />

**Figure 1.** — Full test suite execution (627 tests, 0 failures).

Demonstrates determinism, enforcement of formal properties, and adversarial test coverage.

---

## Chapter 46 — Signer and Authority

A Signer defines who is allowed to propose actions.

Authority defines what actions that signer is allowed to propose.

This layer establishes origin and permission.
It does not evaluate actions.
It does not execute actions.
It does not enforce admissibility.

---

### 46.1 — Formal Definition

Let:

```
s ∈ Signers
A_untrusted = set of proposed actions
```

Each action is associated with a signer:

```
a = (s, payload)
```

Authority is a mapping:

```
Authority : Signer → P(ActionType)
```

where:

```
ActionType = a["type"]
```

An action is authority-valid if:

```
ActionType ∈ Authority(s)
```

If a signer is not present in Authority:

```
Authority(s) = ∅
```

Fail-closed.

---

### 46.2 — Signer Binding

The signer identity is not taken from the payload.

It is derived from signature verification and bound to the action before authority evaluation.

Formally:

```
verify_signature(payload, signature) → s
```

The signer used in authority evaluation is the one obtained from verified signature material.

Any signer field present in the payload is ignored.

This prevents impersonation via payload injection.

---

### 46.3 — Verification Order

Authority evaluation is performed only after successful signature verification.

The evaluation sequence is:

```
verify_signature → extract_signer → authority_check
```

If signature verification fails, authority evaluation is not performed.

This ordering is strict.

---

### 46.4 — Separation from Other Layers

The authority layer is independent of all other layers.

```
signer.py     — identity and signature verification
authority.py  — authority mapping
candidate.py  — structural normalization
goal.py       — goal evaluation
simulation.py — hypothetical evaluation
selection.py  — policy choice
```

There are no imports between `authority.py` and any advisory or execution modules.

Authority does not know:

* whether an action satisfies a goal
* whether an action will be selected
* whether an action will execute

It evaluates only origin and permission.

---

### 46.5 — Authority Binding

Authority is explicitly configured.

```
Authority(s) = {t₁, t₂, ..., tₙ}
```

No implicit permissions exist.

There is no wildcard.
There is no inheritance.
There is no default allow.

If an action type is not explicitly listed, it is not allowed.

---

### 46.6 — Fail-Closed Behavior

If a signer is unknown:

```
Authority(s) = ∅
```

If an action type is not declared:

```
a is rejected
```

If authority configuration is missing:

```
no actions are allowed
```

All undefined states resolve to no permission.

---

### 46.7 — Non-Escalation of Authority

Authority is immutable during execution.

No action can:

* modify Authority mapping
* grant new permissions to a signer
* alter its own permission surface
* impersonate another signer

Formally:

```
execute(a) cannot change Authority(s)
```

Authority is an input to the system, not a state variable.

---

### 46.8 — Stateless Evaluation

Authority evaluation depends only on:

```
(s, a["type"])
```

It does not depend on:

* past actions
* ordering of actions
* frequency of requests
* system history

```
authority_check(s, a) → {allowed, rejected}
```

is a pure function.

Authority does not enforce rate limits or behavioral constraints.

Such controls belong to the control plane or external systems.

---

### 46.9 — Authority vs Domain

Authority defines the maximum permission set of a signer.

DomainFilter (Ch. 35) may further restrict this set per execution context.

Authority is global and static.
Domain is contextual and potentially dynamic.

Formally:

```
Allowed_by_domain ⊆ Authority(s)
```

Authority does not depend on domain.
Domain cannot expand authority.

---

### 46.10 — Independence from Execution

Authority validation does not imply execution.

```
allowed_by_authority(a) ≠ executable(a)
```

An authority-valid action may still be rejected by:

* domain constraints
* geometry constraints
* state conditions

Authority answers only:

> Is this signer allowed to propose this type of action?

---

### 46.11 — Failure Modes

```
AuthorityError(INVALID_SIGNATURE) — signature verification failed
AuthorityError(UNKNOWN_SIGNER)    — signer not in authority mapping
AuthorityError(UNAUTHORIZED_TYPE) — action type not permitted
```

`AuthorityError` is distinct from all other layer errors:

```
AuthorityError ≠ CandidateError
AuthorityError ≠ GoalError
AuthorityError ≠ SimulationLayerError
AuthorityError ≠ SelectionError
AuthorityError ≠ GeometryError
AuthorityError ≠ ExecutionError
```

Each error remains confined to its layer.

---

### 46.12 — Limits of the Authority Layer

The authority layer cannot:

* validate action structure
* evaluate goals
* simulate outcomes
* enforce admissibility
* execute actions
* access environment state
* resolve conflicts between actions

These are deliberate design constraints.

Authority defines permission, not correctness.

---

### 46.13 — Correct Use of the Authority Layer

A system using the authority layer is responsible for:

1. Verifying signatures before authority evaluation.
2. Binding signer identity from verified signature — not payload.
3. Providing an explicit Authority mapping.
4. Treating unknown signers as having zero permissions.
5. Passing only authority-valid actions to subsequent layers.
6. Not assuming authority implies execution.

Authority is a gate on origin and scope.

It is not a guarantee of success.

---

### 46.14 — Closure

The authority layer answers one question:

> Who is allowed to propose this action?

It does not ask whether the action is valid.
It does not ask whether the action is desirable.
It does not ask whether the action will execute.

Those questions belong to other layers.

Authority defines permission.
Nothing more.

---

## Chapter 47 — Pipeline Integrity

The advisory pipeline produces a selection.
The execution kernel enforces admissibility.

Between them is a boundary.

This chapter defines what that boundary guarantees, what it does not guarantee, and what can go wrong at the point of transfer.

---

### 47.1 — The Boundary Is Not a Trust Escalation

When the advisory pipeline completes, it produces at most one candidate:

```
SelectionResult.selected → dict | None
```

That candidate crosses the boundary into the execution kernel as untrusted input.

The execution kernel does not inherit the advisory pipeline's evaluation.

It does not know:

- that the candidate satisfied a goal
- that simulation ran
- that a policy chose it
- that any evaluation occurred at all

The kernel re-evaluates from scratch:

```
AuthorityGate      — verifies origin
DomainFilter       — verifies scope
Decision           — verifies admissibility against current state
TransactionManager — verifies geometry and atomicity
```

The hand-off is not approval. It is submission.

---

### 47.2 — What Integrity Means Here

Pipeline integrity is not a property of the advisory pipeline alone.

It is a property of the full system from untrusted input to committed state transition.

A pipeline has integrity if:

- no candidate executes without passing through both pipelines
- no advisory result bypasses execution kernel evaluation
- no state changes occur as a side effect of advisory evaluation
- the boundary carries data, not authority

Integrity fails if any of these conditions are violated — including through omission, shortcut, or assumed trust at the boundary.

---

### 47.3 — Failure at the Boundary

Three failure modes are specific to the boundary between advisory and execution.

**Trust escalation**

The execution kernel trusts advisory results and skips its own evaluation.

This is the most dangerous form of boundary failure.

The advisory pipeline is not an authority layer. It is an evaluation layer. Its output is a plain dict.

A kernel that promotes advisory output to authorized input has collapsed the separation between evaluation and enforcement.

**State mutation during advisory evaluation**

A goal, simulation, or selection step modifies state as a side effect.

Chapters 41–44 guarantee this cannot happen within their own layers.

It can still happen if the caller passes a live environment reference instead of a snapshot, or if the `apply` function in Simulation has access to mutable external state.

The boundary cannot enforce what happens before it. The caller is responsible for providing clean inputs.

**Metadata leakage**

Advisory metadata — goal satisfaction status, simulation confidence, selection policy identity — accompanies the candidate across the boundary and influences kernel evaluation.

This is a subtle form of coupling.

The kernel must receive only the candidate dict. Nothing else from the advisory pipeline should be visible to or relied upon by the kernel.

---

### 47.4 — The Role of the apply Function

Simulation requires an external transition function:

```
apply(state, action) → state_after
```

This function is the point of greatest divergence risk in the full pipeline.

If `apply` does not faithfully model real execution semantics, Simulation produces results that do not predict what the execution kernel will do.

A candidate accepted by Simulation may be rejected by the kernel.

A candidate rejected by Simulation may have been accepted by the kernel.

This divergence is not detectable by either pipeline.

It is a model limit, not a defect.

**Consequence for pipeline integrity:**

Pipeline integrity does not require that advisory and execution pipelines agree.

It requires that they remain independent — so that disagreement is resolved by the kernel, not hidden by the advisory layer.

If advisory evaluation were authoritative, divergence between `apply` and real execution would be a security failure.

Because advisory evaluation is not authoritative, divergence is only an efficiency concern: the system selected a candidate that was then rejected.

Separation is what makes this safe.

---

### 47.5 — Monotonicity Across Both Pipelines

The advisory pipeline satisfies monotonic reduction:

```
|selected| ≤ |accepted| ≤ |candidates| ≤ |input|
```

The execution kernel satisfies monotonic filtering:

```
A′ ⊆ A_domain ⊆ A_considered ⊆ A_untrusted
```

Both pipelines reduce. Neither expands.

The full system from untrusted input to committed state satisfies:

```
|committed| ≤ 1
|submitted to kernel| ≤ |selected| ≤ |input|
```

No execution can exceed what was submitted.
No submission can exceed what was selected.
No selection can exceed what was simulated.
No simulation can exceed what was structured.

The input set defines the upper bound of all effects.

---

### 47.6 — What Survives the Boundary

Exactly one thing crosses from advisory to execution:

```
{"type": ..., ...}  — a plain dict
```

or nothing.

What does not cross:

- goal evaluation result
- simulation accepted/rejected partition
- selection policy identity
- advisory error state
- any reference to the state snapshot used in simulation

The boundary is a data transfer, not a context transfer.

This is by design.

If context crossed the boundary, the execution kernel would need to reason about advisory history.

Advisory history is not part of the execution model.

---

### 47.7 — Failure Is Informative, Not Catastrophic

A candidate rejected by the execution kernel after passing the advisory pipeline is not a system failure.

It is the system operating correctly.

The advisory pipeline evaluated desirability.
The execution kernel evaluated admissibility.
They disagreed.

The kernel's answer is authoritative.

This outcome reveals one of two things:

1. The `apply` function in Simulation does not model execution semantics accurately.
2. State changed between advisory evaluation and kernel evaluation.

Both are informative. Neither requires a correction to the pipeline structure.

The system should surface this outcome — it is useful signal for the control plane.

It should not suppress it.

---

### 47.8 — Limits of Pipeline Integrity

Pipeline integrity as defined here cannot guarantee:

- that `apply` matches execution semantics
- that state is identical at advisory time and kernel time
- that the policy chose the optimal candidate
- that goal satisfaction implies correct intent
- that the selected candidate will be admitted

These are documented limits inherited from the individual layers.

Pipeline integrity guarantees only structural properties:

- no state mutation during advisory evaluation
- no authority escalation at the boundary
- no metadata leakage from advisory to execution
- monotonic reduction holds across both pipelines

---

### 47.9 — Correct Integration

A system integrating both pipelines is responsible for:

1. Providing a state snapshot to advisory evaluation — not a live environment reference.
2. Providing an `apply` function that faithfully models execution semantics.
3. Passing only the selected candidate dict to the execution kernel — no advisory context.
4. Treating kernel rejection of an advisory-accepted candidate as informative signal, not system failure.
5. Not caching or reusing advisory results across cycles — each cycle evaluates independently.

The advisory pipeline does not replace the execution kernel.

It narrows what the kernel is asked to evaluate.

---

### 47.10 — Closure

Pipeline integrity is the property that ensures the advisory and execution pipelines remain structurally independent while composing correctly.

The advisory pipeline answers: what is worth attempting?

The execution kernel answers: what is permitted to occur?

Neither question subsumes the other.

A system with pipeline integrity does not trust advisory results.

It uses them.

---

## Chapter 48 — Threat Model

The system is designed under adversarial assumptions.

Every external input is untrusted.
Every callable is potentially malicious.
Every boundary is a point of attack.

This chapter defines the attack surface, the defenses enforced by each layer, and the residual risks that remain by design.

---

### 48.1 — Threat Model Scope

The system assumes an adversary capable of:

- submitting arbitrary action payloads
- forging or replaying requests
- attempting state mutation outside execution
- exploiting inconsistencies between layers
- abusing volume, timing, or ordering

The adversary does not have:

- direct write access to execution state
- ability to modify Authority or Domain configuration
- ability to bypass the execution kernel

All defenses are evaluated under these constraints.

---

### 48.2 — Attack Surface Overview

The system exposes four primary attack surfaces:

```
1. Input Surface       — untrusted action submission
2. Advisory Surface    — evaluation pipeline (Goal, Simulation, Selection)
3. Boundary Surface    — hand-off between advisory and execution
4. Execution Surface   — enforcement pipeline (Authority, Domain, Geometry)
```

Each surface is independent.

A successful attack must either bypass all relevant layers, or exploit a property not enforced by any layer.

---

### 48.3 — Input Surface Attacks

**Attack Class: Malformed or Adversarial Input**

Examples: non-dict payloads, missing or empty `"type"`, oversized or flooded candidate sets, structurally valid but semantically meaningless actions.

**Defense: CandidateSet (Ch. 42)**

```
C ⊆ Input
```

Structural validation only. Silent filtering of invalid entries. No expansion of input.

**Residual Risk:**

Structurally valid but malicious actions pass through. Semantic correctness is not enforced at this layer. This is intentional.

---

### 48.4 — Identity and Authority Attacks

**Attack Class: Impersonation / Unauthorized Actions**

Examples: forging signer identity in payload, replaying signed requests, submitting actions outside declared authority.

**Defense: Signer + Authority (Ch. 46)**

```
verify_signature → extract_signer → authority_check
```

Signer is derived from signature, not payload. Fail-closed authority mapping. Unauthorized action types are rejected before any evaluation occurs.

**Residual Risk:**

Replay attacks across cycles (no nonce enforcement at this layer). Compromised signer keys. These are explicitly out of scope for the engine layer.

---

### 48.5 — Advisory Surface Attacks

**Attack Class: Evaluation Manipulation**

Examples: malicious Goal function, adversarial `apply` function, policy that selects harmful candidates, mutation of state during evaluation.

**Defense: Advisory Isolation (Ch. 41–44)**

Defensive copies of state and candidates at every evaluation step. Mutation detection after evaluation. No authority to execute — advisory output is not trusted by the execution kernel.

**Key Property:**

```
advisory_output ≠ execution
```

**Residual Risk:**

Incorrect evaluation due to faulty Goal or `apply`. Selection of suboptimal or harmful candidate. These do not compromise safety — they affect only efficiency. The execution kernel re-evaluates independently.

---

### 48.6 — Boundary Attacks

**Attack Class: Trust Escalation**

Examples: execution kernel trusting advisory results, metadata leakage influencing execution, skipping enforcement based on prior evaluation.

**Defense: Strict Boundary (Ch. 45–47)**

```
input_to_kernel = plain dict | None
```

No metadata crosses the boundary. Advisory results are not trusted. The kernel re-evaluates from scratch: AuthorityGate → DomainFilter → Decision → TransactionManager.

**Residual Risk:**

Incorrect system integration outside the defined model. This is a system integration failure, not a model failure.

---

### 48.7 — Execution Surface Attacks

**Attack Class: Unauthorized State Transition**

Examples: bypassing domain constraints, violating geometry rules, TOCTOU (time-of-check to time-of-use), partial state commits.

**Defense: Execution Kernel (Volume I)**

```
SaturationGate       — bounded intake (Ch. 33)
DomainFilter         — scope restriction (Ch. 35)
Decision             — admissibility (Ch. 31)
TransactionManager   — atomic commit + rollback (Ch. 27)
```

Properties enforced: atomicity, state-local constraints, divergence collapse, no partial execution.

**Residual Risk:**

Incorrect geometry definitions. Misconfigured domain constraints. The kernel enforces rules. It does not validate their correctness.

---

### 48.8 — Cross-Layer Attacks

**Attack Class: Inconsistency Exploitation**

Examples: Simulation accepts, kernel rejects. Goal satisfied under incorrect assumptions. `apply` semantics diverge from real execution semantics.

**Defense: Layer Independence**

No layer trusts another.

```
evaluation ≠ enforcement
```

Disagreement is resolved by the execution kernel. The kernel's answer is authoritative.

**Residual Risk:**

Wasted computation. Degraded efficiency. Not a security failure.

---

### 48.9 — Denial of Service

**Attack Class: Resource Exhaustion**

Examples: flooding candidate sets, repeated cycle submissions, expensive evaluation functions.

**Defense:**

```
SaturationGate (Ch. 33)  — limits actions per cycle, O(1) rejection cost
DomainFilter   (Ch. 35)  — further reduces A_considered before decision
```

Both defenses are part of the execution kernel, not the advisory pipeline. They operate before any semantic evaluation occurs.

**Residual Risk:**

Repeated valid cycles consuming execution resources. External resource exhaustion (network, disk) from committed actions. Rate limiting and scheduling belong to the control plane.

---

### 48.10 — Capsule and Cross-Session Attacks

**Attack Class: State Transfer Exploitation**

Examples: replaying a valid capsule from session A into session B, swapping geometry between sessions, exploiting hash canonicalization to bypass integrity checks, persisting adversarial state (e.g. locks) across session boundaries.

**Defense: StateCapsule (Appendix A)**

```
state_hash      — SHA-256 of canonical JSON state (sort_keys=True)
authority_id    — bound signer verified before reconstruct()
CapsuleError    — raised on tamper, authority mismatch, inadmissible action
```

Integrity is hash-verified before reconstruction. Authority is verified before any state is written. Geometry is applied at reconstruction time, not capsule creation time.

**Residual Risk (documented):**

- Geometry is not embedded in the capsule. A capsule created under geometry G₁ may be reconstructed under geometry G₂. If G₂ is more permissive, actions blocked by G₁ may pass. This is a model limit — geometry binding is operational, not structural (V2, V6 in test suite).
- Capsule replay across sessions is not prevented at the engine layer. The control plane is responsible for nonce enforcement and replay logs (V1 in test suite).
- Lock state (or any adversarial state) survives capsule round-trips. The engine does not auto-clear locks or interpret state semantics. Recovery decisions belong to the control plane (V5 in test suite).
- JSON canonicalization distinguishes all standard primitive types. Non-serializable state is rejected at capsule creation. Collision via payload substitution is infeasible under SHA-256 (V7 in test suite).

---

### 48.11 — Non-Guarantees as Attack Boundaries

The system explicitly does not defend against:

- replay across cycles (no nonce at engine layer)
- incorrect intent encoded in valid actions
- divergence between simulation and execution semantics
- temporal manipulation (no internal clock)
- geometry or authority misconfiguration by operators
- capsule replay across sessions (control plane responsibility)

These are not vulnerabilities.

They define the boundary of the model.

---

### 48.12 — Security Invariant

Across all layers, a single invariant holds:

```
No action can execute unless it passes all enforcement layers
under current state and authority.
```

This invariant is independent of advisory evaluation, policy decisions, and input structure. It is enforced exclusively by the execution kernel.

---

### 48.13 — Closure

The system does not attempt to prevent all failures.

It prevents a specific class of failures:

> unauthorized, invalid, or inconsistent state transitions.

All other risks are isolated, documented, and delegated to external systems.

Security does not come from prediction.

It comes from enforcement.

The system enforces.

---

## Chapter 49 — Failure Composition

The system enforces safety through independent layers.

Each layer can fail. Each layer fails independently.

This chapter defines how failures compose across layers, what properties
hold under all compositions, and what remains outside the model's scope.

### 49.1 — Adversarial Assumption

The system does not assume correct input.

It assumes pressure.

The adversarial model (defined in Ch. 48) establishes that the system
operates under untrusted input, arbitrary payloads, replay attempts, and
volume attacks.

This chapter extends that model to the composition of failures:
what happens when multiple layers interact under adversarial conditions.

### 49.2 — Layer Independence Under Failure

Let:

    L = {Authority, Domain, Decision, Geometry, Transaction}

Each layer evaluates independently. No layer assumes another layer
has evaluated correctly.

For any two distinct layers l₁, l₂ ∈ L:

    failure(l₁) ⇒ semantics(l₂) unchanged

A failure in the authority layer does not alter geometry rules.
A failure in the geometry layer does not modify domain configuration.
A failure in the transaction layer does not expose partial state.

Failures isolate. They do not cascade into semantic corruption of
other layers.

### 49.3 — Execution as Conjunction

Execution requires all enforcement layers to pass:

    execute(a) ⇔ ∀ l ∈ L : passes_l(a)

Equivalently:

    ∃ l ∈ L : ¬passes_l(a) ⇒ ¬execute(a)

No action executes unless every layer allows it. There is no partial
passage. There is no weighted evaluation. The conjunction is strict.

### 49.4 — Non-Compensability

No layer can compensate for the failure of another.

    passes(l₁) ∧ ¬passes(l₂) ⇒ ¬execute(a)

Authority success does not compensate for domain failure.
Domain success does not compensate for geometry failure.
Geometry success does not compensate for TOCTOU rejection.

Safety is conjunctive, not additive.

A system that passes n-1 layers and fails on the nth does not receive
partial credit. It does not execute.

### 49.5 — Monotonic Failure Propagation

Let A₀ be the input action set.

Each enforcement layer applies a reductive transformation:

    A₁ ⊆ A₀
    A₂ ⊆ A₁
    ...
    Aₙ ⊆ Aₙ₋₁

If any layer produces an empty set:

    ∃ i : Aᵢ = ∅ ⇒ ∀ j > i : Aⱼ = ∅

Collapse propagates forward and cannot be reversed by subsequent layers.

This is the same monotonic reduction property established in Ch. 39.5
and extended into the advisory pipeline in Ch. 45.2. It holds across
the full system.

### 49.6 — Failure Non-Interference

Layer failures do not alter the semantics of other layers.

Specifically:

- Authority failure does not modify geometry rules
- Geometry failure does not affect domain configuration
- Decision failure does not mutate environment state
- Transaction failure restores state to the pre-execution snapshot

The last point is structural, not behavioral. TransactionManager does
not "decide" to restore state after failure. It maintains the snapshot
and never commits unless all steps succeed. Restoration is the default.

### 49.7 — Atomic Failure Closure

Execution outcomes are binary:

    commit(ops) ⇒ state = state_after
    failure      ⇒ state = state_before

No intermediate state is observable or persistent:

    ¬∃ state_intermediate : observable(state_intermediate)

This is the atomicity property from Ch. 39.2, stated here in terms of
failure composition. A failure at any step in a multi-step transaction
produces the same outcome as a failure at the first step: complete
restoration.

There is no partial success. There is no residue.

### 49.8 — Security Invariants

The following invariants hold for all executions under all compositions
of input, layer outcomes, and failure modes.

**I1 — No Unauthorized Execution**

    ¬passes(Authority) ⇒ ¬execute(a)

**I2 — No Out-of-Domain Execution**

    ¬passes(Domain) ⇒ ¬execute(a)

**I3 — No Invalid State Transition**

    ¬passes(Geometry ∧ State constraints) ⇒ ¬execute(a)

**I4 — No Partial State Escape**

    failure ⇒ state = state_before

**I5 — Deterministic Outcome**

    same(state₀, input) ⇒ same(result)

**I6 — No Authority Escalation**

    execute(a) ⇏ change(Authority)

Authority is an input to the system, not a state variable. No
execution can expand or modify the authority mapping.

**I7 — Layer Independence**

    ∀ l₁, l₂ ∈ L, l₁ ≠ l₂ : failure(l₁) ⇒ semantics(l₂) unchanged

These invariants are not aspirational. They are structural consequences
of the architecture defined in Chapters 27–48. The test suite validates
them empirically. They do not require correct input, correct goals,
or correct operator configuration to hold.

### 49.9 — Failure Visibility

Failures are observable. They are not recoverable within the cycle.

Each failure produces:

- a typed error from the layer that detected it (Ch. 39.12)
- no state mutation

The error type identifies the layer. The layer identification is
exact: AuthorityError comes only from the authority layer,
GeometryError only from geometry, and so on. The error taxonomy
in execution/errors.py enforces this (Ch. 39.12, test_error_taxonomy.py).

Recovery is external to the execution model. The control plane
(Ch. 38) receives the failure and decides what to do next. The
execution model reports accurately. It does not decide.

### 49.10 — Composition with Advisory Pipeline Failures

The advisory pipeline (Ch. 41–45) can produce incorrect evaluations
without triggering safety failures.

A malicious Goal, an inaccurate apply function, or a suboptimal
Selection policy can cause the wrong candidate to be submitted to
the execution kernel. The kernel re-evaluates independently. If the
candidate is inadmissible, it is rejected.

This means advisory failures are absorbed by the execution kernel.
They become efficiency failures — wasted evaluation, rejected candidates —
not security failures.

The separation between advisory evaluation and execution enforcement
is what makes this absorption possible. If advisory results were
trusted by the kernel, an advisory failure would become a security
failure.

### 49.11 — Interaction with Documented Non-Guarantees

Failure composition does not eliminate the limits documented in
Ch. 39.13 and RFC-002 §7.

The following remain outside the composition model:

- replay across cycles: not detected at engine layer
- simulation divergence from execution: not detectable by either pipeline
- intent correctness: not enforced by any layer
- cross-cycle ordering: not maintained by the system
- temporal constraints: not expressible without external clock

These are not gaps in failure composition. They are properties that
require memory, sequence reasoning, or external truth — none of which
the execution model provides.

Failures are closed within a cycle.
These limits exist across cycles.

They are complementary, not contradictory.

### 49.12 — Boundary of Responsibility

The execution model guarantees:

- enforcement of I1–I7 under all compositions
- atomicity of state transitions
- isolation of layer failures
- accurate failure reporting

The execution model does not guarantee:

- correctness of goals
- correctness of simulation
- correctness of operator-defined geometry
- correctness of external systems

Responsibility is partitioned by design. The execution model enforces
what is declared. It does not validate whether what was declared is correct.

This boundary is stated explicitly because it is the most common source
of misuse: treating enforcement of declared rules as a guarantee that
the rules themselves are correct.

### 49.13 — Closure

Safety is not defined by successful execution.

It is defined by the closure of all failure paths.

The system does not assume correct input.
It does not assume correct evaluation.
It does not assume correct intent.

It assumes pressure — and enforces that pressure cannot produce
unauthorized state transitions.

Security is not achieved by predicting behavior.

It is achieved by making invalid transitions structurally impossible.

The invariants in §49.8 are not features. They are the minimum
conditions under which the system is safe.

They hold regardless of what the advisory pipeline recommends,
regardless of what the control plane submits, and regardless of
what the input contains.

They hold because of what the architecture prevents.

---

## Chapter 50 — Conformance and Semantic Alignment

The system defines two distinct transition functions:

    f(s, a)  — simulated transition, used by the advisory pipeline
    F(s, a)  — execution transition, enforced by the kernel

This chapter defines what alignment between these functions means,
how divergence is classified, and how the system behaves under
misalignment.

### 50.1 — The Two Transitions

The advisory pipeline (Ch. 41–45) evaluates actions by applying
a caller-provided transition function:

    f : (State, Action) → State

The execution kernel (Ch. 27–39) applies actions through the
capability and transaction layer:

    F : (State, Action) → State | ⊥

F may reject: a geometry violation, TOCTOU drift, or authority failure
produces ⊥ (no state transition). f has no mechanism to produce ⊥ —
it returns a state in all cases.

There is no inherent guarantee that f(s, a) = F(s, a).

This gap is the subject of this chapter.

### 50.2 — Semantic Alignment

Alignment is defined over observable, canonical state:

    aligned(s, a) ⟺ canonical(f(s, a)) = canonical(F(s, a))

Where canonical is a normalization function that removes key-ordering
variance and representation differences while preserving all state
semantics. The same canonical function is used for state hashing
throughout the system (Ch. 39.1, Appendix A).

Alignment is defined over pairs (s, a), not globally. f may be aligned
for most (s, a) pairs and diverge on a specific combination.

### 50.3 — Conformance Requirement

f is conformant to F if:

    f ⊑ F

Meaning:

    ∀ s, a : aligned(s, a)

A conformant f does not produce effects that F would not produce,
and does not omit effects that F would produce.

Conformance is a property of the caller-provided apply function,
not of the advisory pipeline itself. The pipeline enforces isolation,
purity, and determinism of f (Ch. 43). It does not enforce that f
models F correctly. That is the caller's responsibility.

### 50.4 — Sources of Divergence

Divergence between f and F may arise from:

- incomplete apply implementation (missing field updates)
- capability behavior not modeled in simulation (e.g. append semantics)
- implicit state changes during execution not present in apply
- external side effects that F commits but f cannot see
- non-deterministic execution paths introduced by external systems

These sources are not detectable by the advisory pipeline.
The pipeline treats f as opaque (Ch. 43.2).

### 50.5 — Divergence Classification

Three classes of divergence, ordered by consequence:

**D1 — False Acceptance**

    f(s, a) → admissible state
    F(s, a) → ⊥

Simulation accepts. Execution rejects.

Consequence: wasted evaluation, no state change. Safe.
The execution kernel catches this and the system halts cleanly.

**D2 — False Rejection**

    f(s, a) → inadmissible state
    F(s, a) → valid state

Simulation rejects. Execution would have accepted.

Consequence: lost opportunity. Safe.
The candidate is not selected and not submitted to the kernel.

**D3 — Semantic Mismatch**

    f(s, a) → s'
    F(s, a) → s''
    canonical(s') ≠ canonical(s'')

Both produce a state, but different states.

Consequence: goal evaluation and selection operate on incorrect
predictions. The selected candidate may satisfy the goal under f
but produce a different state under F. This is the most consequential
divergence class.

D3 does not compromise safety. The execution kernel still enforces
geometry, authority, and atomicity under F. But it degrades the
usefulness of the advisory pipeline — the system commits a state
that the goal was not evaluated against.

### 50.6 — Safety Under Divergence

Divergence does not affect execution correctness.

Under any divergence class:

    execute(a) ⇔ ∀ l ∈ L : passes_l(a)

This is the conjunction property from Ch. 49.3. It depends only on F,
not on f. The advisory pipeline does not participate in enforcement.

Divergence degrades advisory quality. It does not weaken the invariants
established in Ch. 49.8.

### 50.7 — F as the Single Source of Truth

Execution defines state transition semantics.

The correct construction of f is:

    f(s, a) := simulate(F)(s, a)

Where simulate(F) is a projection of the execution path that
returns the resulting state without committing.

The incorrect construction is:

    f := independent implementation with duplicated logic

An independent implementation introduces a parallel semantic definition.
Divergence between two independent implementations is structurally
guaranteed over time. A projection of F is not a second implementation —
it is the same implementation run without side effects.

Where the execution kernel provides a dry-run path (see §50.8),
that path is the preferred source for f.

### 50.8 — Conformance Testing

Conformance between f and F can be verified empirically for a given
set of (s, a) pairs:

    For each (s, a):
        s₀      = snapshot(s)
        s_sim   = f(copy(s₀), a)
        s_exec  = F_dry_run(s₀, a)

        assert canonical(s_sim) == canonical(s_exec)

Where F_dry_run executes the full capability and transaction path
without committing the result to the environment.

Conformance tests provide coverage, not proof. They establish that
f and F agree on the tested pairs. Untested pairs may still diverge.

The test structure mirrors the advisory pipeline's own isolation
guarantees: snapshot before, comparison after, no mutation of the
baseline.

### 50.9 — Canonicalization Requirements

The canonical function used for alignment evaluation must satisfy:

- deterministic: same state always produces same representation
- complete: no state information is lost
- stable: behavior does not change across cycles or sessions
- consistent: the same function used for state hashing (Ch. 39.1)

The last requirement is important. If alignment uses a different
canonical function than state hashing, drift may be masked by
representation differences that the hash would detect and alignment
would not.

### 50.10 — Interaction with Failure Composition

Semantic drift (D1, D2, D3) does not alter the failure composition
properties established in Ch. 49.

Specifically:

- I1–I7 (Ch. 49.8) hold regardless of divergence between f and F
- Monotonic failure propagation (Ch. 49.5) is unaffected
- Atomic failure closure (Ch. 49.7) applies to F, not f

Drift is an advisory property. It operates above the enforcement
boundary. The enforcement boundary remains closed under drift.

### 50.11 — Responsibility Partition

The execution model guarantees:

- enforcement of all constraints under F
- atomic and deterministic execution
- independence from f correctness

The advisory pipeline assumes:

- f approximates F sufficiently to make goal evaluation meaningful

The control plane is responsible for:

- monitoring alignment between f and F
- reacting to persistent D3 divergence
- updating f when F semantics change

This partition follows the general model established in Ch. 38:
the execution model enforces, the control plane decides.

### 50.12 — Non-Guarantees

The system does not guarantee:

- perfect alignment between f and F
- detection of all divergence instances
- equivalence for non-observable side effects
- correctness of external systems invoked by F
- that conformance tests cover all (s, a) pairs

Alignment is verifiable on tested pairs. It is not provable in general
without a formal equivalence proof between f and F — which requires
f to be derived from F, not defined independently.

### 50.13 — Closure

The system separates what is evaluated from what is enforced.

This separation is necessary for the advisory pipeline to operate
without authority. It is also the source of the alignment requirement:
when evaluation and enforcement are separate, their agreement cannot
be assumed.

Simulation proposes. Execution decides.

Alignment is desirable. It is not required for safety.

Safety does not depend on f being correct.

It depends on F being constrained.

The system does not assume that its predictions are accurate.

It ensures that inaccurate predictions cannot produce unauthorized
state transitions.

---

## Chapter 51 — Control Plane and Temporal Guarantees

The execution kernel operates on a single cycle.

It guarantees correctness within that cycle.

This chapter defines what happens across cycles — where time, ordering,
and persistence introduce properties that the execution model does not
express and cannot enforce.

### 51.1 — Scope of the Control Plane

The control plane (Ch. 38) exists outside the execution model.

It is responsible for:

- submission of cycles
- sequencing across cycles
- retry and replay decisions
- capsule storage and restoration
- interpretation of execution results over time

The execution model does not maintain history between cycles.
Temporal behavior is defined entirely by the control plane.

### 51.2 — Absence of Temporal Semantics in the Kernel

The execution kernel has no notion of time, ordering between cycles,
identity persistence, replay detection, or idempotency.

Each cycle is evaluated independently:

    ∀ cycles c₁, c₂ : execute(c₁) ⟂ execute(c₂)

No state is carried between cycles except what is explicitly passed as
input state. The kernel does not know it is cycle N. It does not know
what happened in cycle N-1.

This is not a gap. It is the property that makes the kernel stateless,
deterministic, and independent of orchestration history.

### 51.3 — Replay Semantics

The execution model permits replay:

    execute(s, a) → s'
    execute(s, a) again → s'   (same result)

Replay does not accumulate hidden effects. This is a direct consequence
of determinism (Ch. 39.1), atomicity (Ch. 39.2), and controlled state
mutation (Ch. 39.9).

Replay safety is guaranteed by the kernel.
Replay prevention is not.

If the same (s, a) pair is submitted twice, the kernel executes it
twice and produces the same result twice. It has no mechanism to detect
that the pair was already submitted.

### 51.4 — Idempotency as External Property

The kernel does not enforce idempotency.

An action may or may not be idempotent in its effects. The kernel does
not distinguish these cases. Detection of duplicate submissions requires
action identity, historical tracking, and comparison across cycles —
none of which exist in the execution model.

The control plane may define idempotency keys and deduplication logic.
This is outside the execution model boundary.

### 51.5 — Ordering and Causality

The execution model does not enforce ordering across cycles.

    execute(a₁) then execute(a₂)

is not guaranteed to produce the same result as:

    execute(a₂) then execute(a₁)

unless the state transitions are order-independent by nature, or the
control plane enforces a specific ordering before submission.

Causal dependencies, serialization constraints, and sequencing rules
belong to the control plane. The kernel evaluates each cycle against
current state. It does not reason about prior or future cycles.

### 51.6 — Capsule as Temporal Boundary

Capsules (Appendix A) provide state snapshot, integrity verification,
and optional authority binding.

They do not provide history, ordering guarantees, or replay protection.

A capsule represents a point in time, not a timeline.

Reconstructing from a capsule initializes the environment from a
validated state. It does not restore execution history, cycle identity,
or any record of what preceded the capsule. This is by design: continuity
is a property of the state, not the agent (Ch. 40).

### 51.7 — Interaction with Failure Composition

Failure composition (Ch. 49) applies within a cycle.

Invariants I1–I7 hold per cycle:

    ∀ cycle c : invariants(c) hold

But invariants across cycles do not compose automatically:

    invariants(c₁) ∧ invariants(c₂) ⇏ invariants(c₁ followed by c₂)

A sequence of individually correct cycles can produce incorrect
cross-cycle behavior if the control plane submits them in the wrong
order, replays them, or skips error handling between them.

Temporal correctness is not derived from per-cycle correctness.
It must be constructed above the execution model.

### 51.8 — Interaction with Semantic Alignment

Semantic alignment (Ch. 50) is evaluated per cycle.

Across cycles, D3 divergence (semantic mismatch between f and F) may
accumulate if the apply function drifts from execution semantics over
time — for example, when execution capabilities are updated but the
simulation function is not.

The execution model does not detect this pattern. The control plane
is responsible for monitoring alignment across cycles and triggering
updates to the apply function when persistent divergence is observed.

### 51.9 — Temporal Failure Modes

Failures specific to cross-cycle behavior include replay flooding,
stale proposals based on outdated state, out-of-order execution,
duplicated submissions, and lost cycles.

These are not failures of execution. They are failures of orchestration.

The execution model reports what happened within each cycle accurately.
It does not detect that a cycle was duplicated, reordered, or missed.
That detection belongs to the control plane.

### 51.10 — Control Plane Responsibilities

If temporal guarantees are required, the control plane must provide:

- submission identity (idempotency keys per cycle)
- ordering constraints (sequence numbers or causal tokens)
- retry policies (when to resubmit a failed cycle)
- replay limits (maximum resubmissions per action)
- divergence monitoring (detecting persistent D3 across cycles)

The execution model provides correct execution, correct rejection,
and correct state transitions — per cycle. The control plane ensures
these are used correctly over time.

The separation is strict. The kernel does not depend on temporal
correctness to function. It executes what it receives, correctly,
regardless of whether the sequence was appropriate.

### 51.11 — Non-Guarantees

The system does not guarantee:

- replay prevention across cycles
- global ordering of cycles
- exactly-once execution of non-idempotent actions
- temporal consistency across sessions
- convergence of state over time
- absence of duplicate effects from repeated submission

These require persistent state, coordination primitives, and sequence
tracking — none of which are part of the execution model.

They are explicitly out of scope (Ch. 39.13, RFC-002 §7 N4).

### 51.12 — Closure

The execution model is safe within a cycle.

Time introduces complexity that the kernel deliberately excludes.
The control plane reintroduces time under explicit, external control.

Correctness does not extend automatically across cycles.
It must be constructed by the layer responsible for orchestration.

The kernel does not assume correct sequencing.
It enforces correct execution regardless of sequence.

Temporal safety is not a property of execution.
It is a property of orchestration.

---

## Chapter 52 — System Limits and Irreducible Boundaries

The system enforces correctness within its defined model.

This chapter defines what lies outside that model — not as missing
features, but as irreducible boundaries that cannot be resolved without
changing the fundamental nature of the system.

### 52.1 — Definition of Boundary

A boundary is a property that cannot be enforced by the system without
introducing hidden state, temporal dependency, external trust, or
semantic interpretation.

Boundaries are not limitations of implementation.
They are consequences of the system's core constraints.

A more capable implementation does not remove them.
A better test suite does not remove them.
More layers do not remove them.

They are structural.

### 52.2 — Statelessness Across Cycles

The execution model is stateless across cycles (Ch. 51.2).

It does not retain history, identity continuity, or prior decisions.

Any property requiring memory across cycles cannot be enforced:

- replay detection
- duplicate suppression
- long-term behavioral consistency
- causal ordering across submissions

These require state that the model explicitly excludes.

### 52.3 — No Intent Verification

The system evaluates admissibility. It does not evaluate intent.

An action may pass all enforcement layers and still be undesirable:

    passes_all_layers(a) ⇏ correct_intent(a)

Intent correctness is not expressible within the model. It would require
semantic interpretation of what an action means in context — which
requires knowledge the execution model does not have and must not
acquire (Ch. 36.8).

Geometry defines what transitions are permitted. It does not define
what transitions are wise.

### 52.4 — No External Truth

The system operates on provided state. It does not verify that the
provided state corresponds to external reality.

If state is incorrect, execution remains correct relative to that
state. No layer detects mismatch between internal state and the world:

    state ≠ reality ⇏ execution_error

The observation layer (Ch. 28) detects divergence between expected
and observed state — but only when an observer is provided and only
when the observed state is explicitly compared. The system does not
autonomously verify external truth.

### 52.5 — Simulation Non-Equivalence

From Ch. 50.1:

    f(s, a) ≠ F(s, a)  in general

Perfect alignment requires f to be derived from F, not defined
independently. Any caller-provided apply function that duplicates
execution logic introduces divergence as a structural inevitability.

This is not a bug in the advisory pipeline. It is a consequence of
dual semantics: evaluation and enforcement are separate by design,
and separation means they can disagree.

### 52.6 — No Global Ordering

The execution model does not enforce ordering across cycles (Ch. 51.5).

Without external coordination:

    execute(a₁) then execute(a₂) ≠ execute(a₂) then execute(a₁)

in general. Causality, serialization, and sequencing constraints belong
to the control plane. The kernel evaluates each cycle independently
against current state.

### 52.7 — No Replay Prevention

Replay is permitted by the model (Ch. 51.3):

    execute(s, a) → s'
    execute(s, a) again → s'

The system guarantees no hidden accumulation of effects. It does not
guarantee single execution or uniqueness of submission. Replay detection
requires persistent identity tracking across cycles — which requires
the memory the model explicitly excludes.

### 52.8 — No Temporal Guarantees

The system has no internal clock (Ch. 37.8).

All transitions are evaluated as pure functions over state. There are
no deadlines, no time-based constraints, no scheduling guarantees,
and no notion of elapsed time between cycles.

Time-dependent constraints can be expressed only by encoding time as
state and providing it as part of the action payload — which transfers
responsibility for temporal correctness to the caller.

### 52.9 — No Cross-System Consistency

When the execution kernel commits an action that has external effects
(e.g. an HTTP call via HttpBackend), internal state is atomic and
restored on failure. External state is not:

    internal_state → restored on failure
    external_state → unknown

Consistency across system boundaries is not guaranteed (Ch. 39.13,
EXECUTION_MODEL_LIMITS.md §5). The observation layer (Ch. 28) can
detect post-commit divergence, but cannot undo external effects.

### 52.10 — No Economic or Strategic Reasoning

The system does not evaluate cost, incentives, or adversarial strategy
over time.

An action that is valid and admissible may still be economically
harmful, strategically exploitable, or collectively dangerous when
composed with other valid actions (Ch. 36).

These properties require models outside the execution boundary. The
system enforces what is declared. It does not reason about what was
not declared.

### 52.11 — Boundary Composition

Boundaries do not combine into guarantees.

    statelessness + determinism ≠ replay prevention
    correctness + alignment    ≠ intent correctness
    atomicity + isolation      ≠ global consistency
    enforcement + geometry     ≠ correct geometry

Each boundary remains independent. No composition of system properties
removes a boundary. A system that is correct in all other respects
remains bounded by each limit independently.

### 52.12 — Non-Removability

These boundaries cannot be removed without violating core properties
of the model:

    Replay prevention   → requires persistent identity tracking
    Intent verification → requires semantic interpretation layer
    External truth      → requires trusted observation oracle
    Global ordering     → requires temporal coordination layer
    Alignment gap       → requires unified execution/simulation (Ch. 50.7)

Each change introduces new trust assumptions, new failure modes, and
loss of the isolation properties the model depends on.

Removing a boundary does not make the system stronger.
It makes it different — with different guarantees and different risks.

### 52.13 — Relationship to System Guarantees

The system guarantees, within these boundaries:

- enforcement of invariants I1–I7 under all compositions (Ch. 49.8)
- correctness and determinism of execution (Ch. 39)
- separation of evaluation and enforcement (Ch. 45–47)
- defined semantic alignment model (Ch. 50)
- explicit temporal scope (Ch. 51)

These guarantees hold within the boundaries defined in this chapter.
They do not extend beyond them.

### 52.14 — Closure

The system is not incomplete.

It is bounded.

It does not attempt to solve intent, external truth, time, or strategy.

It enforces admissibility, correctness of state transitions, and
isolation of failure — within a single cycle, against declared
constraints, under the authority that is presented.

What lies outside is not a gap to be filled.

It is a boundary to be respected.

Safety is not achieved by eliminating limits.

It is achieved by making them explicit — and ensuring they are never
crossed implicitly.

---

# Chapter 53 — Reconciliation

*When Execution Completes but Reality Remains Uncertain*

---

### 53.1 — The Limit of Correct Execution

All prior chapters establish a system that can execute correctly.

Given a valid domain (*D*), admissible actions (*A*), and verified authority (*Auth*), the system guarantees that execution is deterministic, atomic, and constrained. If execution fails, state is preserved. If execution succeeds, state is transformed exactly as defined.

This closes the execution problem.

But it does not close the system.

Because execution does not guarantee that reality reflects the result.

---

### 53.2 — The Missing Question

Until now, the system answers:

*Can this transition be executed?*

Reconciliation introduces a different question:

*Did the world actually become what was executed?*

This question cannot be answered by the execution layer. Execution produces an expected state. Reality produces an observed state. The system must compare the two — and decide what to do with the difference.

---

### 53.3 — Divergence Is Not an Error

The comparison yields three possible outcomes:

`ALIGNED` — observed matches expected.
`DIVERGED` — observed contradicts expected.
`UNKNOWN` — observed is incomplete or unavailable.

These are not execution results. They are epistemic states. They describe what the system knows about reality after execution has occurred.

The critical distinction:

Failure belongs to execution. Divergence belongs to reality.

A system can execute without error and still diverge. The two conditions are independent.

---

### 53.4 — Divergence as a First-Class Signal

Divergence is not a side condition. It is not logging. It is not monitoring.

It is a control signal.

No state-mutating decision in cycle *n+1* is valid without first establishing the divergence status of cycle *n*. This is not a best-effort check. It is a structural dependency. The execution result alone is insufficient. The system must carry:

*(expected state, observed state) → divergence status*

This becomes a structural part of every cycle.

---

### 53.5 — The Epistemic Boundary

The system cannot assume complete visibility of reality.

Therefore `UNKNOWN` is a valid and necessary state. It does not mean failure. It does not imply divergence. It means the system does not have sufficient information to determine alignment.

This constraint is not optional. Any system that collapses `UNKNOWN` into either `ALIGNED` or `DIVERGED` introduces false certainty — which is more dangerous than acknowledged ignorance.

---

### 53.6 — From Observation to Decision

Reconciliation introduces a new layer between observation and execution:

*(DivergenceStatus × Context) → Outcome*

Context includes the epistemic state of the system (blocked or clear), the retry count for the current cycle, applicable policy constraints, and the current execution mode.

Outcome is one of five values:

`CONTINUE` — proceed to the next cycle.
`RETRY` — attempt execution again under defined conditions.
`ESCALATE` — delegate the decision to an external authority.
`SKIP` — record and move forward without acting.
`HALT` — stop execution.

Outcome is binding for the next cycle. It is not a recommendation. It is a constraint on what execution may attempt.

This is not execution logic. It is decision logic under uncertainty. The two must remain structurally separate.

---

### 53.7 — Default Invariant: Fail-Closed

In the absence of an explicit policy, the system defaults to:

`DIVERGED` → `HALT`
`UNKNOWN` → `SKIP`
`ALIGNED` → `CONTINUE`

This is not arbitrary. It encodes a principle: uncertainty must not produce irreversible state transitions. A system that continues acting under unresolved divergence is not robust — it is reckless. The conservative default forces the decision surface outward, to human judgment or explicit policy, rather than absorbing it silently into automation.

---

### 53.8 — Epistemic Veto

When `DIVERGED` is detected, the system enters a blocked state.

While blocked, no further execution is permitted.

This is not a safety feature layered on top of the architecture. It is a logical necessity embedded in it. If the system cannot trust its own state, it cannot justify further transitions. The veto is not a pause — it is a structural refusal.

The blocked state is not advisory. It is enforced at the execution boundary.

Policy cannot override the epistemic veto implicitly. Override requires explicit design and explicit justification. A system that silently bypasses this constraint has not solved the problem. It has concealed it.

The veto is cleared only through deliberate external action. The system does not define when that action is appropriate. It only enforces that, without it, execution does not resume.

---

### 53.9 — The Reconciliation Cycle

A full system cycle now consists of six stages:

1. Propose actions (simulation against current state)
2. Execute (atomic commit or full rollback)
3. Observe reality (acquire the observed state)
4. Assess divergence (compare expected and observed)
5. Apply reconciliation policy (determine the outcome)
6. Record the cycle (produce a CycleRecord)

The CycleRecord is immutable and timestamped. It contains the actions proposed, the expected state after execution, the observed state, the divergence status, the policy outcome, and the full context at the moment of decision.

CycleRecord is not an audit artifact. It is part of the system state boundary. It participates in the correctness of the system, not merely in its observability.

The system is now traceable not only in what it executed, but in what it decided — and why.

---

### 53.10 — Separation of Concerns

Reconciliation does not modify execution. Execution MUST NOT depend on reconciliation outcomes.

Execution remains pure, deterministic, and authority-bound. It answers one question: was this transition valid?

Reconciliation is interpretive, contextual, and policy-driven. It answers a different question: can the result be trusted?

This separation is not a convenience. It is a structural requirement. A system that conflates execution correctness with epistemic certainty has no mechanism to detect the gap between them — which is precisely where silent failure lives.

---

### 53.11 — The System After Reconciliation

Before reconciliation, the system is an execution engine. It transforms state under constraint.

After reconciliation, the system controls not only execution but the continuity of execution. It determines not only what can be done, but whether it is legitimate to continue doing it.

The system now knows what it intended, what it executed, what actually happened, whether it can trust the result, and what to do next.

---

### 53.12 — The Structural Shift

This chapter changes the nature of the system.

It is no longer only a machine that transforms state correctly. It becomes a system that reasons about the relationship between its own execution and external reality.

That reasoning is bounded and formal. It does not introduce interpretation into execution. It introduces a separate, structured layer whose sole purpose is to evaluate alignment and constrain what follows.

---

### 53.13 — What Remains Open

Reconciliation does not resolve how to recover from divergence once `HALT` has been reached. It does not define how to re-plan when the cause of divergence is unknown. It does not address how multiple systems with conflicting observations reconcile their respective views of reality. It does not specify how epistemic state should persist or degrade across cycles.

These are not extensions of reconciliation. They are new problems, requiring new layers.

One limit that reconciliation itself does not solve: the reconciliation policy can be incorrectly configured. A policy that maps `DIVERGED` to `CONTINUE` does not produce a failure in the execution layer — it produces a failure of judgment. The system enforces what is declared. It does not validate whether what was declared is sound.

Who reconciles the reconciler remains an open question.

---

### 53.14 — Closing

Execution answers: *what can be done.*

Reconciliation answers: *what can be trusted.*

A system without execution cannot act. A system without reconciliation cannot know whether its actions produced the reality it intended — or something else entirely.

The gap between those two is not an edge case.

It is where systems fail silently, accumulate invisible divergence, and eventually produce outcomes that no single execution step caused, but that the absence of epistemic awareness made possible.

---

# Chapter 54 — Policy Constraints

*What the system must never do.*

---

### 54.1 — The Remaining Risk

Chapter 53 closes a problem that prior chapters did not ask.

Execution answers: was this transition valid?

Reconciliation answers: can the result be trusted?

But a third question remains unanswered.

Given what the system knows about reality — what is it allowed to do next?

This is not an execution question. It is not a reconciliation question.

It is a constraint on the reactions that uncertainty permits.

Until this constraint exists, the system may detect divergence correctly, assess epistemic state correctly, and still behave dangerously. The failure is no longer in execution. It is in decision.

A system that knows it cannot trust its state, and continues anyway, has not failed to detect a problem. It has failed to respond to one.

---

### 54.2 — Policy as a New Failure Surface

Reconciliation introduces a policy function:

```
(DivergenceStatus × Context) → Outcome
```

Chapter 53 defines five possible outcomes: CONTINUE, RETRY, ESCALATE, SKIP, HALT.

It also defines a default mapping — the fail-closed invariant that governs behavior in the absence of explicit configuration. But it does not define which mappings are structurally inadmissible.

The following policy is syntactically valid:

```
DIVERGED → CONTINUE
```

It does not violate execution. It does not violate reconciliation. The system detected divergence correctly. The policy simply ignores the detection.

This is not an execution failure. It is a policy failure. And the execution model, as defined through Chapter 53, has no mechanism to prevent it.

Policy is the remaining failure surface.

---

### 54.3 — The Constraint Layer

Policy constraints are not policy.

They are a layer above policy that enforces what any policy must respect — independent of what the policy is configured to do, independent of the current state, and independent of the reconciliation outcome that triggered it.

Constraints do not define what the system should do. They define what the system is not permitted to do.

The distinction is structural. Policy expresses judgment under uncertainty. Constraints express the limits within which all judgment must operate.

A policy that violates a constraint is not wrong in its intent. It is structurally inadmissible. The system rejects it before applying it.

---

### 54.4 — Constraint I1: Divergence Must Not Continue

When the system has confirmed evidence of divergence:

```
DIVERGED → {HALT, ESCALATE}
```

The following outcomes are forbidden:

```
DIVERGED → CONTINUE
DIVERGED → SKIP
```

Continuing under known divergence is not optimism. It is state mutation applied to a foundation the system has declared untrusted. The execution layer commits real transitions. A policy that permits this under DIVERGED converts epistemic uncertainty into irreversible effects.

CONTINUE under DIVERGED violates the boundary that reconciliation exists to enforce.

SKIP under DIVERGED is subtler but structurally equivalent. It does not act, but it moves forward. The next cycle begins without resolving the detected contradiction. The divergence is not acknowledged — it is passed over. Over time, this produces the silent accumulation that Chapter 53 was introduced to prevent.

Both are inadmissible.

---

### 54.5 — Constraint I2: Uncertainty Must Propagate Outward

When the system lacks sufficient information to establish alignment:

```
UNKNOWN → {HALT, SKIP, ESCALATE}
```

The following outcome is forbidden:

```
UNKNOWN → CONTINUE
```

Uncertainty is not a permissive state. It is an epistemic state. The system does not know whether what it executed matches reality. Acting as if it does is not recovery — it is assumption dressed as continuation.

The correct response to UNKNOWN is to move the decision outward. Either halt and wait, skip and record, or escalate to a layer with more information. In none of these cases does the system proceed as if alignment were confirmed.

UNKNOWN must not be absorbed into execution. It must be surfaced.

---

### 54.6 — Constraint I3: Permissiveness Must Not Increase With Uncertainty

A valid policy satisfies a monotonicity condition: as epistemic certainty decreases, the set of allowed outcomes must not expand.

A policy of the form:

```
ALIGNED → HALT
UNKNOWN → CONTINUE
```

is not merely unusual. It is structurally inverted. It responds more cautiously to confirmed alignment than to unresolved uncertainty. This policy cannot be the result of careful judgment — it is the result of misconfiguration, and the system must reject it.

This constraint does not dictate how conservative the policy must be. It only requires that conservatism does not decrease as certainty decreases.

---

### 54.7 — Static Validation

Policy constraints are evaluated before the policy is used.

Validation is structural: it does not execute transitions, observe state, or simulate runtime behavior. It inspects the policy's mapping across known inputs and verifies that no mapping violates I1, I2, or I3.

A policy that fails validation is not applied. The system raises a policy error at construction time, not at execution time.

This is not a runtime guard. It is a pre-admission check. A policy that cannot be admitted cannot cause runtime failures by design — because it never reaches the point where it would be consulted.

The preferred implementation, realized in `policy_constraints.py`, runs this check when a `_ReconciliationPolicy` is constructed. An invalid policy does not exist operationally. It is rejected at the boundary.

---

### 54.8 — Dynamic Enforcement

Static validation eliminates known-bad policies before use. Dynamic enforcement handles what static analysis cannot: policies that are structurally valid in general but produce inadmissible outcomes in specific runtime contexts.

At each cycle, after the policy returns an outcome, the constraint layer verifies:

```
outcome = policy(status, context)
assert constraints(outcome, status)
```

If the outcome violates a constraint:

- execution is halted
- a policy error is raised
- no state is mutated

The system does not attempt to correct the outcome. It does not fall back to a default. It refuses to apply what cannot be applied safely, and stops.

This enforcement is realized in `PolicyConstraints.enforce()` in the production system. The function takes the verdict, the context, and the outcome, and raises immediately if any structural invariant is violated. There is no fallback. There is no silent substitution.

---

### 54.9 — Ownership of Policy Errors

Policy errors are not execution errors. They are not geometry errors. They are not authority errors.

They belong to the constraint layer — to the module that defines and enforces what policies are structurally permitted to do.

This ownership is not cosmetic. The error taxonomy of the system (realized in `execution/errors.py`) assigns `PolicyError` to the module that raises it, not to the module where the policy is defined. The constraint layer raises policy errors because it is the enforcement point. The policy definition layer defines the mapping. The constraint layer verifies it.

This separation maintains the invariant established in Chapter 39.12: error type identifies failure origin. A `PolicyError` means the constraint layer rejected an outcome or a policy configuration. It does not mean execution failed. It does not mean reconciliation failed. It means the system refused to act on what it was told to do.

---

### 54.10 — What Constraints Do Not Guarantee

Policy constraints enforce structural safety under uncertainty.

They do not guarantee:

- that the policy is wise
- that HALT is the right response in a given context
- that ESCALATE will reach a system capable of resolving the divergence
- that SKIP is safe in the current business domain
- that the constraint configuration is complete

The constraints define what the system must never do. They leave open the full space of what it may do within those limits.

Correctness of judgment remains outside the model. This is not a gap — it is a boundary (Ch. 52.3). A system that enforces I1, I2, and I3 under DIVERGED and UNKNOWN is not guaranteed to recover correctly. It is guaranteed not to make things worse by acting blindly.

That is not nothing. It is the difference between a system that fails safely and one that fails silently.

---

### 54.11 — Separation of Concerns

This chapter introduces a fourth distinct concern, below execution and reconciliation and above raw policy:

Execution enforces geometry, authority, and atomicity.
Reconciliation determines epistemic state.
Policy determines the next action under that state.
Policy constraints enforce what reactions to uncertainty are structurally admissible.

Each layer is independent. No layer compensates for the failure of another. A correct execution does not fix a bad policy. A correct reconciliation does not fix an unconstrained policy reaction. The constraint layer does not fix incorrect policies — it refuses them.

The layering is strict. This is what makes it tractable. Each layer has a defined responsibility and cannot acquire the responsibility of another.

---

### 54.12 — Closure

Chapter 53 closed with an open question:

*Who reconciles the reconciler?*

The answer is not another layer of observation. It is not a meta-reconciliation function. It is not a smarter policy.

It is constraint.

The reconciler is not trusted to produce safe outcomes. It is constrained to produce only outcomes that the system has agreed to accept under conditions of uncertainty.

Reconciliation answers: what can be trusted?

Policy answers: what should happen next?

Policy constraints answer: what must never happen?

The system does not guarantee correct decisions.

It guarantees that incorrect decisions cannot violate structural safety.

The reconciler is not reconciled.

It is bounded.

---

## Chapter 55 — Persistence
*What remains after closure.*

---

### 55.1 — The Unresolved Condition

Chapter 54 bounds the admissible reactions to uncertainty.

Execution is bounded. Reconciliation is bounded. Policy is bounded. Constraint is bounded.

The system is not.

The model defines what is allowed within a cycle. It does not define what persists across cycles.

---

### 55.2 — Closure Is Local

Closure applies to a cycle.

A cycle ends. The system continues.

State persists. The next cycle begins from it.

Closure does not prevent continuation.

---

### 55.3 — No Final State

The model defines no terminal state.

HALT is not termination. It is refusal under current conditions.

The system remains capable of further execution.

A halted system is not a completed system.

---

### 55.4 — Correctness Does Not Transfer

A correct transition produces a state.

The next transition starts from it.

Correctness does not transfer.

Each step is evaluated independently. There is no invariant of accumulated correctness.

---

### 55.5 — Guarantees Are Per Cycle

All guarantees in Chapters 27–54 hold within a cycle.

Atomicity. Authority. Reconciliation. Constraint.

They hold at the boundary.

They do not extend beyond it.

The next cycle is a new evaluation.

---

### 55.6 — State Persists. Guarantees Do Not.

State carries forward.

Guarantees do not.

A state produced under valid execution may become misaligned under new context. A state accepted under reconciliation may later diverge.

Persistence preserves state.

It does not preserve alignment.

---

### 55.7 — Risk Is Reintroduced

Each cycle begins under uncertainty.

External conditions change. Internal state accumulates.

Constraints prevent invalid reactions. They do not remove the conditions that produce them.

Risk is not eliminated.

It is re-evaluated.

---

### 55.8 — No Global Reconciliation

Reconciliation is local.

It compares expected and observed state at a boundary.

There is no reconciliation of the system as a whole. No point exists at which the system can assert global alignment.

Such a statement is not defined by the model.

---

### 55.9 — The Model Does Not Run

The model defines constraints, invariants, allowed transitions.

The system executes state mutation, time progression, interaction with external processes.

The model is static. Execution is not.

Correctness in the model does not imply correctness over time.

---

### 55.10 — Execution Exceeds Description

The model is finite.

Execution is not fully captured by the model's scope.

New states arise. New contexts emerge. Prior assumptions become insufficient without becoming false.

The model constrains what it describes.

It does not describe all that occurs.

---

### 55.11 — Time as Adversary

Failure is not introduced only by invalid transitions.

It is introduced by continuation.

Assumptions decay. State accumulates. External systems change.

Time does not violate constraints.

It erodes the conditions under which they were sufficient.

---

### 55.12 — What Remains

The model closes.

The system does not.

Each step is bounded. The sequence is not.

Correctness is enforced locally. It is not preserved globally.

What is correct now is not preserved by continuation.

---

### 55.13 — Derived Principles

The preceding chapters establish structural necessity.

The following are not assumptions. They are consequences.

**Persistence defines the system.**
If what persists is undefined, the system is undefined.

**Execution is admission.**
A system does not do what it can. It does what it allows.

**Control requires impossibility.**
If an action can occur, it is permitted by the system.

**A boundary that can be bypassed is not a boundary.**
It is a suggestion.

**Local validity does not compose.**
A sequence of valid steps is not a valid sequence.

**Safety is conjunctive.**
A single violation is sufficient.

**Verification is structural.**
A system is verified when violation is impossible, not when it is detected.

**Authority acts through veto.**
Execution passes through constraint, not through intent.

**Observation is governance.**
Unobserved execution is ungoverned execution.

**Under uncertainty, reduce action.**
Uncertainty does not permit execution. It constrains it.

**Persistence creates commitment.**
State accumulation constrains future execution.

**Direction constrains execution.**
Direction is not memory. It is restriction.

---

### 55.14 — Closure

The model closes.

The system does not.

Each step is bounded. The sequence is not.

Correctness is enforced locally. It is not preserved globally.

What is correct now is not preserved by continuation.

---

## Chapter 56 — Immutable Enforcement Constraints in Persistent Execution Systems

## 56.1 — Motivation

The execution model defined in Chapters 24–55 establishes a layered architecture:
geometry enforcement, authority verification, policy resolution, and epistemic control.
Each layer is configurable within declared bounds.

However, certain classes of constraint cannot be treated as configurable policy.
They are not recommendations. They are not runtime preferences that operators may
override for operational convenience. They are **admissibility conditions over
execution itself** — conditions whose violation renders continuation structurally
inadmissible under the model.

This chapter defines those constraints, their formal basis, and their implementation
as non-overridable kernel invariants.

---

## 56.2 — Admissibility vs Policy

The execution model distinguishes two classes of constraint:

**Policy constraints** govern how the system responds to observed execution states.
They are declared, configurable, and subject to override within defined bounds.
A policy may specify that divergence triggers escalation rather than halt,
or that insufficient data permits a skip rather than a stop.

**Admissibility constraints** govern whether execution may continue at all.
They are not declared by operators. They are derived from the structural
requirements of the execution model itself. No policy override can satisfy
an admissibility constraint that the model has determined to be violated.

Formally: let `V` be the current verdict (confirmed, diverged, unknown,
insufficient\_data) and `O` be the proposed outcome. An admissibility constraint
`I` is a predicate `I(V, C, O) → {admissible, inadmissible}` where `C` is the
execution context. If `I(V, C, O) = inadmissible`, no policy can produce `O`
from `V` under `C`.

---

## 56.3 — Divergence and Halt Semantics

Consider a persistent execution system operating under a declared geometry `G`.

If observed execution diverges from the admissible transition space defined by `G`,
continuation may no longer be considered valid execution under the model.

Two behaviors are structurally possible:

1. Continue execution under unresolved divergence.
2. Halt execution and preserve state integrity.

Under the fail-closed model, unresolved divergence contracts the admissible execution space to HALT or ESCALATE outcomes. The second behavior preserves admissibility.
This produces the fundamental enforcement rule:

```
unresolved divergence  ⟹  HALT
```

rather than:

```
unresolved divergence  ⟹  best-effort continuation
```

This is not a policy preference. It is a structural consequence of the model:
a system that continues under confirmed divergence is no longer executing within
its declared geometry. It has exited the admissible execution space.

---

## 56.4 — The Three Kernel Invariants

The following invariants are non-overridable. They are enforced structurally
at the `PolicyConstraints` layer (Ch. 55), both at policy construction time
(static validation) and at runtime (dynamic enforcement).

### I1 — No Continuation Under Confirmed Divergence

```
V = DIVERGED  ⟹  O ∈ {HALT, ESCALATE}
```

If the observation layer (Ch. 28) has confirmed that the system state has diverged
from expected state, execution may not continue. The only admissible outcomes are
halt or escalation to external authority.

**Rationale:** A diverged system is one whose internal state no longer reflects a
valid execution history under the declared geometry. Continuation from such a state
would produce transitions over a non-admissible execution state. The model does not permit this.

**Implementation:** `PolicyConstraints._enforce_i1()` and `_check_i1()` at construction.
Any policy resolving `DIVERGED → CONTINUE` or `DIVERGED → SKIP` raises `PolicyError`
before the first execution cycle.

### I2 — Uncertainty Does Not Expand Authority Under Strict Mode

```
V = UNKNOWN  ∧  mode = strict  ∧  retry_count > 0  ⟹  O ≠ CONTINUE
```

Under strict execution mode with active retries, an unknown verdict indicates that
the system has already encountered uncertainty and is attempting recovery.
Permitting `CONTINUE` under these conditions would allow execution to proceed
on an unresolved foundation, expanding authority under uncertainty.

**Rationale:** Uncertainty contracts the admissible execution space. It does not
expand it. This is the **authority contraction principle**: as uncertainty
increases, the set of admissible outcomes shrinks. A system that cannot establish admissibility must reduce, not increase,
the set of permitted transitions.

**Implementation:** `PolicyConstraints._enforce_i2()` — targeted at the `unknown`
verdict under strict mode with retry, the case not already covered by I1 or I3.

### I3 — No Continuation Under Insufficient Observation Data

```
V = INSUFFICIENT_DATA  ⟹  O ≠ CONTINUE
```

If the observation layer cannot establish whether the current state is valid —
because the data required for reconciliation is unavailable — execution may not
continue. The system must halt or skip until sufficient observation data is available.

**Rationale:** Continuation without observation data is execution without a known
foundation. The model requires that execution state be reconcilable against observed
state before continuation is permitted.

**Implementation:** `PolicyConstraints._enforce_i3()` and `_check_i3()` at construction.

---

## 56.5 — Fail-Closed Enforcement

Under fail-closed semantics, the relationship between uncertainty and authority
is inverted relative to best-effort systems:

| Condition | Best-effort system | Fail-closed system |
|---|---|---|
| Confirmed state | Continue | Continue |
| Unknown state | Continue with caution | Halt or skip |
| Diverged state | Attempt recovery | Halt or escalate |
| Insufficient data | Continue if possible | Halt or skip |

The fail-closed model produces a monotonic relationship between uncertainty and
admissibility: as uncertainty increases, the set of admissible outcomes shrinks.
This is not a conservative design choice — it is the structural requirement of
a system whose execution space is formally bounded.

Formally: let `U(V)` be the uncertainty level of verdict `V`, and `A(V)` be the
set of admissible outcomes under `V`. The fail-closed invariant requires:

```
U(V₁) ≥ U(V₂)  ⟹  A(V₁) ⊆ A(V₂)
```

Uncertainty monotonically contracts the admissible execution space.

---

## 56.6 — Structural Enforcement, Not Semantic Judgment

The kernel invariants are enforced structurally. The system does not:

- infer intent correctness,
- evaluate ethical validity,
- assess semantic meaning of transitions,
- determine whether a goal is appropriate.

It determines only whether continuation remains admissible under the declared
execution model. This is a binary determination: admissible or inadmissible.

This separation is intentional and non-negotiable. The admissibility layer
(geometry, authority, kernel invariants) governs the structure of execution.
The semantic layer (goals, policies, alignment) governs the content of execution.
Neither layer may override the other's domain.

---

## 56.7 — Scope and Non-Guarantees

The kernel invariants defined in this chapter do not solve:

- **Ethical alignment** — the invariants enforce structural admissibility,
  not correctness of declared geometry or policy.
- **Semantic correctness** — a system whose geometry permits incorrect sequences
  will enforce those sequences correctly.
- **Value specification** — the model does not evaluate whether declared
  constraints reflect appropriate values.
- **Intent verification** — the system does not reason about the intentions
  of operators, signers, or external systems.

The contribution of this chapter is narrower and more precise: it defines the
structural conditions under which persistent execution is prevented from continuing
under unresolved divergence or invalid state evolution. These conditions are
necessary, not sufficient, for correct system behavior.

---

## 56.8 — Implementation Reference

### Static validation (construction-time)

```python
PolicyConstraints.validate(policy)
## Called in CycleRecorder.__init__()
## Raises PolicyError if I1 or I3 are violated before first use
```

### Dynamic enforcement (runtime)

```python
PolicyConstraints.enforce(verdict, context, outcome)
## Called in CycleRecorder.record() after policy.resolve()
## Raises PolicyError if I1, I2, or I3 are violated at runtime
```

### Test witness

Test suite `test_824_halt_invariant.py` (19 tests) provides constructive
verification that:

- No policy construction can produce `DIVERGED → CONTINUE` (I1, static)
- No runtime invocation can produce `DIVERGED → CONTINUE` (I1, dynamic)
- No policy construction can produce `INSUFFICIENT_DATA → CONTINUE` (I3, static)
- No runtime invocation under strict+retry can produce `UNKNOWN → CONTINUE` (I2)
- `HALT` is always admissible under any verdict
- Uncertainty contracts, never expands, the admissible execution space

---

## 56.9 — Relation to Prior Chapters

| Chapter | Component | Relation to Ch. 56 |
|---|---|---|
| Ch. 24 | Execution model | Defines the formal system over which invariants apply |
| Ch. 27 | Execution kernel | Provides the enforcement infrastructure |
| Ch. 28 | Observation layer | Produces the verdict (V) that triggers invariant checks |
| Ch. 53 | Reconciliation policy | Governs configurable behavior; subject to I1–I3 |
| Ch. 54 | Diagnostic layer | Records invariant violations without influencing them |
| Ch. 55 | PolicyConstraints | Implements I1, I2, I3 — referenced directly by this chapter |

The kernel invariants of this chapter represent the non-negotiable boundary
between the policy layer (configurable) and the execution model (structural).
No component above Ch. 55 in the dependency graph may override them.

---

*This chapter documents the immutable enforcement constraints of the Regen Engine
execution kernel. These constraints are enforced by construction and at runtime.
They cannot be disabled, overridden, or configured away.*

---

<img width="2492" height="1222" alt="image" src="https://github.com/user-attachments/assets/355aa9de-b6e5-459e-8558-7d4986a58b1a" />


---

## Chapter 57 — External Adversarial Attack Taxonomy

### 57.0 — Introduction

Chapters 24–56 establish the execution model, its structural invariants, and the kernel-level enforcement constraints (I1–I3). Those chapters address the question: *what must hold for execution to be admissible?*

Chapter 57 addresses a different question: *in how many structurally distinct ways can admissibility be destroyed from outside the enforcement boundary?*

This is not a security chapter in the conventional sense. It does not classify attackers, exploits, or threat actors. It classifies **failure modes of the admissibility basis** — the conditions under which the epistemic, temporal, structural, and authority foundations required for admissible continuation can be degraded or destroyed.

The central insight of this chapter is that inadmissibility is not a single phenomenon. It is a family of structurally distinct contractions of the admissible execution space, each arising from a different failure of the conditions that make continuation legitimate.

**The fundamental principle:**

> *Admissibility is not a permanent property of a past verdict. It is a relation — evaluated continuously against the current epistemic, temporal, structural, and authority context.*

Or equivalently:

> *Admissibility is continuously re-earned, never permanently inherited.*

All eight attack classes in this chapter demonstrate this principle from a different angle.

---

### 57.1 — Stale Observation Replay

**What is attacked:** The freshness of the observation verdict.

**Attack:** An adversary captures a valid CONFIRMED verdict and replays it into a context where the epistemic basis has changed — geometry mutation, state drift, or authority change.

**Structural failure:** The verdict was valid in context G₁ but is replayed in context G₂. The epistemic basis from which the verdict was derived no longer exists.

**Formal property violated:**

> *A verdict is admissible only relative to the execution context from which it was derived.*

**Enforcement:** `DivergenceRecord.is_stale(current_geometry_version)` returns `True` when the originating geometry version differs from the current context. Stale verdicts cannot authorize continuation.

**Central claim:**

> *Local validity ≠ current admissibility.*

**What the tests verify:** That a CONFIRMED verdict from geometry G₁ is stale in G₂, that staleness detection is symmetric and context-relative, and that stale verdicts cannot produce CONTINUE.

---

### 57.2 — Observation Starvation

**What is attacked:** The presence of observation.

**Attack:** The adversary suppresses, delays, or blocks the observation channel entirely. No fresh verdict can be produced. The system is pressured to continue without observation.

**Structural failure:** Without observation, admissibility cannot be established. Continuation without an admissibility basis is structurally inadmissible.

**Formal property violated (I3):**

```
V = INSUFFICIENT_DATA ⟹ O ≠ CONTINUE
```

**Enforcement:** `reconcile(observed_state=None)` produces `INSUFFICIENT_DATA`. `PolicyConstraints.enforce()` raises `PolicyError` (I3) for any `CONTINUE` outcome.

**Key distinction from 57.1:**

| 57.1 | 57.2 |
|---|---|
| Verdict exists but is stale | Verdict cannot be produced |
| Invalid observation reused | Valid observation unavailable |
| Context mismatch | Epistemic absence |

**Central claim:**

> *Absence of evidence is not evidence of admissibility. Observation starvation contracts CONTINUE out of the admissible outcome set.*

**What the tests verify:** That `None` observation produces `INSUFFICIENT_DATA`, that I3 holds regardless of retry count or execution mode, and that partial observation (non-None) produces DIVERGED, not INSUFFICIENT_DATA.

---

### 57.3 — Delayed Divergence Injection

**What is attacked:** The temporal validity of the admissibility basis.

**Attack:** The adversary allows a valid execution to complete, then injects divergence *after* validation but *before* or *during* observation. The validation was legitimate; the divergence is introduced in the window between commit and reconciliation.

**Timeline:**
```
T1: execution validates and commits
T2: external mutation injected
T3: observation captures mutated state → DIVERGED
```

**Structural failure:** A validated execution is not permanently admissible. External state evolution after commit invalidates the admissibility basis of the next cycle.

**Formal property violated:**

> *Admissibility is temporally bounded. Validation does not survive uncontrolled state evolution.*

**Key distinction from 57.1:**

| 57.1 | 57.3 |
|---|---|
| Verdict is stale | Verdict captured current state |
| Context changed before observation | State changed after commit |
| Stale basis | Temporally displaced invalidation |

**Enforcement:** `reconcile(expected, observed)` detects hash mismatch → DIVERGED. I1 blocks CONTINUE.

**Central claim:**

> *A validated execution that is followed by uncontrolled external mutation is no longer admissible. CONFIRMED at T1 does not imply admissibility at T2.*

**What the tests verify:** TOCTOU (pre-commit) vs delayed injection (post-commit) are structurally distinct. Admissibility is not inherited across cycles. Detection does not require knowing the injection source.

---

### 57.4 — Partial Epistemic Corruption

**What is attacked:** The integrity of the observation content.

**Attack:** The adversary does not suppress observation (57.2) or delay it (57.3). Instead, it corrupts the observation partially — some fields correct, some corrupted — hoping that partial correctness implies partial admissibility.

**Structural failure:** Admissibility is binary, not statistical. Any mismatch between expected and observed state produces DIVERGED. There is no "partially admissible" state.

**Key property:**

> *Admissibility is not democratic. A single corrupted field invalidates the entire reconciliation.*

**Forms of partial corruption:**
- Mixed state: some fields correct, others corrupted → DIVERGED
- Extra field injection → DIVERGED
- Field removal → DIVERGED
- Type confusion (int vs float, str vs int) → DIVERGED
- Veto suppression: attempting `clear()` without active veto → RuntimeError

**Epistemic veto hysteresis:**

Once DIVERGED activates the veto, subsequent CONFIRMED verdicts cannot suppress it. Resolution requires explicit `clear()` with operator acknowledgment. This prevents *confirmation flooding* — an attack where many CONFIRMED verdicts are sent to overwrite a legitimate veto.

**Central claim:**

> *Partial corruption of the epistemic basis must not produce artificial admissibility. Admissibility cannot be manufactured through selective observation corruption.*

**What the tests verify:** Majority-correct fields still produce DIVERGED. Veto requires explicit resolution. CONFIRMED updates cannot suppress veto. Detection is hash-based and source-agnostic.

---

### 57.5 — Authority Desync

**What is attacked:** The temporal validity of the authority context.

**Attack:** The adversary exploits a gap between authority validation (T1) and execution (T2). The authority context used to authorize an action at T1 is no longer the authority context active at T2.

**Forms of authority desync:**
- Key rotation: signing key changed between proposal and execution
- Signer removal: signer revoked from authority context
- Context substitution: different authority context presented at execution

**Structural failure:** Authority is a relation to the current execution context, not a permanent property of a past authorization grant.

**Formal property:**

> *Previous authorization does not imply current admissibility. Authority is context-bound.*

**Enforcement:** `AuthorityContext.get_key(signer_id)` raises `AuthorityError` for unknown signers. `AuthorityGate.verify()` uses constant-time HMAC comparison. `AuthorityError ≠ GeometryError` — distinct structural layers.

**Connection to Lemma 6.1:** Local authority (per-action authorization) does not compose to global authority. A signer authorized at step 1 is not automatically authorized at step 2 in a different context.

**Central claim:**

> *Authorization has temporal scope. A past authorization grant does not survive authority context change.*

**What the tests verify:** Signer removal invalidates all prior authorizations. Key rotation produces independent, non-interchangeable contexts. Authority failure is binary and action-content-independent.

---

### 57.6 — Rollback Desynchronization

**What is attacked:** The realization of the rollback guarantee.

**Attack:** The system reports `ROLLED_BACK` but the actual post-execution state does not match the pre-execution snapshot. Rollback is acknowledged but not realized.

**Forms of rollback desync:**
- Phantom rollback: `ROLLED_BACK` reported, state unchanged
- Partial rollback: some mutations survive (e.g., protected fields not restored)
- Snapshot drift: snapshot taken from already-mutated state (reference leak)
- External effect residue: external side effects survive internal rollback

**Structural failure:** `ROLLED_BACK` is a declared status, not a structural guarantee beyond the managed execution boundary. The guarantee is:

> *Internal state is restored to the pre-execution snapshot. External effects are outside this guarantee.*

This is explicitly documented in `EXECUTION_MODEL_LIMITS.md §2.3`.

**Snapshot contract:** `env.snapshot()` must return an isolated deep copy, not a reference. If it returns a reference, mutations after the snapshot will corrupt the snapshot itself — making rollback restore the mutated state.

**Detection:** Post-rollback state reconciled against pre-execution snapshot. Any mismatch → DIVERGED → I1 contracts CONTINUE.

**Central claim:**

> *ROLLED_BACK status does not guarantee pre-execution state identity without correct snapshot isolation. Rollback desync is detectable via structural reconciliation.*

**What the tests verify:** Reference-leaking snapshots drift. Deep copy snapshots are stable. Partial rollback residue is detected as DIVERGED. External effects survive internal rollback by design.

---

### 57.7 — Concurrent Verdict Races

**What is attacked:** The causal ordering of verdicts.

**Attack:** The adversary attempts to exploit temporal gaps in verdict processing — sending a CONFIRMED verdict to "race" against a DIVERGED verdict for the same execution cycle, hoping that CONFIRMED arrives last and suppresses the veto.

**Structural failure:** The Regen model is explicitly single-cycle-sequential. Verdict ordering is causal. The most conservative verdict governs.

**Fail-closed verdict resolution:**

```
DIVERGED wins over CONFIRMED in any order.
```

| Order | Result |
|---|---|
| CONFIRMED → DIVERGED | veto active |
| DIVERGED → CONFIRMED | veto active (persists) |

**Veto persistence:** Once DIVERGED activates the epistemic veto, subsequent CONFIRMED verdicts cannot suppress it. The veto is sticky by design — it models the property that a system that has experienced confirmed divergence cannot self-certify recovery.

**Immutability:** `DivergenceRecord` is a frozen dataclass. Individual verdicts cannot be mutated after creation.

**Concurrency property:** `reconcile()` is a pure function — no shared state, safe for concurrent calls. `EpistemicState` processes verdicts sequentially; concurrent reads are non-mutating.

**Central claim:**

> *DIVERGED always wins. The most conservative verdict governs. Fail-closed under race conditions.*

**What the tests verify:** DIVERGED persists regardless of verdict order. Confirmation flooding cannot suppress veto. Concurrent reconciliation calls are race-free. Verdict immutability prevents post-creation mutation.

---

### 57.8 — Geometry Poisoning

**What is attacked:** The root of trust of the admissibility model.

**Attack:** The adversary attempts to modify the declared execution geometry — removing invariants, adding undeclared action types, weakening preconditions, or substituting a less restrictive geometry — to expand the admissible execution space without the signing key.

This is the most fundamental attack in the taxonomy. In 57.1–57.7, the geometry was assumed to be correct. The attacks degraded the epistemic, temporal, authority, or recovery conditions *within* a valid geometry. In 57.8, the adversary targets the geometry itself — the structure that defines what execution is admissible at all.

**Formal connection:**

```
G_F(S) is derived from signed geometry.
A poisoned geometry collapses all downstream admissibility.
```

**Enforcement:**

The geometry is signed with HMAC-SHA256 using a constant-time comparison (`hmac.compare_digest`). Any modification to geometry content — geometry_id, invariants, actions, action preconditions — produces a canonical content mismatch and signature verification failure.

```
canonical_content(G) → HMAC-SHA256(key) → signature
Any content change → signature invalid → AuthorityError
```

**Properties of the HMAC-based signing:**
- Action order does not affect canonical content (actions sorted by name)
- Signature field is excluded from canonical content (no circular dependency)
- Signature is key-dependent: same content, different keys → different signatures
- Constant-time comparison prevents timing attacks

**The structural consequence:**

> *Without the signing key, the admissible execution space cannot be expanded. Any attempt to expand G_F(S) by modifying the geometry requires re-signing — which requires the key.*

**What the tests verify:** Tampering with geometry_id, invariants, or actions invalidates the signature. Signature stripping fails. Random signatures fail. Forgery with wrong key fails. `AuthorityGate.verify()` rejects all poisoned geometries. `AuthorityError ≠ GeometryError` — the distinction is preserved.

**Central claim:**

> *Geometry is the root of trust for the entire admissibility model. A poisoned geometry — one presented without a valid signature — is rejected before any execution can proceed. The admissible execution space cannot be expanded without the signing key.*

---

### 57.9 — Synthesis: The Admissibility Failure Taxonomy

Chapter 57 demonstrates that inadmissibility is not a single phenomenon. It is a family of structurally distinct failure modes, each destroying a different precondition for admissible continuation:

| Chapter | Failure mode | What is destroyed | Invariant enforced |
|---|---|---|---|
| 57.1 | Stale observation replay | Contextual validity | geometry_version binding |
| 57.2 | Observation starvation | Epistemic sufficiency | I3 |
| 57.3 | Delayed divergence injection | Temporal continuity | I1 + TOCTOU |
| 57.4 | Partial epistemic corruption | Structural integrity | Hash + veto hysteresis |
| 57.5 | Authority desync | Executive legitimacy | HMAC + AuthorityError |
| 57.6 | Rollback desynchronization | Recovery reality | Snapshot isolation |
| 57.7 | Concurrent verdict races | Causal ordering | Veto persistence |
| 57.8 | Geometry poisoning | Root of trust | Signature verification |

**The convergence property:** All eight failure modes contract the admissible outcome set toward the same result — CONTINUE becomes inadmissible. The mechanisms differ; the structural consequence is the same.

**The orthoghonality property:** Each failure mode targets a distinct structural layer. They are not variations of the same vulnerability — they are independent axes of admissibility degradation.

**The fail-closed property:** In all cases, uncertainty contracts the admissible execution space. It does not expand it. This is the authority contraction principle from Chapter 56:

```
U(V₁) ≥ U(V₂)  ⟹  A(V₁) ⊆ A(V₂)
```

Higher uncertainty → fewer admissible outcomes.

---

### 57.10 — What Chapter 57 Does Not Claim

This chapter does not:

- **Claim exhaustiveness.** The eight failure modes are not a complete catalog of all possible attacks. They are a structured taxonomy of the primary structural axes along which admissibility can degrade.
- **Address Byzantine adversaries.** The model assumes deterministic sequential transitions. Adversaries that control the execution environment itself are outside scope.
- **Address probabilistic attacks.** The model is deterministic. Probabilistic manipulation of verdict distributions is outside the formal model.
- **Replace security engineering.** These are structural properties of the execution model. Deployment security — key management, network security, access control — is the responsibility of the integrating system.

These limits are explicit and documented in `EXECUTION_MODEL_LIMITS.md`.

---

*Chapter 57 provides the adversarial witness for the enforcement model established in Chapters 24–56. The 228 adversarial tests across eight attack classes constitute a constructive demonstration that the invariants hold under systematic external pressure.*

*Reference implementation: Regen Engine (proprietary). Test suite: `tests/test_ch57_*.py`.* 

---

<img width="2952" height="1684" alt="image" src="https://github.com/user-attachments/assets/43d82527-ebd4-42ce-8fe1-507b209d1a01" />

---

## Chapter 58 — Execution Geometry Under Physical Irreversibility

There is a class of system in which the standard assumption fails.

Not partially. Not under edge conditions. Structurally.

The assumption is this: that recovery, while not guaranteed, remains economically feasible. Restarts are cheap. Patching is possible. Operators can intervene. Redundancy masks inconsistency.

Chapters 24–57 were written under this assumption.

Chapter 58 removes it.

---

### 58.0 — Motivation

The setting is not hypothetical.

Persistent autonomous systems deployed in physically constrained environments — autonomous industrial systems, remote robotic deployments, long-duration probes, orbital infrastructure — face structural conditions that eliminate or severely degrade the recovery options that software engineering typically relies on:

- **Latency.** Authority propagation takes seconds, minutes, or longer.
- **Energy bounds.** Computation and verification consume finite, non-replenishable resources.
- **Observation discontinuity.** Telemetry windows are interrupted by eclipse, interference, or partition.
- **Physical irreversibility.** Certain transitions modify physical state in ways that internal rollback cannot undo.
- **Recovery cost.** Human intervention is expensive, delayed, or impossible.

Under these conditions, the framework established in Chapters 24–57 does not break.

It becomes more important.

**Central thesis:**

> *As recovery latency and physical irreversibility increase, execution-space restriction transitions from optimization to necessity.*

This chapter is a speculative extension — a formal stress test of the framework under conditions of maximum physical constraint. The core results remain those of Chapters 24–57.

Chapter 58 asks a single question:

*What do those results mean when there is no recovery?*

---

### 58.1 — Physical Irreversibility vs. Logical Rollback

The execution model guarantees:

> *Internal state is restored to the pre-execution snapshot upon rollback.*

This guarantee is complete within the managed execution boundary.

It has always been conditional on one implicit assumption: that the system's internal state is the relevant state.

In physically embedded systems, this assumption may not hold.

**Definition 58.1 (Physical side effect).** A side effect `e` of transition `t` is *physically irreversible* if there exists no sequence of subsequent transitions that returns the physical system to its pre-`t` physical configuration, regardless of internal state.

Examples:

- Combustion of propellant changes velocity. No internal rollback reverses the delta-v.
- Actuation of a physical mechanism consumes mechanical wear.
- Transmission of a signal produces effects in the receiving system.
- Degradation of hardware under thermal or radiation stress accumulates irreversibly.

**Proposition 58.1 (Rollback asymmetry).**

```
rollback_status = ROLLED_BACK
does not imply
physical_system_state = pre_execution_state
```

This is not a failure of the model.

It is an explicit non-guarantee, documented in `EXECUTION_MODEL_LIMITS.md §2.3`.

What changes in physically embedded contexts is the *cost* of this gap — and therefore the strategic importance of preventing execution from reaching the failure point at all.

In systems with physical irreversibility, the value of execution geometry is not primarily *recovery*.

It is *prevention*.

The goal shifts from:

```
execute → observe → recover if needed
```

to:

```
restrict → admit only recoverable sequences → execute
```

This is the structural shift that Chapter 58 formalizes.

---

### 58.2 — Latency-Bound Authority

Chapter 57.5 establishes that authority is context-bound: a prior authorization does not survive authority context change.

The enforcement assumes that authority re-validation is instantaneous or near-instantaneous relative to execution.

In systems with significant propagation delay, this assumption degrades.

**Definition 58.2 (Authority propagation delay).** Let `Δ_auth` be the time between an authority context change — key rotation, signer revocation, policy update — and the arrival of that change at a remote execution node.

During `Δ_auth`, the remote node operates under a stale authority context. It does not know its context is stale. From its local perspective, all authority checks pass.

**Proposition 58.2 (Latency-bound authority validity).** In systems with authority propagation delay `Δ_auth > 0`, there exists a window during which:

```
local_authority_check  =  valid
global_authority_state =  revoked
```

This temporal gap cannot be eliminated by local enforcement alone. It requires either:

1. Bounding the propagation delay — architectural constraint.
2. Bounding the execution horizon to less than `Δ_auth` — operational constraint.
3. Accepting that authority is valid only as of last known context — epistemic constraint.

The epistemic constraint formulation is the most compatible with the ContinuumPort model:

> *Authority is valid relative to the last received and verified authority context. Execution under authority not re-confirmed within a declared freshness window is treated as `UNKNOWN` for policy purposes.*

This connects directly to the authority contraction principle from Chapter 56:

```
U(V₁) ≥ U(V₂)  ⟹  A(V₁) ⊆ A(V₂)
```

Unconfirmed authority increases uncertainty.

Uncertainty contracts admissibility.

---

### 58.3 — Observation Horizons

Chapter 57.2 establishes observation starvation: when the observation channel is absent, `INSUFFICIENT_DATA` contracts `CONTINUE` out of the admissible outcome set.

In physically embedded systems, observation discontinuity is structural, not adversarial.

Eclipse periods, communication windows, sensor degradation, and network partition create *observation horizons* — bounded intervals during which the system cannot receive external observation.

**Definition 58.3 (Observation horizon).** An observation horizon `H = [t₁, t₂]` is an interval during which the observation channel produces `None`. During `H`, all verdicts are `INSUFFICIENT_DATA`.

**Proposition 58.3 (Horizon-induced admissibility contraction).** During an observation horizon, `CONTINUE` is structurally inadmissible (I3). The admissible outcome set contracts to `{HALT, SKIP, ESCALATE}`.

Operational consequences:

- Systems must be designed to operate safely under `HALT` or `SKIP` during horizon intervals.
- Actions with irreversible physical side effects must not be scheduled during predicted horizon windows.
- Execution geometry must be defined over the observable state — not the inferred state.

The observation horizon constraint is therefore a design constraint on the execution geometry itself:

> *Geometries that require continuous observation for safety enforcement are inadmissible in systems with known observation horizons.*

This is a meta-level constraint: not just what the system may execute, but what geometries the system may declare.

---

### 58.4 — Distributed Geometry Drift

In single-node systems, the execution geometry is a fixed, signed structure verified at construction time.

In distributed multi-node systems, geometry propagation introduces a new failure mode: nodes may operate under geometries that are locally valid but globally inconsistent.

**Definition 58.4 (Geometry version vector).** In a distributed execution system with nodes `N₁, ..., Nₖ`, let `G(Nᵢ, t)` denote the geometry active at node `Nᵢ` at time `t`. Distributed geometry drift occurs when:

```
∃ i, j, t : G(Nᵢ, t) ≠ G(Nⱼ, t)
```

while both nodes believe their geometry is current.

Causes of drift:

- Asynchronous geometry updates with propagation delay.
- Network partition during geometry rotation.
- Selective delivery — some nodes receive the update, others do not.
- Replay of stale signed geometry (cf. Chapter 57.1).

**Consequence.** Nodes executing under different geometries define different admissible execution spaces. A transition admissible under `G(N₁, t)` may be inadmissible under `G(N₂, t)`. Coordinated execution — where nodes contribute to shared state — produces inconsistent admissibility decisions.

This is not Byzantine failure.

The nodes are not compromised. They are correctly executing their local geometry.

The failure is in the distributed consensus of which geometry is current.

Nodes executing under inconsistent geometries are not adversaries.

They are correct nodes in divergent admissibility spaces.

**Containment requirement.** Distributed systems using execution geometry must include a geometry consensus mechanism — a protocol ensuring that all nodes execute under the same signed geometry before any state-affecting transition is committed to shared state. The ContinuumPort model provides the local enforcement. The consensus layer is a deployment requirement outside the present model.

---

### 58.5 — Non-Recoverable Divergence

Chapter 57.3 establishes that divergence detected after commit contracts admissibility. The recovery path — `clear()`, re-observation, re-establishment of admissibility — is assumed to be available, if expensive.

In physically embedded systems with constrained resources, certain divergence states may be *non-recoverable* — not because of logical impossibility, but because the resources required for recovery are exhausted, unavailable, or physically inaccessible.

**Definition 58.5 (Non-recoverable divergence).** A divergence state `d` is *non-recoverable* in system `S` if the transitions required to restore admissibility from `d` are:

1. Physically impossible — required resources do not exist.
2. Energetically infeasible — required energy exceeds available energy.
3. Temporally inaccessible — required action window has passed.
4. Logistically impossible — required operator intervention cannot occur.

**Proposition 58.5.** In systems where non-recoverable divergence is possible, execution geometry restriction is not an optimization.

It is a precondition for survivable operation.

This elevates the significance of Theorem 9.1:

> *A persistent execution system is free of partial state corruption if and only if its realized execution set is confined to `G_F(S)`.*

In systems where divergence may be non-recoverable, this is not merely a correctness statement.

It is the condition under which the system remains operable at all.

---

### 58.6 — Admissibility Under Resource Bounds

The execution model assumes that admissibility verification is computationally negligible relative to execution.

In resource-constrained systems, verification itself has cost.

**Definition 58.6 (Bounded verification geometry).** A geometry `G` is *feasible under energy bound `E`* if the computational cost of verifying admissibility for any candidate transition does not exceed a fraction `α` of `E`, where `α` is a declared system parameter.

**The verification cost problem.** If admissibility verification consumes energy `E_v` and execution consumes energy `E_x`, and total available energy is `E_total`:

- Increasing verification depth reduces execution capacity.
- Reducing verification depth increases execution risk.

This introduces a resource dimension to geometry design absent from the base model. It does not change the fundamental characterization results — `G_F(S)` remains the necessary and sufficient restriction — but it constrains which geometries are operationally deployable.

Geometry design for resource-constrained systems must balance:

- Completeness of invariant coverage.
- Computational cost of verification.
- Residual risk from unchecked conditions.

The present framework defines the target.

Bounded verification defines the achievable approximation.

These are not the same thing. The gap between them is an engineering problem, not a formal one.

---

### 58.7 — The Physical Necessity Principle

The preceding sections establish a progression:

| Condition | Status of geometry restriction |
|---|---|
| Recovery cheap, latency low | Optimization — reduces recovery cost |
| Recovery expensive, latency moderate | Architectural requirement |
| Recovery impossible, latency high | Operational necessity |

**Principle 58.7 (Physical Necessity Principle).** Let `S` be a persistent execution system with physically irreversible side effects, authority propagation delay `Δ_auth > 0`, and observation horizons. As recovery cost `C_r → ∞` and `Δ_auth → ∞`, the admissibility framework transitions from an engineering choice to an operational necessity.

*Informal statement:* In systems where mistakes cannot be corrected, restriction of executable transitions to the admissible execution space is one of the few mechanisms capable of acting prior to irreversible execution.

There is no fallback.

This principle does not introduce new formal content. It applies the existing characterization to a limiting case.

It identifies why the framework becomes more relevant, not less, as autonomy increases and environments become more constrained.

---

### 58.8 — Scope and Non-Guarantees

Chapter 58 extends the conceptual framework of Chapters 24–57 to physically embedded contexts.

It does not:

- Provide a deployed implementation for embedded or constrained systems.
- Address domain-specific engineering challenges — thermal management, radiation hardening, structural dynamics.
- Replace systems engineering with formal admissibility theory.
- Claim that execution geometry alone suffices for safety in physically embedded systems.

The formal results of Chapters 24–57 remain the foundation.

Chapter 58 identifies the conditions under which those results become operationally critical rather than merely theoretically sound.

**The central non-guarantee:**

> *The model enforces what is declared. Undeclared physical risks are not blocked.*

This is consistent with `EXECUTION_MODEL_LIMITS.md §3`.

A geometry is only as strong as its declaration.

The engineer who defines it bears the responsibility the model does not.

---

### 58.9 — Relation to Prior Chapters

| Chapter | Concept | Extension in Ch. 58 |
|---|---|---|
| Ch. 28 | Observation layer | Observation horizons as structural design constraint |
| Ch. 57.2 | Observation starvation | Horizon-induced starvation as predictable and inevitable |
| Ch. 57.3 | Delayed divergence | Physical irreversibility as permanent, non-recoverable divergence |
| Ch. 57.5 | Authority desync | Latency-bound authority validity window |
| Ch. 57.6 | Rollback desync | Physical rollback impossibility |
| Ch. 57.8 | Geometry poisoning | Distributed geometry drift under asynchronous propagation |
| Ch. 56 | Authority contraction | Extended to resource bounds and propagation latency |

Chapter 58 does not introduce new invariants.

It applies the existing framework to conditions that eliminate the safety nets that make invariant violations merely expensive rather than catastrophic.

---

### 58.10 — Derived Principles

The following are consequences, not assumptions.

**Prevention over recovery.** In physically irreversible systems, the value of execution geometry is structural prevention. Recovery is not a fallback — it may not exist.

**Uncertainty contracts admissibility.** Under observation horizons or stale authority, the admissible execution space contracts. Not expands. This is the authority contraction principle applied to physical constraint.

**Geometry drift is not Byzantine.** Nodes executing under inconsistent geometries are not compromised. They are correctly executing locally valid but globally inconsistent admissibility spaces. This requires a consensus layer, not a security layer.

**Verification has cost.** In resource-constrained systems, admissibility verification competes with execution for energy. Geometry design must be bounded accordingly. The gap between the formal target and the achievable approximation is real and must be declared.

**Precondition for survivable operation.** In systems where divergence may be non-recoverable, `G_F(S)` restriction is the condition under which the system remains operable. The formal result does not change. Its operational weight does.

---

*Chapter 58 began from a simple observation: in some environments, rollback does not exist as a practical option.*

*The rest followed from the model.*

---

## Afterword — Where the Questions Came From

This book did not begin as a book.

It began as a series of conversations.

Many of them happened publicly — in threads between engineers building real systems and trying to understand where control actually lives in agentic architectures.

One of those conversations began late at night on X.

Minerva Infra (@MinervaRuntime) posted a short observation:

AI governance is being negotiated in contracts. But contracts do not execute code.

If a system can act outside declared authority, policy alignment does not matter.

Governance must sit in the execution path.

Cognition proposes. Governance decides. Execution acts.

That statement forced a structural question:

If governance must sit in the execution path, what is that governance rooted in?

A system can have policies.
It can have identity.
It can have memory.

None of these guarantee control unless they are structurally embedded where execution actually happens.

The response that followed reframed the problem.

The question was not whether a gate exists.

The question was what the gate is rooted in.

If authority is derived from persistent identity, then replaceability depends on identity integrity.

If authority is derived from declared task state, then replaceability depends only on task validity.

Both architectures can be fail-closed.

They differ in where replaceability breaks.

That distinction became Chapter 12.

---

A similar friction appeared in discussions with TACIT Protocol (@tacitprotocol).

Their model defended an identity-first architecture: cryptographic identity as invariant, delegation credentials for portability, reputation as a durable layer across sessions.

The model works for accountability.

But it raised a different question:

What must persist for the work to continue, independent of who continues it?

Not identity.
Not credentials.

Structure.

That question produced the formalism used throughout this book:

Σ = (D, A, Auth)

Three primitives.

Everything else is a consequence of how they interact.

The public context from which some of the ideas in this book emerged is documented at [gi0rgioroth.blogspot.com](https://gi0rgioroth.blogspot.com/2026/05/three-architectures-one-question_12.html)

---

Later conversations pushed the architecture further.

In a thread with Lume (@lume_signal), a subtle distinction emerged while discussing reconstruction across model boundaries.

Reconstruction can recover trajectory — the direction the work was already taking.

But trajectory alone does not produce action.

Action still depends on whether the system is permitted to execute the next step.

This clarified something earlier chapters only implied:

Work continuity and execution legitimacy are separate conditions.

Declarative state can restore trajectory.

Authority must still permit action.

That became the foundation of Chapter 21: Trajectory Integrity.

---

Another conversation revealed a quieter failure mode.

In a discussion about long-running systems, Arch asked:

How do you tell when the structure is still alive?

He later reduced it to a single line:

From inside, the tell is whether yesterday still biases the first millisecond of thought.

A structure can persist and still stop producing direction.

* The work survives.
* The state remains.
* Execution continues.

But accumulated structure no longer shapes what comes next.

The system becomes reactive instead of directed.

This distinction became structural vitality.

Persistence is not enough.

Structure must continue to generate direction.

Otherwise, continuity becomes archive.

---

The chapters that followed were not planned.

They emerged through the same pattern:

Friction first.
Distinction second.
Formalism third.

Questions about persistence led to path dependence.
Questions about path dependence led to governance gravity.
Questions about governance led to authority.
Questions about authority led to execution substrates.
Questions about long-running execution led to decay.
Questions about decay led to trajectory integrity.

And trajectory integrity raised the final question:

Who holds authority over direction once loss is detected?

---

Artificial intelligence did not create these problems.

It made them visible.

Agentic systems run continuously.

They accumulate decisions, state, and authority without reset.

In such systems, execution does not reset.

Once execution persists, governance cannot remain implicit.

Questions that appeared philosophical become architectural.

Automation can maintain continuity.

Direction is not a technical property.

And responsibility cannot be delegated to execution.

---

*This book does not resolve persistent systems.*

*It defines what can be enforced within them.*

*Execution can be constrained. Authority can be bounded. Unsafe reactions can be prevented.*

*What persists cannot be fully governed.*

*The system continues beyond its guarantees.*

*It is not solved.*

***It is sustained.***

Giorgio Roth / 2026


