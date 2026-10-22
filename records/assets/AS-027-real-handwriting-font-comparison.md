---
id: AS-027
title: Real handwriting font comparison
type: asset
# idea | candidate | decided | built | parked
status: candidate
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-010
# Generator or tool used
tool: ReportLab / actual Google Fonts TTF files / Poppler
# Path from the project folder once made, e.g. assets/star-chart.png
file: output/pdf/font-comparison/Handwriting_Font_Comparison.pdf
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Designer selection - 2026-10-21
Designer chooses option 4, Handlee. PR-007 is the authoritative selected font
record; AS-028 is the rebuilt native-text note. The comparison sheet remains a
reference asset rather than the production note.

## Actual font comparison - 2026-10-21
User requests real installable fonts that match the selected Engineer's notebook
appearance. One letter page compares Patrick Hand, Architects Daughter, Kalam and
Handlee, using identical note excerpts at 14 pt regular weight. Additional character
samples use 12 pt. This is real embedded/selectable font text, not ImageGen lettering.

Patrick Hand is the assistant recommendation for readability; Architects Daughter
is the technical-notebook alternative. These are subjective recommendations for
review, not a new designer selection. PR-007 style and current note remain unchanged.

Fonts and OFL.txt files downloaded directly from the official google/fonts GitHub
repository into source/fonts/handwriting-candidates/. Exact download URLs are in
output/pdf/font-comparison/font-sources.json. No system-wide font installation.
Every downloaded licence verified as SIL Open Font License. Retain those files
when redistributing fonts. No font has been chosen for production yet.

Builder: source/build_handwriting_font_comparison.py. PNG preview beside the PDF.
One-page letter size, four names and native text bounds checked. Poppler rendering
visually inspected. No physical font/print legibility test or note-layout change.
