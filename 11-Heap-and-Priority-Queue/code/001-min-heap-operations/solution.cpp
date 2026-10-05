// Min-Heap implementation and C++ std::priority_queue demonstration
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
