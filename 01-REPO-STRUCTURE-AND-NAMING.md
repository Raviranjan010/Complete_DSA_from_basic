# 01 — REPO STRUCTURE & NAMING CONVENTIONS

## 1. Top-level layout

```
DSA-Zero-To-Hero/
├── README.md                     # Master TOC, how to use the repo, roadmap image/table
├── GLOSSARY.md                   # Every technical term, alphabetical, plain-English definitions
├── PATTERNS.md                   # Pattern-name -> list of questions using it (cross-repo index)
├── PROGRESS-TRACKER.md           # Checklist of every topic + every question (learner ticks off)
├── CHEATSHEETS/
│   ├── complexity-cheatsheet.md
│   ├── cpp-stl-cheatsheet.md
│   ├── recursion-cheatsheet.md
│   ├── sorting-cheatsheet.md
│   ├── graph-algorithms-cheatsheet.md
│   ├── dp-patterns-cheatsheet.md
│   └── interview-last-minute-revision.md
├── 00-prerequisites/
├── 01-complexity-analysis/
├── 02-arrays-and-strings/
├── 03-recursion-and-backtracking/
├── 04-linked-list/
├── 05-stack-and-queue/
├── 06-hashing/
├── 07-trees/
├── 08-heaps-and-priority-queue/
├── 09-graphs/
├── 10-greedy/
├── 11-dynamic-programming/
├── 12-advanced-strings/
├── 13-bit-manipulation-and-math/
├── 14-advanced-topics/
└── 15-interview-prep/
```

Phase numbers here map exactly 1:1 to the Phase numbers in
`02-COMPLETE-DSA-CURRICULUM.md`. Never rename or reorder these folders.

## 2. Inside each phase folder

Each `NN-topic-name/` folder must contain:

```
NN-topic-name/
├── README.md                  # Phase overview: what you'll learn, why it matters,
│                               #   prerequisites (linked to earlier files), roadmap of sub-topics
├── 01-subtopic-name.md        # Concept file (follows template in file 03)
├── 01-subtopic-name-practice.md   # Practice question set for that subtopic
├── 02-subtopic-name.md
├── 02-subtopic-name-practice.md
├── ...
└── phase-summary-and-quiz.md  # Recap + 10-15 self-check questions (conceptual, not coding)
```

- Sub-topic files are numbered in the exact teaching order from file 02.
- If a sub-topic is large, split it: `05a-`, `05b-` suffixes, never
  renumber existing files when inserting — use letter suffixes instead.
- Every concept file has a matching `-practice.md` sibling. Never mix
  theory and the full practice-question bank in one file (keeps files
  scannable), though 2-3 fully worked example problems DO live inside the
  concept file itself per the template in file 03.

## 3. File naming rules

- All lowercase, words separated by hyphens, no spaces, no underscores.
- Always prefix with two-digit zero-padded numbers for ordering
  (`01-`, `02-`, ... `10-`, not `1-`).
- File names must describe the concept, not be vague: use
  `03-sliding-window-technique.md`, never `topic3.md`.
- Practice files always end in `-practice.md`.
- Every folder has exactly one `README.md` (capital letters, per GitHub
  convention) — all other files are lowercase.

## 4. Root README.md required sections

1. **What this repo is** (2-3 lines) + who it's for (the 3 personas).
2. **How to use this repo** (linear reading order, or "jump to a topic"
   for revision — but recommend linear for first-time learners).
3. **Full Table of Contents** — nested list, every phase, every sub-topic,
   each linking directly to its file.
4. **Legend** for difficulty tags and pattern tags used throughout.
5. **Links** to `PATTERNS.md`, `GLOSSARY.md`, `PROGRESS-TRACKER.md`,
   `CHEATSHEETS/`.
6. **Contribution / how to keep it updated** section (even if solo project).

## 5. Cross-linking rules

- Every concept file that depends on an earlier concept must link to it
  inline the first time it's mentioned, e.g.
  "we'll use a *[hash map](../06-hashing/01-hash-map-basics.md)* here."
- Every practice file links back up to its concept file at the top.
- `PATTERNS.md` links down into every question that uses that pattern.
- `PROGRESS-TRACKER.md` links to every concept and every practice file.

## 6. Version control hygiene

- One commit per sub-topic (concept + its practice file together) —
  keeps history reviewable and lets the IDE AI generate in resumable
  batches (see file 04).
- Commit message format: `feat(phaseNN): add <subtopic-name> concept + practice`.
