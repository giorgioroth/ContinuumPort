# ContinuumPort

## Latest progress — 26 October 2026

- **Two new private chapters:** Chapter 63 — *From Passing Tests to a Reason for Adoption*; Chapter 64 — *What the Test Actually Establishes*.
- **Implementation and checks:** reconciliation preserves direct revocations in the tested cases; 20 additional tests cover evaluator behavior and selected GS and legacy execution cases.
- **Latest recorded Windows run — 25 October:** **2,097 tests and 31 subtests passed**, including those 20 additional tests.

These are maintainer-reported results from private, AI-assisted work, not an independent audit. The public manuscript remains at 62 chapters; the kernel source and complete evidence archives remain private.

[Read the full development update and evidence limits](#private-development-update--26-october-2026).

---

Imagine renovating a house with a builder. The plan, what has been done, and
what comes next live in a file, so another builder can continue if the first
one leaves. If the builder wants to knock down a wall or spend money, a note
saying "ask first" is not enough: the approval has to stop the work when
permission is missing. And a builder who follows the plan perfectly does not
prove the plan is right, or that he had the right to change it.

In this analogy, CP-Core is the portable file within ContinuumPort. Regen
Engine is the execution gate that checks whether the work may proceed.

## Status — documentation updated 26 October 2026

Public source development in this repository remains paused as of September
2026. Work on the execution kernel continues privately; its source is not
published, and this repository does not track its source revisions.

Published specifications, books and documents retain their own dates and
declared status. The 21 October documentation update aligned this README and
[Where Regen Engine Belongs](https://github.com/giorgioroth/ContinuumPort/blob/main/5.%20WHERE_REGEN_ENGINE_BELONGS.md)
with the bounded evidence summarized there. The 26 October update adds the
private development summary below. Neither update is a kernel release or a
repository-wide revision of the specifications. Private review has also
narrowed claims in other documents, including the definition of compliance
in `REGEN-COMPLIANCE-v1.md`; those files retain their own scope and status.

**Practical comparative advantage is not established.** Reported local
comparisons support specific observations, not general implementation
conformance, application-wide protection or a commercial valuation. A useful
advantage could be additional protection or comparable protection with lower
total integration, verification and maintenance cost.

The public quickstart demonstrates checks against a declared geometry and
restoration of managed state after a failed sequence. The private kernel has
been tested on transitions entering its evaluated boundary. It has not been
shown that every effect in an application reaches that boundary; restoration
of managed state does not promise reversal of external effects.

The published model does not establish general governance over replacing one
accepted geometry with another. Reported private GS observations do not
ratify a new public succession contract or establish an advantage over a
conventional solution to that problem.

---

## Private development update — 26 October 2026

Work continues privately on the manuscript, execution kernel and evaluation tools.

**Two additional chapters have been written for the private continuation of AI Architectural Thinking:**

- **Chapter 63 — From Passing Tests to a Reason for Adoption:** examines what evidence would justify adopting Regen over a conventional implementation.
- **Chapter 64 — What the Test Actually Establishes:** examines evaluator reliability, positive controls and the conclusions supported by a passing test.

Both chapters are informative and introduce no normative changes. The public manuscript remains at 62 chapters.

**Implementation and verification progress includes:**

- In the tested direct-revocation cases, reconciliation leaves the revocation in force. Removing its direct cause requires an explicit grant accepted by a configured granting authority; other access conditions still apply.
- Twenty additional automated tests covering evaluator behavior and selected GS and legacy execution cases, including detection of no-op implementations, misleading success reports and test errors mistaken for fault detection.
- A maintainer-recorded Windows run on **25 October 2026** reporting **2,097 tests and 31 subtests passed**, including those twenty additional tests.
- Separate GS phases reporting **20 property tests passed** and **15 test–mutant pairs producing the expected assertion failures**, with zero test errors.

The suite includes both regression checks and tests documenting known limitations. These private, AI-assisted results establish outcomes for the exercised cases; they do not establish an independent audit, general implementation conformance or comparative advantage. Work on the formalization and its scope remains under review.

The kernel source, detailed implementation materials and complete evidence archives remain private. This update does not change the public specifications or announce a kernel release.

---

## The problem

In persistent systems, execution fails mid-sequence. When it does, the state may reflect a committed prefix — neither the initial state nor the intended result. This is not an edge case. It is a structural property of unconstrained execution.

Reactive recovery — rollback, retry, or compensation — addresses failures after execution has begun. For non-invertible transitions or externally visible side effects, restoration cannot be guaranteed.

The formal model describes admissible execution sequences under declared
constraints. Establishing that an implementation and a complete application
enforce the modeled boundary requires separate evidence.

---

## Quickstart

```bash
git clone https://github.com/giorgioroth/ContinuumPort
cd ContinuumPort/quickstart
python run.py                   # I4 — no partial state escape
python run_determinism.py       # I5 — deterministic outcome
python run_address_invariant.py # I2 — domain integrity
```

No dependencies. Runs in seconds.

---

## What the demos show

**I4 — Partial state escape**

```
[FaultyAdapter]
Action 1 succeeds. Action 2 fails.
State after: {'account': 'active', 'balance': 100, 'processed': True}
✗ VIOLATED — partial state escaped

[ContinuumPort]
State after: {'account': 'active', 'balance': 100}
✓ ENFORCED — internal state restored to pre-execution snapshot
```

**I5 — Determinism**

```
[FaultyAdapter]   Run 1: {'x': 2}   Run 2: {'x': 1}   ✗ VIOLATED
[ContinuumPort]   Run 1: {'x': 2}   Run 2: {'x': 2}   ✓ ENFORCED
```

**Composition attack**

```
Same engine. Same actions. Different geometry.
Incomplete geometry → authorized=True  → budget=-50
Complete geometry   → authorized=False → BLOCKED
```

These demos exercise declared constraints. Neither a successful check nor
the declaration itself certifies that the permitted action is safe in the
real world. The public demo adapter is not the private Regen Engine.

**Domain integrity**

In the formal model, an out-of-domain action is excluded from the admissible
execution space. That model statement does not establish that arbitrary
application code cannot reach an effect outside the implemented boundary.

---

## Invariants and their enforcement basis

The five invariants do not have the same evidentiary status. The I1-I5 labels
below belong to this README's invariant table; they should not be used to
identify unrelated properties carrying the same numbers elsewhere.

The published formal basis cited below is
[*Trajectory Integrity in Persistent AI Systems*](https://doi.org/10.17605/OSF.IO/B8SGR).
The associated [model limits](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/EXECUTION_MODEL_LIMITS.md)
exclude concurrent/distributed execution (Section 2.4) and Byzantine or
adversarial environments (Section 2.6). Adapter compliance is assumed and is
not verified by the model (Section 2.9). The table records that published
basis; this documentation update does not independently re-verify the proofs.

| Property | Published basis and scope |
| --- | --- |
| I1 — No unauthorized execution | Model-level claim: authority is required for admissibility under the stated assumptions. Cited formal basis: [Trajectory Integrity in Persistent AI Systems](https://doi.org/10.17605/OSF.IO/B8SGR), Sections 3-5. This is not a proof of application-wide path closure. |
| I2 — No out-of-domain execution | Model-level claim: the declared domain bounds the admissible execution space. Cited formal basis: [same source](https://doi.org/10.17605/OSF.IO/B8SGR), Sections 3-5. Implementation and integration enforcement require separate evidence. |
| I3 — No invalid state transition | Model-level claim: admissible transitions satisfy the declared constraints. Cited formal basis: [same source](https://doi.org/10.17605/OSF.IO/B8SGR), Theorem 5.1, under its stated assumptions. |
| I4 — No partial state escape | Model-level claim within the declared internal-state boundary and adapter assumptions. Cited formal basis: [same source](https://doi.org/10.17605/OSF.IO/B8SGR), Theorem 5.1 and Corollary 5.4. This does not establish rollback of external effects. |
| I5 — Deterministic outcome | Exercised empirically by the subset of the suite that tests it directly: repeated execution of the same configuration and sequence, compared for identical final state, with negative controls. Other tests document limitations or exercise other properties; a suite total would not be a count of evidence for I5. The audit replay mechanism is assumed by construction: no test independently verifies replay determinism across adapter implementations. |

The model results are conditional on their declared boundary and assumptions.
Concurrency and adversarial implementation probes are empirical evidence
under their own conditions; they do not extend these formal results. Recorded
tests exercise I5 as described in the table. A passing suite establishes that
the written cases were satisfied in the recorded run, not that the cases
cover every claim or that an arbitrary adapter satisfies the contract.

---

## Tests

The self-contained quickstart demos above run on a clean checkout of this repository with no dependencies. The full validation suite runs against the Regen Engine kernel, which is proprietary (Beta license) and is not included in this public repository. Evaluation access to the suite is available on request (access@continuumport.com).

<img width="2973" height="1627" alt="image" src="https://github.com/user-attachments/assets/9f726630-922c-4b83-8f2d-5ffa54cfd86b" />



The screenshot above records a historical run in the author's Windows environment. It is not a current suite total; its execution date and source revision are not established by this README.

Paper 4 (*Adversarial Execution Governance*) reported a historical cumulative corpus of 1,806 tests at submission, after Batches 1–12. A subsequent historical result and its provenance limits are recorded in the private evidence ledger `CP-EVIDENCE-001`, revision 0.5.4, entry `EV-KERNEL-SUITE-001` (reviewed 21 September 2026 UTC). That is the ledger's review date, not an established execution date; the entry also lacks the executed build and suite revision. The canonical ledger is maintained privately and is not synchronized with the historical GitHub copy. It is available on request at access@continuumport.com. These historical entries do not establish a current suite total; see the dated private development update above for the separate 25 October record.

A later maintainer-supplied record reports the following run on **17 October
2026**, Windows, Python 3.14.4 and pytest 9.0.2:

| Evidence class | Reported result |
| --- | --- |
| Existing regression suite | 2,077 test instances and 31 subtests passed |
| GS property suite | 20 tests passed |
| Matched injected-fault controls | 15/15 reported assertion failures, with zero test errors |

These are distinct evidence classes, not a combined guarantee count. The
15 controls are matched to known tests; five GS cases have no corresponding
fault in that set. The results are reported from private records and were
not rerun for this README update. They neither date the historical screenshot
nor establish application-wide protection. See
[Where Regen Engine Belongs, Section 4](https://github.com/giorgioroth/ContinuumPort/blob/main/5.%20WHERE_REGEN_ENGINE_BELONGS.md#4-reported-verification-record)
for provenance and sensitivity limits, and Section 5 for the separate
comparisons, including the reported 30/30 request-binding executions on each
variant. No difference was observed on that declared comparison set; general
equivalence and practical advantage remain unestablished.

The adversarial corpus was developed across 13 batches with the assistance of Claude (Anthropic), ChatGPT (OpenAI), and Gemini (Google) — in that order of contribution. The validation suite is the primary empirical research artifact of this project.

Model-family names alone do not establish review independence; roles, prior
exposure, reused cases and reproduction scope must be recorded separately.

The validation suite includes:

- replay attacks
- state drift injection
- geometry swap attacks
- capability rebinding
- TOCTOU patterns
- composition attacks
- hash canonicalization failures
- authority desynchronization
- rollback desynchronization
- cross-cycle state trap scenarios
- malformed capsule reconstruction
- deterministic integrity verification
- hostile observation (H1–H5)
- commitment graph attacks (G1–G6)
- causal opacity (O1–O5)
- provenance enforcement (P1–P5)
- authority laundering (L1–L6)
- admissibility erosion (E1–E5)
- concurrent adversarial pressure (C1–C5)
- control-effect binding (the subject validated for admissibility versus the object whose effects commit)
- fail-closed ordering (refusal before the actuator, not materialization followed by rollback)
- audit provenance substitution (a caller's description of intent varying the record of what was performed)
- commit-boundary enumeration (a second, unasserted implementation of a repaired boundary)

The recorded tests exercise these patterns and limitations: some show refusal at the declared boundary, while others document gaps or assumptions. Coverage of enumerated cases does not establish structural impossibility for categories beyond the formal model (see Scope and limits).

---

## Scope and limits

ContinuumPort specifies correctness conditions for execution under declared constraints. Regen Engine enforces those constraints on transitions that reach its declared boundary, subject to the adapter and effect limits below.

It does not guarantee:

- Correctness of intent
- Correctness of declared constraints
- External side effects beyond the execution boundary

Undeclared risks are not blocked.

These limits are explicit and documented in [`EXECUTION_MODEL_LIMITS.md`](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/EXECUTION_MODEL_LIMITS.md)

---

## Architecture

[Architecture diagram](https://giorgioroth.github.io/ContinuumPort/)

```
Actions
   ↓
Authority check
   ↓
Geometry enforcement
   ↓
Execution (atomic)
   ↓
Commit / Rollback
```

The diagram describes the intended governed path. The private implementation
is evaluated for selected behaviors on that path; the diagram does not prove
that all effect-capable application paths pass through it.

Formal model: GF(S) — the maximal prefix-closed, failure-free execution space.
Only sequences inside GF(S) are admissible in the specified model. These
formal definitions are distinct from proving that a concrete implementation
and its integration preserve the modeled properties.

---

## Why "Execution-Governance Kernel"

The name describes the intended role of a commit boundary: checking a
prepared transition against the applicable authority, state and declared
constraints before permitting its governed effects. Refusal before an effect
is different from restoring managed state after that effect has occurred.

**Correct routing and adapter compliance are integration preconditions.**
Defining a compliant adapter as one that routes through the kernel does not
prove that a deployed adapter is compliant or that no other effect path
exists. The evaluated setting trusts the host, implementation, adapters,
keys, authority store and instrumentation. Its local gate is not a
demonstrated isolation boundary against arbitrary code in that host.

Reported local tests exercise particular checks and refusal paths. They do
not establish universal fail-closed behavior, complete mediation of an
application, or general implementation conformance. The April preprint's
broader non-bypassability claim must be read with the correction recorded in
[*Evidence That Does Not Reach the Claim*](https://ssrn.com/abstract=7295418);
the [April preprint](https://ssrn.com/abstract=6533358) remains a historical
record, not replacement evidence for the withdrawn support.

The practical selection question is whether Regen prevents a relevant
failure, or reduces the total work needed to prevent it, compared with
competent existing controls under comparable trust assumptions. The name
"kernel" does not answer that question.

---

## Compliance interface

```python
class RegenAdapter(ABC):
    def reset(self, state: dict) -> None: ...
    def snapshot(self) -> dict: ...
    def execute(self, actions: list[dict]) -> ExecutionResult: ...
    def simulate(self, state: dict, action: dict) -> dict: ...
```

See [`EXECUTION_MODEL_LIMITS.md` §2.9](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/EXECUTION_MODEL_LIMITS.md) for the trust assumptions this contract relies on.

---

## Repository structure

This public repository contains the specification, the self-contained demos, and the published books and essays:

```
quickstart/       — self-contained runnable demos (no dependencies)
docs/             — formal specification, scope boundaries, invariant-test documentation
cp-core/          — CP-Core normative schema and handoff specification
regen-engine/     — engine demonstrations (attack, side-effects)
```

The Regen Engine kernel and the full compliance/validation suite are proprietary (Beta license) and are not included in this public repository. Evaluation access is available on request: access@continuumport.com

---

## Reading path

The numbered documents at the repository root are meant to be read in order:

1. [PROJECT_STATUS](https://github.com/giorgioroth/ContinuumPort/blob/main/1.%20PROJECT_STATUS.md) — where the project stands
2. [Whitepaper](https://github.com/giorgioroth/ContinuumPort/blob/main/2.%20Whitepaper.md) — what it is, technically
3. [LICENSE_REGEN](https://github.com/giorgioroth/ContinuumPort/blob/main/3.%20LICENSE_REGEN.md) — under what conditions it may be used
4. [Roadmap](https://github.com/giorgioroth/ContinuumPort/blob/main/4.%20Roadmap.md) — where the project is going
5. [WHERE_REGEN_ENGINE_BELONGS](https://github.com/giorgioroth/ContinuumPort/blob/main/5.%20WHERE_REGEN_ENGINE_BELONGS.md) — where it applies, and where it does not

Documents 1–4 address status, design, licensing and roadmap. Their declared
authority and scope must be read in the documents themselves; their position
in this list grants no authority. Document 5 is informative positioning and
grants no rights or conformance status. Applicable license terms and separate
governing agreements control licensed use.

---

[![CP-Core](https://img.shields.io/badge/CP--Core-Apache%202.0-green)](LICENSE) 
[![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/3.%20LICENSE_REGEN.md) 
[![Status](https://img.shields.io/badge/status-research%20artifact-blue)](https://github.com/giorgioroth/ContinuumPort/blob/main/1.%20PROJECT_STATUS.md) 


---

[![PRINCIPLES](https://img.shields.io/badge/PRINCIPLES%20-orange)](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/PRINCIPLES.md)


## Further reading

- [AI Architectural Thinking](https://github.com/giorgioroth/ContinuumPort/blob/main/AI_Architectural_Thinking.md) — the conceptual framework (62 chapters)
- [EXECUTION_MODEL_LIMITS.md](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/EXECUTION_MODEL_LIMITS.md) — explicit scope boundaries
- [Blog](https://gi0rgioroth.blogspot.com/) — context and philosophy
- [continuumport.com](https://continuumport.com/)

---

## Documentation change record

- **26 October 2026.** Added a private development summary covering Chapters
  63 and 64, tested direct-revocation behavior and the maintainer-reported
  25 October results. Distinguished regression checks from tests documenting
  known limitations. Preserved the 17 October results as a historical
  record. No private source or evidence archive is published by this update;
  it makes no normative, licensing or kernel-release change.

- **21 October 2026.** Clarified formal-model assumptions and the distinction
  between a compliant path and demonstrated application-wide mediation.
  Added the dated, maintainer-reported 17 October counts without replacing
  historical records; linked the current positioning document and the April
  claim's self-audit. This is a documentation change, not a kernel release,
  test rerun, license amendment or ratification of a new specification.

*Gh. Rotaru (Giorgio Roth) — Independent researcher, 2026*

contact: access@continuumport.com

