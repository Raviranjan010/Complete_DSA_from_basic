# Problem Coverage Sources (`_meta/COVERAGE_SOURCES.md`)

Access Date: 2026-10-06  
Recorded by: Google Antigravity  
Rule: Strict compliance with Section 4.1: If a list cannot be opened from a verified source, write 'list unavailable' and ask user to paste. Never recreate from memory.

| List ID | List Name | Source URL | Access Status | Verified Count |
|---|---|---|---|---|
| L1 | Blind 75 | https://github.com/mdabarik/blind-75-leetcode-questions | **list unavailable** (Raw fetch truncated; please paste list) | Pending |
| L2 | NeetCode 150 | https://github.com/echobash/neetcode-150-with-leetcode-question-numbers | **list unavailable** (Raw fetch truncated; please paste list) | Pending |
| L3 | LeetCode Top Interview 150 | https://github.com/JedLee6/Top150-LeetCode-Quick-Review-Notes | **list unavailable** (Raw fetch truncated; please paste list) | Pending |
| L4 | Striver SDE Sheet | https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/ | **list unavailable** (Connection aborted; please paste list) | Pending |
| L5 | CSES Problem Set | https://cses.fi/problemset/ | **VERIFIED (Opened live)** | 47 core tasks |
| L6 | Classic Textbook Problems | CLRS / Standard Algorithms Curricula | **agent-curated, no external source** (Not verified) | 35 canonical algorithms |
| L7 | Existing Repository Problems | Local module problems/ suites | **VERIFIED** | 23 problems |

---

## 📖 L6 Classic Textbook Problems (Pedagogical Rationale)

The following 35 canonical problems are agent-curated to ensure essential standard curriculum coverage:

1. **Bubble Sort, Selection Sort & Insertion Sort** (`04-Searching-and-Sorting`): Fundamental O(N^2) comparison sorts demonstrating in-place swapping and loop invariant maintenance.
2. **Merge Sort & Inversion Count** (`04-Searching-and-Sorting`): Canonical divide-and-conquer algorithm with stable O(N log N) runtime and classical array inversion counting.
3. **Quick Sort & Quickselect** (`04-Searching-and-Sorting`): Core partitioning algorithm illustrating Lomuto/Hoare pivots and expected O(N) order statistics selection.
4. **Heap Sort** (`04-Searching-and-Sorting`): In-place O(N log N) sorting leveraging binary heap property and sift-down operations without extra memory.
5. **Counting Sort & Radix Sort** (`04-Searching-and-Sorting`): Foundational non-comparison linear-time sorting algorithms for bounded integer keys.
6. **Singly Linked List Insertion & Deletion** (`08-Linked-List`): Elementary pointer manipulation covering head/tail insertions, node removal, and sentinel nodes.
7. **Reverse Linked List (Iterative & Recursive)** (`08-Linked-List`): Foundational pointer reversal problem testing three-pointer iterative mechanics and call-stack recursion.
8. **Linked List Cycle Detection (Floyd Cycle)** (`08-Linked-List`): Definitive two-pointer slow/fast cycle detection algorithm with mathematical proof of meeting point.
9. **Merge Two Sorted Linked Lists** (`08-Linked-List`): Standard linear-time list splicing technique forming the base subroutine of linked list merge sort.
10. **Stack Implementation via Array & Linked List** (`09-Stack-and-Queue`): Canonical LIFO data structure implementation exploring dynamic array growth and memory trade-offs.
11. **Queue Implementation via Circular Array** (`09-Stack-and-Queue`): Standard FIFO data structure utilizing modulo arithmetic to prevent linear array drift.
12. **Min Stack Design O(1)** (`09-Stack-and-Queue`): Classical auxiliary stack / paired value pattern enabling constant-time minimum element queries.
13. **Binary Tree Traversals (Inorder, Preorder, Postorder)** (`10-Trees`): Fundamental recursive and iterative tree traversal techniques establishing baseline tree traversal orderings.
14. **Level Order Traversal (BFS)** (`10-Trees`): Foundational queue-based breadth-first tree traversal computing per-level node groupings.
15. **Lowest Common Ancestor in Binary Tree** (`10-Trees`): Classic divide-and-conquer tree problem identifying the deepest shared ancestor node.
16. **Binary Search Tree Search, Insert & Delete** (`10-Trees`): Core BST invariant operations including predecessor/successor replacement upon two-child deletion.
17. **Min Heap & Max Heapify Operations** (`11-Heap-and-Priority-Queue`): Binary tree array representation implementing sift-up, sift-down, and O(N) bottom-up heap construction.
18. **Top K Frequent Elements** (`11-Heap-and-Priority-Queue`): Classical heap / bucket select pattern demonstrating O(N log K) priority queue maintenance.
19. **Activity Selection / Interval Scheduling** (`12-Greedy-and-Intervals`): Definitive greedy algorithm proving optimal choice by earliest finish time ordering.
20. **Fractional Knapsack Problem** (`12-Greedy-and-Intervals`): Benchmark continuous greedy problem using value-to-weight density sorting.
21. **Graph Representation (Adjacency Matrix & List)** (`13-Graphs`): Core vertex-edge data structure modeling with memory and traversal efficiency trade-offs.
22. **Breadth First Search (BFS) in Graph** (`13-Graphs`): Standard unweighted shortest path and level-order traversal algorithm using queue and visited array.
23. **Depth First Search (DFS) in Graph** (`13-Graphs`): Foundational recursive graph exploration pattern used for connectivity, cycle detection, and component labeling.
24. **Dijkstra Shortest Path Algorithm** (`13-Graphs`): Canonical non-negative edge single-source shortest path algorithm using min-priority queue relaxation.
25. **Bellman-Ford Shortest Path Algorithm** (`13-Graphs`): Dynamic programming shortest path algorithm supporting negative weights and detecting negative cycles.
26. **Floyd-Warshall All-Pairs Shortest Path** (`13-Graphs`): Classic triple-nested O(V^3) all-pairs shortest path matrix DP algorithm.
27. **Topological Sort (Kahn Algorithm & DFS)** (`13-Graphs`): Essential directed acyclic graph (DAG) linear ordering using in-degree queue or post-order DFS stack.
28. **Disjoint Set Union (DSU with Union by Rank & Path Compression)** (`17-Advanced-Data-Structures`): Essential near-O(1) amortized partition structure for dynamic graph connectivity.
29. **Kruskal Minimum Spanning Tree** (`13-Graphs`): Greedy edge-centric minimum spanning tree algorithm combining edge sorting with DSU cycle checks.
30. **Prim Minimum Spanning Tree** (`13-Graphs`): Greedy vertex-centric minimum spanning tree algorithm growing the tree using priority queue cut edges.
31. **0/1 Knapsack Problem (Tabulation & Space Optimization)** (`14-Dynamic-Programming`): Foundational dynamic programming subset problem teaching weight-capacity state transition and 1D rolling array.
32. **Longest Common Subsequence (LCS)** (`14-Dynamic-Programming`): Standard two-string 2D dynamic programming formulation for string alignment and edit distance.
33. **Longest Increasing Subsequence (LIS O(N log N))** (`14-Dynamic-Programming`): Benchmark sequence optimization combining dynamic programming with patience sorting / binary search.
34. **Matrix Chain Multiplication (Interval DP)** (`14-Dynamic-Programming`): Classic interval dynamic programming problem illustrating optimal parenthesization over subranges [i, j].
35. **Bit Manipulation: Check, Set, Clear, Toggle, Lowest Set Bit** (`15-Bit-Manipulation`): Fundamental bitwise mask operations and Brian Kernighan bit-twiddling primitives.
