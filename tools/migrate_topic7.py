import os
import shutil
import csv

os.makedirs('07-Recursion-and-Backtracking/concepts', exist_ok=True)
os.makedirs('07-Recursion-and-Backtracking/problems', exist_ok=True)
os.makedirs('07-Recursion-and-Backtracking/code', exist_ok=True)

ledger = []

# README
with open('07-Recursion-and-Backtracking/README.md', 'w', encoding='utf-8') as f:
    f.write('# 07 — Recursion and Backtracking\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`\n\nRecursive problem formulation, call stack visualization, recurrence relations, divide & conquer, and state-space tree exploration (backtracking).\n')
ledger.append(('07-Recursion-and-Backtracking/README.md', 'NA', 'NA', 'Created topic hub README for Recursion and Backtracking'))

# Concepts
concepts = [
    ('07-Recursion-and-Backtracking/concepts/01-recursion-foundations-and-call-stack.md', 'DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/04_notes.md', ['Summer_pep_DSA-main/06-Recursion.md'], 'Consolidated recursion foundations, call stack diagrams, and base case rules'),
    ('07-Recursion-and-Backtracking/concepts/02-divide-and-conquer-principles.md', 'DSA_server-main/DSA-MasterCourse/17_Divide_and_Conquer/17_notes.md', [], 'Divide and conquer strategy, recurrence solving, and master theorem preview'),
    ('07-Recursion-and-Backtracking/concepts/03-recursion-and-backtracking-mcqs.md', 'DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/04_mcqs.md', [], 'Self-check MCQs for recursion and backtracking')
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

# Code Solutions
code_mapping = [
    ('07-Recursion-and-Backtracking/code/001-factorial-recursion', 'dsa-main/1_factorial.cpp', [], 'Factorial recursive solution'),
    ('07-Recursion-and-Backtracking/code/002-array-recursion', 'dsa-main/7_array_recursive.cpp', ['dsa-main/8_max_ele_inArray_recursive.cpp', 'dsa-main/9_sum_array_ele_usingRecursion.cpp'], 'Recursive array printing, maximum element, and array sum'),
    ('07-Recursion-and-Backtracking/code/003-math-recursion', 'dsa-main/4_recursive_sum_of_Digitts.cpp', ['dsa-main/13_k_Multiple_of_n.cpp', 'dsa-main/14_sum_of_natural_num_with_alternateign.cpp'], 'Recursive sum of digits, k multiples, and alternate sum of natural numbers'),
    ('07-Recursion-and-Backtracking/code/004-frog-jump', 'dsa-main/17_Frog_jump.cpp', [], 'Frog jump classic recursion and path minimization'),
    ('07-Recursion-and-Backtracking/code/005-string-recursion', 'dsa-main/10_remove_Occurence(a).cpp', [], 'Recursive string element removal'),
    ('07-Recursion-and-Backtracking/code/006-backtracking-basics', 'DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/code/backtracking.cpp', ['DSA_server-main/DSA-MasterCourse/04_Recursion_and_Backtracking/code/basics.cpp'], 'Standard backtracking: permutations, subsets, and N-Queens')
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

print(f'Migrated Topic 7: {len(ledger)} actions logged')
