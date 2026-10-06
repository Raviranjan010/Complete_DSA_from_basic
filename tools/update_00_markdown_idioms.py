#!/usr/bin/env python3
"""
tools/update_00_markdown_idioms.py
Updates the Markdown documentation for problems 001, 002, and 003 in 00-Start-Here
to explain real language-specific equivalents (references, object identity, garbage collection)
without mimicking C++ pointers.
"""

from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent

# --- 001 Problem Markdown Update ---
p1_file = repo_root / '00-Start-Here' / 'problems' / '001-pointers-and-memory-basics.md'
p1_text = p1_file.read_text(encoding='utf-8')

p1_py_java = """### Python 3 Implementation (Object Identity, Reference Model & Garbage Collection)
> **Idiomatic Principle:** Python does **not** have raw pointers, address-of operators (`&`), or pointer arithmetic. Variables in Python are symbolic names bound to objects in heap memory. Python manages memory via reference counting and cyclic garbage collection.

```python
import sys
import gc

class Entity:
    \"\"\"Demonstrating reference binding and attribute mutation.\"\"\"
    def __init__(self, value: int):
        self.value = value

def demonstrate_object_identity():
    # 1. Variable names as object bindings
    val1 = 1000
    val2 = val1
    assert val1 is val2
    assert id(val1) == id(val2)

    # 2. Immutability: Rebinding creates a new integer object; does not mutate in-place
    val2 += 1
    assert val1 == 1000 and val2 == 1001
    assert val1 is not val2

    # 3. Mutable Objects: Multiple references share the same heap object
    entity1 = Entity(10)
    entity2 = entity1  # Aliased reference
    assert entity1 is entity2
    assert id(entity1) == id(entity2)

    entity2.value = 42
    assert entity1.value == 42  # Mutation visible through entity1

    # 4. Traversal: Lists store references to objects, not raw contiguous structs
    items = [Entity(10), Entity(20), Entity(30)]
    for i, item in enumerate(items):
        assert item.value == (i + 1) * 10
        assert isinstance(id(item), int)

    # 5. Reference Counting and Automatic Garbage Collection
    initial_refs = sys.getrefcount(entity1)
    alias = entity1
    assert sys.getrefcount(entity1) == initial_refs + 1
    del alias
    assert sys.getrefcount(entity1) == initial_refs

    print("[Python] Object identity, reference semantics, and GC verified successfully.")

if __name__ == "__main__":
    demonstrate_object_identity()
```

### Java 17 Implementation (Reference Handles, Heap Objects & JVM Garbage Collection)
> **Idiomatic Principle:** Java forbids raw memory addresses, pointer dereferencing, and pointer arithmetic. Primitives reside directly on the execution stack, while all objects reside on the JVM managed heap. References are type-safe, opaque 32/64-bit handles.

```java
public class Solution {
    static class Node {
        int value;
        Node(int value) {
            this.value = value;
        }
    }

    public static void demonstrateReferenceModel() {
        // 1. Primitive types: Independent stack variables
        int a = 10;
        int b = a;
        b = 42;
        assert a == 10 && b == 42 : "Primitives do not share state";

        // 2. Reference types: Handles pointing to the same heap instance
        Node n1 = new Node(10);
        Node n2 = n1; // Reference handle copy
        assert n1 == n2 : "n1 and n2 reference identical heap object";
        assert System.identityHashCode(n1) == System.identityHashCode(n2);

        // 3. Mutation through reference
        n2.value = 42;
        assert n1.value == 42 : "Mutation via n2 visible through n1";

        // 4. Reference rebinding: Does NOT affect the original heap object
        n2 = new Node(99);
        assert n1.value == 42 : "n1 retains original object";
        assert n1 != n2;

        // 5. Array of references: Java arrays of objects store reference handles
        Node[] nodes = new Node[]{ new Node(10), new Node(20), new Node(30) };
        assert nodes.length == 3;
        for (int i = 0; i < nodes.length; i++) {
            assert nodes[i].value == (i + 1) * 10;
        }

        // 6. Automatic Garbage Collection: Nulling drops reference, making object GC-eligible
        n2 = null;
        assert n2 == null;

        System.out.println("[Java] Object references, identity, and GC semantics verified successfully.");
    }

    public static void main(String[] args) {
        demonstrateReferenceModel();
    }
}
```"""

# Find python section and replace until complexity analysis
py_pos1 = p1_text.find('### Python 3 Implementation')
c_pos1 = p1_text.find('---', py_pos1)
if py_pos1 != -1 and c_pos1 != -1:
    p1_text = p1_text[:py_pos1] + p1_py_java + '\n\n' + p1_text[c_pos1:]
    p1_file.write_text(p1_text, encoding='utf-8')
    print("Updated 001 markdown.")

# --- 002 Problem Markdown Update ---
p2_file = repo_root / '00-Start-Here' / 'problems' / '002-pass-by-value-vs-reference.md'
p2_text = p2_file.read_text(encoding='utf-8')

p2_py_java = """### Python 3 Implementation (Call-by-Object-Reference Mechanics)
> **Idiomatic Principle:** Python evaluation is strictly **Call-by-Object-Reference** (call-by-sharing). Reassigning an immutable parameter (`int`, `str`) rebinds the local name without altering the caller's variable. Idiomatic swapping uses tuple assignment (`a, b = b, a`). Mutating a mutable collection in-place alters the shared object directly.

```python
def attempt_swap_immutable(x: int, y: int):
    \"\"\"Rebinding local parameters has NO effect on the caller.\"\"\"
    x, y = y, x

def swap_in_mutable_sequence(seq: list, i: int, j: int):
    \"\"\"In-place mutation affects the shared heap object.\"\"\"
    seq[i], seq[j] = seq[j], seq[i]

def reassign_container(seq: list):
    \"\"\"Rebinding the parameter does NOT rebind the caller's reference.\"\"\"
    seq = [999, 888]

def inspect_large_structure_zero_copy(data: tuple) -> int:
    \"\"\"Passing large structures is O(1) zero-copy reference passing.\"\"\"
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
```

### Java 17 Implementation (Strict Pass-by-Value Mechanics)
> **Idiomatic Principle:** Java is strictly **Pass-by-Value**. For primitives, the value itself is copied. For objects and arrays, the reference handle is copied into the stack frame. Reassigning a reference parameter does not alter the caller's reference, but mutating fields/elements through the handle modifies the shared heap instance.

```java
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
```"""

py_pos2 = p2_text.find('### Python 3 Implementation')
c_pos2 = p2_text.find('---', py_pos2)
if py_pos2 != -1 and c_pos2 != -1:
    p2_text = p2_text[:py_pos2] + p2_py_java + '\n\n' + p2_text[c_pos2:]
    p2_file.write_text(p2_text, encoding='utf-8')
    print("Updated 002 markdown.")

# --- 003 Problem Markdown Update ---
p3_file = repo_root / '00-Start-Here' / 'problems' / '003-array-decay-and-dynamic-allocation.md'
p3_text = p3_file.read_text(encoding='utf-8')

p3_py_java = """### Python 3 Implementation (Dynamic Lists & Absence of Array Decay)
> **Idiomatic Principle:** Python lists are dynamic array objects allocated on the heap. They **never decay** into raw pointers; `len(lst)` is an $\\mathcal{O}(1)$ query into the list's `ob_size` header that remains permanently accessible across all scopes.

```python
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
```

### Java 17 Implementation (First-Class Array Objects & ArrayList)
> **Idiomatic Principle:** In Java, arrays are true first-class objects residing on the garbage-collected heap. They have an immutable `.length` property and never decay to raw pointers. Dynamic growth is handled cleanly via `ArrayList<E>`, backed by automatic JVM garbage collection.

```java
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
```"""

py_pos3 = p3_text.find('### Python 3 Implementation')
c_pos3 = p3_text.find('---', py_pos3)
if py_pos3 != -1 and c_pos3 != -1:
    p3_text = p3_text[:py_pos3] + p3_py_java + '\n\n' + p3_text[c_pos3:]
    p3_file.write_text(p3_text, encoding='utf-8')
    print("Updated 003 markdown.")
