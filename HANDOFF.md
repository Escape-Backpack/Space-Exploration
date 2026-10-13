# Handoff

## 2026-10-05: full Galileo note and optics artwork (Codex)
- **Status:** Designer chose all information on the note (Q-007 answered). Generated AS-009 as a candidate full handwritten note with four dated observations and a Galilean lens/ray sketch. PP-007 contains full draft text. PZ-001 no longer requires PP-002; card split explicitly superseded. Existing answer unchanged.
- **Files:** New `assets/galileo-note-and-lens-diagram-v1.png`, AS-009 with exact ImageGen prompt/reference; PP-007, PZ-001, PP-002, Q-007, Q-004; rebuilt ignored `site/`; both handoffs. Source-backed month labels replace old date shorthand, whose history is retained. Unrelated changes preserved.
- **Checks:** Rice chronology/Museo Galileo optics checked. Full image reviewed word for word, for all four observations, correct date-block order, readable labels and qualitative convex-objective/concave-eyepiece ray layout. 40 records valid; scoped whitespace check passed. HTTP browser confirms complete note, AS-009 link and image loaded; layout reviewed, no console warnings/errors. No physical print, optical calibration or puzzle playtest.
- **Next:** Designer reviews the full draft wording and drawing before choosing print dimensions and testing the note with the map/magnifier. No commit, push or publication.

## 2026-10-05: Galileo note and lens-sketch discussion (Codex)
- **Status:** Recorded the designer's candidate note/optics direction in PP-007. Q-007 asks whether all dates go in the note or retain the card/note split; unanswered. Final wording/artwork not approved or generated.
- **Files:** PP-007, new Q-007, rebuilt ignored `site/`, both handoffs. Unrelated work preserved.
- **Checks:** Primary institutional sources reviewed for Saturn, Venus chronology and Galilean optics. Noted date-precision gaps in PP-007 rather than silently rewriting Q-004/PZ-001. Record validation passed (39 records, no problems). Browser refresh over HTTP confirms new note/research sections and question link; visual layout checked, no console warnings/errors.
- **Next:** Resolve Q-007 and agree the note's wording before creating the handwritten note and lens diagram. No commit, push or publication.

## 2026-10-05: next puzzle reviewed (Codex)
- **Status:** Reviewed PZ-001 as the intended second lock after the luggage tag: Galileo card/note identify dated discoveries, magnifier reveals map digits, chronology orders the code. No design changes.
- **Files/checks:** Handoffs only; checked PZ-001, PP-002, PP-007 and AS-003 against current files. Player map exists; card/note wording and card availability remain incomplete. Physical magnifier readability untested.
- **Next:** Discuss and draft the Galileo card and uncle note together before generating their artwork. No commit, push or publication.

## 2026-10-05: approved luggage tag recorded and HTML rebuilt (Codex)
- **Status:** Recorded PP-008 as the decided luggage-tag design: existing stars on front (AS-002), exact welcome and original telescope V1 on back (AS-008), first clue and note from the start. Finer graphite V2 remains an unselected alternative. Physical size/readability and QR placement remain pending.
- **Files:** PP-008; rebuilt ignored `site/index.html`, `site/data.js` and companion views/files through the shared kit; both handoffs. Saved verification screenshot `output/qa/luggage-tag-board.png`. No asset images changed; unrelated edits preserved.
- **Checks:** `kit.py check` passed (38 records, no problems); local build completed. In-app browser over HTTP: PP-008 decided status, exact welcome and face assignments visible; both asset images load and AS-008 shows original V1. Visual layout checked; no browser warnings/errors. No physical print or playtest.
- **Preview:** Local-only server serves `C:/EscapeBackpack` at `http://127.0.0.1:8734/Space-Exploration/site/index.html#props/PP-008`. HTML is generated from records; rebuild rather than editing generated copies. `preview_start` is not available in this session, so the existing Python HTTP mechanism was started directly.
- **Next:** Confirm physical tag dimensions and QR placement before preparing a two-sided print. No commit, push or publication.

## 2026-10-05: original luggage-tag telescope selected (Codex)
- **Status:** Designer chose original V1 after viewing V2. AS-008 now selects V1 and records visual approval; PP-008 marks the thinner-line experiment superseded. V2 and its source remain as alternatives; no images overwritten.
- **Files/checks:** AS-008, PP-008 and both handoffs; record validation passed (38 records, no problems); both image files confirmed present. No new visual changes. Physical printing and tag size remain unconfirmed.
- **Next:** Confirm tag dimensions and QR placement before preparing a two-sided print using selected V1. No commit, push or publication.

## 2026-10-05: finer graphite telescope preview (Codex)
- **Status:** User requested the refined preview. Edited AS-008 twice using built-in ImageGen; v2 retains the note and telescope with finer grey strokes. V1 preserved; v2 remains candidate. Exact physical stroke widths and 1:5 ratio unmeasured.
- **Files:** New `assets/luggage-tag-back-note-telescope-v2.png`, intermediate in `source/`; AS-008 records both exact prompts and review, PP-008 updated, both handoffs updated. Unrelated changes preserved.
- **Checks:** Both generated passes screen-reviewed; final words, punctuation, line wrapping, drawing geometry and layout checked. Record validation passed (38 records, no problems); scoped whitespace check passed. No claim of pixel-identical preservation, physical readability or calibrated stroke widths.
- **Next:** Designer reviews v2; confirm final print size before calibrating lines and testing readability. No commit, push or publication.

## 2026-10-05: telescope retained and line weights specified (Codex)
- **Status:** Designer kept AS-008's telescope and proposed writing/drawing widths of 0.5/0.1 mm. PP-008 records the target ratio and its interpretation at final print size. AS-008 records acceptance and pending refinement; v1 artwork unchanged.
- **Files/checks:** PP-008, AS-008 and both handoffs; record validation passed (38 records, no problems). No artwork or HTML edits requiring visual checks. Final physical size and measured strokes remain unresolved.
- **Next:** Confirm final tag size before applying and measuring the thinner pencil-style drawing. No commit, push or publication.

## 2026-10-05: luggage-tag welcome and telescope back (Codex)
- **Status:** Designer approved star artwork as front and exact welcome note plus vintage telescope as back. Generated AS-008 using AS-007's centre handwriting reference; visual rendering remains candidate for review. The star-count mechanism is unchanged; lock colour order remains unresolved.
- **Files:** New `assets/luggage-tag-back-note-telescope-v1.png` and AS-008 (exact prompt); PP-008 stores approved note and superseded draft; PZ-002/AS-002 face references updated without renaming existing images. Both handoffs updated; unrelated work preserved.
- **Checks:** Full-resolution artwork reviewed word for word and for text/sketch separation. No added codes, labels or signature. Record validation passed (38 records, no problems); scoped whitespace and face-reference checks passed. Physical note readability, trim and mirrored strap-hole alignment untested; QR placement remains pending. No print PDF requested or generated.
- **Next:** Designer reviews AS-008; then confirm physical tag size and QR placement before preparing and testing a two-sided print. No commit, push or publication.

## 2026-10-05: luggage-tag clue review (Codex)
- **Status:** Confirmed PZ-002 uses the tag-back's coloured constellation star counts as its visual clue. Written clue and hints sections remain empty; PP-008 contains a draft welcome only. Final digit order depends on the actual lock wheel colours.
- **Files/checks:** Handoffs only; reviewed PZ-002, PP-008, AS-002 and related questions. No design or artwork edits.
- **Next:** Discuss whether the welcome needs a subtle pointer to the tag's sky before designing its handwritten front. No commit, push or publication.

## 2026-10-05: existing uncle handwriting review (Codex)
- **Status:** Answered whether existing props use the selected handwriting. AS-007 is the style sample; PP-008 has draft welcome text but no front artwork; PP-007 has no wording yet. AS-005 contains an earlier handwritten signature, not a recorded application of PR-007.
- **Files:** This handoff and sibling EscapeBackpack handoff only; no design or artwork changes.
- **Checks:** Searched active records and inventoried asset/source files. No visual or print changes requiring checks.
- **Next:** Propose applying PR-007 to PP-008's existing welcome text. No commit, push or publication.

## 2026-10-05: option 2 handwriting selected (Codex)
- **Status:** Designer selected option 2 from AS-007. Recorded the chosen handwriting in PR-007 and updated AS-007's selection history; the full sheet remains concept artwork.
- **Files:** PR-007, AS-007, this handoff and sibling EscapeBackpack handoff. No image changes; unrelated edits preserved.
- **Checks:** Record validation passed (37 records, no problems). No new artwork or HTML requiring visual checks.
- **Next:** Apply PR-007 to the next approved uncle note or diagram; correct diagram annotation leaders before player use. Typeface and puzzle mechanism remain unselected. No commit, push or publication.

## 2026-10-05: handwriting and sketch examples (Codex)
- **Status:** User requested examples. Generated a three-column comparison sheet (AS-007) for PR-007: drafting print, engineer's notebook and rounded technical. Option 2 recommended in chat; no selection recorded.
- **Files:** `assets/handwriting-and-technical-sketch-styles-v1.png`, AS-007 (exact prompt and review), this handoff; sibling EscapeBackpack handoff updated. Unrelated changes preserved.
- **Checks:** Full sheet visually reviewed: lettering readable, requested subjects present. Sketches remain very similar across columns, and some label leaders need correction before puzzle use. Record validation passed (37 records, no problems); handoff whitespace check passed. No physical print test or scientific validation.
- **Next:** Designer selects or adjusts a handwriting sample; then develop the sketch style and correct labels for a specific prop. No commit, push or publication.

## 2026-10-05: handwriting and sketch identity discussion (Codex)
- **Status:** Reviewed the existing visual direction and recorded the designer's explicit handwriting/sketch preferences in PR-007. The engineer's astronomy notebook direction is a proposal in chat, not an approved complete style guide.
- **Files:** New `records/premise/PR-007-uncle-s-handwriting-and-technical-sketch.md`; this handoff. Existing unrelated changes preserved.
- **Checks:** Reviewed active premise, prop and artwork records; `python ../backpack-kit/kit.py check` passed (36 records, no problems). No artwork or HTML changed, so no new visual validation required.
- **Next:** Review one proposed handwriting/sketch sample before selecting the detailed style. Typeface and puzzle use remain unselected in PR-007. No commit, push or publication.

## 2026-10-05: documentation closeout (Codex)
- **Status:** Requested document synchronization completed; chat ready to archive. Existing improved shared-back notes and digital assets remain current; sibling EscapeBackpack/index.html now links the Space v1 print package in the shared six-adventure file list.
- **Checks:** Document links and active records checked; root index and both Aurora guide sections reviewed over local HTTP; all 29 new section links/images return 200; images load, identity appears in print content, and no browser console warnings/errors. Earlier digital geometry checks still apply; no physical print or actual printer-profile slice.
- **Next:** Print the thin back trial with the intended printer/material and inspect S/B/K, then test the full medallion. No commit, push or publication.


## 2026-10-05: approved medallion back reused (Codex)
- **Recorded:** The designer approved AS-006's digital design and asked for the same back on Norse and Hiking. Approval evidence is in AS-006; physical testing remains pending.
- **Created elsewhere:** Norse v3 retains the existing raven front exactly; Hiking v1 uses the selected mountains, winding trail and pine trees. Files and design notes are in `../EscapeBackpack/`.
- **Checks:** The three readable back SVGs are byte-identical. Norse/Hiking full models and thin lettering trials pass exported-mesh checks. Space records pass validation.
- **Next step:** Print a full-size thin back trial with the intended printer/material and inspect S/B/K before a complete print.

## 2026-10-05: Space medallion STL and larger back lettering (Codex)
- **Worked on:** PP-003, AS-004 and new AS-006, following approval of the front and a request for the Space STL.
- **Designer report:** An earlier medallion's S, B and K in "ESCAPE BACKPACK" printed poorly. Exact printed version, material and slicer settings are unconfirmed; no printer diagnosis was invented.
- **Created:** One-piece STL from the selected front, a matching thin back-only test disk, exact SVG profiles/preview, measured reports, rebuild script, README and ZIP. AS-006 is built as a digital asset; the physical prop is not marked tested.
- **Changed:** Larger, more open brand glyphs and wider lower text arcs. Exact curved glyph gaps are validated. Printing instructions keep the engraved back down and explain the colour-change layer and first-layer limitations.
- **Checks:** Both exported STLs are closed, consistently oriented, one connected solid, without degenerate facets; mesh volumes match analytic layers. Preview inspected; record validation passed. No actual printer-profile slice or physical print completed.
- **Next step:** Print the thin lettering disk at full scale using the intended printer/filament settings, review S/B/K, then print the full two-colour medallion.

## 2026-10-05: medallion front and final ticket drafts (Codex)
- **Worked on:** PP-003 and PP-004 together at the designer's request.
- **Created:** AS-004 stores the navy/yellow telescope-Moon-orbit medallion concept and exact prompt. AS-005 stores the final-reward ticket artwork, exact prompt, Letter print PDF and rebuild script.
- **Status:** Both asset designs remain candidate. No prop approvals, physical dimensions, manufacturing success or playtest results were invented. The medallion image is concept art only; no Space STL or relief profile was made.
- **Checks:** Screen-reviewed both images and ticket spelling; rendered the PDF with Poppler and reviewed its layout, crop marks and size-check line. Record validation passed. Physical printing remains untested.
- **Next step:** Review the two designs. If the medallion motif is accepted, translate it into two-colour relief geometry; test the ticket PDF at actual size.

## 2026-10-05: remaining artwork review (Codex)
- **Worked on:** Reviewed existing assets and prop records for remaining artwork/layout needs.
- **Decided:** None; no assets generated or puzzle decisions changed.
- **Recommendation:** Prioritise PP-002's Galileo card and PP-007's note so the existing map can be solved. PP-008's front, PP-003 and PP-004 also need design work; PP-001 remains an optional idea with no settled role.
- **Next step:** Draft the Galileo card and note together, keeping PZ-001's split of discovery information. Later-era art depends on further puzzle design.

## 2026-10-04: numbered player map (Codex)
- **Worked on:** AS-003, following the designer's request to add hidden answer digits and decoys to the non-solution map.
- **Created:** `assets/galileo-sky-map-player-v1.png`, edited from the base using built-in ImageGen, then refined to subdue the digits. AS-003 now uses this player file and stores both exact prompts. Base and solution images preserved.
- **Checks:** Screen inspection counted four correct object-associated digits plus ten decoys; Jupiter retains four moon dots. Record validation passed. The digits are readable in the full-resolution screen image, so magnifier-only readability is not established.
- **Status:** PZ-001 and AS-003 remain candidate; physical testing remains unperformed and public hints remain disabled.
- **Next step:** Choose final print size and test the printed map with the actual magnifier; adjust digit size/contrast if necessary.

## 2026-10-04: highlighted second-lock solution (Codex)
- **Worked on:** PZ-001 and AS-003, following the designer's digit selection.
- **Decided:** PZ-001 now stores the chosen answer and object-to-digit mapping. The puzzle remains candidate, untested, with public hints disabled.
- **Created:** `assets/galileo-sky-map-solution-v1.png` using built-in ImageGen to annotate the base map. AS-003 records the exact edit prompt and companion path; the solution is not assigned as the player asset.
- **Checks:** Screen-verified all four highlighted digits, object associations and central code. Physical print/magnifier readability remains untested.
- **Next step:** Choose the print size, add tiny answer digits and decoys to a separate player map, and test the physical print.

## 2026-10-04: second-lock sky map artwork draft (Codex)
- **Worked on:** Reviewed PZ-001 (the second lock), PP-005 and the opening sequence; generated AS-003 using the Space cover as a style reference.
- **Created:** `assets/galileo-sky-map-base-v1.png`, a draft chart containing the four celestial objects. AS-003 stores the exact prompt and remains candidate.
- **Decided:** No code, print size, difficulty, clue wording or puzzle status changes. Existing uncommitted PZ-001 edits were preserved.
- **Checks:** Screen-reviewed the four objects and Jupiter's four moon dots. The draft has no digits yet; physical print and magnifier tests remain unperformed.
- **Next step:** Await the designer's code (Moon, Jupiter, Saturn, Venus order) and print size, then add the tiny digits and decoys required by PZ-001 and test a physical print.

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
