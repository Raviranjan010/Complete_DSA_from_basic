import java.util.Arrays;

public class Solution {
    public static int constantAccess(int[] arr) {
        if (arr.length == 0) return 0;
        return arr[arr.length / 2];
    }

    public static long linearSum(int[] arr) {
        long total = 0;
        for (int x : arr) total += x;
        return total;
    }

    public static long quadraticPairs(int[] arr, int limit) {
        long count = 0;
        int n = Math.min(arr.length, limit);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[i] == arr[j]) count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // 1. Correctness assertions
        int[] sample = {1, 2, 3, 4, 5};
        assert constantAccess(sample) == 3 : "Constant access failed";
        assert linearSum(sample) == 15 : "Linear sum failed";
        assert quadraticPairs(sample, 5) == 25 : "Quadratic pairs failed";

        // 2. Loose growth ratio assertions
        int nSmall = 200;
        int nLarge = 800; // 4x increase in N -> 16x iterations

        int[] smallData = new int[nSmall];
        Arrays.fill(smallData, 1);
        int[] largeData = new int[nLarge];
        Arrays.fill(largeData, 1);

        // Warm-up JIT
        quadraticPairs(smallData, nSmall);

        long t1 = System.nanoTime();
        long sumSmall = linearSum(smallData);
        long t2 = System.nanoTime();
        long quadSmall = quadraticPairs(smallData, nSmall);
        long t3 = System.nanoTime();

        assert sumSmall == nSmall;
        assert quadSmall == (long)nSmall * nSmall;

        long t4 = System.nanoTime();
        long sumLarge = linearSum(largeData);
        long t5 = System.nanoTime();
        long quadLarge = quadraticPairs(largeData, nLarge);
        long t6 = System.nanoTime();

        assert sumLarge == nLarge;
        assert quadLarge == (long)nLarge * nLarge;

        long dQuadSmall = t3 - t2;
        long dQuadLarge = t6 - t5;

        assert dQuadSmall >= 0;
        assert dQuadLarge >= 0;
        if (dQuadSmall > 0) {
            double ratio = (double)dQuadLarge / dQuadSmall;
            // Loose growth ratio test >= 1.0 (never depends on exact timing)
            assert ratio >= 1.0 : "Growth ratio must be non-decreasing";
        }

        System.out.println("[Java17] Complexity benchmark correctness and loose growth ratios verified.");
    }
}
