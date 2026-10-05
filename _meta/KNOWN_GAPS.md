# Known Gaps & Incomplete Content Log (`KNOWN_GAPS.md`)

This log explicitly tracks all areas where content is missing, incomplete, or marked `NA`, adhering to Rule R7 (No Placeholders) and Rule R11 (No Silent Scope Cuts).

## 1. Language Support Gaps in Original Repo
- **Current State**: 99% of original code is C++. There are virtually zero Python or Java implementations in existing problem files.
- **Target Resolution**: During Phase 5, all Tier A and Tier B problems will be provided with tested C++, Python, and Java implementations.

## 2. Topic Coverage Gaps in Original Repo
- **02-Math-for-DSA**: Only 1 basic note existed; lacks modular arithmetic, fast power, GCD/LCM, sieve, combinatorics.
- **21-Intervals**: Scattered across Arrays; lacks dedicated pattern hub (Merge Intervals, Insert Interval, Non-overlapping).
- **25-DSU (Disjoint Set Union)**: Mentioned briefly in graphs; lacks dedicated topic hub and path compression/union by rank explanations.
- **27-Fenwick-Tree / Segment-Tree Lazy**: Only a high-level summary note existed; lacks full implementation and range update problems.
- **28-Advanced-String-Algorithms**: KMP, Z-Algorithm, and Rabin-Karp only exist as raw unannotated snippets; need systematic teaching.

## 3. Code Health Gaps in Original Repo
- 4 original C++ files failed compilation:
  - `dsa-main/1_factorial.cpp` (truncated code)
  - `dsa-main/7_sort_Squared_array.cpp` (syntax typo)
  - `dsa-main/8_increment_address.cpp` (empty file)
  - `DSA_final-main/01_Basics_Of_Cpp/operators.cpp` (misnamed markdown file)
- Solution files currently lack automated unit test cases (`tests/input.txt`, `tests/output.txt`).

## 4. Documentation & Link Gaps
- 423 broken internal links in legacy root planning documents.
- Cheatsheet files in `CHEATSHEETS/` are stubs that state "Full content will be populated during finalization".
