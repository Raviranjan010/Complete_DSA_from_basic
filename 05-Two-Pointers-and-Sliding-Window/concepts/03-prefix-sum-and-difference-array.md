# Prefix Sum Technique — Complete Guide

> **What You'll Learn**: 1D prefix sum, 2D prefix sum, prefix XOR  
> **Prerequisites**: Array Basics, Complexity Analysis  
> **Time Required**: 2-3 hours

---

## 1. 📌 Definition

**Prefix Sum** precomputes cumulative sums to answer range sum queries in O(1) time instead of O(n).

**Core Idea**: `prefix[i]` stores sum of all elements from index 0 to i.

---

## 2. 🌍 Real-World Analogy

### Analogy 1: Bank Account Statement 🏦

Imagine tracking your spending:
- Day 1: Spent $10 → Total: $10
- Day 2: Spent $20 → Total: $30
- Day 3: Spent $15 → Total: $45

To find spending from Day 2 to Day 3:
- Total by Day 3 ($45) - Total by Day 1 ($10) = $35 ✓

### Analogy 2: Mile Markers on Highway 🛣️

Highway mile markers show distance from start:
- Marker at mile 100
- Marker at mile 150
- Distance between them: 150 - 100 = 50 miles

No need to measure from the beginning each time!

---

## 3. 🎨 Visual Diagram

### 1D Prefix Sum Array

```
Original Array:  [3,  1,  4,  2,  5,  3]
Indices:          0   1   2   3   4   5

Prefix Sum:      [3,  4,  8,  10, 15, 18]
                  ↑   ↑   ↑    ↑   ↑   ↑
                3   3+1 3+1+4 ... cumulative sums

To find sum from index 2 to 4:
prefix[4] - prefix[1] = 15 - 4 = 11
Check: arr[2] + arr[3] + arr[4] = 4 + 2 + 5 = 11 ✓
```

### Formula

```
Sum from index L to R = prefix[R] - prefix[L-1]

Special case: If L = 0, sum = prefix[R]
```

---

## 4. 🔑 Pattern Recognition Keywords

**Look for these words in problems**:
- "Range sum"
- "Sum from index i to j"
- "Count subarrays with sum K"
- "Subarray sum"
- "Cumulative sum"
- "XOR of range"
- "Multiple queries"

---

## 5. 📋 Template Code

### Template 1: Basic Prefix Sum

```cpp
#include <iostream>
#include <vector>
using namespace std;

class PrefixSum {
private:
    vector<int> prefix;
    
public:
    PrefixSum(vector<int>& arr) {
        int n = arr.size();
        prefix.resize(n);
        
        // Build prefix sum array
        prefix[0] = arr[0];
        for(int i = 1; i < n; i++) {
            prefix[i] = prefix[i-1] + arr[i];
        }
    }
    
    // Get sum from index L to R in O(1)
    int rangeSum(int L, int R) {
        if(L == 0) return prefix[R];
        return prefix[R] - prefix[L-1];
    }
};
```

### Template 2: Prefix Sum for Subarray Counting

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> prefixCount;
    prefixCount[0] = 1;  // Important: empty prefix
    
    int currentSum = 0;
    int count = 0;
    
    for(int num : nums) {
        currentSum += num;
        
        // If (currentSum - k) exists, we found subarrays
        if(prefixCount.find(currentSum - k) != prefixCount.end()) {
            count += prefixCount[currentSum - k];
        }
        
        // Record this prefix sum
        prefixCount[currentSum]++;
    }
    
    return count;
}
```

---

## 6. 🔍 Step-by-Step Example

### Problem: Range Sum Query

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr = {3, 1, 4, 2, 5, 3};
    int n = arr.size();
    
    // Build prefix sum array
    vector<int> prefix(n);
    prefix[0] = arr[0];
    
    for(int i = 1; i < n; i++) {
        prefix[i] = prefix[i-1] + arr[i];
    }
    
    cout << "Prefix array: ";
    for(int x : prefix) {
        cout << x << " ";  // 3 4 8 10 15 18
    }
    cout << endl;
    
    // Query 1: Sum from index 2 to 4
    int L = 2, R = 4;
    int sum = prefix[R] - prefix[L-1];
    cout << "Sum from " << L << " to " << R << " = " << sum << endl;  // 11
    
    // Query 2: Sum from index 0 to 3
    L = 0, R = 3;
    sum = prefix[R];  // Special case: L = 0
    cout << "Sum from " << L << " to " << R << " = " << sum << endl;  // 10
    
    return 0;
}
```

**Dry Run - Building Prefix Array**:
```
arr = [3, 1, 4, 2, 5, 3]

i=0: prefix[0] = 3
i=1: prefix[1] = prefix[0] + 1 = 3 + 1 = 4
i=2: prefix[2] = prefix[1] + 4 = 4 + 4 = 8
i=3: prefix[3] = prefix[2] + 2 = 8 + 2 = 10
i=4: prefix[4] = prefix[3] + 5 = 10 + 5 = 15
i=5: prefix[5] = prefix[4] + 3 = 15 + 3 = 18

prefix = [3, 4, 8, 10, 15, 18]
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Off-by-One in Formula
```cpp
// WRONG
int sum = prefix[R] - prefix[L];  // Missing -1!

// CORRECT
int sum = prefix[R] - prefix[L-1];  // When L > 0
```

### Mistake 2: Forgetting L=0 Case
```cpp
// WRONG: Will access prefix[-1]!
int sum = prefix[R] - prefix[L-1];

// CORRECT: Handle L=0 separately
if(L == 0) {
    sum = prefix[R];
} else {
    sum = prefix[R] - prefix[L-1];
}
```

### Mistake 3: Integer Overflow
```cpp
// WRONG: Sum might exceed int range
int prefix[n];

// CORRECT: Use long long for large sums
long long prefix[n];
```

### Mistake 4: Not Initializing Hash Map
```cpp
// WRONG: Missing base case
unordered_map<int, int> prefixCount;
// Will miss subarrays starting from index 0!

// CORRECT: Initialize with 0
unordered_map<int, int> prefixCount;
prefixCount[0] = 1;  // Empty prefix has sum 0
```

---

## 8. ⏱️ Time & Space Complexity

| Operation | Time | Space | Reasoning |
|-----------|------|-------|-----------|
| **Build prefix array** | **O(n)** | **O(n)** | One pass through array |
| **Range sum query** | **O(1)** | **O(1)** | Simple subtraction |
| **Brute force query** | O(n) | O(1) | Loop through range |
| **Count subarrays** | **O(n)** | **O(n)** | Hash map storage |

**Key Trade-off**: O(n) extra space for O(1) query time!

---

## 9. 📝 Pattern Variations

### Variation 1: Prefix XOR

Same concept but with XOR instead of sum:

```cpp
#include <iostream>
#include <vector>
using namespace std;

// XOR has same property: a ^ a = 0
vector<int> buildPrefixXOR(vector<int>& arr) {
    int n = arr.size();
    vector<int> prefixXOR(n);
    
    prefixXOR[0] = arr[0];
    for(int i = 1; i < n; i++) {
        prefixXOR[i] = prefixXOR[i-1] ^ arr[i];
    }
    
    return prefixXOR;
}

// XOR from L to R
int rangeXOR(vector<int>& prefixXOR, int L, int R) {
    if(L == 0) return prefixXOR[R];
    return prefixXOR[R] ^ prefixXOR[L-1];
}
```

### Variation 2: 2D Prefix Sum (Matrix)

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Build 2D prefix sum
vector<vector<int>> build2DPrefix(vector<vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    vector<vector<int>> prefix(rows, vector<int>(cols));
    
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            prefix[i][j] = matrix[i][j];
            
            // Add from top
            if(i > 0) prefix[i][j] += prefix[i-1][j];
            
            // Add from left
            if(j > 0) prefix[i][j] += prefix[i][j-1];
            
            // Subtract double-counted corner
            if(i > 0 && j > 0) prefix[i][j] -= prefix[i-1][j-1];
        }
    }
    
    return prefix;
}

// Query sum of rectangle from (r1,c1) to (r2,c2)
int query2D(vector<vector<int>>& prefix, int r1, int c1, int r2, int c2) {
    int total = prefix[r2][c2];
    
    if(r1 > 0) total -= prefix[r1-1][c2];
    if(c1 > 0) total -= prefix[r2][c1-1];
    if(r1 > 0 && c1 > 0) total += prefix[r1-1][c1-1];
    
    return total;
}
```

---

## 10. 💡 Pro Tips

1. **Handle L=0 separately** — Most common mistake!
2. **Use long long** — Prevent overflow for large sums
3. **Initialize hash map with 0** — For subarray counting
4. **Prefix XOR works same way** — Just replace + with ^
5. **2D prefix sum** — Use inclusion-exclusion principle
6. **Space optimization** — Can sometimes compute on-the-fly

---

## 11. 🎯 When to Use Prefix Sum

✅ **Use when**:
- Multiple range sum queries
- Count subarrays with given sum
- Find subarray with specific property
- Need O(1) query time
- Static array (no updates)

❌ **Don't use when**:
- Array changes frequently (use Segment Tree)
- Only one query (brute force is fine)
- Need actual subarray elements (prefix only gives sum)

---

## 12. 📚 Practice Problems

### Easy (Start Here)
1. Range Sum Query - Immutable (LeetCode 303)
2. Find Pivot Index (LeetCode 724)
3. Subarray Sum Equals K (LeetCode 560)
4. Continuous Subarray Sum (LeetCode 523)
5. Binary Subarrays With Sum (LeetCode 930)

### Medium
1. Contiguous Array (LeetCode 525)
2. Product of Array Except Self (LeetCode 238)
3. Sum of Absolute Differences (LeetCode 1685)
4. Grid Game (LeetCode 2017)
5. Count Number of Nice Subarrays (LeetCode 1248)

### Hard
1. Range Sum Query 2D - Immutable (LeetCode 304)
2. Count of Range Sum (LeetCode 327)
3. Maximum Sum of 3 Non-Overlapping Subarrays (LeetCode 689)

---

## 13. 🎯 Key Takeaways

1. Prefix sum converts O(n) queries to O(1)
2. **Formula**: `sum(L,R) = prefix[R] - prefix[L-1]`
3. **Handle L=0** as special case
4. **Hash map + prefix** = count subarrays efficiently
5. Works for **XOR** and other operations too
6. **2D prefix sum** uses inclusion-exclusion
7. Trade-off: O(n) space for O(1) query time

---

**Next**: Solve problems in `Problems/` folder! →

[← Back to README](../README.md) | [Problems →](../../03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md)


---

## Supplementary Notes from 08-Prefix-Sum.md

# ➕ 08 — Prefix Sum

> **The central theme:**
> **Without prefix sums:** I keep recalculating addition from the past ($O(n)$ per query).
> **With prefix sums:** I remember previous additions and reuse them instantly ($O(1)$ per query).

---

## 🎯 Range Sum Queries: Why Prefix Sums Matter

Imagine you have an array `arr` and need to answer multiple queries of the form: **"What is the sum of elements from index $L$ to $R$?"**

- **The Brute Force Approach:** Iterate from $L$ to $R$ and add the elements. If there are $Q$ queries, this takes $O(Q \times n)$ time. If $n = 10^5$ and $Q = 10^5$, this is $10^{10}$ operations, which will crash (Time Limit Exceeded).
- **The Prefix Sum Approach:** 
  Precompute a running sum array $P$ where $P[i] = arr[0] + arr[1] + \dots + arr[i]$.
  
  $$\text{Sum}(L, R) = P[R] - P[L - 1] \quad (\text{if } L > 0)$$
  $$\text{Sum}(0, R) = P[R]$$

### Visualizing Range Sum Subtraction
To find the sum between indices $2$ and $4$ for the array `[1, 2, 3, 4, 5]`:

```
Array:    [  1,  2,  3,  4,  5  ]
Indices:     0   1   2   3   4
                     L───────►R
Prefix P: [  1,  3,  6, 10, 15  ]

Sum(2, 4) = P[4] - P[1]
          = 15 - 3 = 12
          (Indeed: 3 + 4 + 5 = 12)
```

We subtract the sum of elements before $L$ (which is $P[L-1]$) from the sum of elements up to $R$ (which is $P[R]$). This gives us the range sum in **$O(1)$ time**!

---

## 🎯 Practice Problems & Worked Solutions

Work through these prefix sum variants to build your pattern recognition.

| # | Problem | Difficulty | Link | Key Idea |
|---|---|---|---|---|
| 1 | Running Sum of 1D Array | Easy | [LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) | Build prefix sum in-place. |
| 2 | Find Highest Altitude | Easy | [LeetCode](https://leetcode.com/problems/find-the-highest-altitude/) | Track peak running sum. |
| 3 | Find Pivot Index | Easy | [LeetCode](https://leetcode.com/problems/find-pivot-index/) | balance left sum and right sum. |
| 4 | Left & Right Sum Differences | Easy | [LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/) | Absolute difference at each pivot. |
| 5 | Minimum Start Value | Easy | [LeetCode](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) | Find minimum running sum state. |
| 6 | Product of Array Except Self | Medium | [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) | Prefix products $\times$ Suffix products. |

---

### Solution 1: Running Sum of 1D Array

**Complexity:**
- **Time:** $O(n)$ — Single pass.
- **Space:** $O(1)$ — Modifying the array in-place.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] runningSum(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
        nums[i] += nums[i - 1]; // Accumulate previous sums
    }
    return nums;
}
```

#### Python
```python
def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] # Accumulate previous sums
    return nums
```

#### C++
```cpp
vector<int> runningSum(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        nums[i] += nums[i - 1]; // Accumulate previous sums
    }
    return nums;
}
```
</details>

---

### Solution 2: Find the Highest Altitude

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int largestAltitude(int[] gain) {
    int currentAltitude = 0;
    int maxAltitude = 0;
    for (int g : gain) {
        currentAltitude += g;
        maxAltitude = Math.max(maxAltitude, currentAltitude);
    }
    return maxAltitude;
}
```

#### Python
```python
def largest_altitude(gain):
    current_altitude = 0
    max_altitude = 0
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude
```

#### C++
```cpp
int largestAltitude(vector<int>& gain) {
    int currentAltitude = 0;
    int maxAltitude = 0;
    for (int g : gain) {
        currentAltitude += g;
        maxAltitude = max(maxAltitude, currentAltitude);
    }
    return maxAltitude;
}
```
</details>

---

### Solution 3: Find Pivot Index

**Intuition:**
We need to find the index `i` where the sum of elements to the left equals the sum of elements to the right.
- Let the total sum of the array be `totalSum`.
- As we iterate, we maintain `leftSum`.
- The sum of elements to the right of `i` is simply:
  $$\text{rightSum} = \text{totalSum} - \text{leftSum} - arr[i]$$
- If `leftSum == rightSum`, then `i` is the pivot index.

**Complexity:**
- **Time:** $O(n)$ — Two passes (one for total sum, one to find pivot).
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int pivotIndex(int[] nums) {
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    
    int leftSum = 0;
    for (int i = 0; i < nums.length; i++) {
        int rightSum = totalSum - leftSum - nums[i];
        if (leftSum == rightSum) {
            return i; // Found pivot index
        }
        leftSum += nums[i];
    }
    return -1;
}
```

#### Python
```python
def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1
```

#### C++
```cpp
int pivotIndex(vector<int>& nums) {
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    
    int leftSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        int rightSum = totalSum - leftSum - nums[i];
        if (leftSum == rightSum) {
            return i;
        }
        leftSum += nums[i];
    }
    return -1;
}
```
</details>

---

### Solution 4: Left and Right Sum Differences

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(n)$ to store the result array.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] leftRightDifference(int[] nums) {
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    
    int leftSum = 0;
    int[] ans = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
        int rightSum = totalSum - leftSum - nums[i];
        ans[i] = Math.abs(leftSum - rightSum);
        leftSum += nums[i];
    }
    return ans;
}
```

#### Python
```python
def left_right_difference(nums):
    total_sum = sum(nums)
    left_sum = 0
    ans = []
    for num in nums:
        right_sum = total_sum - left_sum - num
        ans.append(abs(left_sum - right_sum))
        left_sum += num
    return ans
```

#### C++
```cpp
vector<int> leftRightDifference(vector<int>& nums) {
    int totalSum = 0;
    for (int num : nums) {
        totalSum += num;
    }
    
    int leftSum = 0;
    vector<int> ans(nums.size());
    for (int i = 0; i < nums.size(); i++) {
        int rightSum = totalSum - leftSum - nums[i];
        ans[i] = abs(leftSum - rightSum);
        leftSum += nums[i];
    }
    return ans;
}
```
</details>

---

### Solution 5: Minimum Start Value (Minimum Value for Positive Step sum)

**Intuition:**
We need the running sum to never fall below 1.
- Track the running prefix sum.
- Identify the minimum value `minPrefix` the running sum ever reaches.
- The minimum start value $X$ needed is:
  $$X = 1 - \text{minPrefix}$$
  *(For example, if the running sum drops to $-4$ at its lowest, you need a starting value of $1 - (-4) = 5$ to prevent it from dropping below 1).*

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int minStartValue(int[] nums) {
    int prefix = 0;
    int minPrefix = 0;
    for (int num : nums) {
        prefix += num;
        minPrefix = Math.min(minPrefix, prefix);
    }
    return 1 - minPrefix;
}
```

#### Python
```python
def min_start_value(nums):
    prefix = 0
    min_prefix = 0
    for num in nums:
        prefix += num
        min_prefix = min(min_prefix, prefix)
    return 1 - min_prefix
```

#### C++
```cpp
int minStartValue(vector<int>& nums) {
    int prefix = 0;
    int minPrefix = 0;
    for (int num : nums) {
        prefix += num;
        minPrefix = min(minPrefix, prefix);
    }
    return 1 - minPrefix;
}
```
</details>

---

### Solution 6: Product of Array Except Self

**Intuition:**
We cannot use division (e.g. dividing the total product by `nums[i]` is not allowed, and breaks if `nums[i]` is 0).
Instead, notice that for any index `i`, the product of all elements except `nums[i]` is:

$$\text{Product Except Self} = (\text{Product of all elements to the left}) \times (\text{Product of all elements to the right})$$

1. Create a result array `ans`. Set `ans[0] = 1`.
2. Do a left-to-right pass. Populate `ans[i]` with the product of all elements to the left of `i`: `ans[i] = ans[i-1] * nums[i-1]`.
3. Do a right-to-left pass. Maintain a running variable `right` (initially `1`). Multiply `ans[i]` by `right`, then update `right = right * nums[i]`.

**Complexity:**
- **Time:** $O(n)$ — Two passes.
- **Space:** $O(1)$ auxiliary space (excluding the output array).

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] ans = new int[n];
    
    // Step 1: Compute prefix (left) products in the ans array
    ans[0] = 1;
    for (int i = 1; i < n; i++) {
        ans[i] = ans[i - 1] * nums[i - 1];
    }
    
    // Step 2: Compute suffix (right) products and multiply on the fly
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] = ans[i] * right; // left product * right product
        right = right * nums[i];  // update running suffix product
    }
    return ans;
}
```

#### Python
```python
def product_except_self(nums):
    n = len(nums)
    ans = [1] * n
    
    # Step 1: Compute left products
    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]
        
    # Step 2: Multiply by right products
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] = ans[i] * right
        right = right * nums[i]
        
    return ans
```

#### C++
```cpp
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n);
    
    // Step 1: Compute left products
    ans[0] = 1;
    for (int i = 1; i < n; i++) {
        ans[i] = ans[i - 1] * nums[i - 1];
    }
    
    // Step 2: Multiply by right products
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] = ans[i] * right;
        right = right * nums[i];
    }
    return ans;
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `nums = [1, 2, 3, 4]`

- **Left pass (Prefix):**
  - `ans[0] = 1`
  - `ans[1] = ans[0] * nums[0] = 1 * 1 = 1`
  - `ans[2] = ans[1] * nums[1] = 1 * 2 = 2`
  - `ans[3] = ans[2] * nums[2] = 2 * 3 = 6`
  - `ans` state: `[1, 1, 2, 6]`

- **Right pass (Suffix):**
  - Initial `right = 1`
  - `i = 3`: `ans[3] = ans[3] * right = 6 * 1 = 6`. Update `right = 1 * 4 = 4`
  - `i = 2`: `ans[2] = ans[2] * right = 2 * 4 = 8`. Update `right = 4 * 3 = 12`
  - `i = 1`: `ans[1] = ans[1] * right = 1 * 12 = 12`. Update `right = 12 * 2 = 24`
  - `i = 0`: `ans[0] = ans[0] * right = 1 * 24 = 24`.

**Final output:** `[24, 12, 8, 6]` ✅
</details>

---

## 🎓 Viva Questions & Answers

### Q1: What is the core intuition behind the Prefix Sum technique?
**Answer:**
Prefix Sum is a precomputation technique where we construct an auxiliary array $P$ where $P[i]$ holds the sum of elements from index $0$ to $i$. This transforms any subarray sum query $\sum_{k=L}^{R} arr[k]$ from $O(n)$ time into an instantaneous $O(1)$ calculation: $P[R] - P[L-1]$.

### Q2: Why is 1-based indexing (Prefix array of size $N+1$) preferred in implementation?
**Answer:**
Using a prefix array `P` of size $N+1$ with `P[0] = 0` eliminates special-case branching when $L = 0$. The subarray sum from index $L$ to $R$ (0-indexed in the original array) becomes simply `P[R + 1] - P[L]`.

### Q3: How does Prefix Sum help solve Subarray Sum Equals K ($O(n)$ time complexity)?
**Answer:**
For any current index $i$ with prefix sum $S_i$, we are looking for a previous index $j$ such that $S_i - S_j = K \implies S_j = S_i - K$. By storing the frequencies of all previous prefix sums in a HashMap, we can check if $S_i - K$ exists in $O(1)$ time per element, achieving $O(n)$ total time instead of $O(n^2)$.

### Q4: What is a Difference Array, and how does it relate to Prefix Sum?
**Answer:**
A Difference Array $D$ is used for $O(1)$ range update operations $+V$ on subarray $[L, R]$. We update $D[L] += V$ and $D[R + 1] -= V$. Taking the prefix sum of $D$ at the end reconstructs the modified array in $O(n)$ total time.

### Q5: How do 2D Prefix Sums work?
**Answer:**
For a 2D matrix, $P[i][j]$ stores the sum of all elements in the submatrix from $(0, 0)$ to $(i, j)$:
$$P[i][j] = \text{mat}[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]$$
To query the sum of submatrix between top-left $(r_1, c_1)$ and bottom-right $(r_2, c_2)$ in $O(1)$:
$$\text{Sum} = P[r_2][c_2] - P[r_1-1][c_2] - P[r_2][c_1-1] + P[r_1-1][c_1-1]$$

---

## ⚠️ Beginner Pitfalls & Common Mistakes

1. **Off-by-One on Range Sum Queries:**
   - When calculating `Sum(L, R)`, using `P[R] - P[L]` is a common mistake. If you do this, you subtract the element at index $L$, which should be included.
   - The correct formula is `P[R] - P[L-1]`.
   - Always handle the boundary case when $L = 0$ separately (since `P[-1]` is invalid), or declare your prefix array of size $n+1$ with `P[0] = 0` (1-based indexing).

2. **Integer Overflow:**
   - Cumulative sums grow rapidly. If your array has size $10^5$ and elements can be $10^5$, the prefix sum can reach $10^{10}$, which overflows a standard 32-bit signed integer. In Java/C++, use `long[]` prefix arrays to prevent overflow.

---

> 👉 Next, open `09-Sliding-Window.md` to learn how we track contiguous sub-arrays dynamically! 💪



---

## Supplementary Notes from Patterns.md

# Prefix Sum — Patterns Reference

> **Complete catalog of prefix sum patterns**

---

## 📋 Pattern Variations

### 1. 1D Prefix Sum

**Use When**: Range sum queries on 1D array  
**Time Complexity**: O(1) per query after O(n) preprocessing

#### Template
```cpp
// Build prefix sum
vector<int> prefix(n);
prefix[0] = nums[0];
for(int i = 1; i < n; i++) {
    prefix[i] = prefix[i-1] + nums[i];
}

// Query range [left, right]
int rangeSum(int left, int right) {
    if(left == 0) return prefix[right];
    return prefix[right] - prefix[left-1];
}
```

#### Example Problems
- Range Sum Query - Immutable
- Find Pivot Index
- Product of Array Except Self

---

### 2. Prefix Sum + Hash Map

**Use When**: Count/find subarrays with specific sum  
**Time Complexity**: O(n)

#### Template
```cpp
unordered_map<int, int> prefixCount;
prefixCount[0] = 1;  // Important base case

int currentSum = 0;
int count = 0;

for(int num : nums) {
    currentSum += num;
    
    // Check if (currentSum - k) exists
    if(prefixCount.count(currentSum - k)) {
        count += prefixCount[currentSum - k];
    }
    
    // Record current prefix sum
    prefixCount[currentSum]++;
}
```

#### Example Problems
- Subarray Sum Equals K
- Continuous Subarray Sum
- Subarray Sum Divisible by K

---

### 3. 2D Prefix Sum

**Use When**: Range sum queries on 2D matrix  
**Time Complexity**: O(1) per query after O(m×n) preprocessing

#### Template
```cpp
// Build 2D prefix sum
vector<vector<int>> prefix(m+1, vector<int>(n+1, 0));
for(int i = 0; i < m; i++) {
    for(int j = 0; j < n; j++) {
        prefix[i+1][j+1] = matrix[i][j] +
            prefix[i][j+1] + prefix[i+1][j] - prefix[i][j];
    }
}

// Query rectangle (row1, col1) to (row2, col2)
int sumRegion(int row1, int col1, int row2, int col2) {
    return prefix[row2+1][col2+1] -
           prefix[row1][col2+1] -
           prefix[row2+1][col1] +
           prefix[row1][col1];
}
```

#### Example Problems
- Range Sum Query 2D
- Maximum Size Rectangle

---

### 4. Prefix XOR

**Use When**: XOR range queries  
**Time Complexity**: O(1) per query

#### Template
```cpp
// Build prefix XOR
vector<int> prefixXOR(n);
prefixXOR[0] = nums[0];
for(int i = 1; i < n; i++) {
    prefixXOR[i] = prefixXOR[i-1] ^ nums[i];
}

// Query XOR range [left, right]
int xorRange(int left, int right) {
    if(left == 0) return prefixXOR[right];
    return prefixXOR[right] ^ prefixXOR[left-1];
}
```

#### Example Problems
- XOR Queries of a Subarray
- Find XOR Sum

---

## 🎯 Cross-Pattern Combinations

### Prefix Sum + Sliding Window
```cpp
// Check if any subarray of size k sums to target
bool hasTargetSum(vector<int>& nums, int k, int target) {
    int currentSum = 0;
    for(int i = 0; i < k; i++) {
        currentSum += nums[i];
    }
    
    if(currentSum == target) return true;
    
    for(int i = k; i < nums.size(); i++) {
        currentSum += nums[i] - nums[i-k];
        if(currentSum == target) return true;
    }
    
    return false;
}
```

### Prefix Sum + Binary Search
```cpp
// Find subarray with sum closest to target
int closestSum(vector<int>& nums, int target) {
    vector<int> prefix = {0};
    for(int num : nums) {
        prefix.push_back(prefix.back() + num);
    }
    
    int closest = INT_MAX;
    set<int> seen;
    
    for(int p : prefix) {
        auto it = seen.lower_bound(p - target);
        if(it != seen.end()) {
            closest = min(closest, abs(p - *it - target));
        }
        seen.insert(p);
    }
    
    return closest;
}
```

---

## 📊 Pattern Decision Flowchart

```
Problem mentions "sum of range" or "subarray sum"
         ↓
    Multiple queries?
    ↓           ↓
   YES          NO (single query)
    ↓           ↓
  Build       Just iterate
  prefix      
  array       
    ↓
    1D or 2D?
    ↓           ↓
   1D          2D
    ↓           ↓
  1D Prefix   2D Prefix
  Sum         Sum
    ↓
    Need to count subarrays?
    ↓           ↓
   YES          NO
    ↓           ↓
  Prefix      Simple
  + Hash      prefix
  Map         queries
```

---

## 🎨 Quick Reference Cards

### Card 1: 1D Prefix Sum
```
WHEN: Range sum queries
BUILD: prefix[i] = prefix[i-1] + nums[i]
QUERY: prefix[right] - prefix[left-1]
TIME: O(1) per query
SPACE: O(n)
```

### Card 2: Prefix + Hash Map
```
WHEN: Count subarrays with sum k
KEY INSIGHT: prefix[j] - prefix[i] = k
BASE CASE: prefixCount[0] = 1
TIME: O(n)
SPACE: O(n)
```

### Card 3: 2D Prefix Sum
```
WHEN: Matrix range queries
BUILD: Add current + top + left - diagonal
QUERY: Use inclusion-exclusion (4 corners)
TIME: O(1) per query
SPACE: O(m×n)
```

### Card 4: Prefix XOR
```
WHEN: XOR range queries
PROPERTY: a ^ a = 0
BUILD: prefixXOR[i] = prefixXOR[i-1] ^ nums[i]
TIME: O(1) per query
SPACE: O(n)
```

---

## 💡 Pro Tips

1. **Always handle left=0** as special case
2. **Base case**: prefixCount[0] = 1 for hash map problems
3. **Handle negative remainders** properly: ((sum % k) + k) % k
4. **2D formula**: Include-exclude pattern (4 terms)
5. **Transform problems** - e.g., treat 0 as -1 for equal count

---

## 🎓 Mastery Checklist

- [ ] Can implement 1D prefix sum from memory
- [ ] Can handle left=0 boundary correctly
- [ ] Can use hash map with prefix sum
- [ ] Can implement 2D prefix sum
- [ ] Understand why prefixCount[0] = 1
- [ ] Can solve subarray counting problems
- [ ] Can transform problems to fit pattern

---

**Master prefix sum for efficient range queries!**

[← Back to Notes](../../03-Arrays-and-Strings/concepts/02-subarrays-and-kadane-algorithm.md) | [Easy_Medium Problems](../problems/004-prefix-sum-problems.md)


---

## Supplementary Notes from Mistakes.md

# Prefix Sum — Common Mistakes

> **Top mistakes students make with prefix sum**

---

## 🔴 Critical Mistakes

### Mistake 1: Forgetting to Handle left=0 Case
**Wrong**:
```cpp
int sumRange(int left, int right) {
    return prefix[right] - prefix[left-1];  // CRASH when left=0!
}
```


**Correct**:
```cpp
int sumRange(int left, int right) {
    if(left == 0) return prefix[right];
    return prefix[right] - prefix[left-1];
}
```

**Why**: Accessing prefix[-1] causes undefined behavior!

---

### Mistake 2: Incorrect 2D Prefix Sum Formula
**Wrong**:
```cpp
prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1];
// Missing: - prefix[i-1][j-1]
```

**Correct**:
```cpp
prefix[i][j] = matrix[i][j] + 
               prefix[i-1][j] + prefix[i][j-1] - 
               prefix[i-1][j-1];  // Don't double count!
```

**Why**: Corner cell counted twice!

---

### Mistake 3: Forgetting Base Case prefixCount[0] = 1
**Wrong**:
```cpp
unordered_map<int, int> prefixCount;
// Missing base case!
```

**Correct**:
```cpp
unordered_map<int, int> prefixCount;
prefixCount[0] = 1;  // Empty prefix has sum 0
```

**Why**: Misses subarrays starting from index 0!

---

### Mistake 4: Not Handling Negative Remainders
**Wrong**:
```cpp
int remainder = currentSum % k;  // Can be negative!
```

**Correct**:
```cpp
int remainder = ((currentSum % k) + k) % k;  // Always positive
```

**Why**: C++ modulo can return negative values!

---

### Mistake 5: Using Wrong Indices in 2D Query
**Wrong**:
```cpp
int sumRegion(int row1, int col1, int row2, int col2) {
    return prefix[row2][col2] - prefix[row1][col2] - 
           prefix[row2][col1] + prefix[row1][col1];
}
```

**Correct**:
```cpp
int sumRegion(int row1, int col1, int row2, int col2) {
    return prefix[row2+1][col2+1] - prefix[row1][col2+1] - 
           prefix[row2+1][col1] + prefix[row1][col1];
}
```

**Why**: Prefix array is 1-indexed (size m+1, n+1)!

---

### Mistake 6: Counting Subarrays Incorrectly
**Wrong**:
```cpp
if(prefixCount.count(currentSum - k)) {
    count++;  // WRONG! Only counts 1
}
```

**Correct**:
```cpp
if(prefixCount.count(currentSum - k)) {
    count += prefixCount[currentSum - k];  // Add all occurrences
}
```

**Why**: Multiple subarrays can have same prefix sum!

---

### Mistake 7: Not Storing First Occurrence for Max Length
**Wrong**:
```cpp
prefixIndex[currentSum] = i;  // Overwrites earlier occurrence!
```

**Correct**:
```cpp
if(!prefixIndex.count(currentSum)) {
    prefixIndex[currentSum] = i;  // Store only first time
}
```

**Why**: Earlier occurrence gives longer subarray!

---

### Mistake 8: Confusing Prefix Sum with Current Sum
**Wrong**:
```cpp
int currentSum = 0;
for(int num : nums) {
    currentSum += num;
    if(currentSum == k) count++;  // Only checks from start
}
```

**Correct**:
```cpp
int currentSum = 0;
for(int num : nums) {
    currentSum += num;
    if(prefixCount.count(currentSum - k)) {
        count += prefixCount[currentSum - k];  // Checks all subarrays
    }
    prefixCount[currentSum]++;
}
```

---

### Mistake 9: Off-by-One in Prefix Array Size
**Wrong**:
```cpp
vector<int> prefix(n);  // Should be n+1 for easier indexing
```

**Correct**:
```cpp
vector<int> prefix(n);  // 0-indexed, handle left=0
// OR
vector<int> prefix(n+1, 0);  // 1-indexed, easier queries
```

---

### Mistake 10: Integer Overflow
**Wrong**:
```cpp
int currentSum = 0;  // May overflow with large inputs
for(int num : nums) {
    currentSum += num;
}
```

**Correct**:
```cpp
long long currentSum = 0;  // Use larger type
for(int num : nums) {
    currentSum += num;
}
```

**Why**: Sum can exceed INT_MAX!

---

## ✅ Debug Checklist

When stuck, check:

- [ ] Handling left=0 case correctly?
- [ ] Base case prefixCount[0] = 1 included?
- [ ] 2D formula has all 4 terms?
- [ ] Using (row2+1, col2+1) in 2D queries?
- [ ] Handling negative remainders?
- [ ] Adding count (not just incrementing)?
- [ ] Storing first occurrence for max length?
- [ ] Using long long if needed?
- [ ] Prefix array size correct?
- [ ] Testing with small example manually?

---

## 💡 Best Practices

1. **Draw it out** - Visualize prefix sum array
2. **Test with left=0** - Always edge case
3. **Use hash map wisely** - Store what you need
4. **Handle negatives** - Especially for modulo
5. **Think in terms of differences** - prefix[j] - prefix[i]

---

**Avoid these mistakes and prefix sum becomes second nature!**

[← Back to Patterns](../../03-Arrays-and-Strings/concepts/04-pattern-recognition-guide.md) | [← Back to Notes](../../03-Arrays-and-Strings/concepts/01-array-master-notes.md)
