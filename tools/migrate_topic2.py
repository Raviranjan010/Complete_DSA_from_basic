import os
import shutil
import csv

os.makedirs('02-Math-for-DSA/concepts', exist_ok=True)
os.makedirs('02-Math-for-DSA/problems', exist_ok=True)
os.makedirs('02-Math-for-DSA/code', exist_ok=True)

ledger = []

# README
with open('02-Math-for-DSA/README.md', 'w', encoding='utf-8') as f:
    f.write('# 02 — Math for DSA\n\nPrerequisites: `00-Start-Here`\n\nCore number theory, modular arithmetic, GCD, prime testing, and exponentiation.\n')
ledger.append(('02-Math-for-DSA/README.md', 'NA', 'NA', 'Created topic hub README for Math for DSA'))

# Concepts
c1 = '''# Greatest Common Divisor (GCD) & Euclidean Algorithm

## 1. Motivation
Finding the greatest common divisor of two integers is essential in simplifying fractions, modular arithmetic, and geometric algorithms.

## 2. Intuition
Euclid discovered that the GCD of two numbers also divides their difference:
$$\\gcd(a, b) = \\gcd(b, a \\pmod b)$$
Base case: $\\gcd(a, 0) = a$.

## 3. Complexity
- Time Complexity: $O(\\log(\\min(a, b)))$ (Lame's Theorem)
- Space Complexity: $O(\\log(\\min(a, b)))$ recursive call stack
'''
with open('02-Math-for-DSA/concepts/01-gcd-and-euclidean-algorithm.md', 'w', encoding='utf-8') as f:
    f.write(c1)
ledger.append(('02-Math-for-DSA/concepts/01-gcd-and-euclidean-algorithm.md', 'dsa-main/15_GCD_recursion.cpp', 'NA', 'Created GCD & Euclidean algorithm theory from implementation notes'))

# Binary Exponentiation
base_pow = 'DSA_ac-main/Array/04_DSA_Binary_Exponentiation_and_Stock_Problem_Notes.md'
if os.path.exists(base_pow):
    with open(base_pow, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open('02-Math-for-DSA/concepts/02-fast-exponentiation-and-powers.md', 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append(('02-Math-for-DSA/concepts/02-fast-exponentiation-and-powers.md', base_pow, 'NA', 'Preserved binary exponentiation theory notes'))

# Armstrong
c3 = '''# Armstrong Number & Digit Mathematics

An Armstrong number (or narcissistic number) for a given number of digits is an integer such that the sum of its digits raised to the power of the number of digits equals the number itself.

Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
'''
with open('02-Math-for-DSA/concepts/03-armstrong-and-digit-math.md', 'w', encoding='utf-8') as f:
    f.write(c3)
ledger.append(('02-Math-for-DSA/concepts/03-armstrong-and-digit-math.md', 'dsa-main/16_Armstrong_Number_check.cpp', 'NA', 'Created Armstrong number theory notes'))

# Code
code_map = [
    ('02-Math-for-DSA/code/001-gcd-euclidean', 'dsa-main/15_GCD_recursion.cpp', 'Recursive Euclidean GCD implementation'),
    ('02-Math-for-DSA/code/002-armstrong-number', 'dsa-main/16_Armstrong_Number_check.cpp', 'Armstrong number check implementation'),
    ('02-Math-for-DSA/code/003-binary-exponentiation', 'dsa-main/5_p_to_the_power_q_UsingRecursion.cpp', 'Fast recursive power / exponentiation')
]

for cdir, src, desc in code_map:
    os.makedirs(cdir, exist_ok=True)
    if os.path.exists(src):
        shutil.copy(src, f'{cdir}/solution.cpp')
        ledger.append((f'{cdir}/solution.cpp', src, 'NA', desc))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 2: {len(ledger)} actions logged')
