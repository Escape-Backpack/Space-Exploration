---
id: AS-010
title: Sky observation page layout - 4 x 6 inch draft
type: asset
status: decided
kind: print
for: PP-010
tool: ReportLab / Poppler
file: assets/observation-pages/Observation_Page_4x6_Draft_v1.pdf
links: []
superseded_by:
tags: []
---

## Files
- [Exact-size draft](assets/observation-pages/Observation_Page_4x6_Draft_v1.pdf)
- [Letter print sheet](assets/observation-pages/Observation_Page_Letter_Print_v1.pdf)
- [Preview](assets/observation-pages/Observation_Page_4x6_Draft_v1.png)
- [Reproducible source](source/build_observation_page_v1.py)

## Construction
Deterministic vector form, authored with ReportLab using the locally available IBM
Plex Mono fonts. No ImageGen prompt or generated illustration. PP-010 holds the layout
specification and unresolved design choices. PDF title/field text is selectable; fonts
are embedded. The letter sheet puts all instructions and crop marks outside the card.

## Verification - 2026-10-21
Both PDFs have one page. Exact-size media box: 288 x 432 pt; letter media box: 612 x 792 pt.
Expected header and field text extracted successfully. Both pages were rendered with
Poppler and visually reviewed: no overlap or clipping. No physical print or puzzle test.

## Selection - 2026-10-21
The designer selected this layout for use. Existing files keep their draft filenames
for link stability; the blank layout is approved, with no physical print or puzzle test.
