[← Chapter 16](07-arrays-and-vectors-ch16-66-pair-sum-on-an-unsorted-arr.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 18 →](07-arrays-and-vectors-ch18-91-pair-sum-pattern-recognitio.md)

---

# 79. Candidate vs Verified Majority

This is a critical point.

Moore's algorithm's first pass gives a **candidate**.

If the problem does **not guarantee** that a majority element exists, you should verify it.

Example:

```text
[1, 2, 3]
```

Moore's process may return a candidate, but there is no majority element because:

```text
frequency of each = 1
n/2 = 1
```

and:

```text
1 > 1
```

is false.

---

# 80. Moore's Voting with Verification

```cpp
int majorityElement(const vector<int>& nums) {

    int candidate = 0;
    int count = 0;

    // Phase 1: find candidate
    for (int value : nums) {

        if (count == 0) {
            candidate = value;
        }

        if (value == candidate) {
            count++;
        }
        else {
            count--;
        }
    }

    // Phase 2: verify candidate
    int freq = 0;

    for (int value : nums) {

        if (value == candidate) {
            freq++;
        }
    }

    if (freq > nums.size() / 2) {
        return candidate;
    }

    return -1;
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

---

# 81. Majority Element Approaches

| Approach | Time | Extra Space | Main Idea |
|---|---:|---:|---|
| Brute force | O(n²) | O(1) | Count every value |
| Hashing | O(n) average | O(n) | Store frequencies |
| Sorting | O(n log n) | Depends | Middle element |
| Moore's Voting | O(n) | O(1) | Cancel opposing votes |

---

# 82. Vector Passing: Value vs Reference

The original pair-sum code uses:

```cpp
vector<int> pairSum(vector<int> nums, int target)
```

This passes the vector by value, which creates a copy.

For read-only input, prefer:

```cpp
vector<int> pairSum(const vector<int>& nums, int target)
```

Meaning:

```text
const
 ↓
function cannot modify nums

&
 ↓
avoid copying the entire vector
```

This is a very important C++ DSA habit.

---

# 83. `vector<int> nums` vs `const vector<int>& nums`

### By value

```cpp
void solve(vector<int> nums)
```

Conceptually:

```text
original vector
      ↓
    COPY
      ↓
function
```

Potential extra:

```text
O(n)
```

copy cost.

### By const reference

```cpp
void solve(const vector<int>& nums)
```

Conceptually:

```text
original vector
      ↓
function accesses it
      ↓
no copy
```

Usually preferred when the function only needs to read the vector.

---

# 84. If Function Needs to Modify the Vector

Use:

```cpp
void modify(vector<int>& nums) {
    nums[0] = 100;
}
```

The `&` allows the function to modify the original vector.

If you don't want modification:

```cpp
void print(const vector<int>& nums)
```

---

# 85. Important Code Corrections from the Source

Several snippets in the original notes are conceptually correct but contain syntax or implementation issues.

## Issue 1 — `ans` not declared

This:

```cpp
ans.push_back(i);
```

requires:

```cpp
vector<int> ans;
```

inside the function.

Correct:

```cpp
vector<int> pairSum(const vector<int>& nums, int target) {

    vector<int> ans;

    ...
}
```

---

## Issue 2 — Missing `&` in output

Incorrect:

```cpp
cout << ans[0] << " "< ans[1];
```

Correct:

```cpp
cout << ans[0] << " " << ans[1];
```

---

## Issue 3 — Missing `vector<int>` return syntax details

Correct function:

```cpp
vector<int> pairSum(const vector<int>& nums, int target)
```

---

## Issue 4 — Sorting requires `<algorithm>`

If you use:

```cpp
sort(nums.begin(), nums.end());
```

include:

```cpp
#include <algorithm>
```

---

## Issue 5 — Majority-element sorting code

A safer/simple approach is:

```cpp
sort(nums.begin(), nums.end());

return nums[nums.size() / 2];
```

when the problem guarantees a majority exists.

If existence is not guaranteed, verify the candidate.

---

# 86. Common Vector Mistakes

## Mistake 1 — Confusing size and capacity

```cpp
vector<int> v;

v.reserve(10);
```

does not mean:

```text
10 elements exist
```

It means approximately:

```text
space for at least 10 elements has been reserved
```

---

## Mistake 2 — Assuming capacity always doubles

Do not rely on:

```text
capacity *= 2
```

as a C++ guarantee.

---

## Mistake 3 — Calling `front()` on empty vector

```cpp
vector<int> v;

cout << v.front();
```

Invalid.

---

## Mistake 4 — Calling `back()` after `pop_back()` without checking

```cpp
v.pop_back();
cout << v.back();
```

If the vector was originally size 1, it is now empty.

---

## Mistake 5 — Using invalid index

```cpp
v[100]
```

is invalid if the vector has fewer than 101 elements.

---

## Mistake 6 — Assuming `at()` silently returns something

It does not.

An invalid index causes an exception.

---

# 87. Important Vector Complexity Table

| Operation | Typical Complexity |
|---|---:|
| Access `v[i]` | O(1) |
| `front()` | O(1) |
| `back()` | O(1) |
| `push_back()` | Amortized O(1) |
| `pop_back()` | O(1) |
| `insert()` at end | Amortized O(1) when equivalent to append |
| `insert()` in middle | O(n) |
| `erase()` in middle | O(n) |
| `clear()` | O(n) |
| `size()` | O(1) |
| `empty()` | O(1) |
| `reserve()` | May reallocate; complexity depends on reallocation |
| `resize()` | Depends on operation; can be O(n) |

---

# 88. Vector Memory Model

Conceptually:

```text
Vector object
     │
     ├── pointer ───────────────┐
     ├── size                   │
     └── capacity               │
                                ↓
                         Dynamic storage
                    ┌────┬────┬────┬────┐
                    │ 10 │ 20 │ 30 │    │
                    └────┴────┴────┴────┘
```

The exact internal representation is implementation-specific, but this is a useful conceptual model.

---

# 89. Reallocation

Suppose:

```text
size = capacity
```

and you execute:

```cpp
push_back(x);
```

The current storage may not have enough room.

The vector can:

```text
1. allocate larger storage
2. move/copy existing elements
3. add the new element
4. release old storage
```

Conceptually:

```text
Old:
[10][20][30]

        ↓ reallocation

New:
[10][20][30][40][ ][ ]
```

This is why one individual `push_back()` can cost O(n).

---

# 90. Why Amortized O(1)?

Although some insertions require expensive reallocation, they do not happen every time.

Across many `push_back()` operations, the total cost averages out.

Therefore:

```text
push_back()
     ↓
amortized O(1)
```

This concept is called **amortized analysis**.

---
