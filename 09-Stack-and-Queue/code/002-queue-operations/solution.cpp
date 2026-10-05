// Queue implementation using circular array in C++
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
