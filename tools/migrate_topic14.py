import os
import shutil
import csv

os.makedirs('14-Dynamic-Programming/concepts', exist_ok=True)
os.makedirs('14-Dynamic-Programming/problems', exist_ok=True)
os.makedirs('14-Dynamic-Programming/code', exist_ok=True)

ledger = []

# README
with open('14-Dynamic-Programming/README.md', 'w', encoding='utf-8') as f:
    f.write('# 14 — Dynamic Programming\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `03-Arrays-and-Strings`, `07-Recursion-and-Backtracking`\n\nOptimal substructure, overlapping subproblems, top-down memoization, bottom-up tabulation, space optimization, 1D/2D DP, Knapsack, LCS, and LIS.\n')
ledger.append(('14-Dynamic-Programming/README.md', 'NA', 'NA', 'Created topic hub README for Dynamic Programming'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/15_Dynamic_Programming/15_notes.md'
target_c1 = '14-Dynamic-Programming/concepts/01-dp-fundamentals-memoization-tabulation.md'
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c1, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c1, c1_base, 'NA', 'Preserved DP fundamentals, 1D/2D patterns, knapsack, and LCS/LIS frameworks'))

c2_base = 'DSA_server-main/DSA-MasterCourse/21_Advanced_DP/21_notes.md'
target_c2 = '14-Dynamic-Programming/concepts/02-advanced-dp-and-optimizations.md'
if os.path.exists(c2_base):
    with open(c2_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c2, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c2, c2_base, 'NA', 'Preserved advanced DP notes (bitmask DP, tree DP, and digit DP)'))

# Code
os.makedirs('14-Dynamic-Programming/code/001-climbing-stairs-fibonacci', exist_ok=True)
code1 = '''// Climbing Stairs / Fibonacci using Memoization and Tabulation in C++
#include <iostream>
#include <vector>
using namespace std;

// Tabulation with O(1) space
int climbStairs(int n) {
    if (n <= 2) return n;
    int prev2 = 1, prev1 = 2;
    for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

int main() {
    int n = 5;
    cout << "Ways to climb " << n << " stairs: " << climbStairs(n) << endl;
    return 0;
}
'''
with open('14-Dynamic-Programming/code/001-climbing-stairs-fibonacci/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('14-Dynamic-Programming/code/001-climbing-stairs-fibonacci/solution.cpp', 'NA', 'NA', 'Created climbing stairs 1D DP solution'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 14: {len(ledger)} actions logged')
