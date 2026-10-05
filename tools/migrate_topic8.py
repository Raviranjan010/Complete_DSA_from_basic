import os
import shutil
import csv

os.makedirs('08-Linked-List/concepts', exist_ok=True)
os.makedirs('08-Linked-List/problems', exist_ok=True)
os.makedirs('08-Linked-List/code', exist_ok=True)

ledger = []

# README
with open('08-Linked-List/README.md', 'w', encoding='utf-8') as f:
    f.write('# 08 — Linked List\n\nPrerequisites: `00-Start-Here` (Pointers), `01-Complexity-Analysis`\n\nDynamic node-based linear data structures: singly, doubly, and circular linked lists, reversals, cycle detection (Floyd’s algorithm), and merge operations.\n')
ledger.append(('08-Linked-List/README.md', 'NA', 'NA', 'Created topic hub README for Linked List'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/06_Linked_List/06_notes.md'
c1_contrib = 'Summer_pep_DSA-main/10-Linked-List.md'
target_c1 = '08-Linked-List/concepts/01-linked-list-fundamentals-and-operations.md'

content = ''
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_b:
        content = f_b.read()
if os.path.exists(c1_contrib):
    with open(c1_contrib, 'r', encoding='utf-8', errors='ignore') as f_c:
        content += '\n\n---\n\n## Supplementary Notes from ' + os.path.basename(c1_contrib) + '\n\n' + f_c.read()

with open(target_c1, 'w', encoding='utf-8') as f_out:
    f_out.write(content)
ledger.append((target_c1, c1_base, c1_contrib, 'Merged linked list structure, pointer linking, traversal, insertion, and reversal'))

# Code
os.makedirs('08-Linked-List/code/001-singly-linked-list', exist_ok=True)
cpp_code = '''// Basic Singly Linked List operations in C++: insertion, traversal, and reversal
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

void printList(ListNode* head) {
    ListNode* curr = head;
    while (curr) {
        cout << curr->val << (curr->next ? " -> " : "");
        curr = curr->next;
    }
    cout << endl;
}

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);

    cout << "Original list: ";
    printList(head);

    head = reverseList(head);
    cout << "Reversed list: ";
    printList(head);

    return 0;
}
'''
with open('08-Linked-List/code/001-singly-linked-list/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(cpp_code)
ledger.append(('08-Linked-List/code/001-singly-linked-list/solution.cpp', 'NA', 'NA', 'Created singly linked list insertion, traversal, and reversal implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 8: {len(ledger)} actions logged')
