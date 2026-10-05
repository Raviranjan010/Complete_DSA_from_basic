public class Solution {
    public static boolean isArmstrong(long n) {
        if (n < 0) return false;
        long temp = n;
        int k = 0;
        while (temp > 0) {
            k++;
            temp /= 10;
        }
        long sum = 0;
        temp = n;
        while (temp > 0) {
            long d = temp % 10;
            sum += Math.pow(d, k);
            temp /= 10;
        }
        return sum == n;
    }

    public static boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int rev = 0;
        while (x > rev) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return x == rev || x == rev / 10;
    }

    public static void main(String[] args) {
        System.out.println("153 is Armstrong? " + isArmstrong(153));
        System.out.println("1221 is Palindrome? " + isPalindrome(1221));
    }
}
