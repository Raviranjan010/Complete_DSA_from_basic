# DSA Curriculum Gap Analysis (`GAP_ANALYSIS.md`)

**Analysis Date**: 2026-10-05  
**Objective**: Benchmark existing repository coverage against Section 6 DSA Coverage Requirements (Levels L0–L6, all major patterns, data structures, and algorithms).

---

## 1. Topic Coverage Matrix

Legend: **COMPLETE** (rich notes, problems, all levels) | **PARTIAL** (some notes/problems, missing languages or tiers) | **MISSING** (scant or absent).

| Topic | Theory / Notes | Patterns | Level Range | C++ Code | Python Code | Java Code | Visuals / Dry Run | Status | Action Needed |
|---|---|---|---|---|---|---|---|---|---|
| 00-Getting-Started & Setup | COMPLETE | N/A | L0–L1 | COMPLETE | PARTIAL | PARTIAL | COMPLETE | **PARTIAL** | Unify C++, Python, Java setup guides |
| 01-Complexity-Analysis | COMPLETE | COMPLETE | L0–L3 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Master Theorem, amortized analysis |
| 02-Math-for-DSA | PARTIAL | PARTIAL | L1–L3 | PARTIAL | MISSING | MISSING | PARTIAL | **MISSING** | Add Sieve, Fast Power, Modular Arithmetic, GCD |
| 03-Arrays | COMPLETE | COMPLETE | L1–L5 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Python/Java solutions, dry-run tables |
| 04-Strings | COMPLETE | PARTIAL | L1–L4 | COMPLETE | MISSING | MISSING | PARTIAL | **PARTIAL** | Add string reversal, anagrams, palindrome Tier A |
| 05-Searching (Binary Search) | COMPLETE | COMPLETE | L1–L5 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Python/Java solutions, 2D BS |
| 06-Sorting | PARTIAL | PARTIAL | L1–L3 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add Merge Sort, Quick Sort, Count Sort walkthroughs |
| 07-Two-Pointers | COMPLETE | COMPLETE | L2–L5 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Python/Java solutions |
| 08-Sliding-Window | COMPLETE | COMPLETE | L2–L5 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Python/Java solutions |
| 09-Prefix-Sum-and-Diff-Array | COMPLETE | COMPLETE | L2–L5 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Difference Array notes and Tier A problems |
| 10-Hashing | COMPLETE | PARTIAL | L1–L4 | COMPLETE | MISSING | MISSING | PARTIAL | **PARTIAL** | Add collision resolution theory, custom hash |
| 11-Linked-List | PARTIAL | PARTIAL | L1–L4 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Expand Tier A flagship problems (reversal, cycle, LRU) |
| 12-Stack | PARTIAL | PARTIAL | L1–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add Monotonic Stack pattern guide + Tier A problems |
| 13-Queue-and-Deque | PARTIAL | PARTIAL | L1–L4 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add circular queue, sliding window max deque |
| 14-Recursion | COMPLETE | COMPLETE | L1–L4 | COMPLETE | MISSING | MISSING | COMPLETE | **PARTIAL** | Add Python/Java solutions, call stack trees |
| 15-Backtracking | PARTIAL | PARTIAL | L3–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add N-Queens, Sudoku, Subsets state trees |
| 16-Bit-Manipulation | PARTIAL | PARTIAL | L1–L4 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add bitmask basics, subset generation |
| 17-Binary-Trees | PARTIAL | PARTIAL | L2–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add traversals, height, diameter, views, LCA |
| 18-BST | PARTIAL | PARTIAL | L2–L4 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add validate BST, search/insert/delete, LCA in BST |
| 19-Heap-and-Priority-Queue | PARTIAL | PARTIAL | L2–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add Top-K, K-way merge, median from data stream |
| 20-Greedy | PARTIAL | PARTIAL | L2–L4 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add Activity selection, fractional knapsack, jump game |
| 21-Intervals | MISSING | MISSING | L2–L4 | MISSING | MISSING | MISSING | MISSING | **MISSING** | Create dedicated Intervals hub (Merge, Insert, Non-overlapping) |
| 22-Graphs | PARTIAL | PARTIAL | L2–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add BFS, DFS, cycle check, Dijkstra, Bipartite |
| 23-Dynamic-Programming | PARTIAL | PARTIAL | L2–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | 1D, 2D Grid, 0/1 Knapsack, LCS, LIS tabulations |
| 24-Trie | PARTIAL | PARTIAL | L3–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add Trie node structure, prefix search, word search |
| 25-DSU | MISSING | MISSING | L3–L5 | MISSING | MISSING | MISSING | MISSING | **MISSING** | Create dedicated DSU hub with path compression + rank |
| 26-Segment-Tree | MISSING | MISSING | L4–L6 | MISSING | MISSING | MISSING | MISSING | **MISSING** | Add Range sum query, point update, lazy propagation |
| 27-Fenwick-Tree | MISSING | MISSING | L4–L6 | MISSING | MISSING | MISSING | MISSING | **MISSING** | Add BIT operations, point update / range query |
| 28-Advanced-Algorithms | MISSING | MISSING | L5–L6 | MISSING | MISSING | MISSING | MISSING | **MISSING** | KMP, Tarjan's SCC, Bridges, Euler Tour, LCA |
| 29-Competitive-Programming | PARTIAL | PARTIAL | L3–L6 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Add Fast I/O, modular templates, stress testing harness |
| 30-Interview-Preparation | PARTIAL | PARTIAL | L1–L5 | PARTIAL | MISSING | MISSING | PARTIAL | **PARTIAL** | Consolidate 4/8/12-week study plans, mock checklist |
| 31-Company-Wise | PARTIAL | N/A | L2–L5 | PARTIAL | MISSING | MISSING | N/A | **PARTIAL** | Clean up 7 company sheets with strict legacy sourcing |
| 32-Patterns | PARTIAL | COMPLETE | L1–L5 | PARTIAL | MISSING | MISSING | COMPLETE | **PARTIAL** | Build pattern-first index linking to canonical files |
| 33-Cheat-Sheets | MISSING | N/A | L0–L5 | MISSING | MISSING | MISSING | N/A | **MISSING** | Replace 7 stubs with dense, high-yield cheat sheets |

---

## 2. Missing Core Algorithmic Patterns

1. **Monotonic Stack / Queue**: Next Greater Element, Largest Rectangle in Histogram, Daily Temperatures.
2. **Fast & Slow Pointers (Floyd's Tortoise and Hare)**: Linked List cycle detection and start node.
3. **Topological Sort**: Kahn's BFS algorithm and DFS topological sort with cycle detection.
4. **0-1 BFS & Dijkstra**: Shortest path on unweighted vs unit/non-negative weighted graphs.
5. **0/1 Knapsack & Unbounded Knapsack Family**: Subset sum, partition equal subset, coin change.
6. **Longest Common Subsequence (LCS) Family**: Edit distance, shortest common supersequence.
7. **Longest Increasing Subsequence (LIS)**: DP $O(n^2)$ and Binary Search patience sorting $O(n \log n)$.
8. **Interval Scheduling & Merging**: Merge intervals, meeting rooms, insert interval.
9. **Binary Lifting / LCA**: Lowest common ancestor on trees.

---

## 3. Prioritized Reconstruction Roadmap (Learner Impact)

| Priority | Phase / Batch | Scope | Impact |
|---|---|---|---|
| **P0** | Foundation & Clean Architecture | Remove junk/binaries, restructure into 3-level tree, fix 423 broken links | Unblocks repository navigation and build integrity |
| **P1** | Core Linear Data Structures | Arrays, Vectors, Strings, Searching, Sorting, Two Pointers, Sliding Window, Prefix Sum | Covers 60%+ of beginner & medium interview topics |
| **P2** | Pointer & Node Structures | Linked Lists, Stacks, Queues, Monotonic Structures, Recursion, Backtracking | Critical transition from linear logic to state exploration |
| **P3** | Hierarchical & Associative Structures | Binary Trees, BST, Heaps/PQ, Hashing, Bit Manipulation | Core medium interview topics |
| **P4** | Graphs & Dynamic Programming | BFS/DFS, Shortest Path, MST, 1D/2D DP, Knapsack, LCS, LIS, Intervals | The highest interview failure points |
| **P5** | Advanced Data Structures & CP | Trie, DSU, Segment Tree, Fenwick, Advanced Strings (KMP) | Senior engineering & competitive programming depth |
| **P6** | Synthesizers & Prep Portals | Patterns Index, Cheat Sheets, Verified Company Banks, Interview Roadmap | Final retention, quick revision, interview readiness |