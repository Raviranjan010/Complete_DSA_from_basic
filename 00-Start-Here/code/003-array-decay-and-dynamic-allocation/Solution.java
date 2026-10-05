public class Solution {
    // Java arrays are true heap objects with an immutable .length property
    public static void printArrayLength(int[] arr) {
        System.out.println("Inside method: array length is preserved = " + arr.length);
    }

    public static void main(String[] args) {
        int[] arr = new int[]{10, 20, 30, 40, 50};
        System.out.println("In main: array length = " + arr.length);
        printArrayLength(arr);
    }
}
