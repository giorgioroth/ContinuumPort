
# What This Model Does **Not** Protect

## Explicit Limits of the CP-Core Threat Model

This document is a normative companion to the CP-Core threat model. It defines explicit non-goals and excluded risk categories.

It specifies the categories of risk that ContinuumPort and CP-Core do not address and do not claim to eliminate.

These limits are not defects or omissions.
They are **deliberate design decisions**, required to preserve the structural separation between **continuity of work** and **personal identity**.

---

## 1. Quality, correctness, or semantic validity of the work

ContinuumPort **does not guarantee**:

* factual correctness of the content;
* logical validity of captured decisions;
* suitability of conclusions to real-world context;
* absence of conceptual or technical errors.

CP-Core transports **the state of work as defined by the operator**, without verification, validation, or correction.

Reasoning errors, misinterpretations, or suboptimal decisions may be transferred intact.
**This behavior is intentional.**

---

## 2. Misinterpretation or abusive use of transferred work

ContinuumPort **does not prevent**:

* incorrect reinterpretation of original intent;
* use of the work for purposes different from the original one;
* unauthorized extrapolation or abusive derivative conclusions.

Once transferred, the work becomes **autonomous from the original author**.
The protocol does not retain control over subsequent usage of the content.

---

## 3. Risks associated with deliberately introduced sensitive or dangerous content

ContinuumPort **does not protect against risks** arising from:

* deliberate inclusion of sensitive data in CP-Core;
* inclusion of confidential information, trade secrets, or personal data;
* intentional capture of emotional, relational, or identifiable context.

Using CP-Core to transport such information **explicitly violates the protocol’s purpose** and places that usage **outside the ContinuumPort compliance domain**.

---

## 4. Legal, ethical, or compliance risk of the resulting work

ContinuumPort **does not provide**:

* legal compliance guarantees;
* ethical evaluation of content;
* protection against unlawful use of outputs.

Responsibility for the use of regenerated work rests **exclusively** with the operator or organization applying it.

---

## 5. Stylistic, narrative, or authorial coherence

CP-Core **does not preserve**:

* personal authorial style;
* narrative voice;
* expressive preferences;
* rhetorical consistency across sessions.

Regeneration is **semantic**, not **narrative**.
Differences in wording, tone, or structure are **expected and accepted**.

---

## 6. Protection against malicious actors with legitimate access

ContinuumPort **is not** an access control mechanism.

If an actor gains legitimate access to a CP-Core (e.g., via intentional sharing), the protocol **does not distinguish** between benign and malicious usage.

Access control, authentication, and authorization remain **external responsibilities**.

---

## 7. Relational or emotional continuity

ContinuumPort **does not attempt to protect**:

* human–AI relationships;
* emotional attachment;
* a sense of continuous presence;
* affective coherence across sessions.

These forms of continuity are **deliberately excluded**, as they introduce cumulative risk and dependency.

---

## Closing principle

ContinuumPort **is not a universal safety system**.
It is a protocol for **risk surface reduction**, achieved through the structural elimination of elements that should not circulate.

Anything left unprotected remains so **not by negligence**, but to avoid **false simulation of control**.

---

## Boundary formula

**CP-Core transfers work.**
**It does not transfer guarantees.**

---

**Giorgio Roth**

*ContinuumPort – Continuity without presence*
January 2026
