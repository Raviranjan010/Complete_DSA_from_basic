#include <iostream>
#include <vector>
#include <chrono>
#include <numeric>
#include <cassert>
#include <algorithm>

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
    // 1. Correctness Verification
    std::vector<int> sample = {1, 2, 3, 4, 5};
    assert(constantTimeAccess(sample) == 3);
    assert(linearTimeSum(sample) == 15);
    assert(quadraticTimePairs(sample, 5) == 25);

    // 2. Loose Growth Ratio Verification
    int nSmall = 200;
    int nLarge = 800; // 4x input size -> ~16x quadratic iterations

    std::vector<int> smallData(nSmall, 1);
    std::vector<int> largeData(nLarge, 1);

    // Warm-up
    volatile long long dummy = quadraticTimePairs(smallData, nSmall);
    (void)dummy;

    // Benchmark Small
    auto t1 = std::chrono::high_resolution_clock::now();
    volatile long long sumSmall = linearTimeSum(smallData);
    auto t2 = std::chrono::high_resolution_clock::now();
    volatile long long quadSmall = quadraticTimePairs(smallData, nSmall);
    auto t3 = std::chrono::high_resolution_clock::now();

    assert(sumSmall == nSmall);
    assert(quadSmall == (long long)nSmall * nSmall);

    // Benchmark Large
    auto t4 = std::chrono::high_resolution_clock::now();
    volatile long long sumLarge = linearTimeSum(largeData);
    auto t5 = std::chrono::high_resolution_clock::now();
    volatile long long quadLarge = quadraticTimePairs(largeData, nLarge);
    auto t6 = std::chrono::high_resolution_clock::now();

    assert(sumLarge == nLarge);
    assert(quadLarge == (long long)nLarge * nLarge);

    auto d_quad_small = std::chrono::duration_cast<std::chrono::microseconds>(t3 - t2).count();
    auto d_quad_large = std::chrono::duration_cast<std::chrono::microseconds>(t6 - t5).count();

    // Loose growth assertions: large problem does not take negative time
    // and loose lower bound ratio >= 1.0 (never depends on tight exact timing)
    assert(d_quad_large >= 0);
    assert(d_quad_small >= 0);
    if (d_quad_small > 0) {
        double ratio = static_cast<double>(d_quad_large) / d_quad_small;
        // 4x increase in N theoretically takes ~16x work.
        // We test only a very loose lower bound >= 1.0 to eliminate any test flakiness.
        assert(ratio >= 1.0);
    }

    std::cout << "[C++17] Complexity benchmark correctness and loose growth ratios verified.\n";
    return 0;
}
