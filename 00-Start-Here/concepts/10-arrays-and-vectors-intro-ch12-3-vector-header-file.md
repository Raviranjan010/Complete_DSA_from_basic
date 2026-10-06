[← Chapter 11](10-arrays-and-vectors-intro-ch11-91-practice-questions-2d-array.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 13 →](10-arrays-and-vectors-intro-ch13-19-front.md)

---

# 3. Vector Header File

To use vectors:

```cpp
#include <vector>
```

Example:

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {

    vector<int> nums;

    nums.push_back(10);
    nums.push_back(20);

    cout << nums[0];

    return 0;
}
```

Output:

```text
10
```

---

# 4. Vector is a Template

Vectors are implemented as a class template.

Syntax:

```cpp
vector<data_type> vector_name;
```

Examples:

```cpp
vector<int> nums;
vector<double> prices;
vector<char> letters;
vector<string> names;
```

The type inside `< >` determines the type of elements stored.

---

# 5. Basic Vector Declaration

## Method 1 — Empty Vector

```cpp
vector<int> nums;
```

Initially:

```text
size = 0
```

---

## Method 2 — Empty Vector Using `{}`

```cpp
vector<int> nums = {};
```

This also creates an empty vector.

---

## Method 3 — Vector with a Given Size

```cpp
vector<int> nums(5);
```

This creates:

```text
[0][0][0][0][0]
```

The vector has:

```text
size = 5
```

### Important

This does **not** mean:

> "Reserve space for 5 elements and keep size 0."

It actually creates **5 elements** initialized to zero.

---

# 6. Vector with Size and Initial Value

```cpp
vector<int> nums(5, 10);
```

Result:

```text
[10][10][10][10][10]
```

So:

```text
vector<int>(size, value)
```

means:

> Create `size` elements, each initialized with `value`.

Example:

```cpp
vector<int> arr(4, -1);
```

Result:

```text
-1 -1 -1 -1
```

---

# 7. Vector Initialization Using Values

```cpp
vector<int> nums = {10, 20, 30, 40};
```

or:

```cpp
vector<int> nums{10, 20, 30, 40};
```

Result:

```text
Index:  0   1   2   3
Value: 10  20  30  40
```

---

# 8. Vector from Another Vector

```cpp
vector<int> a = {1, 2, 3};

vector<int> b(a);
```

Now:

```text
a = 1 2 3
b = 1 2 3
```

`b` is a separate vector containing copies of the elements.

---

# 9. Vector Size

Use:

```cpp
vec.size()
```

Example:

```cpp
vector<int> vec = {10, 20, 30};

cout << vec.size();
```

Output:

```text
3
```

### Definition

`size()` returns the **number of elements currently stored in the vector**.

---

# 10. Size vs Capacity

This is one of the most important vector concepts.

## Size

Number of actual elements currently stored.

## Capacity

Number of elements the vector can currently store in its allocated storage before requiring a reallocation.

Example:

```cpp
vector<int> v;

v.push_back(10);
```

Conceptually, you might have:

```text
size     = 1
capacity = some value >= 1
```

The exact capacity growth strategy is implementation-dependent.

---

# 11. `capacity()`

Use:

```cpp
vec.capacity()
```

Example:

```cpp
cout << vec.capacity();
```

It tells you how many elements can currently fit in the allocated storage without reallocating.

---

# 12. Size vs Capacity Example

Suppose:

```cpp
vector<int> v;

v.push_back(10);
v.push_back(20);
v.push_back(30);
```

You might observe:

```text
size = 3
capacity = 4
```

That means:

```text
Actual elements:
[10][20][30]

Allocated room:
[10][20][30][ ]
```

The exact capacity value is not guaranteed to be 4.

---

# 13. Important Correction About Capacity Doubling

A common beginner statement is:

> "Vector capacity always doubles when size becomes greater than capacity."

This is **not a C++ language guarantee**.

A vector grows its capacity when necessary, but the exact growth strategy is implementation-dependent.

You may observe doubling on some implementations:

```text
1 → 2 → 4 → 8 → 16
```

but you should not write DSA logic that depends on a guaranteed doubling factor.

The important concept is:

> **When the current capacity is insufficient, the vector reallocates storage with a larger capacity.**

---

# 14. `push_back()`

## Definition

`push_back()` adds an element to the end of the vector.

Example:

```cpp
vector<int> v;

v.push_back(10);
v.push_back(20);
v.push_back(30);
```

Result:

```text
10 20 30
```

---

# 15. `push_back()` Dry Run

Start:

```text
v = []
```

After:

```cpp
v.push_back(10);
```

```text
v = [10]
```

After:

```cpp
v.push_back(20);
```

```text
v = [10, 20]
```

After:

```cpp
v.push_back(30);
```

```text
v = [10, 20, 30]
```

---

# 16. Complexity of `push_back()`

Usually:

```text
Amortized time = O(1)
```

But an individual `push_back()` can take:

```text
O(n)
```

when reallocation is required and existing elements must be moved/copied.

### Important DSA concept

Do not say:

> `push_back()` is always O(1).

The more accurate statement is:

> **`push_back()` has amortized O(1) complexity, while an individual operation can be O(n) during reallocation.**

---

# 17. `pop_back()`

## Definition

`pop_back()` removes the last element.

Example:

```cpp
vector<int> v = {10, 20, 30};

v.pop_back();
```

Result:

```text
10 20
```

The removed value is:

```text
30
```

---

# 18. `pop_back()` Does Not Return the Removed Value

This is important.

Do not write:

```cpp
int x = v.pop_back();
```

because `pop_back()` returns `void`.

If you need the last value first:

```cpp
int x = v.back();

v.pop_back();
```

---
