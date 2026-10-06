# Architectural & Engineering Decisions Log (`DECISIONS.md`)

This file records all significant design decisions, tradeoffs, toolchain findings, and policy resolutions.

## Toolchain Detection & Environment Setup
- **C++ Compiler**: LLVM-MinGW (UCRT runtime, Clang 22.1.8). Dynamic path resolution implemented in `tools/env_setup.py` without hardcoded paths. All C++ compiled with `-std=c++17 -O2 -Wall -Wextra`.
- **Python**: Verified `Python 3.12.10` available on Windows.
- **Java**: Verified `javac 24.0.2` and `java 24.0.2` available. Per User Condition 6, all Java files compiled with `javac --release 17`.
- **Git**: Verified `git version 2.52.0.windows.1`. Line endings normalized via `.gitattributes` (`* text=auto eol=lf`).
- **Network Access**: Verified active HTTP connectivity (HTTP 200 to external endpoints).
- **Git Hygiene**: Created backup tag `before-merge` and working branch `merge-and-organize`.

---

## Core Architectural Decisions (D1–D12)

### D1: Content Preservation vs Structure Reconstruction
- **Decision**: Restructure the repository into a clean, 3-level hierarchy (`NN-Topic-Name/subtopic/problem.md`). Preserve high-value educational content from the 5 historical sub-repositories (`DSA_server-main`, `DSA_ac-main`, `Summer_pep_DSA-main`, `DSA_final-main`, `dsa-main`).
- **Rationale**: The repository was an unmerged accumulation of multiple study initiatives. Consolidating them topic-by-topic eliminates massive redundancy while keeping the richest explanations.

### D2: Content Tiers (Tier A, Tier B, Tier C)
- **Decision**:
  - **Tier A (Flagship)**: Full template, complete explanations, multiple approaches (brute/better/optimal where distinct), dry run, visual trace, tested code in C++, Python, and Java.
  - **Tier B (Practice)**: Compact template with problem statement, pattern, intuition, verified C++/Python/Java solutions, complexity, edge cases, and external link.
  - **Tier C (Index)**: Curated practice problems listed in topic README tables linking to external canonical platforms.
  - Target per-topic allocation matrix documented in `_meta/STRUCTURE_PLAN.md`.

### D3: Binary & Junk File Cleanup
- **Decision**: In `dsa-main`, 14 compiled `.exe` files and 0-byte files are removed. Non-empty scratch files (such as `DSA_final-main/commit.txt`) are moved to `_archive/`.
- **Rationale**: Strict compliance with Non-Negotiable Rule R3 and User Condition 1.

### D4: Company Tags & Sourcing Policy
- **Decision**: Legacy company tags inherited from original repositories are mapped in `_meta/COMPANY_SOURCES.md` and listed in problems as `Companies: NA (unverified legacy tag: <Name>)`. No fabricated or guessed company tags.
- **Rationale**: Strict compliance with Golden Rule R5 (No Fake Information).

### D5: External Links & Verification Policy
- **Decision**: Only canonical problem URLs (LeetCode, GeeksforGeeks, Codeforces, HackerRank, InterviewBit, CSES) that resolve to valid problem statements are linked. Unverified or guessed URLs are designated `NA`.

### D6: Multi-Language Parity (C++, Python, Java)
- **Decision**: While existing source code was almost 100% C++, Tier A and Tier B problems will have verified implementations in all three languages: C++17, Python 3, and Java 17 (`--release 17`).

### D7: Root Zip Backup Exclusion
- **Decision**: `Complete_DSA_from_basic-main.zip` and all zip backups are explicitly ignored via `.gitignore` and kept outside git commits.
- **Rationale**: User Condition 2: Root archive files must not inflate git history.

### D8: Non-Compiling C++ Source Resolution & Repair
- **Decision**: Four C++ source files that previously failed compilation are investigated and repaired rather than deleted:
  1. `dsa-main/1_factorial.cpp`: Incomplete file ending with `int`. Completed with standard recursive factorial implementation and driver `main()`.
  2. `dsa-main/7_sort_Squared_array.cpp`: Syntax errors (`v([right_ptr])`, missing `#include <algorithm>`, `count` instead of `cout`, missing function argument). Repaired with two-pointer squared array algorithm.
  3. `dsa-main/8_increment_address.cpp`: 0-byte file. Populated with pointer increment and address demonstration from `DSA_final-main/01_Basics_Of_Cpp/08_pointers.md`.
  4. `DSA_final-main/01_Basics_Of_Cpp/operators.cpp`: Misnamed file containing markdown text. Markdown notes preserved in `concepts/03-operators.md`; C++ demonstration code created to illustrate all operators described.

### D9: Phase 4 Pure Merge Scope
- **Decision**: In Phase 4, existing educational content and source files are de-duplicated, consolidated, and organized topic-by-topic. Stub READMEs and cheatsheets are maintained until Phase 5, where they are expanded and upgraded.
- **Rationale**: User Condition 4: Keeps structural migration decoupled from content generation.

### D10: Compiler PATH Discovery Without Hardcoding
- **Decision**: Implemented `tools/env_setup.py` using Windows registry and WinGet directory introspection to discover `g++`, `javac`, and `python` dynamically at runtime.
- **Rationale**: User Condition 7: Ensures portable and reproducible test runs across developer machines.

### D11: Topic-by-Topic Merge & Verification Cycle
- **Decision**: Topics are merged sequentially according to prerequisite order. After each topic:
  1. Link check is executed.
  2. `_meta/PROBLEM_REGISTRY.csv` is updated.
  3. `_meta/MERGE_LEDGER.csv` logs base source and additions.
  4. Changes are committed to git.
  5. Every 3 topics, rules from Section 2 are audited and sampled.

### D12: Branch & Tag Reconciliation (D11 Resolution)

#### Raw Git Outputs:

\\	ext
$ git branch -a
  dsa-reconstruction
* main
  merge-and-organize
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/merge-and-organize

$ git tag
before-merge
pre-reconstruction

$ git log --oneline -n 15
d5dc223 feat: add link validation report for repository documentation
1bce236 feat: add time complexity benchmarking implementations and link validation utilities
1076249 feat: add time complexity benchmarking solutions in C++, Java, and Python with flake testing tool
1d048db feat: add initial start-here problems, solutions, and progress tracking tools
dcffb9a fix(02-Math-for-DSA): fix LaTeX formula escaping in 001 problem doc
af7331a feat(02-Math-for-DSA): upgrade topic hub README, complete 6 Tier A flagship problems with C++17, Python3, and Java17 solutions, and fill curriculum gaps (Sieve, SPF, Modular Inverse)
058cb99 feat(01-Complexity-Analysis): upgrade topic hub README and complete Tier A benchmark & space complexity suites with C++17, Python3, and Java17 solutions
80392c1 feat(00-Start-Here): upgrade topic hub README and complete Tier A flagship problems with C++17, Python3, and Java17 solutions
321c242 docs(progress): complete Phase 4 migration and initialize Phase 5 topic tracking
1523fad test(tools): add parallel C++17 compilation checker script
7426011 fix(links): normalize internal markdown links across all module concepts and problems
47f3a2f feat: complete Phase 4 pure merge - migrate all 255 files, remove junk, archive raw leftovers
8e8adf6 feat(15-Bit-Manipulation): migrate bitwise operations, bitmasking, and bit tricks code
89badd0 feat(14-Dynamic-Programming): migrate 1D/2D DP patterns, advanced DP notes, and code
f06e61a feat(13-Graphs): migrate graph representations, traversals, shortest paths, and code
\
#### Plain Reconciliation Statement:
Earlier planning documents intermittently referenced branch \dsa-reconstruction\ and tag \pre-reconstruction\, whereas the agreed operational working branch was \merge-and-organize\ and backup tag was \efore-merge\. Both tags (\efore-merge\ and \pre-reconstruction\) point to the identical pre-reconstruction commit 80394143b325dccc19355ac0b77e6f89437634b\. All completed commits on \merge-and-organize\ have been fast-forward merged directly into \main\ and pushed to \origin/main\, so local \main\, local \merge-and-organize\, and remote \origin/main\ are now fully synchronized at HEAD.
