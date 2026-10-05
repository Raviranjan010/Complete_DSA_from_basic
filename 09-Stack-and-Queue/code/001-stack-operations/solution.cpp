// Stack implementation using std::vector in C++
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
