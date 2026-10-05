# Two Pointer Technique — Complete Guide

> **What You'll Learn**: Opposite direction, same direction, and Dutch National Flag patterns  
> **Prerequisites**: Array Basics, Indexing  
> **Time Required**: 3-4 hours

---

## 1. 📌 Definition

The **Two Pointer** technique uses **two indices** to traverse an array simultaneously, reducing time complexity from O(n²) to O(n) by eliminating nested loops.

**When to use**: When you need to compare pairs, search from both ends, or partition elements.

---

## 2. 🌍 Real-World Analogy

### Analogy 1: Bookends 📚

Imagine holding a book from both sides:
- Left hand = left pointer
- Right hand = right pointer
- You squeeze inward to find something in the middle

### Analogy 2: Conveyor Belt 🏭

Two workers inspecting items on a belt:
- Worker 1 starts from the beginning
- Worker 2 starts from the end
- They meet in the middle

---

## 3. 🎨 Visual Diagram

### Pattern 1: Opposite Direction

```
Array: [1, 3, 5, 7, 9, 11, 13]
        L                 R     ← Start: left=0, right=6
           L           R        ← Move inward
              L     R           ← Continue
                 L,R            ← Meet! Stop

Used for: Sorted arrays, finding pairs, palindrome checks
```

### Pattern 2: Same Direction (Fast/Slow)

```
Array: [1, 2, 3, 4, 5, 6, 7, 8]
        S  F                    ← Start: slow=0, fast=0
           S     F              ← Fast moves 2x speed
              S        F        ← Fast ahead of slow
                 S           F  ← Gap increases

Used for: Cycle detection, remove duplicates, find middle
```

---

## 4. 🔑 Pattern Recognition Keywords

**Look for these words in problems**:
- "Sorted array"
- "Find pair/triplet"
- "Reverse"
- "Partition"
- "Two elements that sum to X"
- "Remove duplicates"
- "Palindrome"
- "Container with most water"

---

## 5. 📋 Template Code

### Template 1: Opposite Direction

```cpp
#include <iostream>
#include <vector>
using namespace std;

void twoPointerOpposite(vector<int>& arr) {
    int left = 0;              // Start from beginning
    int right = arr.size() - 1; // Start from end
    
    while(left < right) {
        // Process arr[left] and arr[right]
        
        // Move pointers based on condition
        if(/* condition */) {
            left++;   // Move left pointer right
        } else {
            right--;  // Move right pointer left
        }
    }
}
```

### Template 2: Same Direction (Fast/Slow)

```cpp
#include <iostream>
#include <vector>
using namespace std;

void twoPointerSameDirection(vector<int>& arr) {
    int slow = 0;  // Slow pointer
    int fast = 0;  // Fast pointer
    
    while(fast < arr.size()) {
        // Fast pointer moves every iteration
        // Slow pointer moves conditionally
        
        if(/* condition */) {
            arr[slow] = arr[fast];
            slow++;
        }
        
        fast++;
    }
}
```

---

## 6. 🔍 Step-by-Step Example

### Problem: Two Sum II (Sorted Array)

**Problem**: Find two numbers that add up to target.

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& numbers, int target) {
    int left = 0;
    int right = numbers.size() - 1;
    
    while(left < right) {
        int sum = numbers[left] + numbers[right];
        
        if(sum == target) {
            return {left + 1, right + 1};  // 1-indexed
        } else if(sum < target) {
            left++;   // Need larger sum
        } else {
            right--;  // Need smaller sum
        }
    }
    
    return {};  // No solution
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = twoSum(nums, target);
    cout << "Indices: " << result[0] << ", " << result[1] << endl;
    // Output: 1, 2 (because 2 + 7 = 9)
    
    return 0;
}
```

**Dry Run**:
```
Array: [2, 7, 11, 15], Target: 9
        L          R

Step 1: sum = 2 + 15 = 17 > 9
        Need smaller sum → right--
        
Array: [2, 7, 11, 15]
        L     R

Step 2: sum = 2 + 11 = 13 > 9
        Need smaller sum → right--
        
Array: [2, 7, 11, 15]
        L  R

Step 3: sum = 2 + 7 = 9 == 9 ✓
        Found! Return {1, 2}
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Wrong Initialization
```cpp
// WRONG
int left = 1;              // Should be 0
int right = arr.size();    // Should be size - 1

// CORRECT
int left = 0;
int right = arr.size() - 1;
```

### Mistake 2: Wrong Loop Condition
```cpp
// WRONG
while(left <= right) {  // May process same element twice
    // ...
}

// CORRECT (for most cases)
while(left < right) {
    // ...
}
```

### Mistake 3: Forgetting to Move Pointers
```cpp
while(left < right) {
    if(arr[left] + arr[right] == target) {
        return {left, right};
    }
    // FORGOT to move pointers! Infinite loop!
    
    // CORRECT:
    if(arr[left] + arr[right] < target) {
        left++;
    } else {
        right--;
    }
}
```

---

## 8. ⏱️ Time & Space Complexity

| Operation | Time | Space | Reasoning |
|-----------|------|-------|-----------|
| Two Pointer (opposite) | **O(n)** | **O(1)** | Each element visited once |
| Two Pointer (same direction) | **O(n)** | **O(1)** | Single pass through array |
| Brute Force (nested loops) | O(n²) | O(1) | All pairs checked |

**Why O(n) and not O(n/2)?**
- Constants are dropped in Big-O
- n/2 = O(n) mathematically

---

## 9. 📝 Pattern Variations

### Variation 1: Dutch National Flag (3-Way Partition)

```cpp
#include <iostream>
#include <vector>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0;      // Boundary for 0s
    int mid = 0;      // Current element
    int high = nums.size() - 1;  // Boundary for 2s
    
    while(mid <= high) {
        if(nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        } else if(nums[mid] == 1) {
            mid++;
        } else {  // nums[mid] == 2
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}

int main() {
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sortColors(nums);
    
    for(int x : nums) {
        cout << x << " ";  // 0 0 1 1 2 2
    }
    
    return 0;
}
```

---

## 10. 💡 Pro Tips

1. **Sort first** — Many two-pointer problems require sorted input
2. **Draw it out** — Visualize pointer movement on paper
3. **Check boundaries** — Ensure pointers don't go out of bounds
4. **Handle duplicates** — Skip them if problem requires unique pairs
5. **Think about movement** — When to move left vs right pointer?

---

## 11. 🎯 When to Use Two Pointer

✅ **Use when**:
- Array is sorted (or can be sorted)
- Looking for pairs/triplets
- Need to compare elements from both ends
- Partitioning elements
- Removing duplicates in-place

❌ **Don't use when**:
- Array is unsorted and can't be sorted
- Need to find all combinations (use nested loops)
- Elements need to maintain original order

---

## 12. 📚 Practice Problems

### Easy (Start Here)
1. Valid Palindrome (LeetCode 125)
2. Reverse String (LeetCode 344)
3. Remove Duplicates from Sorted Array (LeetCode 26)
4. Two Sum II (LeetCode 167)
5. Squares of Sorted Array (LeetCode 977)

### Medium
1. Container With Most Water (LeetCode 11)
2. 3Sum (LeetCode 15)
3. 4Sum (LeetCode 18)
4. Trapping Rain Water (LeetCode 42)
5. Remove Nth Node From End (LeetCode 19)

### Hard
1. Trapping Rain Water (LeetCode 42)
2. Minimum Window Substring (LeetCode 76)
3. Sliding Window Maximum (LeetCode 239)
4. Median of Two Sorted Arrays (LeetCode 4)

---

## 13. 🎯 Key Takeaways

1. Two pointers reduce O(n²) to O(n)
2. **Opposite direction**: Start from both ends, move inward
3. **Same direction**: Fast and slow pointers
4. **Dutch flag**: Three pointers for 3-way partition
5. Works best on **sorted arrays**
6. Watch for **off-by-one errors** in loop conditions
7. Always **move pointers** to avoid infinite loops

---

**Next**: Solve problems in `Problems/` folder! →

[← Back to README](../README.md) | [Problems →](../../03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md)

---

## Supplementary Notes from 03-Two-Pointers.md

# 🤝 03 — Two Pointers

> **Explain Like I'm 5:** Imagine two fingers pointing to elements in an array. Sometimes they start at opposite ends and walk towards the middle. Other times, one finger walks slowly while the other scans quickly ahead. 
> This simple strategy helps us avoid checking every single combination, optimizing our runtime from $O(n^2)$ to $O(n)$!

---

## 💡 The Core Intuition: Why does it work?

To understand why Two Pointers is so powerful, let's look at **Two Sum II (Pair with Target Sum in a Sorted Array)**.

### The Slow Way (Brute Force): $O(n^2)$
Check every possible pair:
`(index 0, index 1)`, `(index 0, index 2)`, ..., `(index 1, index 2)`, etc. 
This takes a nested loop, running in $O(n^2)$ time.

### The Fast Way (Two Pointers): $O(n)$
Since the array is **sorted**, we can place `left` at the beginning (smallest value) and `right` at the end (largest value).
```
Array: [1, 3, 5, 8, 10], Target = 13
Pointers: left (index 0, val 1), right (index 4, val 10)
```

1. **Current Sum:** `1 + 10 = 11`. 
   - Since `11 < 13` (too small), we need a larger sum.
   - Because the array is sorted, pairing `left` (value 1) with *any* other element to its left is impossible (there are none), and pairing it with elements to its right will yield smaller sums than if we used a larger element. Thus, **we can completely discard the element at `left`**.
   - Action: `left++` (move pointer to a larger value).
2. **Current Sum:** `3 + 10 = 13`.
   - Found target!

By skipping redundant checks, we examine each element at most once, reducing our time to $O(n)$.

---

## 🎨 The Two Pointer Templates

There are two main configurations of two-pointer techniques:

### Template 1: Opposite Ends (Meeting in the Middle)
Used for reversing arrays, checking palindromes, or finding pairs in sorted arrays.

```
[  X,  X,  X,  X,  X,  X  ]
   ▲                   ▲
  left               right
   └───►           ◄───┘
```

```python
# Opposite Ends Python Template
left, right = 0, len(arr) - 1
while left < right:
    # 1. Evaluate elements at arr[left] and arr[right]
    # 2. Shift pointers based on conditions
    if condition:
        left += 1
    else:
        right -= 1
```

### Template 2: Fast & Slow (Same Direction)
Used for in-place modifications (deleting duplicates, moving elements) or finding cycles in linked lists.

```
[  X,  X,  X,  X,  X,  X  ]
   ▲   ▲
 slow fast ───► (scans ahead)
```

```python
# Fast & Slow Python Template
slow = 0
for fast in range(len(arr)):
    if should_process(arr[fast]):
        # Swap or copy arr[fast] to arr[slow]
        arr[slow], arr[fast] = arr[fast], arr[slow]
        slow += 1
```

---

## 🎯 Practice Problems & Worked Solutions

Practice these problems in order. They represent the core two-pointer patterns.

| # | Problem | Difficulty | Link | Template Type |
|---|---|---|---|---|
| 1 | Reverse String | Easy | [LeetCode](https://leetcode.com/problems/reverse-string/) | Opposite Ends |
| 2 | Two Sum II (Sorted Array) | Medium | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Opposite Ends |
| 3 | Squares of a Sorted Array | Easy | [LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/) | Opposite Ends (filling from back) |
| 4 | Move Zeroes | Easy | [LeetCode](https://leetcode.com/problems/move-zeroes/) | Fast & Slow |
| 5 | Remove Duplicates from Sorted Array | Easy | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Fast & Slow |

---

### Solution 1: Reverse String

**Intuition:** Swap the characters pointed to by `left` and `right`, then move `left` forward and `right` backward until they cross.

**Complexity:**
- **Time:** $O(n)$ — We inspect each character once.
- **Space:** $O(1)$ — Done in-place.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public void reverseString(char[] s) {
    int left = 0;
    int right = s.length - 1;
    while (left < right) {
        // Swap characters
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        // Move pointers inward
        left++;
        right--;
    }
}
```

#### Python
```python
def reverse_string(s): # s is a list of characters
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters in-place
        s[left], s[right] = s[right], s[left]
        # Move pointers inward
        left += 1
        right -= 1
```

#### C++
```cpp
void reverseString(vector<char>& s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        swap(s[left], s[right]); // Built-in utility swap
        left++;
        right--;
    }
}
```
</details>

---

### Solution 2: Two Sum II (Input Array Is Sorted)

**Intuition:** Since the indices must be 1-based, return `[left + 1, right + 1]`. Shrink search bounds according to the sum compared to the target.

**Complexity:**
- **Time:** $O(n)$ — Single pass scan.
- **Space:** $O(1)$ — No extra storage.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] twoSum(int[] numbers, int target) {
    int left = 0;
    int right = numbers.length - 1;
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return new int[]{left + 1, right + 1}; // 1-based index
        } else if (sum < target) {
            left++;  // We need a larger value
        } else {
            right--; // We need a smaller value
        }
    }
    return new int[]{-1, -1};
}
```

#### Python
```python
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

#### C++
```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
    int left = 0;
    int right = numbers.size() - 1;
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return {left + 1, right + 1};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {-1, -1};
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `numbers = [2, 7, 11, 15], target = 9`

- `left = 0` (value 2), `right = 3` (value 15)
- `sum = 2 + 15 = 17`. `17 > 9` -> `right--` (`right` becomes 2)
- `left = 0` (value 2), `right = 2` (value 11)
- `sum = 2 + 11 = 13`. `13 > 9` -> `right--` (`right` becomes 1)
- `left = 0` (value 2), `right = 1` (value 7)
- `sum = 2 + 7 = 9`. `9 == 9` -> returns `[1, 2]` ✅
</details>

---

### Solution 3: Squares of a Sorted Array

**Intuition:** 
Because the input can contain negative numbers (e.g. `[-4, -1, 0, 3, 10]`), the largest squares could reside at the beginning (e.g. $(-4)^2 = 16$) or at the end (e.g. $(10)^2 = 100$).
Place pointers at `left` and `right`. Compare their squared values. Write the larger square at the **back** of a new results array, then move that pointer inward.

**Complexity:**
- **Time:** $O(n)$ — Single pass to fill the new array.
- **Space:** $O(n)$ — To store the result.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] sortedSquares(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    int left = 0;
    int right = n - 1;
    int pos = n - 1; // Start filling from the back

    while (left <= right) {
        int leftSquare = nums[left] * nums[left];
        int rightSquare = nums[right] * nums[right];
        
        if (leftSquare > rightSquare) {
            result[pos] = leftSquare;
            left++;
        } else {
            result[pos] = rightSquare;
            right--;
        }
        pos--;
    }
    return result;
}
```

#### Python
```python
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1 # Start filling from the back
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    return result
```

#### C++
```cpp
vector<int> sortedSquares(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n);
    int left = 0;
    int right = n - 1;
    int pos = n - 1;
    
    while (left <= right) {
        int leftSquare = nums[left] * nums[left];
        int rightSquare = nums[right] * nums[right];
        
        if (leftSquare > rightSquare) {
            result[pos] = leftSquare;
            left++;
        } else {
            result[pos] = rightSquare;
            right--;
        }
        pos--;
    }
    return result;
}
```
</details>

---

### Solution 4: Move Zeroes

**Intuition:** 
Use the **Fast & Slow** template.
- The `slow` pointer marks the index where the next non-zero element should go.
- The `fast` pointer scans the array.
- When `fast` finds a non-zero element, swap the elements at `slow` and `fast`, then increment `slow`.

**Complexity:**
- **Time:** $O(n)$ — Single pass scan.
- **Space:** $O(1)$ — Modifies array in-place.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public void moveZeroes(int[] nums) {
    int slow = 0;
    for (int fast = 0; fast < nums.length; fast++) {
        if (nums[fast] != 0) {
            // Swap elements at slow and fast
            int temp = nums[slow];
            nums[slow] = nums[fast];
            nums[fast] = temp;
            
            slow++;
        }
    }
}
```

#### Python
```python
def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            # Swap elements in-place
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

#### C++
```cpp
void moveZeroes(vector<int>& nums) {
    int slow = 0;
    for (int fast = 0; fast < nums.size(); fast++) {
        if (nums[fast] != 0) {
            swap(nums[slow], nums[fast]);
            slow++;
        }
    }
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `nums = [0, 1, 0, 3, 12]`

- `slow = 0`, `fast = 0` (value 0). No swap.
- `slow = 0`, `fast = 1` (value 1). Swap `nums[0]` and `nums[1]`. Array: `[1, 0, 0, 3, 12]`, `slow` becomes 1.
- `slow = 1`, `fast = 2` (value 0). No swap.
- `slow = 1`, `fast = 3` (value 3). Swap `nums[1]` and `nums[3]`. Array: `[1, 3, 0, 0, 12]`, `slow` becomes 2.
- `slow = 2`, `fast = 4` (value 12). Swap `nums[2]` and `nums[4]`. Array: `[1, 3, 12, 0, 0]`, `slow` becomes 3.

**Result:** `[1, 3, 12, 0, 0]` ✅
</details>

---

### Solution 5: Remove Duplicates from Sorted Array

**Intuition:**
Since the array is sorted, duplicates are guaranteed to be adjacent.
- `slow` pointer points to the last known unique element.
- `fast` pointer scans the array starting from index 1.
- If `nums[fast] != nums[slow]`, it means we found a new unique element. We increment `slow`, and copy `nums[fast]` to `nums[slow]`.

**Complexity:**
- **Time:** $O(n)$ — Traverses the array once.
- **Space:** $O(1)$ — In-place.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast]; // Overwrite next position with unique element
        }
    }
    return slow + 1; // Length of the unique sub-array
}
```

#### Python
```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

#### C++
```cpp
int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0;
    int slow = 0;
    for (int fast = 1; fast < nums.size(); fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    return slow + 1;
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `nums = [0, 0, 1, 1, 1, 2, 2, 33]`

| `fast` | `nums[fast]` | `nums[slow]` | Condition `nums[fast] != nums[slow]` | Action | Array State |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | False | No action | `[0, 0, 1, 1, 1, 2, 2, 33]` |
| 2 | 1 | 0 | True | `slow`=1, `nums[1]`=1 | `[0, 1, 1, 1, 1, 2, 2, 33]` |
| 3 | 1 | 1 | False | No action | `[0, 1, 1, 1, 1, 2, 2, 33]` |
| 4 | 1 | 1 | False | No action | `[0, 1, 1, 1, 1, 2, 2, 33]` |
| 5 | 2 | 1 | True | `slow`=2, `nums[2]`=2 | `[0, 1, 2, 1, 1, 2, 2, 33]` |
| 6 | 2 | 2 | False | No action | `[0, 1, 2, 1, 1, 2, 2, 33]` |
| 7 | 33 | 2 | True | `slow`=3, `nums[3]`=33 | `[0, 1, 2, 33, 1, 2, 2, 33]` |

**Returned New Length:** `slow + 1 = 4` (Unique subarray: `[0, 1, 2, 33]`) ✅
</details>

---

## 🎓 Viva Questions & Answers

### Q1: What is the main prerequisites for using the two-pointer technique in Two-Sum problems?
**Answer:**
The input array must be **sorted**. If the array is unsorted, moving `left` rightward or `right` leftward does not give a deterministic guarantee of increasing or decreasing the sum, rendering the two-pointer strategy invalid unless sorted first.

### Q2: What are the two primary variations of Two-Pointers?
**Answer:**
1. **Opposite-Direction Pointers (Meeting-in-the-middle):** One pointer starts at index `0` (`left`) and another at `n-1` (`right`). Used in Pair Sum, Palindrome Check, Container With Most Water.
2. **Same-Direction Pointers (Fast & Slow / Reader & Writer):** Both pointers start at index `0` and move forward at different speeds or conditions. Used in Remove Duplicates, Move Zeroes, Cycle Detection.

### Q3: Why is Two-Pointer preferred over nested loops for Pair Sum problems?
**Answer:**
Nested loops check every possible pair, resulting in $O(n^2)$ time complexity. Two-Pointer takes advantage of array sorting to eliminate invalid pairs at each step, reducing time complexity to $O(n)$ with $O(1)$ extra space.

### Q4: Explain Floyd’s Cycle Detection Algorithm (Tortoise and Hare).
**Answer:**
It uses two pointers: a **Slow** pointer moving 1 step at a time and a **Fast** pointer moving 2 steps at a time. If a cycle exists, the fast pointer will eventually enter the cycle and catch up to the slow pointer from behind (they will meet). If no cycle exists, fast reaches `null`.

### Q5: How do you handle duplicate values in 3Sum (`a + b + c = 0`) using two pointers?
**Answer:**
After processing a valid triplet or incrementing/decrementing pointers, skip duplicate elements by advancing `left` while `nums[left] == nums[left + 1]` and decrementing `right` while `nums[right] == nums[right - 1]`.

---

## ⚠️ Beginner Pitfalls & Common Mistakes

1. **Forgetting to Sort:**
   - The opposite-ends summation trick *only* works if the array is sorted. If it is unsorted, you must sort it first ($O(n \log n)$ time) or use a HashMap ($O(n)$ space).

2. **Pointer Index Bounds:**
   - In meeting-in-the-middle, the condition is usually `while left < right`. If you use `while left <= right`, the pointers might cross and cause duplicates or infinite loops.

3. **Writing to the Wrong Index in Fast & Slow:**
   - In "Remove Duplicates", make sure to increment `slow` *before* copying: `slow++; nums[slow] = nums[fast];`. Otherwise, you overwrite the current unique element.

---

> 👉 Next, open `04-Binary-Search.md` to see how we search sorted lists at lightning speed! 💪



---

## Supplementary Notes from Patterns.md

# Two Pointer — Pattern Catalog

> **Complete reference for all two-pointer variations**

---

## 📋 Pattern Variations

### Variation 1: Opposite Direction (Converging Pointers)

**When to use**: 
- Array is sorted
- Looking for pairs that satisfy a condition
- Palindrome checks
- Partitioning problems

**Template**:
```cpp
int left = 0;
int right = arr.size() - 1;

while(left < right) {
    // Process arr[left] and arr[right]
    if(condition_met) {
        return result;
    }
    
    // Move pointers based on condition
    if(need_larger_value) {
        left++;
    } else {
        right--;
    }
}
```

**Example Problems**:
1. Two Sum II (LeetCode 167)
2. Container With Most Water (LeetCode 11)
3. Valid Palindrome (LeetCode 125)
4. 3Sum (LeetCode 15)
5. Reverse String (LeetCode 344)

**Complexity**: O(n) time, O(1) space

---

### Variation 2: Same Direction (Fast/Slow Pointers)

**When to use**:
- Remove duplicates in-place
- Cycle detection
- Find middle element
- Overwrite array based on condition

**Template**:
```cpp
int slow = 0;

for(int fast = 0; fast < arr.size(); fast++) {
    if(should_include(arr[fast])) {
        arr[slow] = arr[fast];
        slow++;
    }
}

return slow;  // New size
```

**Example Problems**:
1. Remove Duplicates from Sorted Array (LeetCode 26)
2. Move Zeroes (LeetCode 283)
3. Remove Element (LeetCode 27)
4. Middle of Linked List (find middle)
5. Happy Number (cycle detection)

**Complexity**: O(n) time, O(1) space

---

### Variation 3: Dutch National Flag (3-Way Partition)

**When to use**:
- Partition array into 3 groups
- Sort colors/0s, 1s, 2s
- QuickSort partition step

**Template**:
```cpp
int low = 0, mid = 0, high = n - 1;

while(mid <= high) {
    if(arr[mid] == 0) {
        swap(arr[low], arr[mid]);
        low++;
        mid++;
    } else if(arr[mid] == 1) {
        mid++;
    } else {  // arr[mid] == 2
        swap(arr[mid], arr[high]);
        high--;
    }
}
```

**Example Problems**:
1. Sort Colors (LeetCode 75)
2. Partition array by value
3. QuickSort implementation

**Complexity**: O(n) time, O(1) space

---

## 🔀 Cross-Pattern Combinations

### Two Pointer + Binary Search
- **Use case**: Find pair with sum closest to target
- **Strategy**: Fix one element, binary search for the other

### Two Pointer + Sorting
- **Use case**: 3Sum, 4Sum problems
- **Strategy**: Sort first, then use two pointers for remaining elements

### Two Pointer + Sliding Window
- **Use case**: Variable window problems
- **Strategy**: Left and right pointers form the window

---

## 🎯 Decision Flowchart

```
Problem asks to find pairs?
├─ YES → Is array sorted?
│  ├─ YES → Opposite Direction Two Pointer
│  └─ NO → Sort first, then Opposite Direction
│
├─ NO → Need to remove/filter elements?
│  ├─ YES → Same Direction (Fast/Slow)
│  └─ NO → Partition into groups?
│     ├─ YES (3 groups) → Dutch National Flag
│     └─ NO → Check if palindrome → Opposite Direction
│
└─ Check problem keywords:
   - "sorted" + "pair" → Opposite Direction
   - "remove" + "in-place" → Same Direction
   - "partition" + "0,1,2" → Dutch Flag
```

---

## 💡 Pattern Recognition Keywords

### Opposite Direction Keywords:
- "sorted array"
- "two numbers that sum to"
- "container with most water"
- "valid palindrome"
- "reverse"
- "from both ends"

### Same Direction Keywords:
- "remove duplicates"
- "in-place"
- "move zeroes"
- "overwrite"
- "filter elements"
- "compact array"

### Dutch Flag Keywords:
- "sort colors"
- "partition into 3"
- "0s, 1s, and 2s"
- "three-way partition"
- "Dutch national flag"

---

## 📊 Comparison Table

| Variation | Pointers | Movement | Best For | Complexity |
|-----------|----------|----------|----------|------------|
| **Opposite** | left, right | Converge | Sorted pairs, palindromes | O(n) |
| **Same Direction** | slow, fast | Both right | Filtering, duplicates | O(n) |
| **Dutch Flag** | low, mid, high | Complex | 3-way partition | O(n) |

---

## 🔑 Key Insights

1. **Opposite Direction**: Eliminates one element per iteration
2. **Same Direction**: slow ≤ fast always, slow tracks valid position
3. **Dutch Flag**: Maintain invariants for each region
4. **Always sort first** if problem doesn't guarantee sorted input (unless order matters)
5. **Watch boundaries**: left < right vs left <= right
6. **Skip duplicates**: When problem requires unique pairs

---

## ⚡ Quick Reference Cards

### Card 1: Two Sum Pattern
```cpp
// Find pair with target sum in sorted array
int left = 0, right = n - 1;
while(left < right) {
    int sum = arr[left] + arr[right];
    if(sum == target) return {left, right};
    else if(sum < target) left++;
    else right--;
}
```

### Card 2: Remove Duplicates
```cpp
// Remove duplicates in-place
int slow = 0;
for(int fast = 1; fast < n; fast++) {
    if(arr[fast] != arr[slow]) {
        slow++;
        arr[slow] = arr[fast];
    }
}
return slow + 1;
```

### Card 3: Sort Colors
```cpp
// 3-way partition
int l = 0, m = 0, h = n - 1;
while(m <= h) {
    if(nums[m] == 0) swap(nums[l++], nums[m++]);
    else if(nums[m] == 1) m++;
    else swap(nums[m], nums[h--]);
}
```

---

**Next**: Review common mistakes in `Mistakes.md` →

[← Back to Notes](../../03-Arrays-and-Strings/concepts/01-array-master-notes.md) | [Mistakes →](../../03-Arrays-and-Strings/concepts/05-common-mistakes-and-pitfalls.md)

---

## Supplementary Notes from Mistakes.md

# Two Pointer — Common Mistakes

> **Top 10 mistakes and how to avoid them**

---

## ❌ Mistake 1: Wrong Pointer Initialization

### The Error
```cpp
// WRONG
int left = 1;              // Should be 0
int right = arr.size();    // Should be size - 1

// This causes:
// - Misses first element
// - Out-of-bounds access on last element
```

### ✅ The Fix
```cpp
// CORRECT
int left = 0;
int right = arr.size() - 1;
```

### 🔍 How to Debug
- Print initial values: `cout << left << " " << right << endl;`
- Check if they point to valid indices

### 🚨 When This Occurs
- Rushing into coding without thinking
- Confused by 1-based problem description

---

## ❌ Mistake 2: Wrong Loop Condition

### The Error
```cpp
// WRONG: May process same element twice or miss cases
while(left <= right) {  // or while(left < right)
    // Depends on problem!
}
```

### ✅ The Fix
```cpp
// For finding pairs (don't use same element twice):
while(left < right) {

// For searching (need to check single element):
while(left <= right) {
```

### 🔍 How to Debug
- Trace with single-element array
- Check if loop terminates correctly

### 💡 Rule of Thumb
- **Two distinct elements**: `left < right`
- **Search/Range**: `left <= right`

---

## ❌ Mistake 3: Forgetting to Move Pointers

### The Error
```cpp
while(left < right) {
    if(arr[left] + arr[right] == target) {
        return {left, right};
    }
    // FORGOT to move pointers! → Infinite loop!
}
```

### ✅ The Fix
```cpp
while(left < right) {
    int sum = arr[left] + arr[right];
    if(sum == target) {
        return {left, right};
    } else if(sum < target) {
        left++;   // ← MUST move!
    } else {
        right--;  // ← MUST move!
    }
}
```

### 🔍 How to Debug
- Add counter to detect infinite loops
- Print pointer values each iteration

---

## ❌ Mistake 4: Moving Both Pointers Unnecessarily

### The Error
```cpp
// WRONG: Might skip valid pairs
if(arr[left] + arr[right] == target) {
    left++;
    right--;  // What if there are multiple solutions?
}
```

### ✅ The Fix
```cpp
// Move based on condition
if(sum < target) {
    left++;   // Only move left
} else if(sum > target) {
    right--;  // Only move right
} else {
    // Found! Move both or return
    return {left, right};
}
```

---

## ❌ Mistake 5: Not Handling Duplicates

### The Error
```cpp
// Problem: Find all unique pairs
// WRONG: Returns duplicate pairs
while(left < right) {
    if(arr[left] + arr[right] == target) {
        result.push_back({arr[left], arr[right]});
        left++;
        right--;
    }
}
```

### ✅ The Fix
```cpp
while(left < right) {
    if(arr[left] + arr[right] == target) {
        result.push_back({arr[left], arr[right]});
        left++;
        right--;
        
        // Skip duplicates
        while(left < right && arr[left] == arr[left-1]) {
            left++;
        }
        while(left < right && arr[right] == arr[right+1]) {
            right--;
        }
    }
}
```

---

## ❌ Mistake 6: Integer Overflow

### The Error
```cpp
// WRONG: Sum might overflow
if(arr[left] + arr[right] == target) {
    // arr[left] + arr[right] could exceed INT_MAX
}
```

### ✅ The Fix
```cpp
// Use long long for safety
long long sum = (long long)arr[left] + arr[right];
if(sum == target) {
    // Safe from overflow
}
```

---

## ❌ Mistake 7: Not Sorting When Required

### The Error
```cpp
// WRONG: Two pointer on unsorted array
vector<int> arr = {5, 2, 8, 1, 9};
int left = 0, right = 4;
// This won't work correctly!
```

### ✅ The Fix
```cpp
// MUST sort first (if order doesn't matter)
sort(arr.begin(), arr.end());
// Now two pointer works
```

### 💡 When NOT to Sort
- Problem requires maintaining original order
- Use hash map instead for unsorted arrays

---

## ❌ Mistake 8: Off-by-One in Fast/Slow Pattern

### The Error
```cpp
// WRONG: Slow and fast start at same position
int slow = 0, fast = 0;
while(fast < n) {
    arr[slow] = arr[fast];
    slow++;
    fast++;
}
// This just copies everything!
```

### ✅ The Fix
```cpp
// CORRECT: Add condition for slow
int slow = 0;
for(int fast = 0; fast < n; fast++) {
    if(should_include(arr[fast])) {  // ← Key condition!
        arr[slow] = arr[fast];
        slow++;
    }
}
```

---

## ❌ Mistake 9: Dutch Flag - Wrong Swap Logic

### The Error
```cpp
// WRONG: Not incrementing mid after swap with low
if(arr[mid] == 0) {
    swap(arr[low], arr[mid]);
    low++;
    // FORGOT: mid++
}
```

### ✅ The Fix
```cpp
if(arr[mid] == 0) {
    swap(arr[low], arr[mid]);
    low++;
    mid++;  // ← MUST increment!
} else if(arr[mid] == 1) {
    mid++;
} else {
    swap(arr[mid], arr[high]);
    high--;  // Don't increment mid here!
}
```

### 🔍 Why?
- After swap with low, arr[mid] is guaranteed to be 1 (already processed)
- After swap with high, arr[mid] is unknown (need to check)

---

## ❌ Mistake 10: Accessing Invalid Indices After Loop

### The Error
```cpp
while(left < right) {
    // ...
}
// WRONG: left and right might be invalid now
cout << arr[left] << arr[right];
```

### ✅ The Fix
```cpp
while(left < right) {
    if(found) {
        return result;  // Return inside loop
    }
}
return -1;  // Not found
```

---

## 🛠️ Debug Checklist

Before submitting two-pointer solution:

- [ ] Pointers initialized correctly (0 and n-1)?
- [ ] Loop condition appropriate (< or <=)?
- [ ] Pointers move in every iteration?
- [ ] No out-of-bounds access?
- [ ] Array sorted if required?
- [ ] Duplicates handled if needed?
- [ ] Overflow checked for sums?
- [ ] Edge cases tested (empty, single element)?

---

## 🎯 Interview Trap Questions

1. **"What if array has duplicates?"**
   - Answer: Add while loops to skip duplicates

2. **"Can you solve without sorting?"**
   - Answer: Use hash map instead (trade space for time)

3. **"What if array is circular?"**
   - Answer: Use modular arithmetic or double the array

4. **"How to find ALL pairs, not just one?"**
   - Answer: Don't return after finding first pair, continue

5. **"What if elements can be negative?"**
   - Answer: Same logic works, but sorting still required

---

## 💡 Pro Tips

1. **Always draw it out** - Visualize pointer movement
2. **Test with small cases first** - [1, 2], [1], []
3. **Print pointers** - Debug by printing left/right values
4. **Think about termination** - When does loop stop?
5. **Consider all movements** - When does each pointer move?

---

**Next**: Practice problems in `Problems/` folder →

[← Back to Patterns](../../03-Arrays-and-Strings/concepts/04-pattern-recognition-guide.md) | [Problems →](../../03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md)