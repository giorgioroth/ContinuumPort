# External Timestamp Anchors

This document lists timestamps for this repository and related work that were set by parties other than the repository owner: the Internet Archive, GitHub, and the DOI registries DataCite and Crossref. Each entry can be re-verified independently.

These anchors support timeline claims made elsewhere in this repository (see `docs/REGEN_ENGINE_BEHAVIORAL_VALIDATION_REPORT.md` and `AI_Architectural_Thinking.md`). They establish existence, timing, and public availability. They do not establish authorship, correctness, or originality on their own.

*Last updated: 2026-10-10.*

## Repository history note

The original repository `giorgioroth/continuumport` was deleted by its owner and recreated on 2025-12-01. Commits made before that date are not part of the current history. The only verified anchor for that period is a GitHub-signed notification email (see below).

## 1. GitHub-signed email (DKIM)

| Signed at (UTC) | Signer | What it attests |
| --- | --- | --- |
| 2025-11-29 20:59:43 | `github.com`, DKIM selector `pf2023` | Push to `giorgioroth/continuumport`, branch `main`, commit `fa803e27b49560636531eeb88b1e37c91eb469e6`, modifying `README.md` ("Revise README notes and strategic alignment section") |

The body hash and the RSA-SHA256 signature were verified on 2026-10-10 against the key GitHub publishes in DNS for `pf2023._domainkey.github.com`. The original message (SHA-256 `e7dcbdf8b024b3884310e567aff2f510032ff1d04df487c9c086b82a0f7f64a4`) is retained by the author and can be provided for independent verification. This is the earliest verified anchor. It shows that the repository existed and that `README.md` was changed. It does not show what `README.md` contained.

## 2. GitHub-signed commit history

As of 2026-10-10, all 533 commits on `main` were created through GitHub's web interface. Each has `GitHub <noreply@github.com>` as committer and is signed with GitHub's web-flow key:

- Key ID: `B5690EEEBB952194`
- Fingerprint: `9684 79A1 AFF9 27E3 7D1A 566B B569 0EEE BB95 2194`

Compare this fingerprint with the one GitHub publishes for web-flow commits before relying on it.

For web-flow commits, GitHub's server sets the committer timestamp and signs it, so these timestamps are attested by GitHub rather than by the author. All 533 signatures verified as valid on 2026-10-10.

| Commit | Signed at (UTC) | Note |
| --- | --- | --- |
| `0912f2929d4e1724c8a5d664abec992278b4cb10` | 2025-12-01 18:36:11 | First commit of the current repository |
| `2580485b8f8cb80ac535fe72f58c9612c9b1fad2` | 2026-01-18 09:23:35 | Introduces "Author Absence Invariance" in `README.md`; falls between the two January archive captures below |
| `4e396fba16712e841448ce7d5eb6337158d7dd0c` | 2026-09-25 | Pinned book baseline: `AI_Architectural_Thinking.md`, SHA-256 `0624d53a14228c9b55b1d6fd5fd4a3926ee9d4f046f92278b10e824b91ef860b`, 408,617 bytes |

To verify, import GitHub's web-flow public key, clone the repository, and run:

```
git verify-commit <commit>
git log --format="%H %cn %cI" | head
```

## 3. Internet Archive captures

| Capture (UTC) | What it shows | Archive link |
| --- | --- | --- |
| 2026-01-08 00:31:33 | Repository page at 149 commits. In the signed history at that time, the terms "execution geometry", "admissibility" and "fail-closed" do not yet occur; "Regen" occurs 121 times and "invariant" 3 times. | [Wayback capture](https://web.archive.org/web/20260108003133/https://github.com/giorgioroth/ContinuumPort) |
| 2026-01-08 01:31:39 | Repository page. Original HTML (`id_`) SHA-256: `679D9DD8751DA3C5011046681D954D30AFFC493C2D296C908A012E5129E5B0C5`. Contains "Proprietary Regen engine" and "Only intention and working state are portable"; does not contain "Author Absence Invariance". | [Wayback capture](https://web.archive.org/web/20260108013139/https://github.com/giorgioroth/ContinuumPort) |
| 2026-01-30 09:43:46 | Repository page at 207 commits. Original HTML (`id_`) SHA-256: `5ECBCF3598CC1E66C974847B61C8477D6BB142D5408BFB343410ED848D5FE834`. Between the January captures, 58 commits were made and `README.md` changed 15 times, including the addition of "Author Absence Invariance" on 2026-01-18. | [Wayback capture](https://web.archive.org/web/20260130094346/https://github.com/giorgioroth/ContinuumPort) |
| 2026-08-31 18:37:23 | Raw `AI_Architectural_Thinking.md` from `main`. Per the signed history, the expected content is the version last changed in commit `f3ff21d` (2026-08-08): SHA-256 `1f3b05770fca657c5135d4c71322d288244ac636221f2dcd2c1f948c3199c133`, 408,583 bytes. **Verified 2026-10-10: the archived bytes match this hash exactly.** | [Wayback capture](https://web.archive.org/web/20260831183723/https://raw.githubusercontent.com/giorgioroth/ContinuumPort/main/AI_Architectural_Thinking.md) |
| 2026-08-31 19:03:33 | Blame view of `AI_Architectural_Thinking.md`. Rendered GitHub view: confirm that the capture displays content. | [Wayback capture](https://web.archive.org/web/20260831190333/https://github.com/giorgioroth/ContinuumPort/blame/main/AI_Architectural_Thinking.md) |
| 2026-08-31 18:37:15 | Blame view of `5. WHERE_REGEN_ENGINE_BELONGS.md`. Rendered GitHub view: confirm that the capture displays content. | [Wayback capture](https://web.archive.org/web/20260831183715/https://github.com/giorgioroth/ContinuumPort/blame/main/5.%20WHERE_REGEN_ENGINE_BELONGS.md) |

To reproduce a hash, download the original bytes by adding `id_` after the timestamp, then hash the file:

```
https://web.archive.org/web/<timestamp>id_/<original URL>
```

## 4. DOI registrations

These timestamps are recorded by the registries. They attest the title and creator at registration time, not the content of the work.

| DOI | Short title | Registry | Created (UTC) |
| --- | --- | --- | --- |
| `10.2139/ssrn.6271360` | Structural Bifurcation in Adaptive AI Systems | Crossref | 2026-03-13 18:02:42 |
| `10.17605/OSF.IO/B8SGR` | Trajectory Integrity in Persistent AI Systems | DataCite | 2026-04-28 18:08:59 |
| `10.17605/OSF.IO/M8YBN` | Epistemic admissibility in persistent conversational systems | DataCite | 2026-05-17 10:16:48 |
| `10.17605/OSF.IO/QWF8A` | Execution authority revocation under epistemic divergence | DataCite | 2026-05-18 04:45:44 |
| `10.17605/OSF.IO/W7Q9N` | Adversarial execution governance | DataCite | 2026-05-19 18:01:47 |
| `10.2139/ssrn.6533358` | Execution Control in Persistent AI Systems | Crossref | 2026-07-29 13:18:16 |

Verify through `https://api.datacite.org/dois/<DOI>` and `https://api.crossref.org/works/<DOI>`. All records link the author to ORCID `0009-0006-0616-7241`.

## What does not count as an anchor

- **Archive captures of JavaScript applications** (for example OSF project pages and ORCID profiles) may show an empty page, an error such as "resource not found", or data from a later capture. A capture of such a page can display content that did not exist on its capture date. Do not cite these captures. Archive the platform's API or the raw file instead.
- **Git author and committer dates on commits not made through GitHub's web interface.** These are set by the author's machine and can be changed.
- **Contribution graphs.** They are computed from commit dates and do not identify the repository.

## How to add a new anchor

1. Go to `web.archive.org/save/` followed by the full URL to capture. Prefer raw files (`raw.githubusercontent.com/...` at a specific commit), API endpoints, and PDFs over rendered pages.
2. Copy the resulting URL, which starts with `https://web.archive.org/web/` followed by a timestamp.
3. Download the `id_` version, record its SHA-256, and add a row with the timestamp, what it shows, the hash, and the link.

For a given milestone, the strongest combination is a signed commit (what and when, attested by GitHub), a raw-file capture at that commit (public availability, attested by the Internet Archive), and a matching hash between the two.

## What each type of evidence establishes

- **Internet Archive capture**: the content was publicly retrievable no later than the capture timestamp.
- **GitHub web-flow signed commit**: GitHub created the commit with this content at this time. The timestamp is set and signed by GitHub.
- **DKIM-signed email from GitHub**: GitHub reported this event at this time. The signature covers the date, the subject, and the body.
- **DOI registration (DataCite, Crossref)**: a work with this title and creator was registered at this time.
- **Preprint platform metadata (SSRN, OSF)**: the platform's own record of deposit and availability. Submission and public-availability dates can differ and should be stated separately.

No single type establishes content, authorship, timing, and public disclosure at once. Where two independent types agree on the same event, the timeline is corroborated rather than merely asserted. Two such agreements are recorded above: the January captures bracket commit `2580485b` (timing), and the 2026-08-31 raw capture matches the GitHub-signed history byte for byte (content).
