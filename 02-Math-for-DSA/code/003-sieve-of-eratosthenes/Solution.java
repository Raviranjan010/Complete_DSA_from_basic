import java.util.Arrays;

public class Solution {
    public static boolean[] sieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        if (n >= 0) isPrime[0] = false;
        if (n >= 1) isPrime[1] = false;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        return isPrime;
    }

    public static void main(String[] args) {
        int limit = 30;
        boolean[] primes = sieve(limit);
        System.out.print("Primes up to " + limit + ": ");
        for (int i = 2; i <= limit; i++) {
            if (primes[i]) System.out.print(i + " ");
        }
        System.out.println();
    }
}
