# External Repository Snapshots

**Status:** Informative evidence record
**Governance or conformance effect:** None

This document records evidence items preserved by the ContinuumPort maintainer for
possible later chronology or provenance analysis. It holds two classes of record,
kept separate and separately scoped:

- `EV-EXTERNAL-*` — snapshots of external public repositories;
- `EV-CONTINUUMPORT-*` — chronology anchors for this repository itself.

A recorded snapshot is not an allegation. It does not establish access to
ContinuumPort, copying, derivation, authorship, or independent creation. Those
questions require a separate comparison of dated contents and relevant prior art.

---

## EV-EXTERNAL-CONTINUUM-SNAPSHOT-001

**Source repository:** https://github.com/Cyrax321/CONTINUUM

**Metadata source:** Public GitHub repository, Git refs, commit history, releases,
branches, tags, issues, and pull-request records retrieved during capture.

| Field | Value |
|---|---|
| Capture date | 2026-09-16 |
| Capture timestamp | 2026-09-16T11:05:28.069010+00:00 |
| GitHub repository `created_at` | 2026-08-09T06:15:40Z |
| GitHub repository ID | 1328498728 |
| Fork status at verification | `fork: false` |
| Captured default branch | `main` |
| Captured HEAD | `cef019d72321c96075e68257b00767afb815da8a` |
| Earliest reachable commit | `ee9032b5afa3e60c46297580740748f38c791e89` |
| Reachable commits across captured refs | 2,446 |

**Preserved archive filename:** `CONTINUUM_PUBLIC_HISTORY_SNAPSHOT_2026-09-16.zip`

**Preserved archive SHA-256:**
`ec6e84cf92f2c9ff321305a77c4e7a1be85d521ee3fa0bdeb300c4aec02f2fe2`

**Custody:** Archive privately retained by the ContinuumPort maintainer.

**Archive publication:** Not published in this repository.

### Independent public-event anchor

GH Archive event `17170184905`, a public `PushEvent` recorded at
2026-08-09T06:40:08Z for repository ID 1328498728.

| Field | Value |
|---|---|
| GH Archive source file | `2026-08-09-6.json.gz` |
| GH Archive source URL | https://data.gharchive.org/2026-08-09-6.json.gz |
| GH Archive source file size | 20,935,930 bytes |
| GH Archive source file SHA-256 | `64d58a5c823761c86023d0b437d58a9e78905407761bb0e34d3ee02d5d54f21d` |
| Preserved GH Archive event SHA-256 | `815299eebaafe458dee4370c6245dce7ebb9be1806e684a0b51bc6d60fa02ed2` |

### Preserved scope

The archive contains the Git bundle for all refs advertised by GitHub at capture
time, the reachable commit history, ref listings, release/tag/branch metadata,
repository metadata, and the earliest 1,000 issue and pull-request records
returned through the public GitHub API.

### Earliest captured chronology

The earliest reachable commit is a root commit with no parent:
`ee9032b5afa3e60c46297580740748f38c791e89`.

Its recorded author and committer timestamp is 2026-08-09T11:49:13+05:30.
Converted to UTC, that timestamp is 2026-08-09T06:19:13Z — three minutes and
33 seconds after the repository `created_at` value. Its subject is
`feat: CONTINUUM v0.1.0 — Phase 1 complete`. Git reports that the root commit
introduced 15 files and 4,177 inserted lines.

The later commit `6653b669331c581f7bdc24ccc7a738e8c9d8c923`, recorded at
2026-08-09T13:19:17+05:30, has the subject
`feat(actions): implement idempotent action ledger for duplicate side-effect prevention`.

Across all refs present in the captured bundle, no commit author timestamp
precedes the GitHub repository `created_at` value; the root commit has the
earliest recorded author timestamp.

The GitHub API identifies the eight other repositories enumerated during review
as forks whose source is `Cyrax321/CONTINUUM`; within that enumerated set,
Cyrax321 is the source repository, not a fork.

These are repository-history observations. They do not independently establish
when the underlying work was created, when any particular content first became
publicly retrievable, or whether development occurred privately before the root
commit.

### What this record establishes

This Git commit publicly records the archive identity and the metadata stated
above. The SHA-256 digest binds any archive later supplied under this evidence ID
to the bytes held at the time of this record, provided that recomputation
produces the same digest.

The GH Archive event independently establishes that GitHub reported the
repository as public no later than 2026-08-09T06:40:08Z. It does not establish
that the repository was public at its creation time or at the root commit time.

The complete hourly GH Archive file contains one event bearing repository ID
1328498728: event `17170184905`. No earlier `CreateEvent` or other event for that
repository ID is present in that hourly file. The event payload records branch
`refs/heads/main`, before commit `35ddb1c8d034a8772102529b96ff1985b0280217`, and
head commit `1f207cc2a30096adb3c5cf98bd7a98829710420d`.

The captured Git objects verify that the root commit
`ee9032b5afa3e60c46297580740748f38c791e89` is an ancestor of the event's head
commit. Subject to the integrity assumptions of Git's content-addressed commit
chain, the public event therefore anchors the captured root commit indirectly
through that ancestry; it does not state the root hash directly.

### Limits

The snapshot cannot recover objects or platform records deleted before capture.

Git author and committer timestamps are repository data, not independent proof of
public retrievability at those times.

GitHub's repository `created_at` value records repository creation; it does not
disclose whether the repository was private before becoming public.

The issue and pull-request export is limited to the earliest 1,000 records
because the unauthenticated API limit was reached during capture.

The archive was collected and retained by an interested project maintainer, not
by an independent archival institution.

Neither chronological priority nor thematic similarity, alone or together, proves
copying.

### Interpretation rule

Any later comparison must distinguish:

- publicly timestamped ContinuumPort material;
- content present in the captured external repository;
- common prior art;
- distinctive correspondence not adequately explained by common prior art; and
- inference from evidence versus demonstrated provenance.

No copying claim should be attributed to this evidence record without that
separate analysis.

---

## EV-CONTINUUMPORT-ROOT-001

Chronology anchor for this repository. Recorded here for reference; it is not
part of, and carries no bearing on, the external snapshot record above.

**Root commit of this repository:**
`0912f2929d4e1724c8a5d664abec992278b4cb10`

https://github.com/giorgioroth/ContinuumPort/commit/0912f2929d4e1724c8a5d664abec992278b4cb10

| Field | Value |
|---|---|
| Recorded author date | 2025-12-01 |
| Parents | none (root commit) |
| Signature | verified by GitHub |
| Subject | `Initialize ContinuumPort CP-Core project structure` |

### What this record establishes

GitHub reports the commit signature as verified. The commit is the root of the
repository that exists today.

### Limits

The recorded author date is repository data, not independent proof of public
retrievability at that time. The same limitation stated above for external
repository timestamps applies here without exception.

An earlier repository, referenced in a GitHub notification dated 2025-11-29, was
deleted and is not recoverable. The present repository is therefore not a
continuous history from that date, and this record does not establish when the
underlying work began.
