---
id: PP-014
title: Jointed paper Canadarm
type: prop
status: candidate
form: printed
source: print
envelope:
after_game: return
reset_name: Jointed paper Canadarm
links: []
superseded_by:
tags: []
---

## Selected arm labels - 2026-10-22
Designer renames the three moving pieces **A, B, C, from longest to shortest**:
- A: upper arm, shoulder/base pivot (110 pt pin-to-pin in the current candidate).
- B: forearm, elbow pivot (100 pt in the current candidate).
- C: short hand piece, wrist pivot (35 pt to reading centre in the candidate).
Use these labels on revised parts and movement clues. Turn A at its base; turn B
where it joins A; turn C where it joins B. Upstream turns carry downstream pieces,
with their relative settings retained. Numeric dimensions remain prototype values.

Designer asks whether degree marks should be 0, 30, 60, 90, etc. Assistant recommends
30-degree tick spacing: 60 is two intervals, 90 is three. Final dial radius, label
density and physical readability remain open; no new dial artwork produced yet.

## Joint-angle aids proposed - 2026-10-22
Designer suggests adding angles to support the revised sequential movements in
PZ-011. Proposed aid: small degree scales centred at the three joints and indicators
on the outgoing links. Commands are relative turns, with other joint settings held;
turning shoulder carries elbow/wrist/hand, turning elbow carries wrist/hand.
Calibration/reference directions and dial geometry are not yet built or tested.
The old plain three-piece cutting sheet remains a historical physical prototype.

## Candidate mechanism
Three opaque cardstock pieces: shoulder-to-elbow link, elbow-to-wrist link and short
reading hand. Assemble before play with three split pins, one fixing shoulder to
PP-013 board and two joining elbow/wrist. Keep printed sides up; joints must turn
freely. The small round opening in the hand reveals a board digit.

AS-037 holds cutting paths/instructions. Pin-to-pin lengths and reading aperture
are candidate game geometry in source/build_canadarm_sketch_prototype_v1.py, not
real Canadarm dimensions or a full-joint replica. Dimensions/paper/fasteners need
physical testing for slack, friction and readability. No cutting or assembly by
players is currently proposed. At reset return all three joined pieces and board.
Puzzle order, packing and final answer remain unassigned.
