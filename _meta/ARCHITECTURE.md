# DSA Repository Architecture Design (`ARCHITECTURE.md`)

**Date**: 2026-10-05  
**Architect**: Google Antigravity  
**Target Milestone**: Phase 3 Deliverable (Pre-requisite for Gate G1 Approval)

---

## 1. Executive Summary & Architectural Goals

The reconstructed repository transforms an unstructured aggregation of 5 legacy sub-repositories into a **pedagogically sequenced, zero-placeholder, 3-level hierarchical textbook + interview prep engine**.

### Primary Success Metric
> *"How effectively can this repository teach a complete beginner to solve unseen DSA problems independently?"*

### Core Architectural Principles
1. **Strict 3-Level Nesting**: Repo Root $\to$ Topic Folder (`NN-Topic-Name`) $\to$ Subtopic / Problem File. No 4th level directories.
2. **Pedagogical Ordering**: Topic numbers strictly respect conceptual prerequisites (e.g., Recursion before Trees and DP; Sorting before Binary Search on Answer; Heaps before Dijkstra).
3. **Canonical Single Source of Truth**: Every algorithm and problem has exactly ONE home file registered in `PROBLEM_REGISTRY.csv`. Other sections cross-reference with markdown links.
4. **Three-Tier Problem Classification**:
   - **Tier A (Flagship)**: Complete pedagogical walkthroughs, all 3 languages (C++, Python, Java), dry-run tables, visual traces, verified test suites. (Estimated: 60–80 flagship problems).
   - **Tier B (Practice)**: Compact, high-yield templates with problem statement, intuition, complexity, and verified solutions in C++, Python, and Java. (Estimated: 120–150 practice problems).
   - **Tier C (Index)**: Curated practice index tables in topic READMEs linking to verified external canonical platforms (LeetCode, GFG, Codeforces). (Estimated: 250+ indexed problems).
5. **Multi-Language Parity**: All Tier A and Tier B problems feature tested, idiomatic implementations in **C++17**, **Python 3**, and **Java 24**.

---

## 2. Target Directory Hierarchy (Max 3 Levels)

```text
d:\Temp\Complete_DSA_from_basic/
├── README.md                                  # Global navigation hub, roadmap & tracker
├── .gitignore                                 # Clean gitignore (ignores build/, *.exe, *.o)
├── _meta/                                     # Permanent state & maintenance registry
│   ├── PROGRESS.md
│   ├── AUDIT_REPORT.md
│   ├── GAP_ANALYSIS.md
│   ├── ARCHITECTURE.md
│   ├── TOPIC_DEPENDENCY.md
│   ├── MIGRATION_MAP.md
│   ├── PROBLEM_REGISTRY.csv
│   ├── DECISIONS.md
│   ├── KNOWN_GAPS.md
│   ├── LINK_REPORT.md
│   ├── TEST_REPORT.md
│   ├── COMPANY_SOURCES.md
│   └── STYLE_GUIDE.md
├── tools/                                     # Automation, test harness & validation scripts
│   ├── run_all_tests.py                       # Automated compile & test runner
│   ├── validate_links.py                      # Internal & external link validator
│   ├── validate_registry.py                   # Filesystem <-> CSV consistency checker
│   └── sync_code_blocks.py                    # Ensures markdown matches verified code
│
├── 00-Getting-Started/                        # Setup, memory model, pointers, language basics
├── 01-Complexity-Analysis/                    # Big-O, amortized time, recurrence relations
├── 02-Math-for-DSA/                           # Modular arithmetic, GCD/LCM, fast power, primes
├── 03-Arrays/                                 # Static arrays, vectors, matrices, Kadane
├── 04-Strings/                                # String manipulation, anagrams, palindromes
├── 05-Searching/                              # Linear search, Binary search, BS on answer, 2D BS
├── 06-Sorting/                                # Comparison & linear sorts, stability, invariants
├── 07-Two-Pointers/                           # Opposite direction, same direction, fast/slow
├── 08-Sliding-Window/                         # Fixed size, variable size, frequency maps
├── 09-Prefix-Sum-and-Difference-Array/        # 1D/2D prefix sums, difference array updates
├── 10-Hashing/                                # Hash maps/sets, collision resolution, custom hash
├── 11-Linked-List/                            # Singly, doubly, circular, Floyd cycle, reversals
├── 12-Stack/                                  # LIFO mechanics, monotonic stacks, histogram
├── 13-Queue-and-Deque/                        # FIFO mechanics, circular queue, monotonic deque
├── 14-Recursion/                              # Call stack mechanics, recurrence trees, memoization
├── 15-Backtracking/                           # State-space exploration, pruning, N-Queens
├── 16-Bit-Manipulation/                       # Bitwise ops, binary representations, bitmasks
├── 17-Binary-Trees/                           # Traversals, views, height, diameter, LCA
├── 18-BST/                                    # BST invariants, search, insert, delete, balance
├── 19-Heap-and-Priority-Queue/                # Min/max heaps, heapify, top-K, K-way merge
├── 20-Greedy/                                 # Activity selection, fractional knapsack, proofs
├── 21-Intervals/                              # Merge intervals, insert interval, meeting rooms
├── 22-Graphs/                                 # Adjacency, BFS, DFS, Dijkstra, Bellman-Ford, MST
├── 23-Dynamic-Programming/                    # 1D, 2D Grid, Knapsack, LCS, LIS, Interval DP
├── 24-Trie/                                   # Prefix trees, autocomplete, bitwise XOR trie
├── 25-DSU/                                    # Disjoint set union with path compression + rank
├── 26-Segment-Tree/                           # Point & range queries, lazy propagation
├── 27-Fenwick-Tree/                           # Binary indexed tree (BIT) point & range queries
├── 28-Advanced-Algorithms/                    # KMP, Z-algo, Tarjan SCC, Bridges, Euler Tour
├── 29-Competitive-Programming/                # Fast I/O, contest playbook, stress testing harness
├── 30-Interview-Preparation/                  # 4/8/12-week study plans, mock interview checklist
├── 31-Company-Wise/                           # Verified interview question banks (strict sourcing)
├── 32-Patterns/                               # Pattern-first index cross-linking to problems
└── 33-Cheat-Sheets/                           # High-density quick revision cheat sheets
```

---

## 3. Topic Internal Structure (3 Levels Max)

Each topic folder `NN-Topic-Name` follows a uniform layout:
```text
NN-Topic-Name/
├── README.md                                  # Topic hub (definition, learning order, pattern list)
├── 01-concept-notes.md                        # Theory, memory diagrams, operations, library pitfalls
├── 02-pattern-recognition.md                  # "If you see X -> Think Y" pattern decision tables
├── 03-interview-guide.md                      # Conceptual Q&A, follow-ups, common traps
├── 001-flagship-problem-a.md                  # Tier A problem (full template, 3 languages, dry run)
├── 002-practice-problem-b.md                  # Tier B problem (compact template, 3 languages)
└── code/                                      # Standalone tested code files
    ├── flagship-problem-a/
    │   ├── solution.cpp                       # Verified C++17 implementation
    │   ├── solution.py                        # Verified Python 3 implementation
    │   ├── Solution.java                      # Verified Java 24 implementation
    │   └── tests.json                         # Test cases (examples + edge cases)
    └── practice-problem-b/
        ├── solution.cpp
        ├── solution.py
        ├── Solution.java
        └── tests.json
```

---

## 4. Pattern Cross-Indexing Model

The `32-Patterns/` directory serves as an inverted index:
- It **never duplicates** problem statements or code solutions.
- It contains dedicated pattern cards (e.g., `01-two-pointers.md`, `02-sliding-window.md`, `03-monotonic-stack.md`, `04-binary-search-on-answer.md`, `05-knapsack-family.md`).
- Each card documents:
  1. The core theoretical intuition and invariant.
  2. The canonical mental trigger ("When to apply").
  3. The reusable algorithmic template.
  4. Clickable links to every Tier A and Tier B problem in the repository that uses this pattern.
  5. Variant matrix explaining what changes between problems.

---

## 5. Migration Execution Strategy & Phasing Plan

Migration will proceed topic-by-topic in strict topological order:
1. **Batch 0**: Clean repository hygiene — remove 14 `.exe` binaries, temporary runner files, and 0-byte stubs via `MIGRATION_MAP.md`. Initialize `tools/` automation.
2. **Batch 1 (Foundations)**: Topics 00, 01, 02 (Language basics, Complexity, Math).
3. **Batch 2 (Core Linear Structures)**: Topics 03, 04, 05, 06 (Arrays, Strings, Searching, Sorting).
4. **Batch 3 (Linear Patterns)**: Topics 07, 08, 09, 10 (Two Pointers, Sliding Window, Prefix Sum, Hashing).
5. **Batch 4 (Node & Stack Structures)**: Topics 11, 12, 13, 14, 15, 16 (Linked List, Stack, Queue, Recursion, Backtracking, Bits).
6. **Batch 5 (Hierarchical Structures)**: Topics 17, 18, 19, 20, 21 (Trees, BST, Heaps, Greedy, Intervals).
7. **Batch 6 (Graphs & DP)**: Topics 22, 23 (Graphs, Dynamic Programming).
8. **Batch 7 (Advanced Structures & Extensions)**: Topics 24, 25, 26, 27, 28, 29 (Trie, DSU, Segment Tree, Fenwick, Advanced, CP).
9. **Batch 8 (Portals & Synthesis)**: Topics 30, 31, 32, 33 and Root `README.md` (Interview prep, Company bank, Patterns index, Cheat sheets).
