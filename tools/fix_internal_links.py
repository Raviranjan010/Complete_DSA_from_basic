"""
Fix legacy relative markdown links to point to new canonical locations.
"""

import os
import re
from pathlib import Path

replacements = {
    '../01_Complexity_Analysis/01_notes.md': '../../01-Complexity-Analysis/concepts/01-asymptotic-analysis-and-big-o.md',
    '../02_Arrays/02_notes.md': '../../03-Arrays-and-Strings/concepts/01-array-master-notes.md',
    '../02_Arrays/ARRAY_MASTER_NOTES.md': '../../03-Arrays-and-Strings/concepts/01-array-master-notes.md',
    '../03_Strings/03_notes.md': '../../03-Arrays-and-Strings/concepts/03-strings-fundamentals-and-manipulation.md',
    '../04_Recursion_and_Backtracking/04_notes.md': '../../07-Recursion-and-Backtracking/concepts/01-recursion-foundations-and-call-stack.md',
    '../05_Sorting_and_Searching/05_notes.md': '../../04-Searching-and-Sorting/concepts/03-sorting-algorithms-theory.md',
    '../06_Linked_List/06_notes.md': '../../08-Linked-List/concepts/01-linked-list-fundamentals-and-operations.md',
    '../07_Stack/07_notes.md': '../../09-Stack-and-Queue/concepts/01-stack-fundamentals-and-monotonic-stack.md',
    '../08_Queue_and_Deque/08_notes.md': '../../09-Stack-and-Queue/concepts/02-queue-deque-and-sliding-window-maximum.md',
    '../09_Hashing/09_notes.md': '../../06-Hashing/concepts/01-hashing-fundamentals-and-collision-handling.md',
    '../10_Trees/10_notes.md': '../../10-Trees/concepts/01-binary-trees-fundamentals-and-traversals.md',
    '../11_Binary_Search_Tree/11_notes.md': '../../10-Trees/concepts/02-binary-search-tree-properties-and-ops.md',
    '../12_Heaps_and_Priority_Queue/12_notes.md': '../../11-Heap-and-Priority-Queue/concepts/01-heaps-and-priority-queues-theory.md',
    '../13_Tries/13_notes.md': '../../17-Advanced-Data-Structures/concepts/01-trie-prefix-tree-guide.md',
    '../14_Graphs/14_notes.md': '../../13-Graphs/concepts/01-graph-representations-and-traversals.md',
    '../15_Dynamic_Programming/15_notes.md': '../../14-Dynamic-Programming/concepts/01-dp-fundamentals-memoization-tabulation.md',
    '../16_Greedy_Algorithms/16_notes.md': '../../12-Greedy-and-Intervals/concepts/01-greedy-choice-property-and-proofs.md',
    '../18_Bit_Manipulation/18_notes.md': '../../15-Bit-Manipulation/concepts/01-bitwise-operators-and-binary-tricks.md',
    '../19_Segment_Tree_and_BIT/19_notes.md': '../../17-Advanced-Data-Structures/concepts/02-segment-tree-and-fenwick-tree.md',
    '../20_Advanced_Graphs/20_notes.md': '../../13-Graphs/concepts/02-shortest-paths-and-advanced-graphs.md',
    '../21_Advanced_DP/21_notes.md': '../../14-Dynamic-Programming/concepts/02-advanced-dp-and-optimizations.md',
    '../22_Competitive_Programming_Extras/22_notes.md': '../../18-Advanced-Algorithms/concepts/01-competitive-programming-patterns.md',
    '../01_Two_Pointer/Notes.md': '../../05-Two-Pointers-and-Sliding-Window/concepts/01-two-pointers-technique-guide.md',
    '../02_Sliding_Window/Notes.md': '../../05-Two-Pointers-and-Sliding-Window/concepts/02-sliding-window-fixed-and-variable.md',
    '../03_Prefix_Sum/Notes.md': '../../05-Two-Pointers-and-Sliding-Window/concepts/03-prefix-sum-and-difference-array.md',
    '../04_Kadane/Notes.md': '../../03-Arrays-and-Strings/concepts/02-subarrays-and-kadane-algorithm.md',
    '../05_Binary_Search/Notes.md': '../../04-Searching-and-Sorting/concepts/01-linear-and-binary-search-foundations.md',
    '00_notes.md': '01-getting-started-basics.md',
    '01_notes.md': '01-asymptotic-analysis-and-big-o.md',
    'Array_Basics.md': '01-array-master-notes.md',
    'Indexing_and_Traversal.md': '01-array-master-notes.md',
    'Complexity_Analysis.md': '../../01-Complexity-Analysis/concepts/01-asymptotic-analysis-and-big-o.md',
    'Memory_Model.md': '09-pointers-and-memory-model.md',
    '01-array-master-notes.md': '01-array-master-notes.md',
    'ROADMAP.md': '../../_archive/DSA_server-main/ROADMAP.md',
    'STUDY_PLAN.md': '../../_archive/DSA_server-main/STUDY_PLAN.md',
    'PROBLEM_INDEX.md': '../README.md',
    '00_Fundamentals/05_Easy_Problems.md': '../problems/001-two-sum-pair-sum.md',
    '06_Medium_Problems/Complete_Solutions.md': '../problems/002-majority-element.md',
    '07_Hard_Problems/Complete_Solutions.md': '../problems/004-maximum-subarray-kadane.md',
    '08_Pattern_Recognition/Complete_Guide.md': '04-pattern-recognition-guide.md',
    '09_Common_Mistakes/Complete_Guide.md': '05-common-mistakes-and-pitfalls.md',
    '../00_Fundamentals/Array_Easy_Problems.md': '../problems/001-two-sum-pair-sum.md',
    'Problems/Easy.md': '../problems/001-two-sum-pair-sum.md',
    'Problems/Medium.md': '../problems/002-majority-element.md',
    'Problems/Hard.md': '../problems/004-maximum-subarray-kadane.md',
    '../Notes.md': '02-subarrays-and-kadane-algorithm.md',
    'Patterns.md': '04-pattern-recognition-guide.md',
    'Mistakes.md': '05-common-mistakes-and-pitfalls.md',
    'Notes.md': '01-array-master-notes.md'
}

def fix_links():
    fixed_count = 0
    for root, dirs, files in os.walk('.'):
        if root == '.' or '.git' in Path(root).parts or '_meta' in Path(root).parts or '_archive' in Path(root).parts:
            continue
        for f in files:
            if not f.endswith('.md'): continue
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as mf:
                content = mf.read()
            original = content
            for old_target, new_target in replacements.items():
                if f'({old_target})' in content:
                    content = content.replace(f'({old_target})', f'({new_target})')
            if os.path.basename(root) == 'concepts' and '(README.md)' in content:
                content = content.replace('(README.md)', '(../README.md)')
            if content != original:
                with open(fp, 'w', encoding='utf-8') as mf:
                    mf.write(content)
                fixed_count += 1
    print(f'Fixed legacy links across {fixed_count} markdown files.')

if __name__ == '__main__':
    fix_links()
