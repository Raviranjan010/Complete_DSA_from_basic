import os
import shutil
import csv

os.makedirs('12-Greedy-and-Intervals/concepts', exist_ok=True)
os.makedirs('12-Greedy-and-Intervals/problems', exist_ok=True)
os.makedirs('12-Greedy-and-Intervals/code', exist_ok=True)

ledger = []

# README
with open('12-Greedy-and-Intervals/README.md', 'w', encoding='utf-8') as f:
    f.write('# 12 — Greedy and Intervals\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `04-Searching-and-Sorting`\n\nGreedy choice property, optimal substructure, exchange argument proofs, fractional knapsack, activity selection, and interval merging.\n')
ledger.append(('12-Greedy-and-Intervals/README.md', 'NA', 'NA', 'Created topic hub README for Greedy and Intervals'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/16_Greedy_Algorithms/16_notes.md'
target_c1 = '12-Greedy-and-Intervals/concepts/01-greedy-choice-property-and-proofs.md'
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(target_c1, 'w', encoding='utf-8') as f_out:
            f_out.write(f_in.read())
    ledger.append((target_c1, c1_base, 'NA', 'Preserved greedy choice property, exchange argument proof strategy, and problems'))

# Code
os.makedirs('12-Greedy-and-Intervals/code/001-activity-selection', exist_ok=True)
code1 = '''// Activity selection / Non-overlapping intervals in C++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Activity {
    int start, finish;
};

bool compareActivities(const Activity& a, const Activity& b) {
    return a.finish < b.finish;
}

int maxActivities(vector<Activity>& activities) {
    if (activities.empty()) return 0;
    sort(activities.begin(), activities.end(), compareActivities);

    int count = 1;
    int lastFinish = activities[0].finish;

    for (size_t i = 1; i < activities.size(); i++) {
        if (activities[i].start >= lastFinish) {
            count++;
            lastFinish = activities[i].finish;
        }
    }
    return count;
}

int main() {
    vector<Activity> acts = {{1, 2}, {3, 4}, {0, 6}, {5, 7}, {8, 9}, {5, 9}};
    cout << "Maximum non-conflicting activities: " << maxActivities(acts) << endl;
    return 0;
}
'''
with open('12-Greedy-and-Intervals/code/001-activity-selection/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('12-Greedy-and-Intervals/code/001-activity-selection/solution.cpp', 'NA', 'NA', 'Created activity selection greedy implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 12: {len(ledger)} actions logged')
