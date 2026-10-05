import os
import shutil
import csv

os.makedirs('03-Arrays-and-Strings/concepts', exist_ok=True)
os.makedirs('03-Arrays-and-Strings/problems', exist_ok=True)
os.makedirs('03-Arrays-and-Strings/code', exist_ok=True)

ledger = []

# README
with open('03-Arrays-and-Strings/README.md', 'w', encoding='utf-8') as f:
    f.write('# 03 — Arrays and Strings\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`\n\nFoundational linear data structures: memory layout, in-place manipulation, Kadane, 2D arrays, and string operations.\n')
ledger.append(('03-Arrays-and-Strings/README.md', '02-arrays-and-strings/README.md', 'NA', 'Maintained topic hub README for Arrays and Strings'))

# Concepts
concepts = [
    ('03-Arrays-and-Strings/concepts/01-array-master-notes.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/ARRAY_MASTER_NOTES.md', ['Summer_pep_DSA-main/02-Arrays-Basics.md'], 'Comprehensive master notes on array operations and memory layout'),
    ('03-Arrays-and-Strings/concepts/02-subarrays-and-kadane-algorithm.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Notes.md', ['DSA_final-main/02_Arrays/05_Subarrays_and_Kadanes_Algorithm.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Patterns.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Mistakes.md'], 'Kadane algorithm and subarray generation theory'),
    ('03-Arrays-and-Strings/concepts/03-strings-fundamentals-and-manipulation.md', 'DSA_server-main/DSA-MasterCourse/03_Strings/03_notes.md', ['Summer_pep_DSA-main/05-Strings.md'], 'String immutability, manipulation, and pattern foundation'),
    ('03-Arrays-and-Strings/concepts/04-pattern-recognition-guide.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/08_Pattern_Recognition/Complete_Guide.md', [], 'Striver array pattern recognition guide'),
    ('03-Arrays-and-Strings/concepts/05-common-mistakes-and-pitfalls.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/09_Common_Mistakes/Complete_Guide.md', [], 'Common student pitfalls and edge cases in array processing'),
    ('03-Arrays-and-Strings/concepts/06-arrays-and-strings-mcqs.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/10_MCQs/Arrays_MCQs.md', ['DSA_server-main/DSA-MasterCourse/03_Strings/03_mcqs.md'], 'Array and string self-assessment MCQs')
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

# Canonical Problem Writeups
problems = [
    ('03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md', 'DSA_ac-main/Array/03_DSA_Pair_Sum_Majority_Element_Brute_Better_Optimal.md', 'Two Sum / Pair Sum Brute-Better-Optimal analysis'),
    ('03-Arrays-and-Strings/problems/002-majority-element.md', 'DSA_ac-main/Array/03_DSA_Pair_Sum_Majority_Element_Brute_Better_Optimal.md', 'Majority Element (Boyer-Moore Voting) analysis'),
    ('03-Arrays-and-Strings/problems/003-product-of-array-except-self.md', 'DSA_ac-main/Array/06_DSA_Product_of_Array_Except_Self_LeetCode_238.md', 'Product of Array Except Self without division analysis'),
    ('03-Arrays-and-Strings/problems/004-maximum-subarray-kadane.md', 'DSA_server-main/DSA-MasterCourse/02_Arrays/04_Kadane/Problems/Medium_Hard.md', 'Maximum Subarray Sum Kadane problem analysis')
]

for target, base, desc in problems:
    if os.path.exists(base):
        with open(base, 'r', encoding='utf-8', errors='ignore') as f_in:
            with open(target, 'w', encoding='utf-8') as f_out:
                f_out.write(f_in.read())
        ledger.append((target, base, 'None', desc))

# Code Solutions
code_mapping = [
    ('03-Arrays-and-Strings/code/001-two-sum', 'dsa-main/target_sum.cpp', ['dsa-main/target_sum2.cpp'], 'Two Sum / Target Sum implementations'),
    ('03-Arrays-and-Strings/code/002-check-sorted', 'dsa-main/check_sorted_or_not.cpp', [], 'Check if array is sorted implementation'),
    ('03-Arrays-and-Strings/code/003-reverse-and-palindrome', 'dsa-main/reverse_arr.cpp', ['dsa-main/11_Palindrome.cpp'], 'Array reverse and string palindrome check'),
    ('03-Arrays-and-Strings/code/004-element-frequency', 'dsa-main/frequency_query.cpp', ['dsa-main/Count_occurence.cpp'], 'Element frequency queries in array'),
    ('03-Arrays-and-Strings/code/005-extreme-elements', 'dsa-main/largest.cpp', ['dsa-main/second_largest.cpp'], 'Largest and second largest element finding'),
    ('03-Arrays-and-Strings/code/006-array-reordering', 'dsa-main/even_int_move.cpp', ['dsa-main/even_int_move2.cpp', 'dsa-main/even-odd.cpp', 'dsa-main/5_sort_zero_One.cpp'], 'Parity movement and 0/1 array sorting'),
    ('03-Arrays-and-Strings/code/007-matrix-operations', 'dsa-main/matrix_Transpose.cpp', ['dsa-main/11_Matrix_muktiplication.cpp'], '2D Matrix transpose and matrix multiplication'),
    ('03-Arrays-and-Strings/code/008-array-manipulation', 'dsa-main/arr_manipulation.cpp', ['dsa-main/arr_manipulation1.cpp', 'dsa-main/delete_add.cpp', 'dsa-main/adding_removing.cpp', 'dsa-main/printing_elements.cpp', 'dsa-main/12_printing_numbers.cpp'], 'Array element addition, deletion, and rotation'),
    ('03-Arrays-and-Strings/code/009-strings-basics', 'DSA_server-main/DSA-MasterCourse/03_Strings/code/basics.cpp', ['DSA_server-main/DSA-MasterCourse/03_Strings/code/string_manipulation.cpp'], 'Basic string manipulation and traversal in C++')
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

print(f'Migrated Topic 3: {len(ledger)} actions logged')
