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
