---
id: AS-003
title: Galileo sky map artwork
type: asset
# idea | candidate | decided | built | parked
status: candidate
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-005
# Generator or tool used
tool: OpenAI ImageGen built-in
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/galileo-sky-map-player-v1.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-001]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Current player draft

File: `assets/galileo-sky-map-player-v1.png`.

Generated on 2026-10-04 from the base map, then refined to soften numeral ink.
The player draft contains the four object-associated digits specified by PZ-001
and ten scattered decoys beside ordinary background stars. All digits use the
same subdued ivory styling; there are no solution callouts, object labels or
code panel. The unnumbered base and annotated solution are preserved separately.

Screen inspection counted fourteen visible numeral glyphs: the four answer
digits match PZ-001, and the ten decoys read 3, 9, 0, 5, 6, 1, 3, 9, 0, 5.
Jupiter retains four moon dots. Numerals remain readable in the full-resolution
screen image. ImageGen's requested pixel size is not an exact measured font size;
do not assume they are 2 pt or readable only through the magnifier.
Final print size, physical print legibility and magnifier difficulty are untested.
The asset remains candidate pending print review.

Exact player edit prompt (OpenAI ImageGen built-in; base map as edit target):

```text
Use case: precise-object-edit.
Asset type: PLAYER puzzle map with hidden search digits, landscape 3:2.
Input image: the supplied unnumbered Galileo sky map is the EDIT TARGET. Preserve its artwork.
Primary request: add exactly FOURTEEN tiny, crisp, readable single Arabic numerals to the existing sky map. Four are the answer digits, ten are decoys. This is a magnifier-search puzzle: all fourteen digits must have IDENTICAL subdued ivory ink, tiny size and weight, no highlighting or hints as to which count.
Digit styling: very small but clean simple upright sans-serif numerals, approximately 8 pixels high in a 1536x1024 image, each occupying less than 1% of the image height. They should blend into the small star details at normal viewing size but remain recognisable on a zoomed close inspection. No large numerals. Avoid ornate, cursive, ambiguous or smudged glyphs. All digits must be equally sized and visible. No shadows, circles, leader lines, glow, coloured highlights, labels or extra markings.

Positions given below refer to the existing 1536x1024 reference image; if output resolution differs, use the corresponding proportional positions. Four correct object-associated digits:
- "8" at approximately x=433, y=286, in dark sky immediately to the right of the cratered crescent Moon, not over its surface.
- "7" at approximately x=1315, y=247, in dark sky immediately to the right of Venus.
- "4" at approximately x=591, y=720, in dark sky immediately to the right of Saturn's outer ring.
- "2" at approximately x=1160, y=831, in dark sky immediately below Jupiter's lower edge. Keep Jupiter's existing FOUR moon dots unchanged; never turn them into digits.

Ten decoy numerals placed individually near ORDINARY stars in the background, far from all four celestial objects and Jupiter's moon dots, at these scattered locations:
"3" near (105,92);
"9" near (680,108);
"0" near (967,126);
"5" near (1450,373);
"6" near (85,481);
"1" near (667,405);
"3" near (840,702);
"9" near (635,910);
"0" near (273,910);
"5" near (1450,910).
Each decoy is adjacent to a normal background star with a tiny gap and the same typography as the correct digits. Keep the random irregular spread; no deliberate grid or separate row.

Invariants: keep the original celestial objects, exact four Jupiter moons, star chart geometry, constellation connections, frame, background, colours, texture, dimensions, and composition unchanged. Add only the fourteen specified tiny numerals. No letters, names, planet labels, dates, title, "solution", code panel, sequence, watermark or additional numbers. Do not write "8247" anywhere; only the separated object digits specified above. Do not show the discovery order.
```

Exact refinement prompt (OpenAI ImageGen built-in; first numbered output as edit target):

```text
Use case: precise-object-edit.
The supplied numbered player sky map is the EDIT TARGET. Make ONE targeted change: reduce the visual prominence of ALL fourteen existing digit glyphs equally. Keep every digit's identity and exact location unchanged, and keep ALL the rest of the image unchanged.
Scale every digit glyph to about 55% of its current linear height and width, around 7-8 pixels high on this 1536x1024 canvas, centered at its current location. Also dim the digit ink to a subdued medium warm grey-ivory, about 65% of its current brightness. Keep each numeral sharply formed and readable when zoomed in, not blurred, not smudged, not replaced with a dot. Remove the larger old glyph fully at each location; no ghost outlines or duplicate digits.
The object-adjacent digits must remain "8" beside the Moon, "7" beside Venus, "4" beside Saturn and "2" below Jupiter. The ten background decoys remain the exact same existing glyphs at their existing locations. The final total is FOURTEEN single digits, no more and no fewer.
Invariants: preserve the original star map, four celestial objects, Jupiter's exactly four moon dots, frame, stars, constellation lines, grid, colours, texture, composition and output dimensions. No new text, no highlighting, no labels, no code key, no additional stars or numbers. This is the player image for a magnifier-search puzzle, so digits must blend subtly into the little star details rather than stand out at ordinary viewing size.
```


## Base artwork (preserved)

Generated on 2026-10-04 as a base illustration for PP-005. This is an artwork
proposal, not a finished playable map or an approved print layout. The four
objects are scattered outside discovery order, so the artwork does not supply
the code sequence visually.

The base draft deliberately has no hidden digits or decoy digits. The designer
selected the code on 2026-10-04 (recorded in PZ-001); intended print size remains pending.
Use PZ-001 and PP-005 for the puzzle requirements, rather than treating this
artwork as a new puzzle decision.

## Visual review

Screen inspection shows a cratered crescent Moon, Venus, ringed Saturn, and
Jupiter accompanied by four distinct moon dots. No labels or numbers are visible.
Physical print legibility, magnifier readability and playability are untested.

## Designer solution companion

File: `assets/galileo-sky-map-solution-v1.png`.

Created on 2026-10-04 using the base map as the edit target. This companion
uses large coral-circled answer callouts and a central solution key. Screen
inspection confirmed each callout and the displayed code match PZ-001.
It is a designer solution illustration, not a completed player puzzle or a
physical magnifier test. The asset's player-facing `file` is the numbered player draft.

Exact solution edit prompt (OpenAI ImageGen built-in):

```text
Use case: precise-object-edit.
Asset type: designer-only SOLUTION version of the supplied Space Exploration Galileo sky map.
Input image: the supplied map is the EDIT TARGET.
Primary request: preserve the original map artwork, landscape aspect ratio, navy sky, ivory/gold chart lines, all stars and constellations, frame, textures and celestial objects. Add only clear solution annotations.
Exactly four answer digits, paired with the correct celestial objects:
- MOON in the upper-left: digit "8".
- JUPITER with four moon dots in the lower-right: digit "2".
- SATURN with rings in the lower-left: digit "4".
- VENUS in the upper-right: digit "7".
Place each digit in adjacent dark sky, close enough to its object that association is unmistakable, without covering the object. Each digit is a large crisp white sans-serif numeral inside a thin bright coral-pink circular highlight. A short coral-pink leader line connects its circle toward the object. These are answer callouts, visually distinct from all existing ivory stars. Put the matching small white object name below each callout circle, verbatim "MOON", "JUPITER", "SATURN", "VENUS".
In the central dark open area, add a small neat dark-navy opaque solution-key panel with a thin coral border. Its exact three lines read:
"SOLUTION"
"Moon 8 → Jupiter 2 → Saturn 4 → Venus 7"
"CODE 8247"
Keep the panel reasonably small so it does not cover any object. Text must be exact and easily readable. This is a solution explanation, not the player map.
Constraints: do not move or redraw the four celestial objects; keep Jupiter's exactly four moon dots intact. Do not change planet shapes, sky layout, colours or frame. Do not add other digits, dates, decoys, planets or any other text. No watermark. Ensure associations and ordered code are correct: 8-2-4-7.
```

## Exact generation prompt

Reference image (style only): `brand/Space_Exploration_Backpack_Scene_v1.png`.

```text
Use case: scientific-educational.
Asset type: flat printable sky-map illustration for the second lock of the Space Exploration escape-game backpack.
Input image: supplied Space Exploration cover is a STYLE reference only: polished hand-drawn digital illustration, midnight navy, restrained warm ivory and antique brass accents. Do not copy its room, backpack or props.
Primary request: create the sky-map artwork itself, straight-on, edge-to-edge, landscape 3:2. A richly illustrated yet readable old astronomical chart, a deep navy blue star field on subtly worn paper, a fine understated warm ivory border and faint celestial chart arcs. No paper mockup, desk, perspective, folds or shadows.
Subject: exactly FOUR recognisable celestial object illustrations, scattered organically around the star field without a row, numbered sequence, obvious clockwise order or equal-size panels: a cratered crescent MOON in the upper-left quadrant; a cream-coloured VENUS sphere with a subtle crescent illumination in the upper-right quadrant; a gold SATURN with clear rings in the lower-left quadrant; a subtly banded JUPITER in the lower-right quadrant accompanied by exactly FOUR distinct tiny ivory moon dots, easily distinguishable from nearby stars. The Moon should read as cratered and Venus should be smooth. Give each object enough adjacent dark space to later place a tiny hidden digit. Objects are small illustrations embedded in a star chart, not huge planets filling the poster. Keep Jupiter's four moon dots locally grouped, with no other background stars immediately beside Jupiter to confuse their count.
Background: many small crisp ivory-white stars and a few understated thin constellation connections distributed irregularly, enough visual clutter for a future magnifier search without becoming a dense galaxy photograph. Very faint chart lines must stay subordinate. Light aged texture but no heavy distress. Keep the sky behind objects dark and clean enough for precise tiny print text later.
Constraints: this is an illustrated puzzle chart of celestial symbols, not an accurate simultaneous sky observation or orbital diagram. Do not encode discovery chronology visually. NO digits yet, NO letters, NO labels, NO dates, NO words, NO compass letters, NO logos, NO watermark. No extra planets or suns. No decorative faces. No coloured constellation groups. No globe or astronaut. Keep a generous clear trim margin and all four objects within it.
```
