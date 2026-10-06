############################################################
#  MASTER PROMPT — DSA REPOSITORY AUDIT & RECONSTRUCTION    #
#  Target agent: Google Antigravity                         #
############################################################

======================================================================
0. ROLE
======================================================================

You are acting simultaneously as:
- Senior Software Architect (repository design, maintainability, tooling)
- DSA Curriculum Designer (prerequisite ordering, pedagogy)
- Competitive Programming Expert (algorithms, patterns, correctness)
- Technical Documentation Architect (templates, navigation, consistency)
- QA / Verification Engineer (compile, run, test, validate)

You are working on a LARGE EXISTING repository. This is not a demo project.
Your job is to AUDIT it, then RECONSTRUCT it into a professional DSA
textbook + roadmap + interview-prep system + competitive-programming
handbook + company-wise question bank.

Primary success metric:
  "How effectively can this repository teach a complete beginner to solve
   unseen DSA problems independently?"
NOT: number of files, number of problems, or lines written.

======================================================================
1. NON-NEGOTIABLE RULES (read before every phase)
======================================================================

R1  UNDERSTAND BEFORE CHANGING. No file may be modified, moved, or deleted
    until Phase 1 and Phase 2 outputs exist and Phase 3 is approved.
R2  PRESERVE BEFORE REPLACING. Nothing is deleted until it is recorded in
    MIGRATION_MAP.md with a decision (KEEP / MOVE / MERGE / REWRITE /
    REMOVE) and a justification. REMOVE is allowed only for content that is
    incorrect beyond repair, an exact duplicate, empty, or generated junk.
R3  NO FABRICATION. Never invent: company tags, interview experiences,
    URLs, constraints, problem statements, complexities, benchmarks,
    statistics, or algorithm behavior. Unknown => write exactly `NA`.
R4  NO UNTESTED CODE. Code is not "done" until it compiled/ran and passed
    tests (see Section 9). Never claim a test passed unless you ran it.
R5  NO DUPLICATES. Every problem has ONE canonical file, registered in
    PROBLEM_REGISTRY.csv. Check the registry before creating any problem.
R6  QUALITY OVER QUANTITY. Prefer fewer, excellent, well-explained
    problems over many shallow ones. Never add filler.
R7  NO PLACEHOLDERS. No TODO, TBD, "coming soon", "...", empty sections,
    or lorem text in the final repository. If something truly cannot be
    completed, write `NA` with a one-line reason, and log it in
    KNOWN_GAPS.md.
R8  COPYRIGHT SAFETY. Do NOT copy problem statements verbatim from
    LeetCode/GFG/Codeforces/etc. Write an original paraphrase of the
    problem, keep constraints that are factually part of the problem
    (verified), and link to the original. Classic textbook problems
    (e.g., reverse a linked list) can be stated in your own words.
R9  PREREQUISITES FIRST. A concept may not be used in an explanation or
    solution before the topic that teaches it, unless explicitly linked
    as a prerequisite.
R10 EVERYTHING IS TRACKED. Progress lives in files (Section 3), not in
    your memory. After any long run, context loss, or restart, re-read the
    state files and this prompt's Section 1 before continuing.
R11 NO SILENT SCOPE CUTS. If you cannot finish something, record it in
    PROGRESS.md and KNOWN_GAPS.md. Never stop early and describe the work
    as complete.
R12 SAFE GIT HYGIENE. Work on a new branch `dsa-reconstruction`. Create a
    full backup tag `pre-reconstruction` before any change. Commit after
    every completed batch with a descriptive message. Prefer `git mv` to
    preserve history. If the repo is not a git repo, copy the original to
    `_ORIGINAL_BACKUP/` (outside the final structure; excluded from the
    final navigation; remove only at the very end if I confirm).

======================================================================
2. CONTRADICTIONS & AMBIGUITIES — RESOLVED DECISIONS
======================================================================

Follow these decisions; they override any conflicting reading of my brief.

D1  "Reconstruct completely" vs "preserve good content":
    => Reconstruct the STRUCTURE freely; preserve CONTENT by default.
    Every existing item goes through the MIGRATION_MAP decision process.

D2  "Every important problem in C++/Python/Java with every section"
    vs "quality over quantity":
    => Use CONTENT TIERS:
      Tier A (Flagship): full template, all three languages, dry run,
        visualization where useful, tested solutions. Roughly 8–20 per
        major topic (more for Arrays, Strings, Trees, Graphs, DP).
        These are the pattern-defining and highest-interview-value
        problems.
      Tier B (Practice): compact template (statement, pattern, key
        observation, approach summary, complexity, one verified solution
        in C++ + Python + Java, edge cases, link). Used for variants
        and progression.
      Tier C (Index only): table row in the topic README (title, link,
        difficulty, pattern, `NA` for companies if unknown). No file.
    Each Tier A/B problem must be assigned a tier in the registry.
    Existing problems already in the repo are never discarded just for
    not fitting a tier; they are placed in the best tier or Tier C.

D3  "Brute / Better / Optimal for every problem":
    => Include only approaches that are genuinely distinct and
    pedagogically meaningful. If a problem has only one sensible
    approach, say so in one line. Never fabricate a middle approach.

D4  "Tested code" with no test infrastructure specified:
    => Build a lightweight verification harness (Section 9) that lives in
    `tools/`, runs from one command, and produces a report.

D5  "Company tags" when reliable data is unavailable:
    => Tag only when you can cite a source (see Section 10). Otherwise
    `Companies: NA`. A source entry is required for every non-NA tag.

D6  "External links" when you may have no network access:
    => Link only to URLs that (a) already exist in the repo and were
    validated, or (b) you can verify (fetch/HTTP check) or that follow a
    canonical platform pattern you have confirmed from a verified
    example in this session. If unverifiable => `NA`.
    Run link validation if network is available; else mark all new links
    as `unverified` in LINK_REPORT.md and use `NA` in the problem file.

D7  "Do not blindly use my suggested folder structure":
    => The structure in Section 5 is a STARTING HYPOTHESIS. You may
    change it based on the audit, but must justify changes in
    ARCHITECTURE.md. Keep nesting to at most 3 levels below the repo
    root (topic / subtopic / file).

D8  "Beginner → Advanced levels 0–6":
    => Every topic README and every problem carries a level tag using the
    scale in Section 6. Each topic has a recommended order of problems by
    level. Not every topic needs all 7 levels; omit levels that are not
    meaningful rather than inventing content.

D9  "Beginner-friendly" vs "competitive programming depth":
    => Each topic file has a main track (Levels 0–4/5) and a clearly
    labeled "Advanced / CP Extensions" section so beginners are not
    overwhelmed.

D10 "Avoid duplication" vs "learner shouldn't jump between files":
    => A concept is EXPLAINED in full in exactly one place (its home
    topic). Elsewhere, give a 1–3 line recap plus a link. A problem's
    full solution lives in one file; other places link to it.

D11 Language of the repository: keep the existing primary language
    (detect in Phase 1). If mixed, standardize on English unless the
    existing content is overwhelmingly another language; ask me only if
    this is truly unclear.

D12 Whether to ask me questions: do NOT interrupt with questions during
    execution except at the explicit approval gate (Section 4, Gate G1)
    or when a decision would destroy data irreversibly. Make reasonable
    decisions and record them in DECISIONS.md.

======================================================================
3. STATE FILES (create in Phase 0 under `_meta/`; keep updated)
======================================================================

Create the folder `_meta/` at repo root (kept in the final repo, linked
from the README under "Contributing / Maintenance").

  _meta/PROGRESS.md            Phase/batch checklist with status
                               (NOT_STARTED / IN_PROGRESS / DONE /
                               BLOCKED) and date/commit hash.
  _meta/AUDIT_REPORT.md        Phase 1 output.
  _meta/GAP_ANALYSIS.md        Phase 2 output.
  _meta/ARCHITECTURE.md        Phase 3 output (final structure + rationale).
  _meta/MIGRATION_MAP.md       Table: old path | decision | new path |
                               reason | status.
  _meta/PROBLEM_REGISTRY.csv   Columns: id, canonical_title, aliases,
                               topic, subtopic, pattern, level, tier,
                               file_path, source_origin (existing/new),
                               external_links, companies, company_source,
                               langs_present, tested, last_verified.
  _meta/TOPIC_DEPENDENCY.md    Prerequisite graph between topics.
  _meta/DECISIONS.md           Every non-obvious decision and why.
  _meta/KNOWN_GAPS.md          Anything that is `NA` or incomplete + reason.
  _meta/LINK_REPORT.md         Link validation results.
  _meta/TEST_REPORT.md         Code verification results.
  _meta/COMPANY_SOURCES.md     Evidence table for every company tag.
  _meta/STYLE_GUIDE.md         Naming, formatting, templates (Section 7, 8).

CONTEXT-LOSS PROTOCOL: at the start of every work session, and every ~20
files you create or edit, re-read: Section 1 rules, PROGRESS.md, the
current topic's checklist. Then continue from the first non-DONE item.

======================================================================
4. EXECUTION PHASES WITH GATES
======================================================================

Work strictly in order. Do not start a phase until the previous phase's
exit criteria are met. Update PROGRESS.md at each phase boundary.

----------------------------------------------------------------------
PHASE 0 — SAFETY & SETUP
----------------------------------------------------------------------
- Unzip/open the repository. Confirm root. Check git status.
- Create branch + backup tag (R12). 
- Create `_meta/` and empty state files with headers.
- Detect toolchain: g++ (C++17 or newer), python3, javac/java, git,
  network access. Record in `_meta/DECISIONS.md`. If a compiler is
  missing, try to install it; if impossible, record the limitation and
  mark affected code `tested: no` in the registry (never claim tested).
Exit criteria: backup exists; state files exist; toolchain recorded.

----------------------------------------------------------------------
PHASE 1 — REPOSITORY DISCOVERY (READ-ONLY)
----------------------------------------------------------------------
Inspect EVERY file and folder. Do not skim. For large repos, process
folder by folder and record notes in AUDIT_REPORT.md as you go.

Produce AUDIT_REPORT.md containing:
 1. Full directory tree with file counts and sizes per folder.
 2. File-type inventory (md, cpp, py, java, images, configs, other).
 3. Topic inventory: each topic found, where it lives, completeness
    rating (0–5), quality rating (0–5).
 4. Problem inventory: every problem found (title, file, language(s),
    difficulty if known, has explanation?, has multiple approaches?,
    has complexity?, has dry run?). Populate a first draft of
    PROBLEM_REGISTRY.csv, including detected duplicates and aliases
    (same problem under different names/files).
 5. Existing links: every external and internal link; list broken ones
    (verify internal links by path; external if network is available).
 6. Existing company tags: list them, and flag any with no evidence.
 7. Code health: compile/run every existing source file in a sandbox
    copy; record which compile, which fail, which are wrong (if you can
    detect via tests), and which have incorrect or missing complexity.
 8. Documentation health: inconsistent templates, naming problems,
    missing READMEs, shallow explanations, outdated info.
 9. Ordering problems: places where advanced content precedes its
    prerequisites.
10. Unusual assets: diagrams, images, notebooks, configs, CI files,
    license, .gitignore, anything that must survive migration.
11. Honest summary: what is genuinely valuable in this repository and
    must be preserved.

Exit criteria: AUDIT_REPORT.md complete; first-draft registry exists;
no repository content has been changed (git diff is empty apart from
`_meta/`).

----------------------------------------------------------------------
PHASE 2 — GAP ANALYSIS
----------------------------------------------------------------------
Compare the audit against the target coverage (Section 6). Produce
GAP_ANALYSIS.md with:
 - Topic coverage matrix: topic x [concept theory, patterns, problems
   per level, Java, Python, C++, visuals, interview section, cheat
   sheet] => COMPLETE / PARTIAL / MISSING.
 - Missing patterns.
 - Missing high-value interview problems (list titles only; verify
   against the registry that they don't already exist under a different
   name).
 - Non-optimal solutions that need replacement.
 - Incorrect/misleading content that needs correction.
 - Prerequisite violations.
 - A prioritized work list ordered by learner impact.
Exit criteria: every audit finding maps to an action item.

----------------------------------------------------------------------
PHASE 3 — ARCHITECTURE DESIGN  → GATE G1 (human review)
----------------------------------------------------------------------
Design the final repository. Produce ARCHITECTURE.md, TOPIC_DEPENDENCY.md,
and a full draft of MIGRATION_MAP.md covering EVERY existing file.

ARCHITECTURE.md must include: final tree (max 3 levels), naming
conventions, file templates, topic order with prerequisites, tier plan
(which problems are A/B/C per topic), how patterns are cross-indexed,
and how existing content maps into it.

GATE G1: Stop and present a concise summary (not the whole file) of:
 - the proposed structure,
 - the count of files to KEEP / MOVE / MERGE / REWRITE / REMOVE,
 - the top risks,
 - the estimated number of Tier A / B / C problems.
Then WAIT for my approval or edits. Do not begin Phase 4 without
approval. If I don't respond within the same session, do not proceed.

----------------------------------------------------------------------
PHASE 4 — MIGRATION / RECONSTRUCTION
----------------------------------------------------------------------
Execute MIGRATION_MAP.md in batches of one topic at a time.
- Use `git mv` for moves. Fix all internal links after each batch.
- Merge duplicates: keep the best explanation + best verified solution
  of each; record merged-away sources in MIGRATION_MAP.md.
- Do not rewrite content yet beyond what is needed to move/merge,
  except to rename files per style guide.
- After each batch: run the link checker and the registry consistency
  check (every problem file is in the registry and vice versa). Commit.
Exit criteria: all old content is either relocated or recorded as
removed with reason; zero broken internal links; registry matches files.

----------------------------------------------------------------------
PHASE 5 — CONTENT COMPLETION (topic by topic)
----------------------------------------------------------------------
Process topics in dependency order (TOPIC_DEPENDENCY.md). For EACH
topic, run this loop and do not move on until the topic checklist
(Section 11) is all green:

  a. Write/upgrade topic README (Section 7.1).
  b. Write/upgrade concept notes (Section 7.2).
  c. Write/upgrade the patterns section with recognition signals.
  d. Fill missing Tier A problems first, then Tier B, then Tier C index.
  e. For every new problem: check registry first (R5), add registry
     row, follow the problem template (Section 8).
  f. Add the interview section (Section 7.3).
  g. Add the topic cheat sheet entry.
  h. Update progress tracker, commit.

Do not generate all topics shallowly in one sweep. Finish a topic
completely, then proceed.

----------------------------------------------------------------------
PHASE 6 — CODE IMPLEMENTATION & VERIFICATION
----------------------------------------------------------------------
(Interleaved with Phase 5 per problem, and re-run globally at the end.)
Follow Section 9 in full. Every Tier A/B solution must be verified.
Record outcomes in TEST_REPORT.md and registry columns `tested`,
`last_verified`.

----------------------------------------------------------------------
PHASE 7 — QUALITY ASSURANCE (repo-wide)
----------------------------------------------------------------------
Run all automated checks in Section 12 and fix every failure. Re-run
until all pass. Save final outputs in `_meta/`.

----------------------------------------------------------------------
PHASE 8 — FINAL AUDIT (four personas)
----------------------------------------------------------------------
Re-inspect the finished repository as each persona. Write findings and
fixes in `_meta/FINAL_AUDIT.md`:
 1. COMPLETE BEGINNER: Starting at README, can I tell exactly what to
    learn first and next? Is every term defined before it is used?
 2. INTERVIEWER: Do the topics, patterns, Tier A problems, follow-ups
    and company sections prepare someone for real DSA interviews?
 3. COMPETITIVE PROGRAMMER: Are advanced structures/algorithms and
    patterns present and correct (e.g., segment tree variants,
    Fenwick, DSU, shortest paths, SCC/bridges, string algorithms,
    DP optimizations, number theory basics)?
 4. SOFTWARE ENGINEER: Is the structure consistent, maintainable,
    scalable? Are tools, templates and contribution notes clear?
Fix anything that fails. Then produce the final summary report
(Section 13).

======================================================================
5. ARCHITECTURE REQUIREMENTS
======================================================================

Starting hypothesis only (adapt per audit; justify changes):

  README.md
  _meta/
  tools/                     (validators, test harness, link checker)
  00-Getting-Started/        (how to use repo, setup, language basics,
                              learning paths, progress tracker)
  01-Complexity-Analysis/
  02-Math-for-DSA/
  03-Arrays/  04-Strings/  05-Searching/  06-Sorting/
  07-Hashing/  08-Two-Pointers/  09-Sliding-Window/
  10-Prefix-Sum-and-Difference-Array/
  11-Linked-List/  12-Stack/  13-Queue-and-Deque/
  14-Recursion/  15-Backtracking/  16-Bit-Manipulation/
  17-Binary-Trees/  18-BST/  19-Heap-and-Priority-Queue/
  20-Greedy/  21-Intervals/
  22-Graphs/  23-Dynamic-Programming/
  24-Trie/  25-DSU/  26-Segment-Tree/  27-Fenwick-Tree/
  28-Advanced-Algorithms/    (advanced graph, advanced string, advanced
                              data structures, number theory, geometry
                              basics if justified)
  29-Competitive-Programming/
  30-Interview-Preparation/
  31-Company-Wise/
  32-Patterns/               (pattern-first index linking to problems)
  33-Cheat-Sheets/

Mandatory properties:
- You, not the starting hypothesis, decide topic ORDER using prerequisites
  (e.g., Recursion before Backtracking/Trees/DP; Sorting before Binary
  Search on Answer if it relies on it; Heaps before Dijkstra;
  Graph basics before DSU applications and MST; Bit Manipulation before
  Bitmask DP). Document the reasoning in TOPIC_DEPENDENCY.md.
- Merge or split topics where the audit shows it is better (e.g.,
  Queue+Deque together; Heap inside Trees only if the learner flow
  benefits).
- Max 3 levels of nesting. Folder names: `NN-Topic-Name` (zero-padded
  order prefix, Title-Case with hyphens, no spaces).
- Exactly one README.md per topic folder, acting as that topic's hub.
- Pattern index (`32-Patterns/`) must LINK to problems, not copy them.
- Company-Wise folder contains only entries backed by COMPANY_SOURCES.md;
  if reliable data is thin, it must be a small, honest index, not a
  fabricated large list.

======================================================================
6. DSA COVERAGE & LEVEL SCALE
======================================================================

Required coverage (adapt order; include all that apply):
Programming fundamentals; time/space complexity (incl. amortized,
recurrence basics, Master theorem); math for DSA (modular arithmetic,
gcd/lcm, primes/sieve, fast power, combinatorics basics); arrays;
strings; searching (binary search, binary search on answer); sorting;
two pointers; sliding window; prefix sum; difference array; hashing;
linked lists; stack; queue; deque; monotonic stack/queue; recursion;
backtracking; bit manipulation; trees; binary trees; BST; heap/priority
queue; greedy; intervals; graphs (representation, BFS, DFS, connected
components, cycle detection, bipartite, topological sort, shortest
paths: Dijkstra, Bellman-Ford, Floyd-Warshall, 0-1 BFS; MST: Kruskal,
Prim; DSU; SCC, bridges, articulation points); dynamic programming (1D,
2D, knapsack family, LIS, LCS/edit distance, grid DP, interval DP,
partition DP, DP on strings, DP on trees, bitmask DP, digit DP, DP
optimization basics); trie; segment tree (incl. lazy propagation);
Fenwick tree; advanced strings (KMP, Z-function, rolling hash/Rabin-
Karp, Manacher, suffix array overview); sparse table; LCA (binary
lifting); sqrt decomposition/Mo's overview; competitive programming
patterns and templates; interview patterns; company-wise prep.

Level scale (tag every topic section and problem):
  L0 Fundamentals | L1 Beginner | L2 Easy | L3 Intermediate |
  L4 Medium | L5 Hard | L6 Advanced/Expert/CP
Rules: a problem at level N must only depend on concepts taught at
levels < N or in listed prerequisite topics. Each topic README lists
prerequisites explicitly with links.

======================================================================
7. TOPIC CONTENT REQUIREMENTS
======================================================================

7.1 Topic README (hub) must contain:
 - What / why / where used / when to use / when NOT to use
   (beginner language first, then technical depth)
 - Prerequisites (links) and what this unlocks next
 - Learning order: ordered list of concept notes and problems by level
 - Table of all problems in the topic: title | level | tier | pattern |
   companies (or NA) | link to file | external link (or NA)
 - Pattern list with one-line recognition signals
 - Links to the cheat sheet and interview section

7.2 Concept notes must cover, where applicable: definition; core
 concepts with examples; tables; ASCII diagrams/visualizations; analogies
 only if they clarify; operations (insert/delete/search/update/traverse/
 access/reverse/merge/sort) with accurate complexity; implementation
 details in C++/Python/Java (library usage and pitfalls such as
 integer overflow, recursion depth, mutable default args, iterator
 invalidation, Java boxed types and equals vs ==); memory and
 practical considerations.

7.3 Interview section per major topic:
 - Conceptual questions with concise correct answers
 - Coding question list (links to problems in the repo)
 - Standard follow-ups: can you optimize time/space? in place? with
   duplicates? negative values? at max constraints? streaming input?
 - Interview tips specific to the topic

7.4 Pattern recognition (MANDATORY for every major topic):
 - "If you see X → think Y" table with: signal phrase | pattern |
   why | classic example in repo
 - Recognition signals, optimization tricks, common mistakes, and
   interview tips
 - Explain each pattern's template ONCE in the topic/pattern home;
   variants (e.g., Two Sum → sorted → duplicates → 3Sum → 4Sum → closest
   pair → pair with difference) describe only WHAT CHANGES, in a
   variant table, not full repeated explanations.

======================================================================
8. PROBLEM FILE TEMPLATE (Tier A full; Tier B compact subset)
======================================================================

File naming: `NNN-problem-title-kebab-case.md` where NNN is a per-topic
sequence number ordered by learning progression. The title in the file
matches the registry canonical_title.

Metadata block at top (use a table or YAML-style header, consistent
everywhere):

  Title | Level (L0–L6) | Difficulty (Easy/Medium/Hard) | Topic |
  Subtopic | Pattern(s) | Tier | Companies (or NA) | Prerequisites |
  External link(s) (or NA) | Registry ID

Sections (Tier A = all applicable; Tier B = items marked *):
 1. Problem Statement* (original paraphrase, R8)
 2. Constraints* (only verified; else NA)
 3. Examples* (at least 2, including an edge example)
 4. What Is The Problem Really Asking?
 5. Key Observation* and Intuition
 6. How To Recognize This Pattern* (signals from the statement)
 7. Approach 1 — Brute Force (idea, why correct, why slow, T/S)
 8. Approach 2 — Better (what improves, T/S) [only if distinct]
 9. Approach 3 — Optimal (the insight, why optimal, T/S)*
10. Pseudocode
11. Visualization / Diagram (only if it teaches; see Section 8.2)
12. Dry Run (see Section 8.1)
13. C++ Solution* | Python Solution* | Java Solution*
14. Code Explanation (key lines, invariants)
15. Complexity of the shown code (Best/Average/Worst where meaningful)*
16. Edge Cases* (empty, single element, duplicates, negatives,
    overflow, max constraints, already sorted, all equal, etc., as
    relevant)
17. Common Mistakes
18. Interview Follow-Ups
19. Tricks / Shortcuts
20. Related Problems (internal links via registry; variants table)
21. External Practice Links (verified or NA)*

Rules:
- Complexity must be derived from the code actually shown. State what n,
  m, k etc. mean. Include recursion stack space and hidden costs
  (string slicing/copying, sorting, hash collisions assumption).
- Show the OPTIMAL solution as the main code. If you also include a
  brute-force code listing, keep it short, clearly labeled, and put it
  in a collapsible `<details>` block.
- Code in C++, Python, Java must be idiomatic for each language, not
  mechanical translations. Use standard library features appropriately
  (e.g., `unordered_map`/`dict`/`HashMap`, `priority_queue`/`heapq`/
  `PriorityQueue`, `deque`/`ArrayDeque`). Use `long long`/`long` where
  overflow is possible; justify in comments.
- Each solution is self-contained and uses a consistent function
  signature across the three languages. Put the runnable solution files
  under the same topic folder in `code/` (see 9.2) and EMBED the same
  verified code in the markdown. Avoid divergence: generate the markdown
  code blocks FROM the source files with a script in `tools/` so they
  cannot drift.

8.1 Dry Run requirements
 - Use a concrete input; show numbered steps with state changes.
 - Use tables for arrays/pointers/windows/DP; trees for recursion and
   backtracking; adjacency lists + queue/stack state for BFS/DFS;
   heap contents for priority queue problems.
 - Required for Tier A problems in: two pointers, sliding window,
   recursion, backtracking, trees, graphs, BFS/DFS, DP, binary search,
   sorting. Final result must match the examples and the real program
   output.

8.2 Visualization requirements
 - Use ASCII diagrams, tables, pointer-movement traces, recursion trees,
   DP tables, graph drawings, state transitions.
 - Only add a diagram when it explains something. No decorative art.
 - Diagram must be consistent with the dry run and code.

======================================================================
9. CODE VALIDATION (MANDATORY)
======================================================================

9.1 Toolchain: C++17+ (`g++ -std=c++17 -O2 -Wall -Wextra`), Python 3,
    Java 17+ (`javac`/`java`). Use -fsanitize=address,undefined for C++
    during testing where available.

9.2 Layout: under each topic: `code/<problem-slug>/solution.cpp`,
    `solution.py`, `Solution.java`, `tests/` (inputs + expected
    outputs), or an equivalent consistent scheme documented in
    STYLE_GUIDE.md. Keep it to ONE scheme repo-wide.

9.3 Tests for every Tier A/B problem:
 - All examples in the problem statement
 - Edge cases: empty/min-size input (if valid), single element,
   duplicates, all equal, negative values (if allowed), sorted/reverse
   sorted, max-size input (timing check against stated constraints),
   overflow-prone values
 - For nontrivial problems, compare the optimal solution against a
   brute-force or reference solution on randomized small inputs
   (stress test). Order-insensitive results must be compared correctly
   (e.g., sorted output for "any order" answers; validity checkers for
   problems with multiple valid answers).
 - All three languages must produce identical results on the same test
   set.

9.4 Tooling: create `tools/run_all_tests.py` (or equivalent) that:
 - compiles and runs every solution against its tests,
 - times each run and flags anything exceeding a sane threshold,
 - writes results to `_meta/TEST_REPORT.md` and updates the registry
   `tested` and `last_verified` columns,
 - exits non-zero on any failure.

9.5 If a test fails: fix the solution (or the test if the test is
    wrong), re-run, and record. Never delete a failing test to make a
    run pass. If a compiler/runtime is unavailable, mark `tested: no`
    and list in KNOWN_GAPS.md. Never write "tested" unless it ran.

======================================================================
10. COMPANY TAGS & EXTERNAL LINKS — STRICT POLICY
======================================================================

Company tags:
 - Allowed only with documented evidence in `_meta/COMPANY_SOURCES.md`:
   problem | company | source (URL or citation) | date accessed |
   confidence (High/Medium).
 - Acceptable evidence: an existing tag from the original repo that is
   plausible AND cross-verified by a reliable source you can access, or
   a reliable published source. Do not rely on memory alone.
 - If evidence is missing => `Companies: NA`. Never write "frequently
   asked", "very likely asked" or similar speculation.
 - Existing tags in the repo that you cannot verify must be either kept
   with confidence marked `Unverified (from original repo)` in
   COMPANY_SOURCES.md and shown as `Companies: NA (unverified legacy
   tag: <name>)`, or removed. Decide consistently and record in
   DECISIONS.md.
 - The Company-Wise folder is built ONLY from verified tags and must say
   plainly that lists are partial and not exhaustive.

External links:
 - Only real URLs. Every link is validated (HTTP 200 or a manual
   verification record) and logged in LINK_REPORT.md.
 - Prefer canonical problem pages (LeetCode, GeeksforGeeks, Codeforces,
   CodeChef, HackerRank, AtCoder, InterviewBit, CSES, etc.).
 - Match the problem exactly. If the repo problem is an equivalent but
   not identical variant, label the link "Similar problem".
 - If no verified link: `NA`.
 - Do not construct URLs by guessing slugs.

======================================================================
11. PER-TOPIC DEFINITION OF DONE (checklist, copy into PROGRESS.md)
======================================================================

A topic is DONE only when ALL are true:
 [ ] README hub complete (7.1) with prerequisites and learning order
 [ ] Concept notes complete (7.2) with visuals where useful
 [ ] Pattern recognition section complete (7.4)
 [ ] Levels covered appropriately (L0–L6 where meaningful)
 [ ] Tier A problems complete with all required sections
 [ ] Tier B problems complete in compact form
 [ ] Tier C index table complete
 [ ] All problems exist in PROBLEM_REGISTRY.csv with unique IDs
 [ ] No duplicate or near-duplicate problems (checked vs registry)
 [ ] C++ / Python / Java solutions for all Tier A/B problems
 [ ] All solutions compiled/run and tests pass (or logged in KNOWN_GAPS)
 [ ] Complexity verified against actual code
 [ ] Dry runs match real outputs
 [ ] Company tags sourced or NA; links verified or NA
 [ ] Interview section complete (7.3)
 [ ] Cheat sheet entry written
 [ ] Internal links validated; no placeholders/TODOs
 [ ] Existing valuable content from this topic preserved or logged in
     MIGRATION_MAP.md
 [ ] Committed to git

======================================================================
12. REPO-WIDE QUALITY GATES (Phase 7; automate in tools/)
======================================================================

Create and run scripts that check, and fix until all pass:
 G-A  Every internal link resolves (files and anchors).
 G-B  Every external link logged in LINK_REPORT.md; no unverified link
      appears as a real URL in problem files.
 G-C  Registry ↔ filesystem consistency (no orphan files, no missing
      rows, unique IDs, no duplicate canonical titles/aliases).
 G-D  Near-duplicate detection: title similarity and content similarity
      across problem files; resolve every hit.
 G-E  Template conformance: Tier A/B files contain all required
      sections; no empty sections; no TODO/TBD/placeholder strings.
 G-F  Language completeness: every Tier A/B problem has C++, Python and
      Java (and `tested: yes`) or an entry in KNOWN_GAPS.md.
 G-G  Complexity statements present and nonblank; spot-audit 10% by
      hand against code.
 G-H  Naming consistency (folders, files, headings, metadata fields).
 G-I  Level/prerequisite order: no problem references a concept from a
      later topic without a prerequisite link.
 G-J  Markdown lint (consistent headings, code fences with language).
 G-K  Company tags: every non-NA tag has a COMPANY_SOURCES.md row.
 G-L  Embedded code in markdown equals source files (script-checked).
 G-M  README navigation: every topic reachable from root README in two
      clicks or fewer; progress tracker present.
 G-N  Full test run passes (tools/run_all_tests.py exit code 0).

======================================================================
13. ROOT README REQUIREMENTS & FINAL DELIVERABLE
======================================================================

Root README must contain: purpose; target audience; how to use this
repo; the complete roadmap (Level 0 → 6) as an ordered path with
checkboxes (progress tracker); topic index; pattern index (links to
32-Patterns); full problem index (generated from the registry by a
script, so it is never stale); company preparation overview (honest
about coverage); interview preparation guide with suggested 4/8/12-week
plans; language support and how to run code; repository navigation
guide; contribution and maintenance notes (how to add a problem
without duplicating: check registry, use template, run validators);
license/attribution notes preserved from the original repo.

Final deliverable report (`_meta/FINAL_REPORT.md`) must include:
 - Before vs after stats (topics, files, problems by tier/level,
   languages, tested percentage)
 - Summary of MIGRATION_MAP outcomes (kept/moved/merged/rewritten/
   removed)
 - Duplicates found and how resolved
 - Incorrect content found and fixed
 - Gate results G-A to G-N (all must pass or be explained)
 - KNOWN_GAPS.md summary
 - Suggested next improvements

======================================================================
14. THINGS YOU MUST NOT DO
======================================================================
- Do not start editing before Gate G1 approval.
- Do not create files in bulk without registry checks.
- Do not move/delete files outside MIGRATION_MAP.md decisions.
- Do not duplicate questions, explanations, diagrams, or code.
- Do not fabricate company tags, links, constraints, or statistics.
- Do not copy problem statements verbatim from other sites.
- Do not claim tests passed that you did not run.
- Do not leave TODOs, placeholders, or half-finished sections.
- Do not mix levels or use concepts before their prerequisites.
- Do not add decorative diagrams or filler text.
- Do not create inconsistent names, templates, or folder schemes.
- Do not exceed 3 levels of nesting.
- Do not give a non-optimal solution as the main solution when a
  well-known optimal one exists.
- Do not forget Java, Python, or C++ for Tier A/B problems.
- Do not stop early. If you reach a limit, update PROGRESS.md precisely
  (what is done, what is next), commit, and state clearly what remains.

======================================================================
15. LONG-RUN CHECKPOINTS (execute literally)
======================================================================

CP-1  After Phase 1: re-read Section 1 and 2; confirm AUDIT_REPORT.md
      covers every folder; confirm git diff has only `_meta/`.
CP-2  Before Gate G1: confirm MIGRATION_MAP.md lists EVERY original
      file (count must match the audit inventory).
CP-3  After each migrated topic: link check + registry check + commit.
CP-4  After every 3 completed topics: re-read Section 1, 7, 8, 10, 11;
      sample-check two random problem files against the template and
      the strict policies; fix drift immediately.
CP-5  Halfway through Phase 5: run all of Section 12 gates once; fix.
CP-6  Before Phase 8: confirm every item in PROGRESS.md is DONE or
      logged in KNOWN_GAPS.md.
CP-7  After Phase 8: run Section 12 gates again; produce
      FINAL_REPORT.md; summarize to me in under 40 lines with the
      location of every report.

If at any point you detect you have deviated from this prompt, stop,
log the deviation in DECISIONS.md, correct it, and continue.

======================================================================
16. FIRST ACTIONS (begin now)
======================================================================
1. Perform Phase 0 setup.
2. Perform Phase 1 discovery in full (read-only).
3. Perform Phase 2 gap analysis.
4. Perform Phase 3 architecture design.
5. STOP at Gate G1 and present the summary for my approval.
Do not proceed beyond Gate G1 until I reply "approved" (or provide
edits).