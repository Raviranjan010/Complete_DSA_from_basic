# Sliding Window Technique — Complete Guide

> **What You'll Learn**: Fixed window, variable window, and monotonic window patterns  
> **Prerequisites**: Array Basics, Two Pointer  
> **Time Required**: 3-4 hours

---

## 1. 📌 Definition

The **Sliding Window** technique maintains a "window" of consecutive elements and slides it through the array, avoiding redundant calculations by reusing information from the previous window.

**When to use**: When you need to find optimal subarrays/substrings or process consecutive elements.

---

## 2. 🌍 Real-World Analogy

### Analogy 1: Camera Viewfinder 📷

Imagine taking a panoramic photo with a camera:
- Camera frame = window size
- You slide the camera left to right
- Each shot captures a new section
- You don't retake the entire panorama!

### Analogy 2: Moving Spotlight 🔦

A spotlight scanning a stage:
- Light beam = window
- Illuminates consecutive actors
- Moves smoothly across the stage
- Only sees what's in the beam

---

## 3. 🎨 Visual Diagram

### Pattern 1: Fixed Window

```
Array: [1, 4, 2, 10, 2, 3, 1, 0, 20], Window Size: 3

Window 1: [1, 4, 2]              → Sum = 7
             ↓ slide right
Window 2:    [4, 2, 10]          → Sum = 16 (reuse: 7 - 1 + 10)
                ↓ slide right
Window 3:       [2, 10, 2]       → Sum = 14 (reuse: 16 - 4 + 2)
                   ↓ slide right
Window 4:          [10, 2, 3]    → Sum = 15
```

### Pattern 2: Variable Window (Expand-Shrink)

```
Array: [2, 5, 1, 7, 3, 9], Find longest subarray with sum ≤ 10

Expand:  [2]           → Sum = 2 ✓  (window size = 1)
         [2, 5]        → Sum = 7 ✓  (window size = 2)
         [2, 5, 1]     → Sum = 8 ✓  (window size = 3)
         [2, 5, 1, 7]  → Sum = 15 ✗ (too large!)
         
Shrink:     [5, 1, 7]  → Sum = 13 ✗ (still too large)
              [1, 7]   → Sum = 8 ✓  (window size = 2)
              [1, 7, 3]→ Sum = 11 ✗ (too large)
                 [7, 3]→ Sum = 10 ✓ (window size = 2)
```

---

## 4. 🔑 Pattern Recognition Keywords

**Look for these words in problems**:
- "Subarray" or "substring"
- "Consecutive elements"
- "Longest/shortest/maximum/minimum"
- "Window of size K"
- "At most K"
- "Contiguous"
- "Sliding window" (obvious!)

---

## 5. 📋 Template Code

### Template 1: Fixed Window Size

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSumFixedWindow(vector<int>& arr, int k) {
    int n = arr.size();
    if(n < k) return -1;  // Invalid case
    
    // Calculate sum of first window
    int windowSum = 0;
    for(int i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    
    int maxSum = windowSum;
    
    // Slide window
    for(int i = k; i < n; i++) {
        windowSum = windowSum - arr[i - k] + arr[i];  // Remove old, add new
        maxSum = max(maxSum, windowSum);
    }
    
    return maxSum;
}
```

### Template 2: Variable Window (Expand-Shrink)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int longestSubarrayWithSum(vector<int>& arr, int target) {
    int n = arr.size();
    int left = 0;
    int currentSum = 0;
    int maxLength = 0;
    
    for(int right = 0; right < n; right++) {
        // Expand window
        currentSum += arr[right];
        
        // Shrink window if condition violated
        while(currentSum > target && left <= right) {
            currentSum -= arr[left];
            left++;
        }
        
        // Update answer
        maxLength = max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```

---

## 6. 🔍 Step-by-Step Example

### Problem: Maximum Sum Subarray of Size K

**Problem**: Find maximum sum of any contiguous subarray of size k.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSumSubarraySizeK(vector<int>& arr, int k) {
    int n = arr.size();
    if(n < k) {
        cout << "Invalid: array smaller than window" << endl;
        return -1;
    }
    
    // Step 1: Sum of first window
    int windowSum = 0;
    for(int i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    
    int maxSum = windowSum;
    
    // Step 2: Slide window through rest of array
    for(int i = k; i < n; i++) {
        // Remove element going out, add element coming in
        windowSum = windowSum - arr[i - k] + arr[i];
        
        // Update maximum
        maxSum = max(maxSum, windowSum);
    }
    
    return maxSum;
}

int main() {
    vector<int> arr = {1, 4, 2, 10, 2, 3, 1, 0, 20};
    int k = 3;
    
    int result = maxSumSubarraySizeK(arr, k);
    cout << "Maximum sum: " << result << endl;  // 24 (from [1, 0, 20])
    
    return 0;
}
```

**Dry Run**:
```
Array: [1, 4, 2, 10, 2, 3, 1, 0, 20], k = 3

Step 1: Initial window [1, 4, 2]
        windowSum = 1 + 4 + 2 = 7
        maxSum = 7

Step 2: Slide window right
        Remove arr[0]=1, Add arr[3]=10
        windowSum = 7 - 1 + 10 = 16
        maxSum = max(7, 16) = 16

Step 3: Slide again
        Remove arr[1]=4, Add arr[4]=2
        windowSum = 16 - 4 + 2 = 14
        maxSum = max(16, 14) = 16

Step 4: Continue sliding...
        Window [10, 2, 3]: sum = 15, maxSum = 16
        Window [2, 3, 1]: sum = 6, maxSum = 16
        Window [3, 1, 0]: sum = 4, maxSum = 16
        Window [1, 0, 20]: sum = 21, maxSum = 21

Result: 21 ✓
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Recalculating Window Sum from Scratch
```cpp
// WRONG: O(n*k) - Defeats the purpose!
for(int i = 0; i <= n - k; i++) {
    int currentSum = 0;
    for(int j = i; j < i + k; j++) {  // Recalculates every time!
        currentSum += arr[j];
    }
    maxSum = max(maxSum, currentSum);
}

// CORRECT: O(n) - Reuse previous calculation
windowSum = windowSum - arr[i - k] + arr[i];
```

### Mistake 2: Wrong Window Boundaries
```cpp
// WRONG: Off-by-one error
for(int i = k; i < n; i++) {
    windowSum -= arr[i - k - 1];  // Wrong index!
}

// CORRECT:
for(int i = k; i < n; i++) {
    windowSum -= arr[i - k];  // Element leaving the window
}
```

### Mistake 3: Forgetting to Handle Edge Cases
```cpp
// WRONG: No validation
int maxSum = 0;  // What if all numbers are negative?

// CORRECT: Handle edge cases
if(n < k) return -1;
int maxSum = INT_MIN;  // Handle negative numbers
```

### Mistake 4: Not Shrinking Window Properly
```cpp
// WRONG: If statement instead of while
if(currentSum > target) {
    currentSum -= arr[left];
    left++;  // Only shrinks once!
}

// CORRECT: While loop to shrink completely
while(currentSum > target && left <= right) {
    currentSum -= arr[left];
    left++;
}
```

---

## 8. ⏱️ Time & Space Complexity

| Pattern | Time | Space | Reasoning |
|---------|------|-------|-----------|
| **Fixed Window** | **O(n)** | **O(1)** | Each element added/removed once |
| **Variable Window** | **O(n)** | **O(1)** | Each element visited at most twice |
| **Brute Force** | O(n×k) or O(n²) | O(1) | Recalculates each window |

**Key Insight**: Sliding window is O(n) because each element is:
- Added to window exactly once
- Removed from window at most once
- Total operations: 2n = O(n)

---

## 9. 📝 Pattern Variations

### Variation 1: Monotonic Window (Advanced)

Used for "sliding window maximum" problems with a deque:

```cpp
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& arr, int k) {
    deque<int> dq;  // Stores indices
    vector<int> result;
    
    for(int i = 0; i < arr.size(); i++) {
        // Remove elements out of window
        if(!dq.empty() && dq.front() == i - k) {
            dq.pop_front();
        }
        
        // Remove smaller elements (they're useless)
        while(!dq.empty() && arr[dq.back()] < arr[i]) {
            dq.pop_back();
        }
        
        // Add current element
        dq.push_back(i);
        
        // Record maximum for valid windows
        if(i >= k - 1) {
            result.push_back(arr[dq.front()]);
        }
    }
    
    return result;
}

int main() {
    vector<int> arr = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    
    vector<int> result = maxSlidingWindow(arr, k);
    
    for(int x : result) {
        cout << x << " ";  // 3 3 5 5 6 7
    }
    
    return 0;
}
```

---

## 10. 💡 Pro Tips

1. **Identify window type first** — Fixed or variable?
2. **Use the sliding formula** — `new_sum = old_sum - outgoing + incoming`
3. **Track what you need** — Sum, count, max, min, frequency map
4. **Variable window** — Use while loop to shrink, not if
5. **Watch boundaries** — Ensure left never exceeds right
6. **Monotonic deque** — For sliding window maximum/minimum

---

## 11. 🎯 When to Use Sliding Window

✅ **Use when**:
- Problem mentions "subarray" or "substring"
- Looking for longest/shortest/consecutive elements
- Need optimal value in a window
- Can maintain state as window slides
- Fixed or variable window size

❌ **Don't use when**:
- Elements don't need to be consecutive
- Need to compare non-adjacent elements
- Array needs to be reordered
- Problem is about subsequences (not subarrays)

---

## 12. 📚 Practice Problems

### Easy (Start Here)
1. Maximum Average Subarray I (LeetCode 643)
2. Maximum Sum Subarray of Size K (GFG)
3. Contains Duplicate II (LeetCode 219)
4. Longest Subarray of 1's After Deleting One (LeetCode 1493)
5. Subarray Product Less Than K (LeetCode 713)

### Medium
1. Longest Substring Without Repeating (LeetCode 3)
2. Minimum Size Subarray Sum (LeetCode 209)
3. Find All Anagrams in String (LeetCode 438)
4. Longest Repeating Character Replacement (LeetCode 424)
5. Permutation in String (LeetCode 567)

### Hard
1. Minimum Window Substring (LeetCode 76)
2. Sliding Window Maximum (LeetCode 239)
3. Subarrays with K Different Integers (LeetCode 992)
4. Number of Substrings Containing All Three Characters (LeetCode 1358)

---

## 13. 🎯 Key Takeaways

1. Sliding window eliminates redundant calculations
2. **Fixed window** — Known size, slide by one position
3. **Variable window** — Expand and shrink based on condition
4. **Monotonic deque** — For efficient max/min in window
5. Each element processed at most twice → O(n) time
6. **Key formula**: `new = old - outgoing + incoming`
7. Use while loop for shrinking, not if statement

---

**Next**: Solve problems in `Problems/` folder! →

[← Back to README](../README.md) | [Problems →](../../03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md)


---

## Supplementary Notes from 09-Sliding-Window.md

# 🪟 09 — Sliding Window (The Slow & Clear Guide)

> 📣 **If you've been lost for two days — start here and read every line slowly. Do NOT skip the boxes.** By the end you'll wonder why it ever felt hard. We're going to build it one tiny step at a time. No step is skipped. Promise. 💛

---

## 🧠 Part 1 — The ONE Idea (read this 3 times)

Forget code for a minute. Here's the whole topic in a picture.

You have marks: `[1, 2, 3, 4, 5]`. Find the **sum of every group of 3 in a row**.

```
[1, 2, 3] 4  5   →  1+2+3 = 6
 1 [2, 3, 4] 5   →  2+3+4 = 9
 1  2 [3, 4, 5]  →  3+4+5 = 12
```

The **slow way**: add 3 numbers, every single time. That's wasteful.

Now look closely at how the window *moves* from the first group to the second:

```
[1, 2, 3]  →  [2, 3, 4]
```

> ❓ What actually changed?
> - The **1 left** (it slid out the left side) 👋
> - The **4 joined** (it slid in on the right side) 🤝
> - The `2` and `3` **never moved** — they're still in the window!

So instead of re-adding everything, just do:

> ## ⭐ new sum = old sum − outgoing + incoming
> `9 = 6 − 1 + 4`

That's it. **That single line is the entire topic.** A "window" is a group we slide across the array, updating it cheaply instead of recomputing. 🪟

> 🧊 **Frozen-in-your-brain version:**
> **Remove the one leaving. Add the one entering. Keep the rest.**

---

## 🪟 Part 2 — Two Types of Windows (know which one you're in)

There are only **two kinds** of sliding window. Every problem is one of these:

| Type | The window size is… | You're asked… | Example |
|------|--------------------|---------------|---------|
| **Fixed** | given to you (a number `k`) | best/count of size-k groups | "biggest sum of any 3 in a row" |
| **Variable** | *not* given — it grows & shrinks | longest/shortest that follows a rule | "longest run with no repeats" |

> 🎯 **Before writing ANY code, ask: is my window size fixed (given a `k`)? Or does it grow/shrink based on a rule?** Answering this tells you which template to use. That one question removes 90% of the confusion.

---

# 🟦 PART A — FIXED WINDOW

> The size `k` is handed to you. The window is always exactly `k` wide. It just slides right, one step at a time.

## The Recipe (memorize these 3 steps)

> 1. **Build** the first window (add the first `k` elements).
> 2. **Slide**: for each new element → `add the incoming, remove the outgoing`.
> 3. **Update** your answer (max? count?) after each slide.

```
Build first window        Then slide, one step at a time:
┌─────────┐               ┌─────────┐
│ k items │  ...          x │ k items │ ...
└─────────┘               └─────────┘
                          ↑ remove this   ↑ add this
```

---

## 🟢 A1 — Maximum Average Subarray `(LC 643)`

> **Story:** A teacher wants the best group of 4 students in a row (highest total marks). Find it.
> `marks = [1, 12, -5, -6, 50, 3]`, `k = 4`

**Watch the window slide (this dry run is the heart of everything — follow every line):**

```
Build first window: 1 + 12 + (-5) + (-6) = 2     → maxSum = 2

Slide → remove 1, add 50:   2 − 1 + 50 = 51       → maxSum = 51
Slide → remove 12, add 3:  51 − 12 + 3 = 42       → maxSum = 51 (42 is smaller)

Best sum = 51.  Average = 51 / 4 = 12.75  ✅
```

<details>
<summary>☕ Java</summary>

```java
public double findMaxAverage(int[] nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];   // STEP 1: build first window
    int maxSum = sum;

    for (int i = k; i < nums.length; i++) {
        sum += nums[i];          // STEP 2a: add the incoming (right)
        sum -= nums[i - k];      // STEP 2b: remove the outgoing (left)
        maxSum = Math.max(maxSum, sum);            // STEP 3: update answer
    }
    return (double) maxSum / k;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def findMaxAverage(self, nums, k):
    window = sum(nums[:k])          # STEP 1: build first window
    ans = window
    for i in range(k, len(nums)):
        window += nums[i]           # STEP 2a: add the incoming
        window -= nums[i - k]       # STEP 2b: remove the outgoing
        ans = max(ans, window)      # STEP 3: update answer
    return ans / k
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
double findMaxAverage(vector<int>& nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];    // STEP 1: build first window
    int mx = sum;
    for (int i = k; i < nums.size(); i++) {
        sum += nums[i];         // STEP 2a: add the incoming
        sum -= nums[i - k];     // STEP 2b: remove the outgoing
        mx = max(mx, sum);      // STEP 3: update answer
    }
    return (double) mx / k;
}
```
</details>

> 🔑 **The magic line is `sum += nums[i]; sum -= nums[i - k];`** — `nums[i]` is entering, `nums[i-k]` is the one exactly `k` steps back that's leaving. Stare at `i - k` until it clicks: if the window is size `k`, the element leaving is `k` positions behind the one entering.

> ⏱️ Time O(n) · Space O(1)

---

## 🟢 A2 — Maximum Number of Vowels `(LC 1456)`

> 😲 **Here's the important part:** this is the **EXACT same problem** as A1. The *only* thing that changed is **what we count** — vowels instead of a sum.
> `s = "abciiidef"`, `k = 3`

```
Window "abc" → vowels: a         → count 1, max 1
Slide "bci"  → remove a, add i   → count 1, max 1
Slide "cii"  → remove b, add i   → count 2, max 2
Slide "iii"  → remove c, add i   → count 3, max 3   ✅
```

<details>
<summary>☕ Java</summary>

```java
public int maxVowels(String s, int k) {
    int count = 0;
    for (int i = 0; i < k; i++)                    // STEP 1: build first window
        if (isVowel(s.charAt(i))) count++;
    int max = count;

    for (int i = k; i < s.length(); i++) {
        if (isVowel(s.charAt(i))) count++;         // incoming is a vowel? +1
        if (isVowel(s.charAt(i - k))) count--;     // outgoing was a vowel? −1
        max = Math.max(max, count);                // STEP 3: update answer
    }
    return max;
}
private boolean isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def maxVowels(self, s, k):
    vowels = set('aeiou')
    count = sum(1 for i in range(k) if s[i] in vowels)   # build first window
    ans = count
    for i in range(k, len(s)):
        if s[i] in vowels: count += 1          # incoming vowel? +1
        if s[i - k] in vowels: count -= 1      # outgoing vowel? −1
        ans = max(ans, count)
    return ans
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
bool isVowel(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}
int maxVowels(string s, int k) {
    int count = 0;
    for (int i = 0; i < k; i++)                    // build first window
        if (isVowel(s[i])) count++;
    int mx = count;
    for (int i = k; i < s.size(); i++) {
        if (isVowel(s[i])) count++;         // incoming vowel? +1
        if (isVowel(s[i - k])) count--;     // outgoing vowel? −1
        mx = max(mx, count);
    }
    return mx;
}
```
</details>

> 🧠 **See the pattern?** Same skeleton as A1. We swapped "add the number" for "add 1 if it's a vowel." *That's the whole difference.* If you understood A1, you already understand A2.

> ⏱️ Time O(n) · Space O(1)

---

## 🟢 A3 — Count Valid Subarrays `(LC 1343)`

> **What changed this time? Almost nothing.** Now we *count* how many windows of size `k` have an average `≥ threshold`.
> `arr = [2,2,2,2,5,5,5,8]`, `k = 3`, `threshold = 4`

> 🪄 **The one clever trick:** "average ≥ threshold" is annoying because of division. Multiply both sides:
> `sum / k ≥ threshold` → `sum ≥ k × threshold`. **No division needed** — just compare the window sum to `k × threshold`.

```
target = k × threshold = 3 × 4 = 12

Window 2+2+2 = 6  → 6 ≥ 12? no    count 0
Window 2+2+2 = 6  → no             count 0
Window 2+2+5 = 9  → no             count 0
Window 2+5+5 = 12 → 12 ≥ 12? yes   count 1
Window 5+5+5 = 15 → yes            count 2
Window 5+5+8 = 18 → yes            count 3   ✅
```

<details>
<summary>☕ Java</summary>

```java
public int numOfSubarrays(int[] arr, int k, int threshold) {
    int target = k * threshold;    // the no-division trick
    int sum = 0, count = 0;

    for (int i = 0; i < arr.length; i++) {
        sum += arr[i];             // add incoming
        if (i >= k) sum -= arr[i - k];             // remove outgoing (once window is full)
        if (i >= k - 1 && sum >= target) count++;  // window is size k AND valid → count it
    }
    return count;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def numOfSubarrays(self, arr, k, threshold):
    target = k * threshold
    window_sum = 0
    count = 0
    for i in range(len(arr)):
        window_sum += arr[i]                # add incoming
        if i >= k:
            window_sum -= arr[i - k]        # remove outgoing
        if i >= k - 1 and window_sum >= target:
            count += 1                      # size k AND valid
    return count
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    int target = k * threshold;
    int sum = 0, count = 0;
    for (int i = 0; i < arr.size(); i++) {
        sum += arr[i];                      // add incoming
        if (i >= k) sum -= arr[i - k];      // remove outgoing
        if (i >= k - 1 && sum >= target) count++;  // size k AND valid
    }
    return count;
}
```
</details>

> 🔑 The check `i >= k - 1` means "the window has finally reached full size `k`." Before that, we're still filling the first window and shouldn't count yet.

> ⏱️ Time O(n) · Space O(1)

---

## 🟦 Fixed Window — Board Summary

```
LC 643   Window Sum          →  find MAXIMUM
LC 1456  Window Vowel Count   →  find MAXIMUM
LC 1343  Window Sum           →  COUNT valid windows
```

> All three are the *same three steps*: **build → slide (remove left, add right) → update.** Only "what we track" and "what we do with it" changed. 🎯

---

# 🟨 PART B — VARIABLE WINDOW

> 🚨 **This is where most students get stuck. Read extra slowly.**
>
> Now nobody gives us a size `k`. The window **grows** when things are fine, and **shrinks** when a rule breaks. Two pointers, `left` and `right`, mark the window's edges.

## The New Recipe

> 1. `right` moves forward every step → the window **grows** (add `nums[right]`).
> 2. If a **rule breaks**, move `left` forward to **shrink** until the rule is happy again.
> 3. **Update** the answer (longest? shortest? biggest sum?).

```
   left→                    ←right
   ┌──────────────────────────┐
   │  the window can grow/shrink │
   └──────────────────────────┘
   right always moves right.
   left only moves when we must fix a broken rule.
```

> 💡 **The mental model:** `right` is greedy — it always wants more. `left` is the cleanup crew — it only steps in when `right` caused a problem.

---

## 🟠 B1 — Minimum Size Subarray Sum `(LC 209)`

> **Find the SHORTEST subarray whose sum is `≥ target`.** Window grows to reach the target, then shrinks to stay minimal.
> `target = 7`, `nums = [2,3,1,2,4,3]`

```
right adds until sum ≥ 7, then left shrinks while still ≥ 7:

[2]              sum 2
[2,3]            sum 5
[2,3,1]          sum 6
[2,3,1,2]        sum 8 ≥7 → length 4, try shrink → remove 2 → [3,1,2] sum 6 <7 stop
[3,1,2,4]        sum 10 ≥7 → length 4 → shrink [1,2,4] sum 7 ≥7 length 3 → shrink [2,4] sum 6 stop
[2,4,3]          sum 9 ≥7 → shrink [4,3] sum 7 length 2 ✅ → shrink [3] sum 3 stop

shortest = 2   ([4,3])
```

<details>
<summary>☕ Java</summary>

```java
public int minSubArrayLen(int target, int[] nums) {
    int left = 0, sum = 0, ans = Integer.MAX_VALUE;
    for (int right = 0; right < nums.length; right++) {
        sum += nums[right];                    // grow: add right
        while (sum >= target) {                // rule met → try to shrink
            ans = Math.min(ans, right - left + 1);
            sum -= nums[left];                 // shrink: remove left
            left++;
        }
    }
    return ans == Integer.MAX_VALUE ? 0 : ans;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def minSubArrayLen(self, target, nums):
    left = 0
    total = 0
    ans = float('inf')
    for right in range(len(nums)):
        total += nums[right]                   # grow: add right
        while total >= target:                 # rule met → shrink
            ans = min(ans, right - left + 1)
            total -= nums[left]                # shrink: remove left
            left += 1
    return 0 if ans == float('inf') else ans
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
int minSubArrayLen(int target, vector<int>& nums) {
    int left = 0, sum = 0, ans = INT_MAX;
    for (int right = 0; right < nums.size(); right++) {
        sum += nums[right];                    // grow: add right
        while (sum >= target) {                // rule met → shrink
            ans = min(ans, right - left + 1);
            sum -= nums[left++];               // shrink: remove left
        }
    }
    return ans == INT_MAX ? 0 : ans;
}
```
</details>

> 🔑 **Window length = `right - left + 1`.** Memorize this — it's how you measure a variable window every time.

> ⏱️ Time O(n) · Space O(1)

---

## 🟠 B2 — Max Consecutive Ones III `(LC 1004)`

> **Longest run of 1s if you may flip at most `k` zeros.** Same as: longest window with **at most `k` zeros**. Window grows; when zeros exceed `k`, shrink.
> `nums = [1,1,0,0,1,1,1]`, `k = 1`

<details>
<summary>☕ Java</summary>

```java
public int longestOnes(int[] nums, int k) {
    int left = 0, zeros = 0, ans = 0;
    for (int right = 0; right < nums.length; right++) {
        if (nums[right] == 0) zeros++;         // grow: track zeros
        while (zeros > k) {                    // rule broken (too many zeros)
            if (nums[left] == 0) zeros--;      // shrink from left
            left++;
        }
        ans = Math.max(ans, right - left + 1); // update longest
    }
    return ans;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def longestOnes(self, nums, k):
    left = 0
    zeros = 0
    ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1                         # grow: track zeros
        while zeros > k:                       # too many zeros → shrink
            if nums[left] == 0:
                zeros -= 1
            left += 1
        ans = max(ans, right - left + 1)       # update longest
    return ans
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
int longestOnes(vector<int>& nums, int k) {
    int left = 0, zeros = 0, ans = 0;
    for (int right = 0; right < nums.size(); right++) {
        if (nums[right] == 0) zeros++;         // grow: track zeros
        while (zeros > k) {                    // too many zeros → shrink
            if (nums[left] == 0) zeros--;
            left++;
        }
        ans = max(ans, right - left + 1);      // update longest
    }
    return ans;
}
```
</details>

> 🧠 Notice: B1 shrank to find the **shortest**; B2 shrinks only to *stay legal*, then measures the **longest**. Same machine, different question.

> ⏱️ Time O(n) · Space O(1)

---

## 🟠 B3 — Longest Substring Without Repeating Characters `(LC 3)`

> **Longest window with all-unique characters.** Use a **Set** to know if a character is already inside. If the new char is a repeat, shrink from the left until it's gone.
> `s = "abcabcbb"` → answer `3` ("abc")

<details>
<summary>☕ Java</summary>

```java
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0, ans = 0;
    for (int right = 0; right < s.length(); right++) {
        while (set.contains(s.charAt(right))) {    // repeat found → shrink
            set.remove(s.charAt(left));
            left++;
        }
        set.add(s.charAt(right));                  // grow: add unique char
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def lengthOfLongestSubstring(self, s):
    seen = set()
    left = 0
    ans = 0
    for right in range(len(s)):
        while s[right] in seen:                    # repeat found → shrink
            seen.remove(s[left])
            left += 1
        seen.add(s[right])                         # grow: add unique char
        ans = max(ans, right - left + 1)
    return ans
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
int lengthOfLongestSubstring(string s) {
    unordered_set<char> st;
    int left = 0, ans = 0;
    for (int right = 0; right < s.size(); right++) {
        while (st.count(s[right])) {               // repeat found → shrink
            st.erase(s[left]);
            left++;
        }
        st.insert(s[right]);                       // grow: add unique char
        ans = max(ans, right - left + 1);
    }
    return ans;
}
```
</details>

> ⏱️ Time O(n) · Space O(n)

---

## 🟠 B4 — Fruit Into Baskets `(LC 904)`

> **Longest window with at most 2 different numbers.** Use a **Map** to count how many of each fruit are in the window. When more than 2 types appear, shrink.
> `fruits = [1,2,1,2,3]`

<details>
<summary>☕ Java</summary>

```java
public int totalFruit(int[] fruits) {
    Map<Integer, Integer> map = new HashMap<>();
    int left = 0, ans = 0;
    for (int right = 0; right < fruits.length; right++) {
        map.put(fruits[right], map.getOrDefault(fruits[right], 0) + 1);  // grow
        while (map.size() > 2) {                   // more than 2 types → shrink
            map.put(fruits[left], map.get(fruits[left]) - 1);
            if (map.get(fruits[left]) == 0) map.remove(fruits[left]);
            left++;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def totalFruit(self, fruits):
    count = {}
    left = 0
    ans = 0
    for right in range(len(fruits)):
        count[fruits[right]] = count.get(fruits[right], 0) + 1   # grow
        while len(count) > 2:                      # more than 2 types → shrink
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
int totalFruit(vector<int>& fruits) {
    unordered_map<int,int> mp;
    int left = 0, ans = 0;
    for (int right = 0; right < fruits.size(); right++) {
        mp[fruits[right]]++;                        // grow
        while (mp.size() > 2) {                     // more than 2 types → shrink
            mp[fruits[left]]--;
            if (mp[fruits[left]] == 0) mp.erase(fruits[left]);
            left++;
        }
        ans = max(ans, right - left + 1);
    }
    return ans;
}
```
</details>

> 🔑 **Set vs Map:** use a **Set** when you only care "is it present?" (B3). Use a **Map** when you need "how many of each?" (B4), so you know when a type fully leaves the window.

> ⏱️ Time O(n) · Space O(n)

---

## 🟠 B5 — Maximum Erasure Value `(LC 1695)`

> **Biggest SUM of a window with all-unique numbers.** Same as B3 (unique window with a Set), but we also track a running `sum`.
> `nums = [4,2,4,5,6]` → answer `17` ([4,5,6] ... wait, [2,4,5,6] = 17)

<details>
<summary>☕ Java</summary>

```java
public int maximumUniqueSubarray(int[] nums) {
    Set<Integer> set = new HashSet<>();
    int left = 0, sum = 0, ans = 0;
    for (int right = 0; right < nums.length; right++) {
        while (set.contains(nums[right])) {        // repeat → shrink
            set.remove(nums[left]);
            sum -= nums[left];                     // remove its value too
            left++;
        }
        set.add(nums[right]);
        sum += nums[right];                        // add its value
        ans = Math.max(ans, sum);
    }
    return ans;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def maximumUniqueSubarray(self, nums):
    seen = set()
    left = 0
    curr_sum = 0
    ans = 0
    for right in range(len(nums)):
        while nums[right] in seen:                 # repeat → shrink
            seen.remove(nums[left])
            curr_sum -= nums[left]                 # remove its value too
            left += 1
        seen.add(nums[right])
        curr_sum += nums[right]                    # add its value
        ans = max(ans, curr_sum)
    return ans
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
int maximumUniqueSubarray(vector<int>& nums) {
    unordered_set<int> st;
    int left = 0, sum = 0, ans = 0;
    for (int right = 0; right < nums.size(); right++) {
        while (st.count(nums[right])) {            // repeat → shrink
            st.erase(nums[left]);
            sum -= nums[left];                     // remove its value too
            left++;
        }
        st.insert(nums[right]);
        sum += nums[right];                        // add its value
        ans = max(ans, sum);
    }
    return ans;
}
```
</details>

> 🧠 B5 = B3 + a running sum. Once you see B3, this is a 2-line upgrade.

> ⏱️ Time O(n) · Space O(n)

---

## 🟪 PART C — The Bridge Problem: Permutation in String `(LC 567)`

> This one blends **fixed window + frequency counting** (your anagram logic from hashing). Check if any rearrangement of `s1` appears inside `s2`.
> **Idea:** `s1` has a fixed length `k`. Slide a size-`k` window across `s2`. If the window's letter-counts ever exactly match `s1`'s letter-counts → found a permutation.

<details>
<summary>☕ Java</summary>

```java
public boolean checkInclusion(String s1, String s2) {
    if (s1.length() > s2.length()) return false;
    int[] need = new int[26], window = new int[26];
    for (char c : s1.toCharArray()) need[c - 'a']++;   // s1's letter counts
    int k = s1.length();

    for (int i = 0; i < s2.length(); i++) {
        window[s2.charAt(i) - 'a']++;                  // add incoming
        if (i >= k) window[s2.charAt(i - k) - 'a']--;  // remove outgoing
        if (Arrays.equals(need, window)) return true;  // counts match → permutation!
    }
    return false;
}
```
</details>

<details>
<summary>🐍 Python</summary>

```python
def checkInclusion(self, s1, s2):
    if len(s1) > len(s2): return False
    need = [0] * 26
    window = [0] * 26
    for ch in s1: need[ord(ch) - ord('a')] += 1        # s1's letter counts
    k = len(s1)
    for i in range(len(s2)):
        window[ord(s2[i]) - ord('a')] += 1             # add incoming
        if i >= k:
            window[ord(s2[i - k]) - ord('a')] -= 1     # remove outgoing
        if window == need:                             # counts match!
            return True
    return False
```
</details>

<details>
<summary>⚡ C++</summary>

```cpp
bool checkInclusion(string s1, string s2) {
    if (s1.size() > s2.size()) return false;
    vector<int> need(26, 0), window(26, 0);
    for (char c : s1) need[c - 'a']++;                 // s1's letter counts
    int k = s1.size();
    for (int i = 0; i < s2.size(); i++) {
        window[s2[i] - 'a']++;                         // add incoming
        if (i >= k) window[s2[i - k] - 'a']--;         // remove outgoing
        if (window == need) return true;               // counts match!
    }
    return false;
}
```
</details>

> ⏱️ Time O(n) · Space O(1) (26 counts)

---

## 🗺️ The Whole Topic on One Page

| Pattern | What's new | Problems |
|---------|-----------|----------|
| **Fixed window + sum** | the base recipe | 643, 1456, 1343 |
| **Fixed window + frequency** | count letters, compare | 567 |
| **Variable window + sum** | grow to reach, shrink to minimize | 209 |
| **Variable window + bad-count** | shrink when a "bad" count exceeds k | 1004 |
| **Set + window** | uniqueness check | 3 |
| **Map + window** | count of each type | 904 |
| **Set + sum + window** | uniqueness + running sum | 1695 |

> 🎓 **Each problem adds exactly ONE new idea to the one before it.** That's why we teach them in order. If a problem feels hard, go back one row — you probably skipped a step.

---

## ✅ Before You Say "I Don't Get It" — Checklist

- [ ] Can I say the golden line? *(new = old − outgoing + incoming)*
- [ ] Can I tell if a problem is **fixed** or **variable** window?
- [ ] For fixed: do I **build → slide → update**?
- [ ] For variable: does `right` grow, and `left` only shrink when a rule breaks?
- [ ] Do I know window length is `right - left + 1`?

> If any box is unticked, that's *exactly* the line to ask me about. A precise question ("why does `left` move here?") gets a fast answer. 🙌

---

# 🎯 Practice (in this order — each builds on the last)

| Problem | Difficulty | Link |
|---------|-----------|------|
| Maximum Average Subarray I | Easy | https://leetcode.com/problems/maximum-average-subarray-i/ |
| Maximum Number of Vowels in a Substring | Medium | https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/ |
| Number of Sub-arrays of Size K and Avg ≥ Threshold | Medium | https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/ |
| Permutation in String | Medium | https://leetcode.com/problems/permutation-in-string/ |
| Minimum Size Subarray Sum | Medium | https://leetcode.com/problems/minimum-size-subarray-sum/ |
| Max Consecutive Ones III | Medium | https://leetcode.com/problems/max-consecutive-ones-iii/ |
| Longest Substring Without Repeating Characters | Medium | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |
| Fruit Into Baskets | Medium | https://leetcode.com/problems/fruit-into-baskets/ |
| Maximum Erasure Value | Medium | https://leetcode.com/problems/maximum-erasure-value/ |

---

## 🎓 Viva Questions & Answers

### Q1: What is the Sliding Window technique, and when should you use it?
**Answer:**
Sliding Window is an optimization technique used to transform nested loop $O(n^2)$ subarray/substring searches into linear $O(n)$ time by maintaining a contiguous window defined by two pointers (`left` and `right`).
Use it when:
1. The problem involves **contiguous sub-arrays or sub-strings**.
2. Asking for min/max length, max sum, or sub-arrays satisfying a specific condition (e.g. at most $k$ zeros).

### Q2: What is the key difference between Fixed-Size and Variable-Size Sliding Windows?
**Answer:**
- **Fixed-Size Window:** Window length $K$ is constant. Expand `right`, add incoming element, and when $right - left + 1 > K$, remove outgoing element at `left` ($left++$).
- **Variable-Size Window:** Window size grows dynamically ($right++$) until a condition is violated, then shrinks dynamically ($left++$) until the condition becomes valid again.

### Q3: Why is the overall time complexity of Variable Sliding Window $O(n)$ even with a nested `while` loop?
**Answer:**
Because both the `right` pointer and the `left` pointer only move forward from $0$ to $n-1$. Each element is added to the window at most once by `right` and removed at most once by `left`. Therefore, total operations are at most $2n$, giving $O(n)$ time complexity.

### Q4: How do you calculate the number of valid sub-arrays inside a sliding window?
**Answer:**
If a window $[left, right]$ satisfies a monotonic condition, the number of valid sub-arrays ending at `right` is given by:
$$\text{Count} = right - left + 1$$
This accounts for all sub-arrays starting at any index from $left$ to $right$ and ending at $right$.

### Q5: How does sliding window compare to Two Pointers?
**Answer:**
Sliding Window is a specialized form of Two Pointers focused on **contiguous sub-segments** of an array or string. General Two Pointers (like 2Sum on sorted array) operate on non-contiguous elements from opposite ends of a sorted array.

---

> 🌟 **Do them top to bottom.** Solve 643 until it's boring, THEN move down. Each next problem is a small twist, not a new mountain. That's the secret to sliding window — it only looks like 9 problems; it's really *one idea, dressed 9 ways.* I'm right here for any doubt. 💪 — *Ajai Raj (Mentor)*



---

## Supplementary Notes from Patterns.md

# Sliding Window — Patterns Reference

> **Complete catalog of sliding window patterns and variations**

---

## 📋 Pattern Variations

### 1. Fixed Window

**Use When**: Window size is known  
**Time Complexity**: O(n)

#### Template
```cpp
int fixedWindow(vector<int>& arr, int k) {
    int n = arr.size();
    int currentSum = 0;
    
    // First window
    for(int i = 0; i < k; i++) {
        currentSum += arr[i];
    }
    
    int maxSum = currentSum;
    
    // Slide window
    for(int i = k; i < n; i++) {
        currentSum += arr[i] - arr[i-k];
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}
```

#### Example Problems
- Maximum Sum Subarray of Size K
- First Negative in Every Window of Size K
- Count Anagrams

---

### 2. Variable Window (Expand-Shrink)

**Use When**: Window size varies based on condition  
**Time Complexity**: O(n)

#### Template
```cpp
int variableWindow(vector<int>& arr, int target) {
    int left = 0;
    int currentSum = 0;
    int maxLength = 0;
    
    for(int right = 0; right < arr.size(); right++) {
        // Expand
        currentSum += arr[right];
        
        // Shrink if condition violated
        while(currentSum > target && left <= right) {
            currentSum -= arr[left];
            left++;
        }
        
        // Update answer
        maxLength = max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```

#### Example Problems
- Longest Subarray with Sum ≤ K
- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters

---

### 3. Monotonic Window (Deque-Based)

**Use When**: Need max/min in sliding window  
**Time Complexity**: O(n)

#### Template
```cpp
vector<int> monotonicWindow(vector<int>& arr, int k) {
    vector<int> result;
    deque<int> dq;  // Stores indices
    
    for(int i = 0; i < arr.size(); i++) {
        // Remove out of window
        if(!dq.empty() && dq.front() == i - k) {
            dq.pop_front();
        }
        
        // Maintain monotonic property
        while(!dq.empty() && arr[dq.back()] < arr[i]) {
            dq.pop_back();
        }
        
        dq.push_back(i);
        
        if(i >= k - 1) {
            result.push_back(arr[dq.front()]);
        }
    }
    
    return result;
}
```

#### Example Problems
- Sliding Window Maximum
- Sliding Window Minimum
- Next Greater Element

---

### 4. Hash Map + Sliding Window

**Use When**: Tracking character/element frequencies  
**Time Complexity**: O(n)

#### Template
```cpp
int hashMapWindow(string s, int k) {
    unordered_map<char, int> count;
    int left = 0;
    int maxLength = 0;
    
    for(int right = 0; right < s.size(); right++) {
        count[s[right]]++;
        
        // Shrink if condition violated
        while(count.size() > k) {
            count[s[left]]--;
            if(count[s[left]] == 0) {
                count.erase(s[left]);
            }
            left++;
        }
        
        maxLength = max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```

#### Example Problems
- Longest Substring with At Most K Distinct Characters
- Find All Anagrams in a String
- Permutation in String

---

## 🎯 Cross-Pattern Combinations

### Two Pointer + Sliding Window
```cpp
// Container With Most Water
int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int maxArea = 0;
    
    while(left < right) {
        int h = min(height[left], height[right]);
        int w = right - left;
        maxArea = max(maxArea, h * w);
        
        if(height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}
```

### Prefix Sum + Sliding Window
```cpp
// Check if subarray sum exists in range
bool hasValidSubarray(vector<int>& nums, int k) {
    unordered_set<int> prefixSet;
    int currentSum = 0;
    
    for(int num : nums) {
        currentSum += num;
        if(prefixSet.count(currentSum - k)) {
            return true;
        }
        prefixSet.insert(currentSum);
    }
    
    return false;
}
```

---

## 📊 Pattern Decision Flowchart

```
Problem mentions "subarray" or "substring"
         ↓
    Window size fixed?
    ↓           ↓
   YES          NO
    ↓           ↓
  Fixed     Condition given?
  Window    ↓           ↓
           YES          NO
            ↓           ↓
        Variable    Not sliding
        Window      window
            ↓
        Need max/min?
        ↓           ↓
       YES          NO
        ↓           ↓
    Monotonic    Hash Map
    Deque        Window
```

---

## 🎨 Quick Reference Cards

### Card 1: Fixed Window
```
WHEN: Window size known
TEMPLATE: 
  1. Build first window
  2. Slide by adding/removing
  3. Update answer
TIME: O(n)
SPACE: O(1)
```

### Card 2: Variable Window
```
WHEN: Condition-based window
TEMPLATE:
  1. Expand with right
  2. Shrink with left if needed
  3. Update answer
TIME: O(n)
SPACE: O(1)
```

### Card 3: Monotonic Deque
```
WHEN: Max/Min in window
TEMPLATE:
  1. Remove outdated elements
  2. Maintain monotonic order
  3. Front has answer
TIME: O(n)
SPACE: O(k)
```

### Card 4: Hash Map Window
```
WHEN: Track frequencies
TEMPLATE:
  1. Add element to map
  2. Shrink if condition violated
  3. Check map for answer
TIME: O(n)
SPACE: O(k)
```

---

## 💡 Pro Tips

1. **Always use `while` for shrinking** - Not `if`
2. **Track what matters** - Sum, count, or frequency
3. **Update answer at right time** - After expansion or before shrinking
4. **Handle empty window** - Check `left <= right`
5. **Optimize map operations** - Use array for small charset

---

## 🎓 Mastery Checklist

- [ ] Can implement fixed window from memory
- [ ] Can implement variable window from memory
- [ ] Understand when to use deque
- [ ] Can combine with hash map
- [ ] Can identify sliding window problems
- [ ] Can write templates without reference
- [ ] Can optimize from O(n²) to O(n)

---

**Master all 4 variations to solve any sliding window problem!**

[← Back to Notes](../../03-Arrays-and-Strings/concepts/02-subarrays-and-kadane-algorithm.md) | [Easy Problems](../../03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md)


---

## Supplementary Notes from Mistakes.md

# Sliding Window — Common Mistakes

> **Top mistakes students make with sliding window**

---

## 🔴 Critical Mistakes


### Mistake 1: Using `if` Instead of `while` for Shrinking
**Wrong**:
```cpp
if(currentSum > target) {
    currentSum -= arr[left];
    left++;
}
```


**Correct**:
```cpp
while(currentSum > target && left <= right) {
    currentSum -= arr[left];
    left++;
}
```

**Why**: One `if` might not shrink enough!

---

### Mistake 2: Forgetting to Check `left <= right`
**Wrong**:
```cpp
while(currentSum > target) {
    currentSum -= arr[left];
    left++;
}
```

**Correct**:
```cpp
while(currentSum > target && left <= right) {
    currentSum -= arr[left];
    left++;
}
```

**Why**: Can go out of bounds if left > right!

---

### Mistake 3: Not Updating Answer After Shrinking
**Wrong**:
```cpp
for(int right = 0; right < n; right++) {
    currentSum += arr[right];
    
    while(currentSum > target && left <= right) {
        currentSum -= arr[left];
        left++;
    }
    // Missing: maxLength = max(maxLength, right - left + 1);
}
```

**Correct**:
```cpp
for(int right = 0; right < n; right++) {
    currentSum += arr[right];
    
    while(currentSum > target && left <= right) {
        currentSum -= arr[left];
        left++;
    }
    
    // Update AFTER shrinking
    maxLength = max(maxLength, right - left + 1);
}
```

---

### Mistake 4: Incorrect Window Size Calculation
**Wrong**:
```cpp
maxLength = max(maxLength, right - left);  // Missing +1
```

**Correct**:
```cpp
maxLength = max(maxLength, right - left + 1);  // Inclusive
```

**Why**: Window is [left, right], both inclusive!

---

### Mistake 5: Not Handling First Window Separately
**Wrong** (Fixed Window):
```cpp
int currentSum = 0;
for(int i = 0; i < n; i++) {
    currentSum += arr[i];
    // Processes incomplete windows!
}
```

**Correct**:
```cpp
int currentSum = 0;
// Build first window
for(int i = 0; i < k; i++) {
    currentSum += arr[i];
}

// Then slide
for(int i = k; i < n; i++) {
    currentSum += arr[i] - arr[i-k];
}
```

---

### Mistake 6: Forgetting to Update Hash Map When Shrinking
**Wrong**:
```cpp
while(count.size() > k) {
    left++;  // Map not updated!
}
```

**Correct**:
```cpp
while(count.size() > k) {
    count[s[left]]--;
    if(count[s[left]] == 0) {
        count.erase(s[left]);
    }
    left++;
}
```

---

### Mistake 7: Using Wrong Comparison in Monotonic Deque
**Wrong**:
```cpp
while(!dq.empty() && arr[dq.back()] > arr[i]) {  // Wrong direction
    dq.pop_back();
}
```

**Correct** (for maximum):
```cpp
while(!dq.empty() && arr[dq.back()] < arr[i]) {  // Remove smaller
    dq.pop_back();
}
```

---

### Mistake 8: Not Checking for Empty Deque
**Wrong**:
```cpp
if(dq.front() == i - k) {  // Can crash if deque empty!
    dq.pop_front();
}
```

**Correct**:
```cpp
if(!dq.empty() && dq.front() == i - k) {
    dq.pop_front();
}
```

---

### Mistake 9: Forgetting Base Case in Hash Map
**Wrong**:
```cpp
unordered_map<int, int> count;
// Missing: count[0] = 1;
```

**Correct**:
```cpp
unordered_map<int, int> count;
count[0] = 1;  // Important for problems like "subarray sum equals k"
```

---

### Mistake 10: Confusing Fixed vs Variable Window
**Wrong** (Using variable when fixed needed):
```cpp
// Problem says "window of size k"
int left = 0;
for(int right = 0; right < n; right++) {
    // Shrinking logic - WRONG!
    while(right - left + 1 > k) {
        left++;
    }
}
```

**Correct**:
```cpp
// Just slide fixed window
for(int i = k; i < n; i++) {
    currentSum += arr[i] - arr[i-k];
}
```

---

## ✅ Debug Checklist

Run through this checklist when stuck:

- [ ] Am I using `while` for shrinking (not `if`)?
- [ ] Am I checking `left <= right`?
- [ ] Am I updating answer at the right time?
- [ ] Is window size calculation correct (right - left + 1)?
- [ ] For fixed window: Is first window built separately?
- [ ] For hash map: Am I updating counts when shrinking?
- [ ] For deque: Am I checking `!dq.empty()` before accessing?
- [ ] For deque: Is monotonic direction correct (< or >)?
- [ ] Am I using the right pattern (fixed vs variable)?
- [ ] Did I handle edge cases (empty array, k > n)?

---

## 🎯 Interview Trap Questions

### Trap 1: "Longest subarray with sum ≤ K"
**Trap**: Students use fixed window  
**Correct**: Variable window (expand-shrink)

### Trap 2: "Maximum in every window of size K"
**Trap**: Students use O(n*k) brute force  
**Correct**: Monotonic deque O(n)

### Trap 3: "Minimum window substring"
**Trap**: Students don't track all required characters  
**Correct**: Hash map with `formed` counter

### Trap 4: "Subarrays with exactly K distinct"
**Trap**: Students try to count exactly K directly  
**Correct**: Use trick: Exactly(K) = AtMost(K) - AtMost(K-1)

---

## 💡 Best Practices

1. **Always use `while` for shrinking** - Ensures condition is fully met
2. **Update answer strategically** - Know when to update (after expand or after shrink)
3. **Use appropriate data structure** - Deque for max/min, map for counts
4. **Initialize carefully** - First window or base cases
5. **Test with small examples** - Trace manually before coding

---

**Avoid these mistakes and sliding window becomes easy!**

[← Back to Patterns](../../03-Arrays-and-Strings/concepts/04-pattern-recognition-guide.md) | [← Back to Notes](../../03-Arrays-and-Strings/concepts/01-array-master-notes.md)
