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

### Python 3 Implementation (Call-by-Object-Reference Mechanics)
> **Idiomatic Principle:** Python evaluation is strictly **Call-by-Object-Reference** (call-by-sharing). Reassigning an immutable parameter (`int`, `str`) rebinds the local name without altering the caller's variable. Idiomatic swapping uses tuple assignment (`a, b = b, a`). Mutating a mutable collection in-place alters the shared object directly.

```python
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
