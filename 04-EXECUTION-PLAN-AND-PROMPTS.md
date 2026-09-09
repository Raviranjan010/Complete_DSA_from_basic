# 04 — EXECUTION PLAN & READY-TO-PASTE PROMPTS

> Building the whole repo in one shot will overflow any IDE AI's context
> and cause it to skip things. Build it in the batches below, in order,
> verifying after every batch with the audit prompt.

## 0. Session kickoff (paste once, at the very start)

```
I'm building the repo "DSA-Zero-To-Hero". I'm giving you 4 spec files:
00-MASTER-PROMPT.md, 01-REPO-STRUCTURE-AND-NAMING.md,
02-COMPLETE-DSA-CURRICULUM.md, 03-CONTENT-STANDARDS-AND-TEMPLATE.md.

Read all four fully before writing any code or files. Then reply with:
1. The full folder structure you understood (from file 01).
2. The full ordered topic list you understood (from file 02), phase by phase.
3. The exact template you will use for every concept file and every
   practice file (from file 03).
4. Confirmation you understand the non-negotiable rules in file 00
   (zero gaps, zero skipped topics, strict sequencing, C++ only,
   beginner-first language, no placeholders, real links only).

Do not generate any repo content yet — wait for my "Start Phase 0" prompt.
```

Review the AI's restatement carefully. If anything is wrong or missing,
correct it before proceeding — do not start content generation on a
faulty understanding.

## 1. Batch plan (one prompt per batch, wait for completion each time)

Generate the repo in this exact batch order. Each batch = one prompt.

| Batch | Scope | Prompt to send |
|---|---|---|
| 1 | Root scaffolding | "Create the root `README.md` (with full TOC placeholder to be filled as we go), `GLOSSARY.md` (empty sections per phase, to be filled as we go), `PATTERNS.md` (empty pattern index, to be filled as we go), `PROGRESS-TRACKER.md`, and all `CHEATSHEETS/` files with their headings only, and create every phase folder (00 through 15) with an empty `README.md` stub per file 01's structure. Do not fill in phase READMEs yet — just create the skeleton exactly matching file 01." |
| 2 | Phase 0 | "Generate all of Phase 0 (Prerequisites) completely: the phase README plus every concept file and practice file for sub-topics 0.1 through 0.13, following the file-03 template exactly and the file-02 topic list exactly. Update GLOSSARY.md with every new term introduced in this phase. Update PROGRESS-TRACKER.md and PATTERNS.md if any patterns were introduced." |
| 3 | Phase 1 | Same instruction, scoped to Phase 1 (1.1–1.8). |
| 4 | Phase 2 | Same instruction, scoped to Phase 2 (2.1–2.19). This is large — if needed, split into 2a (2.1–2.9 sorting/searching) and 2b (2.10–2.19 strings), telling the AI explicitly which sub-range to generate in each prompt. |
| 5 | Phase 3 | Same pattern, scoped to Phase 3 (3.1–3.10). |
| 6 | Phase 4 | Same pattern, scoped to Phase 4 (4.1–4.10). |
| 7 | Phase 5 | Same pattern, scoped to Phase 5 (5.1–5.7). |
| 8 | Phase 6 | Same pattern, scoped to Phase 6 (6.1–6.8). |
| 9 | Phase 7 | Same pattern, scoped to Phase 7 (7.1–7.13) — large, split into 7a (7.1–7.8 core trees/BST) and 7b (7.9–7.13 advanced trees/segment/Fenwick/trie). |
| 10 | Phase 8 | Same pattern, scoped to Phase 8 (8.1–8.6). |
| 11 | Phase 9 | Same pattern, scoped to Phase 9 (9.1–9.14) — large, split into 9a (9.1–9.6 traversal/shortest path basics), 9b (9.7–9.10 advanced shortest path/MST/DSU), 9c (9.11–9.14 SCC/bridges/flow). |
| 12 | Phase 10 | Same pattern, scoped to Phase 10 (10.1–10.7). |
| 13 | Phase 11 | Same pattern, scoped to Phase 11 (11.1–11.13) — large, split into 11a (11.1–11.7), 11b (11.8–11.13). |
| 14 | Phase 12 | Same pattern, scoped to Phase 12 (12.1–12.7). |
| 15 | Phase 13 | Same pattern, scoped to Phase 13 (13.1–13.8). |
| 16 | Phase 14 | Same pattern, scoped to Phase 14 (14.1–14.6). |
| 17 | Phase 15 | Same pattern, scoped to Phase 15 (15.1–15.7) — this is the interview-prep capstone; instruct the AI to also cross-check `PATTERNS.md` is fully populated by now. |
| 18 | Finalization | See "Finalization prompt" below. |

### Generic per-phase prompt template (reuse for every batch)

```
Start Phase <N>: <phase name>, covering sub-topics <X.1 through X.Y>
exactly as listed in 02-COMPLETE-DSA-CURRICULUM.md.

For each sub-topic:
1. Create the concept file using the exact template in
   03-CONTENT-STANDARDS-AND-TEMPLATE.md section A.
2. Create the matching practice file using template section B, with real
   links only (never fabricate URLs), meeting the minimum question-count
   and difficulty-spread rules.
3. Update this phase's README.md with a short description and link.
4. Append any new terms to GLOSSARY.md.
5. Append any recurring patterns to PATTERNS.md, linking to the questions
   that use them.
6. Update PROGRESS-TRACKER.md with checklist entries for this phase.

Obey every rule in 00-MASTER-PROMPT.md, especially: no forward references
to untaught concepts, no placeholders, beginner-first explanations before
formal definitions, and full dry runs with diagrams for anything spatial.

When finished, list every file you created/modified in this batch so I
can verify against the curriculum before we continue.
```

## 2. Audit prompt (run after EVERY batch, before starting the next)

```
Audit the phase(s) you just generated against these checks and report
PASS/FAIL with specifics for each:

1. Every sub-topic number from 02-COMPLETE-DSA-CURRICULUM.md for this
   phase has a concept file AND a practice file — list any missing.
2. No concept file references a term/concept from a LATER phase without
   a "we'll cover this later" link.
3. No concept file assumes a term from an EARLIER phase without linking
   to it on first use.
4. Every code sample uses only C++ syntax that has been introduced by
   this point in the curriculum (or is explained inline if new).
5. Every practice file meets the minimum question count and difficulty
   spread from 03-CONTENT-STANDARDS-AND-TEMPLATE.md section B.
6. No placeholder text ("TODO", "coming soon", etc.) exists anywhere.
7. GLOSSARY.md, PATTERNS.md, and PROGRESS-TRACKER.md were actually updated
   for this phase.

Fix anything that fails before moving to the next phase.
```

## 3. Finalization prompt (run once, after all 16 phases are complete)

```
All phases (0-15) are generated. Now do a full-repo finalization pass:

1. Rebuild the root README.md's Table of Contents by scanning every phase
   folder — make sure every single file is linked, in the correct order.
2. Verify GLOSSARY.md has no duplicate or missing terms — scan every
   concept file for technical terms and cross-check.
3. Verify PATTERNS.md lists every pattern tag used anywhere in the repo,
   each linking to every question file that uses it.
4. Verify PROGRESS-TRACKER.md has one checklist line per concept file and
   per question (not just per subtopic) across the whole repo.
5. Re-run the audit prompt (section 2 above) across the ENTIRE repo, not
   just one phase, and fix every failure found.
6. Fill in all CHEATSHEETS/ files completely now that all content exists,
   summarizing each phase's key formulas/patterns/complexities in a
   quick-revision format.
7. Do a final broken-link and fabricated-URL sweep: flag any practice
   question link that isn't a real, verifiable platform URL pattern.

Report a final completion summary: total phases, total concept files,
total practice files, total questions, total patterns indexed.
```

## 4. Tips for keeping the IDE AI on track

- Never let it "summarize the rest" or skip ahead — if it tries, resend
  the relevant part of file 00 (rule 8 & 9) and ask it to redo the batch.
- If a batch is rejected by the audit, ask it to fix ONLY the failing
  items, not regenerate the whole batch from scratch (saves time/tokens).
- Keep batches phase-sized or smaller — never ask for multiple phases at
  once; that's when topics silently get thinner or skipped.
- After every 3-4 phases, re-paste the Definition of Done checklist from
  file 00 section 4 and ask "which of these are still unmet so far?" as
  a running sanity check.
