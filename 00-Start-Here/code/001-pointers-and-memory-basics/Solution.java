public class Solution {
    static class Box {
        int value;
        Box(int value) { this.value = value; }
    }

    public static void demonstrateReferenceBasics() {
        Box box = new Box(10);
        Box ref = box;

        System.out.println("Initial scalar value: " + ref.value);
        System.out.println("Identity hash code: " + Integer.toHexString(System.identityHashCode(box)));

        // Indirect mutation through reference
        ref.value = 42;
        System.out.println("Modified scalar value via reference: " + box.value);

        int[] arr = {10, 20, 30};
        System.out.println("\nTraversing array elements:");
        for (int i = 0; i < arr.length; i++) {
            System.out.println("Index " + i + ": Value = " + arr[i]);
        }
    }

    public static void main(String[] args) {
        demonstrateReferenceBasics();
    }
}
