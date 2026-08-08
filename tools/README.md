# tools/

Build recipes for the manuscripts in this repository.

## Why these files exist

The Markdown in this repository is written for readers on GitHub. An EPUB needs
transformations that do not belong in the manuscript: heading shifts, removal of
the title block the generated title page already carries, removal of section
rules that fall at file boundaries, and explicit line breaks where the prose
depends on them.

Those transformations previously lived only in an operator's memory. The result
was a published edition that had diverged from its own source: six chapter
titles missing and welded into the preceding chapter, six 21-byte files reading
`Host not in allowlist` in place of figures, and a sentence present in the
shipped book but absent from the manuscript. The first two made the file fail
EPUB validation while it was on sale.

`build_epub.py` is that recipe, written down.

## Contents

| File | Purpose |
|---|---|
| `build_epub.py` | The build. One config block per title. |
| `pcra_stylesheet.css` | The 647-byte stylesheet of the published *Parent–Child Relationship Arithmetic*. Kept so a rebuild does not silently restyle the whole book. |
| `aat_line_breaks.json` | Author decisions on which folded line groups keep their breaks in *AI Architectural Thinking*, keyed by content hash so they survive edits elsewhere in the file. |

## Usage

```
pip install --break-system-packages lxml
python3 tools/build_epub.py aat     # AI Architectural Thinking
python3 tools/build_epub.py pcra    # Parent-Child Relationship Arithmetic
```

Requires pandoc >= 3.1.

## Validating

```
java -jar epubcheck.jar --usage <file>.epub
```

`--usage` also reports optional-practice hints. A clean build is
`0 fatals / 0 errors / 0 warnings / 0 infos / 0 usages`.

EPUBCheck confirms conformance. It does **not** confirm that a build preserved
the previous edition's stylesheet, metadata, or resource inventory — a rebuild
that silently drops three `dc:subject` entries and changes the typography still
validates clean. Compare those separately, and state which artifact you
compared against. A diff without a named baseline is not a diff.

## Covers

No cover is embedded. KDP charges delivery per MB per copy sold, deducted from
royalty; the cover uploads separately in its own KDP field as TIFF. The KDP
previewer will warn that the file has no cover. That warning is the intended
outcome.

## When the build stops

The script fails rather than continuing if a rewrite rule no longer matches
exactly one line, or if an approved line-break block has vanished from the
source. Both mean the manuscript changed underneath a decision. Review the
decision; do not loosen the rule.

## Known divergence

The published edition of *AI Architectural Thinking* reads
"documented on the author's blog." The canonical manuscript still carries a
hyperlink whose anchor text is "Blog", which reads as "documented at Blog" once
links are stripped. A rewrite rule in `build_epub.py` reproduces the shipped
wording; it is marked `DIVERGENCE, pending resolution` and should be deleted
once the sentence is corrected in the manuscript.
