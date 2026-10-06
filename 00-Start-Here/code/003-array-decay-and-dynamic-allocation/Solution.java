/**
 * 003-array-decay-and-dynamic-allocation: Java Array Objects & Dynamic Collections
 *
 * In Java, there is NO array decay:
 * 1. Java arrays are true first-class heap objects with an immutable, built-in `.length` field.
 * 2. Arrays never decay to raw pointers when passed to methods; `.length` is always preserved.
 * 3. Runtime bounds checking prevents buffer overruns (`ArrayIndexOutOfBoundsException`).
 * 4. Dynamic Resizing: Handled by `java.util.ArrayList`, which manages a backing `Object[]`
 *    and resizes by 1.5x on overflow.
 * 5. Automatic Memory Management: The JVM garbage collector automatically frees unreferenced arrays.
 */

import java.util.ArrayList;

public class Solution {
    // Array length is permanently attached to the heap object
    public static int getLength(int[] arr) {
        return arr.length;
    }

    public static void demonstrateJavaArrays() {
        int[] fixedArr = new int[]{10, 20, 30, 40, 50};

        // 1. No array decay: Length is fully preserved
        assert fixedArr.length == 5;
        assert getLength(fixedArr) == 5 : "Array length must be preserved across method calls";

        // 2. Dynamic growth via ArrayList (managed heap array resizing)
        ArrayList<Integer> dynamicList = new ArrayList<>();
        for (int i = 0; i < 50; i++) {
            dynamicList.add(i);
        }
        assert dynamicList.size() == 50;
        assert dynamicList.get(49) == 49;

        // 3. JVM GC handles deallocation automatically when references go out of scope
        fixedArr = null;
        assert fixedArr == null;

        System.out.println("[Java] Array objects and dynamic collections verified successfully.");
    }

    public static void main(String[] args) {
        demonstrateJavaArrays();
    }
}
