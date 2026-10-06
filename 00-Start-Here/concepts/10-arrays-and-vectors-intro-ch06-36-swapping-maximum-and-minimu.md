[← Chapter 05](10-arrays-and-vectors-intro-ch05-21-binary-search-dry-run.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 07 →](10-arrays-and-vectors-intro-ch07-50-why-does-the-array-change.md)

---

# 36. Swapping Maximum and Minimum

### Problem

Given:

```text
5 2 9 1 7
```

minimum:

```text
1
```

maximum:

```text
9
```

After swapping their positions:

```text
5 2 1 9 7
```

### Approach

1. Find minimum value and its index.
2. Find maximum value and its index.
3. Swap the two positions.

```cpp
int minIndex = 0;
int maxIndex = 0;

for (int i = 1; i < n; i++) {

    if (arr[i] < arr[minIndex])
        minIndex = i;

    if (arr[i] > arr[maxIndex])
        maxIndex = i;
}

swap(arr[minIndex], arr[maxIndex]);
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 37. Important Question: What If Minimum = Maximum?

Example:

```text
5 5 5 5
```

Both minimum and maximum are `5`.

Swapping their positions changes nothing.

Result:

```text
5 5 5 5
```

This is an important edge case.

---

# 38. Unique Elements

## What Does "Unique" Mean?

There are two common interpretations.

### Interpretation 1

Print elements that appear **exactly once**.

Example:

```text
Input:
1 2 2 3 4 4 5

Output:
1 3 5
```

### Interpretation 2

Print each distinct value only once.

Example:

```text
Input:
1 2 2 3 4 4 5

Output:
1 2 3 4 5
```

These are **different problems**.

Always determine which meaning the question intends.

---

# 39. Print Elements Appearing Exactly Once

Simple approach using nested loops:

```cpp
for (int i = 0; i < n; i++) {

    int count = 0;

    for (int j = 0; j < n; j++) {

        if (arr[i] == arr[j]) {
            count++;
        }
    }

    if (count == 1) {
        cout << arr[i] << " ";
    }
}
```

Complexity:

```text
Time  = O(n²)
Space = O(1)
```

---

# 40. Distinct Elements Using `set`

If you want each value only once:

```cpp
set<int> s;

for (int i = 0; i < n; i++) {
    s.insert(arr[i]);
}
```

Then:

```cpp
for (int x : s) {
    cout << x << " ";
}
```

Note:

> `set` stores unique values and keeps them ordered.

If you need insertion-order-like behavior or faster average lookup, other approaches may be appropriate.

---

# 41. Frequency of an Element

### Problem

Count how many times `target` occurs.

```cpp
int count = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] == target) {
        count++;
    }
}
```

Example:

```text
Array:
1 2 2 3 2 4

target = 2

count = 3
```

---

# 42. First Occurrence

The first occurrence is the smallest index at which the target appears.

```cpp
int index = -1;

for (int i = 0; i < n; i++) {

    if (arr[i] == target) {
        index = i;
        break;
    }
}
```

---

# 43. Last Occurrence

```cpp
int index = -1;

for (int i = 0; i < n; i++) {

    if (arr[i] == target) {
        index = i;
    }
}
```

Example:

```text
Array: 1 2 3 2 4 2

target = 2
```

Last occurrence:

```text
index = 5
```

---

# 44. Check if Array is Sorted

Suppose:

```text
1 2 3 4 5
```

is sorted in non-decreasing order.

We check adjacent elements.

```cpp
bool sorted = true;

for (int i = 1; i < n; i++) {

    if (arr[i] < arr[i - 1]) {
        sorted = false;
        break;
    }
}
```

If `sorted` remains true, the array is sorted.

### Complexity

```text
O(n)
```

---

# 45. Ascending vs Strictly Increasing

These are different.

### Non-decreasing

```text
1 2 2 3 4
```

Duplicates allowed.

Condition:

```cpp
arr[i] >= arr[i - 1]
```

### Strictly increasing

```text
1 2 3 4 5
```

Duplicates are not allowed.

Condition:

```cpp
arr[i] > arr[i - 1]
```

---

# 46. Copy an Array

```cpp
for (int i = 0; i < n; i++) {
    copy[i] = arr[i];
}
```

Complexity:

```text
Time  = O(n)
Space = O(n)
```

because a second array is created.

---

# 47. In-Place vs Extra-Space Operations

### In-place

Modifies the original array.

Example:

```cpp
swap(arr[i], arr[j]);
```

Extra space:

```text
O(1)
```

### Extra array

Creates another array.

```cpp
int copy[n];
```

Extra space:

```text
O(n)
```

This distinction becomes very important in DSA interviews.

---

# 48. Passing Arrays to Functions

Example:

```cpp
void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
```

Call:

```cpp
int arr[] = {1, 2, 3, 4, 5};

printArray(arr, 5);
```

### Important correction

It is misleading to simply say:

> "An array is passed by reference."

For a built-in array parameter written as:

```cpp
void func(int arr[], int n)
```

the parameter is adjusted to a pointer type.

Conceptually:

```cpp
void func(int* arr, int n)
```

So the function receives access to the original array elements.

Therefore:

```cpp
arr[i] = 100;
```

inside the function changes the original array.

---

# 49. Modifying an Array in a Function

```cpp
void changeArr(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        arr[i] *= 2;
    }
}
```

Main:

```cpp
int arr[] = {1, 2, 3, 4, 5};

changeArr(arr, 5);
```

Array becomes:

```text
2 4 6 8 10
```

---
