# 📘 DSA — Time & Space Complexity

## 1. What Is Time Complexity?

**Time Complexity** is the amount of computational work performed by an algorithm as a function of the input size `n`.

It does **not** mean the actual time in seconds.

Example:

```cpp
for(int i = 0; i < n; i++) {
    cout << i;
}
```

The loop runs `n` times:

```text
Time Complexity = O(n)
```

### Why don't we use actual seconds?

Actual execution time depends on:

- CPU
- RAM
- compiler
- compiler optimization
- operating system
- programming language
- machine load

Therefore, DSA focuses on **growth with input size**.

---

# 2. What Is `n`?

`n` generally represents the **input size**.

For an array:

```cpp
int arr[n];
```

```text
n = number of elements
```

For a string:

```text
n = length of string
```

For an `n × n` matrix:

```text
number of elements = n²
```

For a graph:

```text
V = number of vertices
E = number of edges
```

---

# 3. Big-O, Big-Omega and Big-Theta

A common shortcut is:

```text
Worst case  → O
Average case → Θ
Best case   → Ω
```

This is an oversimplification.

These notations describe **mathematical bounds**, while best/average/worst describe **cases**.

## Big-O — `O()`

Big-O represents an **asymptotic upper bound**.

In normal DSA discussions, Big-O is commonly used to state worst-case complexity.

Example:

```text
Linear Search
Worst Case → O(n)
```

## Big-Omega — `Ω()`

Omega represents an **asymptotic lower bound**.

Example:

```text
Linear Search
Best Case → Ω(1)
```

## Big-Theta — `Θ()`

Theta represents a **tight asymptotic bound**.

If an algorithm has both an `O(n)` upper bound and an `Ω(n)` lower bound, its tight bound is:

```text
Θ(n)
```

### Remember

```text
O(f(n))  → Upper Bound
Ω(f(n))  → Lower Bound
Θ(f(n))  → Tight Bound
```

Best, average, and worst case are separate forms of case analysis.

---

# 4. Space Complexity

**Space Complexity** is the amount of memory an algorithm requires as a function of input size `n`.

Example:

```cpp
int sum = 0;

for(int i = 0; i < n; i++) {
    sum += arr[i];
}
```

Only a few variables are used, so:

```text
Auxiliary Space = O(1)
```

## Auxiliary Space

Extra memory used by the algorithm apart from the input.

Example:

```cpp
vector<int> temp(n);
```

requires:

```text
Auxiliary Space = O(n)
```

---

# 5. Complexity Order

Generally:

```text
O(1)
    ↓
O(log n)
    ↓
O(n)
    ↓
O(n log n)
    ↓
O(n²)
    ↓
O(n³)
    ↓
O(2ⁿ)
    ↓
O(n!)
```

For large inputs, slower-growing complexity is generally more scalable.

---

# 6. O(1) — Constant Complexity

Example:

```cpp
int x = arr[5];
```

Accessing a known array index takes constant work:

```text
O(1)
```

It does not depend on the number of elements in the array.

---

# 7. O(n) — Linear Complexity

Example:

```cpp
for(int i = 0; i < n; i++) {
    cout << arr[i];
}
```

The loop executes:

```text
n times
```

Therefore:

```text
Time Complexity = O(n)
```

Common examples:

- Linear Search
- Kadane's Algorithm
- Moore's Voting Algorithm
- Two-pointer traversal
- Finding maximum/minimum

---

# 8. O(log n) — Logarithmic Complexity

Binary Search is the classic example.

Suppose:

```text
n = 16
```

The search space becomes:

```text
16
↓
8
↓
4
↓
2
↓
1
```

Number of steps:

```text
4
```

And:

```text
log₂(16) = 4
```

Therefore:

```text
Binary Search = O(log n)
```

---

# 9. Binary Search Derivation

Initially:

```text
n
```

After one iteration:

```text
n / 2
```

After two:

```text
n / 2²
```

After `x` iterations:

```text
n / 2ˣ
```

Eventually:

```text
n / 2ˣ = 1
```

Therefore:

```text
n = 2ˣ
```

Taking log base 2:

```text
log₂(n) = x
```

So:

```text
x = log₂(n)
```

Hence:

```text
Binary Search = O(log n)
```

---

# 10. Correct Binary Search Code

```cpp
int s = 0;
int e = n - 1;

while(s <= e) {

    int mid = s + (e - s) / 2;

    if(arr[mid] < target) {
        s = mid + 1;
    }

    else if(arr[mid] > target) {
        e = mid - 1;
    }

    else {
        return mid;
    }
}

return -1;
```

## Important Correction

Incorrect:

```cpp
if(arr[mid] < target) {
    s = mid - 1;
}
```

Correct:

```cpp
s = mid + 1;
```

### Why?

If:

```text
arr[mid] < target
```

the target must be to the **right** of `mid`.

Therefore:

```text
left = mid + 1
```

If:

```text
arr[mid] > target
```

the target must be to the **left**:

```text
right = mid - 1
```

### Requirement

Classic binary search requires a **sorted array**.

---

# 11. Factorial

Mathematically:

```text
n! = n × (n-1) × (n-2) × ... × 1
```

Example:

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

## Iterative Factorial

```cpp
int fact = 1;

for(int i = 1; i <= n; i++) {
    fact *= i;
}
```

The loop executes `n` times.

Therefore:

```text
Time Complexity = O(n)
```

### Very Important Distinction

The **result** grows as:

```text
n!
```

but the **algorithm** performs:

```text
n iterations
```

Therefore:

```text
Factorial value       → n!
Iterative calculation → O(n)
```

Do not confuse mathematical output growth with algorithmic running time.

---

# 12. Fibonacci Using Dynamic Programming

Fibonacci sequence:

```text
0 1 1 2 3 5 8 13 21 ...
```

Formula:

```text
F(n) = F(n-1) + F(n-2)
```

DP implementation:

```cpp
vector<int> dp(n + 1);

dp[0] = 0;
dp[1] = 1;

for(int i = 2; i <= n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
}
```

The loop executes approximately `n` times:

```text
Time = O(n)
```

The DP array stores `n + 1` values:

```text
Space = O(n)
```

---

# 13. Fibonacci Space Optimization

To calculate the next Fibonacci value, we only need the previous two values.

```cpp
int prev2 = 0;
int prev1 = 1;

for(int i = 2; i <= n; i++) {

    int curr = prev1 + prev2;

    prev2 = prev1;
    prev1 = curr;
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

This is an important example of **space optimization in DP**.

---

# 14. Kadane's Algorithm

## Problem

Find the maximum sum of a **contiguous subarray**.

Example:

```text
[-2, 3, -1, 5, -6]
```

Best subarray:

```text
[3, -1, 5]
```

Sum:

```text
7
```

---

# 15. Kadane's Code

```cpp
int currSum = 0;
int ans = INT_MIN;

for(int i = 0; i < n; i++) {

    currSum += arr[i];

    ans = max(currSum, ans);

    currSum = currSum < 0 ? 0 : currSum;
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

---

# 16. Why Does Kadane Reset a Negative Sum?

Suppose:

```text
currSum = -10
```

and the next element is:

```text
20
```

Continuing:

```text
-10 + 20 = 10
```

Starting fresh:

```text
20
```

is better.

Therefore, when:

```text
currSum < 0
```

we discard the previous prefix:

```cpp
currSum = 0;
```

### Core idea

```text
Negative prefix
      ↓
Hurts future sum
      ↓
Discard it
      ↓
Start fresh
```

---

# 17. Kadane Edge Case

Consider:

```text
[-5, -2, -8]
```

Maximum non-empty subarray:

```text
[-2]
```

Answer:

```text
-2
```

not:

```text
0
```

Therefore:

```cpp
ans = INT_MIN;
```

is important in the standard implementation when the subarray must be non-empty.

---

# 18. Bubble Sort

## Definition

Bubble Sort repeatedly compares **adjacent elements** and swaps them if they are in the wrong order.

Example:

```text
5 3 4 1
```

Compare:

```text
5 and 3
```

Swap:

```text
3 5 4 1
```

Then:

```text
5 and 4
```

Swap:

```text
3 4 5 1
```

Then:

```text
5 and 1
```

Swap:

```text
3 4 1 5
```

The largest element has moved to the end.

---

# 19. Bubble Sort Code

```cpp
for(int i = 0; i < n - 1; i++) {

    for(int j = 0; j < n - i - 1; j++) {

        if(arr[j] > arr[j + 1]) {
            swap(arr[j], arr[j + 1]);
        }
    }
}
```

---

# 20. Bubble Sort Complexity Derivation

Suppose:

```text
n = 4
```

Pass 1:

```text
3 comparisons
```

Pass 2:

```text
2 comparisons
```

Pass 3:

```text
1 comparison
```

Total:

```text
3 + 2 + 1 = 6
```

For general `n`:

```text
(n-1) + (n-2) + ... + 2 + 1
```

Using:

```text
1 + 2 + ... + k = k(k+1)/2
```

with:

```text
k = n - 1
```

we get:

```text
n(n-1)/2
```

Expand:

```text
(n² - n)/2
```

Ignore the constant:

```text
n² - n
```

The dominant term is:

```text
n²
```

Therefore:

```text
Bubble Sort = O(n²)
```

---

# 21. Important Correction

A common incorrect conclusion is:

```text
n² - n ≈ n
```

Therefore:

```text
O(n)
```

This is wrong.

For large `n`, `n²` dominates `n`.

Example:

```text
n = 1000

n² = 1,000,000
n  = 1,000
```

Therefore:

```text
n² - n = O(n²)
```

---

# 22. Bubble Sort Complexity

For the basic implementation:

```text
Best Case    = O(n²)
Average Case = O(n²)
Worst Case   = O(n²)
Space        = O(1)
```

Why is the basic best case still `O(n²)`?

Because the nested loops continue making comparisons even when the array is already sorted.

---

# 23. Optimized Bubble Sort

We can stop early if no swap happens.

```cpp
for(int i = 0; i < n - 1; i++) {

    bool swapped = false;

    for(int j = 0; j < n - i - 1; j++) {

        if(arr[j] > arr[j + 1]) {

            swap(arr[j], arr[j + 1]);

            swapped = true;
        }
    }

    if(!swapped)
        break;
}
```

Now:

```text
Best Case    = O(n)
Average Case = O(n²)
Worst Case   = O(n²)
```

---

# 24. Selection Sort

## Definition

Selection Sort repeatedly finds the **minimum element** from the unsorted portion and places it at the current position.

Example:

```text
5 3 4 1
```

Find minimum:

```text
1
```

Swap with first position:

```text
1 3 4 5
```

Continue with the remaining unsorted portion.

---

# 25. Selection Sort Code

```cpp
for(int i = 0; i < n - 1; i++) {

    int minIdx = i;

    for(int j = i + 1; j < n; j++) {

        if(arr[j] < arr[minIdx]) {
            minIdx = j;
        }
    }

    swap(arr[i], arr[minIdx]);
}
```

---

# 26. Selection Sort Complexity Derivation

For:

```text
n = 5
```

When `i = 0`:

```text
4 comparisons
```

When `i = 1`:

```text
3 comparisons
```

Then:

```text
2
1
```

Total:

```text
4 + 3 + 2 + 1
```

General:

```text
(n-1) + (n-2) + ... + 1
```

Using:

```text
n(n-1)/2
```

Therefore:

```text
Selection Sort = O(n²)
```

---

# 27. Selection Sort Complexity

Standard Selection Sort:

```text
Best Case    = O(n²)
Average Case = O(n²)
Worst Case   = O(n²)
Space        = O(1)
```

Even if the array is already sorted, the algorithm still scans the remaining unsorted portion.

---

# 28. Bubble Sort vs Selection Sort

| Feature | Bubble Sort | Selection Sort |
|---|---|---|
| Main idea | Swap adjacent elements | Select minimum |
| Best basic | O(n²) | O(n²) |
| Best optimized Bubble | O(n) | O(n²) |
| Average | O(n²) | O(n²) |
| Worst | O(n²) | O(n²) |
| Extra space | O(1) | O(1) |
| Stable | Yes | Usually no |
| In-place | Yes | Yes |

---

# 29. Common Loop Patterns

## Linear Loop

```cpp
for(int i = 0; i < n; i++)
```

```text
O(n)
```

## Nested Linear Loops

```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
    }
}
```

```text
O(n²)
```

## Triple Nested Loops

```cpp
for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)
        for(int k = 0; k < n; k++)
```

```text
O(n³)
```

## Doubling

```cpp
for(int i = 1; i < n; i *= 2)
```

```text
O(log n)
```

## Halving

```cpp
for(int i = n; i > 0; i /= 2)
```

```text
O(log n)
```

---

# 30. Sequential vs Nested Loops

## Sequential

```cpp
for(int i = 0; i < n; i++) {
}

for(int i = 0; i < n; i++) {
}
```

Work:

```text
n + n
= 2n
= O(n)
```

## Nested

```cpp
for(int i = 0; i < n; i++) {

    for(int j = 0; j < n; j++) {
    }
}
```

Work:

```text
n × n
= n²
= O(n²)
```

### Mental Rule

```text
Sequential → Add
Nested     → Multiply
```

This is a useful starting rule, but always inspect the actual bounds.

---

# 31. Different Input Sizes

```cpp
for(int i = 0; i < n; i++) {

    for(int j = 0; j < m; j++) {
    }
}
```

Complexity:

```text
O(nm)
```

Not automatically:

```text
O(n²)
```

unless:

```text
m = n
```

---

# 32. Constant Inner Loop

```cpp
for(int i = 0; i < n; i++) {

    for(int j = 0; j < 10; j++) {
    }
}
```

Work:

```text
10n
```

Drop the constant:

```text
O(n)
```

---

# 33. Removing Constants

Suppose:

```text
T(n) = 5n² + 3n + 10
```

The dominant term is:

```text
n²
```

Therefore:

```text
O(n²)
```

---

# 34. Removing Lower-Order Terms

Suppose:

```text
T(n) = n² + 5n + 20
```

For large `n`, `n²` dominates.

Therefore:

```text
O(n²)
```

---

# 35. Complexity Cheat Sheet

| Complexity | Example |
|---|---|
| O(1) | Array access |
| O(log n) | Binary Search |
| O(n) | Linear Search |
| O(n) | Kadane |
| O(n) | Moore Voting |
| O(n) | Two Pointer |
| O(n log n) | Merge Sort |
| O(n²) | Bubble Sort |
| O(n²) | Selection Sort |
| O(n³) | Three nested loops |
| O(2ⁿ) | Naive recursive Fibonacci |
| O(n!) | Permutation brute force |

---

# 36. Common Mistakes

## Mistake 1

Thinking:

```text
Factorial result = n!
Therefore algorithm = O(n!)
```

Wrong.

```text
Iterative factorial = O(n)
```

---

## Mistake 2

Thinking:

```text
n² - n ≈ n
```

Wrong.

```text
n² - n = O(n²)
```

---

## Mistake 3

Thinking:

```text
Θ = average case
```

Wrong.

Theta means:

```text
tight asymptotic bound
```

---

## Mistake 4

Using:

```cpp
s = mid - 1;
```

when:

```text
arr[mid] < target
```

Correct:

```cpp
s = mid + 1;
```

---

## Mistake 5

Thinking every three-loop program is `O(n³)`.

Always inspect the actual loop limits.

---

# 37. Complexity Analysis Checklist

When given code:

### Step 1
Identify what `n` represents.

### Step 2
Count how many times each loop executes.

### Step 3
Check how loop variables change:

```text
i++
i--
i *= 2
i /= 2
```

### Step 4
Determine whether loops are:

```text
Sequential
```

or:

```text
Nested
```

### Step 5
Add sequential work.

### Step 6
Multiply nested work.

### Step 7
Remove constants.

### Step 8
Remove lower-order terms.

### Step 9
Keep the dominant term.

### Step 10
Analyze extra memory separately.

---

# 38. Practice Questions

## Basic

### Q1
Find the complexity:

```cpp
for(int i = 0; i < n; i++) {
}
```

Answer:

```text
O(n)
```

### Q2

```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
    }
}
```

Answer:

```text
O(n²)
```

### Q3

```cpp
for(int i = 1; i < n; i *= 2) {
}
```

Answer:

```text
O(log n)
```

### Q4

```cpp
for(int i = 0; i < n; i++) {
}

for(int i = 0; i < n; i++) {
}
```

Answer:

```text
O(n)
```

because:

```text
O(n) + O(n)
= O(2n)
= O(n)
```

### Q5

```cpp
for(int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
    }
}
```

Total work:

```text
0 + 1 + 2 + ... + (n-1)
```

Therefore:

```text
O(n²)
```

---

# 39. Intermediate Questions

1. Derive the number of comparisons in Bubble Sort.
2. Explain why Selection Sort is `O(n²)` even when the array is sorted.
3. Explain why Binary Search is `O(log n)`.
4. Explain the difference between `O`, `Ω`, and `Θ`.
5. Explain the difference between best, average, and worst case.
6. Find time and space complexity of Fibonacci DP.
7. Optimize Fibonacci space from `O(n)` to `O(1)`.
8. Explain why Kadane's Algorithm works.
9. Find complexity:

```cpp
for(int i = 1; i < n; i *= 2)
    for(int j = 0; j < n; j++) {
    }
```

Answer:

```text
O(n log n)
```

10. Find complexity:

```cpp
for(int i = 0; i < n; i++)
    for(int j = 1; j < n; j *= 2) {
    }
```

Answer:

```text
O(n log n)
```

---

# 40. Interview Questions

1. What is Time Complexity?
2. What is Space Complexity?
3. What is Big-O?
4. What is Big-Omega?
5. What is Big-Theta?
6. Are Big-O and worst case exactly the same concept?
7. Why do we ignore constants?
8. Why do we ignore lower-order terms?
9. Why is Binary Search `O(log n)`?
10. Why is Bubble Sort `O(n²)`?
11. Why is Selection Sort `O(n²)`?
12. Why is iterative factorial `O(n)`?
13. Why is naive recursive Fibonacci exponential?
14. How does DP improve Fibonacci?
15. How can Fibonacci space be reduced from `O(n)` to `O(1)`?
16. Why does Kadane use `O(1)` extra space?
17. What is the difference between input and auxiliary space?
18. What is the complexity of nested loops with bounds `n` and `m`?
19. What happens when a loop variable doubles each iteration?
20. How do you analyze mixed sequential and nested loops?

---

# 41. Must-Know Takeaways

```text
Time Complexity
→ Growth of computational work

Space Complexity
→ Growth of memory usage

O
→ Upper asymptotic bound

Ω
→ Lower asymptotic bound

Θ
→ Tight asymptotic bound

Factorial loop
→ O(n)

Fibonacci DP
→ O(n) time
→ O(n) space
→ O(1) space with optimization

Kadane
→ O(n) time
→ O(1) extra space

Binary Search
→ O(log n)
→ Sorted data required

Bubble Sort
→ O(n²) basic
→ O(n) best with early-exit optimization

Selection Sort
→ O(n²)

Sequential work
→ Add

Nested work
→ Multiply

Loop ×2 / ÷2
→ Usually O(log n)

n² - n
→ O(n²)

Dominant term
→ Determines asymptotic growth
```

---

# 42. Final Mental Model

```text
Given Code
    ↓
Identify n
    ↓
Analyze every loop
    ↓
How does the variable change?
    ├── +1 / -1 → usually linear
    ├── ×2 / ÷2 → usually logarithmic
    └── nested   → multiply work
    ↓
Sequential sections → add
    ↓
Write mathematical expression
    ↓
Remove constants
    ↓
Remove lower-order terms
    ↓
Keep dominant term
    ↓
Final Time Complexity
    ↓
Analyze extra memory
    ↓
Final Space Complexity
```

> **Core DSA skill:** Never classify complexity from the number of loops alone. Analyze how many times each loop actually executes. A single loop can be `O(log n)`, two nested loops can be `O(n log n)`, and a three-level-looking structure can still be `O(n²)` if one loop is constant-sized.


---

## Supplementary Mastery Notes from DSA MasterCourse

# 01 — Complexity Analysis — Complete Notes

> **What You'll Learn**: Big-O notation, time/space complexity, amortized analysis, and how to analyze any algorithm  
> **Prerequisites**: Basic C++ programming (Topic 00)  
> **Time Required**: 1 week (10-12 hours)

---

## 1. What is Complexity Analysis? (Real-World Analogy)

Imagine you're planning a road trip:

- **Time Complexity** = How long will the trip take? (1 hour? 10 hours?)
- **Space Complexity** = How much fuel/gas do you need? (5 liters? 50 liters?)

Now imagine two routes:
- **Route A**: 100 km, takes 2 hours, uses 10L fuel
- **Route B**: 500 km, takes 10 hours, uses 50L fuel

Which is better? **Route A**, obviously! But how do we know without actually driving?

**Complexity analysis** is like a GPS that tells us:
- How fast an algorithm runs **before** we run it
- How much memory it uses **before** we execute it
- Which algorithm is better for large inputs

💡 **TRICK**: Think of complexity as the **"nutrition label"** for algorithms — it tells you what you're getting before you consume it!

---

## 2. Why Do We Need Complexity Analysis?

### Problem: Measuring actual time is unreliable!

```cpp
// Algorithm 1: Find element in array
for(int i = 0; i < n; i++) {
    if(arr[i] == target) return i;
}

// Algorithm 2: Find element using binary search (sorted array)
int left = 0, right = n-1;
while(left <= right) {
    int mid = left + (right - left) / 2;
    if(arr[mid] == target) return mid;
    else if(arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}
```

**Which is faster?**  
If you measure with a stopwatch:
- Depends on your computer speed
- Depends on other running programs
- Depends on input data
- **Cannot compare fairly!**

**Solution**: Count operations mathematically → **Big-O notation**

### Real Reasons:
1. **Predict Performance**: Know how algorithm scales with large inputs
2. **Compare Algorithms**: Objectively decide which is better
3. **Interview Requirement**: Every FAANG interview asks complexity
4. **Optimize Code**: Identify bottlenecks before they become problems
5. **Resource Planning**: Know memory requirements for production systems

---

## 3. Core Concepts & Terminology

### 3.1 Time Complexity

**Definition**: How the **number of operations** grows as input size increases.

**Key Insight**: We don't count exact operations. We count **growth rate**.

```
Input Size (n)    →    Operations
     10           →         100
    100           →       10,000
  1,000           →    1,000,000
 10,000           →  100,000,000
```

If operations = n², we say **Time Complexity = O(n²)**

---

### 3.2 Big-O Notation (Upper Bound)

**Big-O** = **Worst-case scenario** (maximum time algorithm can take)

**Formal Definition**:  
f(n) = O(g(n)) means there exist constants c and n₀ such that:  
f(n) ≤ c × g(n) for all n ≥ n₀

**Simple Translation**:  
"For large enough inputs, my algorithm won't take longer than this"

---

### 3.3 Common Time Complexities (Best to Worst)

```
O(1)     <  O(log n)   <  O(n)   <  O(n log n)   <  O(n²)   <  O(2ⁿ)   <  O(n!)
Constant    Logarithmic    Linear   Linearithmic   Quadratic  Exponential Factorial

  ✅ Excellent     ✅ Good      👍 OK       👍 OK        ⚠️ Bad       ❌ Terrible   ❌ Worst
```

**Visual Growth**:

```
Operations
  ↑
  |                                    O(n²)
  |                               /
  |                          /
  |                     /
  |                /          O(n log n)
  |           /            /
  |      /             /
  |  O(n)          /
  |  /        /
  | /   O(log n)
  |/___/_______________________→ Input (n)
  O(1) →
```

---

### 3.4 Big-Theta (Θ) Notation (Tight Bound)

**Big-Theta** = **Average-case** (exact growth rate)

```cpp
// This is Θ(n) because it ALWAYS runs n times
for(int i = 0; i < n; i++) {
    cout << i << " ";
}
```

**When to use**: When best case = worst case = same complexity

---

### 3.5 Big-Omega (Ω) Notation (Lower Bound)

**Big-Omega** = **Best-case scenario** (minimum time algorithm can take)

```cpp
// Linear search: Ω(1) if element is at first position
for(int i = 0; i < n; i++) {
    if(arr[i] == target) return i;  // Could return immediately!
}
```

---

## 4. Visual Diagram: Complexity Comparison

```
┌──────────────────────────────────────────────────────────────┐
│          Time Complexity Comparison Table                     │
├──────────┬──────────────┬────────────┬────────────────────────┤
│ Big-O    │ Name         │ n=10       │ n=1,000,000            │
├──────────┼──────────────┼────────────┼────────────────────────┤
│ O(1)     │ Constant     │ 1          │ 1                      │
│ O(log n) │ Logarithmic  │ 3          │ 20                     │
│ O(n)     │ Linear       │ 10         │ 1,000,000              │
│ O(n log n)│ Linearithmic│ 30         │ 20,000,000             │
│ O(n²)    │ Quadratic    │ 100        │ 1,000,000,000,000      │
│ O(2ⁿ)    │ Exponential  │ 1,024      │ 10^(300,000)           │
│ O(n!)    │ Factorial    │ 3,628,800  │ ∞ (impossible)         │
└──────────┴──────────────┴────────────┴────────────────────────┘

Key Insight:
- O(1), O(log n): Can handle ANY input size ✅
- O(n), O(n log n): Can handle n ≤ 10⁶ ✅
- O(n²): Can only handle n ≤ 10⁴ ⚠️
- O(2ⁿ), O(n!): Can only handle n ≤ 20 ❌
```

---

## 5. C++ Implementation: Analyzing Code Examples

### Example 1: O(1) — Constant Time

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 100;
    
    // Each of these is O(1) - doesn't depend on n
    int x = 5;              // 1 operation
    int y = x + 10;         // 1 operation
    cout << x + y;          // 1 operation
    
    // Total: 3 operations = O(1)
    // Even if n = 1,000,000, still 3 operations!
    
    return 0;
}
```

**Why O(1)?**  
Number of operations stays constant regardless of input size.

---

### Example 2: O(n) — Linear Time

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 100;
    vector<int> arr(n);
    
    // This loop runs n times
    for(int i = 0; i < n; i++) {        // 1 operation × n times
        arr[i] = i * 2;                  // 1 operation × n times
    }
    
    // Total: 2n operations = O(n)
    // If n doubles, time doubles
    
    return 0;
}
```

**Dry Run** (n = 5):
```
i = 0: arr[0] = 0
i = 1: arr[1] = 2
i = 2: arr[2] = 4
i = 3: arr[3] = 6
i = 4: arr[4] = 8
Total iterations: 5 = n
```

---

### Example 3: O(n²) — Quadratic Time

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    
    // Nested loops: outer runs n times, inner runs n times
    for(int i = 0; i < n; i++) {            // n times
        for(int j = 0; j < n; j++) {        // n times for each i
            cout << "(" << i << "," << j << ") ";  // 1 operation
        }
        cout << endl;
    }
    
    // Total: n × n = n² operations = O(n²)
    // If n doubles, time quadruples!
    
    return 0;
}
```

**Dry Run** (n = 3):
```
i=0: (0,0) (0,1) (0,2)     → 3 operations
i=1: (1,0) (1,1) (1,2)     → 3 operations
i=2: (2,0) (2,1) (2,2)     → 3 operations
Total: 9 = 3² = n² operations
```

---

### Example 4: O(log n) — Logarithmic Time

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 16;
    
    // Variable doubles each iteration: 1, 2, 4, 8, 16
    for(int i = 1; i < n; i *= 2) {
        cout << i << " ";
    }
    // Output: 1 2 4 8
    // Iterations: log₂(16) = 4
    
    return 0;
}
```

**Why O(log n)?**
```
n = 16:
Iteration 1: i = 1
Iteration 2: i = 2   (doubled)
Iteration 3: i = 4   (doubled)
Iteration 4: i = 8   (doubled)
Iteration 5: i = 16  (stops, i >= n)

Total iterations: log₂(16) = 4

Key: If we keep dividing n by 2, how many steps to reach 1?
Answer: log₂(n)
```

**Real-World Analogy**:  
Finding a page in a book:
- **Linear search** (O(n)): Check each page one by one
- **Binary search** (O(log n)): Open middle, eliminate half, repeat

---

### Example 5: O(n log n) — Linearithmic Time

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 8;
    
    // Outer loop: n times
    // Inner loop: log n times
    for(int i = 0; i < n; i++) {            // n times
        for(int j = 1; j < n; j *= 2) {     // log n times
            cout << "*";
        }
        cout << endl;
    }
    
    // Total: n × log n = O(n log n)
    
    return 0;
}
```

**Where you'll see this**: Merge Sort, Quick Sort, Heap Sort

---

### Example 6: O(2ⁿ) — Exponential Time

```cpp
#include <iostream>
using namespace std;

// Fibonacci using recursion (naive approach)
int fibonacci(int n) {
    if(n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    cout << fibonacci(5) << endl;  // 5
    // fibonacci(5) calls fibonacci(4) and fibonacci(3)
    // Each of those calls two more... exponential growth!
    
    return 0;
}
```

**Recursion Tree** (fibonacci(4)):
```
                    fib(4)
                   /      \
              fib(3)      fib(2)
             /     \      /     \
         fib(2)  fib(1) fib(1) fib(0)
        /     \
    fib(1)  fib(0)

Total calls: 9 for n=4
For n=30: Over 2 million calls!
```

---

## 6. Dry Run: Analyzing Complex Code

Let's analyze this step-by-step:

```cpp
void analyze(int n) {
    // Part 1
    for(int i = 0; i < n; i++) {
        cout << i;
    }
    
    // Part 2
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << "*";
        }
    }
    
    // Part 3
    for(int i = 1; i < n; i *= 2) {
        cout << i;
    }
}
```

**Step-by-Step Analysis**:

```
Part 1: Single loop
  → Runs n times
  → Complexity: O(n)

Part 2: Nested loops
  → Outer: n times
  → Inner: n times for each outer iteration
  → Total: n × n = n²
  → Complexity: O(n²)

Part 3: Logarithmic loop
  → i doubles each time: 1, 2, 4, 8, 16, ...
  → Stops when i >= n
  → Number of doublings: log₂(n)
  → Complexity: O(log n)

Overall Complexity:
  O(n) + O(n²) + O(log n)
  = O(n²)  [take the dominant term]
```

💡 **TRICK**: **Dominant Term Rule** — When adding complexities, keep only the FASTEST growing term!
- O(n² + n + log n) → O(n²)
- O(2ⁿ + n³) → O(2ⁿ)
- O(n + 5) → O(n)

---

## 7. All Operations with Time & Space Complexity

### Array Operations:

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index | O(1) | O(1) | Direct memory access |
| Search (unsorted) | O(n) | O(1) | Must check each element |
| Search (sorted, binary) | O(log n) | O(1) | Divide and conquer |
| Insert at end | O(1) | O(1) | If capacity available |
| Insert at beginning | O(n) | O(1) | Must shift all elements |
| Delete at end | O(1) | O(1) | Simple removal |
| Delete at beginning | O(n) | O(1) | Must shift all elements |

### Vector Operations (STL):

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| push_back | O(1)* | O(1) | *Amortized |
| pop_back | O(1) | O(1) | Always constant |
| insert (middle) | O(n) | O(1) | Shifts elements |
| erase (middle) | O(n) | O(1) | Shifts elements |
| resize | O(n) | O(n) | Allocates new array |

### Map/Set Operations (STL):

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| insert | O(log n) | O(1) | Balanced BST |
| search | O(log n) | O(1) | Tree traversal |
| delete | O(log n) | O(1) | Rebalance tree |
| iterate all | O(n) | O(1) | In-order traversal |

### Stack/Queue Operations:

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| push/enqueue | O(1) | O(1) |
| pop/dequeue | O(1) | O(1) |
| top/front | O(1) | O(1) |
| size | O(1) | O(1) |

---

## 8. Common Patterns & Tricks

### 💡 TRICK 1: Drop Constants
```cpp
// This is O(n), NOT O(2n)
for(int i = 0; i < n; i++) {    // n iterations
    cout << i;
}
for(int i = 0; i < n; i++) {    // n iterations
    cout << i * 2;
}
// Total: 2n operations → O(n) [drop constant 2]
```

### 💡 TRICK 2: Drop Lower Order Terms
```cpp
// This is O(n²), NOT O(n² + n + 1)
for(int i = 0; i < n; i++) {          // n iterations
    for(int j = 0; j < n; j++) {      // n² iterations
        cout << "*";
    }
    cout << i;                        // n iterations
}
cout << "Done";                       // 1 iteration
// Total: n² + n + 1 → O(n²) [keep dominant term]
```

### 💡 TRICK 3: Nested Loop Pattern Recognition
```cpp
// Pattern 1: O(n²)
for(int i = 0; i < n; i++)
    for(int j = 0; j < n; j++)

// Pattern 2: O(n²) also!
for(int i = 0; i < n; i++)
    for(int j = i; j < n; j++)
// n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n²)

// Pattern 3: O(n)
for(int i = 0; i < n; i++)
    for(int j = 0; j < 100; j++)
// 100n → O(n) [100 is constant]
```

### 💡 TRICK 4: Recursive Function Complexity
```cpp
// Single recursive call: O(n)
void func(int n) {
    if(n <= 0) return;
    func(n-1);  // Reduces by 1 each time → n calls
}

// Two recursive calls: O(2ⁿ)
void func(int n) {
    if(n <= 0) return;
    func(n-1);  // Branches into 2 calls
    func(n-1);  // Each branches again → 2ⁿ
}
```

💡 **TRICK 5: Space Complexity Shortcut**
- **Variables**: O(1) space
- **Arrays/Vectors**: O(n) space
- **Recursion**: O(recursion depth) space (call stack)
- **2D Array**: O(n²) space

---

## 9. Common Mistakes & How to Avoid Them

### ❌ Mistake 1: Confusing O(n) with O(n²)
```cpp
// This is O(n), NOT O(n²)
for(int i = 0; i < n; i++) {
    cout << i;
}
for(int j = 0; j < n; j++) {  // Separate loop!
    cout << j;
}
```
✅ **Fix**: Sequential loops ADD → O(n) + O(n) = O(n)

### ❌ Mistake 2: Forgetting Space Complexity of Recursion
```cpp
// Time: O(n), Space: O(n) [call stack], NOT O(1)!
void recursive(int n) {
    if(n <= 0) return;
    recursive(n-1);
}
```
✅ **Fix**: Always count recursion stack space!

### ❌ Mistake 3: Assuming All Loops Are O(n)
```cpp
// This is O(log n), NOT O(n)
for(int i = 1; i < n; i *= 2) {
    cout << i;
}
```
✅ **Fix**: Check how loop variable changes (multiplication → logarithmic)

### ❌ Mistake 4: Ignoring Amortized Analysis
```cpp
vector<int> v;
for(int i = 0; i < n; i++) {
    v.push_back(i);  // O(1) amortized, not always O(1)
}
```
✅ **Fix**: push_back is O(1) amortized (occasionally O(n) for resizing)

### ❌ Mistake 5: Wrong Complexity for String Operations
```cpp
string s1 = "hello";
string s2 = "world";
string s3 = s1 + s2;  // O(n) where n = length of strings, NOT O(1)!
```
✅ **Fix**: String concatenation copies characters → O(length)

---

## 10. Interview Tips & What Companies Ask

### Most Common Interview Questions:
1. **"What is the time complexity of this code?"** (90% of interviews)
2. **"Can you optimize this algorithm?"** 
3. **"What is the space complexity?"**
4. **"Explain Big-O to a non-technical person"**
5. **"When would you use O(n²) vs O(n log n)?"**

### What Interviewers Look For:
- ✅ Can you analyze code without running it?
- ✅ Do you understand trade-offs (time vs space)?
- ✅ Can you identify bottlenecks?
- ✅ Can you explain complexity in simple terms?

### Pro Tips for Interviews:
1. **Always state complexity** after writing code
2. **Explain your reasoning**: "This is O(n) because..."
3. **Mention trade-offs**: "We can reduce time to O(log n) but need O(n) extra space"
4. **Use examples**: "For n=1000, O(n²) means 1,000,000 operations"

---

## 11. Practice Problems

### 🟢 Easy Problems:
1. **Analyze Simple Loop** — Find complexity of single loop
2. **Constant Time Check** — Identify O(1) operations
3. **Nested Loop Count** — Count operations in nested loops
4. **Logarithmic Pattern** — Identify O(log n) loops
5. **Recursive Fibonacci** — Analyze naive recursion complexity

### 🟡 Medium Problems:
6. **Multiple Loops** — Analyze code with sequential + nested loops 🏢 [Amazon]
7. **Recursive Function** — Find complexity of recursive algorithms 🏢 [Google]
8. **Space Complexity** — Analyze memory usage 🏢 [Microsoft]
9. **Amortized Analysis** — Vector push_back pattern 🏢 [Meta]
10. **Optimize Brute Force** — Reduce O(n²) to O(n log n) 🏢 [Adobe]

### Problem Links:
- LeetCode Complexity Problems: https://leetcode.com/tag/
- GeeksforGeeks Analysis: https://geeksforgeeks.org/analysis-algorithms/

---

## 12. Solved Example Problems

### Example 1: Analyze This Code

**Problem**: Find time and space complexity:
```cpp
void function(int n) {
    int count = 0;
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            count++;
        }
    }
}
```

**Solution**:

**Time Complexity Analysis**:
```
i = 0: inner loop runs n times (j = 0 to n-1)
i = 1: inner loop runs n-1 times (j = 1 to n-1)
i = 2: inner loop runs n-2 times (j = 2 to n-1)
...
i = n-1: inner loop runs 1 time

Total: n + (n-1) + (n-2) + ... + 1
     = n(n+1)/2
     = (n² + n)/2
     = O(n²)  [drop constant 1/2 and lower term n]
```

**Space Complexity**: O(1) — only using variables (count, i, j)

---

### Example 2: Recursive Complexity

**Problem**: Find complexity:
```cpp
int func(int n) {
    if(n <= 1) return 1;
    return func(n-1) + func(n-2);
}
```

**Solution**:

**Recursion Tree**:
```
                    func(n)
                   /       \
            func(n-1)     func(n-2)
            /     \       /       \
      func(n-2) func(n-3) ...    ...
      /      \
 func(n-3) func(n-4)

Height of tree: n
Branches per node: 2
Total nodes: 2⁰ + 2¹ + 2² + ... + 2ⁿ⁻¹ = 2ⁿ - 1

Time Complexity: O(2ⁿ)
Space Complexity: O(n) [maximum recursion depth]
```

---

### Example 3: Amortized Analysis

**Problem**: What is the complexity of n push_back operations?

```cpp
vector<int> v;
for(int i = 0; i < n; i++) {
    v.push_back(i);
}
```

**Solution**:

**Understanding Vector Resizing**:
```
Capacity: 1 → 2 → 4 → 8 → 16 → ... (doubles when full)

Cost analysis:
- push_back #1: 1 operation (no resize)
- push_back #2: 2 operations (resize: copy 1 element + add new)
- push_back #3: 1 operation (no resize)
- push_back #4: 4 operations (resize: copy 3 elements + add new)
- push_back #5: 1 operation
- ...

Total cost for n operations:
= n (for normal insertions) + (1 + 2 + 4 + 8 + ... + n/2) (for resizing)
= n + (n - 1)  [geometric series]
= 2n - 1
= O(n) for n operations

Amortized cost per operation:
= O(n) / n = O(1) per push_back
```

**Answer**: O(1) amortized per operation, O(n) total for n operations

---

## 13. Glossary

| Term | Definition |
|------|------------|
| **Time Complexity** | How runtime grows with input size |
| **Space Complexity** | How memory usage grows with input size |
| **Big-O (O)** | Upper bound (worst-case) complexity |
| **Big-Theta (Θ)** | Tight bound (average-case) complexity |
| **Big-Omega (Ω)** | Lower bound (best-case) complexity |
| **Constant Time** | O(1) — doesn't depend on input size |
| **Linear Time** | O(n) — grows proportionally with input |
| **Quadratic Time** | O(n²) — grows with square of input |
| **Logarithmic Time** | O(log n) — grows with log of input |
| **Amortized Analysis** | Average cost per operation over many operations |
| **Dominant Term** | Fastest-growing term in complexity expression |
| **Call Stack** | Memory used by recursive function calls |
| **Growth Rate** | How quickly complexity increases as n grows |

---

## 14. Future Questions (Predictions)

Based on current interview trends:
1. **Space-Time Trade-offs** — When to sacrifice space for time
2. **Average vs Worst Case** — QuickSort O(n log n) vs O(n²)
3. **Amortized Analysis** — Dynamic array resizing, hash table operations
4. **Complexity of STL Operations** — Deep understanding of internal implementations
5. **Lower Bounds** — Proving an algorithm is optimal

---

## 15. Competitive Programming Section

### Operation Limits (1 Second):
```
n ≤ 10⁶:  O(n) or O(n log n) acceptable
n ≤ 10⁴:  O(n²) acceptable
n ≤ 500:  O(n³) acceptable
n ≤ 20:   O(2ⁿ) acceptable
n ≤ 10:   O(n!) acceptable
```

### Quick Complexity Check:
```cpp
// If you see this pattern in contest:
for(...)           // O(n)
  for(...)         // O(n)
    for(...)       // O(n)

if n = 10⁵: n³ = 10¹⁵ → TLE! ❌
if n = 100: n³ = 10⁶ → OK ✅
```

### Common Optimizations:
```cpp
// O(n²) → O(n log n): Use sorting + binary search
// O(n²) → O(n): Use hash map for lookups
// O(2ⁿ) → O(n): Use dynamic programming (memoization)
// O(n) → O(log n): Use binary search on sorted data
```

---

**🎉 Congratulations! You've mastered Complexity Analysis!**

**Next Steps**:
1. ✅ Complete all MCQs in `01_mcqs.md`
2. ✅ Practice analyzing 20+ code snippets
3. ✅ Move to **02_Arrays**

[← Back to README](../README.md) | [Next: Arrays →](../../03-Arrays-and-Strings/concepts/01-array-master-notes.md)
