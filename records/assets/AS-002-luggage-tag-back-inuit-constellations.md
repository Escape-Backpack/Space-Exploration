---
id: AS-002
title: Luggage tag back - Inuit constellations
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for: PP-008
# Generator or tool used
tool: OpenAI ImageGen built-in
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/luggage-tag-back-inuit-constellations-v2.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-002, Q-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

Placeholder colours (red, blue, green) stand in for the 3-digit colour lock's real wheel colours,
not yet known (Q-006, backpack not bought). Swap the colours in the prompt once those are set;
the star counts and layout stay the same.

Version 2 is the current artwork. It retains the v1 composition and star counts while
softening the coloured highlights. Version 1 remains at
`assets/luggage-tag-back-inuit-constellations-v1.png`.

Tested by cropping v2 to a 3.5"x2.25" tag at 300dpi (screen proxy, not a physical print test):
all three star counts stayed legible. Approved as-is at that crop. The tag's strap hole goes
top-right (PP-008), not top-left, so it doesn't sit over the red constellation.

Exact v2 edit prompt (built-in ImageGen, v1 as the edit target):

> Use case: precise-object-edit. Edit the supplied luggage-tag artwork. Keep the entire Arctic night landscape, sky texture, framing, star positions, constellation shapes, and exact highlighted-star counts unchanged: seven red stars on the left, three blue stars in the center, two green stars on the right. Change only the conspicuous constellation highlighting: lower the brightness, saturation, bloom/glow, and line intensity of the red, blue, and green stars and their connecting lines by a modest amount, about 25-35%, so they are still findable and countable on a small printed tag but less obvious at first glance. Make the points slightly less spiky and luminous. Keep all ordinary white background stars and the scenic background as they are. No new stars, no removed stars, no text, no labels, no logos, no watermark.

Initial concept prompt:

> Use case: illustration-print. Asset type: back-of-tag illustration for a luggage tag prop in
> Escape Backpack's Space Exploration adventure, matching the polished hand-drawn digital
> illustration style of the adventure's cover art (deep blue night tones, warm accents, no
> photorealism). A simple northern night sky filled with small white stars, with three
> constellations picked out in bold colour so each is easy to trace and count at a glance:
> a red constellation of exactly 7 stars connected in the shape of the Big Dipper (Tukturjuit,
> "the caribou"); a blue constellation of exactly 3 stars in a short straight line (Ullaktut,
> "the runners", Orion's Belt); a green constellation of exactly 2 stars close together
> (Aagjuuk, Altair and Tarazed). The three constellations are spaced apart and clearly
> separated so their star counts can be counted without ambiguity. No people, no readable
> text, no labels, no logos, no watermarks, no compass rose.

## Generated version 1

Created with the built-in ImageGen tool on 2026-09-27, using
`brand/Space_Exploration_Backpack_Scene_v1.png` as a style reference. The image
visibly has 7 red, 3 blue, and 2 green highlighted stars. The colours are still
placeholders until the lock is chosen (Q-006). Print-size legibility has not been tested.

Exact v1 generation prompt:

> Use case: scientific-educational. Asset type: flat printable illustration for the BACK of a small luggage tag in a space exploration escape-game backpack. Use the provided cover illustration only as a STYLE reference: polished hand-drawn digital illustration, deep midnight and navy blues with warm subtle accents. Create the artwork itself, straight-on and edge-to-edge, no photograph or mockup of a tag. A simple dark Arctic night sky with restrained tiny WHITE background stars. Three separate highlighted star patterns are the unmistakable focus: LEFT, a RED Big Dipper-shaped seven-star pattern representing Tukturjuit, with exactly SEVEN red stars connected by thin red lines; CENTER, a BLUE Orion's-Belt-like straight row of exactly THREE blue stars connected by thin blue lines, representing Ullaktut; RIGHT, a GREEN close pair of exactly TWO green stars connected by a thin green line, representing Aagjuuk. Give each coloured group generous separation and even visual weight. The coloured stars must be large and crisp enough to count on a luggage tag; all other background stars must be tiny, white, and visually subordinate. Preserve clear margins for later print trimming. No labels, letters, numbers, words, logos, compass rose, people, extra coloured stars, or watermark. Do not add decorative stars in red, blue, or green. No text at all.
