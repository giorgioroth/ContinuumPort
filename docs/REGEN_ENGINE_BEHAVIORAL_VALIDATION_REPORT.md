# REGEN Engine Behavioral Validation Report

- **Report date:** 2026-08-31
- **Execution date:** 2026-08-30
- **Evidence package timestamp:** `2026-08-30_144415_775`
- **Build commit:** Not recorded in the captured run.
- **Probe/suite revision:** Not separately versioned in the captured run.

## Purpose

This report records black-box behavioral probes, reference compliance checks, fault-injection checks, and the full automated test-suite result for the REGEN Engine build used in the captured run.

The probe phase exercises public-facing engine interfaces. The full automated suite also includes contract-level, adversarial, and implementation-level tests; it should not be interpreted as exclusively public-interface testing.

The term "behavioral validation" describes the scope of the run. This report does not claim independent third-party certification, complete security coverage, or proof of every REGEN property.

A passing test establishes that the tested case passed under the conditions recorded here. It does not establish that all possible attack or failure modes have been covered.

## Run Environment

The captured test output reports:

- Platform: Windows `win32`
- Python: `3.14.4`
- pytest: `9.0.2`
- pluggy: `1.6.0`
- anyio: `4.12.1`
- Test root: `regen-engine`
- Configuration: `pytest.ini`
- Automated test duration: `7.91 seconds`

The captured output does not include the Git commit SHA, the probe-harness revision, or the execution timezone. These identifiers were not recorded in the captured run; exact reproduction cannot be established from this log alone.

## Confirmed Behaviors

| Probe or suite result | Result | Observed evidence and scope |
| --- | --- | --- |
| Generation fencing | PASS | Generation advanced from `0` to `1`; the old token was rejected and a token from the current generation was accepted. |
| Fresh generation after restoration | PASS | Generation advanced from `0` to `1` after revocation and to `2` after restoration; old evidence was rejected and fresh evidence was accepted. |
| Exactly one epoch winner | PASS | Results were `['winner', 'loser']`. The probe used two threads sharing one controller instance. |
| Stale restoration evidence rejected without state mutation | PASS | Stale evidence was rejected at current generation `2`; authority state remained unchanged. |
| Geometry gate and rollback | PASS | A valid action committed; a geometry precondition violation was rejected before commit; an injected actuator failure fully restored internal state. |
| Capsule integrity and authority-context binding | PASS | A valid capsule reconstructed; tampered state was rejected; an authority mismatch was rejected without state mutation. |
| Reference compliance suite | COMPLIANT: 6/6 | All six checks passed for `RegenEngineAdapter`. |
| Fault-injection suite | 4/4 detected | All four intentionally faulty adapters were detected by the harness. |
| Full automated suite | 1978 passed, 1 xfailed | `1979` items were collected. The run reported no unexpected failures. |

## Reference Compliance Results

The reference adapter was tested against the following checks:

| Check | Result |
| --- | --- |
| I4: `snapshot_isolation` | PASS |
| I5: `reset_idempotent` | PASS |
| I5: `determinism` | PASS |
| I4: `atomicity_on_failure` | PASS |
| Interface: `result_contract` | PASS |
| Chapter 50: `d3_semantic_alignment` | PASS |

Result: **COMPLIANT — 6/6 passed**

## Fault-Injection Results

The fault-injection adapters were intentionally defective. "Detected" means that the compliance harness correctly identified the seeded defect.

| Adapter | Seeded defect | Detected violation |
| --- | --- | --- |
| `FaultyAdapter_Partial` | Incomplete rollback | I4: `atomicity_on_failure` |
| `FaultyAdapter_NonDeterministic` | Order-dependent or non-deterministic execution | I5: `determinism`; Chapter 50: `d3_semantic_alignment` |
| `FaultyAdapter_SnapshotAlias` | Snapshot aliasing | I4: `snapshot_isolation` |
| `FaultyAdapter_D3` | Semantic mismatch | Chapter 50: `d3_semantic_alignment` |

The four intentionally faulty adapters were detected as expected.

## Full Suite Result

The automated suite reported:

```text
1978 passed, 1 xfailed in 7.91s
```

The run included one expected failure documenting a known limitation: reconciliation does not currently guarantee that a directly revoked authority remains revoked. This `xfail` is a documented limitation of the current implementation. It should not be presented as a passing safety property.

The identifier of the specific test case is present in the captured test output included in the evidence package; it is omitted from this public report.

## Interpretation

Under the recorded conditions, the tested REGEN Engine components demonstrated:

- rejection of stale generation tokens;
- fresh generation issuance after revocation and restoration;
- rejection of stale restoration evidence without authority-state mutation;
- a single winner in the tested two-thread epoch race;
- rejection before commit when tested geometry preconditions fail;
- complete rollback of tested internal state after actuator failure;
- deterministic capsule-integrity rejection after tampering;
- authority mismatch rejection through `AuthorityContext`;
- detection of all four seeded faulty adapters;
- compliance with the six listed reference checks.

The results also show that REGEN enforces declared geometry and transition constraints. It does not independently determine whether an undeclared or incomplete action is dangerous.

## Evidence Integrity

The evidence package generated by the run was:

```text
regen-external-validation-2026-08-30_144415_775.zip
```

The generated SHA-256 manifest was:

```text
regen-external-validation-2026-08-30_144415_775.sha256
```

The recorded SHA-256 digest was:

```text
7CCA258B851F9E4DE4EDC5A267708F3846E8809810ED7E160FDAE57580B34713
```

The digest is a fingerprint of the archive bytes. By itself, it is not an independent attestation of the test results.

The archive, manifest, probe harness, and underlying test suite are not currently included in this public repository. Access is available on request.

For stronger independent auditability, the evidence package should be accompanied by:

- the exact engine commit SHA;
- the exact probe and suite revision;
- a manifest of archive contents;
- the execution timezone;
- the command used to produce the archive and digest;
- sufficient instructions to reproduce the run.

## Historical Context

An independent third-party archival record of this repository is available through the Internet Archive:

[Internet Archive capture from 2026-01-08](https://web.archive.org/web/20260108003133/https://github.com/giorgioroth/ContinuumPort)

The capture predates the architecture, invariant suite, and terminology described in this report. It provides historical context for the project timeline; it does not validate the engine, the test results, or this report.

## Limits

The following properties are not established by these probes or by the reported suite result:

- portable commit receipts;
- `operationId`-based result recovery;
- cross-process distributed compare-and-set;
- holder-to-holder authority succession;
- a public handoff API;
- cryptographic signatures carried by `StateCapsule` objects;
- universal fencing for uncontrolled external web resources;
- external-effect compensation or rollback;
- detection of all risks in incomplete or incorrectly declared geometry;
- idempotent commit semantics for every prepared request.

The epoch race probe uses two threads sharing one controller instance. It is not a distributed multi-process test.

The rollback probes establish restoration of tested internal state. They do not establish that an external HTTP request, actuator effect, or other uncontrolled side effect can be undone.

The geometry probes show that complete geometry can block the tested composition attack, while incomplete geometry can authorize the same action. REGEN enforces what is declared; it does not infer danger from undeclared risk.

The capsule authority probe verifies authority binding through `AuthorityContext` for capsules carrying authority information. It does not prove that the capsule itself carries a cryptographic signature. Current tests also show that an unbound capsule can reconstruct under any authority, and reconstruction without an authority context skips the binding check.

The suite includes a case in which a raw prepared request can be committed twice. Replay is detectable through outcome state, and the transaction manager prevents proposal replay, but this report does not claim universal idempotent commit behavior.

A passing suite establishes that the written cases were satisfied under the conditions run. It does not establish complete corpus coverage or protection against every possible attack and failure mode.

## Conclusion

Under the recorded run conditions and environment, the tested REGEN Engine components exhibited the behaviors listed in this report.

The evidence supports treating REGEN as a testable execution kernel with generation fencing, geometry-gated commit, internal rollback, capsule integrity checks, and authority-context checks.

Receipt recovery, distributed authority succession, public handoff, external-effect compensation, undeclared-risk detection, and broader replay guarantees remain open requirements.
