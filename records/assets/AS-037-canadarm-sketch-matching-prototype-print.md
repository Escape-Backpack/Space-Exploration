---
id: AS-037
title: Canadarm sketch-matching prototype print pack
type: asset
status: candidate
kind: print
for: PP-013
tool: ReportLab / Shapely / Poppler
file: assets/canadarm-sketch-prototype-v1.pdf
links: []
superseded_by:
tags: []
---

## Selected approach and proposed implementation
User selects sketch matching for PZ-011. This assistant prototype proposes four
tests. Each gives a shoulder/elbow partial view and elbow/hand partial view with
matching elbow E and common UP orientation. Combine the views, reproduce the pose
with PP-014 mounted on PP-013, then read the digit inside its hand. No angle values
or calculations appear on player pages. Small joint labels S/E/W identify anatomy.

Five mixed-size pages: letter board, letter arm cutting sheet, two 4 x 6 observation
notes, letter designer key. Handlee 11.5/12 pt prose with IBM Plex Mono form labels.
Keep key out of player materials; print all pages 100% / Actual size. Candidate
extraction 5938 is a construction choice for review, not an approved answer. PZ-011
answer remains blank and publish_hints stays no.

Source: source/build_canadarm_sketch_prototype_v1.py; exact geometry/decoys and
internal construction angles: output/pdf/canadarm-sketch-v1/geometry-audit.json.
README and five PNG renders are alongside. Deterministic vector art, no ImageGen.
Two proposed observation-page texts are in the builder and visible in the PDF.

## Checks and limits
Four forward-constructed arm poses stay on board; intended target centres are
separated by more than 60 pt; no other numbered centre within 36 pt of any intended
reading centre. PDF page sizes, native text bounds, labels and test numbers checked.
All five pages rendered and visually reviewed; crowded joint labels repositioned.
These checks do not establish physical/perceptual unique fitting, difficulty or
player success. Joint slack/friction, cutting, pin-hole sizes and small diagram
legibility remain untested. No physical or player pass; candidate artwork only.
