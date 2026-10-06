[← Chapter 08](10-arrays-and-vectors-intro-ch08-66-intersection-of-two-arrays.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 10 →](10-arrays-and-vectors-intro-ch10-83-practice-questions-searchin.md)

---

# 78. Common Array Mistakes

## Mistake 1 — Out-of-bounds access

For:

```cpp
int arr[5];
```

valid indices:

```text
0,1,2,3,4
```

This is invalid:

```cpp
arr[5]
```

---

## Mistake 2 — Loop boundary error

Wrong:

```cpp
for (int i = 0; i <= n; i++)
```

Correct:

```cpp
for (int i = 0; i < n; i++)
```

Because the last valid index is:

```text
n - 1
```

---

## Mistake 3 — Starting maximum at zero

This fails for an all-negative array.

Example:

```text
-5 -10 -2
```

If:

```cpp
int largest = 0;
```

you may incorrectly get:

```text
0
```

which isn't even in the array.

Prefer:

```cpp
int largest = arr[0];
```

for a non-empty array.

---

## Mistake 4 — Starting product at zero

Wrong:

```cpp
int product = 0;
```

Then:

```text
0 × anything = 0
```

Correct:

```cpp
long long product = 1;
```

---

## Mistake 5 — Binary search on an unsorted array

Binary search requires appropriate sorted ordering.

Do not apply binary search blindly to:

```text
8 2 10 1 5
```

---

## Mistake 6 — Forgetting empty-array cases

Code like:

```cpp
int smallest = arr[0];
```

requires at least one element.

If `n == 0`, there is no `arr[0]`.

Always understand the problem's constraints.

---

## Mistake 7 — Integer overflow

This can overflow:

```cpp
int sum = 0;
```

if the values and `n` are large.

Sometimes use:

```cpp
long long sum = 0;
```

depending on constraints.

---

# 79. Edge Cases You Must Check

Whenever solving an array problem, ask:

### Case 1 — Empty array

```text
[]
```

Is it allowed?

### Case 2 — One element

```text
[5]
```

### Case 3 — All equal

```text
[7,7,7,7]
```

### Case 4 — All negative

```text
[-5,-2,-10]
```

### Case 5 — All positive

```text
[1,5,9]
```

### Case 6 — Duplicate values

```text
[1,2,2,3]
```

### Case 7 — Already sorted

```text
[1,2,3,4,5]
```

### Case 8 — Reverse sorted

```text
[5,4,3,2,1]
```

### Case 9 — Target absent

```text
target = 100
```

### Case 10 — Target occurs multiple times

```text
[2,5,2,7,2]
```

These cases reveal many bugs.

---

# 80. Array Problem-Solving Checklist

Before coding, ask:

```text
1. Is the array sorted?
2. Are duplicates allowed?
3. Do I need the value or index?
4. Do I need first occurrence or last occurrence?
5. Is the answer based on contiguous elements?
6. Is extra space allowed?
7. Can I use hashing?
8. Can I use two pointers?
9. Can I use prefix sums?
10. Can I use binary search?
11. Are negative numbers possible?
12. Can values overflow int?
13. Can n be zero?
14. Is the result required modulo something?
15. What is the expected complexity?
```

---

# 81. Important Array Patterns

You should eventually recognize these patterns:

## Pattern 1 — Simple Traversal

```cpp
for (int i = 0; i < n; i++)
```

Used for:

- sum
- count
- min/max
- search
- frequency

---

## Pattern 2 — Two Pointers

```cpp
int left = 0;
int right = n - 1;
```

Used for:

- reverse
- pair problems
- sorted-array problems
- partitioning
- removing duplicates

---

## Pattern 3 — Sliding Window

Used for:

- subarray problems
- fixed-size windows
- longest/shortest valid ranges

---

## Pattern 4 — Prefix Sum

Used for:

- repeated range-sum queries
- subarray sum calculations
- cumulative information

---

## Pattern 5 — Hashing

Used for:

- frequency
- duplicates
- two-sum type problems
- distinct elements

---

## Pattern 6 — Binary Search

Used when:

- search space is ordered
- answer has a monotonic property
- sorted data is available
- "binary search on answer" is applicable

---

# 82. Practice Questions — Beginner

## Q1. Print all array elements

Input:

```text
5
10 20 30 40 50
```

Output:

```text
10 20 30 40 50
```

---

## Q2. Find the sum

Input:

```text
5
1 2 3 4 5
```

Output:

```text
15
```

---

## Q3. Find minimum

Input:

```text
5
8 3 10 2 6
```

Output:

```text
2
```

---

## Q4. Find maximum

Input:

```text
5
8 3 10 2 6
```

Output:

```text
10
```

---

## Q5. Count even numbers

Input:

```text
6
1 2 4 7 8 9
```

Output:

```text
3
```

---

## Q6. Count positive, negative, and zero

Input:

```text
7
-2 0 5 -1 0 8 3
```

Expected:

```text
Positive = 3
Negative = 2
Zero = 2
```

---
