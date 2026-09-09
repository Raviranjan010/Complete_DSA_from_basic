# DSA-Zero-To-Hero: Master Data Structures & Algorithms with C++

Welcome to **DSA-Zero-To-Hero**, a comprehensive, zero-gap, beginner-to-advanced curriculum for mastering Data Structures & Algorithms using **C++17**.

This repository is designed from first principles to take a reader with **zero prior programming experience** all the way to **top-tier technical interview readiness** and competitive programming competence.

---

## 🎯 Target Audience & Personas

This repository is structured to serve three distinct learner profiles simultaneously:

- **Persona A — True Beginner**: Has never written a line of code. Needs Phase 0 spelling out syntax, memory models, compilation, and basic logic step-by-step with analogies and zero skipped assumptions.
- **Persona B — Computer Science Student**: Wants clear time/space complexity derivations, pattern recognition across problems, rigorous dry runs, and a high volume of practice problems.
- **Persona C — Interview Candidate (SDE Roles)**: Focuses on pattern categorization, optimal trade-off discussions, mock interview communication strategies, company-curated question sets, and high-frequency pattern cheat sheets.

---

## 📖 How to Use This Repository

1. **For First-Time Learners (Linear Path)**:
   - Start at [Phase 0 — Prerequisites](./00-prerequisites/README.md) and move sequentially down the Table of Contents.
   - Every topic strictly builds *only* on what was previously introduced—no forward jumps or unlinked assumptions.
   - For every sub-topic:
     1. Read the **Concept File** (`NN-subtopic-name.md`). Trace the dry runs by hand and study the C++ code explanations.
     2. Open the **Practice File** (`NN-subtopic-name-practice.md`) and solve the target problem set. Study the fully worked walkthrough solutions.
     3. Check off your progress in [`PROGRESS-TRACKER.md`](./PROGRESS-TRACKER.md).
     4. Complete the `phase-summary-and-quiz.md` at the end of each phase before proceeding.

2. **For Revision & Interview Candidates (Pattern-Driven Path)**:
   - Use [`PATTERNS.md`](./PATTERNS.md) to locate specific algorithmic patterns (e.g., `#two-pointers`, `#monotonic-stack`, `#dp-knapsack`).
   - Consult the [`CHEATSHEETS/`](./CHEATSHEETS/) directory for quick last-minute formula & algorithm summaries.
   - Check technical definitions in [`GLOSSARY.md`](./GLOSSARY.md).

---

## 🏷️ Legend & Tagging Standards

### Difficulty Levels
- 🟢 **Easy**: Fundamental problem testing direct application of a concept or syntax.
- 🟡 **Medium**: Standard interview question involving multi-step logic, pattern combinations, or edge cases.
- 🔴 **Hard**: Advanced problem requiring subtle insights, multiple data structure compositions, or optimal space/time tricks.

### Pattern Tags
Questions across practice sets are tagged with standard pattern identifiers (e.g., `#two-pointers`, `#sliding-window`, `#fast-slow-pointers`, `#monotonic-stack`). All pattern tags are centrally indexed in [`PATTERNS.md`](./PATTERNS.md).

---

## 📚 Core Navigation & Resources

- **[Glossary of Technical Terms (`GLOSSARY.md`)](./GLOSSARY.md)**
- **[Pattern-to-Question Index (`PATTERNS.md`)](./PATTERNS.md)**
- **[Progress Tracker & Checklist (`PROGRESS-TRACKER.md`)](./PROGRESS-TRACKER.md)**
- **[Quick Reference Cheatsheets (`CHEATSHEETS/`)](./CHEATSHEETS/)**
  - [Complexity Analysis Cheatsheet](./CHEATSHEETS/complexity-cheatsheet.md)
  - [C++ STL Cheatsheet](./CHEATSHEETS/cpp-stl-cheatsheet.md)
  - [Recursion & Backtracking Cheatsheet](./CHEATSHEETS/recursion-cheatsheet.md)
  - [Sorting Algorithms Cheatsheet](./CHEATSHEETS/sorting-cheatsheet.md)
  - [Graph Algorithms Cheatsheet](./CHEATSHEETS/graph-algorithms-cheatsheet.md)
  - [Dynamic Programming Patterns Cheatsheet](./CHEATSHEETS/dp-patterns-cheatsheet.md)
  - [Interview Last-Minute Revision](./CHEATSHEETS/interview-last-minute-revision.md)

---

## 🗺️ Master Table of Contents

### [Phase 0 — Prerequisites (for true beginners)](./00-prerequisites/README.md)
- [0.1 What is a program, compiler vs interpreter, what happens when C++ code runs](./00-prerequisites/01-what-is-a-program.md) | [Practice](./00-prerequisites/01-what-is-a-program-practice.md)
- [0.2 Setting up: installing a C++ compiler / using an online judge, writing & running "Hello World"](./00-prerequisites/02-setting-up-and-hello-world.md) | [Practice](./00-prerequisites/02-setting-up-and-hello-world-practice.md)
- [0.3 Variables, data types, type sizes, int, long long, float, double, char, bool, string](./00-prerequisites/03-variables-and-data-types.md) | [Practice](./00-prerequisites/03-variables-and-data-types-practice.md)
- [0.4 Input/output: cin, cout, fast I/O for competitive programming](./00-prerequisites/04-input-output-fast-io.md) | [Practice](./00-prerequisites/04-input-output-fast-io-practice.md)
- [0.5 Operators: arithmetic, relational, logical, bitwise preview, ternary](./00-prerequisites/05-operators.md) | [Practice](./00-prerequisites/05-operators-practice.md)
- [0.6 Conditionals: if/else, switch](./00-prerequisites/06-conditionals.md) | [Practice](./00-prerequisites/06-conditionals-practice.md)
- [0.7 Loops: for, while, do-while, break/continue, nested loops](./00-prerequisites/07-loops.md) | [Practice](./00-prerequisites/07-loops-practice.md)
- [0.8 Functions: declaration, definition, parameters, return values, pass-by-value vs pass-by-reference](./00-prerequisites/08-functions.md) | [Practice](./00-prerequisites/08-functions-practice.md)
- [0.9 Arrays basics: declaration, indexing, iterating, fixed size vs dynamic](./00-prerequisites/09-arrays-basics.md) | [Practice](./00-prerequisites/09-arrays-basics-practice.md)
- [0.10 Pointers & references from scratch (memory model, address-of &, dereference *)](./00-prerequisites/10-pointers-and-references.md) | [Practice](./00-prerequisites/10-pointers-and-references-practice.md)
- [0.11 Structures (struct) and basic classes/objects](./00-prerequisites/11-structures-and-classes.md) | [Practice](./00-prerequisites/11-structures-and-classes-practice.md)
- [0.12 Introduction to the C++ Standard Template Library (STL)](./00-prerequisites/12-cpp-stl-intro.md) | [Practice](./00-prerequisites/12-cpp-stl-intro-practice.md)
- [0.13 Basic math for DSA: modulo, integer overflow, GCD/LCM by hand, primes basics](./00-prerequisites/13-basic-math-for-dsa.md) | [Practice](./00-prerequisites/13-basic-math-for-dsa-practice.md)

### [Phase 1 — Complexity Analysis](./01-complexity-analysis/README.md)
- [1.1 Why we measure efficiency: real-world motivation](./01-complexity-analysis/01-why-measure-efficiency.md) | [Practice](./01-complexity-analysis/01-why-measure-efficiency-practice.md)
- [1.2 Time complexity intuition (counting steps) before Big-O notation](./01-complexity-analysis/02-time-complexity-intuition.md) | [Practice](./01-complexity-analysis/02-time-complexity-intuition-practice.md)
- [1.3 Big-O, Big-Theta, Big-Omega — formal definitions with examples](./01-complexity-analysis/03-asymptotic-notations.md) | [Practice](./01-complexity-analysis/03-asymptotic-notations-practice.md)
- [1.4 Best, average, worst case analysis](./01-complexity-analysis/04-best-average-worst-case.md) | [Practice](./01-complexity-analysis/04-best-average-worst-case-practice.md)
- [1.5 Common complexity classes with graphs: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)](./01-complexity-analysis/05-common-complexity-classes.md) | [Practice](./01-complexity-analysis/05-common-complexity-classes-practice.md)
- [1.6 Space complexity, auxiliary space vs input space](./01-complexity-analysis/06-space-complexity.md) | [Practice](./01-complexity-analysis/06-space-complexity-practice.md)
- [1.7 Analyzing loops (single, nested, dependent loops), recursive complexity preview](./01-complexity-analysis/07-analyzing-loops.md) | [Practice](./01-complexity-analysis/07-analyzing-loops-practice.md)
- [1.8 Amortized analysis intuition](./01-complexity-analysis/08-amortized-analysis.md) | [Practice](./01-complexity-analysis/08-amortized-analysis-practice.md)

### [Phase 2 — Arrays & Strings](./02-arrays-and-strings/README.md)
- [2.1 Arrays in depth: memory layout, static vs dynamic arrays, std::vector fully explained](./02-arrays-and-strings/01-arrays-in-depth-vector.md) | [Practice](./02-arrays-and-strings/01-arrays-in-depth-vector-practice.md)
- [2.2 Multi-dimensional arrays (2D/3D), row-major order](./02-arrays-and-strings/02-multidimensional-arrays.md) | [Practice](./02-arrays-and-strings/02-multidimensional-arrays-practice.md)
- [2.3 Array traversal patterns, in-place modification](./02-arrays-and-strings/03-array-traversal-inplace.md) | [Practice](./02-arrays-and-strings/03-array-traversal-inplace-practice.md)
- [2.4 Two-pointer technique (opposite-direction and same-direction)](./02-arrays-and-strings/04-two-pointer-technique.md) | [Practice](./02-arrays-and-strings/04-two-pointer-technique-practice.md)
- [2.5 Sliding window technique (fixed size and variable size)](./02-arrays-and-strings/05-sliding-window-technique.md) | [Practice](./02-arrays-and-strings/05-sliding-window-technique-practice.md)
- [2.6 Prefix sum and difference arrays](./02-arrays-and-strings/06-prefix-sum-and-difference-arrays.md) | [Practice](./02-arrays-and-strings/06-prefix-sum-and-difference-arrays-practice.md)
- [2.7 Kadane's algorithm (maximum subarray)](./02-arrays-and-strings/07-kadanes-algorithm.md) | [Practice](./02-arrays-and-strings/07-kadanes-algorithm-practice.md)
- [2.8 Sorting algorithms from scratch: bubble, selection, insertion](./02-arrays-and-strings/08-basic-sorting-algorithms.md) | [Practice](./02-arrays-and-strings/08-basic-sorting-algorithms-practice.md)
- [2.9 Sorting algorithms (efficient): merge sort, quick sort, heap sort](./02-arrays-and-strings/09-efficient-sorting-algorithms.md) | [Practice](./02-arrays-and-strings/09-efficient-sorting-algorithms-practice.md)
- [2.10 Counting sort, radix sort, bucket sort](./02-arrays-and-strings/10-linear-time-sorting.md) | [Practice](./02-arrays-and-strings/10-linear-time-sorting-practice.md)
- [2.11 std::sort and comparator functions in C++](./02-arrays-and-strings/11-cpp-sort-and-comparators.md) | [Practice](./02-arrays-and-strings/11-cpp-sort-and-comparators-practice.md)
- [2.12 Searching: linear search, binary search (iterative + recursive), binary search on answer](./02-arrays-and-strings/12-binary-search-fundamentals.md) | [Practice](./02-arrays-and-strings/12-binary-search-fundamentals-practice.md)
- [2.13 Binary search variants: first/last occurrence, search in rotated sorted array, peak element](./02-arrays-and-strings/13-binary-search-variants.md) | [Practice](./02-arrays-and-strings/13-binary-search-variants-practice.md)
- [2.14 Strings in depth: std::string, mutability, common operations](./02-arrays-and-strings/14-strings-in-depth.md) | [Practice](./02-arrays-and-strings/14-strings-in-depth-practice.md)
- [2.15 String traversal & manipulation patterns](./02-arrays-and-strings/15-string-traversal-manipulation.md) | [Practice](./02-arrays-and-strings/15-string-traversal-manipulation-practice.md)
- [2.16 Frequency counting with arrays/hash maps on strings](./02-arrays-and-strings/16-string-frequency-counting.md) | [Practice](./02-arrays-and-strings/16-string-frequency-counting-practice.md)
- [2.17 Two-pointer & sliding window on strings](./02-arrays-and-strings/17-two-pointer-sliding-window-strings.md) | [Practice](./02-arrays-and-strings/17-two-pointer-sliding-window-strings-practice.md)
- [2.18 Basic pattern matching (naive substring search)](./02-arrays-and-strings/18-basic-pattern-matching.md) | [Practice](./02-arrays-and-strings/18-basic-pattern-matching-practice.md)
- [2.19 Cyclic rotations, Dutch national flag problem, merge intervals](./02-arrays-and-strings/19-miscellaneous-array-problems.md) | [Practice](./02-arrays-and-strings/19-miscellaneous-array-problems-practice.md)

### [Phase 3 — Recursion & Backtracking](./03-recursion-and-backtracking/README.md)
- [3.1 What is recursion: call stack visualized, base case & recursive case](./03-recursion-and-backtracking/01-recursion-basics.md) | [Practice](./03-recursion-and-backtracking/01-recursion-basics-practice.md)
- [3.2 Recursion tree diagrams, tracing recursive calls by hand](./03-recursion-and-backtracking/02-recursion-trees-tracing.md) | [Practice](./03-recursion-and-backtracking/02-recursion-trees-tracing-practice.md)
- [3.3 Classic recursion: factorial, Fibonacci](./03-recursion-and-backtracking/03-classic-recursion-problems.md) | [Practice](./03-recursion-and-backtracking/03-classic-recursion-problems-practice.md)
- [3.4 Recursion on arrays/strings (sum, reverse, check palindrome recursively)](./03-recursion-and-backtracking/04-recursion-on-arrays-and-strings.md) | [Practice](./03-recursion-and-backtracking/04-recursion-on-arrays-and-strings-practice.md)
- [3.5 Multiple recursive calls & recursion trees (subsets via include/exclude)](./03-recursion-and-backtracking/05-multiple-recursive-calls.md) | [Practice](./03-recursion-and-backtracking/05-multiple-recursive-calls-practice.md)
- [3.6 Backtracking framework: choose → explore → un-choose](./03-recursion-and-backtracking/06-backtracking-framework.md) | [Practice](./03-recursion-and-backtracking/06-backtracking-framework-practice.md)
- [3.7 Backtracking problems: subsets, permutations, combinations, combination sum](./03-recursion-and-backtracking/07-subsets-permutations-combinations.md) | [Practice](./03-recursion-and-backtracking/07-subsets-permutations-combinations-practice.md)
- [3.8 Backtracking on grids/boards: N-Queens, Sudoku solver, Rat in a Maze](./03-recursion-and-backtracking/08-grid-and-board-backtracking.md) | [Practice](./03-recursion-and-backtracking/08-grid-and-board-backtracking-practice.md)
- [3.9 Backtracking on strings: palindrome partitioning, word search](./03-recursion-and-backtracking/09-string-backtracking.md) | [Practice](./03-recursion-and-backtracking/09-string-backtracking-practice.md)
- [3.10 Recursion & backtracking complexity analysis](./03-recursion-and-backtracking/10-recursion-complexity-analysis.md) | [Practice](./03-recursion-and-backtracking/10-recursion-complexity-analysis-practice.md)

### [Phase 4 — Linked List](./04-linked-list/README.md)
- [4.1 Why linked lists: arrays' limitations, memory model of a linked list](./04-linked-list/01-linked-list-motivation-memory-model.md) | [Practice](./04-linked-list/01-linked-list-motivation-memory-model-practice.md)
- [4.2 Singly linked list: node structure, insertion, deletion, traversal](./04-linked-list/02-singly-linked-list-operations.md) | [Practice](./04-linked-list/02-singly-linked-list-operations-practice.md)
- [4.3 Searching in a linked list, reversing a linked list (iterative + recursive)](./04-linked-list/03-reversing-linked-list.md) | [Practice](./04-linked-list/03-reversing-linked-list-practice.md)
- [4.4 Doubly linked list: structure and operations](./04-linked-list/04-doubly-linked-list.md) | [Practice](./04-linked-list/04-doubly-linked-list-practice.md)
- [4.5 Circular linked list: structure and operations](./04-linked-list/05-circular-linked-list.md) | [Practice](./04-linked-list/05-circular-linked-list-practice.md)
- [4.6 Fast & slow pointer technique: cycle detection (Floyd's algorithm), middle node](./04-linked-list/06-fast-slow-pointers-floyds-algorithm.md) | [Practice](./04-linked-list/06-fast-slow-pointers-floyds-algorithm-practice.md)
- [4.7 Merging two sorted linked lists, merge sort on linked list](./04-linked-list/07-merge-sorted-lists-and-merge-sort.md) | [Practice](./04-linked-list/07-merge-sorted-lists-and-merge-sort-practice.md)
- [4.8 Removing Nth node from end, intersection of two linked lists](./04-linked-list/08-nth-node-from-end-and-intersection.md) | [Practice](./04-linked-list/08-nth-node-from-end-and-intersection-practice.md)
- [4.9 Applications: LRU cache using doubly linked list + hash map](./04-linked-list/09-lru-cache-implementation.md) | [Practice](./04-linked-list/09-lru-cache-implementation-practice.md)
- [4.10 Linked list vs array — when to use which (decision guide)](./04-linked-list/10-array-vs-linked-list-decision-guide.md) | [Practice](./04-linked-list/10-array-vs-linked-list-decision-guide-practice.md)

### [Phase 5 — Stack & Queue](./05-stack-and-queue/README.md)
- [5.1 Stack: LIFO concept, array/linked-list implementation, std::stack](./05-stack-and-queue/01-stack-fundamentals.md) | [Practice](./05-stack-and-queue/01-stack-fundamentals-practice.md)
- [5.2 Stack applications: balanced parentheses, infix/postfix/prefix conversion](./05-stack-and-queue/02-stack-applications.md) | [Practice](./05-stack-and-queue/02-stack-applications-practice.md)
- [5.3 Monotonic stack pattern: next greater element, next smaller element, stock span](./05-stack-and-queue/03-monotonic-stack-pattern.md) | [Practice](./05-stack-and-queue/03-monotonic-stack-pattern-practice.md)
- [5.4 Queue: FIFO concept, circular queue, linked-list implementation, std::queue](./05-stack-and-queue/04-queue-fundamentals.md) | [Practice](./05-stack-and-queue/04-queue-fundamentals-practice.md)
- [5.5 Deque (double-ended queue), std::deque, sliding window maximum using deque](./05-stack-and-queue/05-deque-and-sliding-window-maximum.md) | [Practice](./05-stack-and-queue/05-deque-and-sliding-window-maximum-practice.md)
- [5.6 Priority concepts preview](./05-stack-and-queue/06-priority-queue-preview.md) | [Practice](./05-stack-and-queue/06-priority-queue-preview-practice.md)
- [5.7 Implementing a queue using two stacks and vice versa](./05-stack-and-queue/07-queue-using-stacks-and-vice-versa.md) | [Practice](./05-stack-and-queue/07-queue-using-stacks-and-vice-versa-practice.md)

### [Phase 6 — Hashing](./06-hashing/README.md)
- [6.1 Why hashing: the lookup problem, hash functions intuition](./06-hashing/01-hashing-motivation-hash-functions.md) | [Practice](./06-hashing/01-hashing-motivation-hash-functions-practice.md)
- [6.2 Collision handling: chaining vs open addressing](./06-hashing/02-collision-handling-strategies.md) | [Practice](./06-hashing/02-collision-handling-strategies-practice.md)
- [6.3 std::unordered_map, std::unordered_set, std::map, std::set — differences and complexities](./06-hashing/03-cpp-stl-hash-maps-and-sets.md) | [Practice](./06-hashing/03-cpp-stl-hash-maps-and-sets-practice.md)
- [6.4 Frequency counting patterns using hash maps](./06-hashing/04-frequency-counting-patterns.md) | [Practice](./06-hashing/04-frequency-counting-patterns-practice.md)
- [6.5 Two-sum and generalized k-sum patterns using hashing](./06-hashing/05-two-sum-and-k-sum-patterns.md) | [Practice](./06-hashing/05-two-sum-and-k-sum-patterns-practice.md)
- [6.6 Subarray sum problems using prefix-sum + hashing](./06-hashing/06-prefix-sum-with-hashing.md) | [Practice](./06-hashing/06-prefix-sum-with-hashing-practice.md)
- [6.7 Grouping/categorizing data with hash maps](./06-hashing/07-grouping-and-categorizing-data.md) | [Practice](./06-hashing/07-grouping-and-categorizing-data-practice.md)
- [6.8 Custom hashing for pairs/tuples in C++](./06-hashing/08-custom-hash-functions-in-cpp.md) | [Practice](./06-hashing/08-custom-hash-functions-in-cpp-practice.md)

### [Phase 7 — Trees](./07-trees/README.md)
- [7.1 Tree terminology: root, node, edge, height, depth, leaf, subtree](./07-trees/01-tree-terminology-and-basics.md) | [Practice](./07-trees/01-tree-terminology-and-basics-practice.md)
- [7.2 Binary trees: representation in C++, types (full, complete, perfect, balanced, skewed)](./07-trees/02-binary-tree-types-and-representation.md) | [Practice](./07-trees/02-binary-tree-types-and-representation-practice.md)
- [7.3 Tree traversals: preorder, inorder, postorder (recursive + iterative)](./07-trees/03-dfs-tree-traversals.md) | [Practice](./07-trees/03-dfs-tree-traversals-practice.md)
- [7.4 Level-order traversal (BFS on trees), views (top/bottom/left/right view)](./07-trees/04-bfs-level-order-and-tree-views.md) | [Practice](./07-trees/04-bfs-level-order-and-tree-views-practice.md)
- [7.5 Height, diameter, balanced-check, symmetric-check, mirror of a tree](./07-trees/05-tree-properties-and-metrics.md) | [Practice](./07-trees/05-tree-properties-and-metrics-practice.md)
- [7.6 Binary Search Tree (BST): property, insertion, deletion, search](./07-trees/06-binary-search-tree-basics.md) | [Practice](./07-trees/06-binary-search-tree-basics-practice.md)
- [7.7 BST validation, floor/ceil, kth smallest/largest, BST iterator](./07-trees/07-bst-operations-and-problems.md) | [Practice](./07-trees/07-bst-operations-and-problems-practice.md)
- [7.8 Lowest Common Ancestor (LCA) — binary tree and BST versions](./07-trees/08-lowest-common-ancestor.md) | [Practice](./07-trees/08-lowest-common-ancestor-practice.md)
- [7.9 Balanced BSTs: AVL tree rotations and Red-Black tree overview](./07-trees/09-avl-and-red-black-trees.md) | [Practice](./07-trees/09-avl-and-red-black-trees-practice.md)
- [7.10 Trie (prefix tree): structure, insert, search, prefix search, applications](./07-trees/10-trie-prefix-tree.md) | [Practice](./07-trees/10-trie-prefix-tree-practice.md)
- [7.11 Segment Tree: build, range query, point update, range update (lazy propagation)](./07-trees/11-segment-tree-and-lazy-propagation.md) | [Practice](./07-trees/11-segment-tree-and-lazy-propagation-practice.md)
- [7.12 Fenwick Tree / Binary Indexed Tree: build, point update, prefix query](./07-trees/12-fenwick-tree-binary-indexed-tree.md) | [Practice](./07-trees/12-fenwick-tree-binary-indexed-tree-practice.md)
- [7.13 Tree DP introduction (diameter via DP, max path sum)](./07-trees/13-tree-dynamic-programming-intro.md) | [Practice](./07-trees/13-tree-dynamic-programming-intro-practice.md)

### [Phase 8 — Heaps & Priority Queue](./08-heaps-and-priority-queue/README.md)
- [8.1 Heap property (min-heap, max-heap), array representation of a heap](./08-heaps-and-priority-queue/01-heap-basics-array-representation.md) | [Practice](./08-heaps-and-priority-queue/01-heap-basics-array-representation-practice.md)
- [8.2 Heapify, build-heap, insert, extract-min/max, heap sort](./08-heaps-and-priority-queue/02-heap-operations-and-heap-sort.md) | [Practice](./08-heaps-and-priority-queue/02-heap-operations-and-heap-sort-practice.md)
- [8.3 std::priority_queue in C++, custom comparators](./08-heaps-and-priority-queue/03-cpp-priority-queue.md) | [Practice](./08-heaps-and-priority-queue/03-cpp-priority-queue-practice.md)
- [8.4 Applications: kth largest/smallest element, top-k frequent elements](./08-heaps-and-priority-queue/04-kth-element-and-top-k-patterns.md) | [Practice](./08-heaps-and-priority-queue/04-kth-element-and-top-k-patterns-practice.md)
- [8.5 K-way merge (merge k sorted lists/arrays)](./08-heaps-and-priority-queue/05-k-way-merge-pattern.md) | [Practice](./08-heaps-and-priority-queue/05-k-way-merge-pattern-practice.md)
- [8.6 Median in a data stream (two-heap technique)](./08-heaps-and-priority-queue/06-two-heap-technique-median-stream.md) | [Practice](./08-heaps-and-priority-queue/06-two-heap-technique-median-stream-practice.md)

### [Phase 9 — Graphs](./09-graphs/README.md)
- [9.1 Graph terminology: directed/undirected, weighted/unweighted, cyclic/acyclic, degree](./09-graphs/01-graph-terminology-and-types.md) | [Practice](./09-graphs/01-graph-terminology-and-types-practice.md)
- [9.2 Graph representation: adjacency matrix vs adjacency list](./09-graphs/02-graph-representation.md) | [Practice](./09-graphs/02-graph-representation-practice.md)
- [9.3 Graph traversal: BFS (with applications: shortest path in unweighted graph)](./09-graphs/03-breadth-first-search.md) | [Practice](./09-graphs/03-breadth-first-search-practice.md)
- [9.4 Graph traversal: DFS (with applications: connected components, cycle detection)](./09-graphs/04-depth-first-search.md) | [Practice](./09-graphs/04-depth-first-search-practice.md)
- [9.5 Topological sort: Kahn's algorithm (BFS) and DFS-based](./09-graphs/05-topological-sort.md) | [Practice](./09-graphs/05-topological-sort-practice.md)
- [9.6 Shortest path: Dijkstra's algorithm (with priority queue)](./09-graphs/06-dijkstras-algorithm.md) | [Practice](./09-graphs/06-dijkstras-algorithm-practice.md)
- [9.7 Shortest path: Bellman-Ford algorithm (negative weights & cycles)](./09-graphs/07-bellman-ford-algorithm.md) | [Practice](./09-graphs/07-bellman-ford-algorithm-practice.md)
- [9.8 Shortest path: Floyd-Warshall algorithm (all-pairs)](./09-graphs/08-floyd-warshall-algorithm.md) | [Practice](./09-graphs/08-floyd-warshall-algorithm-practice.md)
- [9.9 Minimum Spanning Tree: Prim's algorithm, Kruskal's algorithm](./09-graphs/09-minimum-spanning-tree.md) | [Practice](./09-graphs/09-minimum-spanning-tree-practice.md)
- [9.10 Disjoint Set Union (Union-Find): path compression & union by rank](./09-graphs/10-disjoint-set-union.md) | [Practice](./09-graphs/10-disjoint-set-union-practice.md)
- [9.11 Bipartite graph check (BFS/DFS coloring)](./09-graphs/11-bipartite-graph-check.md) | [Practice](./09-graphs/11-bipartite-graph-check-practice.md)
- [9.12 Strongly Connected Components: Kosaraju's algorithm, Tarjan's algorithm](./09-graphs/12-strongly-connected-components.md) | [Practice](./09-graphs/12-strongly-connected-components-practice.md)
- [9.13 Bridges and articulation points](./09-graphs/13-bridges-and-articulation-points.md) | [Practice](./09-graphs/13-bridges-and-articulation-points-practice.md)
- [9.14 Introduction to network flow: Ford-Fulkerson / max-flow min-cut](./09-graphs/14-network-flow-intro.md) | [Practice](./09-graphs/14-network-flow-intro-practice.md)

### [Phase 10 — Greedy Algorithms](./10-greedy/README.md)
- [10.1 What makes a problem greedy: greedy-choice property & exchange argument proofs](./10-greedy/01-greedy-choice-property-and-proofs.md) | [Practice](./10-greedy/01-greedy-choice-property-and-proofs-practice.md)
- [10.2 Activity selection / interval scheduling](./10-greedy/02-activity-selection-interval-scheduling.md) | [Practice](./10-greedy/02-activity-selection-interval-scheduling-practice.md)
- [10.3 Fractional knapsack](./10-greedy/03-fractional-knapsack.md) | [Practice](./10-greedy/03-fractional-knapsack-practice.md)
- [10.4 Huffman coding](./10-greedy/04-huffman-coding.md) | [Practice](./10-greedy/04-huffman-coding-practice.md)
- [10.5 Job sequencing with deadlines](./10-greedy/05-job-sequencing-with-deadlines.md) | [Practice](./10-greedy/05-job-sequencing-with-deadlines-practice.md)
- [10.6 Greedy on graphs (Prim's/Kruskal's/Dijkstra's as greedy algorithms)](./10-greedy/06-greedy-on-graphs.md) | [Practice](./10-greedy/06-greedy-on-graphs-practice.md)
- [10.7 When greedy fails — counter-examples that require DP](./10-greedy/07-when-greedy-fails-vs-dp.md) | [Practice](./10-greedy/07-when-greedy-fails-vs-dp-practice.md)

### [Phase 11 — Dynamic Programming](./11-dynamic-programming/README.md)
- [11.1 What is DP: overlapping subproblems & optimal substructure, memoization vs tabulation](./11-dynamic-programming/01-dp-fundamentals-memoization-vs-tabulation.md) | [Practice](./11-dynamic-programming/01-dp-fundamentals-memoization-vs-tabulation-practice.md)
- [11.2 Converting recursion to memoization to tabulation (step-by-step)](./11-dynamic-programming/02-recursion-to-dp-conversion.md) | [Practice](./11-dynamic-programming/02-recursion-to-dp-conversion-practice.md)
- [11.3 1D DP: climbing stairs, house robber, maximum subarray](./11-dynamic-programming/03-1d-dp-patterns.md) | [Practice](./11-dynamic-programming/03-1d-dp-patterns-practice.md)
- [11.4 2D DP (grid): unique paths, minimum path sum, grid with obstacles](./11-dynamic-programming/04-2d-grid-dp.md) | [Practice](./11-dynamic-programming/04-2d-grid-dp-practice.md)
- [11.5 Knapsack family: 0/1 knapsack, unbounded knapsack, subset sum, partition sum](./11-dynamic-programming/05-knapsack-family.md) | [Practice](./11-dynamic-programming/05-knapsack-family-practice.md)
- [11.6 Longest Common Subsequence (LCS) and its variants](./11-dynamic-programming/06-lcs-and-string-dp.md) | [Practice](./11-dynamic-programming/06-lcs-and-string-dp-practice.md)
- [11.7 Longest Increasing Subsequence (LIS): O(n²) and O(n log n) approaches](./11-dynamic-programming/07-lis-patterns.md) | [Practice](./11-dynamic-programming/07-lis-patterns-practice.md)
- [11.8 Matrix Chain Multiplication and interval DP](./11-dynamic-programming/08-mcm-and-interval-dp.md) | [Practice](./11-dynamic-programming/08-mcm-and-interval-dp-practice.md)
- [11.9 DP on trees](./11-dynamic-programming/09-dp-on-trees.md) | [Practice](./11-dynamic-programming/09-dp-on-trees-practice.md)
- [11.10 DP on bitmasks (traveling salesman, assignment problems)](./11-dynamic-programming/10-dp-on-bitmasks.md) | [Practice](./11-dynamic-programming/10-dp-on-bitmasks-practice.md)
- [11.11 Digit DP (counting numbers with a property in a range)](./11-dynamic-programming/11-digit-dp.md) | [Practice](./11-dynamic-programming/11-digit-dp-practice.md)
- [11.12 DP with state compression / rolling arrays](./11-dynamic-programming/12-dp-space-optimization.md) | [Practice](./11-dynamic-programming/12-dp-space-optimization-practice.md)
- [11.13 Practice roadmap: DP pattern decision tree](./11-dynamic-programming/13-dp-pattern-decision-tree.md) | [Practice](./11-dynamic-programming/13-dp-pattern-decision-tree-practice.md)

### [Phase 12 — Advanced Strings](./12-advanced-strings/README.md)
- [12.1 Naive pattern matching recap and inefficiency](./12-advanced-strings/01-naive-pattern-matching.md) | [Practice](./12-advanced-strings/01-naive-pattern-matching-practice.md)
- [12.2 KMP (Knuth-Morris-Pratt) algorithm: LPS array, full derivation](./12-advanced-strings/02-kmp-algorithm.md) | [Practice](./12-advanced-strings/02-kmp-algorithm-practice.md)
- [12.3 Z-algorithm](./12-advanced-strings/03-z-algorithm.md) | [Practice](./12-advanced-strings/03-z-algorithm-practice.md)
- [12.4 Rabin-Karp algorithm (rolling hash)](./12-advanced-strings/04-rabin-karp-algorithm.md) | [Practice](./12-advanced-strings/04-rabin-karp-algorithm-practice.md)
- [12.5 Trie-based string algorithms revisited](./12-advanced-strings/05-trie-advanced-string-algorithms.md) | [Practice](./12-advanced-strings/05-trie-advanced-string-algorithms-practice.md)
- [12.6 Manacher's algorithm (longest palindromic substring in linear time)](./12-advanced-strings/06-manachers-algorithm.md) | [Practice](./12-advanced-strings/06-manachers-algorithm-practice.md)
- [12.7 Suffix array & suffix tree conceptual overview](./12-advanced-strings/07-suffix-array-and-suffix-tree.md) | [Practice](./12-advanced-strings/07-suffix-array-and-suffix-tree-practice.md)

### [Phase 13 — Bit Manipulation & Math for DSA](./13-bit-manipulation-and-math/README.md)
- [13.1 Binary representation, two's complement, bitwise operators recap](./13-bit-manipulation-and-math/01-bitwise-operators-and-binary-basics.md) | [Practice](./13-bit-manipulation-and-math/01-bitwise-operators-and-binary-basics-practice.md)
- [13.2 Common bit tricks: check/set/clear/toggle bit, set bits count, power of 2](./13-bit-manipulation-and-math/02-essential-bit-tricks.md) | [Practice](./13-bit-manipulation-and-math/02-essential-bit-tricks-practice.md)
- [13.3 XOR tricks: single number problems, swapping without temp variable](./13-bit-manipulation-and-math/03-xor-tricks-and-single-number.md) | [Practice](./13-bit-manipulation-and-math/03-xor-tricks-and-single-number-practice.md)
- [13.4 Subsets via bitmasking](./13-bit-manipulation-and-math/04-bitmask-subsets.md) | [Practice](./13-bit-manipulation-and-math/04-bitmask-subsets-practice.md)
- [13.5 Number theory: primes (Sieve of Eratosthenes), GCD/LCM, modular arithmetic](./13-bit-manipulation-and-math/05-number-theory-primes-gcd-sieve.md) | [Practice](./13-bit-manipulation-and-math/05-number-theory-primes-gcd-sieve-practice.md)
- [13.6 Modular exponentiation, modular inverse](./13-bit-manipulation-and-math/06-modular-exponentiation-and-inverse.md) | [Practice](./13-bit-manipulation-and-math/06-modular-exponentiation-and-inverse-practice.md)
- [13.7 Combinatorics basics: permutations, combinations, Pascal's triangle, nCr](./13-bit-manipulation-and-math/07-combinatorics-basics.md) | [Practice](./13-bit-manipulation-and-math/07-combinatorics-basics-practice.md)
- [13.8 Basic game theory (Nim game, Grundy numbers)](./13-bit-manipulation-and-math/08-game-theory-basics.md) | [Practice](./13-bit-manipulation-and-math/08-game-theory-basics-practice.md)

### [Phase 14 — Advanced Topics (Capstone / Competitive-level)](./14-advanced-topics/README.md)
- [14.1 Advanced graph: network flow deep dive, bipartite matching](./14-advanced-topics/01-network-flow-deep-dive.md) | [Practice](./14-advanced-topics/01-network-flow-deep-dive-practice.md)
- [14.2 Advanced DP: DP + bitmask + trees combined problems](./14-advanced-topics/02-advanced-dp-combinations.md) | [Practice](./14-advanced-topics/02-advanced-dp-combinations-practice.md)
- [14.3 Sqrt decomposition, Mo's algorithm](./14-advanced-topics/03-sqrt-decomposition-and-mos-algorithm.md) | [Practice](./14-advanced-topics/03-sqrt-decomposition-and-mos-algorithm-practice.md)
- [14.4 Heavy-Light Decomposition (conceptual overview)](./14-advanced-topics/04-heavy-light-decomposition.md) | [Practice](./14-advanced-topics/04-heavy-light-decomposition-practice.md)
- [14.5 Randomized algorithms basics (reservoir sampling, random pivot quicksort)](./14-advanced-topics/05-randomized-algorithms.md) | [Practice](./14-advanced-topics/05-randomized-algorithms-practice.md)
- [14.6 Competitive programming contest strategy](./14-advanced-topics/06-competitive-programming-strategy.md) | [Practice](./14-advanced-topics/06-competitive-programming-strategy-practice.md)

### [Phase 15 — Interview Prep & Capstone](./15-interview-prep/README.md)
- [15.1 Pattern recognition cheat sheet: phrasing -> likely pattern/data structure](./15-interview-prep/01-pattern-recognition-cheat-sheet.md) | [Practice](./15-interview-prep/01-pattern-recognition-cheat-sheet-practice.md)
- [15.2 Company-wise curated question lists](./15-interview-prep/02-company-wise-question-lists.md) | [Practice](./15-interview-prep/02-company-wise-question-lists-practice.md)
- [15.3 Mock interview structure: talking out loud, clarifying questions](./15-interview-prep/03-mock-interview-structure.md) | [Practice](./15-interview-prep/03-mock-interview-structure-practice.md)
- [15.4 Time/space tradeoff discussions expected in interviews](./15-interview-prep/04-time-space-tradeoff-discussions.md) | [Practice](./15-interview-prep/04-time-space-tradeoff-discussions-practice.md)
- [15.5 System-design-adjacent DSA capstone projects](./15-interview-prep/05-system-design-adjacent-dsa.md) | [Practice](./15-interview-prep/05-system-design-adjacent-dsa-practice.md)
- [15.6 Full mock test set: timed mixed-topic problem sets](./15-interview-prep/06-full-mock-test-set.md) | [Practice](./15-interview-prep/06-full-mock-test-set-practice.md)
- [15.7 Final review checklist before an interview/assessment](./15-interview-prep/07-final-pre-interview-checklist.md) | [Practice](./15-interview-prep/07-final-pre-interview-checklist-practice.md)

---

## 🛠️ Contribution & Maintenance

This repository is maintained as an open-access, zero-gap computer science learning resource. Every code file is benchmarked against standard C++17 compilers (`g++ -std=c++17 -O2`).