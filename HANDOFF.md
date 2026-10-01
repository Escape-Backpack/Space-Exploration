# Handoff

## 2026-09-28: Shared kit process review (Codex)
- **Worked on:** Updated the shared kit and synchronized this project's agent instructions. Added separate playtest/release audits, generated Flow and Setup & reset, optional puzzle/prop documentation, and explicit public-hint opt-in. Rebuilt the ignored local site for review.
- **Decided:** No Space puzzle decisions, answers or test results changed.
- **Checks:** The existing 31 records still pass check. The candidate-inclusive readiness audit reports 47 preparation gaps; these are documentation/availability gaps, not newly invented facts or invalid records. Kit regression tests passed. Existing uncommitted project work preserved.
- **Next step:** Continue the current puzzle session below. Add the new fields/notes as each puzzle is worked on. Public hints stay empty until decided/built puzzles are explicitly marked publish_hints: yes.


## 2026-09-28: Galileo's sky map puzzle (PZ-001)
- **Worked on:** Q-004 (which four discoveries) and the decoy-digit mechanic for PZ-001.
- **Decided:** Q-004 answered - four discoveries in date order: Moon's mountains/craters
  (Nov 30, 1609), Jupiter's four moons (Jan 7, 1610), Saturn's triple form/rings (Jul 25,
  1610), phases of Venus (Oct 1610). Milky Way dropped, no distinct date. PZ-001's decoy
  mechanic decided: one sky map (PP-005), about 8-12 decoy digits on ordinary stars,
  blending into the map's natural clutter; only the 4 Galileo objects' digits count.
- **Checks:** `python ../backpack-kit/kit.py check` reported 31 records, no problems.
- **Next step:** PZ-001 still needs a difficulty rating and clue/hint wording. Compartment
  and lock hardware decisions (Q-006, PP-009) wait until a few more puzzles are drafted.

## 2026-09-27: approve the tag art, place the strap hole
- **Worked on:** AS-002 print-size check and PP-008's strap hole placement.
- **Decided:** AS-002 v2 approved as-is after a 3.5"x2.25" @300dpi crop test (screen proxy, not a
  physical print) — all three star counts stayed legible. PP-008's strap hole goes top-right,
  clear of the red constellation (a top-left hole collided with it in the test crop).
- **Checks:** `python ../backpack-kit/kit.py check` reported 31 records, no problems.
- **Next step:** Galileo's sky map puzzle (PZ-001, second lock). Compartment/lock hardware
  decisions (Q-006, PP-009) wait until there are a few more puzzles drafted.

## 2026-09-27: soften the constellation highlights
- **Worked on:** AS-002, at the designer's request.
- **Built:** `assets/luggage-tag-back-inuit-constellations-v2.png`; it keeps the v1 background and layout with dimmer coloured stars and lines. V1 is preserved.
- **Checks:** visually counted 7 red, 3 blue, and 2 green highlighted stars in v2. Print-size legibility remains untested.
- **Next step:** choose the lock colours (Q-006), then print-test the current art at tag size.

## 2026-09-27: generate the constellation tag back
- **Worked on:** AS-002 for the first lock, PZ-002.
- **Built:** `assets/luggage-tag-back-inuit-constellations-v1.png`, using the Space cover as a style reference. AS-002 now records the file and exact generation prompt.
- **Checks:** visually counted 7 red, 3 blue, and 2 green highlighted stars. The image has not been tested at luggage-tag print size.
- **Next step:** choose the backpack and lock (Q-006), replace placeholder colours if needed, and print-test the art at final size.

## 2026-09-27: review the opening constellation puzzle
- **Worked on:** read the project records and reviewed the PZ-002 to PZ-001 opening sequence.
- **Decided:** none. PZ-002 remains a candidate; AS-002 remains an ungenerated prompt.
- **Review notes:** test whether the three coloured groups are unmistakable at printed tag size and whether players discover the tag-to-lock connection without prompting. PP-002's Galileo card needs a defined location before PZ-001. ST-001's wording and PZ-002's chronology sentence need a review for how they frame Inuit sky knowledge.
- **Next step:** choose the backpack and lock (Q-006), make a print-scale tag prototype, then play-test the first unlock.

## 2026-09-26: illustrated adventure cover
- **Worked on:** public-facing Space Exploration cover art in the same backpack-on-a-table illustration family as Hiking.
- **Built:** `brand/Space_Exploration_Backpack_Scene_v1.png`; asset record `AS-001` stores the exact ImageGen prompt and Hiking style reference. The scene shows an astronomy workshop and does not add a story location or puzzle.
- **Checks:** `python ../backpack-kit/kit.py check` reported 18 records with no problems; `kit.py build` copied the asset into `site/files/`. The scene was visually reviewed with the other three covers on both local project listings.
- **Next step:** no design decision needed for this cover. The adventure title remains a working title.

Update at the end of every session. Newest entry on top. Refer to records by ID.

## 2026-09-27: research Q-005, Inuit constellations
- **Worked on:** Q-005, checking the three candidate Inuit constellations against sources.
- **Decided:** Q-005 answered. Tukturjuit ("the caribou", Big Dipper, 7 stars), Ullaktut
  ("the runners", Orion's Belt, 3 stars, hunters chasing the polar bear Nanurjuk), Aagjuuk
  (Altair and Tarazed, 2 stars, heralds the sun's midwinter return) — all checked against
  MacDonald's *The Arctic Sky* and corroborating sources. PZ-002 updated with the digits (7-3-2).
- **Built:** AS-002, the luggage tag back illustration prompt (three constellations, star
  counts, placeholder lock colours). Not yet generated — no image tool in this session.
- **Checks:** `python ../backpack-kit/kit.py check` reported 31 records, no problems.
- **Next step:** generate AS-002's image and set its `file`/`status: built`, or work Q-004
  (Galileo discoveries) or Q-006 (which backpack to buy — PZ-002's lock colours depend on it).

## 2026-09-27: finalise the eras
- **Worked on:** the list of eras.
- **Decided:** six themed eras in chronological order: Looking (ST-001), Sending (ST-006), Going (ST-003), Exploring (ST-002), Building (ST-004), Beyond (ST-005). PR-002 decided.
- **Also settled:** Going = Apollo and Artemis. A Canadian touch per era where possible (not required). Design label "Era"; players don't need a name for them.
- **Also:** first puzzle drafted: PZ-001 Galileo's sky map (candidate), with PP-005 sky map, PP-006 magnifier, PP-007 uncle's note, and the Galileo card in PP-002.
- **New open questions:** Q-003 (first lock / what holds the magnifier), Q-004 (which four discoveries and dates).
- **Also:** first lock drafted: PZ-002 Inuit constellations on the luggage tag (PP-008), a colour lock opening a backpack compartment (PP-009) with the Galileo kit. Q-003 answered.
- **New open questions:** Q-005 (Inuit constellations, check sources), Q-006 (which backpack).
- **Next step:** Q-004 or Q-005 (research), or find the backpack (Q-006).

## 2026-09-26: brainstorm Q-002 (the secret project)
- **Worked on:** Q-002, the uncle's secret project.
- **Decided:** PR-004 (antigravity, and why he's in the North), PR-005 (fun, playful tone), PR-006 (ending: medallion + ticket), ST-005 (fifth era: the future), PP-003 (medallion). Q-002 answered.
- **Candidates:** PP-004 (ticket to the Moon and beyond, no player name).
- **Kit:** medallion added to GUIDE.md as the recurring final prize.
- **Next step:** finalise the list of eras, or design the Space medallion front.

## 2026-09-26: brainstorm Q-001 (structure beats)
- **Worked on:** Q-001, what form the structure beats take.
- **Decided:** PR-001 (sender: the uncle). Q-001 answered: beats are eras of space history, no repeating object.
- **Candidates:** PR-002 (story follows space history), PR-003 (10 to 15 locks), eras ST-001 to ST-004.
- **Ideas:** PP-001 mission patches, PP-002 trading cards (role not decided).
- **New open questions:** Q-002 (the uncle's secret project).
- **Kit:** default locks and build capabilities added to backpack-kit GUIDE.md.
- **Next step:** Q-002, or finalise the list of eras.

## 2026-09-26: project set up from backpack-kit
- **Worked on:** seeded the project from backpack-kit v1.
- **Decided:** none
- **New open questions:** Q-001
- **Next step:** pick the first piece to brainstorm.

<!-- template for new entries:
## YYYY-MM-DD: <piece worked on>
- **Worked on:**
- **Decided:** (IDs whose status changed to decided or built)
- **New open questions:** (Q- IDs)
- **Next step:**
-->
