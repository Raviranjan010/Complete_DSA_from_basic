import os
import shutil
import csv

os.makedirs('09-Stack-and-Queue/concepts', exist_ok=True)
os.makedirs('09-Stack-and-Queue/problems', exist_ok=True)
os.makedirs('09-Stack-and-Queue/code', exist_ok=True)

ledger = []

# README
with open('09-Stack-and-Queue/README.md', 'w', encoding='utf-8') as f:
    f.write('# 09 — Stack and Queue\n\nPrerequisites: `00-Start-Here`, `01-Complexity-Analysis`, `03-Arrays-and-Strings`, `08-Linked-List`\n\nLIFO and FIFO linear abstract data structures: Stack, Queue, Deque, Monotonic Stack (Next Greater Element), and Monotonic Queue.\n')
ledger.append(('09-Stack-and-Queue/README.md', 'NA', 'NA', 'Created topic hub README for Stack and Queue'))

# Concepts
c1_base = 'DSA_server-main/DSA-MasterCourse/07_Stack/07_notes.md'
c1_contrib = 'Summer_pep_DSA-main/11-Stack.md'
target_c1 = '09-Stack-and-Queue/concepts/01-stack-fundamentals-and-monotonic-stack.md'

content1 = ''
if os.path.exists(c1_base):
    with open(c1_base, 'r', encoding='utf-8', errors='ignore') as f_b:
        content1 = f_b.read()
if os.path.exists(c1_contrib):
    with open(c1_contrib, 'r', encoding='utf-8', errors='ignore') as f_c:
        content1 += '\n\n---\n\n## Supplementary Notes from ' + os.path.basename(c1_contrib) + '\n\n' + f_c.read()

with open(target_c1, 'w', encoding='utf-8') as f_out:
    f_out.write(content1)
ledger.append((target_c1, c1_base, c1_contrib, 'Merged stack LIFO theory, push/pop/top, and monotonic stack Next Greater Element pattern'))

c2_base = 'DSA_server-main/DSA-MasterCourse/08_Queue_and_Deque/08_notes.md'
c2_contrib = 'Summer_pep_DSA-main/12-Queue.md'
target_c2 = '09-Stack-and-Queue/concepts/02-queue-deque-and-sliding-window-maximum.md'

content2 = ''
if os.path.exists(c2_base):
    with open(c2_base, 'r', encoding='utf-8', errors='ignore') as f_b:
        content2 = f_b.read()
if os.path.exists(c2_contrib):
    with open(c2_contrib, 'r', encoding='utf-8', errors='ignore') as f_c:
        content2 += '\n\n---\n\n## Supplementary Notes from ' + os.path.basename(c2_contrib) + '\n\n' + f_c.read()

with open(target_c2, 'w', encoding='utf-8') as f_out:
    f_out.write(content2)
ledger.append((target_c2, c2_base, c2_contrib, 'Merged queue FIFO theory, circular queues, deque, and sliding window maximum'))

# Code
os.makedirs('09-Stack-and-Queue/code/001-stack-operations', exist_ok=True)
code1 = '''// Stack implementation using std::vector in C++
#include <iostream>
#include <vector>
using namespace std;

class MyStack {
    vector<int> data;
public:
    void push(int x) { data.push_back(x); }
    void pop() { if (!data.empty()) data.pop_back(); }
    int top() { return data.empty() ? -1 : data.back(); }
    bool empty() { return data.empty(); }
    int size() { return data.size(); }
};

int main() {
    MyStack s;
    s.push(10);
    s.push(20);
    cout << "Top: " << s.top() << endl;
    s.pop();
    cout << "Top after pop: " << s.top() << endl;
    return 0;
}
'''
with open('09-Stack-and-Queue/code/001-stack-operations/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code1)
ledger.append(('09-Stack-and-Queue/code/001-stack-operations/solution.cpp', 'NA', 'NA', 'Created stack data structure implementation'))

os.makedirs('09-Stack-and-Queue/code/002-queue-operations', exist_ok=True)
code2 = '''// Queue implementation using circular array in C++
#include <iostream>
using namespace std;

class MyQueue {
    int* arr;
    int frontIdx, rearIdx, count, capacity;
public:
    MyQueue(int cap = 100) : capacity(cap), frontIdx(0), rearIdx(0), count(0) {
        arr = new int[cap];
    }
    ~MyQueue() { delete[] arr; }
    void push(int x) {
        if (count == capacity) return;
        arr[rearIdx] = x;
        rearIdx = (rearIdx + 1) % capacity;
        count++;
    }
    void pop() {
        if (count == 0) return;
        frontIdx = (frontIdx + 1) % capacity;
        count--;
    }
    int front() { return count == 0 ? -1 : arr[frontIdx]; }
    bool empty() { return count == 0; }
};

int main() {
    MyQueue q(5);
    q.push(1);
    q.push(2);
    q.push(3);
    cout << "Front: " << q.front() << endl;
    q.pop();
    cout << "Front after pop: " << q.front() << endl;
    return 0;
}
'''
with open('09-Stack-and-Queue/code/002-queue-operations/solution.cpp', 'w', encoding='utf-8') as f_code:
    f_code.write(code2)
ledger.append(('09-Stack-and-Queue/code/002-queue-operations/solution.cpp', 'NA', 'NA', 'Created circular queue implementation'))

with open('_meta/MERGE_LEDGER.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in ledger:
        writer.writerow(row)

print(f'Migrated Topic 9: {len(ledger)} actions logged')
