// Climbing Stairs / Fibonacci using Memoization and Tabulation in C++
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
