---
id: AS-005
title: Moon and beyond reward ticket
type: asset
# idea | candidate | decided | built | parked
status: candidate
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-004
# Generator or tool used
tool: OpenAI ImageGen built-in
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/moon-and-beyond-reward-ticket-v1.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

## Reward-ticket proposal

Created on 2026-10-05 for PP-004. The artwork is a one-sided navy/yellow/ivory
celestial invitation ticket. Its text and layout remain candidate proposals.
It has no player name, date, seat, gate, barcode or QR code.

Screen review confirmed the displayed title, invitation, signature and completion
stub match the exact prompt below. The wording includes "the Moon and beyond".
No physical print test has been performed.

## Printable companion

File: `output/pdf/moon-and-beyond-reward-ticket-letter-v1.pdf`.

Draft print layout: one 7.5 x 2.5 inch (190.5 x 63.5 mm) ticket on US Letter,
with crop marks, actual-size printing instructions and a one-inch size-check line.
This size is a proposed home-print format, not an approved physical prop dimension.
The 2172 x 724 artwork is placed unmodified at 289.6 effective dpi. The dotted
stub separator is decorative; cutting/perforating it is not required.

Builder: `source/build_reward_ticket_print_v1.py`, using ReportLab.
Validation: one Letter-size page confirmed; rendered with Poppler and visually
reviewed for crop marks, legibility and clipping. Physical print remains untested.

## Exact generation prompt

Built-in OpenAI ImageGen. Style reference:
`brand/Space_Exploration_Backpack_Scene_v1.png`.

```text
Use case: illustration-story.
Asset type: finished FRONT artwork of a printable fictional final-reward ticket for the Space Exploration escape-game backpack.
Input image: Space Exploration cover is a STYLE reference only: polished hand-drawn illustration, welcoming adventure, navy night sky and warm yellow accents. Do not include the room, backpack, telescope or tabletop.
Primary request: create the ticket graphic itself, flat straight-on and edge-to-edge on a LANDSCAPE canvas with an EXACT 3:1 width-to-height ratio. No photograph, no mockup or perspective. A polished vintage-futurist boarding pass on warm ivory paper with deep midnight navy typography, yellow accent rules and a restrained thin navy border. High print contrast and generous trim-safe margins.
Composition: LEFT quarter is a richly illustrated navy-blue celestial vignette featuring a luminous cream/yellow crescent Moon, a restrained scattering of white stars and one warm yellow sweeping orbital arc. The CENTER is mostly ivory with exceptionally legible typography. The RIGHT narrow tear-off stub is separated by a fine dotted vertical perforation line; it carries a small simple moon/orbit emblem and the words "ADVENTURE" above "COMPLETE". A slight paper grain is acceptable, but no heavy distress or faded text.
Exact typography and text:
Small top header: "ESCAPE BACKPACK"
A modest uppercase subheading: "FIRST COMMERCIAL VOYAGE"
Large bold primary title, on two lines if needed: "THE MOON" and "& BEYOND"
Smaller clean invitation, exactly: "Come join me on the first commercial voyage" then "to the Moon and beyond."
A short warm handwritten signature beneath: "Your uncle"
Right stub only: "ADVENTURE" then "COMPLETE".
All words must be spelled exactly and readable, with deliberate spacing. Use simple legible lettering, confident title hierarchy, no complicated decorative scripts except the brief signature.
Constraints: NO passenger/player name or name field; NO dates, times, gate, seat, terminal, prices, invented airline/company, numbers, serial code, barcode, QR code or extra text. NO rocket or spaceship because the uncle's antigravity craft design is not established. No watermark, no external logos. This is a playful invitation reward, not a puzzle or real travel document. Keep it visually charming and cohesive with the navy/yellow medallion.
```

