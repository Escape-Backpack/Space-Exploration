---
id: AS-043
title: Canadarm mixed-clue observation page mockup
type: asset
status: candidate
kind: print
for: PP-010
tool: ReportLab / native Handlee / vector diagrams / Poppler
file: assets/canadarm-mixed-clue-observation-4x6.pdf
links: []
superseded_by:
tags: []
---

## First-page layout mockup - 2026-10-22
User asks to see the mixed-clue concept on a Sky Observations page. This candidate
4 x 6 page shows only the start and Test 1. Later tests would continue on other
observation pages; it is not the complete Canadarm clue log or a new packing choice.

Established form header, warm Handlee introduction, full starting pose and blank
first-reading box. Test 1 gives a 60-degree CCW elbow sketch, followed by the prose
clue about compensating at the wrist by the same amount in the opposite direction.
A second blank box is explicitly after both moves. No answer digits or fabricated
date/time/location. Labelled base and UP preserve orientation. Starting drawing
keeps the checked link proportions at uniform 0.6 scale.

The full revised board and usable printed angle dials still need engineering;
the earlier printable board is not matched to the new sequential movements.
These page details/wording are assistant proposals for review, not newly approved.

## Files and typography
Exact-size PDF plus letter-print crop-mark version:
output/pdf/canadarm-observation-v3/Canadarm_Observation_Page_Letter.pdf.
PNG previews and README alongside. Print at 100% / Actual size; final card 4 x 6.
Builder source/build_canadarm_observation_mockup_v3.py. All real embedded Handlee
and IBM Plex Mono text, all diagrams native vector paths; no generated lettering.
Body 12/11.5 pt, notebook headings 13 pt, sketch labels 8.5 pt. Existing form unchanged.

## Checks and limitations
Both single-page PDFs dimension/text bounds checked, expected clue words and degree
glyph extract correctly; Handlee verified in native text. Both rendered with Poppler
and visually inspected. Angle arc is CCW from horizontal to 60 degrees; wrist prose
implies the opposite turn. Native text/diagram spacing reviewed. No physical
small-print, pencil-line visibility or player-interpretation test. PZ-011 untested.
