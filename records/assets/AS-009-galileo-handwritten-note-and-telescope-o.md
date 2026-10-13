---
id: AS-009
title: Galileo handwritten note and telescope optics
type: asset
# idea | candidate | decided | built | parked
status: candidate
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-007
# Generator or tool used
tool: OpenAI ImageGen built-in
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/galileo-note-and-lens-diagram-v1.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PR-007, Q-007, Q-004]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Draft note
Created on 2026-10-05 for PP-007 after the designer requested all information
on one handwritten note with a hand drawing. Exact player text lives in PP-007.
Q-007 records the note-only choice; Q-004 holds the sourced chronology.
This image and wording are candidate for review, not an approved physical prop.

Style reference: `assets/luggage-tag-back-note-telescope-v1.png` (AS-008),
handwriting and paper only. PR-007 specifies the handwriting.

## Visual review
Full-resolution screen review checked the introduction, four month/year
observation blocks, captions, labels and ending against the prompt. The blocks
are displayed July, November, December, January; players must sort their dates.
No answer code is shown.

The diagram shows a convex objective and concave eyepiece, with the latter
before the converging bundle meets; output rays are approximately parallel.
It is a qualitative on-axis bundle sketch, not a quantitative demonstration
of angular magnification or a dimensioned optical prescription. No lens focal
lengths, print size or instrument magnification were invented. Print legibility
and a physical puzzle solve remain untested.

Historical/optics sources:
- [Rice University Galileo timeline](https://galileo.library.rice.edu/chron/galileo.html)
- [Museo Galileo telescope](https://catalogue.museogalileo.it/object/GalileosTelescope.html)

## Exact generation prompt
Built-in OpenAI ImageGen, supplied AS-008 V1 as a style reference.
```text
Use case: scientific-educational.
Asset type: complete portrait handwritten uncle's note for a Space Exploration escape backpack, containing all four Galileo observations and a hand-drawn telescope optics diagram.
Reference image: provided luggage-tag note is a handwriting STYLE reference only. Match its tidy natural mixed-case engineer's hand printing and warm ivory paper. Do not copy the greeting, its note wording, its tripod illustration or its landscape layout.
Create one high-resolution PORTRAIT page, flat straight-on and edge-to-edge, 2:3 aspect ratio, with substantial trim margins. Clean ivory paper, dark midnight navy handwritten text and disciplined navy/graphite technical pen sketch lines. Make all handwriting large and comfortably legible. Natural slight pen variation, neat spacing, no cursive and no typeset font.
Composition: a complete personal notebook page. At top, the exact two-sentence introduction. Below it, a small handwritten heading "Galileo's observations". Below, FOUR dated observations in a spacious 2-by-2 group, each a short handwritten paragraph with its date slightly emphasized. Keep their displayed order EXACTLY the supplied order below (not chronological, so players must consider the dates). No bullet numbers. Then a large clean hand-drawn Galilean telescope ray schematic in the lower-middle of the page. Below, exact concluding note at bottom. All the content on this single sheet; no other card needed.
Exact introduction:
"One of the great advances in exploring the sky came from Galileo. It is incredible what he achieved with his telescopes!"
Exact four observations, displayed row-major in this order:
Top left: "July 1610 - Saturn appeared to have two smaller bodies beside it."
Top right: "November 1609 - He saw mountains and craters on the Moon."
Bottom left: "December 1610 - He confirmed that Venus changes phases like the Moon."
Bottom right: "January 1610 - He discovered four moons orbiting Jupiter."
All four planet/object names and every date MUST be readable, unambiguous and spelled exactly. No added observation, no omission, no rewritten prose.
Drawing specification: scientifically coherent schematic of a GALILEAN refracting telescope viewed from the SIDE, not the existing tripod illustration. Two lenses and three rays: ONE large convex converging objective lens on the LEFT; ONE small concave diverging eyepiece on the RIGHT; a small eye further to the right. Sketch a very faint simple tube outline around the two lenses, open so the optics are readable. An axial bundle of exactly THREE horizontal parallel rays arrives from the left. The upper and lower rays bend inward at the convex objective; centre ray stays straight on the axis. Place the concave eyepiece BEFORE those rays meet, while they still converge. At the concave lens bend the top/bottom rays back outward enough to EXIT PARALLEL AND HORIZONTAL, closer together than the incoming bundle, heading to the eye. The rays MUST NOT cross inside the telescope. Smooth simple thin single-line rays with small directional arrowheads pointing left-to-right. No imaginary real image between the lenses, no second convex lens, no extra lens, no mirrors, no focal-length dimensions or equations. This is an on-axis ray-bundle schematic, not a to-scale optical engineering prescription.
Handwritten diagram heading exactly "How the telescope works".
Only these diagram labels with accurate leader lines: "Objective lens (convex)" pointing to the LEFT bulging lens; "Eyepiece (concave)" pointing to the RIGHT narrow-waisted lens; "Light rays" pointing to incoming rays; "Eye" pointing to the eye.
Handwritten caption under the diagram, exactly: "Magnification reveals small details."
Exact concluding text:
"I love following his discoveries through time. A good lens can reveal details that are easy to miss."
Constraints: entire note fits with generous readable spacing. No greeting, no signature, no logo, no code, no hidden answer numbers, no digits other than the supplied dates, no extra text, no unrelated planet sketches, no decorative stars, no watermark, no frame or perspective. Do not add 8247 or any solution digits. Preserve warm personal handwriting style and technical clarity. No graphite-only faint redesign: the user selected the original note's confident dark pen character.
```
