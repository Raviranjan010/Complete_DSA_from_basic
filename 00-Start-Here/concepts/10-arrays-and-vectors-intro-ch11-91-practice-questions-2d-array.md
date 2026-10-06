[← Chapter 10](10-arrays-and-vectors-intro-ch10-83-practice-questions-searchin.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 12 →](10-arrays-and-vectors-intro-ch12-3-vector-header-file.md)

---

# 91. Practice Questions — 2D Arrays

## Q33. Print matrix

Input:

```text
1 2 3
4 5 6
7 8 9
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

---

## Q34. Row sums

For:

```text
1 2 3
4 5 6
7 8 9
```

Expected:

```text
6
15
24
```

---

## Q35. Column sums

Expected:

```text
12
15
18
```

---

## Q36. Primary diagonal

Expected:

```text
1 5 9
```

---

## Q37. Secondary diagonal

Expected:

```text
3 5 7
```

---

# 92. Interview-Level Questions

### Q38. Why is array access O(1)?

Explain using:

```text
base address + index × element size
```

---

### Q39. Why does array indexing start at zero?

Explain the index as an offset from the first element.

---

### Q40. Why is insertion at the beginning O(n)?

Explain element shifting.

---

### Q41. Why is binary search O(log n)?

Explain how the search space becomes approximately:

```text
n
n/2
n/4
n/8
...
1
```

---

### Q42. What is the difference between an array and a vector?

Discuss:

- size
- memory
- resizing
- insertion
- C++ usage

---

### Q43. What is array decay?

Explain why:

```cpp
void func(int arr[])
```

behaves like:

```cpp
void func(int* arr)
```

for a function parameter.

---

### Q44. Why can't a function automatically know the length of a raw array parameter?

Because the array parameter is adjusted to a pointer, so the size information is not carried with that parameter.

That's why we commonly pass:

```cpp
func(arr, n);
```

---

### Q45. What happens if we access `arr[n]`?

For an array with `n` elements, `arr[n]` is outside the valid index range.

Accessing it results in **undefined behavior**.

---

# 93. Array Problem Recognition Guide

When you see:

### "Find maximum/minimum"

Think:

```text
single traversal
```

### "Find whether target exists"

Think:

```text
linear search
```

### "Sorted array + search"

Think:

```text
binary search
```

### "Reverse array"

Think:

```text
two pointers
```

### "Pair sum in sorted array"

Think:

```text
two pointers
```

### "Repeated range sums"

Think:

```text
prefix sum
```

### "Frequency / duplicates"

Think:

```text
hashing / frequency array / set
```

### "Contiguous segment"

Think:

```text
subarray
sliding window
prefix sum
Kadane
```

### "Rotate"

Think:

```text
shifting
or
reversal algorithm
```

---

# 94. Most Important Array Concepts to Master

Before moving to advanced DSA, make sure you understand:

```text
1. Array definition
2. Homogeneous storage
3. Contiguous memory
4. Zero-based indexing
5. Declaration
6. Initialization
7. Traversal
8. Access
9. Update
10. Searching
11. Linear search
12. Binary search
13. Minimum
14. Maximum
15. Sum
16. Product
17. Frequency
18. Reverse
19. Two pointers
20. In-place operations
21. Passing arrays to functions
22. const array parameters
23. 2D arrays
24. Row/column traversal
25. Diagonals
26. Rotation
27. Duplicates
28. Unique elements
29. Prefix sums
30. Subarrays
31. Kadane's algorithm
32. Array complexity
33. Edge cases
34. Overflow
35. Array vs vector
36. Array vs linked list
```

---

# 95. Final Array Cheat Sheet

```text
Array
│
├── Same element type
├── Contiguous storage
├── Zero-based indexing
├── Fixed size for built-in array
│
├── Access → O(1)
├── Update → O(1)
├── Traverse → O(n)
├── Search → O(n)
├── Binary Search → O(log n)
├── Reverse → O(n)
├── Min/Max → O(n)
│
├── Patterns
│   ├── Traversal
│   ├── Two pointers
│   ├── Sliding window
│   ├── Prefix sum
│   ├── Hashing
│   └── Binary search
│
└── Important problems
    ├── Sum
    ├── Min/Max
    ├── Search
    ├── Reverse
    ├── Rotate
    ├── Duplicates
    ├── Unique elements
    ├── Intersection
    ├── Missing number
    ├── Second largest
    ├── Move zeros
    ├── Two Sum
    ├── Prefix Sum
    └── Maximum Subarray
```

---

# 96. Recommended Learning Order

Study arrays in this order:

```text
1. What is an Array?
        ↓
2. Indexing & Memory
        ↓
3. Declaration & Initialization
        ↓
4. Input / Output
        ↓
5. Traversal
        ↓
6. Min / Max
        ↓
7. Sum / Product
        ↓
8. Linear Search
        ↓
9. Reverse
        ↓
10. Frequency / Duplicates
        ↓
11. Sorted Array
        ↓
12. Binary Search
        ↓
13. Two Pointers
        ↓
14. Rotation
        ↓
15. Prefix Sum
        ↓
16. Sliding Window
        ↓
17. Kadane's Algorithm
        ↓
18. 2D Arrays
        ↓
19. Array Interview Problems
        ↓
20. LeetCode / Coding Problems
```

> **Goal:** Do not memorize solutions. Learn to identify the pattern behind the problem. Once you can recognize whether a problem requires traversal, two pointers, hashing, prefix sum, sliding window, or binary search, solving array problems becomes much easier.


---

## Supplementary Reference from 02_Cpp_Vectors_and_Advanced_Array_DSA_Notes.md

# C++ Vectors & Advanced Array Patterns — DSA Notes

> These notes continue the Array chapter and cover **`vector`, vector functions, size vs capacity, dynamic growth, Kadane's Algorithm, Pair Sum, Two Pointers, Hashing, Majority Element, and Moore's Voting Algorithm** with detailed explanations, dry runs, complexity, mistakes, and practice questions.

---

# 1. Vector in C++

## Definition

A **vector** is a dynamic sequence container provided by the C++ Standard Library.

Unlike a built-in array whose size is fixed after creation, a vector can automatically grow or shrink as elements are added or removed.

```cpp
#include <vector>
using namespace std;

vector<int> nums;
```

A vector:

- stores elements of the same type
- supports index-based access
- manages its own memory
- can dynamically change its size
- provides many built-in functions
- is implemented as a class template

---

# 2. Why Do We Need Vectors?

Consider a built-in array:

```cpp
int arr[5];
```

Its capacity is fixed at 5 elements.

You cannot simply do:

```cpp
arr.push_back(10);
```

because a built-in array does not have `push_back()`.

A vector solves this:

```cpp
vector<int> arr;

arr.push_back(10);
arr.push_back(20);
arr.push_back(30);
```

Now:

```text
10 20 30
```

The vector automatically manages the storage required for its elements.

---
