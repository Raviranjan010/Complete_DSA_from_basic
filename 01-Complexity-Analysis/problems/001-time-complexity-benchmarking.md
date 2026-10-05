# Time Complexity Benchmarking: Comparing $\mathcal{O}(1)$, $\mathcal{O}(N)$, and $\mathcal{O}(N^2)$

[← Back to Module Overview](../README.md) · [Concepts: Asymptotic Analysis & Big-O](../concepts/01-asymptotic-analysis-and-big-o.md)

---

## 1. Problem Overview
- **Name:** Empirical Time Complexity Measurement & Asymptotic Scaling
- **Difficulty:** Easy
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#complexity-analysis`, `#benchmarking`
- **External Links:** [GeeksforGeeks: Analysis of Algorithms](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/) · [LeetCode: Discussion on Time Limits](https://leetcode.com/explore/)

---

## 2. Problem Statement
Implement an empirical performance benchmark that implements three algorithms with distinct time complexity profiles on an array of size $N$:
1. **$\mathcal{O}(1)$ Constant Time:** Accesses the middle element directly via pointer indexing.
2. **$\mathcal{O}(N)$ Linear Time:** Computes the sum of all elements with a single pass loop.
3. **$\mathcal{O}(N^2)$ Quadratic Time:** Counts pairs satisfying a condition via nested loops.

The program measures execution time in microseconds across scaling inputs ($N = 10^2, 10^3, 10^4$) and validates how theoretical Big-O bounds predict real CPU clock behavior.

### Input Specification
An integer $N$ representing the size of a dynamically generated test vector.

### Output Specification
The elapsed time in microseconds for each algorithm class at size $N$, proving that doubling $N$ quadruples $\mathcal{O}(N^2)$ runtime while only doubling $\mathcal{O}(N)$ runtime.

---

## 3. Visual Representation: Complexity Growth Curves
```text
Operations / Clock Cycles
  ^
  |                                        * O(N^2) Quadratic
  |                                     *
  |                                  *
  |                               *
  |                            *
  |                        *
  |                     *
  |                  *  
  |             *       ------------------ O(N) Linear
  |        *     
  |   *          
  |*-------------------------------------- O(1) Constant
  +----------------------------------------------------> Input Size (N)
```

---

## 4. Multi-Language Implementations

### C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <numeric>

// O(1) Constant Time
int constantTimeAccess(const std::vector<int>& arr) {
    if (arr.empty()) return 0;
    return arr[arr.size() / 2];
}

// O(N) Linear Time
long long linearTimeSum(const std::vector<int>& arr) {
    long long total = 0;
    for (int x : arr) {
        total += x;
    }
    return total;
}

// O(N^2) Quadratic Time
long long quadraticTimePairs(const std::vector<int>& arr, int limit) {
    long long count = 0;
    int n = std::min(static_cast<int>(arr.size()), limit);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    std::vector<int> testSizes = {500, 1000, 2000};

    for (int n : testSizes) {
        std::vector<int> data(n, 1);

        auto t1 = std::chrono::high_resolution_clock::now();
        volatile int val = constantTimeAccess(data);
        auto t2 = std::chrono::high_resolution_clock::now();

        auto t3 = std::chrono::high_resolution_clock::now();
        volatile long long sum = linearTimeSum(data);
        auto t4 = std::chrono::high_resolution_clock::now();

        auto t5 = std::chrono::high_resolution_clock::now();
        volatile long long pairs = quadraticTimePairs(data, n);
        auto t6 = std::chrono::high_resolution_clock::now();

        auto d_const = std::chrono::duration_cast<std::chrono::nanoseconds>(t2 - t1).count();
        auto d_lin = std::chrono::duration_cast<std::chrono::microseconds>(t4 - t3).count();
        auto d_quad = std::chrono::duration_cast<std::chrono::microseconds>(t6 - t5).count();

        std::cout << "N = " << n 
                  << " | O(1): " << d_const << " ns"
                  << " | O(N): " << d_lin << " us"
                  << " | O(N^2): " << d_quad << " us\n";
    }
    return 0;
}
```

### Python 3 Implementation
```python
import time

def constant_access(arr):
    return arr[len(arr) // 2] if arr else 0

def linear_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def quadratic_pairs(arr, limit):
    count = 0
    n = min(len(arr), limit)
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
    return count

def main():
    sizes = [500, 1000, 2000]
    for n in sizes:
        data = [1] * n

        t0 = time.perf_counter()
        _ = constant_access(data)
        t_const = (time.perf_counter() - t0) * 1e9

        t0 = time.perf_counter()
        _ = linear_sum(data)
        t_lin = (time.perf_counter() - t0) * 1e6

        t0 = time.perf_counter()
        _ = quadratic_pairs(data, n)
        t_quad = (time.perf_counter() - t0) * 1e6

        print(f"N = {n} | O(1): {t_const:.1f} ns | O(N): {t_lin:.1f} us | O(N^2): {t_quad:.1f} us")

if __name__ == "__main__":
    main()
```

### Java 17 Implementation
```java
import java.util.Arrays;

public class Solution {
    public static int constantAccess(int[] arr) {
        if (arr.length == 0) return 0;
        return arr[arr.length / 2];
    }

    public static long linearSum(int[] arr) {
        long total = 0;
        for (int x : arr) total += x;
        return total;
    }

    public static long quadraticPairs(int[] arr, int limit) {
        long count = 0;
        int n = Math.min(arr.length, limit);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i] == arr[j]) count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] sizes = {500, 1000, 2000};
        for (int n : sizes) {
            int[] data = new int[n];
            Arrays.fill(data, 1);

            long t1 = System.nanoTime();
            int cVal = constantAccess(data);
            long t2 = System.nanoTime();

            long t3 = System.nanoTime();
            long lVal = linearSum(data);
            long t4 = System.nanoTime();

            long t5 = System.nanoTime();
            long qVal = quadraticPairs(data, n);
            long t6 = System.nanoTime();

            System.out.printf("N = %d | O(1): %d ns | O(N): %d us | O(N^2): %d us%n",
                n, (t2 - t1), (t4 - t3) / 1000, (t6 - t5) / 1000);
        }
    }
}
```

---

## 5. Complexity Breakdown
- **Rule of Thumb for Interviews:**
  - Modern CPU handles approximately $\sim 10^8$ basic operations per second.
  - If $N \le 10^5$, an $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ solution will comfortably pass within 1.0 second.
  - If $N \le 10^4$, an $\mathcal{O}(N^2)$ solution might barely pass or risk TLE.
  - If $N \ge 10^6$, anything worse than $\mathcal{O}(N)$ or $\mathcal{O}(N \log N)$ will trigger `Time Limit Exceeded` (`TLE`).
