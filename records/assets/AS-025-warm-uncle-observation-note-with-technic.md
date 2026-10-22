---
id: AS-025
title: Warm uncle observation note with technical sketches
type: asset
status: candidate
kind: print
for: PP-010
tool: OpenAI ImageGen built-in / ReportLab / Poppler
file: output/pdf/uncle-note-v3/Uncles_Observations_4x6.pdf
links: []
superseded_by: AS-026
tags: []
---

## Revised second-puzzle note - 2026-10-21
Designer rejects the terse AS-022 note and asks for a warmer tone, sketched diagrams,
the selected handwriting, and an opening about observations over different nights.
Designer specifies this constellation activity is the second puzzle, not the opening.

New candidate prose follows that opening with a personal wish to share the sky,
reference-star pairings, frame alignment/counting guidance and an encouraging signoff.
The candidate text is visible in the generated artwork and exact generation prompt.
Date/time/location deliberately blank. No exact dates or final order/code invented.
Q-009 remains the selected dated-observation ordering approach; this reference note
does not finish the separate dated count-order clue.

## Style and files
Handwriting matches only the centre Engineer's notebook column of AS-007 per PR-007:
tidy open mixed-case hand printing, not cursive. The previous Nothing You Could Do
substitute was not the selected handwriting and is not used here. No installable
typeface is newly selected. The printed observation header retains IBM Plex Mono.

ImageGen source: assets/uncle-note-v3/Handwritten_Body.png. Style reference:
assets/handwriting-and-technical-sketch-styles-v1.png, centre column only.
Exact generation prompt: assets/uncle-note-v3/generation-prompt.txt.
Reproducible PDF placement: source/build_warm_uncle_note_v3.py.
Companion letter-print PDF: output/pdf/uncle-note-v3/Uncles_Observations_Letter.pdf.
Same directory contains PNG page previews and print README. Print letter version at
100% / Actual size, then trim at the crop marks to 4 x 6 inches.

Two small graphite sketches: telescope and one marked alignment corner with a single
star. Neither depicts full target membership or supplies the three count answers.

## Verification and limits
Generated wording read visually against prompt; all three pairings correct. No answer
numbers or invented observation dates. Full note and letter PDF rendered with Poppler,
visually inspected; exact page sizes and native text bounds checked. Physical print,
small-text legibility and player interpretation are untested. Text is candidate for
designer review. No chart/frame geometry changed. publish_hints stays no on PZ-002.
