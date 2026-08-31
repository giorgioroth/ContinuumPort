# External Timestamp Anchors

This document lists independent, third-party archived captures of this repository and its contents. Each entry is a snapshot made by the Internet Archive's Wayback Machine, not by the repository owner, and can be independently re-verified by anyone at any time.

These captures support timeline claims made elsewhere in this repository (see `docs/REGEN_ENGINE_BEHAVIORAL_VALIDATION_REPORT.md` and `AI_Architectural_Thinking.md`). They establish that specific content was publicly retrievable in the archived form no later than the capture timestamp. They do not establish authorship on their own; they are combined with signed commits and prior published preprints for that purpose.

## Captures

| Capture date | What it shows | Archive link |
| --- | --- | --- |
| 2026-01-08 | Repository state before the current architecture, invariant suite, and terminology existed | [Wayback capture](http://web.archive.org/web/20260108003133/https://github.com/giorgioroth/ContinuumPort) |
| 2026-01-30 | Repository state, confirming the pre-architecture baseline was unchanged over three weeks | [Wayback capture](https://web.archive.org/web/20260130094346/https://github.com/giorgioroth/ContinuumPort) |
| 2026-08-31 | Blame view of `AI_Architectural_Thinking.md`, showing revision attribution and per-line commit provenance | [Wayback capture](https://web.archive.org/web/20260831190333/https://github.com/giorgioroth/ContinuumPort/blame/main/AI_Architectural_Thinking.md) |
| 2026-08-31 | Raw content of `AI_Architectural_Thinking.md` at time of capture | [Wayback capture](https://web.archive.org/web/20260831183723/https://raw.githubusercontent.com/giorgioroth/ContinuumPort/main/AI_Architectural_Thinking.md) |
| 2026-08-31 | Blame view of `5. WHERE_REGEN_ENGINE_BELONGS.md`, with per-line calendar dates | [Wayback capture](https://web.archive.org/web/20260831183715/https://github.com/giorgioroth/ContinuumPort/blame/main/5.%20WHERE_REGEN_ENGINE_BELONGS.md) |

## How to verify

Open any link above directly. The Wayback Machine toolbar at the top of the page confirms the capture date independently of anything in this repository. No login or special access is required.

## How to add a new anchor

1. Go to `web.archive.org/save/` followed by the full URL to capture (for example, a raw file URL or a specific commit URL).
2. Wait for the capture to complete, then copy the full resulting URL from the browser address bar. It will start with `https://web.archive.org/web/` followed by a timestamp.
3. Add a new row to the table above with the date, a short description of what the capture shows, and the link.

Prefer capturing raw or plain-text URLs (for example, `raw.githubusercontent.com/...`) over rendered GitHub pages where possible, since static content is captured more reliably than pages that rely on JavaScript to render.

For a given claim or milestone, prefer capturing three things where possible, rather than one: the raw content, the specific commit page, and the commit diff. Together these cover what existed, when it was recorded, and what changed — which is stronger than any single capture on its own.

## What each type of evidence establishes

This repository combines three distinct kinds of evidence. Each answers a different question, and none substitutes for the others:

- **Wayback Machine capture** — "This content was publicly retrievable no later than the archived capture timestamp." The capture is maintained by the Internet Archive, independently of this repository.
- **Signed commit** — "This repository history associates this content with this commit, whose signature can be cryptographically verified against the signing identity/key." Author and committer timestamps are Git metadata and are not, by themselves, independent third-party timestamps.
- **Preprint or publication** (SSRN, OSF) — "This material was deposited and/or made publicly available by date X, according to the platform's own timestamp metadata." Where submission and public-availability dates differ, the relevant date should be stated explicitly.

No single evidence type independently establishes content, authorship/provenance, timing, and public disclosure all at once. Used together, these sources provide complementary evidence for those separate claims.
