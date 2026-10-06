[← Chapter 14](07-arrays-and-vectors-ch14-37-auto-with-vector.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 16 →](07-arrays-and-vectors-ch16-66-pair-sum-on-an-unsorted-arr.md)

---

# 52. Kadane Dry Run

Consider:

```text
arr = [-2, 3, -1, 5, -6]
```

Start:

```text
current = -2
best = -2
```

At `3`:

```text
max(3, -2 + 3)
= max(3, 1)
= 3
```

So:

```text
current = 3
best = 3
```

At `-1`:

```text
max(-1, 3 + -1)
= max(-1, 2)
= 2
```

At `5`:

```text
max(5, 2 + 5)
= 7
```

At `-6`:

```text
max(-6, 7 - 6)
= 1
```

Final:

```text
best = 7
```

---

# 53. The Real Meaning of Kadane

A useful mental model:

```text
current = best sum ending at current index
best    = best sum found anywhere so far
```

This is more precise than simply saying:

> "Remove negative numbers."

Kadane's Algorithm does **not** simply remove every negative number.

For example:

```text
[4, -1, 5]
```

The `-1` is negative, but keeping it gives:

```text
4 + (-1) + 5 = 8
```

which is better than:

```text
4
```

So the correct logic is:

> Keep the previous subarray if extending it improves the sum; otherwise start a new subarray.

---

# 54. Important Kadane Edge Case

Consider:

```text
[-5, -2, -8]
```

The maximum subarray sum is:

```text
-2
```

If you incorrectly initialize:

```cpp
int current = 0;
int best = 0;
```

you may return:

```text
0
```

which is wrong if the problem requires a **non-empty** subarray.

Therefore a robust non-empty-subarray implementation starts from:

```cpp
arr[0]
```

---

# 55. Kadane Complexity

```text
Time  = O(n)
Space = O(1)
```

Comparison:

```text
Brute force → O(n²)
Kadane       → O(n)
```

This is a major optimization.

---

# 56. Pair Sum Problem

## Problem

Given an array and target, find two elements whose sum equals the target.

Example:

```text
nums = [2, 3, 5, 7]
target = 8
```

Possible answer:

```text
3 + 5 = 8
```

---

# 57. Brute-Force Pair Sum

```cpp
vector<int> pairSum(vector<int> nums, int target) {

    vector<int> ans;

    int n = nums.size();

    for (int i = 0; i < n; i++) {

        for (int j = i + 1; j < n; j++) {

            if (nums[i] + nums[j] == target) {

                ans.push_back(i);
                ans.push_back(j);

                return ans;
            }
        }
    }

    return ans;
}
```

---

# 58. Why `j = i + 1`?

We don't want:

```text
i == j
```

because that would use the same element twice.

We also don't need to check both:

```text
(i,j)
(j,i)
```

because they represent the same pair.

Therefore:

```cpp
for (int j = i + 1; j < n; j++)
```

avoids duplicate pair checks.

---

# 59. Pair Sum Complexity

Two nested loops:

```text
O(n²)
```

Extra result storage:

```text
O(1)
```

if the output is limited to two indices.

### Important nuance

If you pass:

```cpp
vector<int> nums
```

by value, the function may copy the vector.

For large inputs, prefer:

```cpp
vector<int> pairSum(const vector<int>& nums, int target)
```

This avoids copying the input vector.

---

# 60. Pair Sum on a Sorted Array — Two Pointers

If the array is sorted:

```text
2 3 4 5 7 9
```

we can use:

```text
left = 0
right = n - 1
```

Example:

```text
target = 9
```

---

# 61. Two-Pointer Logic

Calculate:

```cpp
sum = nums[left] + nums[right];
```

Then:

### If:

```text
sum == target
```

Pair found.

### If:

```text
sum > target
```

Decrease `right`.

Why?

Because the array is sorted, moving right leftward reduces the value.

### If:

```text
sum < target
```

Increase `left`.

Why?

Because moving left rightward increases the value.

---

# 62. Two-Pointer Example

Array:

```text
2 3 4 5 7 9
```

Target:

```text
9
```

Start:

```text
left = 0 → 2
right = 5 → 9
```

Sum:

```text
2 + 9 = 11
```

Too large:

```text
right--
```

Now:

```text
2 + 7 = 9
```

Found.

Indices:

```text
0 and 4
```

---

# 63. Two-Pointer Code

```cpp
vector<int> pairSum(const vector<int>& nums, int target) {

    vector<int> ans;

    int left = 0;
    int right = nums.size() - 1;

    while (left < right) {

        int sum = nums[left] + nums[right];

        if (sum == target) {

            ans.push_back(left);
            ans.push_back(right);

            return ans;
        }

        else if (sum > target) {
            right--;
        }

        else {
            left++;
        }
    }

    return ans;
}
```

---

# 64. Critical Condition for Two-Pointer Pair Sum

The simple:

```text
if sum > target → right--
if sum < target → left++
```

logic depends on the array being **sorted in ascending order**.

For:

```text
2 3 4 5 7 9
```

it works.

For:

```text
2 7 3 9 4 5
```

it does not work reliably.

---

# 65. Pair Sum Complexity — Two Pointers

```text
Time  = O(n)
Space = O(1)
```

assuming the input is already sorted and no additional storage is required.

### But what if the array is unsorted?

You have options.

---
