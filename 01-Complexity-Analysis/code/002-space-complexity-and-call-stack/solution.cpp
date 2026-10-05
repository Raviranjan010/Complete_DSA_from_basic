#include <iostream>
#include <vector>

// 1. O(1) Auxiliary Space: Iterative State Machine
long long fibonacciIterative(int n) {
    if (n <= 1) return n;
    long long prev = 0, curr = 1;
    for (int i = 2; i <= n; ++i) {
        long long nextVal = prev + curr;
        prev = curr;
        curr = nextVal;
    }
    return curr;
}

// 2. O(N) Auxiliary Space: Recursive Call Stack
long long fibonacciRecursiveDepth(int n, int currentDepth, int& maxDepth) {
    if (currentDepth > maxDepth) maxDepth = currentDepth;
    if (n <= 1) return n;
    return fibonacciRecursiveDepth(n - 1, currentDepth + 1, maxDepth) +
           fibonacciRecursiveDepth(n - 2, currentDepth + 1, maxDepth);
}

// 3. O(N) Auxiliary Heap Space: Dynamic Tabulation
long long fibonacciTabulation(int n) {
    if (n <= 1) return n;
    std::vector<long long> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

int main() {
    int n = 10;
    int maxDepth = 0;

    long long resIter = fibonacciIterative(n);
    long long resTab = fibonacciTabulation(n);
    long long resRec = fibonacciRecursiveDepth(n, 1, maxDepth);

    std::cout << "Fibonacci(" << n << ") = " << resIter << "\n";
    std::cout << "Iterative Space: O(1) scalar variables\n";
    std::cout << "Tabulation Space: O(N) vector elements on heap\n";
    std::cout << "Recursive Call Stack Max Depth: " << maxDepth << " frames (O(N) stack memory)\n";

    return 0;
}
