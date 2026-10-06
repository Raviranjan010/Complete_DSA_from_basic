[← Chapter 15](10-arrays-and-vectors-intro-ch15-52-kadane-dry-run.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 17 →](10-arrays-and-vectors-intro-ch17-79-candidate-vs-verified-major.md)

---

# 66. Pair Sum on an Unsorted Array

A common optimal-average approach uses hashing.

For each value:

```text
needed = target - current
```

Check whether `needed` has already been seen.

Example:

```text
nums = [2, 7, 11, 15]
target = 9
```

Start:

```text
current = 2
needed = 9 - 2 = 7
```

Store `2`.

Next:

```text
current = 7
needed = 2
```

`2` is already present.

Pair found.

---

# 67. Hashing Pair Sum

Typical code:

```cpp
vector<int> twoSum(const vector<int>& nums, int target) {

    unordered_map<int, int> seen;

    for (int i = 0; i < nums.size(); i++) {

        int needed = target - nums[i];

        if (seen.count(needed)) {
            return {seen[needed], i};
        }

        seen[nums[i]] = i;
    }

    return {};
}
```

Typical complexity:

```text
Average Time = O(n)
Space        = O(n)
```

Worst-case hash-table complexity can degrade, so the O(n) claim is generally an average/expected complexity statement.

---

# 68. Three Pair-Sum Approaches

| Approach | Array requirement | Time | Extra Space |
|---|---|---:|---:|
| Brute force | Any | O(n²) | O(1) |
| Two pointers | Sorted | O(n) | O(1) |
| Hashing | Any | O(n) average | O(n) |

This is an important interview comparison.

---

# 69. Majority Element

## Definition

An element is a **majority element** if it appears more than:

```text
n / 2
```

times in an array of size `n`.

Example:

```text
[2, 2, 1, 2, 3, 2, 2]
```

Here:

```text
n = 7
```

Majority threshold:

```text
7 / 2 = 3
```

The value `2` occurs 5 times.

Since:

```text
5 > 3
```

`2` is the majority element.

---

# 70. Important Difference: More Than vs At Least

Majority means:

```text
frequency > n/2
```

not:

```text
frequency >= n/2
```

For:

```text
n = 6
```

a majority must occur at least:

```text
4
```

times.

Three occurrences is not a majority because:

```text
3 > 3
```

is false.

---

# 71. Brute-Force Majority Element

The original approach checks the frequency of every value.

```cpp
int majorityElement(vector<int> nums) {

    int n = nums.size();

    for (int val : nums) {

        int freq = 0;

        for (int el : nums) {

            if (el == val) {
                freq++;
            }
        }

        if (freq > n / 2) {
            return val;
        }
    }

    return -1;
}
```

Complexity:

```text
Time  = O(n²)
Space = O(1)
```

---

# 72. Sorting-Based Majority Element

Sort the array:

```cpp
sort(nums.begin(), nums.end());
```

If a majority element exists, it must occupy the middle position.

Therefore:

```cpp
int candidate = nums[n / 2];
```

For the classic majority-element problem where existence is guaranteed, this candidate is the majority element.

### Example

```text
Input:
2 1 2 2 3 2 2

Sorted:
1 2 2 2 2 2 3
```

Middle:

```text
index = 7 / 2 = 3
```

Value:

```text
2
```

---

# 73. Sorting Approach Complexity

Sorting:

```text
O(n log n)
```

Then checking/returning the candidate:

```text
O(1)
```

Overall:

```text
O(n log n)
```

If the array is sorted in place:

```text
Extra space depends on the sorting implementation/standard-library guarantees and recursion details.
```

For the common DSA comparison, the key point is that sorting is slower than Moore's Voting Algorithm in time.

---

# 74. Moore's Voting Algorithm

## Definition

**Moore's Voting Algorithm**, commonly called the **Boyer-Moore Majority Vote Algorithm**, finds a majority element in:

```text
O(n) time
O(1) extra space
```

when a majority element exists.

The algorithm maintains:

```text
candidate
count
```

---

# 75. Core Idea of Moore's Voting

Think of the majority element as having enough votes to survive cancellation.

Whenever we see:

```text
same as candidate
```

increase count.

Whenever we see:

```text
different from candidate
```

decrease count.

If count becomes zero:

```text
choose a new candidate
```

The majority element cannot be completely canceled because it occurs more than all other elements combined.

---

# 76. Moore's Voting Code

```cpp
int majorityElement(const vector<int>& nums) {

    int candidate = 0;
    int count = 0;

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

    return candidate;
}
```

This is sufficient if the problem **guarantees that a majority element exists**.

---

# 77. Moore's Voting Dry Run

Consider:

```text
2 2 1 1 1 2 2
```

Start:

```text
candidate = ?
count = 0
```

### Value = 2

Count is zero:

```text
candidate = 2
```

Same:

```text
count = 1
```

### Value = 2

Same:

```text
count = 2
```

### Value = 1

Different:

```text
count = 1
```

### Value = 1

Different:

```text
count = 0
```

### Value = 1

Count is zero:

```text
candidate = 1
count = 1
```

### Value = 2

Different:

```text
count = 0
```

### Value = 2

Count is zero:

```text
candidate = 2
count = 1
```

Final candidate:

```text
2
```

---

# 78. Why Does Moore's Voting Work?

Suppose a majority element appears:

```text
> n/2
```

times.

Therefore, its frequency is greater than the total frequency of all non-majority elements combined.

Pairing:

```text
majority element
+
different element
```

cancels one majority vote against one non-majority vote.

Because there are more majority votes, some majority votes remain uncanceled.

Therefore the final candidate must be the majority element.

---
