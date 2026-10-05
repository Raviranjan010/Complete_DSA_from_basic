# Pass-by-Value vs Pass-by-Reference & Side Effects

[← Back to Module Overview](../README.md) · [Concepts: Functions & Parameter Passing](../concepts/08-functions-and-parameter-passing.md)

---

## 1. Problem Overview
- **Name:** Pass-by-Value vs Pass-by-Reference Demonstration
- **Difficulty:** Easy
- **Tier:** A (Flagship Foundation)
- **Pattern:** `#functions`, `#parameter-passing`, `#memory-model`
- **External Links:** [GeeksforGeeks: Pass by Value vs Pass by Reference](https://www.geeksforgeeks.org/pass-by-value-and-pass-by-reference-in-cpp/) · [LeetCode: Swap Nodes in Pairs (Concept)](https://leetcode.com/problems/swap-nodes-in-pairs/)

---

## 2. Problem Statement
Implement a demonstration suite comparing the mechanics of parameter passing across modern programming languages:
1. A function `swapByValue(a, b)` that attempts to swap two values using copy semantics. Demonstrate that caller variables remain unchanged.
2. A function `swapByReference(a, b)` (or pointer-based equivalent) that modifies caller variables in-place.
3. A function `printLargeStructure(const vector<int>& v)` demonstrating how `const` reference passing avoids costly $\mathcal{O}(N)$ copy overhead while guaranteeing read-only safety.

### Input Specification
Two integer values `a` and `b`, and a vector/array of $N$ integers.

### Output Specification
Print the values of `a` and `b` before swap, after `swapByValue`, and after `swapByReference`. Print the confirmation of non-copied traversal.

### Sample Input
```text
a = 15, b = 99
Array: [1, 2, 3, 4, 5]
```

### Sample Output
```text
Before swap: a = 15, b = 99
After swapByValue: a = 15, b = 99 (no change)
After swapByReference: a = 99, b = 15 (successfully swapped)
Const reference passed array of size 5 without copying.
```

---

## 3. Real-World Motivation
In algorithm design and competitive programming, passing large collections (vectors, strings, trees, graphs) by value silently clones the entire data structure, transforming an intended $\mathcal{O}(N)$ algorithm into an accidental $\mathcal{O}(N^2)$ algorithm that exceeds time or memory limits (`TLE` / `MLE`). Understanding pass-by-reference and `const &` is mandatory for writing performant code.

---

## 4. Visual Representation & Call Stack
```text
Stack Frames during pass-by-value vs pass-by-reference:

1. PASS BY VALUE:
[ main() frame ]
  a = 15, b = 99
       | copy
       v
[ swapByValue(x, y) frame ]
  x = 15, y = 99  --> temp = x; x = y; y = temp; (x becomes 99, y becomes 15)
  *Stack frame destroyed on return!*
  main's a and b are UNCHANGED.

2. PASS BY REFERENCE:
[ main() frame ]
  a = 15, b = 99
       ^      ^
       | bind |
[ swapByReference(&x, &y) ]
  x aliases a, y aliases b.
  Mutations directly alter memory at addresses &a and &b!
```

---

## 5. Multi-Language Implementations

### C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <utility>

// Pass-by-value: copies are made on function stack
void swapByValue(int x, int y) {
    int temp = x;
    x = y;
    y = temp;
}

// Pass-by-reference: aliases caller's variables directly
void swapByReference(int& x, int& y) {
    int temp = x;
    x = y;
    y = temp;
}

// Pass-by-const-reference: zero-copy read-only access
void processLargeData(const std::vector<int>& data) {
    std::cout << "Read-only access to vector of size " << data.size() 
              << " without copying.\n";
}

int main() {
    int a = 15, b = 99;

    std::cout << "Before swap: a = " << a << ", b = " << b << "\n";

    swapByValue(a, b);
    std::cout << "After swapByValue: a = " << a << ", b = " << b << " (no change)\n";

    swapByReference(a, b);
    std::cout << "After swapByReference: a = " << a << ", b = " << b << " (swapped)\n";

    std::vector<int> numbers = {1, 2, 3, 4, 5};
    processLargeData(numbers);

    return 0;
}
```

### Python 3 Implementation (Call-by-Object-Reference)
```python
def swap_by_value(x: int, y: int):
    # Integers in Python are immutable; rebinding x and y has no outer effect
    temp = x
    x = y
    y = temp

def swap_in_container(container: list, i: int, j: int):
    # In-place swap by mutating the shared container reference
    container[i], container[j] = container[j], container[i]

def main():
    a = 15
    b = 99
    print(f"Before swap: a = {a}, b = {b}")

    swap_by_value(a, b)
    print(f"After swap_by_value: a = {a}, b = {b} (no change)")

    # Swapping values in Python idiomatically
    a, b = b, a
    print(f"After idiomatic swap: a = {a}, b = {b} (swapped)")

    arr = [15, 99]
    swap_in_container(arr, 0, 1)
    print(f"After container in-place swap: arr = {arr}")

if __name__ == "__main__":
    main()
```

### Java 17 Implementation (Pass-by-Value-of-Reference)
```java
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
```

---

## 6. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(1)$ for scalar swap operations. Passing large vectors of size $N$ takes $\mathcal{O}(1)$ with `const &` versus $\mathcal{O}(N)$ when passed by value.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space for reference passing; $\mathcal{O}(N)$ additional stack space when passing containers by value.

---

## 7. Edge Cases & Common Pitfalls
1. **Accidental Copy in Range-based For Loops:** Writing `for (auto x : vec)` makes a copy of every element! Always use `for (const auto& x : vec)` for read-only iteration or `for (auto& x : vec)` for in-place mutation.
2. **Returning References to Local Stack Variables:** Returning `int&` or `string&` pointing to a local variable creates undefined behavior (`dangling reference`).
3. **Java Reference Rebinding:** Reassigning a reference parameter inside a Java method does not change the caller's reference.
