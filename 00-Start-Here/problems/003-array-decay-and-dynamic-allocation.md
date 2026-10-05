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

### Python 3 Implementation (List Internals & Sizing)
```python
import sys

def main():
    # Python lists are dynamic arrays of object references on the heap
    elements = [10, 20, 30, 40, 50]
    
    print(f"List length: {len(elements)}")
    print(f"Base container memory overhead: {sys.getsizeof(elements)} bytes")
    print(f"Elements retain length metadata when passed to functions: len = {len(elements)}")

if __name__ == "__main__":
    main()
```

### Java 17 Implementation (Array Objects)
```java
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
```

---

## 6. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(1)$ for array decay, size inspection, and pointer passing.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary memory. Dynamic vectors allocate $\mathcal{O}(N)$ contiguous memory on the heap.

---

## 7. Edge Cases & Common Pitfalls
1. **Never calculate array size inside a function via `sizeof`** in C/C++. Always pass the size explicitly: `void func(int* arr, int n)` or use standard library containers (`std::vector`, `std::array`, `std::span`).
2. **Buffer Overflows:** Iterating beyond decayed bounds causes undefined behavior.
