public class Solution {
    // Java is strictly pass-by-value. For primitives, values are copied.
    public static void swapPrimitives(int x, int y) {
        int temp = x;
        x = y;
        y = temp;
    }

    // For objects/arrays, the reference handle is passed by value
    public static void swapArrayElements(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int a = 15;
        int b = 99;
        System.out.println("Before swap: a = " + a + ", b = " + b);

        swapPrimitives(a, b);
        System.out.println("After swapPrimitives: a = " + a + ", b = " + b + " (no change)");

        int[] arr = {15, 99};
        swapArrayElements(arr, 0, 1);
        System.out.println("After swapArrayElements: a = " + arr[0] + ", b = " + arr[1] + " (swapped)");
    }
}
