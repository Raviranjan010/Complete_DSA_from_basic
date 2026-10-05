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
