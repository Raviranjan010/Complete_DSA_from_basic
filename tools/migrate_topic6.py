import os
import shutil
import csv

os.makedirs('06-Hashing/concepts', exist_ok=True)
os.makedirs('06-Hashing/problems', exist_ok=True)
os.makedirs('06-Hashing/code', exist_ok=True)

ledger = []

# README
with open('06-Hashing/README.md', 'w', encoding='utf-8') as f:
    f.write('# 06 — Hashing\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `03-Arrays-and-Strings`\n\nHash tables, hash functions, collision resolution (chaining, open addressing), `unordered_map`, `unordered_set`, and frequency counting patterns.\n')
ledger.append(('06-Hashing/README.md', 'NA', 'NA', 'Created topic hub README for Hashing'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/09_Hashing/09_notes.md'
c1_contrib = 'Summer_pep_DSA-main/07-Hashing.md'
target_c1 = '06-Hashing/concepts/01-hashing-fundamentals-and-collision-handling.md'

content = ''
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_b:
        content = f_b.read()
if os.path.exists(c1_contrib):
    with open(c1_contrib, 'r', encoding='utf-8', errors='ignore') as f_c:
        content += '\n\n---\n\n## Supplementary Notes from ' + os.path.basename(c1_contrib) + '\n\n' + f_c.read()

with open(target_c1, 'w', encoding='utf-8') as f_out:
    f_out.write(content)
ledger.append((target_c1, c1_base, c1_contrib, 'Merged hashing theory, hash functions, collision strategies, and STL maps'))

# Code
os.makedirs('06-Hashing/code/001-hashmap-basics', exist_ok=True)
cpp_code = '''// Demonstration of std::unordered_map and std::unordered_set in C++
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
    vector<int> nums = {4, 2, 2, 8, 3, 3, 1};
    unordered_map<int, int> freq;
    for (int x : nums) {
        freq[x]++;
    }

    cout << "Element frequencies:" << endl;
    for (auto& pair : freq) {
        cout << pair.first << " -> " << pair.second << endl;
    }

    unordered_set<int> unique_elements(nums.begin(), nums.end());
    cout << "Unique count: " << unique_elements.size() << endl;

    return 0;
}
'''
with open('06-Hashing/code/001-hashmap-basics/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(cpp_code)
ledger.append(('06-Hashing/code/001-hashmap-basics/solution.cpp', 'NA', 'NA', 'Created hash map and set foundational solution code'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 6: {len(ledger)} actions logged')
