[← Chapter 17](07-arrays-and-vectors-ch17-79-candidate-vs-verified-major.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md)

---

# 91. Pair Sum Pattern Recognition

When you see:

> "Find two numbers whose sum equals target"

Ask:

### Is the array sorted?

If yes:

```text
Two pointers
```

### Is it unsorted?

Consider:

```text
Hashing
```

### Are constraints tiny?

Brute force may be acceptable:

```text
O(n²)
```

### Do you need original indices?

Be careful if sorting because sorting changes positions.

---

# 92. Kadane Pattern Recognition

When you see:

> "Maximum sum of a contiguous subarray"

Think:

```text
Kadane's Algorithm
```

Keywords:

```text
maximum subarray
largest contiguous sum
maximum sum contiguous segment
```

---

# 93. XOR Pattern Recognition

When you see:

> Every number appears twice except one.

Think:

```text
XOR
```

Because:

```text
x ^ x = 0
x ^ 0 = x
```

---

# 94. Majority Element Pattern Recognition

When you see:

> Element appears more than n/2 times.

Think:

```text
Moore's Voting Algorithm
```

If no majority is guaranteed:

```text
candidate + verification
```

---

# 95. Questions You Must Be Able to Answer

## Vector Basics

1. What is a vector?
2. Why is vector called a dynamic array?
3. How is vector different from a built-in array?
4. What does `vector<int> v(5)` create?
5. What does `vector<int> v(5, 10)` create?
6. What is the difference between `size()` and `capacity()`?
7. What does `push_back()` do?
8. What does `pop_back()` do?
9. Does `pop_back()` return the removed value?
10. What does `front()` return?
11. What does `back()` return?
12. What happens when `at()` receives an invalid index?
13. What does `clear()` do?
14. Does `clear()` necessarily reduce capacity?
15. What does `empty()` do?
16. What does `reserve()` do?
17. Difference between `reserve()` and `resize()`?
18. What is reallocation?
19. Why can `push_back()` sometimes be O(n)?
20. Why is `push_back()` amortized O(1)?

---

# 96. Algorithm Questions

21. What is Kadane's Algorithm?
22. What problem does Kadane solve?
23. Why is brute-force maximum subarray O(n²)?
24. What does `current` represent in Kadane?
25. What does `best` represent?
26. Why should Kadane handle all-negative arrays carefully?
27. What is Pair Sum?
28. What is the brute-force complexity?
29. Why does two-pointer Pair Sum require sorting?
30. Why do we move `right` when sum is too large?
31. Why do we move `left` when sum is too small?
32. How can hashing solve Pair Sum in O(n) average time?
33. What is the space complexity of hashing Pair Sum?
34. What is a majority element?
35. Why is the threshold `> n/2`?
36. How does sorting help find majority?
37. What is Moore's Voting Algorithm?
38. Why does cancellation work?
39. What is the difference between a candidate and a verified majority?
40. When should Moore's result be verified?

---

# 97. Coding Questions — Easy

### Q1. Create an empty vector and add five numbers using `push_back()`.

### Q2. Print the vector using a normal `for` loop.

### Q3. Print the vector using a range-based loop.

### Q4. Print first and last elements.

### Q5. Remove the last element.

### Q6. Insert `100` at index `2`.

### Q7. Delete the element at index `3`.

### Q8. Find the minimum element.

### Q9. Find the maximum element.

### Q10. Find the sum of all elements.

---

# 98. Coding Questions — Intermediate

### Q11. Reverse a vector in-place.

### Q12. Find the first occurrence of a target.

### Q13. Find the last occurrence.

### Q14. Count target frequency.

### Q15. Move all zeros to the end.

### Q16. Find the second largest distinct element.

### Q17. Check whether a vector is sorted.

### Q18. Find duplicate elements.

### Q19. Find the unique element using XOR.

### Q20. Rotate a vector left by `k`.

---

# 99. Coding Questions — Advanced

### Q21. Maximum subarray sum using brute force.

### Q22. Maximum subarray sum using Kadane.

### Q23. Return the actual maximum-sum subarray.

### Q24. Two Sum using nested loops.

### Q25. Two Sum using hashing.

### Q26. Two Sum on sorted array using two pointers.

### Q27. Find majority element using brute force.

### Q28. Find majority element using sorting.

### Q29. Find majority element using Moore's Voting.

### Q30. Find majority element and verify whether it actually exists.

---

# 100. Final Mental Map

```text
VECTOR
│
├── Dynamic sequence
│
├── Creation
│   ├── vector<int> v;
│   ├── vector<int> v = {};
│   ├── vector<int> v(5);
│   ├── vector<int> v(5, 10);
│   └── vector<int> v = {1,2,3};
│
├── Access
│   ├── []
│   ├── at()
│   ├── front()
│   └── back()
│
├── Modification
│   ├── push_back()
│   ├── pop_back()
│   ├── insert()
│   ├── erase()
│   ├── clear()
│   └── resize()
│
├── Memory
│   ├── size()
│   ├── capacity()
│   ├── reserve()
│   └── reallocation
│
└── DSA Patterns
    ├── XOR
    ├── Kadane
    ├── Two Pointers
    ├── Hashing
    └── Moore's Voting
```

---

# 101. Final Complexity Cheat Sheet

```text
Vector access              → O(1)
Vector size                → O(1)
Vector front/back          → O(1)
push_back                  → amortized O(1)
pop_back                   → O(1)
middle insertion           → O(n)
middle deletion            → O(n)

Brute-force Pair Sum       → O(n²)
Hashing Pair Sum           → O(n) average, O(n) space
Sorted Two-Pointer PairSum → O(n), O(1) extra space

Brute-force Max Subarray   → O(n²)
Kadane                     → O(n), O(1)

Brute-force Majority       → O(n²)
Sorting Majority           → O(n log n)
Moore's Voting             → O(n), O(1)

XOR unique-element problem → O(n), O(1)
```

---

# 102. The Most Important Things to Remember

```text
1. Vector = dynamic sequence container.
2. size = actual number of elements.
3. capacity = allocated storage available for elements.
4. reserve() changes capacity, not size.
5. resize() changes size.
6. push_back() is amortized O(1), not guaranteed O(1) every time.
7. at() performs bounds checking.
8. [] does not perform bounds checking.
9. pop_back() removes the last element and returns nothing.
10. x ^ x = 0.
11. x ^ 0 = x.
12. Kadane = maximum contiguous subarray sum.
13. Two pointers Pair Sum requires sorted data.
14. Hashing Pair Sum works on unsorted data in O(n) average time.
15. Majority = frequency > n/2.
16. Moore's Voting = O(n) time and O(1) extra space.
17. Moore's candidate must be verified if majority existence is not guaranteed.
18. Pass large vectors using const reference when you only need to read them.
19. Always inspect constraints before choosing an algorithm.
20. Do not memorize code without understanding the pattern.
```

---

# 103. Recommended Study Sequence

Study these concepts in this exact order:

```text
Vector basics
    ↓
size vs capacity
    ↓
push_back / pop_back
    ↓
front / back / at
    ↓
insert / erase
    ↓
clear / empty
    ↓
resize / reserve
    ↓
iterators
    ↓
sorting
    ↓
XOR problems
    ↓
Brute-force subarray problems
    ↓
Kadane's Algorithm
    ↓
Pair Sum brute force
    ↓
Pair Sum hashing
    ↓
Pair Sum two pointers
    ↓
Majority brute force
    ↓
Majority sorting
    ↓
Moore's Voting
    ↓
Mixed array problems
```

> **DSA rule:** First understand the brute-force solution, then identify what repeated work is happening, and finally optimize it using the correct pattern. This is how you move from `O(n²)` to `O(n)` instead of merely memorizing an "optimal" code template.
