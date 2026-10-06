import time

def constant_access(arr):
    if not arr:
        return 0
    return arr[len(arr) // 2]

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
    # 1. Correctness assertions
    sample = [1, 2, 3, 4, 5]
    assert constant_access(sample) == 3
    assert linear_sum(sample) == 15
    assert quadratic_pairs(sample, 5) == 25

    # 2. Loose growth ratio assertions (never exact timing)
    n_small = 100
    n_large = 400 # 4x increase in N -> 16x quadratic pairs
    data_small = [1] * n_small
    data_large = [1] * n_large

    # Warm-up
    _ = quadratic_pairs(data_small, n_small)

    t0 = time.perf_counter()
    sum_small = linear_sum(data_small)
    t1 = time.perf_counter()
    quad_small = quadratic_pairs(data_small, n_small)
    t2 = time.perf_counter()

    assert sum_small == n_small
    assert quad_small == n_small * n_small

    t3 = time.perf_counter()
    sum_large = linear_sum(data_large)
    t4 = time.perf_counter()
    quad_large = quadratic_pairs(data_large, n_large)
    t5 = time.perf_counter()

    assert sum_large == n_large
    assert quad_large == n_large * n_large

    d_quad_small = t2 - t1
    d_quad_large = t5 - t4

    # Assert non-negative duration and loose growth ratio >= 1.0
    assert d_quad_small >= 0
    assert d_quad_large >= 0
    if d_quad_small > 0:
        ratio = d_quad_large / d_quad_small
        # Loose lower bound ratio: 4x input size should not take less time than small input
        assert ratio >= 1.0

    print("[Python3] Complexity benchmark correctness and loose growth ratios verified.")

if __name__ == "__main__":
    main()
