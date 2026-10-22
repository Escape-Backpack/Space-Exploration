---
id: AS-042
title: Canadarm sequential movements - smooth designer GIF
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for:
# Generator or tool used
tool:
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/canadarm-sequential-movements-v2.gif
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-011]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-055
tags: []
---

## Current sequence mockup - 2026-10-22
User asks for smooth transitions and one movement at a time. Shows the full starting
pose/readout, then six separate relative turns, with each active joint highlighted
and named. No resetting between commands. Four readings: start plus three checkpoints.
Other joint settings stay fixed; downstream links are carried by upstream turns.

Commands follow the checked candidate example in PZ-011's current direction. Values
and candidate digits remain illustrative, not a final assigned puzzle answer.
Visible joint scales are schematic; no calibrated cutting geometry is claimed.
The board is redrawn at the new endpoint positions; old printable board is unchanged.
Designer animation only, not a player clue/public hint.

Source: source/build_canadarm_sequence_gif_v2.py. Local output:
output/gif/canadarm-sequence-v2/Canadarm_Sequential_Movements.gif.
Candidate sequence source: output/design/canadarm-sequence-v2/candidate-sequence.json.
Checkpoint/scale PNG inspections and animation-audit.json are beside the GIF.
No ImageGen; native deterministic diagram animation.

## Verification and limits
Smooth quintic easing, 50 ms motion frames (20 fps), pauses before commands and at
checkpoints. Reopened GIF: 194 encoded frames, 27.55 seconds, 900 x 1120 px, loops.
Every movement changes only its named relative joint setting. Upstream positions,
base and all three link lengths verified; final poses match all four checked states.
Four readout holds and the joint-scale view inspected. Shared palette prevents colour
flashing. Actual Studio GIF upload downloaded back and SHA-256 matched.
Physical dials, pin slack/friction, print alignment and player testing remain pending.
