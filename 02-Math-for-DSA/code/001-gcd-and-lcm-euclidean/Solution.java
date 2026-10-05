public class Solution {
    public static long computeGcd(long a, long b) {
        while (b != 0) {
            long rem = a % b;
            a = b;
            b = rem;
        }
        return a;
    }

    public static long computeLcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        return (a / computeGcd(a, b)) * b;
    }

    public static void main(String[] args) {
        long a = 48, b = 18;
        System.out.println("GCD(" + a + ", " + b + ") = " + computeGcd(a, b));
        System.out.println("LCM(" + a + ", " + b + ") = " + computeLcm(a, b));
    }
}
