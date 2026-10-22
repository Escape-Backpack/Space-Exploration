---
id: AS-043
title: Canadarm mixed-clue observation page mockup
type: asset
status: candidate
kind: print
for: PP-010
tool: ReportLab / native Handlee / vector diagrams / Poppler
file: assets/canadarm-observation-bob-v4.pdf
links: []
superseded_by: AS-056
tags: []
---

## Next revision requested - 2026-10-22
Current PDF remains the earlier mockup. PZ-011 now stores the designer's new
makeshift-Canadarm opening and "This is the start position." caption. PP-014 stores
the new A/B/C part labels. Remove the old explicit opening readout instruction when
rebuilding; the designer is still writing the remaining note. No new PDF yet.

## Signed Bob mockup - 2026-10-22
Adds Bob at the bottom in real Handlee 12 pt. The checkpoint line/box moved up
slightly to leave space. Other prose, diagrams and clues unchanged. Local output:
output/pdf/canadarm-observation-v4-bob/Canadarm_Observation_Page_4x6.pdf and the
companion Canadarm_Observation_Page_Letter.pdf. Builder:
source/build_bob_canadarm_observation_v4.py. Prior unsigned v3 preserved.
Current Studio PDF/preview/letter copy updated and byte-verified. Extracted text
matches prior copy plus exactly one native Handlee 12 pt Bob. Both renders reviewed.
This remains only the start/Test 1 mockup; no new gameplay approval or physical test.

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
