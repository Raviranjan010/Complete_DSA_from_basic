public class Solution {
    public static long power(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    public static void main(String[] args) {
        long mod = 1000000007L;
        System.out.println("2^10 mod 1e9+7 = " + power(2, 10, mod));
    }
}
