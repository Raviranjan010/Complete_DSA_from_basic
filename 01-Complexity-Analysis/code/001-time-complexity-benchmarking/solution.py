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
