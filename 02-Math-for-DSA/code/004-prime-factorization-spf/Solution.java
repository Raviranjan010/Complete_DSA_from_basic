import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static int[] computeSPF(int n) {
        int[] spf = new int[n + 1];
        for (int i = 0; i <= n; i++) spf[i] = i;

        for (int p = 2; p * p <= n; p++) {
            if (spf[p] == p) {
                for (int i = p * p; i <= n; i += p) {
                    if (spf[i] == i) spf[i] = p;
                }
            }
        }
        return spf;
    }

    public static List<Integer> factorize(int x, int[] spf) {
        List<Integer> factors = new ArrayList<>();
        while (x > 1) {
            factors.add(spf[x]);
            x /= spf[x];
        }
        return factors;
    }

    public static void main(String[] args) {
        int[] spf = computeSPF(100);
        System.out.println("Prime factors of 84: " + factorize(84, spf));
    }
}
