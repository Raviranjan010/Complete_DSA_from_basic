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
        int[] sizes = {500, 1000, 2000};
        for (int n : sizes) {
            int[] data = new int[n];
            Arrays.fill(data, 1);

            long t1 = System.nanoTime();
            int cVal = constantAccess(data);
            long t2 = System.nanoTime();

            long t3 = System.nanoTime();
            long lVal = linearSum(data);
            long t4 = System.nanoTime();

            long t5 = System.nanoTime();
            long qVal = quadraticPairs(data, n);
            long t6 = System.nanoTime();

            System.out.printf("N = %d | O(1): %d ns | O(N): %d us | O(N^2): %d us%n",
                n, (t2 - t1), (t4 - t3) / 1000, (t6 - t5) / 1000);
        }
    }
}
