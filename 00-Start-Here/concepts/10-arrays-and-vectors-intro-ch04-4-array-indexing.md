[← Chapter 03](10-arrays-and-vectors-intro-ch03-vector-vs-array-decision-guide.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 05 →](10-arrays-and-vectors-intro-ch05-21-binary-search-dry-run.md)

---

# 4. Array Indexing

C++ arrays use **zero-based indexing**.

For:

```cpp
int arr[5];
```

valid indices are:

```text
0
1
2
3
4
```

General rule:

```text
valid index = 0 to n - 1
```

where `n` is the array size.

### Example

```cpp
int arr[5] = {10, 20, 30, 40, 50};

cout << arr[0]; // 10
cout << arr[4]; // 50
```

---

# 5. Why Does Indexing Start at 0?

Arrays are stored contiguously.

If the starting address is represented as `base`, the address of an element can be calculated conceptually as:

```text
address(arr[i]) = base + i × sizeof(element)
```

For example, if an `int` occupies 4 bytes:

```text
arr[0] → base
arr[1] → base + 4
arr[2] → base + 8
arr[3] → base + 12
```

The index represents an **offset from the first element**.

This is one reason zero-based indexing fits naturally with memory addressing.

---

# 6. Array Declaration

### Syntax

```cpp
data_type array_name[size];
```

Example:

```cpp
int arr[5];
```

This creates an array capable of storing 5 integers.

---

# 7. Array Initialization

## Method 1 — Full initialization

```cpp
int arr[5] = {10, 20, 30, 40, 50};
```

## Method 2 — Size inferred

```cpp
int arr[] = {10, 20, 30, 40, 50};
```

C++ determines the size as `5`.

## Method 3 — Partial initialization

```cpp
int arr[5] = {10, 20};
```

The remaining elements are initialized to zero:

```text
10 20 0 0 0
```

---

# 8. Array Size

For a built-in array:

```cpp
int arr[] = {10, 20, 30, 40, 50};
```

you can calculate the number of elements using:

```cpp
int n = sizeof(arr) / sizeof(arr[0]);
```

If `int` is 4 bytes:

```text
sizeof(arr)    = 20
sizeof(arr[0]) = 4

20 / 4 = 5
```

Therefore:

```cpp
n = 5;
```

### Important

This works when `arr` is actually an array in that scope.

It does **not** work the same way after an array has decayed to a pointer when passed to a normal function parameter.

---

# 9. Input into an Array

A common pattern:

```cpp
int n;
cin >> n;

int arr[n];

for (int i = 0; i < n; i++) {
    cin >> arr[i];
}
```

### Important C++ note

`int arr[n];` where `n` is determined at runtime is a **variable-length array (VLA)**. It is not part of standard C++.

Some compilers accept it as an extension, but portable C++ should use:

```cpp
vector<int> arr(n);
```

For beginner DSA on platforms that specifically permit VLAs, you may see the original form, but understand the standard C++ distinction.

---

# 10. Printing an Array

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
```

Example:

```text
10 20 30 40 50
```

---

# 11. Traversal

## Definition

**Array traversal** means visiting each element of an array, usually from the first element to the last.

Example:

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

assuming no additional array is created.

---

# 12. Forward Traversal

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
```

Traversal:

```text
0 → 1 → 2 → 3 → ... → n-1
```

---

# 13. Reverse Traversal

```cpp
for (int i = n - 1; i >= 0; i--) {
    cout << arr[i] << " ";
}
```

Traversal:

```text
n-1 → n-2 → ... → 2 → 1 → 0
```

---

# 14. Accessing an Element

Array access:

```cpp
arr[index]
```

Example:

```cpp
int arr[] = {10, 20, 30};

cout << arr[1];
```

Output:

```text
20
```

Access by index is:

```text
Time = O(1)
```

because the address can be calculated directly.

---

# 15. Updating an Element

```cpp
int arr[] = {10, 20, 30};

arr[1] = 100;
```

Array becomes:

```text
10 100 30
```

Complexity:

```text
O(1)
```

---

# 16. Searching in an Array

Searching means finding whether a target value exists and, often, finding its index.

There are two major approaches:

```text
Linear Search
Binary Search
```

---

# 17. Linear Search

## Definition

**Linear search** checks elements sequentially until the target is found or the array ends.

Example:

```cpp
int linearSearch(int arr[], int n, int target) {

    for (int i = 0; i < n; i++) {

        if (arr[i] == target) {
            return i;
        }
    }

    return -1;
}
```

Example:

```text
Array:   10  20  30  40  50
Index:    0   1   2   3   4

Target = 40
```

Checks:

```text
10 → no
20 → no
30 → no
40 → yes
```

Returns:

```text
3
```

---

# 18. Why Return `-1`?

Array indices are normally:

```text
0 to n-1
```

So `-1` cannot be a valid index.

Therefore it is commonly used as a sentinel value meaning:

> Target was not found.

Example:

```cpp
int index = linearSearch(arr, n, target);

if (index == -1) {
    cout << "Not found";
}
else {
    cout << "Found at index " << index;
}
```

---

# 19. Linear Search Complexity

### Best case

Target is at index `0`.

```text
O(1)
```

### Worst case

Target is at the end or absent.

```text
O(n)
```

### Average case

```text
O(n)
```

### Space

```text
O(1)
```

---

# 20. Binary Search

## Definition

**Binary search** repeatedly divides the search range into two halves.

### Critical requirement

The array must be **sorted** according to the ordering being searched.

Example:

```text
1 3 5 7 9 11 13
```

Search for:

```text
9
```

Instead of checking every element, binary search checks the middle and eliminates half of the remaining search space.

---
