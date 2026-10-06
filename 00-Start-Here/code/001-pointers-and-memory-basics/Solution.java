/**
 * 001-pointers-and-memory-basics: Java Reference Model, Identity & Garbage Collection
 *
 * In Java, there are NO raw pointers, NO address-of operator (&), and NO pointer arithmetic.
 * Instead, Java enforces:
 * 1. Primitive types (int, double, boolean) vs Reference types (Objects, Arrays).
 * 2. Reference Handles: Variables hold reference values pointing to heap objects.
 * 3. Identity vs Equality: '==' compares reference identity; '.equals()' compares logical state.
 * 4. Automatic Garbage Collection: Memory is managed by the JVM (G1/ZGC); objects are
 *    reclaimed automatically when they become unreachable from GC roots.
 */

public class Solution {
    static class Node {
        int value;
        Node(int value) {
            this.value = value;
        }
    }

    public static void demonstrateReferenceModel() {
        // 1. Primitive values: Independent stack values
        int a = 10;
        int b = a;
        b = 42;
        assert a == 10 && b == 42 : "Primitives must not share state";

        // 2. Reference types: Both variables point to the same heap object
        Node n1 = new Node(10);
        Node n2 = n1; // Reference copy
        assert n1 == n2 : "n1 and n2 must refer to the exact same object reference";
        assert System.identityHashCode(n1) == System.identityHashCode(n2);

        // 3. Mutating object state through reference
        n2.value = 42;
        assert n1.value == 42 : "Mutation via n2 must be visible through n1";

        // 4. Rebinding reference: Does NOT mutate the object or other references
        n2 = new Node(99);
        assert n1.value == 42 : "n1 must remain unchanged after n2 rebind";
        assert n1 != n2 : "n1 and n2 now refer to different objects";

        // 5. Array of references: Java arrays of objects store references, not inlined structs
        Node[] nodes = new Node[]{ new Node(10), new Node(20), new Node(30) };
        assert nodes.length == 3;
        for (int i = 0; i < nodes.length; i++) {
            assert nodes[i].value == (i + 1) * 10;
        }

        // 6. Garbage collection eligibility: Nullifying reference drops reference to old node
        n2 = null;
        assert n2 == null;

        System.out.println("[Java] Object references, identity, and GC semantics verified successfully.");
    }

    public static void main(String[] args) {
        demonstrateReferenceModel();
    }
}
