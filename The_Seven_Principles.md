# Seven Principles · A Discipline for Working Intelligently with AI 

[![7 CORE PRINCIPLES](https://img.shields.io/badge/7%20CORE%20PRINCIPLES-purple)](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/PRINCIPLES.md)

### Foreword

---


### On the Word, and on the Source

The seven principles in this book began as the conceptual foundation of ContinuumPort, a software framework I developed in late 2025. That framework's documentation states seven principles intended to define what `.cp` files transport, what they exclude, and how they relate to the ephemeral nature of model inference. Those seven principles remain as stated there. They are the historical starting point of this book — and only the starting point.

Across the months that followed, the seven propositions evolved. Some kept their object and refined their formulation. Others discovered, under sustained adversarial pressure, that they had been naming a mechanism when they meant to name an object — or pointing at one substrate when the property they cared about lived in another. A few changed almost beyond recognition. The framework's original formulations were not wrong. They were incomplete in ways that became visible only through extended work with the systems they were trying to describe.

This book presents the matured form. It is not a revision of ContinuumPort. ContinuumPort remains what it was. This is a separate corpus, with its own seven chapters, sharing some titles and themes with the framework but representing independent editorial work. A reader who consults both will find divergences. The divergences are deliberate. They reflect what sustained adversarial refinement across multiple architectures and multiple voices produced when the original formulations were tested without mercy.

---

There is a question this raises, and it is worth answering directly.

If a principle changes under scrutiny, was it ever a principle?

The answer is yes — provided one keeps a small distinction in mind.

A principle, in the sense used here, is an object: a rule of orientation with high explanatory power. The formulation of that principle is the current best statement of it, given the scrutiny it has so far survived. The object and the formulation are not the same thing. The object can be stable while the formulation evolves.

What changes under adversarial pressure is rarely the existence of the object. What changes is the precision with which the object is identified — whether the formulation points at the mechanism or at the object the mechanism produces, whether it locates a property in the right substrate, whether it draws the boundary where the phenomenon actually lives.

Each chapter that follows has gone through several such refinements. Some have stabilized; some are still under active pressure. In the working documents that produced this book, each chapter carries a revision number and a status — *Active Siege*, *Provisionally Frozen*, *Frozen* — that names where in the refinement process it currently stands. The book itself presents the version that has, at the time of writing, survived the most pressure. That version may be revised in the future, if further work exposes a flaw that the present scrutiny missed. The principles will remain. Their formulations will be whatever the next round of work produces.

---

A reader who notices that the cover claims seven principles, and that some of those principles read more like working positions than axioms, has noticed something true. The distinction matters. These are not axioms in the sense that Euclid's postulates are axioms — fixed points from which everything else is derived. They are propositions that have survived a particular kind of scrutiny, stated as precisely as that scrutiny allowed, and offered with transparency about their status.

That is what *principle* means in this book.

It is not less than the word usually claims. It is what the word actually means, in any discipline that takes its own subject matter seriously.

---

### On Numbering and Reading Order

The principles in this book are numbered as stable objects of analysis.

They are presented in the order that best supports the argument. As a result, the reading order and the principle numbers do not always coincide.

The numbers identify the principles. The order of appearance reflects the path through the argument.

---

## Chapter 1 · Principle 1 · Take Your Work With You


### 1.1 — The Separation

When you write a document in a text editor, close the application, and open the file in a different editor, the work survives.

The first editor is gone. The second may look nothing like it. The document is intact.

This works because the work and the tool are separate. The file does not depend on the editor. The editor does not own the file. You can replace one without damaging the other.

This separation is so ordinary in most computing that it is invisible. You do not notice it when you save a spreadsheet, export a photograph, or copy a folder to a different machine. The work moves because nothing prevents it from moving.

Most AI platforms break this separation.

When work is conducted inside a conversational AI system — context accumulated across sessions, reasoning developed over weeks, definitions negotiated through interaction — the artifact and the infrastructure become difficult to distinguish. The conversation history lives on the platform's servers. The model's memory lives in the platform's architecture. The accumulated context has no independent existence outside the ecosystem that produced it.

The work is still yours.

But it lives in someone else's house.

And you cannot always take it when you leave.

---

### 1.2 — The First Question

When people compare AI systems, they usually ask which model is smarter, which writes better, which reasons more effectively.

These are real questions. They are not the first question.

The first question is simpler:

*If the platform disappeared tomorrow, would the project survive?*

Not in degraded form. Not as files no one can read. As work that can continue.

For most ordinary computing, the answer is yes without thinking. The editor closes; the file opens elsewhere. For most AI work conducted inside conversational platforms, the answer is some version of *I'm not sure* — followed quickly by *I don't want to find out*.

That hesitation is the whole subject of this principle.

If the project cannot survive the disappearance of the platform that produced it, the work and the platform are fused. The fusion may be partial. It may be deniable. It may be invisible during normal operation. But it is real, and it has a cost — paid not at the moment of disruption, but continuously, throughout the life of the project.

---

### 1.3 — What Survival Requires

The survival test sounds like a question about backups. It is not.

Backups answer a different question. They answer: *if the data is lost, can it be retrieved?* The survival test asks: *if the platform is gone, can the project continue?*

These are not the same. A perfect backup of conversation logs is data preservation. Whether those logs are usable on a different system, by a different model, with the context they were embedded in still functional — that is survival. Many platforms offer exports that satisfy the first question while failing the second. The files are there. They are no longer the work.

What survival requires is that the artifact and the engine remain distinguishable. The reasoning, the structured context, the accumulated decisions — these must exist in a form that does not depend on the specific platform that helped produce them. Not because the platform will necessarily disappear, but because the work should be a thing the user holds rather than a state the platform maintains.

This is not always automatic. In many current systems, it is not automatic at all. Maintaining the separation requires deliberate effort: documenting reasoning outside the conversation, exporting in forms that preserve usability, treating the platform as a tool rather than as the location of the work.

The effort feels disproportionate when the platform is working well. It feels obviously necessary the first time it is not.

---

### 1.4 — The Hidden Tax

Most discussions of AI cost focus on what is visible. Tokens. Credits. Subscriptions. Compute hours. These numbers can be measured, compared, optimized.

The larger cost is rarely measured because it does not appear on a bill.

The cost is reconstruction.

Every time continuity is broken — a new session, a new model, a lost context — work must be rebuilt. Assumptions must be restated. Definitions must be re-established. Constraints must be explained again. Decisions that were already settled must be justified again.

The machine time is visible. Tokens have prices. The human time spent rebuilding the same scaffold has no invoice. Yet for any project that extends across weeks rather than minutes, the human cost is larger than the computational one.

The first reconstruction is manageable. The second is tedious. The third begins to alter the work itself. People stop pursuing the best path. They pursue the path that is easiest to explain again. Not because the better path is unknown — but because the cost of re-establishing the context for it exceeds the patience available.

Over time, the tax does not merely slow the work. It shapes it. Exploration narrows. Ambition contracts. Projects quietly downshift from bold to merely feasible — not because the tools are inadequate, but because the cost of re-establishing full context after every disruption makes depth uneconomical.

This is what dependency actually costs.

Not the moment of departure, when it would be visible. The ordinary days, when it is not.

Portability is not valuable only because it protects a right. It is valuable because it reduces reconstruction. The right to leave is, in practice, the right not to start over.

---

### 1.5 — What This Principle Does Not Claim

It does not claim that platforms are adversarial by design. The fusion of work and infrastructure is usually a consequence of convenience, not intent. The same features that make a platform useful — persistent memory, accumulated context, integrated tools — are the features that make portability difficult.

It does not claim that the user should refuse to work on platforms. The principle is not a prohibition. It is a condition: the work must remain separable from the infrastructure, even when the infrastructure is useful.

It does not claim that portability is cost-free. Maintaining exportable records, documenting reasoning outside the platform, structuring work for migration — these require effort. The principle claims only that this effort is cheaper than the reconstruction tax that accumulates when portability is absent.

And it does not claim that portability alone is sufficient. A portable archive is better than a captive one. But files without the capacity to use them may still be inert. That problem belongs to a later principle. This one addresses only the first layer.

---

### 1.6 — Closing

You close the application.
You take the file.
You open it somewhere else.

The fact that this feels ordinary is the point.

The separation is invisible only when it exists. When it does not exist, its absence is invisible too — until the project has been rebuilt for the third time, and the work has quietly contracted to fit the friction.

The first principle does not promise that portability will be needed. It claims only that without it, a cost accumulates that the user does not see — and pays anyway.

The right to leave is the right not to start over.

---

*Giorgio Roth — June 2026*
