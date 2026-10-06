[← Chapter 09](07-arrays-and-vectors-ch09-78-common-array-mistakes.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 11 →](07-arrays-and-vectors-ch11-91-practice-questions-2d-array.md)

---

# 83. Practice Questions — Searching

## Q7. Linear search

Find the index of `30`:

```text
10 20 30 40 50
```

Expected:

```text
2
```

---

## Q8. Search for a missing value

```text
Array = 10 20 30 40
Target = 50
```

Expected:

```text
-1
```

---

## Q9. First occurrence

```text
Array = 2 5 2 7 2
Target = 2
```

Expected:

```text
0
```

---

## Q10. Last occurrence

Same array:

```text
2 5 2 7 2
```

Expected:

```text
4
```

---

## Q11. Count occurrences

```text
Array = 1 2 2 3 2 4
Target = 2
```

Expected:

```text
3
```

---

# 84. Practice Questions — Reverse & Manipulation

## Q12. Reverse an array

Input:

```text
1 2 3 4 5
```

Output:

```text
5 4 3 2 1
```

Constraint:

> Do it in-place.

---

## Q13. Swap minimum and maximum

Input:

```text
5 2 9 1 7
```

Output:

```text
5 2 1 9 7
```

---

## Q14. Left rotate by one

Input:

```text
1 2 3 4 5
```

Output:

```text
2 3 4 5 1
```

---

## Q15. Right rotate by one

Input:

```text
1 2 3 4 5
```

Output:

```text
5 1 2 3 4
```

---

# 85. Practice Questions — Duplicates & Uniqueness

## Q16. Print elements occurring exactly once

Input:

```text
1 2 2 3 4 4 5
```

Output:

```text
1 3 5
```

---

## Q17. Print each distinct value once

Input:

```text
1 2 2 3 4 4 5
```

Output:

```text
1 2 3 4 5
```

---

## Q18. Find duplicate values

Input:

```text
1 2 3 2 4 1
```

Expected duplicate values:

```text
1 2
```

---

# 86. Practice Questions — Sorted Arrays

## Q19. Check whether array is sorted

Input:

```text
1 2 3 4 5
```

Output:

```text
Sorted
```

---

## Q20. Check non-decreasing order

Input:

```text
1 2 2 3 4
```

Output:

```text
Sorted
```

---

## Q21. Check strictly increasing order

Input:

```text
1 2 2 3
```

Output:

```text
Not strictly increasing
```

---

# 87. Practice Questions — Intermediate

## Q22. Find second largest distinct element

Input:

```text
10 5 20 8 20
```

Expected:

```text
10
```

---

## Q23. Move all zeros to the end

Input:

```text
0 1 0 3 12
```

Expected:

```text
1 3 12 0 0
```

Try to solve in:

```text
O(n) time
O(1) extra space
```

---

## Q24. Find missing number

Numbers are from `0` to `n`.

Input:

```text
0 1 3 4
```

Expected:

```text
2
```

---

## Q25. Find intersection

```text
A = 1 2 3 4
B = 3 4 5 6
```

Expected:

```text
3 4
```

---

## Q26. Find union of two arrays

```text
A = 1 2 3
B = 2 3 4
```

Distinct union:

```text
1 2 3 4
```

---

# 88. Practice Questions — Prefix Sum

## Q27. Build prefix sum

Input:

```text
2 4 1 3 5
```

Expected:

```text
2 6 7 10 15
```

---

## Q28. Range sum

Array:

```text
2 4 1 3 5
```

Find sum from index `1` to `3`.

Calculation:

```text
4 + 1 + 3 = 8
```

Expected:

```text
8
```

---

# 89. Practice Questions — Two Pointers

## Q29. Reverse in-place

Constraint:

```text
Do not create another array.
```

---

## Q30. Two Sum in Sorted Array

Given:

```text
1 2 4 6 8 9
```

Target:

```text
10
```

Find two elements whose sum is `10`.

Expected pair:

```text
2 + 8
```

A two-pointer approach can solve this in:

```text
O(n)
```

because the array is sorted.

---

# 90. Practice Questions — Subarrays

## Q31. Maximum subarray sum

Input:

```text
-2 1 -3 4 -1 2 1 -5 4
```

Expected:

```text
6
```

---

## Q32. Print all subarrays

Input:

```text
1 2 3
```

Subarrays:

```text
[1]
[1,2]
[1,2,3]
[2]
[2,3]
[3]
```

Number of non-empty subarrays:

```text
n(n+1)/2
```

For `n = 3`:

```text
3 × 4 / 2 = 6
```

---
