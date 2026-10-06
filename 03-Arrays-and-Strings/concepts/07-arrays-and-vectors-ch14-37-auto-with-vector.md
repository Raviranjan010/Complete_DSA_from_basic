[← Chapter 13](07-arrays-and-vectors-ch13-19-front.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 15 →](07-arrays-and-vectors-ch15-52-kadane-dry-run.md)

---

# 37. `auto` with Vector

You can write:

```cpp
for (auto x : vec) {
    cout << x << " ";
}
```

Or for modification:

```cpp
for (auto &x : vec) {
    x *= 2;
}
```

For read-only access without copying:

```cpp
for (const auto &x : vec) {
    cout << x << " ";
}
```

---

# 38. Vector Iterators

Vectors support iterators.

```cpp
vector<int> v = {10, 20, 30};

auto it = v.begin();

cout << *it;
```

Output:

```text
10
```

`begin()` points to the first element.

`end()` points **one position past the last element**.

Important:

```text
begin() → first element
end()   → one-past-last position
```

Do not dereference `end()`.

---

# 39. `begin()` and `end()`

Example:

```cpp
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";
}
```

Output:

```text
10 20 30
```

This is the basis for many STL algorithms.

---

# 40. Vector and `sort()`

Include:

```cpp
#include <algorithm>
```

Then:

```cpp
sort(v.begin(), v.end());
```

Example:

```cpp
vector<int> v = {5, 2, 9, 1, 4};

sort(v.begin(), v.end());
```

Result:

```text
1 2 4 5 9
```

Typical complexity:

```text
O(n log n)
```

---

# 41. Descending Sort

```cpp
sort(v.begin(), v.end(), greater<int>());
```

Result:

```text
9 5 4 2 1
```

---

# 42. Vector vs Array

| Feature | Built-in Array | Vector |
|---|---|---|
| Size | Fixed | Dynamic |
| `push_back()` | ❌ | ✅ |
| `pop_back()` | ❌ | ✅ |
| `size()` member | ❌ | ✅ |
| `capacity()` | ❌ | ✅ |
| `front()` | ❌ | ✅ |
| `back()` | ❌ | ✅ |
| `at()` | ❌ | ✅ |
| Automatic growth | ❌ | ✅ |
| STL integration | Limited | Excellent |

---

# 43. Static vs Dynamic Allocation — Important Correction

A common beginner statement is:

> "Static is compile time and allocation is runtime."

This is too simplified.

There are several different concepts:

- compile time vs runtime
- storage duration
- stack vs heap
- fixed-size arrays vs dynamic containers

For DSA, remember the practical distinction:

```text
Built-in array with fixed size
    ↓
size cannot dynamically grow

vector
    ↓
can dynamically manage its storage
```

A vector itself is an object with automatic/dynamic storage depending on how it is created, while its element storage is managed dynamically by the vector.

---

# 44. XOR Properties

The uploaded material introduces XOR.

XOR operator:

```cpp
^
```

Important properties:

```text
x ^ x = 0
x ^ 0 = x
```

Also:

```text
x ^ y ^ x = y
```

because:

```text
x ^ x = 0
0 ^ y = y
```

XOR is extremely useful in array problems.

---

# 45. Example — Find Single Element

Suppose every number occurs twice except one:

```text
2 4 1 4 2
```

Answer:

```text
1
```

Using XOR:

```cpp
int ans = 0;

for (int x : nums) {
    ans ^= x;
}
```

Why?

```text
2 ^ 4 ^ 1 ^ 4 ^ 2

(2 ^ 2) ^ (4 ^ 4) ^ 1

0 ^ 0 ^ 1

= 1
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

### Important condition

This simple XOR technique requires the intended frequency property, typically:

> Every element appears exactly twice except one element that appears once.

---

# 46. Kadane's Algorithm

## Problem

Find the **maximum sum of a contiguous subarray**.

Example:

```text
arr = [-2, 3, -1, 5, -6]
```

Possible subarrays include:

```text
[-2]
[3]
[3,-1]
[3,-1,5]
[-1,5]
...
```

The maximum sum is:

```text
3 + (-1) + 5 = 7
```

---

# 47. Brute-Force Maximum Subarray Sum

The uploaded code uses nested loops.

Correct form:

```cpp
vector<int> arr = {2, 33, 4, 63, 12};

int n = arr.size();
int maxSum = INT_MIN;

for (int st = 0; st < n; st++) {

    int currSum = 0;

    for (int en = st; en < n; en++) {

        currSum += arr[en];

        maxSum = max(maxSum, currSum);
    }
}

cout << maxSum << endl;
```

---

# 48. Why Does the Brute-Force Code Work?

For every starting position:

```cpp
st
```

we extend the ending position:

```cpp
en
```

Example:

```text
1 2 3
```

For:

```text
st = 0
```

we calculate:

```text
1
1+2
1+2+3
```

For:

```text
st = 1
```

we calculate:

```text
2
2+3
```

For:

```text
st = 2
```

we calculate:

```text
3
```

Thus every contiguous subarray is considered.

---

# 49. Brute-Force Complexity

Number of start/end combinations is approximately:

```text
n²
```

Therefore:

```text
Time = O(n²)
Space = O(1)
```

This is much better than calculating every subarray sum from scratch with a third loop, which can become O(n³).

---

# 50. Kadane's Core Idea

Kadane's Algorithm improves the maximum-subarray problem to:

```text
O(n)
```

The key question at every element is:

> Should I extend the current subarray, or start a new subarray here?

For each element:

```text
current = max(current + arr[i], arr[i])
```

Meaning:

```text
Either:
1. Continue previous subarray
or
2. Start fresh from arr[i]
```

---

# 51. Kadane's Algorithm

```cpp
long long current = arr[0];
long long best = arr[0];

for (int i = 1; i < n; i++) {

    current = max(1LL * arr[i], current + arr[i]);

    best = max(best, current);
}

cout << best;
```

---
