# Comprehensive Structure Plan & File Migration Architecture (`STRUCTURE_PLAN.md`)

**Date**: 2026-10-05  
**Architect**: Google Antigravity  
**Specification**: Master Prompt Section 6 (Phase 3 Design) & Golden Rules R1–R12.

---

## 1. Executive Summary & Decision Totals

- **Total Files Audited**: 255 files (100% of all files across 5 sources, numbered stubs, and root)
- **MERGE**: 136 files (Consolidating educational notes and problem sets into topic hubs)
- **MOVE**: 58 files (Direct migration of C++ solution source codes and root indexes)
- **REWRITE**: 25 files (Replacing 16 stub READMEs, 7 stub cheatsheets, root README & tracker)
- **REMOVE-JUNK**: 20 files (14 `.exe` binaries, 4 IDE runner artifacts, 2 0-byte/scratch files)
- **ARCHIVE**: 9 files (Root zip snapshot, 5 legacy root planning files, 3 legacy config files)
- **EXTRA**: 7 files (Emscripten WebAssembly student project batch scripts/readme, HTML tutorial, Library Management console app)
- **Reconciliation Total**: 136 + 58 + 25 + 20 + 9 + 7 = **255 files** (100% accounted for).

---

## 2. Proposed Final Repository Layout (Level 2 Tree)

```
DSA-Master/
├── README.md                          # Master learning portal, roadmap & navigation
├── 00-Start-Here/                     # Onboarding, environment setup, study plans, tracker
│   ├── README.md
│   ├── concepts/                      # Setup guides, C++ vs Java vs Python primers
│   └── reference/                     # GLOSSARY.md, PATTERNS.md
├── 01-Complexity-Analysis/            # Big-O, Big-Theta, Big-Omega, recurrence relations
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 02-Math-for-DSA/                   # Number theory, modular arithmetic, GCD, prime sieve
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 03-Arrays-and-Strings/             # Fundamentals, traversal, in-place ops, Kadane, 2D arrays
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 04-Searching-and-Sorting/          # Binary search (array & answer), sorting algorithms
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 05-Two-Pointers-and-Sliding-Window/# Opposite ends, fast/slow, fixed/variable window
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 06-Hashing/                        # Hash maps/sets, collision resolution, frequency counting
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 07-Recursion-and-Backtracking/     # Call stack, recursion trees, state-space exploration
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 08-Linked-List/                    # Singly/doubly linked list, cycle detection, reversals
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 09-Stack-and-Queue/                # Monotonic stack/queue, deque, min-stack
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 10-Trees/                          # Binary trees, BST, LCA, traversals, view problems
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 11-Heap-and-Priority-Queue/        # Min/max heap, heapify, top-K, median finding
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 12-Greedy-and-Intervals/           # Activity selection, interval scheduling & merging
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 13-Graphs/                         # BFS/DFS, Dijkstra, Bellman-Ford, Floyd, topological sort
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 14-Dynamic-Programming/            # 1D, 2D, knapsack, LCS, LIS, space optimizations
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 15-Bit-Manipulation/               # Bitwise tricks, bitmasking, subsets
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 16-Strings-Advanced/               # KMP, Z-algorithm, Rabin-Karp
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 17-Advanced-Data-Structures/       # Trie, DSU (Disjoint Set), Segment Tree, Fenwick (BIT)
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 18-Advanced-Algorithms/            # Tarjan SCC, Bridges, Euler tour, CP extras
│   ├── README.md
│   ├── concepts/
│   ├── problems/
│   └── code/
├── 19-Interview-Preparation/          # Company collections, mock sets, interview strategy
│   ├── README.md
│   ├── company-questions/
│   └── mock-assessments/
├── 20-Cheatsheets/                    # Dense high-yield quick references
│   ├── README.md
│   └── *.md
├── _extras/                           # Standalone non-DSA projects
│   ├── wasm-student-record/           # Emscripten WebAssembly student record project
│   ├── console-projects/              # LibraryManagement console application
│   └── web-tutorials/                 # HTML Form tutorial demo
├── _archive/                          # Raw snapshots, legacy configs, legacy planning
├── _meta/                             # Audits, manifests, progress, registries, decisions
└── tools/                             # Test runner, link checker, code verification scripts
```

---

## 3. Inside Topic Directory Layout

Every topic folder (`01-Complexity-Analysis` to `18-Advanced-Algorithms`) strictly adheres to a uniform 3-level maximum structure:
```
NN-Topic-Name/
├── README.md        # Topic hub: overview, prerequisites, roadmap, problem table
├── concepts/        # Theory & pattern notes (e.g. 01-intro.md, 02-patterns.md)
├── problems/        # Individual problem files (e.g. 001-two-sum.md)
└── code/            # Multi-language solutions (001-two-sum/solution.cpp, solution.py, Solution.java)
```

---

## 4. Naming Conventions

- **Folders**: `NN-Topic-Name` (2-digit zero-padded prefix, Capitalized-Words, hyphens, no spaces).
- **Concept Files**: `NN-concept-name.md` (2-digit order prefix, kebab-case).
- **Problem Files**: `NNN-problem-name.md` (3-digit zero-padded canonical problem ID, kebab-case).
- **Code Directory**: `code/NNN-problem-name/` containing:
  - `solution.cpp` (C++17)
  - `solution.py` (Python 3)
  - `Solution.java` (Java 24)

---

## 5. Content Tier Plan

- **Tier A (Flagship Problems, 8-20 per major topic)**: Complete 21-section template, multi-language solutions (C++, Python, Java), dry run trace, diagram/table, complexity derivation, tested in test runner.
- **Tier B (Practice Problems)**: Compact template (Problem statement, key pattern, brute/optimal approaches, tested C++/Python/Java implementations, complexity, edge cases, external link).
- **Tier C (Index Only)**: Problems cataloged in topic README problem tables with title, difficulty level, pattern, and canonical external practice link.

### Target Tier Allocations by Topic

| Module | Topic Name | Tier A Target | Tier B Target | Tier C Target | Total Problems |
|---|---|---|---|---|---|
| `01` | Complexity Analysis | 5 | 8 | 10 | 23 |
| `02` | Math for DSA | 8 | 12 | 15 | 35 |
| `03` | Arrays and Strings | 18 | 25 | 40 | 83 |
| `04` | Searching and Sorting | 14 | 20 | 25 | 59 |
| `05` | Two Pointers and Sliding Window | 12 | 18 | 20 | 50 |
| `06` | Hashing | 10 | 15 | 20 | 45 |
| `07` | Recursion and Backtracking | 12 | 16 | 20 | 48 |
| `08` | Linked List | 10 | 15 | 20 | 45 |
| `09` | Stack and Queue | 10 | 15 | 20 | 45 |
| `10` | Trees | 14 | 20 | 25 | 59 |
| `11` | Heap and Priority Queue | 8 | 12 | 15 | 35 |
| `12` | Greedy and Intervals | 10 | 15 | 18 | 43 |
| `13` | Graphs | 14 | 20 | 25 | 59 |
| `14` | Dynamic Programming | 18 | 25 | 30 | 73 |
| `15` | Bit Manipulation | 8 | 12 | 15 | 35 |
| `16` | Strings Advanced | 6 | 10 | 12 | 28 |
| `17` | Advanced Data Structures | 8 | 12 | 15 | 35 |
| `18` | Advanced Algorithms | 6 | 10 | 12 | 28 |
| **Total**| — | **191** | **280** | **377** | **848** |


---

## 6. Dependency Sequencing Rationale

1. `00-Start-Here`: Basic language syntax, environment, pointers, and memory layout.
2. `01-Complexity-Analysis`: Big-O, loop counting, recurrence foundations before evaluating algorithms.
3. `02-Math-for-DSA`: Modulo, primes, bitwise foundations needed across array and hashing problems.
4. `03-Arrays-and-Strings`: Foundational contiguous memory structures, basic transformations.
5. `04-Searching-and-Sorting`: Binary search & sorting algorithms depend on 1D arrays.
6. `05-Two-Pointers-and-Sliding-Window`: Applied pointer techniques on sorted arrays and subarrays.
7. `06-Hashing`: Hash sets/maps for O(1) lookups; unlocks frequency counting and lookup optimizations.
8. `07-Recursion-and-Backtracking`: Call stack, base cases, state space trees. Prerequisite for trees and DP.
9. `08-Linked-List`: Dynamic node-based pointer structures.
10. `09-Stack-and-Queue`: LIFO/FIFO linear structures, monotonic stack/queue.
11. `10-Trees`: Hierarchical recursive node structures, DFS/BFS traversals, BST.
12. `11-Heap-and-Priority-Queue`: Complete binary tree array representation, greedy top-K.
13. `12-Greedy-and-Intervals`: Greedy choice property, interval scheduling, sorting prerequisites.
14. `13-Graphs`: Generalized node-edge relationships; builds on BFS/DFS (trees), priority queues (Dijkstra).
15. `14-Dynamic-Programming`: Optimal substructure, overlapping subproblems; builds on recursion and arrays.
16. `15-Bit-Manipulation`: Low-level operations, bitmasks for subset DP.
17. `16-Strings-Advanced`: KMP, Z-algorithm, string hashing.
18. `17-Advanced-Data-Structures`: Trie, DSU, Segment Tree, Fenwick Tree.
19. `18-Advanced-Algorithms`: Tarjan SCC, Bridges, LCA, competitive programming algorithms.
20. `19-Interview-Preparation`: Company sheets, mock assessments, interview synthesis.
21. `20-Cheatsheets`: Final review reference guides.

---

## 7. Full File Migration Mapping Table (All 255 Original Files)

| Original Path | Decision | New Path | Reason |
|---|---|---|---|
| 00-MASTER-PROMPT.md | **ARCHIVE** | _archive/legacy-planning/00-MASTER-PROMPT.md | Legacy planning document superseded by master architecture |
| 01-REPO-STRUCTURE-AND-NAMING.md | **ARCHIVE** | _archive/legacy-planning/01-REPO-STRUCTURE-AND-NAMING.md | Legacy planning document superseded by master architecture |
| 02-COMPLETE-DSA-CURRICULUM.md | **ARCHIVE** | _archive/legacy-planning/02-COMPLETE-DSA-CURRICULUM.md | Legacy planning document superseded by master architecture |
| 03-CONTENT-STANDARDS-AND-TEMPLATE.md | **ARCHIVE** | _archive/legacy-planning/03-CONTENT-STANDARDS-AND-TEMPLATE.md | Legacy planning document superseded by master architecture |
| 04-EXECUTION-PLAN-AND-PROMPTS.md | **ARCHIVE** | _archive/legacy-planning/04-EXECUTION-PLAN-AND-PROMPTS.md | Legacy planning document superseded by master architecture |
| Complete_DSA_from_basic-main.zip | **ARCHIVE** | _archive/Complete_DSA_from_basic-main.zip | Original root repository archive snapshot |
| DSA_MASTER_PROMPT.md | **REMOVE-JUNK** | NA | Empty 0-byte file (DSA_MASTER_PROMPT.md) |
| GLOSSARY.md | **MOVE** | 00-Start-Here/GLOSSARY.md | Preserved core reference index file in 00-Start-Here |
| PATTERNS.md | **MOVE** | 00-Start-Here/PATTERNS.md | Preserved core reference index file in 00-Start-Here |
| PROGRESS-TRACKER.md | **REWRITE** | PROGRESS-TRACKER.md | Master navigation portal & full learning roadmap |
| README.md | **REWRITE** | README.md | Master navigation portal & full learning roadmap |
| 00-prerequisites/README.md | **REWRITE** | 00-prerequisites/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 01-complexity-analysis/README.md | **REWRITE** | 01-complexity-analysis/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 02-arrays-and-strings/README.md | **REWRITE** | 02-arrays-and-strings/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 03-recursion-and-backtracking/README.md | **REWRITE** | 03-recursion-and-backtracking/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 04-linked-list/README.md | **REWRITE** | 04-linked-list/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 05-stack-and-queue/README.md | **REWRITE** | 05-stack-and-queue/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 06-hashing/README.md | **REWRITE** | 06-hashing/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 07-trees/README.md | **REWRITE** | 07-trees/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 08-heaps-and-priority-queue/README.md | **REWRITE** | 08-heaps-and-priority-queue/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 09-graphs/README.md | **REWRITE** | 09-graphs/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 10-greedy/README.md | **REWRITE** | 10-greedy/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 11-dynamic-programming/README.md | **REWRITE** | 11-dynamic-programming/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 12-advanced-strings/README.md | **REWRITE** | 12-advanced-strings/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 13-bit-manipulation-and-math/README.md | **REWRITE** | 13-bit-manipulation-and-math/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 14-advanced-topics/README.md | **REWRITE** | 14-advanced-topics/README.md | Replaced 1-line stub with comprehensive topic hub README |
| 15-interview-prep/README.md | **REWRITE** | 15-interview-prep/README.md | Replaced 1-line stub with comprehensive topic hub README |
| CHEATSHEETS/complexity-cheatsheet.md | **REWRITE** | 20-Cheatsheets/complexity-cheatsheet.md | Expanded stub into high-yield cheatsheet |
| CHEATSHEETS/cpp-stl-cheatsheet.md | **REWRITE** | 20-Cheatsheets/cpp-stl-cheatsheet.md | Expanded stub into high-yield cheatsheet |
| CHEATSHEETS/dp-patterns-cheatsheet.md | **REWRITE** | 20-Cheatsheets/dp-patterns-cheatsheet.md | Expanded stub into high-yield cheatsheet |
| CHEATSHEETS/graph-algorithms-cheatsheet.md | **REWRITE** | 20-Cheatsheets/graph-algorithms-cheatsheet.md | Expanded stub into high-yield cheatsheet |
| CHEATSHEETS/interview-last-minute-revision.md | **REWRITE** | 20-Cheatsheets/interview-last-minute-revision.md | Expanded stub into high-yield cheatsheet |
| CHEATSHEETS/recursion-cheatsheet.md | **REWRITE** | 20-Cheatsheets/recursion-cheatsheet.md | Expanded stub into high-yield cheatsheet |
| CHEATSHEETS/sorting-cheatsheet.md | **REWRITE** | 20-Cheatsheets/sorting-cheatsheet.md | Expanded stub into high-yield cheatsheet |
| dsa-main/.gitignore | **ARCHIVE** | _archive/dsa-main/.gitignore | Legacy sub-project gitignore preserved in archive |
| dsa-main/10_remove_Occurence(a).cpp | **MOVE** | code/dsa-solutions/10_remove_Occurence(a).cpp | Migrated compiling C++ solution code |
| dsa-main/10sum_interval.cpp | **MOVE** | code/dsa-solutions/10sum_interval.cpp | Migrated compiling C++ solution code |
| dsa-main/11_Matrix_muktiplication.cpp | **MOVE** | code/dsa-solutions/11_Matrix_muktiplication.cpp | Migrated compiling C++ solution code |
| dsa-main/11_Matrix_muktiplication.exe | **REMOVE-JUNK** | NA | Compiled binary executable (11_Matrix_muktiplication.exe) |
| dsa-main/11_Palindrome.cpp | **MOVE** | code/dsa-solutions/11_Palindrome.cpp | Migrated compiling C++ solution code |
| dsa-main/12_printing_numbers.cpp | **MOVE** | code/dsa-solutions/12_printing_numbers.cpp | Migrated compiling C++ solution code |
| dsa-main/13_k_Multiple_of_n.cpp | **MOVE** | code/dsa-solutions/13_k_Multiple_of_n.cpp | Migrated compiling C++ solution code |
| dsa-main/14_sum_of_natural_num_with_alternateign.cpp | **MOVE** | code/dsa-solutions/14_sum_of_natural_num_with_alternateign.cpp | Migrated compiling C++ solution code |
| dsa-main/15_GCD_recursion.cpp | **MOVE** | code/dsa-solutions/15_GCD_recursion.cpp | Migrated compiling C++ solution code |
| dsa-main/16_Armstrong_Number_check.cpp | **MOVE** | code/dsa-solutions/16_Armstrong_Number_check.cpp | Migrated compiling C++ solution code |
| dsa-main/17_Frog_jump.cpp | **MOVE** | code/dsa-solutions/17_Frog_jump.cpp | Migrated compiling C++ solution code |
| dsa-main/1_basic.cpp | **MOVE** | code/dsa-solutions/1_basic.cpp | Migrated compiling C++ solution code |
| dsa-main/1_factorial.cpp | **MOVE** | code/dsa-solutions/1_factorial.cpp | Migrated compiling C++ solution code |
| dsa-main/2_valueAtAddreaa.cpp | **MOVE** | code/dsa-solutions/2_valueAtAddreaa.cpp | Migrated compiling C++ solution code |
| dsa-main/3_updatingValueUsingPointer.cpp | **MOVE** | code/dsa-solutions/3_updatingValueUsingPointer.cpp | Migrated compiling C++ solution code |
| dsa-main/4_recursive_sum_of_Digitts.cpp | **MOVE** | code/dsa-solutions/4_recursive_sum_of_Digitts.cpp | Migrated compiling C++ solution code |
| dsa-main/4_swaping_value.cpp | **MOVE** | code/dsa-solutions/4_swaping_value.cpp | Migrated compiling C++ solution code |
| dsa-main/5_firstAndLastOccurence.cpp | **MOVE** | code/dsa-solutions/5_firstAndLastOccurence.cpp | Migrated compiling C++ solution code |
| dsa-main/5_p_to_the_power_q_UsingRecursion.cpp | **MOVE** | code/dsa-solutions/5_p_to_the_power_q_UsingRecursion.cpp | Migrated compiling C++ solution code |
| dsa-main/5_sort_zero_One.cpp | **MOVE** | code/dsa-solutions/5_sort_zero_One.cpp | Migrated compiling C++ solution code |
| dsa-main/6_IncrementDecrement.cpp | **MOVE** | code/dsa-solutions/6_IncrementDecrement.cpp | Migrated compiling C++ solution code |
| dsa-main/6_even_int_move2.cpp | **MOVE** | code/dsa-solutions/6_even_int_move2.cpp | Migrated compiling C++ solution code |
| dsa-main/7_array_recursive.cpp | **MOVE** | code/dsa-solutions/7_array_recursive.cpp | Migrated compiling C++ solution code |
| dsa-main/7_prepostArithematic.cpp | **MOVE** | code/dsa-solutions/7_prepostArithematic.cpp | Migrated compiling C++ solution code |
| dsa-main/7_sort_Squared_array.cpp | **MOVE** | code/dsa-solutions/7_sort_Squared_array.cpp | Migrated compiling C++ solution code |
| dsa-main/7_sort_Squared_array.exe | **REMOVE-JUNK** | NA | Compiled binary executable (7_sort_Squared_array.exe) |
| dsa-main/8_increment_address.cpp | **REMOVE-JUNK** | NA | Empty 0-byte file (8_increment_address.cpp) |
| dsa-main/8_max_ele_inArray_recursive.cpp | **MOVE** | code/dsa-solutions/8_max_ele_inArray_recursive.cpp | Migrated compiling C++ solution code |
| dsa-main/8_prefix_sum.cpp | **MOVE** | code/dsa-solutions/8_prefix_sum.cpp | Migrated compiling C++ solution code |
| dsa-main/9_check_prefix_sum.cpp | **MOVE** | code/dsa-solutions/9_check_prefix_sum.cpp | Migrated compiling C++ solution code |
| dsa-main/9_sum_array_ele_usingRecursion.cpp | **MOVE** | code/dsa-solutions/9_sum_array_ele_usingRecursion.cpp | Migrated compiling C++ solution code |
| dsa-main/Count_occurence.cpp | **MOVE** | code/dsa-solutions/Count_occurence.cpp | Migrated compiling C++ solution code |
| dsa-main/LibraryManagement.cpp | **EXTRA** | _extras/console-projects/LibraryManagement.cpp | Standalone student console library management application |
| dsa-main/README.md | **EXTRA** | _extras/wasm-student-record/README.md | Emscripten WebAssembly student demo documentation |
| dsa-main/adding_removing.cpp | **MOVE** | code/dsa-solutions/adding_removing.cpp | Migrated compiling C++ solution code |
| dsa-main/adding_removing.exe | **REMOVE-JUNK** | NA | Compiled binary executable (adding_removing.exe) |
| dsa-main/arr_manipulation.cpp | **MOVE** | code/dsa-solutions/arr_manipulation.cpp | Migrated compiling C++ solution code |
| dsa-main/arr_manipulation.exe | **REMOVE-JUNK** | NA | Compiled binary executable (arr_manipulation.exe) |
| dsa-main/arr_manipulation1.cpp | **MOVE** | code/dsa-solutions/arr_manipulation1.cpp | Migrated compiling C++ solution code |
| dsa-main/basic_array.cpp | **MOVE** | code/dsa-solutions/basic_array.cpp | Migrated compiling C++ solution code |
| dsa-main/build.bat | **EXTRA** | _extras/wasm-student-record/build.bat | Emscripten WebAssembly student demo build/run script |
| dsa-main/check_sorted_or_not.cpp | **MOVE** | code/dsa-solutions/check_sorted_or_not.cpp | Migrated compiling C++ solution code |
| dsa-main/delete_add.cpp | **MOVE** | code/dsa-solutions/delete_add.cpp | Migrated compiling C++ solution code |
| dsa-main/deploy.bat | **EXTRA** | _extras/wasm-student-record/deploy.bat | Emscripten WebAssembly student demo build/run script |
| dsa-main/even-odd.cpp | **MOVE** | code/dsa-solutions/even-odd.cpp | Migrated compiling C++ solution code |
| dsa-main/even_int_move.cpp | **MOVE** | code/dsa-solutions/even_int_move.cpp | Migrated compiling C++ solution code |
| dsa-main/even_int_move.exe | **REMOVE-JUNK** | NA | Compiled binary executable (even_int_move.exe) |
| dsa-main/even_int_move2.exe | **REMOVE-JUNK** | NA | Compiled binary executable (even_int_move2.exe) |
| dsa-main/frequency_query.cpp | **MOVE** | code/dsa-solutions/frequency_query.cpp | Migrated compiling C++ solution code |
| dsa-main/frequency_query.exe | **REMOVE-JUNK** | NA | Compiled binary executable (frequency_query.exe) |
| dsa-main/largest.cpp | **MOVE** | code/dsa-solutions/largest.cpp | Migrated compiling C++ solution code |
| dsa-main/largest.exe | **REMOVE-JUNK** | NA | Compiled binary executable (largest.exe) |
| dsa-main/launch.json | **REMOVE-JUNK** | NA | IDE scratch/runner artifact (launch.json) |
| dsa-main/linear_search2.cpp | **MOVE** | code/dsa-solutions/linear_search2.cpp | Migrated compiling C++ solution code |
| dsa-main/linear_search2.exe | **REMOVE-JUNK** | NA | Compiled binary executable (linear_search2.exe) |
| dsa-main/linerr_search.cpp | **MOVE** | code/dsa-solutions/linerr_search.cpp | Migrated compiling C++ solution code |
| dsa-main/linerr_search.exe | **REMOVE-JUNK** | NA | Compiled binary executable (linerr_search.exe) |
| dsa-main/matrix_Transpose.cpp | **MOVE** | code/dsa-solutions/matrix_Transpose.cpp | Migrated compiling C++ solution code |
| dsa-main/matrix_Transpose.exe | **REMOVE-JUNK** | NA | Compiled binary executable (matrix_Transpose.exe) |
| dsa-main/occurence.exe | **REMOVE-JUNK** | NA | Compiled binary executable (occurence.exe) |
| dsa-main/printing_elements.cpp | **MOVE** | code/dsa-solutions/printing_elements.cpp | Migrated compiling C++ solution code |
| dsa-main/reverse_arr.cpp | **MOVE** | code/dsa-solutions/reverse_arr.cpp | Migrated compiling C++ solution code |
| dsa-main/second_largest.cpp | **MOVE** | code/dsa-solutions/second_largest.cpp | Migrated compiling C++ solution code |
| dsa-main/serve.bat | **EXTRA** | _extras/wasm-student-record/serve.bat | Emscripten WebAssembly student demo build/run script |
| dsa-main/settings.json | **REMOVE-JUNK** | NA | IDE scratch/runner artifact (settings.json) |
| dsa-main/target_sum.cpp | **MOVE** | code/dsa-solutions/target_sum.cpp | Migrated compiling C++ solution code |
| dsa-main/target_sum2.cpp | **MOVE** | code/dsa-solutions/target_sum2.cpp | Migrated compiling C++ solution code |
| dsa-main/tempCodeRunnerFile.cpp | **REMOVE-JUNK** | NA | IDE scratch/runner artifact (tempCodeRunnerFile.cpp) |
| dsa-main/tempCodeRunnerFile.exe | **REMOVE-JUNK** | NA | Compiled binary executable (tempCodeRunnerFile.exe) |
| dsa-main/user_input_vector.cpp | **MOVE** | code/dsa-solutions/user_input_vector.cpp | Migrated compiling C++ solution code |
| dsa-main/user_input_vector.exe | **REMOVE-JUNK** | NA | Compiled binary executable (user_input_vector.exe) |
| dsa-main/vector_basic.cpp | **MOVE** | code/dsa-solutions/vector_basic.cpp | Migrated compiling C++ solution code |
| dsa-main/verify.bat | **EXTRA** | _extras/wasm-student-record/verify.bat | Emscripten WebAssembly student demo build/run script |
| DSA_ac-main/02_Cpp_Control_Flow_Conditional_Statements_DSA_Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/02_Cpp_Control_Flow_Conditional_Statements_DSA_Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/C++ Fundamentals for DSA.md | **MERGE** | 00-Start-Here/concepts/C++ Fundamentals for DSA.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_ac-main/README.md | **MERGE** | 03-Arrays-and-Strings/concepts/README.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/01_Arrays_Complete_DSA_Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/01_Arrays_Complete_DSA_Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/02_Cpp_Vectors_and_Advanced_Array_DSA_Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/02_Cpp_Vectors_and_Advanced_Array_DSA_Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/03_DSA_Pair_Sum_Majority_Element_Brute_Better_Optimal.md | **MERGE** | 03-Arrays-and-Strings/concepts/03_DSA_Pair_Sum_Majority_Element_Brute_Better_Optimal.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/03_DSA_Time_and_Space_Complexity_Notes.md | **MERGE** | 01-Complexity-Analysis/concepts/03_DSA_Time_and_Space_Complexity_Notes.md | Merged educational notes/problem analysis into 01-Complexity-Analysis |
| DSA_ac-main/Array/04_DSA_Binary_Exponentiation_and_Stock_Problem_Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/04_DSA_Binary_Exponentiation_and_Stock_Problem_Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/05_DSA_Container_With_Most_Water_Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/05_DSA_Container_With_Most_Water_Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/06_DSA_Product_of_Array_Except_Self_LeetCode_238.md | **MERGE** | 03-Arrays-and-Strings/concepts/06_DSA_Product_of_Array_Except_Self_LeetCode_238.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_ac-main/Array/07_DSA_CPP_Pointers_Complete_Notes.md | **MERGE** | 00-Start-Here/concepts/07_DSA_CPP_Pointers_Complete_Notes.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_ac-main/Array/08_DSA_Binary_Search_Complete_Notes.md | **MERGE** | 04-Searching-and-Sorting/concepts/08_DSA_Binary_Search_Complete_Notes.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_final-main/README.md | **MERGE** | 03-Arrays-and-Strings/concepts/README.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_final-main/commit.txt | **REMOVE-JUNK** | NA | Temporary git command notes |
| DSA_final-main/index.html | **EXTRA** | _extras/web-tutorials/html-form-guide.html | HTML Form Tags & Validation tutorial (non-DSA web material) |
| DSA_final-main/01_Basics_Of_Cpp/01_introcution.md | **MERGE** | 00-Start-Here/concepts/01_introcution.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/02_Type_Casting.md | **MERGE** | 00-Start-Here/concepts/02_Type_Casting.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/03_Operators.md | **MERGE** | 00-Start-Here/concepts/03_Operators.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/04_Conditional.md | **MERGE** | 00-Start-Here/concepts/04_Conditional.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/05_loop.md | **MERGE** | 00-Start-Here/concepts/05_loop.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/05_pattern.md | **MERGE** | 00-Start-Here/concepts/05_pattern.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/06__functions.md | **MERGE** | 00-Start-Here/concepts/06__functions.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/06_functions.cpp | **MERGE** | 00-Start-Here/concepts/06_functions.cpp | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/07_BinaryNumber_system.md | **MERGE** | 00-Start-Here/concepts/07_BinaryNumber_system.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/08_pointers.md | **MERGE** | 00-Start-Here/concepts/08_pointers.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/01_Basics_Of_Cpp/operators.cpp | **MERGE** | 00-Start-Here/concepts/operators.cpp | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/02_Arrays/01_basics.md | **MERGE** | 03-Arrays-and-Strings/concepts/01_basics.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_final-main/02_Arrays/02_PassedByValue_and_PassedByReference.md | **MERGE** | 03-Arrays-and-Strings/concepts/02_PassedByValue_and_PassedByReference.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_final-main/02_Arrays/03_Binary Search.md | **MERGE** | 04-Searching-and-Sorting/concepts/03_Binary Search.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_final-main/02_Arrays/04_Pointers_and_Arrays.md | **MERGE** | 00-Start-Here/concepts/04_Pointers_and_Arrays.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_final-main/02_Arrays/05_Subarrays_and_Kadanes_Algorithm.md | **MERGE** | 03-Arrays-and-Strings/concepts/05_Subarrays_and_Kadanes_Algorithm.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/CLAUDE.md | **ARCHIVE** | _archive/DSA_server-main/CLAUDE.md | Legacy instruction/tracking file preserved in archive |
| DSA_server-main/DSA-MasterCourse/README.md | **MERGE** | 03-Arrays-and-Strings/concepts/README.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/ROADMAP.md | **MERGE** | 03-Arrays-and-Strings/concepts/ROADMAP.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/STUDY_PLAN.md | **MERGE** | 03-Arrays-and-Strings/concepts/STUDY_PLAN.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/status.txt | **ARCHIVE** | _archive/DSA_server-main/status.txt | Legacy instruction/tracking file preserved in archive |
| DSA_server-main/DSA-MasterCourse/00_Prerequisites/00_mcqs.md | **MERGE** | 00-Start-Here/concepts/00_mcqs.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/00_Prerequisites/00_notes.md | **MERGE** | 00-Start-Here/concepts/00_notes.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/01_Complexity_Analysis/01_mcqs.md | **MERGE** | 01-Complexity-Analysis/concepts/01_mcqs.md | Merged educational notes/problem analysis into 01-Complexity-Analysis |
| DSA_server-main/DSA-MasterCourse/01_Complexity_Analysis/01_notes.md | **MERGE** | 01-Complexity-Analysis/concepts/01_notes.md | Merged educational notes/problem analysis into 01-Complexity-Analysis |
| DSA_server-main/DSA-MasterCourse/02_Arrays/ARRAY_MASTER_NOTES.md | **MERGE** | 03-Arrays-and-Strings/concepts/ARRAY_MASTER_NOTES.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/PROBLEM_INDEX.md | **MERGE** | 03-Arrays-and-Strings/concepts/PROBLEM_INDEX.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/README.md | **MERGE** | 03-Arrays-and-Strings/concepts/README.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/REORGANIZATION_COMPLETE.md | **MERGE** | 03-Arrays-and-Strings/concepts/REORGANIZATION_COMPLETE.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/01_Array_Basics.md | **MERGE** | 03-Arrays-and-Strings/concepts/01_Array_Basics.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/02_Memory_Model.md | **MERGE** | 03-Arrays-and-Strings/concepts/02_Memory_Model.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/03_Operations_Complexity.md | **MERGE** | 01-Complexity-Analysis/concepts/03_Operations_Complexity.md | Merged educational notes/problem analysis into 01-Complexity-Analysis |
| DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/04_Vector_vs_Array.md | **MERGE** | 03-Arrays-and-Strings/concepts/04_Vector_vs_Array.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/00_Fundamentals/05_Easy_Problems.md | **MERGE** | 03-Arrays-and-Strings/concepts/05_Easy_Problems.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Mistakes.md | **MERGE** | 00-Start-Here/concepts/Mistakes.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Notes.md | **MERGE** | 00-Start-Here/concepts/Notes.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Patterns.md | **MERGE** | 00-Start-Here/concepts/Patterns.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Easy.md | **MERGE** | 00-Start-Here/concepts/Easy.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Hard.md | **MERGE** | 00-Start-Here/concepts/Hard.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Medium.md | **MERGE** | 00-Start-Here/concepts/Medium.md | Merged educational notes/problem analysis into 00-Start-Here |
| DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Mistakes.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/Mistakes.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Notes.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/Notes.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Patterns.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/Patterns.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Easy.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/Easy.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Hard.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/Hard.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Medium.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/Medium.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Mistakes.md | **MERGE** | 03-Arrays-and-Strings/concepts/Mistakes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Patterns.md | **MERGE** | 03-Arrays-and-Strings/concepts/Patterns.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Problems/Easy_Medium.md | **MERGE** | 03-Arrays-and-Strings/concepts/Easy_Medium.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Problems/Hard.md | **MERGE** | 03-Arrays-and-Strings/concepts/Hard.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Mistakes.md | **MERGE** | 03-Arrays-and-Strings/concepts/Mistakes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Patterns.md | **MERGE** | 03-Arrays-and-Strings/concepts/Patterns.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Problems/Medium_Hard.md | **MERGE** | 03-Arrays-and-Strings/concepts/Medium_Hard.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Mistakes.md | **MERGE** | 04-Searching-and-Sorting/concepts/Mistakes.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Notes.md | **MERGE** | 04-Searching-and-Sorting/concepts/Notes.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Patterns.md | **MERGE** | 04-Searching-and-Sorting/concepts/Patterns.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/2D_Arrays.md | **MERGE** | 04-Searching-and-Sorting/concepts/2D_Arrays.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Easy.md | **MERGE** | 04-Searching-and-Sorting/concepts/Easy.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Hard.md | **MERGE** | 04-Searching-and-Sorting/concepts/Hard.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Medium.md | **MERGE** | 04-Searching-and-Sorting/concepts/Medium.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Medium_Hard.md | **MERGE** | 04-Searching-and-Sorting/concepts/Medium_Hard.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Medium_Problems/Complete_Solutions.md | **MERGE** | 03-Arrays-and-Strings/concepts/Complete_Solutions.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Mistakes.md | **MERGE** | 03-Arrays-and-Strings/concepts/Mistakes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/Notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Patterns.md | **MERGE** | 03-Arrays-and-Strings/concepts/Patterns.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Easy.md | **MERGE** | 03-Arrays-and-Strings/concepts/Easy.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Easy_Medium_Hard.md | **MERGE** | 03-Arrays-and-Strings/concepts/Easy_Medium_Hard.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Hard.md | **MERGE** | 03-Arrays-and-Strings/concepts/Hard.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/06_Vector/Problems/Medium.md | **MERGE** | 03-Arrays-and-Strings/concepts/Medium.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/07_Hard_Problems/Complete_Solutions.md | **MERGE** | 03-Arrays-and-Strings/concepts/Complete_Solutions.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/08_Pattern_Recognition/Complete_Guide.md | **MERGE** | 03-Arrays-and-Strings/concepts/Complete_Guide.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/09_Common_Mistakes/Complete_Guide.md | **MERGE** | 03-Arrays-and-Strings/concepts/Complete_Guide.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/10_MCQs/Arrays_MCQs.md | **MERGE** | 03-Arrays-and-Strings/concepts/Arrays_MCQs.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/02_Arrays/11_Interview_Prep/Arrays_Interview.md | **MERGE** | 19-Interview-Preparation/concepts/Arrays_Interview.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/03_Strings/03_mcqs.md | **MERGE** | 16-Strings-Advanced/concepts/03_mcqs.md | Merged educational notes/problem analysis into 16-Strings-Advanced |
| DSA_server-main/DSA-MasterCourse/03_Strings/03_notes.md | **MERGE** | 16-Strings-Advanced/concepts/03_notes.md | Merged educational notes/problem analysis into 16-Strings-Advanced |
| DSA_server-main/DSA-MasterCourse/03_Strings/code/basics.cpp | **MOVE** | code/mastercourse/basics.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/03_Strings/code/pattern_matching.cpp | **MOVE** | code/mastercourse/pattern_matching.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/03_Strings/code/string_manipulation.cpp | **MOVE** | code/mastercourse/string_manipulation.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/04_mcqs.md | **MERGE** | 07-Recursion-and-Backtracking/concepts/04_mcqs.md | Merged educational notes/problem analysis into 07-Recursion-and-Backtracking |
| DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/04_notes.md | **MERGE** | 07-Recursion-and-Backtracking/concepts/04_notes.md | Merged educational notes/problem analysis into 07-Recursion-and-Backtracking |
| DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/code/backtracking.cpp | **MOVE** | code/mastercourse/backtracking.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/code/basics.cpp | **MOVE** | code/mastercourse/basics.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/05_mcqs.md | **MERGE** | 04-Searching-and-Sorting/concepts/05_mcqs.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/05_notes.md | **MERGE** | 04-Searching-and-Sorting/concepts/05_notes.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/code/binary_search.cpp | **MOVE** | code/mastercourse/binary_search.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/code/sorting.cpp | **MOVE** | code/mastercourse/sorting.cpp | Migrated master course demonstration code |
| DSA_server-main/DSA-MasterCourse/06_Linked_List/06_notes.md | **MERGE** | 08-Linked-List/concepts/06_notes.md | Merged educational notes/problem analysis into 08-Linked-List |
| DSA_server-main/DSA-MasterCourse/07_Stack/07_notes.md | **MERGE** | 09-Stack-and-Queue/concepts/07_notes.md | Merged educational notes/problem analysis into 09-Stack-and-Queue |
| DSA_server-main/DSA-MasterCourse/08_Queue_and_Deque/08_notes.md | **MERGE** | 09-Stack-and-Queue/concepts/08_notes.md | Merged educational notes/problem analysis into 09-Stack-and-Queue |
| DSA_server-main/DSA-MasterCourse/09_Hashing/09_notes.md | **MERGE** | 06-Hashing/concepts/09_notes.md | Merged educational notes/problem analysis into 06-Hashing |
| DSA_server-main/DSA-MasterCourse/10_Trees/10_notes.md | **MERGE** | 10-Trees/concepts/10_notes.md | Merged educational notes/problem analysis into 10-Trees |
| DSA_server-main/DSA-MasterCourse/11_Binary_Search_Tree/11_notes.md | **MERGE** | 04-Searching-and-Sorting/concepts/11_notes.md | Merged educational notes/problem analysis into 04-Searching-and-Sorting |
| DSA_server-main/DSA-MasterCourse/12_Heaps_and_Priority_Queue/12_notes.md | **MERGE** | 09-Stack-and-Queue/concepts/12_notes.md | Merged educational notes/problem analysis into 09-Stack-and-Queue |
| DSA_server-main/DSA-MasterCourse/13_Tries/13_notes.md | **MERGE** | 17-Advanced-Data-Structures/concepts/13_notes.md | Merged educational notes/problem analysis into 17-Advanced-Data-Structures |
| DSA_server-main/DSA-MasterCourse/14_Graphs/14_notes.md | **MERGE** | 13-Graphs/concepts/14_notes.md | Merged educational notes/problem analysis into 13-Graphs |
| DSA_server-main/DSA-MasterCourse/15_Dynamic_Programming/15_notes.md | **MERGE** | 14-Dynamic-Programming/concepts/15_notes.md | Merged educational notes/problem analysis into 14-Dynamic-Programming |
| DSA_server-main/DSA-MasterCourse/16_Greedy_Algorithms/16_notes.md | **MERGE** | 12-Greedy-and-Intervals/concepts/16_notes.md | Merged educational notes/problem analysis into 12-Greedy-and-Intervals |
| DSA_server-main/DSA-MasterCourse/17_Divide_and_Conquer/17_notes.md | **MERGE** | 03-Arrays-and-Strings/concepts/17_notes.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| DSA_server-main/DSA-MasterCourse/18_Bit_Manipulation/18_notes.md | **MERGE** | 15-Bit-Manipulation/concepts/18_notes.md | Merged educational notes/problem analysis into 15-Bit-Manipulation |
| DSA_server-main/DSA-MasterCourse/19_Segment_Tree_and_BIT/19_notes.md | **MERGE** | 10-Trees/concepts/19_notes.md | Merged educational notes/problem analysis into 10-Trees |
| DSA_server-main/DSA-MasterCourse/20_Advanced_Graphs/20_notes.md | **MERGE** | 13-Graphs/concepts/20_notes.md | Merged educational notes/problem analysis into 13-Graphs |
| DSA_server-main/DSA-MasterCourse/21_Advanced_DP/21_notes.md | **MERGE** | 14-Dynamic-Programming/concepts/21_notes.md | Merged educational notes/problem analysis into 14-Dynamic-Programming |
| DSA_server-main/DSA-MasterCourse/22_Competitive_Programming_Extras/22_notes.md | **MERGE** | 18-Advanced-Algorithms/concepts/22_notes.md | Merged educational notes/problem analysis into 18-Advanced-Algorithms |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Adobe.md | **MERGE** | 19-Interview-Preparation/concepts/Adobe.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Amazon.md | **MERGE** | 19-Interview-Preparation/concepts/Amazon.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Flipkart.md | **MERGE** | 19-Interview-Preparation/concepts/Flipkart.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Google.md | **MERGE** | 19-Interview-Preparation/concepts/Google.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Meta.md | **MERGE** | 19-Interview-Preparation/concepts/Meta.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/Microsoft.md | **MERGE** | 19-Interview-Preparation/concepts/Microsoft.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| DSA_server-main/DSA-MasterCourse/23_Interview_Questions_by_Company/TCS_Infosys_Wipro.md | **MERGE** | 19-Interview-Preparation/concepts/TCS_Infosys_Wipro.md | Merged educational notes/problem analysis into 19-Interview-Preparation |
| Summer_pep_DSA-main/00-Start-Here-Basics.md | **MERGE** | 00-Start-Here/concepts/00-Start-Here-Basics.md | Merged educational notes/problem analysis into 00-Start-Here |
| Summer_pep_DSA-main/01-Git-And-GitHub.md | **MERGE** | 03-Arrays-and-Strings/concepts/01-Git-And-GitHub.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/02-Arrays-Basics.md | **MERGE** | 03-Arrays-and-Strings/concepts/02-Arrays-Basics.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/03-Two-Pointers.md | **MERGE** | 00-Start-Here/concepts/03-Two-Pointers.md | Merged educational notes/problem analysis into 00-Start-Here |
| Summer_pep_DSA-main/04-Binary-Search.md | **MERGE** | 03-Arrays-and-Strings/concepts/04-Binary-Search.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/05-Strings.md | **MERGE** | 16-Strings-Advanced/concepts/05-Strings.md | Merged educational notes/problem analysis into 16-Strings-Advanced |
| Summer_pep_DSA-main/06-Recursion.md | **MERGE** | 07-Recursion-and-Backtracking/concepts/06-Recursion.md | Merged educational notes/problem analysis into 07-Recursion-and-Backtracking |
| Summer_pep_DSA-main/07-Hashing.md | **MERGE** | 06-Hashing/concepts/07-Hashing.md | Merged educational notes/problem analysis into 06-Hashing |
| Summer_pep_DSA-main/08-Prefix-Sum.md | **MERGE** | 03-Arrays-and-Strings/concepts/08-Prefix-Sum.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/09-Sliding-Window.md | **MERGE** | 05-Two-Pointers-and-Sliding-Window/concepts/09-Sliding-Window.md | Merged educational notes/problem analysis into 05-Two-Pointers-and-Sliding-Window |
| Summer_pep_DSA-main/10-Linked-List.md | **MERGE** | 08-Linked-List/concepts/10-Linked-List.md | Merged educational notes/problem analysis into 08-Linked-List |
| Summer_pep_DSA-main/11-Stack.md | **MERGE** | 09-Stack-and-Queue/concepts/11-Stack.md | Merged educational notes/problem analysis into 09-Stack-and-Queue |
| Summer_pep_DSA-main/12-Queue.md | **MERGE** | 09-Stack-and-Queue/concepts/12-Queue.md | Merged educational notes/problem analysis into 09-Stack-and-Queue |
| Summer_pep_DSA-main/README.md | **MERGE** | 03-Arrays-and-Strings/concepts/README.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/Daily problems/Practice-Problems.md | **MERGE** | 03-Arrays-and-Strings/concepts/Practice-Problems.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/Language-Basics/Cpp-Basics.md | **MERGE** | 00-Start-Here/concepts/Cpp-Basics.md | Merged educational notes/problem analysis into 00-Start-Here |
| Summer_pep_DSA-main/Language-Basics/Java-Basics.md | **MERGE** | 03-Arrays-and-Strings/concepts/Java-Basics.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/Language-Basics/Python-Basics.md | **MERGE** | 03-Arrays-and-Strings/concepts/Python-Basics.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
| Summer_pep_DSA-main/Language-Basics/README.md | **MERGE** | 03-Arrays-and-Strings/concepts/README.md | Merged educational notes/problem analysis into 03-Arrays-and-Strings |
