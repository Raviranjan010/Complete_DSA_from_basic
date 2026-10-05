import os
import shutil
import csv

os.makedirs('15-Bit-Manipulation/concepts', exist_ok=True)
os.makedirs('15-Bit-Manipulation/problems', exist_ok=True)
os.makedirs('15-Bit-Manipulation/code', exist_ok=True)

ledger = []

# README
with open('15-Bit-Manipulation/README.md', 'w', encoding='utf-8') as f:
    f.write('# 15 — Bit Manipulation\n\nPrerequisites: `00-Start-Here` (Binary Numbers), `01-Complexity-Analysis`\n\nBitwise operators (&, |, ^, ~, <<, >>), setting/clearing/toggling bits, Brian Kernighan’s algorithm, XOR properties, power of two, and subset generation.\n')
ledger.append(('15-Bit-Manipulation/README.md', 'NA', 'NA', 'Created topic hub README for Bit Manipulation'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/18_Bit_Manipulation/18_notes.md'
target_c1 = '15-Bit-Manipulation/concepts/01-bitwise-operators-and-binary-tricks.md'
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c1, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c1, c1_base, 'NA', 'Preserved bitwise operations, bitmasking, and single number patterns'))

# Code
os.makedirs('15-Bit-Manipulation/code/001-bitwise-tricks', exist_ok=True)
code1 = '''// Essential Bit Manipulation tricks in C++
#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        n = n & (n - 1); // Clears the lowest set bit
        count++;
    }
    return count;
}

int main() {
    int x = 16;
    cout << x << " is power of two: " << (isPowerOfTwo(x) ? "Yes" : "No") << endl;

    int y = 29; // Binary: 11101
    cout << "Set bits in " << y << ": " << countSetBits(y) << endl;

    return 0;
}
'''
with open('15-Bit-Manipulation/code/001-bitwise-tricks/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('15-Bit-Manipulation/code/001-bitwise-tricks/solution.cpp', 'NA', 'NA', 'Created bitwise tricks and count set bits implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 15: {len(ledger)} actions logged')
