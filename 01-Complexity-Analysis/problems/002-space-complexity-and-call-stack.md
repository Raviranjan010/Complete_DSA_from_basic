# Space Complexity & Call Stack Depth: Iterative vs Recursive Memory

[← Back to Module Overview](../README.md) · [Concepts: Asymptotic Analysis & Big-O](../concepts/01-asymptotic-analysis-and-big-o.md)

---

## 1. Problem Overview
- **Name:** Space Complexity & Call Stack Memory Measurement
- **Difficulty:** Easy
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#complexity-analysis`, `#space-complexity`, `#recursion`
- **External Links:** [GeeksforGeeks: Space Complexity in Algorithms](https://www.geeksforgeeks.org/space-complexity-analysis/) · [LeetCode: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

---

## 2. Problem Statement
Implement a demonstration suite contrasting **auxiliary space complexity** across three paradigms calculating the $N$-th Fibonacci number:
1. **$\mathcal{O}(1)$ Auxiliary Space (Iterative Bottom-Up):** Maintains only two scalar accumulators (`prev`, `curr`).
2. **$\mathcal{O}(N)$ Auxiliary Space (Recursive Call Stack):** Recurses down to depth $N$, creating $N$ active stack frames in RAM.
3. **$\mathcal{O}(N)$ Heap Space (Tabulation Vector):** Allocates a dynamically sized vector of size $N + 1$.

Demonstrate how recursive depth creates risk of Stack Overflow (`SIGSEGV` or `StackOverflowError`) when $N \ge 10^5$, whereas the $\mathcal{O}(1)$ iterative approach processes any $N$ safely with zero memory growth.

---

## 3. Visual Representation: Memory Call Stack vs Constant Space
```text
RECURSIVE CALL STACK (Depth N = 4):
Top of Stack -> [ fib(1) ] (Frame 4: return 1)
                [ fib(2) ] (Frame 3: waiting on fib(1))
                [ fib(3) ] (Frame 2: waiting on fib(2))
                [ fib(4) ] (Frame 1: waiting on fib(3))
Bottom       -> [ main() ]
Total Stack Space: O(N) frames

ITERATIVE STATE MACHINE:
Iteration 0: prev = 0, curr = 1
Iteration 1: prev = 1, curr = 1
Iteration 2: prev = 1, curr = 2
Iteration 3: prev = 2, curr = 3
Total Auxiliary Space: O(1) scalars, zero additional stack frames!
```

---

## 4. Multi-Language Implementations

### C++17 Implementation
```cpp
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
```

### Python 3 Implementation
```python
def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

def fib_tabulation(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def main():
    n = 10
    print(f"Fibonacci({n}) = {fib_iterative(n)}")
    print(f"Iterative Auxiliary Space: O(1)")
    print(f"Tabulation Auxiliary Space: O(N) list allocation")

if __name__ == "__main__":
    main()
```

### Java 17 Implementation
```java
public class Solution {
    public static long fibonacciIterative(int n) {
        if (n <= 1) return n;
        long prev = 0, curr = 1;
        for (int i = 2; i <= n; i++) {
            long nextVal = prev + curr;
            prev = curr;
            curr = nextVal;
        }
        return curr;
    }

    public static long fibonacciTabulation(int n) {
        if (n <= 1) return n;
        long[] dp = new long[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println("Fibonacci(" + n + ") = " + fibonacciIterative(n));
        System.out.println("Iterative Auxiliary Space: O(1)");
        System.out.println("Tabulation Auxiliary Space: O(N) array allocation");
    }
}
```

---

## 5. Complexity Breakdown & Interview Takeaways
- **Input Space vs Auxiliary Space:** Input space is the memory needed to store the input arguments. Auxiliary space is the *extra* or temporary space allocated by the algorithm.
- Always count the **compiler call stack** in auxiliary space analysis. A recursive algorithm with no local allocations still uses $\mathcal{O}(\text{recursion depth})$ auxiliary space.
