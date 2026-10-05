public class Solution {
    static final long MOD = 1000000007L;

    public static long power(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public static long modInverse(long n) {
        return power(n, MOD - 2);
    }

    public static long modDivide(long a, long b) {
        return (a % MOD * modInverse(b)) % MOD;
    }

    public static void main(String[] args) {
        System.out.println("14 / 2 mod 1e9+7 = " + modDivide(14, 2));
    }
}
