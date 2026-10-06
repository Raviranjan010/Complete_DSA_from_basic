# Two Sum (Pair Sum Problem)

| Field | Value |
|---|---|
| **Title** | Two Sum |
| **Level** | L1 |
| **Difficulty** | Easy |
| **Topic** | 03-Arrays-and-Strings |
| **Pattern** | `#hash-map`, `#two-pointers` |
| **Tier** | Tier A |
| **Lists** | Blind75, NeetCode150 |
| **Companies** | NA (unverified legacy tag: Google, Amazon) |
| **Prerequisites** | `00-Start-Here` |
| **External Link** | https://leetcode.com/problems/two-sum/ |
| **Registry ID** | P-0001 |

---

## 1. Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

---

## 2. Constraints
- $2 \le \text{nums.length} \le 10^4$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
- Exactly one valid answer exists.

---

## 3. Examples
### Example 1
```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2 (Edge Case: Negative Numbers)
```text
Input: nums = [-3, 4, 3, 90], target = 0
Output: [0, 2]
Explanation: nums[0] + nums[2] == -3 + 3 == 0.
```

---

## 4. What Is The Problem Really Asking
We are tasked with finding a pair of distinct array positions $(i, j)$ such that $\text{nums}[i] + \text{nums}[j] = \text{target}$. The output must be the zero-based indices of these elements.

---

## 5. Key Observation / Intuition
For any current element $x = \text{nums}[i]$, the required complement is $c = \text{target} - x$. Instead of re-scanning the entire array to look for $c$, we can record elements we have already encountered in a hash table and query for $c$ in $\mathcal{O}(1)$ average time.

---

## 6. How To Recognize This Pattern
Whenever a problem asks for a pair of values satisfying an algebraic equality $A + B = K$, reframe it as a lookup query: $B = K - A$. A hash map enables instant lookup of historical elements.

---

## 7. Approach 1: Brute Force
Enumerate all pairs of indices $(i, j)$ where $0 \le i < j < n$. Check whether $\text{nums}[i] + \text{nums}[j] == \text{target}$.
- **Why slow:** Requires evaluating $n(n - 1) / 2$ pairs.
- **Time Complexity:** $\mathcal{O}(n^2)$
- **Space Complexity:** $\mathcal{O}(1)$

---

## 8. Approach 2: Optimal Hash Map
Maintain a hash map `seen` mapping each element value to its index. While iterating through the array:
1. Compute $\text{complement} = \text{target} - \text{nums}[i]$.
2. If `complement` exists in `seen`, return `[seen[complement], i]`.
3. Otherwise, insert `seen[nums[i]] = i`.
- **Time Complexity:** $\mathcal{O}(n)$
- **Space Complexity:** $\mathcal{O}(n)$

---

## 9. Pseudocode
```text
function twoSum(nums, target):
    seen = empty hash map
    for i from 0 to len(nums) - 1:
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
    return []
```

---

## 10. Visualization
```text
Array:  [ 2,  7, 11, 15 ], target = 9
Index:    0   1   2   3

i = 0: x = 2, complement = 7 -> not in map. Store map[2] = 0.
i = 1: x = 7, complement = 2 -> found in map at index 0!
Result: [0, 1]
```

---

## 11. Dry Run
| Step | Index `i` | Value `nums[i]` | Complement | In Hash Map? | Action |
|---|---|---|---|---|---|
| 1 | 0 | 2 | 7 | No | Insert `{2: 0}` |
| 2 | 1 | 7 | 2 | Yes (at 0) | Return `[0, 1]` |

---

## 12. Solutions (C++, Python, Java)

### C++17
```cpp
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        auto it = seen.find(complement);
        if (it != seen.end()) {
            return {it->second, i};
        }
        seen[nums[i]] = i;
    }
    return {};
}
```

### Python 3
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []
```

### Java 17
```java
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

---

## 13. Code Explanation
We perform a single forward pass over `nums`. At each index $i$, we compute the complement required to achieve `target`. The lookup in the hash map takes $\mathcal{O}(1)$ average time, and upon a match, we immediately return the pair of indices.

---

## 14. Complexity Analysis
- **Time Complexity:** $\mathcal{O}(n)$ because array traversal is linear and hash table lookups take $\mathcal{O}(1)$ amortized time.
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary memory to store up to $n$ elements in the hash map.

---

## 15. Edge Cases
1. **Target with duplicate elements (e.g. `[3, 3]`, target = 6):** Correctly resolved because the complement $3$ is searched before overwriting `seen[3]`.
2. **Negative values:** Addition and subtraction work seamlessly with negative integers without special casing.
3. **No pair exists:** The function safely returns an empty collection if no pair is found.

---

## 16. Common Mistakes
- **Reusing the same element twice:** Initializing the map with all elements before searching allows an element to pair with itself (e.g. `target = 8`, `nums[0] = 4`). Searching before inserting guarantees distinct index selection.
- **Overwriting indices without checking:** When duplicate values exist, searching first ensures the first instance is recognized before being overwritten.

---

## 17. Interview Follow-Ups
- **What if the array is already sorted?** Use two pointers with $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space without a hash map.
- **What if multiple pairs exist and all must be returned?** Collect pairs and skip duplicates to avoid redundant combinations.

---

## 18. Tricks
- Checking the hash map *before* inserting prevents accidental self-matching and elegantly handles duplicate complement values.

---

## 19. Related Problems & Variants
| Problem | Key Difference |
|---|---|
| Two Sum II (Sorted) | Array is sorted; solved with two pointers in $\mathcal{O}(1)$ space |
| 3Sum | Three elements sum to 0; sort + two-pointer traversal in $\mathcal{O}(n^2)$ |
| 4Sum | Generalized to four elements; sort + nested two-pointers in $\mathcal{O}(n^3)$ |

---

## 20. External Practice Links
- [LeetCode 1: Two Sum](https://leetcode.com/problems/two-sum/) (BOT-BLOCKED / Canonical Challenge)
- [GeeksforGeeks: Two Sum Check](https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/)
