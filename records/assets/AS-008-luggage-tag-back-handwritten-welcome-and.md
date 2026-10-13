---
id: AS-008
title: Luggage tag back - handwritten welcome and telescope
type: asset
# idea | candidate | decided | built | parked
status: decided
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-008
# Generator or tool used
tool: OpenAI ImageGen built-in
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/luggage-tag-back-note-telescope-v1.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PR-007]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Purpose and status
Generated on 2026-10-05 for the reverse of PP-008, following the designer's
approved note and vintage telescope request. The exact approved note lives in
PP-008. After comparing the finer graphite version, the designer chose to keep
the original V1 on 2026-10-05. V1 is the selected artwork. V2 remains an unselected
alternative at `assets/luggage-tag-back-note-telescope-v2.png`.
This selection supersedes the proposed line-weight refinement for the tag.
Physical print testing remains pending; approval is of the visual design.

Reference: `assets/handwriting-and-technical-sketch-styles-v1.png` (AS-007),
centre column only; selected handwriting specification is PR-007.

## Visual review
Inspected the full-resolution generated image. The rendered note matches the
approved words and punctuation, including "Hello nibling!" and "re-kindle".
A fine-line vintage refractor and three-legged tripod occupy the right side;
the note is separate on the left, with no added labels, signature, codes or QR.
The upper-left corner is clear for the reverse-side strap-hole area.
No telescope model identification or technical accuracy certification is claimed.
Physical dimensions, hole size/alignment, trimming and printed readability
are untested. No print PDF was requested or made.

## V2 graphite refinement (2026-10-05)
This experiment was superseded by the designer's selection of original V1.
Its files and exact prompts are retained as an alternative and revision history.
Edited v1 in two built-in ImageGen passes. First pass converted the telescope
to graphite but retained some heavy contours; second pass reduced them further.
Intermediate retained at `source/luggage-tag-back-note-telescope-v2-graphite-pass.png`.
Unselected alternative: `assets/luggage-tag-back-note-telescope-v2.png`.

Screen review: note words, punctuation, line wrapping and main layout retained;
telescope design and tripod retained with visibly finer grey contours and reduced
shading. The generated pixels are not claimed identical outside the drawing.
The 1:5 target is approximate, not a measured stroke-width result. Actual
0.5/0.1 mm widths require a defined final print size and print verification.

### Exact first edit prompt
Target: v1.
```text
Use case: precise-object-edit.
Edit target: supplied luggage-tag back artwork with handwritten note at left and vintage telescope at right.
Make ONE targeted revision: replace ONLY the telescope's ink drawing with a fine graphite-pencil rendering of the SAME telescope and tripod.

Line-weight constraint: handwriting represents a 0.5 mm pen stroke; telescope lines represent a 0.1 mm pencil stroke. Each ordinary telescope contour must therefore be approximately ONE-FIFTH (20%) the visible width of an ordinary handwriting stroke in the same image. This is a stroke-width change, not merely lowering opacity or making the original thick outlines grey. Use extremely fine, clean, antialiased hairlines across ALL telescope parts, including objective rim, tube, eyepiece, clamps, yoke, adjustment wheel, tripod legs, joints, braces and feet. Eliminate heavy dark outer contours and thick black bands. Keep recognisable geometry, not a fuzzy pale ghost. Neutral medium graphite grey, restrained natural pencil grain. Only sparse delicate hatching, each hatch also hairline; avoid accumulated dark filled shading that makes the sketch as heavy as the writing. Construction lines still finer and paler.

Preserve the original vintage refractor design, diagonal tilt, size, position and tripod geometry. Do not redesign, simplify away important parts, add parts, labels, dimension lines, equations, stars or numbers.

Critical invariants: the ENTIRE handwritten note must remain unchanged in words, punctuation, lettering shapes, baseline, line wrapping, position, navy ink colour and stroke thickness. Keep "Hello nibling!" and "re-kindle" exactly. Do not lighten or redraw the writing. Keep paper texture, ivory colour, landscape canvas dimensions, framing, margins, whitespace and upper-left strap-hole clearance unchanged. No new objects or text. Do not move or crop anything.
Return the complete edited luggage-tag back, with the note still confident dark pen and the telescope distinctly finer graphite technical sketch. No mockup, no watermark.
```

### Exact refinement prompt
Target: retained intermediate graphite pass.
```text
Use case: precise-object-edit.
Edit the supplied luggage-tag artwork. Retain the complete note, ivory paper, layout, dimensions, telescope design and geometry exactly. Change ONLY the telescope's line thickness.
The previous graphite pass still has ordinary contours too close to the handwriting width. Thin EVERY telescope contour to an approximately 0.6-to-0.8 pixel antialiased hairline at this supplied image's resolution: objective rim, long tube edges, eyepiece, mounting yoke, adjustment wheel, tripod legs, fittings, braces and feet. ONE extremely fine graphite thread per contour, no dark band around rims, no paired closely touching strokes that form a thick contour. The written note's ordinary strokes are several pixels wide and MUST remain untouched; aim for the telescope's visible strokes to be ONE-FIFTH their width. Reduce actual stroke width instead of merely opacity. Keep neutral graphite grey and enough contrast for the finest lines to remain discernible. Construction guides and sparse hatching must also be hairline and can be lighter. Never compensate with heavy shading.
Do not change any words, punctuation, letter shapes, navy handwriting thickness or line breaks. Do not change telescope size, shape, tilt, position, or vintage three-leg stand. No new text or objects. Return the full edited note-and-telescope artwork, landscape.
```

## Exact original V1 generation prompt
Built-in OpenAI ImageGen, with the local AS-007 comparison as a style reference.

```text
Use case: illustration-story.
Asset type: flat printable BACK artwork of the Space Exploration backpack's luggage tag: an uncle's handwritten welcome plus a hand-drawn vintage telescope.
Reference image: supplied three-column handwriting comparison is STYLE REFERENCE ONLY. Match ONLY the centre column, "2 ENGINEER'S NOTEBOOK": tidy natural mixed-case hand printing, open letterforms, fine dark navy ink, slight natural pen variation. Do not reproduce the comparison layout, headings, solar systems or satellites.
Create one landscape 3:2 artwork, flat straight-on edge-to-edge warm ivory paper. This is the artwork itself, no photograph, no table, no hands, no tag mockup, no outer hole illustration. Restrained subtle paper grain, clean print contrast.
Composition: handwriting is the main subject and must be comfortably legible. Left approximately two-thirds is the personal note, generous line spacing, natural line wrapping. Use the full available height without crowding. Right approximately one-third is a compact finely hand-sketched vintage refracting telescope on a wooden tripod, tilted upward. Keep the drawing separate from the text, with a clear breathing gap. Fine navy ink contours, very light grey construction axes, a little disciplined hatching; classic long telescope tube with a large objective at the upper end and small eyepiece at the other, simple cradle and adjustment fittings, convincing three-legged tripod. This is a generic vintage telescope, no branded or historical model claim. Hand drawn technical notebook character, not a photorealistic painting. No labels, measurements or invented equations.
Preserve quiet margins around all edges. Reserve a small EMPTY top-left corner as reverse-side strap-hole clearance; no words or drawing there. Start the greeting slightly below this corner. Do not draw or encode the hole itself; physical placement will be confirmed separately.
Text, VERBATIM, retaining exact spelling, punctuation, mixed case and the hyphen in "re-kindle":
"Hello nibling! My time in the great Canadian North has been a great experience working on an amazing new space project! It also gave me time to re-kindle my passion for all things space. So I created this adventure, you have to solve puzzles to get to the final prize. Pay attention to details and enjoy!"
Allow line breaks and a blank line after "Hello nibling!" but change NO words. Do not add a signature, title, caption, hint, labels or any extra text. Never typeset the note in a digital font: it must convincingly look like the centre reference's tidy technical handwriting. Avoid cursive, large sweeping strokes, childlike bubble writing, rough scrawl, heavy aging, decorative star patterns, glowing ink, borders, stamps, QR codes, numbers or watermark. The star puzzle artwork belongs on the other face and must not be included here.
Output one complete unclipped note with the telescope sketch. This is a proposed visual rendering of the approved text, not a new puzzle mechanism.
```
