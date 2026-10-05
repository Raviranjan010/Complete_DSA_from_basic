# 02 — COMPLETE DSA CURRICULUM (Every Topic, In Order)

> This is the authoritative topic list. Nothing may be removed. Additions
> are welcome but must be inserted in the correct phase, in the correct
> internal order (dependencies before use). Language for all code: **C++**.

---

## Phase 0 — Prerequisites (for true beginners, Persona A)
0.1 What is a program, compiler vs interpreter, what happens when C++ code runs
0.2 Setting up: installing a C++ compiler / using an online judge, writing & running "Hello World"
0.3 Variables, data types, type sizes, `int`, `long long`, `float`, `double`, `char`, `bool`, `string`
0.4 Input/output: `cin`, `cout`, fast I/O for competitive programming
0.5 Operators: arithmetic, relational, logical, bitwise (preview), ternary
0.6 Conditionals: `if/else`, `switch`
0.7 Loops: `for`, `while`, `do-while`, break/continue, nested loops
0.8 Functions: declaration, definition, parameters, return values, pass-by-value vs pass-by-reference
0.9 Arrays basics: declaration, indexing, iterating, fixed size vs dynamic
0.10 Pointers & references from scratch (what is memory, address-of `&`, dereference `*`)
0.11 Structures (`struct`) and basic classes/objects (just enough OOP to understand nodes later)
0.12 Introduction to the C++ Standard Template Library (STL) — what it is and why we'll use it
0.13 Basic math for DSA: modulo operator, integer overflow, GCD/LCM by hand, prime numbers basics

## Phase 1 — Complexity Analysis
1.1 Why we measure efficiency: real-world motivation
1.2 Time complexity intuition (counting steps) before Big-O notation
1.3 Big-O, Big-Theta, Big-Omega — formal definitions with examples
1.4 Best, average, worst case analysis
1.5 Common complexity classes with graphs: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)
1.6 Space complexity, auxiliary space vs input space
1.7 Analyzing loops (single, nested, dependent loops), recursive complexity preview
1.8 Amortized analysis (intuition only, deep dive later with dynamic arrays)

## Phase 2 — Arrays & Strings
2.1 Arrays in depth: memory layout, 1D arrays, static vs dynamic arrays, `std::vector` fully explained
2.2 Multi-dimensional arrays (2D/3D), row-major order
2.3 Array traversal patterns, in-place modification
2.4 Two-pointer technique (opposite-direction and same-direction)
2.5 Sliding window technique (fixed size and variable size)
2.6 Prefix sum and difference arrays
2.7 Kadane's algorithm (maximum subarray)
2.8 Sorting algorithms from scratch: bubble, selection, insertion (with dry runs)
2.9 Sorting algorithms (efficient): merge sort, quick sort, heap sort (heap sort cross-linked once heaps are taught)
2.10 Counting sort, radix sort, bucket sort
2.11 `std::sort` and comparator functions in C++
2.12 Searching: linear search, binary search (iterative + recursive), binary search on answer
2.13 Binary search variants: first/last occurrence, search in rotated sorted array, peak element
2.14 Strings in depth: `std::string`, mutability, common operations
2.15 String traversal & manipulation patterns (reverse, palindrome check, anagram check)
2.16 Frequency counting with arrays/hash maps on strings
2.17 Two-pointer & sliding window on strings
2.18 Basic pattern matching (naive substring search) — sets up Phase 12
2.19 Cyclic rotations, Dutch national flag problem, merge intervals

## Phase 3 — Recursion & Backtracking
3.1 What is recursion: call stack visualized, base case & recursive case
3.2 Recursion tree diagrams, tracing recursive calls by hand
3.3 Classic recursion: factorial, Fibonacci (and why naive Fibonacci is slow — bridges to Phase 11)
3.4 Recursion on arrays/strings (sum, reverse, check palindrome recursively)
3.5 Multiple recursive calls & recursion trees (subsets via include/exclude)
3.6 Backtracking framework: choose → explore → un-choose
3.7 Backtracking problems: subsets, permutations, combinations, combination sum
3.8 Backtracking on grids/boards: N-Queens, Sudoku solver, Rat in a Maze
3.9 Backtracking on strings: palindrome partitioning, word search
3.10 Recursion & backtracking complexity analysis

## Phase 4 — Linked List
4.1 Why linked lists: arrays' limitations, memory model of a linked list
4.2 Singly linked list: node structure, insertion (head/tail/middle), deletion, traversal
4.3 Searching in a linked list, reversing a linked list (iterative + recursive)
4.4 Doubly linked list: structure and operations
4.5 Circular linked list: structure and operations
4.6 Fast & slow pointer technique: cycle detection (Floyd's algorithm), finding middle node
4.7 Merging two sorted linked lists, merge sort on linked list
4.8 Removing Nth node from end, intersection of two linked lists
4.9 Applications: LRU cache using doubly linked list + hash map
4.10 Linked list vs array — when to use which (decision guide)

## Phase 5 — Stack & Queue
5.1 Stack: LIFO concept, array-based and linked-list-based implementation, `std::stack`
5.2 Stack applications: balanced parentheses, infix/postfix/prefix conversion, expression evaluation
5.3 Monotonic stack pattern: next greater element, next smaller element, stock span
5.4 Queue: FIFO concept, array-based (circular queue) and linked-list-based implementation, `std::queue`
5.5 Deque (double-ended queue), `std::deque`, sliding window maximum using deque
5.6 Priority concepts preview (bridges to Phase 8)
5.7 Implementing a queue using two stacks and vice versa

## Phase 6 — Hashing
6.1 Why hashing: the lookup problem, hash functions intuition
6.2 Collision handling: chaining vs open addressing (conceptual)
6.3 `std::unordered_map`, `std::unordered_set`, `std::map`, `std::set` — differences and complexities
6.4 Frequency counting patterns using hash maps
6.5 Two-sum and generalized k-sum patterns using hashing
6.6 Subarray sum problems using prefix-sum + hashing
6.7 Grouping/categorizing data with hash maps (anagram groups, etc.)
6.8 Custom hashing for pairs/tuples in C++

## Phase 7 — Trees
7.1 Tree terminology: root, node, edge, height, depth, leaf, subtree
7.2 Binary trees: representation in C++, types (full, complete, perfect, balanced, skewed)
7.3 Tree traversals: preorder, inorder, postorder (recursive + iterative with explicit stack)
7.4 Level-order traversal (BFS on trees), views (top/bottom/left/right view)
7.5 Height, diameter, balanced-check, symmetric-check, mirror of a tree
7.6 Binary Search Tree (BST): property, insertion, deletion, search
7.7 BST validation, floor/ceil, kth smallest/largest, BST iterator
7.8 Lowest Common Ancestor (LCA) — binary tree and BST versions
7.9 Balanced BSTs: AVL tree rotations (conceptual + rotation mechanics), Red-Black tree (conceptual overview)
7.10 Trie (prefix tree): structure, insert, search, prefix search, applications
7.11 Segment Tree: build, range query, point update, range update (lazy propagation)
7.12 Fenwick Tree / Binary Indexed Tree: build, point update, prefix query
7.13 Tree DP introduction (diameter via DP, max path sum) — bridges to Phase 11

## Phase 8 — Heaps & Priority Queue
8.1 Heap property (min-heap, max-heap), array representation of a heap
8.2 Heapify, build-heap, insert, extract-min/max, heap sort (full derivation)
8.3 `std::priority_queue` in C++, custom comparators
8.4 Applications: kth largest/smallest element, top-k frequent elements
8.5 K-way merge (merge k sorted lists/arrays)
8.6 Median in a data stream (two-heap technique)

## Phase 9 — Graphs
9.1 Graph terminology: directed/undirected, weighted/unweighted, cyclic/acyclic, degree
9.2 Graph representation: adjacency matrix vs adjacency list, trade-offs
9.3 Graph traversal: BFS (with applications: shortest path in unweighted graph)
9.4 Graph traversal: DFS (with applications: connected components, cycle detection)
9.5 Topological sort: Kahn's algorithm (BFS-based) and DFS-based
9.6 Shortest path: Dijkstra's algorithm (with priority queue)
9.7 Shortest path: Bellman-Ford algorithm (handles negative weights), detecting negative cycles
9.8 Shortest path: Floyd-Warshall algorithm (all-pairs)
9.9 Minimum Spanning Tree: Prim's algorithm, Kruskal's algorithm
9.10 Disjoint Set Union (Union-Find): with path compression & union by rank, applications
9.11 Bipartite graph check (BFS/DFS coloring)
9.12 Strongly Connected Components: Kosaraju's algorithm, Tarjan's algorithm (conceptual)
9.13 Bridges and articulation points
9.14 Introduction to network flow: Ford-Fulkerson / max-flow min-cut (conceptual overview)

## Phase 10 — Greedy Algorithms
10.1 What makes a problem "greedy": greedy-choice property, proof intuition (exchange argument)
10.2 Activity selection / interval scheduling
10.3 Fractional knapsack
10.4 Huffman coding
10.5 Job sequencing with deadlines
10.6 Greedy on graphs (recap: Prim's/Kruskal's/Dijkstra's as greedy algorithms)
10.7 When greedy fails — counter-examples that require DP instead (bridges to Phase 11)

## Phase 11 — Dynamic Programming
11.1 What is DP: overlapping subproblems + optimal substructure, memoization vs tabulation
11.2 Converting recursion to memoization to tabulation (step-by-step, using Fibonacci)
11.3 1D DP: climbing stairs, house robber, maximum subarray (DP view)
11.4 2D DP (grid): unique paths, minimum path sum, grid with obstacles
11.5 Knapsack family: 0/1 knapsack, unbounded knapsack, subset sum, partition equal subset sum
11.6 Longest Common Subsequence (LCS) and its variants (edit distance, longest palindromic subsequence)
11.7 Longest Increasing Subsequence (LIS): O(n²) and O(n log n) approaches
11.8 Matrix Chain Multiplication and interval DP (burst balloons, palindrome partitioning DP)
11.9 DP on trees (revisit Phase 7.13 formally)
11.10 DP on bitmasks (traveling salesman problem, assignment problems)
11.11 Digit DP (counting numbers with a property in a range)
11.12 DP with state compression / rolling arrays for space optimization
11.13 Practice roadmap: how to identify which DP pattern a new problem belongs to (decision tree)

## Phase 12 — Advanced Strings
12.1 Naive pattern matching recap and its inefficiency
12.2 KMP (Knuth-Morris-Pratt) algorithm: LPS array, full derivation
12.3 Z-algorithm
12.4 Rabin-Karp algorithm (rolling hash)
12.5 Trie-based string algorithms revisited (autocomplete, longest common prefix)
12.6 Manacher's algorithm (longest palindromic substring, linear time) — conceptual + implementation
12.7 Suffix array & suffix tree — conceptual overview (advanced/optional deep dive)

## Phase 13 — Bit Manipulation & Math for DSA
13.1 Binary representation, two's complement, bitwise operators recap (AND, OR, XOR, NOT, shifts)
13.2 Common bit tricks: check/set/clear/toggle a bit, count set bits, power of two check
13.3 XOR tricks: single number problems, swapping without a temp variable
13.4 Subsets via bitmasking
13.5 Number theory: primes (Sieve of Eratosthenes), GCD/LCM (Euclidean algorithm), modular arithmetic
13.6 Modular exponentiation, modular inverse
13.7 Combinatorics basics: permutations, combinations, Pascal's triangle, nCr with mod
13.8 Basic game theory (Nim game, Grundy numbers) — optional advanced

## Phase 14 — Advanced Topics (Capstone / Competitive-level)
14.1 Advanced graph: network flow deep dive, bipartite matching (Hopcroft-Karp overview)
14.2 Advanced DP: DP + bitmask + trees combined problems
14.3 Sqrt decomposition, Mo's algorithm (conceptual)
14.4 Heavy-Light Decomposition (conceptual overview)
14.5 Randomized algorithms basics (reservoir sampling, random pivot quicksort)
14.6 Introduction to competitive programming contest strategy (time management, reading constraints to infer complexity)

## Phase 15 — Interview Prep & Capstone
15.1 Pattern recognition cheat sheet: mapping problem phrasing → likely pattern/data structure
15.2 Company-wise curated question lists (structure only — links to curated lists on LeetCode/GfG)
15.3 Mock interview structure: how to talk through a problem out loud, clarifying questions to ask
15.4 Time/space tradeoff discussions expected in interviews
15.5 System-design-adjacent DSA (rate limiters, LRU/LFU cache, designing a hashmap/trie from scratch) — capstone projects
15.6 Full mock test set: timed mixed-topic problem sets (easy/medium/hard bands)
15.7 Final review checklist before an interview/assessment

---

### Dependency notes (must be respected when writing content)
- Phase 2.9 (heap sort) is only *mentioned*, not fully taught, until Phase 8 exists — link forward, don't explain heaps early.
- Phase 3 (recursion) must be complete before Phase 4.6 (recursive traversal ideas), Phase 7 (tree recursion), and Phase 11 (DP).
- Phase 6 (hashing) must be complete before Phase 9.10 is *introduced conceptually*, though Union-Find itself is a new structure taught fully in 9.10.
- Phase 7 (trees) must be complete before Phase 9 (graphs), since trees are a special case of graphs and traversal intuition carries over.
- Phase 8 (heaps) must be complete before Phase 9.6 (Dijkstra with priority queue) and Phase 9.9 (Prim's).
- Phase 10 (greedy) should immediately precede Phase 11 (DP) so 10.7's "greedy fails" examples motivate DP naturally.
