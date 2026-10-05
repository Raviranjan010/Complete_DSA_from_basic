import os
import shutil
import csv

os.makedirs('11-Heap-and-Priority-Queue/concepts', exist_ok=True)
os.makedirs('11-Heap-and-Priority-Queue/problems', exist_ok=True)
os.makedirs('11-Heap-and-Priority-Queue/code', exist_ok=True)

ledger = []

# README
with open('11-Heap-and-Priority-Queue/README.md', 'w', encoding='utf-8') as f:
    f.write('# 11 — Heap and Priority Queue\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `03-Arrays-and-Strings`, `10-Trees`\n\nComplete binary trees array representation, Min/Max Heap, Heapify in O(n), priority queue operations, and Top-K elements pattern.\n')
ledger.append(('11-Heap-and-Priority-Queue/README.md', 'NA', 'NA', 'Created topic hub README for Heap and Priority Queue'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/12_Heaps_and_Priority_Queue/12_notes.md'
target_c1 = '11-Heap-and-Priority-Queue/concepts/01-heaps-and-priority-queues-theory.md'
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c1, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c1, c1_base, 'NA', 'Preserved binary heap properties, array indexing, and priority queue complexity'))

# Code
os.makedirs('11-Heap-and-Priority-Queue/code/001-min-heap-operations', exist_ok=True)
code1 = '''// Min-Heap implementation and C++ std::priority_queue demonstration
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // Max heap by default
    priority_queue<int> max_pq;
    max_pq.push(10);
    max_pq.push(30);
    max_pq.push(20);
    cout << "Max Heap Top: " << max_pq.top() << endl;

    // Min heap using std::greater
    priority_queue<int, vector<int>, greater<int>> min_pq;
    min_pq.push(10);
    min_pq.push(30);
    min_pq.push(20);
    cout << "Min Heap Top: " << min_pq.top() << endl;

    return 0;
}
'''
with open('11-Heap-and-Priority-Queue/code/001-min-heap-operations/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('11-Heap-and-Priority-Queue/code/001-min-heap-operations/solution.cpp', 'NA', 'NA', 'Created Min-Heap and priority queue implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 11: {len(ledger)} actions logged')
