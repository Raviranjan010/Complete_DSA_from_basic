# Kadane's Algorithm — Complete Guide

> **What You'll Learn**: Maximum subarray sum, product subarray, variations  
> **Prerequisites**: Array Basics, Dynamic Programming basics  
> **Time Required**: 2-3 hours

---

## 1. 📌 Definition

**Kadane's Algorithm** finds the **maximum sum of a contiguous subarray** in O(n) time using dynamic programming.

**Core Idea**: At each position, decide whether to extend the current subarray or start fresh.

---

## 2. 🌍 Real-World Analogy

### Analogy 1: Stock Trading 📈

Imagine tracking daily profit/loss:
- Day 1: +$100 (good day!)
- Day 2: -$50 (bad day, but overall still positive)
- Day 3: +$200 (recover and grow!)
- Day 4: -$300 (terrible! Start fresh tomorrow)

At each day, you ask: "Should I continue holding or restart my strategy?"

### Analogy 2: Hiking Trail 🥾

You're hiking with elevation changes:
- Some segments go up (positive)
- Some segments go down (negative)
- You want to find the segment with maximum net elevation gain
- If current path goes too negative, restart from next point

---

## 3. 🎨 Visual Diagram

### Kadane's Algorithm Execution

```
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ↑
        Start here

Step-by-Step:
i=0: currentSum = -2,    maxSum = -2    (start new)
i=1: currentSum = 1,     maxSum = 1     (restart: -2+1 < 1)
i=2: currentSum = -2,    maxSum = 1     (extend: 1+(-3) = -2)
i=3: currentSum = 4,     maxSum = 4     (restart: -2+4 < 4)
i=4: currentSum = 3,     maxSum = 4     (extend: 4+(-1) = 3)
i=5: currentSum = 5,     maxSum = 5     (extend: 3+2 = 5)
i=6: currentSum = 6,     maxSum = 6     (extend: 5+1 = 6) ← Maximum!
i=7: currentSum = 1,     maxSum = 6     (extend: 6+(-5) = 1)
i=8: currentSum = 5,     maxSum = 6     (extend: 1+4 = 5)

Result: Maximum subarray sum = 6
Subarray: [4, -1, 2, 1]
```

---

## 4. 🔑 Pattern Recognition Keywords

**Look for these words in problems**:
- "Maximum subarray sum"
- "Contiguous subarray"
- "Maximum product"
- "Largest sum"
- "Continuous subarray"
- "Maximum/minimum sum"

---

## 5. 📋 Template Code

### Template 1: Basic Kadane's Algorithm

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int currentSum = nums[0];
    int maxSum = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        // Either extend current subarray or start new one
        currentSum = max(nums[i], currentSum + nums[i]);
        
        // Update global maximum
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}
```

### Template 2: Kadane's with Subarray Indices

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

pair<int, int> maxSubArrayWithIndices(vector<int>& nums) {
    int currentSum = nums[0];
    int maxSum = nums[0];
    
    int start = 0, end = 0, tempStart = 0;
    
    for(int i = 1; i < nums.size(); i++) {
        // Start new subarray if current element is better
        if(nums[i] > currentSum + nums[i]) {
            currentSum = nums[i];
            tempStart = i;
        } else {
            currentSum = currentSum + nums[i];
        }
        
        // Update maximum
        if(currentSum > maxSum) {
            maxSum = currentSum;
            start = tempStart;
            end = i;
        }
    }
    
    return {start, end};
}
```

---

## 6. 🔍 Step-by-Step Example

### Problem: Maximum Subarray

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int currentSum = nums[0];
    int maxSum = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        // Decision: Start new or extend?
        if(currentSum < 0) {
            // Current sum is negative, start fresh
            currentSum = nums[i];
        } else {
            // Current sum is positive, extend it
            currentSum += nums[i];
        }
        
        // Track maximum
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}

int main() {
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    
    int result = maxSubArray(nums);
    cout << "Maximum subarray sum: " << result << endl;  // 6
    
    return 0;
}
```

**Detailed Dry Run**:
```
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=0: currentSum = -2, maxSum = -2
     State: Just started

i=1: nums[1] = 1
     currentSum < 0? YES (-2 < 0)
     → Start fresh: currentSum = 1
     maxSum = max(-2, 1) = 1
     State: New subarray starts at index 1

i=2: nums[2] = -3
     currentSum < 0? NO (1 > 0)
     → Extend: currentSum = 1 + (-3) = -2
     maxSum = max(1, -2) = 1
     State: Subarray [1, -3], but it's negative now

i=3: nums[3] = 4
     currentSum < 0? YES (-2 < 0)
     → Start fresh: currentSum = 4
     maxSum = max(1, 4) = 4
     State: New subarray starts at index 3

i=4: nums[4] = -1
     currentSum < 0? NO (4 > 0)
     → Extend: currentSum = 4 + (-1) = 3
     maxSum = max(4, 3) = 4
     State: Subarray [4, -1]

i=5: nums[5] = 2
     currentSum < 0? NO (3 > 0)
     → Extend: currentSum = 3 + 2 = 5
     maxSum = max(4, 5) = 5
     State: Subarray [4, -1, 2]

i=6: nums[6] = 1
     currentSum < 0? NO (5 > 0)
     → Extend: currentSum = 5 + 1 = 6
     maxSum = max(5, 6) = 6 ← NEW MAXIMUM!
     State: Subarray [4, -1, 2, 1]

i=7: nums[7] = -5
     currentSum < 0? NO (6 > 0)
     → Extend: currentSum = 6 + (-5) = 1
     maxSum = max(6, 1) = 6
     State: Subarray [4, -1, 2, 1, -5]

i=8: nums[8] = 4
     currentSum < 0? NO (1 > 0)
     → Extend: currentSum = 1 + 4 = 5
     maxSum = max(6, 5) = 6
     State: Subarray [4, -1, 2, 1, -5, 4]

Final Answer: 6 ✓
Subarray: [4, -1, 2, 1]
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Initializing with 0
```cpp
// WRONG: Fails when all numbers are negative
int maxSum = 0;
int currentSum = 0;

// CORRECT: Initialize with first element
int maxSum = nums[0];
int currentSum = nums[0];
```

### Mistake 2: Starting Loop from 0
```cpp
// WRONG: Double-counts first element
int currentSum = nums[0];
for(int i = 0; i < n; i++) {  // Should start from 1!
    currentSum += nums[i];
}

// CORRECT:
for(int i = 1; i < n; i++) {
    currentSum = max(nums[i], currentSum + nums[i]);
}
```

### Mistake 3: Forgetting to Update maxSum
```cpp
// WRONG: Only updates at the end
currentSum = max(nums[i], currentSum + nums[i]);
// Forgot: maxSum = max(maxSum, currentSum);

// CORRECT: Update at every step
currentSum = max(nums[i], currentSum + nums[i]);
maxSum = max(maxSum, currentSum);
```

### Mistake 4: Wrong Condition for Restart
```cpp
// WRONG: Restart only when currentSum == 0
if(currentSum == 0) {
    currentSum = nums[i];
}

// CORRECT: Restart when currentSum < 0
if(currentSum < 0) {
    currentSum = nums[i];
}
```

---

## 8. ⏱️ Time & Space Complexity

| Variant | Time | Space | Reasoning |
|---------|------|-------|-----------|
| **Basic Kadane's** | **O(n)** | **O(1)** | Single pass, two variables |
| **With indices** | **O(n)** | **O(1)** | Track start/end positions |
| **Brute force** | O(n²) or O(n³) | O(1) | Check all subarrays |

**Why O(n)?**
- Each element visited exactly once
- Constant work per element
- No nested loops

---

## 9. 📝 Pattern Variations

### Variation 1: Maximum Product Subarray

Tricky because negative × negative = positive!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxProduct(vector<int>& nums) {
    int maxProd = nums[0];
    int minProd = nums[0];  // Track minimum too!
    int result = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        if(nums[i] < 0) {
            swap(maxProd, minProd);  // Negative flips max/min
        }
        
        maxProd = max(nums[i], maxProd * nums[i]);
        minProd = min(nums[i], minProd * nums[i]);
        
        result = max(result, maxProd);
    }
    
    return result;
}
```

### Variation 2: Circular Subarray Sum

Array wraps around (last element connects to first):

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int maxCircularSubarray(vector<int>& nums) {
    // Case 1: Normal maximum subarray (Kadane's)
    int maxKadane = kadane(nums);
    
    // Case 2: Circular maximum (total - minimum subarray)
    int totalSum = 0;
    for(int& x : nums) {
        totalSum += x;
        x = -x;  // Negate for finding minimum
    }
    int maxCircular = totalSum + kadane(nums);  // total - min = total + (-min)
    
    // Edge case: If all numbers are negative
    if(maxCircular == 0) {
        return maxKadane;
    }
    
    return max(maxKadane, maxCircular);
}

int kadane(vector<int>& nums) {
    int currentSum = nums[0];
    int maxSum = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}
```

---

## 10. 💡 Pro Tips

1. **Initialize with nums[0]** — Not 0!
2. **Start loop from index 1** — First element already used
3. **Update maxSum every iteration** — Don't wait till end
4. **Track min for product** — Negative numbers flip max/min
5. **Circular array** — Use total - minimum trick
6. **All negative** — Kadane's still works correctly!

---

## 11. 🎯 When to Use Kadane's Algorithm

✅ **Use when**:
- Finding maximum/minimum contiguous subarray
- Array has positive and negative numbers
- Need optimal subarray sum/product
- Problem mentions "contiguous" or "subarray"

❌ **Don't use when**:
- Looking for non-contiguous elements (use greedy/DP)
- Need to find actual elements (modify to track indices)
- Array is circular (use modified version)
- All elements negative (still works, but understand why)

---

## 12. 📚 Practice Problems

### Easy (Start Here)
1. Maximum Subarray (LeetCode 53)
2. Best Time to Buy and Sell Stock (LeetCode 121)
3. Maximum Difference Between Increasing Elements (LeetCode 2016)

### Medium
1. Maximum Product Subarray (LeetCode 152)
2. Longest Turbulent Subarray (LeetCode 978)
3. Maximum Sum of Two Non-Overlapping Subarrays (LeetCode 1031)
4. Contiguous Array (LeetCode 525)
5. Maximum Sum Circular Subarray (LeetCode 918)

### Hard
1. Maximum Sum of 3 Non-Overlapping Subarrays (LeetCode 689)
2. Subarray Sum Divisible by K (LeetCode 974)
3. Number of Subarrays with Bounded Maximum (LeetCode 795)

---

## 13. 🎯 Key Takeaways

1. Kadane's finds **maximum contiguous subarray** in O(n)
2. **Core decision**: Extend current or start new?
3. **Initialize** with `nums[0]`, not 0
4. **Update maxSum** at every step
5. **Product variant** — Track both max and min
6. **Circular variant** — Use total - minimum trick
7. Works even with **all negative numbers**
8. **Space optimal** — Only O(1) extra space

---

**Next**: Solve problems in `Problems/` folder! →

[← Back to README](../README.md) | [Problems →](../problems/001-two-sum-pair-sum.md)


---

## Supplementary Notes from 05_Subarrays_and_Kadanes_Algorithm.md

# Subarrays and Kadane's Algorithm in C++ ➕

## 1️⃣ Understanding Subarrays

A subarray is a contiguous part of an array. For an array of size `n`, there are `n(n+1)/2` non-empty subarrays. This guide explores how to generate subarrays and calculate their sums efficiently.

### Printing All Subarrays

To print all subarrays of a given array, you can use nested loops. The outer loop determines the starting point of the subarray, and the inner loop determines the ending point.

```cpp
#include <iostream>
using namespace std;

void printSubarray(int *arr, int n) {
    for (int start = 0; start < n; start++) {
        for (int end = start; end < n; end++) {
            cout << "(" << start << "," << end << ")" << "->";
            for (int i = start; i <= end; i++) {
                cout << arr[i] << " ";
            }
            cout << endl;
        }
    }
}

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(int);
    printSubarray(arr, n);
    return 0;
}
```

### Calculating Subarray Sums

To calculate the sum of each subarray, you can add another loop inside the nested loops to sum the elements of each subarray.

```cpp
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int* arr, int n) {
    int maxSum = INT_MIN;
    for (int start = 0; start < n; start++) {
        for (int end = start; end < n; end++) {
            int currSum = 0;
            for (int i = start; i <= end; i++) {
                currSum += arr[i];
            }
            maxSum = max(maxSum, currSum);
        }
    }
    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(int);
    maxSubArraySum(arr, n);
    return 0;
}
```

## Optimizing Subarray Sum Calculation

The above approach has a time complexity of O(n^3). You can optimize it to O(n^2) by avoiding the inner re-summation loop.

```cpp
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int *arr, int n) {
    int maxSum = INT_MIN;
    for (int start = 0; start < n; start++) {
        int currSum = 0;
        for (int end = start; end < n; end++) {
            currSum += arr[end];
            maxSum = max(maxSum, currSum);
        }
    }
    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 6, 8, 10};
    int n = sizeof(arr) / sizeof(int);
    maxSubArraySum(arr, n);
    return 0;
}
```

## Kadane's Algorithm: Finding Maximum Subarray Sum in O(n)

Kadane's Algorithm is the most efficient way to find the maximum sum of a subarray in an array. It has a time complexity of O(n).

### Core Idea

The main idea behind Kadane's Algorithm is to maintain a running `currSum` and a `maxSum`. If `currSum` becomes negative, reset it to 0 because a negative sum will only decrease the sum of subsequent subarrays.

### Algorithm Steps

1.  Initialize `currSum = 0` and `maxSum = INT_MIN`.
2.  Iterate through the array.
3.  Add the current element to `currSum`.
4.  Update `maxSum` as `max(maxSum, currSum)`.
5.  If `currSum < 0`, reset `currSum = 0`.

---

## Supplementary Notes from Patterns.md

# Kadane's Algorithm — Patterns Reference

> **Complete catalog of Kadane's variations**

---

## 📋 Pattern Variations

### 1. Maximum Subarray Sum (Standard Kadane's)

**Use When**: Find contiguous subarray with maximum sum  
**Time Complexity**: O(n)

#### Template
```cpp
int maxSubArray(vector<int>& nums) {
    int currentSum = nums[0];
    int maxSum = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}
```

#### Example Problems
- Maximum Subarray (LeetCode 53)

---

### 2. Maximum Product Subarray

**Use When**: Find contiguous subarray with maximum product  
**Time Complexity**: O(n)

#### Template
```cpp
int maxProduct(vector<int>& nums) {
    int maxProd = nums[0];
    int minProd = nums[0];
    int result = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        if(nums[i] < 0) swap(maxProd, minProd);
        
        maxProd = max(nums[i], maxProd * nums[i]);
        minProd = min(nums[i], minProd * nums[i]);
        
        result = max(result, maxProd);
    }
    
    return result;
}
```

#### Example Problems
- Maximum Product Subarray (LeetCode 152)

---

### 3. Maximum Sum Circular Subarray

**Use When**: Array wraps around  
**Time Complexity**: O(n)

#### Template
```cpp
int maxSubarraySumCircular(vector<int>& nums) {
    int maxKadane = kadane(nums);
    
    int totalSum = 0;
    for(int& x : nums) {
        totalSum += x;
        x = -x;
    }
    int maxCircular = totalSum + kadane(nums);
    
    return maxCircular == 0 ? maxKadane : max(maxKadane, maxCircular);
}
```

#### Example Problems
- Maximum Sum Circular Subarray (LeetCode 918)

---

## 💡 Pro Tips

1. **Track both max and min** - For product problems
2. **Handle all negatives** - Kadane's works correctly
3. **Circular trick** - total - min_subarray
4. **Return subarray indices** - Track start/end positions

---

**Master Kadane's for all subarray maximum problems!**

[← Back to Notes](02-subarrays-and-kadane-algorithm.md)


---

## Supplementary Notes from Mistakes.md

# Kadane's Algorithm — Common Mistakes

> **Top mistakes students make with Kadane's algorithm**

---

## 🔴 Critical Mistakes

### Mistake 1: Resetting currentSum to 0 Instead of nums[i]
**Wrong**:
```cpp
if(currentSum < 0) {
    currentSum = 0;  // WRONG!
}
```

**Correct**:
```cpp
currentSum = max(nums[i], currentSum + nums[i]);
```

**Why**: Must include current element!

---

### Mistake 2: Not Handling All Negative Numbers
**Wrong**:
```cpp
int maxSum = 0;  // WRONG for all negative!
int currentSum = 0;
```

**Correct**:
```cpp
int maxSum = nums[0];  // Initialize with first element
int currentSum = nums[0];
```

---

### Mistake 3: Forgetting to Track Minimum for Product
**Wrong**:
```cpp
int maxProd = nums[0];
// Missing: int minProd = nums[0];
```

**Why**: Negative * negative = positive!

---

## 💡 Best Practices

1. **Initialize with first element** - Not zero
2. **Track min for product** - Essential
3. **Circular case** - Check if all negative
4. **Update maxSum every iteration** - Don't forget

---

**Avoid these and Kadane's becomes easy!**

[← Back to Patterns](04-pattern-recognition-guide.md) | [← Back to Notes](01-array-master-notes.md)
