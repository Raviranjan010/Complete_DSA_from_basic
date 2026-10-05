# 00 — MASTER PROMPT (Read First, Paste First)

> This file is the constitution for the whole project. Every other file
> (01, 02, 03, 04) is a supporting spec. Paste **this entire file** into
> your IDE AI (Claude Code / Cursor / Copilot Chat) as the very first
> message of the session, then follow it with 01 → 02 → 03 → 04 as
> described in `04-EXECUTION-PLAN-AND-PROMPTS.md`.

## 1. Mission

Build a single GitHub repository named **`DSA-Zero-To-Hero`** that teaches
Data Structures & Algorithms from **absolute zero** (a non-tech-background
reader who has never coded) up to **advanced interview/competitive level**,
using **C++ only** for every code example and solution.

The repo must work as:
1. A **self-study textbook** — read top to bottom, never confused, never
   forced to "already know X" that wasn't taught earlier.
2. A **problem bank** — every important pattern has practice questions
   with links to LeetCode / GeeksforGeeks / Codeforces / HackerRank /
   Coding Ninjas (Naukri Code360), tagged by difficulty and pattern.
3. An **interview prep kit** — cheat sheets, patterns index, company-wise
   lists, and a mock-test structure.

## 2. Non-Negotiable Rules

1. **Zero gaps.** If a later topic uses a concept, that concept must have
   already been explained earlier in the repo, in full, with a link back.
   Never say "as you probably know" or assume prior CS education.
2. **Zero skipped topics.** Follow `02-COMPLETE-DSA-CURRICULUM.md` exactly.
   Do not merge, shorten, or silently drop any listed sub-topic. If you
   believe something should be added, add it — never remove.
3. **Strict sequencing.** Topics appear in the repo in the exact phase
   order given in file 02. Do not jump ahead (e.g., no using recursion
   before Phase 3 is written, no using STL `map` before hashing is taught).
4. **Beginner-first language.** Explain every concept as if to someone who
   has never programmed: define every term the first time it's used,
   use plain analogies before formal definitions, then build up to formal
   CS terminology once the intuition is in place.
5. **One consistent template.** Every concept file and every question file
   must follow the exact structure in `03-CONTENT-STANDARDS-AND-TEMPLATE.md`.
   No file may invent its own structure.
6. **C++ only**, using standard C++17, explained line-by-line the first
   time any new syntax/STL feature appears (e.g., first time `vector` is
   used, explain what it is before using it again unexplained).
7. **Every question has real external links.** Never invent a fake URL.
   If unsure a specific link is correct, use the platform's *search* URL
   pattern (e.g., a LeetCode search link) rather than a guessed problem URL.
8. **Never silently truncate.** If a topic is too large for one file,
   split it into numbered sub-files (e.g., `07-graphs/03-dijkstra.md`,
   `07-graphs/03a-dijkstra-practice.md`) — never cut content short.
9. **Self-check before moving on.** After finishing each phase, run the
   audit checklist in `04-EXECUTION-PLAN-AND-PROMPTS.md` before starting
   the next phase.
10. **No placeholders.** Never write "TODO", "content coming soon", or
    stub sections. Every file committed must be complete.

## 3. Target Reader Personas (design for all three simultaneously)

- **Persona A — True beginner:** never written code before. Needs Phase 0
  fully spelled out, no jumps.
- **Persona B — Student preparing for placements/assessments:** knows some
  coding, wants pattern recognition, complexity tradeoffs, and volume of
  practice problems.
- **Persona C — Interview candidate (SDE roles):** wants patterns cheat
  sheets, company-tagged questions, timed-practice structure, and the
  "how to think in an interview" framing for every pattern.

Every concept file should serve A (explanation), B (patterns + practice),
and C (interview framing) — see the template in file 03 for exactly where
each persona's needs are addressed.

## 4. Definition of Done

The repo is "done" only when ALL of the following are true:
- [ ] Every phase in file 02 has a folder, and every sub-topic in that
      phase has its own concept file following the file-03 template.
- [ ] Every concept file has at least the minimum number of linked
      practice problems specified in file 03, spread across difficulties.
- [ ] The root `README.md` has a full clickable table of contents in the
      exact phase order, with a one-line description per topic.
- [ ] A `PATTERNS.md` file maps every recurring pattern (two pointers,
      sliding window, fast-slow pointer, monotonic stack, DP on subsets,
      etc.) to every question in the repo that uses it.
- [ ] A `PROGRESS-TRACKER.md` (checklist format) lists every topic and
      every question so a learner can tick items off.
- [ ] A `GLOSSARY.md` defines every technical term used anywhere in the repo.
- [ ] Nothing references a topic that hasn't been taught yet (verified via
      the audit prompt in file 04).
- [ ] No file contains a placeholder, a broken link pattern, or an
      unexplained piece of C++ syntax.

## 5. How the 5 files fit together

| File | Purpose |
|---|---|
| **00 (this file)** | Mission, rules, definition of done — the "why" and "what quality bar" |
| **01** | Exact folder/file structure and naming conventions — the "where" |
| **02** | The full ordered curriculum, every topic and sub-topic — the "what content" |
| **03** | The mandatory template every file must follow — the "how it's written" |
| **04** | Batch-by-batch prompts + audit checklists — the "in what order do I ask the AI to build it" |

Do not start generating content until you (the IDE AI) have read all five
files and can restate, in your own words, the folder structure, the full
topic list, and the file template. Only then begin Phase 0 using the
prompts in file 04.
