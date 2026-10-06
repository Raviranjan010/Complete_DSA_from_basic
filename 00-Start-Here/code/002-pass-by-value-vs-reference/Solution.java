/**
 * 002-pass-by-value-vs-reference: Java Strict Pass-by-Value Mechanics
 *
 * In Java, EVERYTHING is passed by value:
 * 1. Primitives: The binary value is copied into the stack frame. Modifying it has zero caller effect.
 * 2. References: The reference value (the 32/64-bit handle pointing to heap memory) is copied!
 *    - Modifying state via the reference (`arr[i] = x`, `obj.setVal(x)`) alters the shared heap object.
 *    - Rebinding the parameter (`arr = new int[]{...}`) only changes the local copy of the handle.
 * 3. Read-only safety: Passed collections can be protected using Collections.unmodifiableList().
 */

import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Solution {
    // Attempting to swap primitives: Fails because values are copied
    public static void swapPrimitives(int x, int y) {
        int temp = x;
        x = y;
        y = temp;
    }

    // In-place mutation through copied reference handle
    public static void swapElements(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Rebinding the reference parameter does NOT affect caller's reference
    public static void reassignReference(int[] arr) {
        arr = new int[]{999, 888};
    }

    public static int processReadOnly(List<Integer> list) {
        // Zero-copy reference pass in O(1) time
        return list.size();
    }

    public static void main(String[] args) {
        int a = 15;
        int b = 99;

        // 1. Primitives are passed by value (copied)
        swapPrimitives(a, b);
        assert a == 15 && b == 99 : "Caller primitives must remain unchanged";

        // 2. Objects/Arrays: Reference is passed by value; object state is mutated
        int[] arr = {15, 99};
        swapElements(arr, 0, 1);
        assert arr[0] == 99 && arr[1] == 15 : "Array elements must be swapped in-place";

        // 3. Rebinding reference does not affect caller
        reassignReference(arr);
        assert arr[0] == 99 && arr[1] == 15 : "Caller reference must not be rebound";

        // 4. Large collections: O(1) reference pass without copying
        List<Integer> largeList = new ArrayList<>();
        for (int i = 0; i < 10000; i++) largeList.add(i);
        List<Integer> unmodifiable = Collections.unmodifiableList(largeList);
        assert processReadOnly(unmodifiable) == 10000;

        System.out.println("[Java] Strict pass-by-value mechanics verified successfully.");
    }
}
