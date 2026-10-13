---
id: Q-008
title: What changes now that Space uses envelopes instead of locks?
type: question
# open | answered | parked
status: open
# Records this question is about, e.g. [PZ-003]
about: [PZ-002, PZ-001, PP-009, PP-008, PR-003, Q-006]
# Leave empty while open
answer:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

On 2026-10-12 the designer switched Space Exploration from locks in a backpack to marked
envelopes in a board-game box, with one lookup cipher per adventure. The migration only
renamed fields (found_in became envelope; lock fields were removed). These design points
still describe the lock version and need a decision:

- **PZ-002 answer.** It was three digits (7-3-2) for the 3-digit colour lock, ordered by the
  wheel colours. Envelope answers are 4 or 5 characters and there are no wheel colours.
- **PZ-002 and PZ-001 text** still say "first lock" and "locked compartment". PZ-002's answer
  now opens the envelope holding the Galileo kit (PP-005, PP-006, PP-007 have envelope: PZ-002).
- **PP-009 The backpack** and **Q-006 Which backpack to buy?**: the container is now a box.
- **PP-008 Luggage tag** is attached to the backpack. Does it stay a luggage tag in a box?
- **PR-003 Aim for 10 to 15 locks**: now 10 to 15 puzzles (envelopes)?
- **Cipher**: backpack.json uses the kit's planets preset (0 Sun, 1 Moon, 2 Mercury ...
  9 Neptune) and 2 decoy envelopes as a starting point. Not chosen by the designer yet.
