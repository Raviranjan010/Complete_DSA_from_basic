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
