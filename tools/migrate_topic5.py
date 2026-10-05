import os
import shutil
import csv

os.makedirs('05-Two-Pointers-and-Sliding-Window/concepts', exist_ok=True)
os.makedirs('05-Two-Pointers-and-Sliding-Window/problems', exist_ok=True)
os.makedirs('05-Two-Pointers-and-Sliding-Window/code', exist_ok=True)

ledger = []

# README
with open('05-Two-Pointers-and-Sliding-Window/README.md', 'w', encoding='utf-8') as f:
    f.write('# 05 — Two Pointers and Sliding Window\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `03-Arrays-and-Strings`\n\nAdvanced linear array techniques: opposite ends, fast & slow pointers, fixed/variable sliding windows, and prefix sums.\n')
ledger.append(('05-Two-Pointers-and-Sliding-Window/README.md', 'NA', 'NA', 'Created topic hub README for Two Pointers and Sliding Window'))

# Concepts
concepts = [
    ('05-Two-Pointers-and-Sliding-Window/concepts/01-two-pointers-technique-guide.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Notes.md', ['Summer_pep_DSA-main/03-Two-Pointers.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Patterns.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Mistakes.md'], 'Consolidated Two Pointer theory, patterns, and common student mistakes'),
    ('05-Two-Pointers-and-Sliding-Window/concepts/02-sliding-window-fixed-and-variable.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Notes.md', ['Summer_pep_DSA-main/09-Sliding-Window.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Patterns.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Mistakes.md'], 'Fixed vs variable size sliding window patterns and templates'),
    ('05-Two-Pointers-and-Sliding-Window/concepts/03-prefix-sum-and-difference-array.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Notes.md', ['Summer_pep_DSA-main/08-Prefix-Sum.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Patterns.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Mistakes.md'], 'Prefix sum queries, range updates, and subarray sum equals K')
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
    ('05-Two-Pointers-and-Sliding-Window/problems/001-container-with-most-water.md', 'DSA_ac-main/Array/05_DSA_Container_With_Most_Water_Notes.md', 'Container With Most Water two-pointer derivation'),
    ('05-Two-Pointers-and-Sliding-Window/problems/002-two-pointers-easy-medium-hard.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/01_Two_Pointer/Problems/Medium.md', 'Curated Two Pointer problem sets across all difficulty levels'),
    ('05-Two-Pointers-and-Sliding-Window/problems/003-sliding-window-problems.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/02_Sliding_Window/Problems/Medium.md', 'Curated Sliding Window problem sets (min window substring, longest unique substr)'),
    ('05-Two-Pointers-and-Sliding-Window/problems/004-prefix-sum-problems.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/03_Prefix_Sum/Problems/Easy_Medium.md', 'Curated Prefix Sum problem solutions')
]

for target, base, desc in problems:
    if os.path.exists(base):
        with open(base, 'r', encoding='utf-8', errors='ignore') as f_in:
            with open(target, 'w', encoding='utf-8') as f_out:
                f_out.write(f_in.read())
        ledger.append((target, base, 'None', desc))

# Code Solutions
code_mapping = [
    ('05-Two-Pointers-and-Sliding-Window/code/001-prefix-sum-queries', 'dsa-main/8_prefix_sum.cpp', ['dsa-main/9_check_prefix_sum.cpp', 'dsa-main/10sum_interval.cpp'], 'Prefix sum array construction, interval sum query, and prefix sum partition check')
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

print(f'Migrated Topic 5: {len(ledger)} actions logged')
