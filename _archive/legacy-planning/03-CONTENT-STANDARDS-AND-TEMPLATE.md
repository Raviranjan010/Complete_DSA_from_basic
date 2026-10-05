# 03 — CONTENT STANDARDS & MANDATORY TEMPLATE

Every concept file and every practice file MUST follow the structure
below exactly. This keeps the whole repo predictable so a learner never
has to "figure out" how a page is organized.

---

## A. TEMPLATE — Concept File (`NN-subtopic-name.md`)

```markdown
# <Subtopic Title>

**Phase:** <phase number & name> | **Prerequisites:** [linked concept files]
**Difficulty to grasp:** Beginner / Intermediate / Advanced
**Pattern tag(s):** e.g. `#two-pointers`, `#sliding-window`

## 1. Why this matters (motivation)
Plain-English real-world or coding-problem scenario that makes the reader
FEEL why this concept is needed, before any formal definition.

## 2. Intuition first
Explain the idea with an analogy or a hand-drawn-style ASCII diagram
BEFORE introducing formal terms or code. Assume zero prior exposure.

## 3. Formal explanation
Now introduce the precise definition/terminology, building on the
intuition above. Define every new term inline the first time it's used.

## 4. Step-by-step dry run
Walk through one small example, step by step (state after each step),
using either a numbered list or an ASCII diagram — never skip a step.

## 5. C++ implementation
- Full, runnable, compilable code (C++17).
- Every line that uses syntax/STL not yet explained gets an inline comment
  explaining it the first time (and links to Phase 0/relevant cheatsheet).
- Include `#include` statements and a `main()` with sample input/output
  when it's a full program; a standalone function is fine if it's part of
  a bigger structure already taught.

## 6. Complexity analysis
- Time complexity: derivation, not just the final answer.
- Space complexity: derivation.
- Best/average/worst case if they differ.

## 7. Common mistakes & edge cases
Bullet list of the specific bugs beginners hit (off-by-one, integer
overflow, empty input, single-element input, etc.) and how to avoid them.

## 8. How this shows up in interviews
1-2 sentences: what interviewers are really testing with this concept,
and the follow-up questions/variants they commonly ask.

## 9. Worked examples (2-3 fully solved problems, in this file)
For each: problem statement → intuition → approach → full code →
complexity. These are teaching examples, not the full practice bank.

## 10. Practice more
Link to the sibling `NN-subtopic-name-practice.md` file for the full
question bank on this topic.

## 11. What's next
One line pointing to the next file in sequence, and why it builds on this.
```

---

## B. TEMPLATE — Practice File (`NN-subtopic-name-practice.md`)

```markdown
# <Subtopic Title> — Practice Questions

Back to concept: [<Subtopic Title>](./NN-subtopic-name.md)

## Legend
🟢 Easy   🟡 Medium   🔴 Hard
Pattern tags shown in `#backticks` — cross-referenced in ../../PATTERNS.md

## Question List

| # | Question | Difficulty | Pattern | Link(s) |
|---|----------|------------|---------|---------|
| 1 | <Question name> | 🟢 | `#pattern` | [LeetCode](url) · [GfG](url) |
| 2 | ... | 🟡 | `#pattern` | [LeetCode](url) |
| ... | | | | |

## Minimum coverage required per subtopic
- At least 8-12 questions per subtopic (more for high-yield topics like
  arrays, DP, trees, graphs — aim for 20-30 there).
- Spread: ~40% Easy, ~40% Medium, ~20% Hard.
- At least 2 questions per subtopic must include a **fully worked
  solution walkthrough** below the table (approach + code + complexity),
  not just a link — pick the most instructive one(s).
- Every question row MUST link to at least one real platform. Preferred
  order: LeetCode → GeeksforGeeks → Codeforces → HackerRank →
  Coding Ninjas/Naukri Code360. Never fabricate a problem URL — if the
  exact URL isn't known for certain, link to the platform's search page
  for that problem's name instead.

## Fully worked solutions
### Q<N>: <Question name>
**Problem:** ...
**Approach:** ...
**Code:**
```cpp
...
```
**Complexity:** ...
```

---

## C. Formatting & style rules (apply everywhere)

1. **Reading level:** short sentences, one idea per sentence, no jargon
   without an immediate definition. Prefer active voice.
2. **No forward references** without a link — if you must mention a term
   not yet taught, link to where it WILL be taught and say "we'll cover
   this in Phase X" rather than assuming knowledge.
3. **Diagrams:** use simple ASCII/Markdown diagrams or numbered
   state-tables for anything spatial (trees, linked lists, arrays,
   pointers moving). Never describe a multi-step pointer movement in
   prose only.
4. **Code style:** consistent 4-space indentation, meaningful variable
   names (`left`/`right` not `l`/`r` on first introduction of a pattern,
   though short names are fine once the pattern is familiar), comments
   explain *why*, not just *what*.
5. **Difficulty tags** must be consistent repo-wide (defined once in the
   root README legend, reused everywhere — never invent new tags per file).
6. **Pattern tags** must come from a single controlled vocabulary list
   maintained in `PATTERNS.md` — check that file before inventing a new tag.
7. **Every file** starts with a one-line breadcrumb back to its phase
   README and, where relevant, its prerequisites.
8. **Every file** ends with a "What's next" pointer — the reader should
   never have to think "where do I go now?"
9. **Self-check questions:** each phase's `phase-summary-and-quiz.md` has
   10-15 conceptual (non-coding) questions with answers, to test
   understanding before moving to the next phase.

## D. Quality bar checklist (apply to every single file before it's "done")

- [ ] Could a total beginner follow section 1-4 with zero prior context?
- [ ] Is every technical term defined at first use or linked to `GLOSSARY.md`?
- [ ] Does the code compile conceptually (no syntax errors, correct headers)?
- [ ] Is the complexity analysis derived, not just stated?
- [ ] Are common mistakes specific (not generic "be careful with edge cases")?
- [ ] Do all practice links point to real platforms (not fabricated URLs)?
- [ ] Is this file cross-linked from its phase README and, if applicable,
      from `PATTERNS.md`?
- [ ] Does nothing in this file use an unexplained concept from a later phase?
