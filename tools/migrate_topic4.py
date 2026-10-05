import os
import shutil
import csv

os.makedirs('04-Searching-and-Sorting/concepts', exist_ok=True)
os.makedirs('04-Searching-and-Sorting/problems', exist_ok=True)
os.makedirs('04-Searching-and-Sorting/code', exist_ok=True)

ledger = []

# README
with open('04-Searching-and-Sorting/README.md', 'w', encoding='utf-8') as f:
    f.write('# 04 — Searching and Sorting\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `03-Arrays-and-Strings`\n\nLinear and binary search, binary search on answer, comparison-based and non-comparison sorting algorithms.\n')
ledger.append(('04-Searching-and-Sorting/README.md', 'NA', 'NA', 'Created topic hub README for Searching and Sorting'))

# Concepts
concepts = [
    ('04-Searching-and-Sorting/concepts/01-linear-and-binary-search-foundations.md', 'DSA_ac-main/Array/08_DSA_Binary_Search_Complete_Notes.md', ['Summer_pep_DSA-main/04-Binary-Search.md', 'DSA_final-main/02_Arrays/03_Binary Search.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Notes.md'], 'Consolidated binary search foundations, dry runs, and invariants'),
    ('04-Searching-and-Sorting/concepts/02-binary-search-patterns-and-bs-on-answer.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Patterns.md', ['DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Mistakes.md'], 'Binary search pattern recognition, boundary search, and BS on answer'),
    ('04-Searching-and-Sorting/concepts/03-sorting-algorithms-theory.md', 'DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/05_notes.md', [], 'Sorting algorithms comparison, stability, and recurrence analysis'),
    ('04-Searching-and-Sorting/concepts/04-searching-and-sorting-mcqs.md', 'DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/05_mcqs.md', [], 'Self-check MCQs for searching and sorting')
]

for target, base, contribs, desc in concepts:
    if os.path.exists(base):
        content = ''
        with open(base, 'r', encoding='utf-8', errors='ignore') as f_b:
            content = f_b.read()
        for c in contribs:
            if os.path.exists(c):
                with open(c, 'r', encoding='utf-8', errors='ignore') as f_c:
                    content += '\n\n---\n\n## Supplementary Notes from ' + os.path.basename(c) + '\n\n' + f_c.read()
        with open(target, 'w', encoding='utf-8') as f_out:
            f_out.write(content)
        ledger.append((target, base, '; '.join(contribs) if contribs else 'None', desc))

# Canonical Problems
problems = [
    ('04-Searching-and-Sorting/problems/001-binary-search-basic.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Easy.md', 'Basic binary search problems suite'),
    ('04-Searching-and-Sorting/problems/002-search-in-rotated-sorted-array.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Medium.md', 'Rotated sorted array and boundary search problems'),
    ('04-Searching-and-Sorting/problems/003-binary-search-2d-matrix.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/2D_Arrays.md', '2D Matrix binary search problems'),
    ('04-Searching-and-Sorting/problems/004-binary-search-on-answer-hard.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/05_Binary_Search/Problems/Hard.md', 'BS on answer / min-max allocation problems')
]

for target, base, desc in problems:
    if os.path.exists(base):
        with open(base, 'r', encoding='utf-8', errors='ignore') as f_in:
            with open(target, 'w', encoding='utf-8') as f_out:
                f_out.write(f_in.read())
        ledger.append((target, base, 'None', desc))

# Code Solutions
code_mapping = [
    ('04-Searching-and-Sorting/code/001-linear-search', 'dsa-main/linerr_search.cpp', ['dsa-main/linear_search2.cpp'], 'Linear search implementation in array'),
    ('04-Searching-and-Sorting/code/002-binary-search', 'DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/code/binary_search.cpp', ['dsa-main/5_firstAndLastOccurence.cpp'], 'Binary search iterative/recursive and first/last occurrence'),
    ('04-Searching-and-Sorting/code/003-sorting-algorithms', 'DSA_server-main/DSA-MasterCourse/05_Sorting_and_Searching/code/sorting.cpp', ['dsa-main/7_sort_Squared_array.cpp'], 'Classic sorting implementations: Bubble, Selection, Insertion, Merge, Quick, and two-pointer sort')
]

for cdir, base, extras, desc in code_mapping:
    os.makedirs(cdir, exist_ok=True)
    if os.path.exists(base):
        shutil.copy(base, f'{cdir}/solution.cpp')
    for extra in extras:
        if os.path.exists(extra):
            fn = os.path.basename(extra)
            shutil.copy(extra, f'{cdir}/{fn}')
    ledger.append((f'{cdir}/solution.cpp', base, '; '.join(extras) if extras else 'None', desc))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 4: {len(ledger)} actions logged')
