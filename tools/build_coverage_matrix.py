#!/usr/bin/env python3
"""
tools/build_coverage_matrix.py
Constructs _meta/COVERAGE_SOURCES.md and _meta/COVERAGE_MATRIX.csv strictly adhering to
Section 4 of REPAIR_PROMPT_v3 and CP-B guidance:
- Relabels L6 as "agent-curated, no external source" with one-line reason for each of the 35 titles.
- Maps CSES problems to topics matching their CSES section, preserving the section name.
- Generates reproducible, script-driven coverage matrix and summary tables.
"""

import os
import re
import csv
from pathlib import Path
from collections import defaultdict

repo_root = Path(__file__).resolve().parent.parent

# 1. Prepare L6 Textbook classics with one-line pedagogical rationale
textbook_classics = [
    ('Bubble Sort, Selection Sort & Insertion Sort', '04-Searching-and-Sorting', '#sorting-elementary', 'L1 Basic',
     'Fundamental O(N^2) comparison sorts demonstrating in-place swapping and loop invariant maintenance.'),
    ('Merge Sort & Inversion Count', '04-Searching-and-Sorting', '#divide-and-conquer', 'L2 Medium',
     'Canonical divide-and-conquer algorithm with stable O(N log N) runtime and classical array inversion counting.'),
    ('Quick Sort & Quickselect', '04-Searching-and-Sorting', '#partitioning', 'L2 Medium',
     'Core partitioning algorithm illustrating Lomuto/Hoare pivots and expected O(N) order statistics selection.'),
    ('Heap Sort', '04-Searching-and-Sorting', '#heapsort', 'L2 Medium',
     'In-place O(N log N) sorting leveraging binary heap property and sift-down operations without extra memory.'),
    ('Counting Sort & Radix Sort', '04-Searching-and-Sorting', '#non-comparison-sort', 'L2 Medium',
     'Foundational non-comparison linear-time sorting algorithms for bounded integer keys.'),
    ('Singly Linked List Insertion & Deletion', '08-Linked-List', '#linked-list-ops', 'L1 Basic',
     'Elementary pointer manipulation covering head/tail insertions, node removal, and sentinel nodes.'),
    ('Reverse Linked List (Iterative & Recursive)', '08-Linked-List', '#linked-list-reversal', 'L1 Basic',
     'Foundational pointer reversal problem testing three-pointer iterative mechanics and call-stack recursion.'),
    ('Linked List Cycle Detection (Floyd Cycle)', '08-Linked-List', '#fast-slow-pointers', 'L1 Basic',
     'Definitive two-pointer slow/fast cycle detection algorithm with mathematical proof of meeting point.'),
    ('Merge Two Sorted Linked Lists', '08-Linked-List', '#merge-linked-lists', 'L1 Basic',
     'Standard linear-time list splicing technique forming the base subroutine of linked list merge sort.'),
    ('Stack Implementation via Array & Linked List', '09-Stack-and-Queue', '#stack-design', 'L1 Basic',
     'Canonical LIFO data structure implementation exploring dynamic array growth and memory trade-offs.'),
    ('Queue Implementation via Circular Array', '09-Stack-and-Queue', '#queue-design', 'L1 Basic',
     'Standard FIFO data structure utilizing modulo arithmetic to prevent linear array drift.'),
    ('Min Stack Design O(1)', '09-Stack-and-Queue', '#min-stack', 'L2 Medium',
     'Classical auxiliary stack / paired value pattern enabling constant-time minimum element queries.'),
    ('Binary Tree Traversals (Inorder, Preorder, Postorder)', '10-Trees', '#tree-traversal', 'L1 Basic',
     'Fundamental recursive and iterative tree traversal techniques establishing baseline tree traversal orderings.'),
    ('Level Order Traversal (BFS)', '10-Trees', '#bfs-tree', 'L2 Medium',
     'Foundational queue-based breadth-first tree traversal computing per-level node groupings.'),
    ('Lowest Common Ancestor in Binary Tree', '10-Trees', '#lca', 'L2 Medium',
     'Classic divide-and-conquer tree problem identifying the deepest shared ancestor node.'),
    ('Binary Search Tree Search, Insert & Delete', '10-Trees', '#bst-operations', 'L2 Medium',
     'Core BST invariant operations including predecessor/successor replacement upon two-child deletion.'),
    ('Min Heap & Max Heapify Operations', '11-Heap-and-Priority-Queue', '#heapify', 'L2 Medium',
     'Binary tree array representation implementing sift-up, sift-down, and O(N) bottom-up heap construction.'),
    ('Top K Frequent Elements', '11-Heap-and-Priority-Queue', '#top-k', 'L2 Medium',
     'Classical heap / bucket select pattern demonstrating O(N log K) priority queue maintenance.'),
    ('Activity Selection / Interval Scheduling', '12-Greedy-and-Intervals', '#greedy-intervals', 'L2 Medium',
     'Definitive greedy algorithm proving optimal choice by earliest finish time ordering.'),
    ('Fractional Knapsack Problem', '12-Greedy-and-Intervals', '#fractional-knapsack', 'L2 Medium',
     'Benchmark continuous greedy problem using value-to-weight density sorting.'),
    ('Graph Representation (Adjacency Matrix & List)', '13-Graphs', '#graph-basics', 'L1 Basic',
     'Core vertex-edge data structure modeling with memory and traversal efficiency trade-offs.'),
    ('Breadth First Search (BFS) in Graph', '13-Graphs', '#bfs-graph', 'L2 Medium',
     'Standard unweighted shortest path and level-order traversal algorithm using queue and visited array.'),
    ('Depth First Search (DFS) in Graph', '13-Graphs', '#dfs-graph', 'L2 Medium',
     'Foundational recursive graph exploration pattern used for connectivity, cycle detection, and component labeling.'),
    ('Dijkstra Shortest Path Algorithm', '13-Graphs', '#dijkstra', 'L3 Advanced',
     'Canonical non-negative edge single-source shortest path algorithm using min-priority queue relaxation.'),
    ('Bellman-Ford Shortest Path Algorithm', '13-Graphs', '#bellman-ford', 'L3 Advanced',
     'Dynamic programming shortest path algorithm supporting negative weights and detecting negative cycles.'),
    ('Floyd-Warshall All-Pairs Shortest Path', '13-Graphs', '#floyd-warshall', 'L3 Advanced',
     'Classic triple-nested O(V^3) all-pairs shortest path matrix DP algorithm.'),
    ('Topological Sort (Kahn Algorithm & DFS)', '13-Graphs', '#topological-sort', 'L2 Medium',
     'Essential directed acyclic graph (DAG) linear ordering using in-degree queue or post-order DFS stack.'),
    ('Disjoint Set Union (DSU with Union by Rank & Path Compression)', '17-Advanced-Data-Structures', '#dsu', 'L3 Advanced',
     'Essential near-O(1) amortized partition structure for dynamic graph connectivity.'),
    ('Kruskal Minimum Spanning Tree', '13-Graphs', '#mst-kruskal', 'L3 Advanced',
     'Greedy edge-centric minimum spanning tree algorithm combining edge sorting with DSU cycle checks.'),
    ('Prim Minimum Spanning Tree', '13-Graphs', '#mst-prim', 'L3 Advanced',
     'Greedy vertex-centric minimum spanning tree algorithm growing the tree using priority queue cut edges.'),
    ('0/1 Knapsack Problem (Tabulation & Space Optimization)', '14-Dynamic-Programming', '#01-knapsack', 'L2 Medium',
     'Foundational dynamic programming subset problem teaching weight-capacity state transition and 1D rolling array.'),
    ('Longest Common Subsequence (LCS)', '14-Dynamic-Programming', '#lcs', 'L2 Medium',
     'Standard two-string 2D dynamic programming formulation for string alignment and edit distance.'),
    ('Longest Increasing Subsequence (LIS O(N log N))', '14-Dynamic-Programming', '#lis-patience-sort', 'L3 Advanced',
     'Benchmark sequence optimization combining dynamic programming with patience sorting / binary search.'),
    ('Matrix Chain Multiplication (Interval DP)', '14-Dynamic-Programming', '#interval-dp', 'L3 Advanced',
     'Classic interval dynamic programming problem illustrating optimal parenthesization over subranges [i, j].'),
    ('Bit Manipulation: Check, Set, Clear, Toggle, Lowest Set Bit', '15-Bit-Manipulation', '#bit-tricks', 'L1 Basic',
     'Fundamental bitwise mask operations and Brian Kernighan bit-twiddling primitives.')
]

# 2. Write _meta/COVERAGE_SOURCES.md
sources_md = """# Problem Coverage Sources (`_meta/COVERAGE_SOURCES.md`)

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

"""

for idx, (title, top, pat, lvl, reason) in enumerate(textbook_classics, 1):
    sources_md += f"{idx}. **{title}** (`{top}`): {reason}\n"

(repo_root / '_meta' / 'COVERAGE_SOURCES.md').write_text(sources_md, encoding='utf-8')

# 3. Collect verified problems
problems = {}

def add_prob(title, list_id, topic, pattern="General", level="L2 Medium", status="MISSING", source_section="NA"):
    t_clean = title.strip()
    if t_clean not in problems:
        problems[t_clean] = {
            'topic': topic,
            'pattern': pattern,
            'level': level,
            'lists': set(),
            'status': status,
            'source_section': source_section
        }
    problems[t_clean]['lists'].add(list_id)
    if source_section != "NA":
        problems[t_clean]['source_section'] = source_section

# L7: Existing repository problems (23 problems across 00, 01, 02, 03, 04, 05)
existing_map = {
    '00-Start-Here': [
        ('Pointer Fundamentals and Memory Addresses', '#pointers', 'L0 Foundational'),
        ('Pass by Value vs Pass by Reference', '#functions', 'L0 Foundational'),
        ('Array Decay and Dynamic Memory Allocation', '#memory-model', 'L0 Foundational')
    ],
    '01-Complexity-Analysis': [
        ('Time Complexity Benchmarking', '#complexity-analysis', 'L1 Basic'),
        ('Space Complexity and Call Stack', '#space-complexity', 'L1 Basic')
    ],
    '02-Math-for-DSA': [
        ('GCD and LCM Euclidean', '#math', 'L1 Basic'),
        ('Fast Binary Exponentiation', '#binary-exponentiation', 'L2 Medium'),
        ('Sieve of Eratosthenes', '#sieve', 'L2 Medium'),
        ('Prime Factorization SPF', '#spf', 'L2 Medium'),
        ('Modular Arithmetic and Modular Inverse', '#modular-arithmetic', 'L2 Medium'),
        ('Armstrong and Palindrome Number', '#digit-math', 'L1 Basic')
    ],
    '03-Arrays-and-Strings': [
        ('Two Sum (Pair Sum Problem)', '#hash-map', 'L1 Basic'),
        ('Majority Element (Boyer-Moore)', '#boyer-moore', 'L2 Medium'),
        ('Product of Array Except Self', '#prefix-suffix', 'L2 Medium'),
        ('Maximum Subarray (Kadane)', '#kadane', 'L2 Medium')
    ],
    '04-Searching-and-Sorting': [
        ('Binary Search Basic', '#binary-search', 'L1 Basic'),
        ('Search in Rotated Sorted Array', '#binary-search-rotated', 'L2 Medium'),
        ('Binary Search 2D Matrix', '#matrix-binary-search', 'L2 Medium'),
        ('Binary Search on Answer Hard', '#bs-on-answer', 'L3 Advanced')
    ],
    '05-Two-Pointers-and-Sliding-Window': [
        ('Two Pointers Foundations', '#two-pointers', 'L1 Basic'),
        ('Two Pointers Easy Medium Hard', '#two-pointers', 'L2 Medium'),
        ('Sliding Window Problems', '#sliding-window', 'L2 Medium'),
        ('Prefix Sum Problems', '#prefix-sum', 'L2 Medium')
    ]
}

for top, p_list in existing_map.items():
    for name, pat, lvl in p_list:
        add_prob(name, 'L7', top, pattern=pat, level=lvl, status='EXISTS (NEEDS-REWRITE)', source_section='Existing Repo')

# L5: CSES tasks mapped strictly to topics matching their CSES section
# Introductory Problems (24 tasks)
cses_introductory = [
    ('Weird Algorithm', '01-Complexity-Analysis', '#simulation-collatz', 'L1 Basic'),
    ('Missing Number', '03-Arrays-and-Strings', '#math-xor', 'L1 Basic'),
    ('Repetitions', '03-Arrays-and-Strings', '#string-traversal', 'L1 Basic'),
    ('Increasing Array', '03-Arrays-and-Strings', '#greedy-array', 'L1 Basic'),
    ('Permutations', '03-Arrays-and-Strings', '#constructive-array', 'L2 Medium'),
    ('Number Spiral', '02-Math-for-DSA', '#math-pattern', 'L2 Medium'),
    ('Two Knights', '02-Math-for-DSA', '#combinatorics', 'L2 Medium'),
    ('Two Sets', '02-Math-for-DSA', '#constructive-math', 'L2 Medium'),
    ('Bit Strings', '02-Math-for-DSA', '#modular-exponentiation', 'L2 Medium'),
    ('Trailing Zeros', '02-Math-for-DSA', '#legendre-formula', 'L2 Medium'),
    ('Coin Piles', '02-Math-for-DSA', '#linear-equations', 'L2 Medium'),
    ('Palindrome Reorder', '03-Arrays-and-Strings', '#counting-palindrome', 'L2 Medium'),
    ('Gray Code', '06-Recursion-and-Backtracking', '#gray-code-recursion', 'L2 Medium'),
    ('Tower of Hanoi', '06-Recursion-and-Backtracking', '#classic-recursion', 'L2 Medium'),
    ('Creating Strings', '06-Recursion-and-Backtracking', '#backtracking-permutations', 'L2 Medium'),
    ('Apple Division', '06-Recursion-and-Backtracking', '#subset-generation', 'L2 Medium'),
    ('Chessboard and Queens', '06-Recursion-and-Backtracking', '#n-queens-backtracking', 'L3 Advanced'),
    ('Raab Game I', '06-Recursion-and-Backtracking', '#game-theory-recursion', 'L3 Advanced'),
    ('Mex Grid Construction', '06-Recursion-and-Backtracking', '#constructive-grid', 'L3 Advanced'),
    ('Knight Moves Grid', '06-Recursion-and-Backtracking', '#grid-backtracking', 'L3 Advanced'),
    ('Grid Coloring I', '06-Recursion-and-Backtracking', '#grid-coloring', 'L3 Advanced'),
    ('Digit Queries', '02-Math-for-DSA', '#digit-math', 'L3 Advanced'),
    ('String Reorder', '03-Arrays-and-Strings', '#greedy-counting', 'L3 Advanced'),
    ('Grid Path Description', '06-Recursion-and-Backtracking', '#pruned-backtracking', 'L3 Advanced')
]

for name, top, pat, lvl in cses_introductory:
    add_prob(f"CSES: {name}", 'L5', top, pattern=pat, level=lvl, status='MISSING', source_section='Introductory Problems')

# Sorting and Searching (23 tasks) -> all map to 04-Searching-and-Sorting
cses_sorting_searching = [
    ('Distinct Numbers', '#hash-sorting', 'L1 Basic'),
    ('Apartments', '#two-pointers-sorting', 'L2 Medium'),
    ('Ferris Wheel', '#greedy-two-pointers', 'L2 Medium'),
    ('Concert Tickets', '#binary-search-multiset', 'L2 Medium'),
    ('Restaurant Customers', '#sweep-line', 'L2 Medium'),
    ('Movie Festival', '#interval-scheduling', 'L2 Medium'),
    ('Sum of Two Values', '#two-pointers-twosum', 'L1 Basic'),
    ('Maximum Subarray Sum', '#kadane', 'L2 Medium'),
    ('Stick Lengths', '#median-minimization', 'L2 Medium'),
    ('Missing Coin Sum', '#greedy-subsets', 'L2 Medium'),
    ('Collecting Numbers', '#inversions-indices', 'L2 Medium'),
    ('Collecting Numbers II', '#inversion-updates', 'L3 Advanced'),
    ('Playlist', '#sliding-window-unique', 'L2 Medium'),
    ('Towers', '#multiset-binary-search', 'L2 Medium'),
    ('Traffic Lights', '#balanced-bst-intervals', 'L3 Advanced'),
    ('Distinct Values Subarrays', '#hash-frequency', 'L3 Advanced'),
    ('Distinct Values Subsequences', '#two-pointers', 'L3 Advanced'),
    ('Josephus Problem I', '#josephus-circle', 'L2 Medium'),
    ('Josephus Problem II', '#order-statistics-tree', 'L3 Advanced'),
    ('Nested Ranges Check', '#interval-sorting', 'L3 Advanced'),
    ('Nested Ranges Count', '#fenwick-intervals', 'L3 Advanced'),
    ('Room Allocation', '#interval-greedy-heap', 'L3 Advanced'),
    ('Factory Machines', '#binary-search-on-answer', 'L3 Advanced')
]

for name, pat, lvl in cses_sorting_searching:
    add_prob(f"CSES: {name}", 'L5', '04-Searching-and-Sorting', pattern=pat, level=lvl, status='MISSING', source_section='Sorting and Searching')

# L6: Textbook classics
for name, top, pat, lvl, reason in textbook_classics:
    add_prob(name, 'L6', top, pattern=pat, level=lvl, status='MISSING', source_section='Textbook Classic')

# 4. Write _meta/COVERAGE_MATRIX.csv
csv_path = repo_root / '_meta' / 'COVERAGE_MATRIX.csv'
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['canonical_title', 'topic_folder', 'pattern', 'level', 'lists', 'status', 'registry_id', 'source_section'])
    for idx, (title, data) in enumerate(sorted(problems.items()), 1):
        reg_id = f"P-{idx:04d}"
        lists_str = ';'.join(sorted(data['lists']))
        writer.writerow([title, data['topic'], data['pattern'], data['level'], lists_str, data['status'], reg_id, data['source_section']])

print(f"Total distinct problems in coverage matrix: {len(problems)}")

# 5. Compute per-topic statistics
topic_counts = defaultdict(lambda: {'total': 0, 'exists': 0, 'missing': 0})
for data in problems.values():
    top = data['topic']
    topic_counts[top]['total'] += 1
    if 'EXISTS' in data['status']:
        topic_counts[top]['exists'] += 1
    else:
        topic_counts[top]['missing'] += 1

print("\n| Topic Folder | Total | Exists (Needs Rewrite) | Missing |")
print("|---|---|---|---|")
tot_all, tot_ex, tot_mis = 0, 0, 0
for top in sorted(topic_counts.keys()):
    c = topic_counts[top]
    tot_all += c['total']
    tot_ex += c['exists']
    tot_mis += c['missing']
    print(f"| `{top}` | {c['total']} | {c['exists']} | {c['missing']} |")
print(f"| **Total** | **{tot_all}** | **{tot_ex}** | **{tot_mis}** |")
