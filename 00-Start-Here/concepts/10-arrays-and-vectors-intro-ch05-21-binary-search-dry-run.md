[← Chapter 04](10-arrays-and-vectors-intro-ch04-4-array-indexing.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 06 →](10-arrays-and-vectors-intro-ch06-36-swapping-maximum-and-minimu.md)

---

# 21. Binary Search Dry Run

Array:

```text
1 3 5 7 9 11 13
```

Target:

```text
9
```

Initial:

```text
low = 0
high = 6
mid = 3
```

```text
arr[mid] = 7
```

Since:

```text
9 > 7
```

ignore the left half.

Now:

```text
low = 4
high = 6
```

Middle:

```text
arr[5] = 11
```

Since:

```text
9 < 11
```

search left.

Now:

```text
low = 4
high = 4
```

`arr[4] = 9`

Found.

---

# 22. Binary Search Complexity

```text
Best case  = O(1)
Worst case = O(log n)
Average    = O(log n)
Space      = O(1) for iterative implementation
```

---

# 23. Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|---|---|---|
| Requires sorted array? | No | Yes |
| Approach | Sequential | Divide and conquer |
| Worst-case | O(n) | O(log n) |
| Easy to implement | Yes | Moderate |
| Works on unsorted array | Yes | No |
| Good for small arrays | Yes | Yes |
| Good for large sorted arrays | Sometimes | Excellent |

---

# 24. Minimum Element

A common array problem is finding the smallest element.

### Approach

Start with the first element:

```cpp
int smallest = arr[0];
```

Then compare every element:

```cpp
for (int i = 1; i < n; i++) {

    if (arr[i] < smallest) {
        smallest = arr[i];
    }
}
```

### Why start with `arr[0]`?

Because it guarantees that the initial value actually belongs to the array.

---

# 25. Using `INT_MAX`

Another approach:

```cpp
int smallest = INT_MAX;

for (int i = 0; i < n; i++) {
    if (arr[i] < smallest) {
        smallest = arr[i];
    }
}
```

`INT_MAX` is larger than every representable `int` value.

Therefore the first array element will replace it.

### Header

Use:

```cpp
#include <climits>
```

for `INT_MAX` and `INT_MIN`.

### Preferred beginner approach

```cpp
int smallest = arr[0];
```

is often simpler and also handles the important idea that the array must be non-empty.

---

# 26. Maximum Element

```cpp
int largest = arr[0];

for (int i = 1; i < n; i++) {

    if (arr[i] > largest) {
        largest = arr[i];
    }
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

---

# 27. `INT_MIN` and `INT_MAX`

You can use:

```cpp
INT_MIN
```

as an initial value for maximum.

And:

```cpp
INT_MAX
```

as an initial value for minimum.

Example:

```cpp
int largest = INT_MIN;
int smallest = INT_MAX;
```

But for a non-empty array, this is often simpler:

```cpp
int largest = arr[0];
int smallest = arr[0];
```

---

# 28. Sum of Array Elements

### Problem

Find the sum of all elements.

```cpp
int sum = 0;

for (int i = 0; i < n; i++) {
    sum += arr[i];
}

cout << sum;
```

Example:

```text
Array: 1 2 3 4 5

sum = 1 + 2 + 3 + 4 + 5
    = 15
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 29. Product of Array Elements

```cpp
long long product = 1;

for (int i = 0; i < n; i++) {
    product *= arr[i];
}
```

### Why `1`?

Because `1` is the multiplicative identity:

```text
1 × x = x
```

Starting with `0` would make the entire product zero.

### Important

Use a sufficiently large integer type if the product can exceed `int`.

Even `long long` can overflow for sufficiently large products.

---

# 30. Count Even and Odd Elements

```cpp
int even = 0;
int odd = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] % 2 == 0)
        even++;
    else
        odd++;
}
```

---

# 31. Count Positive, Negative, and Zero

```cpp
int positive = 0;
int negative = 0;
int zero = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] > 0)
        positive++;
    else if (arr[i] < 0)
        negative++;
    else
        zero++;
}
```

---

# 32. Reverse an Array

## Definition

Reversing an array means changing:

```text
1 2 3 4 5
```

into:

```text
5 4 3 2 1
```

The uploaded material uses the correct **two-pointer/in-place** approach.

---

# 33. Two-Pointer Reverse

```cpp
void reverseArr(int arr[], int n) {

    int start = 0;
    int end = n - 1;

    while (start < end) {

        swap(arr[start], arr[end]);

        start++;
        end--;
    }
}
```

### Dry Run

Array:

```text
1 2 3 4 5
```

Initial:

```text
start = 0
end   = 4
```

Swap:

```text
5 2 3 4 1
```

Move:

```text
start = 1
end = 3
```

Swap:

```text
5 4 3 2 1
```

Move:

```text
start = 2
end = 2
```

Stop.

---

# 34. Why `start < end`?

We only need to swap pairs until the pointers meet.

If:

```text
start == end
```

there is a single middle element, which does not need swapping.

Therefore:

```cpp
while (start < end)
```

is the correct condition.

---

# 35. Reverse Complexity

```text
Time  = O(n)
Space = O(1)
```

It is an **in-place** reversal because no second array is created.

---
