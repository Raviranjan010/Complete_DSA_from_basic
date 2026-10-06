#!/usr/bin/env python3
"""
tools/update_00_idioms.py
Ensures Problems 001-003 in 00-Start-Here follow the Idiomatic Rule:
- Python and Java sections explain real equivalents (references, object identity, garbage collection)
- They do NOT mimic C++ pointers or pointer arithmetic.
"""

import os
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent

# =====================================================================
# PROBLEM 001
# =====================================================================

py_001_code = '''"""
001-pointers-and-memory-basics: Python Reference Semantics, Object Identity & GC

In Python, there are NO raw memory pointers or pointer arithmetic.
Instead, Python uses:
1. Object References: Every variable is a name bound to an object in heap memory.
2. Object Identity (id()): Represents the memory address of the object in CPython.
3. Mutability vs Immutability:
   - Immutable objects (int, float, str, tuple): cannot be changed in place.
   - Mutable objects (list, dict, custom classes): state can be mutated via any reference.
4. Garbage Collection: Python uses reference counting + generational cyclic GC.
"""

import sys
import gc

class Entity:
    """A custom class demonstrating reference binding and field mutation."""
    def __init__(self, value: int):
        self.value = value

def demonstrate_object_identity():
    # 1. Names and Object Identity
    val1 = 1000
    val2 = val1
    assert val1 is val2
    assert id(val1) == id(val2)

    # 2. Immutability: Rebinding does NOT mutate the original object
    val2 += 1
    assert val1 == 1000 and val2 == 1001
    assert val1 is not val2

    # 3. Mutable Objects: Multiple references observe the same mutation
    entity1 = Entity(10)
    entity2 = entity1  # Both names point to the same object reference
    assert entity1 is entity2
    assert id(entity1) == id(entity2)

    entity2.value = 42
    assert entity1.value == 42  # Reflected through entity1

    # 4. Traversal: List holds references to objects, not raw contiguous memory
    items = [Entity(10), Entity(20), Entity(30)]
    for i, item in enumerate(items):
        assert item.value == (i + 1) * 10
        assert isinstance(id(item), int)

    # 5. Reference Counting and Garbage Collection
    initial_refs = sys.getrefcount(entity1)
    alias = entity1
    assert sys.getrefcount(entity1) == initial_refs + 1
    del alias
    assert sys.getrefcount(entity1) == initial_refs

    print("[Python] Object identity, reference semantics, and GC verified successfully.")

if __name__ == "__main__":
    demonstrate_object_identity()
'''

java_001_code = '''/**
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
'''

# =====================================================================
# PROBLEM 002
# =====================================================================

py_002_code = '''"""
002-pass-by-value-vs-reference: Python Call-by-Object-Reference Mechanics

In Python, all arguments are passed via "Call-by-Object-Reference" (call-by-sharing):
1. Immutable objects (int, float, str, tuple):
   Reassigning a parameter binds a new object locally; caller's variable is unaffected.
   Idiomatic swap: `a, b = b, a` (tuple packing & unpacking).
2. Mutable objects (list, dict, set, class instance):
   - Reassigning `param = new_obj` rebinds the local name; caller is unaffected.
   - Mutating in-place `param[i] = val` or `param.append()` mutates the shared object; caller sees changes.
3. Large structures: Python passes references in O(1) time without copying. Read-only
   guarantees are achieved idiomatically via tuples or views.
"""

def attempt_swap_immutable(x: int, y: int):
    """Rebinding local parameters has NO effect on the caller."""
    x, y = y, x

def swap_in_mutable_sequence(seq: list, i: int, j: int):
    """In-place mutation affects the shared heap object."""
    seq[i], seq[j] = seq[j], seq[i]

def reassign_container(seq: list):
    """Rebinding the parameter does NOT rebind the caller's reference."""
    seq = [999, 888]

def inspect_large_structure_zero_copy(data: tuple) -> int:
    """Passing large structures is O(1) zero-copy reference passing."""
    return len(data)

def main():
    a = 15
    b = 99

    # 1. Immutable types cannot be swapped via a mutating helper
    attempt_swap_immutable(a, b)
    assert a == 15 and b == 99

    # 2. Idiomatic Python swap via tuple packing/unpacking
    a, b = b, a
    assert a == 99 and b == 15

    # 3. Mutable sequence in-place mutation
    arr = [15, 99]
    swap_in_mutable_sequence(arr, 0, 1)
    assert arr == [99, 15]

    # 4. Parameter rebinding does not mutate caller's list
    reassign_container(arr)
    assert arr == [99, 15]

    # 5. Zero-copy large container passing
    large_tuple = tuple(range(100000))
    count = inspect_large_structure_zero_copy(large_tuple)
    assert count == 100000

    print("[Python] Call-by-object-reference mechanics verified successfully.")

if __name__ == "__main__":
    main()
'''

java_002_code = '''/**
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
'''

# =====================================================================
# PROBLEM 003
# =====================================================================

py_003_code = '''"""
003-array-decay-and-dynamic-allocation: Python Dynamic Lists & Memory Model

In Python, there is NO array decay:
1. Lists are dynamic arrays of object references allocated on the heap.
2. The length is permanently stored in the PyVarObject header (`ob_size`).
   `len(lst)` is O(1) and is never lost across function calls.
3. Over-allocation: CPython uses an amortized geometric growth pattern
   (0, 4, 8, 16, 25, 35, 46, ...) during `append()`.
4. Garbage Collection: Python reclaims memory automatically when reference count drops to 0.
"""

import sys

def inspect_list(elements: list) -> int:
    # Length metadata is preserved across all function boundaries
    return len(elements)

def demonstrate_dynamic_list():
    elements = [10, 20, 30, 40, 50]
    
    # 1. No array decay: length is preserved
    assert len(elements) == 5
    assert inspect_list(elements) == 5

    # 2. Container memory overhead (PyListObject header + pointer array)
    base_size = sys.getsizeof(elements)
    assert base_size > 0

    # 3. Dynamic resizing via geometric over-allocation
    dynamic_list = []
    sizes = []
    for i in range(20):
        dynamic_list.append(i)
        sizes.append(sys.getsizeof(dynamic_list))
    
    # Over-allocation causes jump steps rather than reallocating every append
    assert len(set(sizes)) > 1

    print("[Python] Dynamic array internals and lack of array decay verified successfully.")

if __name__ == "__main__":
    demonstrate_dynamic_list()
'''

java_003_code = '''/**
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
'''

# Write code files
p1 = repo_root / '00-Start-Here' / 'code' / '001-pointers-and-memory-basics'
with open(p1 / 'solution.py', 'w', encoding='utf-8') as f:
    f.write(py_001_code)
with open(p1 / 'Solution.java', 'w', encoding='utf-8') as f:
    f.write(java_001_code)

p2 = repo_root / '00-Start-Here' / 'code' / '002-pass-by-value-vs-reference'
with open(p2 / 'solution.py', 'w', encoding='utf-8') as f:
    f.write(py_002_code)
with open(p2 / 'Solution.java', 'w', encoding='utf-8') as f:
    f.write(java_002_code)

p3 = repo_root / '00-Start-Here' / 'code' / '003-array-decay-and-dynamic-allocation'
with open(p3 / 'solution.py', 'w', encoding='utf-8') as f:
    f.write(py_003_code)
with open(p3 / 'Solution.java', 'w', encoding='utf-8') as f:
    f.write(java_003_code)

print("Updated code files for 001-003.")
