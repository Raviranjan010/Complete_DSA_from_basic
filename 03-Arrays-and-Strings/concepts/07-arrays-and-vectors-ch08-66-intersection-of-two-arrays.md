[← Chapter 07](07-arrays-and-vectors-ch07-50-why-does-the-array-change.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 09 →](07-arrays-and-vectors-ch09-78-common-array-mistakes.md)

---

# 66. Intersection of Two Arrays

The uploaded file includes this as a practice problem.

Example:

```text
A = 1 2 3 4
B = 3 4 5 6
```

Intersection:

```text
3 4
```

### Important ambiguity

"Intersection" may mean:

1. distinct common values
2. common values respecting duplicates/multiset frequency

Example:

```text
A = 1 2 2 3
B = 2 2 4
```

Distinct intersection:

```text
2
```

Multiset intersection:

```text
2 2
```

Always clarify the intended definition.

---

# 67. Brute-Force Intersection

For distinct values, a simple approach can use nested loops plus duplicate checking.

Basic complexity can be:

```text
O(n × m)
```

where:

- `n` = size of first array
- `m` = size of second array

For larger constraints, hashing or sorting-based solutions are usually better.

---

# 68. Prefix Sum

## Definition

A **prefix sum array** stores cumulative sums.

For:

```text
arr = [2, 4, 1, 3, 5]
```

prefix sums:

```text
[2, 6, 7, 10, 15]
```

Because:

```text
2
2+4 = 6
2+4+1 = 7
2+4+1+3 = 10
2+4+1+3+5 = 15
```

---

# 69. Why Prefix Sum Is Important

Suppose we need many range-sum queries.

For example:

```text
sum from index 1 to 3
```

Without prefix sums, repeatedly summing can take:

```text
O(n)
```

With prefix sums, each range sum can be answered in:

```text
O(1)
```

after:

```text
O(n)
```

preprocessing.

---

# 70. Range Sum Formula

If:

```text
prefix[i] = arr[0] + ... + arr[i]
```

then:

```text
sum(l, r) = prefix[r] - prefix[l - 1]
```

when `l > 0`.

For `l = 0`:

```text
sum(0, r) = prefix[r]
```

A cleaner implementation often uses a prefix array of size `n + 1`:

```cpp
vector<long long> prefix(n + 1, 0);

for (int i = 0; i < n; i++) {
    prefix[i + 1] = prefix[i] + arr[i];
}
```

Then:

```cpp
sum(l, r) = prefix[r + 1] - prefix[l];
```

This avoids a special `l == 0` case.

---

# 71. Kadane's Algorithm — Maximum Subarray Sum

### Problem

Find the maximum sum of a contiguous subarray.

Example:

```text
[-2,1,-3,4,-1,2,1,-5,4]
```

Maximum-sum subarray:

```text
[4,-1,2,1]
```

Sum:

```text
6
```

A common implementation:

```cpp
long long current = arr[0];
long long best = arr[0];

for (int i = 1; i < n; i++) {

    current = max(1LL * arr[i], current + arr[i]);

    best = max(best, current);
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

This is one of the most important array algorithms for interviews.

---

# 72. Subarray vs Subsequence vs Subset

These are commonly confused.

## Subarray

Elements must be **contiguous**.

```text
[2, 3, 4]
```

from:

```text
1 2 3 4 5
```

is a subarray.

## Subsequence

Order is preserved, but elements do not need to be contiguous.

```text
1 3 5
```

is a subsequence of:

```text
1 2 3 4 5
```

## Subset

Order generally does not matter.

For:

```text
{1, 2, 3}
```

possible subsets include:

```text
{}
{1}
{2}
{1,3}
{1,2,3}
```

This distinction becomes very important in DSA.

---

# 73. Time Complexity of Common Array Operations

| Operation | Complexity |
|---|---:|
| Access by index | O(1) |
| Update by index | O(1) |
| Traverse | O(n) |
| Linear search | O(n) |
| Binary search | O(log n), sorted data required |
| Find min/max | O(n) |
| Reverse | O(n) |
| Copy | O(n) |
| Insert at end of fixed array if free position exists | O(1) |
| Insert at beginning | O(n) |
| Insert in middle | O(n) |
| Delete from beginning | O(n) |
| Delete from middle | O(n) |

---

# 74. Why Array Access Is O(1)

Suppose:

```text
arr = [10,20,30,40,50]
```

To access:

```cpp
arr[3]
```

we don't need to inspect:

```text
arr[0]
arr[1]
arr[2]
```

The address is calculated directly from the base address and index.

Therefore:

```text
arr[i] → O(1)
```

This is one of the biggest strengths of arrays.

---

# 75. Why Insertion at the Beginning Is O(n)

Suppose:

```text
10 20 30 40
```

Insert `5` at index `0`.

We must shift:

```text
10 → 1
20 → 2
30 → 3
40 → 4
```

Result:

```text
5 10 20 30 40
```

Potentially many elements must move.

Therefore:

```text
O(n)
```

---

# 76. Array vs Linked List

| Feature | Array | Linked List |
|---|---|---|
| Memory layout | Contiguous | Nodes can be non-contiguous |
| Random access | O(1) | O(n) |
| Search | O(n) generally | O(n) |
| Insert beginning | O(n) | O(1) with head |
| Delete beginning | O(n) | O(1) with head |
| Cache locality | Usually good | Usually weaker |
| Fixed built-in array size | Yes | Dynamic node structure |
| Extra pointer memory | No | Yes |

This comparison becomes important when you study linked lists.

---

# 77. Array vs `vector`

A built-in array:

```cpp
int arr[5];
```

has a fixed size.

A `vector`:

```cpp
vector<int> arr;
```

is a dynamic array abstraction.

Example:

```cpp
vector<int> arr = {1, 2, 3};

arr.push_back(4);
```

Now:

```text
1 2 3 4
```

For modern C++ DSA, `vector` is usually preferred when the size is determined at runtime.

---
