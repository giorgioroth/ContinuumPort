# ContinuumPort — Design Rationale

This note explains why ContinuumPort limits what travels with a task. The [frozen CP-START specification](https://github.com/giorgioroth/ContinuumPort/blob/CP-NORM-H01-FROZEN/cp-core/CP-NORM-H01/CP-START.md) defines how a conforming handoff begins. The [published boundaries](https://github.com/giorgioroth/ContinuumPort/blob/canon-2026-08/docs/cp-boundaries.md) define what it may carry. This note adds no requirements to either document.

## What a successor needs

“Prepare the English edition. The figures have been checked. Publication still needs approval.”

A new editor can tell what to work on, which decision has been recorded, and where to stop. English is an explicit requirement for this edition. It says nothing about the author's usual language or personal preferences. Nor does the handoff give the editor permission to publish.

CP-Core carries the stated goal, decisions, constraints, progress, and open questions. A successor should be able to understand those from the record without reconstructing the original conversation.

## Why draw the boundary here?

The [early project notes](docs/boundaries.md) describe an exploratory handoff that included autobiographical details and emotional framing. The receiving model replied as though it remembered the earlier exchange.

The observation was in the reply. It did not establish that a self had persisted, what caused the wording, or how every model would respond. It exposed a practical problem: a successor could sound entirely familiar while missing the last decision that mattered to the work.

ContinuumPort therefore excludes persona, autobiographical memory, emotional history, and behavioral conditioning from the handoff. Leaving material out of an export does not erase the source conversation. The rules also exclude personally identifiable information. A name can still be typed into a project summary, so checking the field names alone cannot establish that an export is free of personal data.

## Preparing context and authorizing action

The [December 2025 Regen Engine specification](spec/regen-engine.md), marked **Draft**, describes a minimal, stateless component. It parses and validates a CP-Core container, extracts the stated intent, constraints, and task state, and formats that context for the target model without adding its own interpretation.

The [later execution work](5.%20WHERE_REGEN_ENGINE_BELONGS.md) uses **Regen Engine** for a private, experimental kernel. On the evaluated local path, it checks a prepared operation against the relevant state, declared constraints, and current authority at commit.

The distinction matters in the editor's example. A prompt can faithfully carry the words “publication still needs approval.” Preventing an unauthorized release requires control over the path that can actually publish. Delivering the prompt establishes neither that the path is controlled nor that a release occurred.

## What stays outside the shared protocol

A service may need authentication before it releases a handoff. It may sign records or use diagnostics. A safeguard can be necessary for that service without becoming a dependency for every implementation that reads CP-Core.

Extensions still have to respect the boundary. A diagnostic that reports a missing task constraint helps someone repair the handoff. An extension that reconstructs a user's persona changes what is being handed over; calling it optional does not make it conforming.

Before making a feature mandatory, ask what would go wrong for two implementations exchanging the same task without it. If the only answer is that one product would lose a convenience, keep the feature in the product.
