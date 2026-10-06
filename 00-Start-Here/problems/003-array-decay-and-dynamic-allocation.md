# Array Decay, Pointer Sizing & Dynamic Memory Allocation

[← Back to Module Overview](../README.md) · [Concepts: Arrays & Vectors Intro](../concepts/10-arrays-and-vectors-intro.md)

---

## 1. Problem Overview
- **Name:** Array Decay, Pointer Sizing & Dynamic Memory Allocation
- **Difficulty:** Easy
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#memory-model`, `#arrays`, `#dynamic-allocation`
- **External Links:** [GeeksforGeeks: What is Array Decay in C++?](https://www.geeksforgeeks.org/what-is-array-decay-in-c-how-can-it-be-prevented/) · [HackerRank: Variable Sized Arrays](https://www.hackerrank.com/challenges/variable-sized-arrays/problem)

---

## 2. Problem Statement
Implement a demonstration suite illustrating the mechanics of array memory layout and array decay:
1. Demonstrate how a stack-allocated fixed array `int arr[5]` knows its total size in bytes via `sizeof(arr)` within the scope of its declaration.
2. Demonstrate how passing this array to a standard C-style function causes "array decay" into a raw pointer `int*`, reducing `sizeof` to the pointer size (4 or 8 bytes) and losing element count information.
3. Demonstrate modern idioms that prevent array decay:
   - Passing by reference `int (&arr)[N]` or using `std::array<int, N>`.
   - Dynamic heap allocation using `std::vector<int>` with automatic lifetime management.

### Input Specification
An array of $N$ integers.

### Output Specification
- `sizeof` evaluated in the local scope versus inside a decayed function call.
- Demonstration of safe access using `std::vector` and dynamic memory.

### Sample Output
```text
In local scope: sizeof(arr) = 20 bytes (5 elements * 4 bytes)
Inside decayed function: sizeof(decayedPtr) = 8 bytes (pointer size)
Array decay lost the size information!
Safe modern solution: std::vector size = 5, capacity = 5
```

---

## 3. Real-World Motivation
A classic bug in legacy C and early C++ is attempting to determine the length of an array inside a function with `sizeof(arr) / sizeof(arr[0])`. Because arrays decay into pointers when passed to functions, `sizeof(arr)` yields the pointer size (typically 8 bytes on 64-bit systems), leading to silent buffer overflows and security vulnerabilities. Understanding array decay is essential before studying sorting, searching, and custom array containers.

---

## 4. Visual Diagram: Stack vs Heap
```text
Stack Frame (decay vs pointer):
-------------------------------------------------------
[ Local scope ]
arr: [ 10 | 20 | 30 | 40 | 50 ]  (Contiguous 20 bytes on stack)
sizeof(arr) = 20 bytes

[ Function call func(arr) ]
ptr: [ 0x1000 ]                  (Only stores 8-byte memory address!)
sizeof(ptr) = 8 bytes            (The array size metadata is GONE)
-------------------------------------------------------
Modern Vector (RAII on Heap):
Stack: [ pointer to buffer | size = 5 | capacity = 5 ] (24 bytes metadata)
Heap:  [ 10 | 20 | 30 | 40 | 50 ]                      (Dynamic elements buffer)
```

---

## 5. Multi-Language Implementations

### C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <array>

// Decayed function: receives raw pointer, loses size
void decayedFunction(const int arr[]) {
    // sizeof(arr) is sizeof(const int*), not total array size!
    std::cout << "Inside decayed function: sizeof(param) = " << sizeof(arr) 
              << " bytes (pointer size)\n";
}

// Modern C++: prevents decay by accepting std::vector
void safeVectorFunction(const std::vector<int>& vec) {
    std::cout << "Inside safe vector function: size = " << vec.size() 
              << " elements\n";
}

int main() {
    int rawArr[5] = {10, 20, 30, 40, 50};
    
    std::cout << "In local scope: sizeof(rawArr) = " << sizeof(rawArr) 
              << " bytes (5 ints * 4 bytes)\n";
    
    decayedFunction(rawArr);

    std::vector<int> dynamicVec = {10, 20, 30, 40, 50};
    safeVectorFunction(dynamicVec);

    return 0;
}
```

### Python 3 Implementation (Dynamic Lists & Absence of Array Decay)
> **Idiomatic Principle:** Python lists are dynamic array objects allocated on the heap. They **never decay** into raw pointers; `len(lst)` is an $\mathcal{O}(1)$ query into the list's `ob_size` header that remains permanently accessible across all scopes.

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
```

---

## 6. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(1)$ for array decay, size inspection, and pointer passing.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary memory. Dynamic vectors allocate $\mathcal{O}(N)$ contiguous memory on the heap.

---

## 7. Edge Cases & Common Pitfalls
1. **Never calculate array size inside a function via `sizeof`** in C/C++. Always pass the size explicitly: `void func(int* arr, int n)` or use standard library containers (`std::vector`, `std::array`, `std::span`).
2. **Buffer Overflows:** Iterating beyond decayed bounds causes undefined behavior.
