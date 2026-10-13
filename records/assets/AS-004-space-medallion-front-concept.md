---
id: AS-004
title: Space medallion front concept
type: asset
# idea | candidate | decided | built | parked
status: decided
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-003
# Generator or tool used
tool: OpenAI ImageGen built-in
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/space-medallion-front-concept-v1.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Front artwork proposal

Created on 2026-10-05 for PP-003. The concept shows a telescope, crescent Moon,
orbital arc, three stars and a circular border in yellow relief on a navy body.
Selected by the designer on 2026-10-05 ("Good", then request to recreate the STL).
AS-006 holds the manufacturing model. No physical test is implied.

This PNG is a front-face concept preview, NOT an STL, vector relief profile or
dimensionally verified manufacturing drawing. The 50 mm reference and relief
language in the prompt come from the Norse medallion in the shared kit. They
are design references, not new approved Space dimensions. Shading/texture in the
image are illustrative. The smallest gaps and shapes require geometry and
printability review before a physical medallion can be made.

Screen review: one front face, navy/yellow appearance, telescope/Moon/orbit motif,
no text, no suspension hole, and no back design. Physical printing is untested.

## Exact generation prompt

Built-in OpenAI ImageGen. Style reference:
`../EscapeBackpack/NorseBackpack/Props/Medallion/Medallion_v2_Preview.png`.

```text
Use case: product-mockup.
Asset type: FRONT-FACE ART CONCEPT for Space Exploration's circular 3D-printed keepsake medallion.
Input image 1: Norse medallion reference, use ONLY its bold raised heraldic crest and medallion design language, not its raven, shield, compass, text or grey colour.
Primary request: one round SPACE EXPLORATION medallion FRONT shown straight-on from directly above, centred on a plain warm ivory background. Single face only, no reverse side, no split panels, no text. A dark midnight-blue circular body with warm bright YELLOW raised details, exactly two material colours. Flat 0.6 mm raised relief character, like a two-filament 3D print, not a sculpted metallic coin.
Subject: a substantial classic astronomer's telescope on a simple stout tripod, tilted diagonally upward toward a bold crescent Moon in the upper-right of the circle. A clean sweeping orbital arc curves around this central composition, uniting "looking at the sky" and "travelling beyond". Two or three restrained four-point star ornaments balance the remaining spaces. A thin but sturdy raised circular border frames the emblem, well inset from the edge. The telescope, Moon, arc and stars are ALL the same solid yellow material on navy. No rocket, spaceship, landscape or people.
Composition: strong emblem silhouette and clear negative spaces, fills the face with a balanced crafted keepsake feel. Designed to translate later into a two-colour 50 mm diameter relief: thick strokes, substantial separated shapes, broad telescope tube and tripod, minimal tiny details. Keep all emblem shapes inside the circular rim. Do not add lettering, tiny etched dots, dense star fields or hairline ornament.
Materials/light: subtle matte filament surface and very restrained top-left lighting only to show low raised edges. Yellow is yellow plastic, not bronze or gold metal. Navy body remains clearly blue. Crisp face edges, no perspective tilt. This is a concept image, not manufacturing geometry.
Constraints: NO text, letters, dates, numbers, labels, watermark, suspension loop, hole, chain, hands, packaging, mockup scene or extra medallions.
```
