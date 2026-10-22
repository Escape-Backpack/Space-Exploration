---
id: AS-028
title: Handlee uncle observation note - current 4 x 6 PDF
type: asset
status: built
kind: print
for: PP-010
tool: ReportLab / embedded Handlee TTF / Poppler
file: assets/space-constellation-note-bob-v6.pdf
links: []
superseded_by:
tags: []
---

## Signed Bob edition - 2026-10-22
Adds the requested Bob signature in Handlee 12 pt at the end. Existing prose,
drawings, 4 x 6 size and 6 mm margins unchanged. Local production files are now
output/pdf/uncle-note-v6-bob/Uncles_Observations_4x6.pdf and
output/pdf/uncle-note-v6-bob/Uncles_Observations_Letter.pdf. Rebuild with
source/build_bob_constellation_note_v6.py. Earlier v5 output is retained history.
Current Studio file/preview/letter-copy records point to the uploaded signed files.
Extracted text verified as old copy plus exactly one Bob; all three signature
glyphs verified as native Handlee 12 pt. Both renders visually reviewed.

## Studio-hosted file - 2026-10-21
The current PDF is uploaded to Studio file storage and verified byte-for-byte
against output/pdf/uncle-note-v5-handlee/Uncles_Observations_4x6.pdf. Local production output remains unchanged.
The file field now points to the Studio-served asset so the online download works.


## Selected real font implemented - 2026-10-21
Designer accepts this edition and confirms it belongs to the first puzzle (PZ-002),
superseding earlier second-puzzle positioning. Physical playtest is still pending.

Designer selects option 4, Handlee, from AS-027. PR-007 stores this selection.
Rebuilt the note with real embedded native text, retaining the exact AS-026 prose,
relative night order and two original pencil drawings. No ImageGen lettering.

Body: Handlee Regular, 12 pt, 14.4 pt line spacing, 6 mm side margins. Text wraps
around the telescope on the right and the alignment-corner drawing at bottom left.
Form: IBM Plex Mono Medium 12 pt heading, IBM Plex Mono 8.5 pt field labels.
Date/time/location fields remain blank. No new puzzle order, answer or diagram count.

Exact 4 x 6 inch PDF and companion letter printing PDF with crop marks:
output/pdf/uncle-note-v5-handlee/Uncles_Observations_Letter.pdf.
Same directory contains PNG previews, typography.json and README. Print letter
version at 100% / Actual size, then trim. Handlee font/OFL licence retained at
source/fonts/handwriting-candidates/handlee/; no system-wide font installation.

Builder: source/build_handlee_uncle_note_v5.py. Text source remains
assets/uncle-note-v4/note-text.txt. Both drawings are separate PDF clipped placements
of the unchanged assets/uncle-note-v4/Handwritten_Body.png source; hidden surrounding
generated lettering is clipped away and not used as visible prose.

## Verification
Extracted Handlee characters match the approved prose exactly, ignoring layout
whitespace. All body glyphs verified at 12 pt. Exact page sizes/native text bounds
and absence of sketch/text intersections checked. Both PDFs rendered with Poppler
and visually inspected. Physical legibility and player testing remain pending.
PZ-002 test_status stays untested; no chart/frame geometry changes.
