# 📘 DSA Notes: Binary Search

## Complete Guide — Iterative + Recursive Binary Search

---

# 1. What Is Binary Search?

**Binary Search** is a searching algorithm used to efficiently find a target element in a **sorted array**.

Instead of checking every element one by one, binary search repeatedly divides the search space into two halves.

### Core Idea

```text
Sorted Array
     ↓
Find middle element
     ↓
Compare target with middle
     ↓
Eliminate one half
     ↓
Repeat
```

Because half of the search space is eliminated at every step, binary search has:

```text
Time Complexity = O(log n)
```

---

# 2. Most Important Requirement

Binary search requires the data to be sorted according to the search condition.

For an ascending array:

```text
1  3  5  7  9  11
```

we can determine:

```text
target < mid
```

or:

```text
target > mid
```

and safely eliminate one half.

### Example

```text
1  3  5  7  9  11
         ↑
        mid
```

If:

```text
target = 3
mid = 7
```

Since:

```text
3 < 7
```

the target can only be in:

```text
left half
```

We can eliminate:

```text
7  9  11
```

---

# 3. Why Must the Array Be Sorted?

Suppose:

```text
arr = [7, 2, 9, 1, 5]
```

The middle element is:

```text
9
```

If:

```text
target = 5
```

we know:

```text
5 < 9
```

but we cannot conclude that `5` is on the left.

It could be anywhere.

Therefore, binary search cannot safely eliminate half of an unsorted array.

### ⭐ Rule

> **Binary Search → Sorted Data**

---

# 4. Ascending Order

For ascending order:

```text
1  2  3  4  5  6  7
```

The smallest element is on the left.

The largest element is on the right.

If:

```text
target > arr[mid]
```

the target must be to the right.

Therefore:

```cpp
st = mid + 1;
```

If:

```text
target < arr[mid]
```

the target must be to the left.

Therefore:

```cpp
end = mid - 1;
```

---

# 5. The Three Important Variables

Binary search commonly uses:

```cpp
int st = 0;
int end = n - 1;
```

and:

```cpp
int mid;
```

Meaning:

```text
st  → beginning of current search space
end → end of current search space
mid → middle of current search space
```

---

# 6. Initial Search Space

Suppose:

```text
arr = [1,2,3,4,5,6,7]
```

Indices:

```text
 0 1 2 3 4 5 6
```

Initially:

```text
st = 0
end = 6
```

Search space:

```text
[1 2 3 4 5 6 7]
 ↑           ↑
st          end
```

---

# 7. Finding the Middle

The basic formula is:

```cpp
int mid = (st + end) / 2;
```

This works logically, but there is a possible integer overflow issue.

Prefer:

```cpp
int mid = st + (end - st) / 2;
```

---

# 8. Why Is `(st + end) / 2` Potentially Dangerous?

Suppose:

```text
st = INT_MAX - 10
end = INT_MAX
```

Then:

```cpp
st + end
```

may exceed the maximum value representable by `int`.

This can cause integer overflow.

Instead:

```cpp
st + (end - st) / 2
```

calculates the same midpoint without directly adding two potentially huge indices.

### ⭐ Best Practice

Always prefer:

```cpp
int mid = st + (end - st) / 2;
```

---

# 9. Binary Search Conditions

For ascending order:

### Case 1 — Target is greater

```cpp
if(target > arr[mid]) {
    st = mid + 1;
}
```

Meaning:

```text
Target is on the right.
```

---

### Case 2 — Target is smaller

```cpp
else if(target < arr[mid]) {
    end = mid - 1;
}
```

Meaning:

```text
Target is on the left.
```

---

### Case 3 — Target found

```cpp
else {
    return mid;
}
```

Because:

```cpp
target == arr[mid]
```

---

# 10. Iterative Binary Search

## Code

```cpp
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& arr, int target) {

    int st = 0;
    int end = arr.size() - 1;

    while(st <= end) {

        int mid = st + (end - st) / 2;

        if(target > arr[mid]) {

            st = mid + 1;

        }
        else if(target < arr[mid]) {

            end = mid - 1;

        }
        else {

            return mid;
        }
    }

    return -1;
}
```

---

# 11. Why `st <= end`?

This condition is extremely important:

```cpp
while(st <= end)
```

The search is valid while the search range contains at least one element.

### Example

```text
st = 3
end = 3
```

There is still one element:

```text
index 3
```

So we must check it.

Therefore:

```text
st == end
```

must be allowed.

If we used:

```cpp
while(st < end)
```

we could skip the final candidate.

### ⭐ Rule

For the standard inclusive binary-search implementation:

```cpp
while(st <= end)
```

---

# 12. Why `mid + 1` and `mid - 1`?

Suppose:

```text
arr[mid] < target
```

We already know:

```text
arr[mid] != target
```

Therefore, we do not need to search `mid` again.

So:

```cpp
st = mid + 1;
```

Similarly:

```text
arr[mid] > target
```

means:

```text
mid cannot be the answer
```

Therefore:

```cpp
end = mid - 1;
```

---

# 13. Dry Run — Target Found

Array:

```text
arr = [1,2,3,4,5,6,7]
```

Target:

```text
5
```

Indices:

```text
0 1 2 3 4 5 6
1 2 3 4 5 6 7
```

---

## Iteration 1

```text
st = 0
end = 6
```

```text
mid = 0 + (6 - 0)/2
    = 3
```

```text
arr[mid] = 4
```

Target:

```text
5
```

Since:

```text
5 > 4
```

move right:

```text
st = mid + 1
   = 4
```

---

## Iteration 2

```text
st = 4
end = 6
```

```text
mid = 4 + (6 - 4)/2
    = 5
```

```text
arr[5] = 6
```

Since:

```text
5 < 6
```

move left:

```text
end = mid - 1
    = 4
```

---

## Iteration 3

```text
st = 4
end = 4
```

```text
mid = 4
```

```text
arr[4] = 5
```

Target found.

Return:

```text
4
```

---

# 14. Dry Run Table

For:

```text
arr = [1,2,3,4,5,6,7]
target = 5
```

| Iteration | `st` | `end` | `mid` | `arr[mid]` | Decision |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 6 | 3 | 4 | Go right |
| 2 | 4 | 6 | 5 | 6 | Go left |
| 3 | 4 | 4 | 4 | 5 | Found |

Answer:

```text
4
```

---

# 15. Dry Run — Target Not Found

Array:

```text
[1,2,3,4,5,6,7]
```

Target:

```text
10
```

Iteration 1:

```text
mid = 3
arr[mid] = 4
```

Since:

```text
10 > 4
```

move:

```text
st = 4
```

Iteration 2:

```text
mid = 5
arr[mid] = 6
```

Since:

```text
10 > 6
```

move:

```text
st = 6
```

Iteration 3:

```text
mid = 6
arr[mid] = 7
```

Since:

```text
10 > 7
```

move:

```text
st = 7
```

Now:

```text
st = 7
end = 6
```

Therefore:

```text
st > end
```

Search is over.

Return:

```cpp
-1;
```

---

# 16. Why Return `-1`?

Array indices normally begin at:

```text
0
```

Therefore:

```text
-1
```

is not a valid index.

So it is commonly used to indicate:

```text
Target not found
```

---

# 17. Time Complexity

Binary search repeatedly cuts the search space approximately in half:

```text
n
n/2
n/4
n/8
n/16
...
```

After `k` steps:

```text
n / 2^k
```

When only one element remains:

```text
n / 2^k = 1
```

Therefore:

```text
n = 2^k
```

Taking logarithm base 2:

```text
log₂(n) = k
```

Therefore:

```text
Time Complexity = O(log n)
```

---

# 18. Why Is It `O(log n)`?

The important point is not that the loop performs a fixed number of operations.

The number of iterations depends on how many times we can divide `n` by `2`.

Example:

```text
n = 8

8 → 4 → 2 → 1
```

Approximately:

```text
3 divisions
```

and:

```text
log₂(8) = 3
```

For:

```text
n = 16
```

```text
16 → 8 → 4 → 2 → 1
```

```text
log₂(16) = 4
```

So the number of iterations grows very slowly.

---

# 19. Complexity Comparison

For large `n`:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(2ⁿ)
O(n!)
```

Binary search:

```text
O(log n)
```

This is much faster than linear search:

```text
O(n)
```

for large sorted arrays.

---

# 20. Binary Search vs Linear Search

| Feature | Linear Search | Binary Search |
|---|---|---|
| Data requirement | No sorting required | Sorted data required |
| Approach | Check one by one | Eliminate half |
| Worst-case time | O(n) | O(log n) |
| Best case | O(1) | O(1) |
| Random access helpful? | Not required | Yes |
| Main idea | Sequential scan | Divide search space |

---

# 21. Important Trade-Off

Binary search is not automatically better than linear search.

If the data is unsorted:

```text
[7,2,9,1,5]
```

you cannot directly use standard binary search.

You could sort first:

```text
O(n log n)
```

and then binary search:

```text
O(log n)
```

For a single search, sorting may cost more than simply doing:

```text
O(n)
```

linear search.

But if you need many searches on the same data, sorting once can make binary search very useful.

---

# 22. Recursive Binary Search

Binary search can also be implemented using recursion.

The idea is exactly the same:

```text
Check middle
    ↓
Target greater?
    ↓
Search right half

Target smaller?
    ↓
Search left half

Target equal?
    ↓
Return index
```

---

# 23. Recursive Code

```cpp
#include <iostream>
#include <vector>
using namespace std;

int recursiveBinarySearch(
    const vector<int>& arr,
    int target,
    int st,
    int end
) {

    if(st > end) {
        return -1;
    }

    int mid = st + (end - st) / 2;

    if(target > arr[mid]) {

        return recursiveBinarySearch(
            arr,
            target,
            mid + 1,
            end
        );
    }

    else if(target < arr[mid]) {

        return recursiveBinarySearch(
            arr,
            target,
            st,
            mid - 1
        );
    }

    else {

        return mid;
    }
}
```

---

# 24. Recursive Base Case

This is the most important part:

```cpp
if(st > end) {
    return -1;
}
```

Why?

Because:

```text
st > end
```

means the search range is empty.

Example:

```text
st = 5
end = 4
```

There is no valid index to search.

Therefore:

```text
Target does not exist.
```

---

# 25. Recursive Dry Run

Array:

```text
[1,2,3,4,5,6,7]
```

Target:

```text
5
```

Initial:

```text
st = 0
end = 6
```

Middle:

```text
mid = 3
arr[3] = 4
```

Since:

```text
5 > 4
```

call:

```cpp
recursiveBinarySearch(arr, 5, 4, 6);
```

Now:

```text
st = 4
end = 6
```

Middle:

```text
mid = 5
arr[5] = 6
```

Since:

```text
5 < 6
```

call:

```cpp
recursiveBinarySearch(arr, 5, 4, 4);
```

Now:

```text
mid = 4
arr[4] = 5
```

Found.

Return:

```text
4
```

---

# 26. Recursive Call Stack

Conceptually:

```text
binarySearch(0,6)
       ↓
binarySearch(4,6)
       ↓
binarySearch(4,4)
       ↓
return 4
```

Then the result returns back through the recursive calls.

---

# 27. Iterative vs Recursive Binary Search

| Feature | Iterative | Recursive |
|---|---|---|
| Loop | `while` | Function calls |
| Time | O(log n) | O(log n) |
| Extra stack space | O(1) | O(log n) |
| Code | Usually simpler | Often elegant |
| Risk | No recursion depth | Uses call stack |
| Practical choice | Usually preferred | Good for learning/recursive patterns |

Important:

The **time complexity is O(log n)** for both.

But recursive binary search uses additional call-stack space:

```text
O(log n)
```

while the iterative version uses:

```text
O(1)
```

auxiliary space.

---

# 28. Correction to the Provided Code

Your original function declaration was:

```cpp
int binarySearch(vector<int>)
```

This is incomplete because the function needs:

```text
array
target
```

A correct version is:

```cpp
int binarySearch(const vector<int>& arr, int target)
```

---

# 29. Why Use `const vector<int>&`?

Instead of:

```cpp
vector<int> arr
```

we can use:

```cpp
const vector<int>& arr
```

This avoids copying the entire vector.

### By value

```cpp
vector<int> arr
```

creates a copy.

For an array of `n` elements, copying costs:

```text
O(n)
```

### By const reference

```cpp
const vector<int>& arr
```

does not copy the vector.

So it is more efficient.

---

# 30. Important Issue in Your Example

You wrote:

```cpp
vector<int> arr1 = {1,2,-2,44,3,7};
```

This array is **not sorted**.

Therefore standard binary search cannot be correctly applied to it.

Sort it first:

```cpp
vector<int> arr1 = {-2,1,2,3,7,44};
```

or:

```cpp
sort(arr1.begin(), arr1.end());
```

Then binary search can be used.

---

# 31. Another Unsorted Example

You wrote:

```cpp
vector<int> arr2 = {-1,2,4,66,32,76};
```

This is also not sorted.

Correct ascending order:

```text
-1 2 4 32 66 76
```

If you want binary search:

```cpp
sort(arr2.begin(), arr2.end());
```

---

# 32. Correct Complete Program

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binarySearch(const vector<int>& arr, int target) {

    int st = 0;
    int end = arr.size() - 1;

    while(st <= end) {

        int mid = st + (end - st) / 2;

        if(target > arr[mid]) {

            st = mid + 1;
        }

        else if(target < arr[mid]) {

            end = mid - 1;
        }

        else {

            return mid;
        }
    }

    return -1;
}

int main() {

    vector<int> arr = {1, 2, 3, 4, 7, 44};

    int target = 7;

    cout << binarySearch(arr, target) << endl;

    return 0;
}
```

Output:

```text
4
```

---

# 33. Correct Recursive Program

```cpp
#include <iostream>
#include <vector>

using namespace std;

int recursiveBinarySearch(
    const vector<int>& arr,
    int target,
    int st,
    int end
) {

    if(st > end) {
        return -1;
    }

    int mid = st + (end - st) / 2;

    if(target > arr[mid]) {

        return recursiveBinarySearch(
            arr,
            target,
            mid + 1,
            end
        );
    }

    else if(target < arr[mid]) {

        return recursiveBinarySearch(
            arr,
            target,
            st,
            mid - 1
        );
    }

    else {

        return mid;
    }
}

int main() {

    vector<int> arr = {1, 2, 3, 4, 7, 44};

    int target = 7;

    int result = recursiveBinarySearch(
        arr,
        target,
        0,
        arr.size() - 1
    );

    cout << result << endl;

    return 0;
}
```

Output:

```text
4
```

---

# 34. Common Mistakes

## Mistake 1 — Using an Unsorted Array

Wrong:

```text
[1,5,2,8,3]
```

Binary search cannot safely operate on this.

Correct:

```text
[1,2,3,5,8]
```

---

## Mistake 2 — Wrong Mid Formula

Avoid:

```cpp
mid = (st + end) / 2;
```

Prefer:

```cpp
mid = st + (end - st) / 2;
```

---

## Mistake 3 — Wrong Direction

For ascending array:

```cpp
if(target > arr[mid])
    st = mid + 1;
```

and:

```cpp
if(target < arr[mid])
    end = mid - 1;
```

Do not reverse these conditions.

---

## Mistake 4 — Forgetting `+1`

Wrong:

```cpp
st = mid;
```

Correct:

```cpp
st = mid + 1;
```

because `mid` has already been checked.

---

## Mistake 5 — Forgetting `-1`

Wrong:

```cpp
end = mid;
```

Correct:

```cpp
end = mid - 1;
```

because `mid` has already been checked.

---

## Mistake 6 — Using `<` Instead of `<=`

Wrong for this standard implementation:

```cpp
while(st < end)
```

Correct:

```cpp
while(st <= end)
```

The case:

```text
st == end
```

still contains one candidate.

---

## Mistake 7 — Missing Recursive Base Case

Without:

```cpp
if(st > end)
    return -1;
```

the recursion may continue indefinitely.

---

# 35. Binary Search on Descending Arrays

Binary search can also work on descending arrays.

Example:

```text
9 8 7 6 5 4 3
```

But the movement rules change.

For ascending:

```text
target > arr[mid] → right
target < arr[mid] → left
```

For descending:

```text
target > arr[mid] → left
target < arr[mid] → right
```

The important thing is that the direction depends on the array's ordering.

---

# 36. Binary Search Is a Pattern, Not Just a Function

The deeper idea is:

> **Maintain a search space and repeatedly eliminate a portion of it using a monotonic condition.**

Standard binary search uses:

```text
sorted array
```

But the same thinking appears in many advanced problems.

Examples:

```text
First occurrence
Last occurrence
Lower bound
Upper bound
Search insert position
Peak element
Rotated sorted array
Binary search on answer
Minimum feasible value
Maximum feasible value
```

---

# 37. First Occurrence

Suppose:

```text
arr = [1,2,2,2,3,4]
```

Target:

```text
2
```

There are multiple answers:

```text
index 1
index 2
index 3
```

If the problem asks for the **first occurrence**, finding any `2` is not enough.

When:

```cpp
arr[mid] == target
```

store:

```cpp
ans = mid;
```

and continue searching left:

```cpp
end = mid - 1;
```

---

# 38. Last Occurrence

For:

```text
[1,2,2,2,3,4]
```

target:

```text
2
```

last occurrence is:

```text
index 3
```

When found:

```cpp
ans = mid;
```

continue right:

```cpp
st = mid + 1;
```

---

# 39. Search Insert Position

Example:

```text
arr = [1,3,5,6]
target = 5
```

Answer:

```text
2
```

If:

```text
target = 2
```

answer:

```text
1
```

because `2` should be inserted before `3`.

This is a classic binary-search problem.

---

# 40. Lower Bound Concept

For a sorted array, the lower bound of `target` is the first position where:

```text
arr[index] >= target
```

Example:

```text
arr = [1,2,4,4,5,7]
target = 4
```

Lower bound:

```text
index 2
```

---

# 41. Upper Bound Concept

The upper bound is the first position where:

```text
arr[index] > target
```

Example:

```text
arr = [1,2,4,4,5,7]
target = 4
```

Upper bound:

```text
index 4
```

---

# 42. Binary Search on Answer

This is a very important advanced DSA pattern.

Sometimes we are not searching for an element.

Instead, we search for the smallest or largest value satisfying a condition.

Example idea:

```text
Can I complete the task using X?
```

If:

```text
X works
```

then larger values may also work.

This creates a monotonic condition:

```text
false false false true true true
```

We can binary search for the first `true`.

This is called:

```text
Binary Search on Answer
```

---

# 43. Monotonicity

Binary search requires some form of ordered/monotonic structure.

For a sorted array:

```text
1 2 3 4 5 6
```

the comparison behavior changes predictably.

For answer-space binary search:

```text
false false false true true true
```

Once the condition becomes true, it stays true.

That allows us to eliminate half the search space.

---

# 44. Binary Search Pattern Recognition

When you see:

```text
Sorted array
```

think:

```text
Binary Search
```

When you see:

```text
Find first position
```

think:

```text
Binary Search
```

When you see:

```text
Find last position
```

think:

```text
Binary Search
```

When you see:

```text
Minimum value that satisfies condition
```

think:

```text
Binary Search on Answer
```

When you see:

```text
Maximum feasible value
```

think:

```text
Binary Search on Answer
```

---

# 45. Binary Search Template

## Standard Ascending Search

```cpp
int binarySearch(const vector<int>& arr, int target) {

    int st = 0;
    int end = arr.size() - 1;

    while(st <= end) {

        int mid = st + (end - st) / 2;

        if(arr[mid] == target) {

            return mid;
        }

        else if(arr[mid] < target) {

            st = mid + 1;
        }

        else {

            end = mid - 1;
        }
    }

    return -1;
}
```

This is the version worth memorizing.

---

# 46. Standard Binary Search Flow

```text
START
  ↓
st = 0
end = n-1
  ↓
st <= end?
  ↓
YES
  ↓
calculate mid
  ↓
arr[mid] == target?
 ┌───────────────┐
YES             NO
 ↓                ↓
return mid      compare
                 ↓
       ┌─────────┴─────────┐
       ↓                   ↓
target > mid          target < mid
       ↓                   ↓
st = mid + 1         end = mid - 1
       └─────────┬─────────┘
                 ↓
             repeat
                 ↓
           st > end
                 ↓
              return -1
```

---

# 47. Interview Explanation

A strong explanation:

> "Binary search works on sorted data. I maintain a search range using `st` and `end`. At each iteration, I calculate the middle index using `st + (end - st) / 2` to avoid potential integer overflow. If the target is greater than the middle element, I discard the left half by setting `st = mid + 1`. If the target is smaller, I discard the right half using `end = mid - 1`. If they are equal, I return the index. Since the search space is halved at every iteration, the time complexity is O(log n)."

---

# 48. Interview Questions

### Q1

Why does binary search require sorted data?

---

### Q2

Why is binary search O(log n)?

---

### Q3

Why use:

```cpp
st + (end - st)/2
```

instead of:

```cpp
(st + end)/2
```

?

---

### Q4

Why is the condition:

```cpp
st <= end
```

instead of:

```cpp
st < end
```

?

---

### Q5

Why do we use:

```cpp
mid + 1
```

and:

```cpp
mid - 1
```

?

---

### Q6

What happens if the target does not exist?

---

### Q7

What is the difference between iterative and recursive binary search?

---

### Q8

What is the extra space complexity of recursive binary search?

---

### Q9

Can binary search work on descending arrays?

---

### Q10

What is binary search on answer?

---

# 49. Practice Questions

## Beginner

1. Implement binary search iteratively.
2. Implement binary search recursively.
3. Find an element in a sorted array.
4. Return `-1` if the target is missing.
5. Count the number of iterations of binary search.

---

## Intermediate

6. Find first occurrence.
7. Find last occurrence.
8. Find total frequency of a target.
9. Search insert position.
10. Implement lower bound.
11. Implement upper bound.
12. Find floor of a number.
13. Find ceil of a number.

---

## Advanced

14. Search in rotated sorted array.
15. Find minimum in rotated sorted array.
16. Find peak element.
17. Find single element in a sorted array.
18. Search in a 2D matrix.
19. Find square root using binary search.
20. Binary Search on Answer problems.

---

# 50. Important LeetCode Problems

### Basic

**LeetCode 704 — Binary Search**

Classic binary search.

### Search Position

**LeetCode 35 — Search Insert Position**

### First / Last Position

**LeetCode 34 — Find First and Last Position of Element in Sorted Array**

### Rotated Array

**LeetCode 33 — Search in Rotated Sorted Array**

### Minimum Rotated Array

**LeetCode 153 — Find Minimum in Rotated Sorted Array**

### Peak

**LeetCode 162 — Find Peak Element**

### Matrix

**LeetCode 74 — Search a 2D Matrix**

These problems build the binary-search pattern progressively.

---

# 51. Complexity Summary

## Iterative

```text
Time:
O(log n)

Auxiliary Space:
O(1)
```

## Recursive

```text
Time:
O(log n)

Auxiliary Space:
O(log n)
```

because of the recursive call stack.

---

# 52. Binary Search vs Sorting

Do not confuse:

```text
Binary Search
```

with:

```text
Sorting
```

Binary search does **not** sort the array.

It assumes the search space already has the required ordering.

If you sort:

```cpp
sort(arr.begin(), arr.end());
```

the sorting operation itself costs:

```text
O(n log n)
```

Then binary search costs:

```text
O(log n)
```

---

# 53. Important Edge Cases

## Empty Array

```text
[]
```

There is nothing to search.

Return:

```text
-1
```

---

## One Element — Target Exists

```text
[5]
target = 5
```

Return:

```text
0
```

---

## One Element — Target Missing

```text
[5]
target = 10
```

Return:

```text
-1
```

---

## Target Smaller Than Everything

```text
[10,20,30,40]
target = 5
```

Eventually:

```text
end < st
```

Return:

```text
-1
```

---

## Target Greater Than Everything

```text
[10,20,30,40]
target = 50
```

Eventually:

```text
st > end
```

Return:

```text
-1
```

---

# 54. Duplicate Elements

Standard binary search can return **any matching index** when duplicates exist.

Example:

```text
[1,2,2,2,3]
```

Target:

```text
2
```

A standard binary search may return:

```text
1
```

or:

```text
2
```

or:

```text
3
```

depending on the midpoint progression.

If the problem asks for a specific occurrence, modify the algorithm.

---

# 55. ⭐ Most Important Binary Search Rules

```text
1. Data must be sorted for standard binary search.

2. Maintain:
   st = beginning
   end = ending

3. Calculate:
   mid = st + (end-st)/2

4. If target == arr[mid]:
   return mid

5. If target > arr[mid]:
   st = mid + 1

6. If target < arr[mid]:
   end = mid - 1

7. Continue while:
   st <= end

8. If the range becomes empty:
   return -1

9. Time:
   O(log n)

10. Iterative extra space:
    O(1)

11. Recursive extra space:
    O(log n)

12. For duplicate-specific problems:
    modify the search after finding a match.
```

---

# 56. 🧠 Final Mental Model

Think of binary search as a **detective eliminating impossible locations**.

Suppose:

```text
1 2 3 4 5 6 7 8 9
```

Target:

```text
8
```

Check middle:

```text
5
```

Since:

```text
8 > 5
```

everything on the left of `5` can be eliminated.

Remaining:

```text
6 7 8 9
```

Check middle again.

If:

```text
8 == 8
```

we found it.

The key is:

> **Never search where the target cannot possibly be.**

That is why binary search is fast.

---

# 57. ⭐ One-Line Memory Trick

> **"Sorted array → check middle → eliminate half → repeat → O(log n)."**

And remember the three decisions:

```text
target == arr[mid]
        ↓
      FOUND

target > arr[mid]
        ↓
   SEARCH RIGHT
   st = mid + 1

target < arr[mid]
        ↓
    SEARCH LEFT
   end = mid - 1
```

---

# 58. Final Code to Memorize

```cpp
#include <iostream>
#include <vector>

using namespace std;

int binarySearch(const vector<int>& arr, int target) {

    int st = 0;
    int end = arr.size() - 1;

    while(st <= end) {

        int mid = st + (end - st) / 2;

        if(arr[mid] == target) {

            return mid;
        }

        else if(arr[mid] < target) {

            st = mid + 1;
        }

        else {

            end = mid - 1;
        }
    }

    return -1;
}
```

### Complexity

```text
Time  = O(log n)
Space = O(1)
```

This is the **core binary search template** you should be able to write from memory.


---

## Supplementary Notes from 04-Binary-Search.md

# 🔍 04 — Binary Search

> **Explain Like I'm 5:** Finding a name in a physical phonebook. You don't start at page 1. You flip open the exact **middle**. If the name is alphabetically later, you throw away the entire left half of the book. You repeat this in the remaining pages. In just a few flips, you find the name out of millions!
>
> ⚠️ **The Golden Rule:** The input array **must be sorted**. If it is unsorted, binary search will fail.

---

## 📐 Why is it so fast? (The Mathematical Proof)

If you use Linear Search, looking for a target in an array of size $n$ takes up to $n$ steps.
In Binary Search, the search space is cut in half at every step. Let's see how many elements are left after $k$ steps:

- **Start:** $n$ elements
- **Step 1:** $\frac{n}{2}$ elements
- **Step 2:** $\frac{n}{4} = \frac{n}{2^2}$ elements
- **Step 3:** $\frac{n}{8} = \frac{n}{2^3}$ elements
- ...
- **Step $k$:** $\frac{n}{2^k}$ elements

The search terminates when the search space shrinks to $1$ element:

$$\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2(n)$$

Thus, the maximum number of steps is $\log_2(n)$.
- For $n = 1,000,000$ elements, linear search takes up to $1,000,000$ steps. Binary search takes at most $\mathbf{20}$ steps! ($\log_2(1,000,000) \approx 19.93$)

---

## 🎨 Visualizing Search Range Shrinkage

Here is a visual trace of searching for target `7` in the sorted array `[1, 3, 5, 7, 9, 11]`:

```
Step 1:
[ 1,  3,  5,  7,  9,  11 ]
  ▲           ▲        ▲
 low         mid      high
 arr[mid] = 5 < 7. Target is on the RIGHT. 
 Throw away left side. Set low = mid + 1 (index 3).

Step 2:
               [ 7,  9,  11 ]
                 ▲   ▲    ▲
                low mid  high
 arr[mid] = 9 > 7. Target is on the LEFT.
 Throw away right side. Set high = mid - 1 (index 3).

Step 3:
               [ 7 ]
                 ▲
             low, mid, high
 arr[mid] = 7 == 7. Found! Return index 3.
```

---

## 📋 The 3 Binary Search Templates

Not all Binary Search problems are about finding an exact number. There are 3 core patterns:

### Template 1: Pure Exact Match Search
Used when searching for a specific target in a sorted collection.

```python
# Template 1: Exact Match
low, high = 0, len(arr) - 1
while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid  # Found it!
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return -1  # Not found
```

### Template 2: Boundary/Condition Search (Floor, Ceil, Lower Bound)
Used when searching for the *first* or *last* element satisfying a condition (e.g. first element $\ge$ target). We track a candidate variable `ans`.

```python
# Template 2: Boundary (e.g., Floor: largest value <= target)
low, high = 0, len(arr) - 1
ans = -1
while low <= high:
    mid = low + (high - low) // 2
    if arr[mid] <= target:
        ans = mid      # Record candidate index
        low = mid + 1  # Look for a larger valid value to the right
    else:
        high = mid - 1 # Too large, look left
return ans
```

### Template 3: Search on Answer Space
Used when solving word problems where the answer is a number in a known range (e.g., eating speed between $1$ and $10^9$).
```python
# Template 3: Search on Answer
low, high = MIN_POSSIBLE_ANSWER, MAX_POSSIBLE_ANSWER
ans = -1
while low <= high:
    mid = low + (high - low) // 2
    if is_valid_answer(mid):
        ans = mid      # Record valid answer
        high = mid - 1 # Try to find a smaller (better) valid answer
    else:
        low = mid + 1  # Search for larger speeds
return ans
```

---

## 🎯 Practice Problems & Worked Solutions

Practice these standard questions to master Binary Search.

| # | Problem | Difficulty | Link | Key Idea |
|---|---|---|---|---|
| 1 | Binary Search | Easy | [LeetCode](https://leetcode.com/problems/binary-search/) | Exact match search. |
| 2 | Search Insert Position | Easy | [LeetCode](https://leetcode.com/problems/search-insert-position/) | Finding insertion index. |
| 3 | First & Last Position | Medium | [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Two separate boundary searches. |
| 4 | Floor in a Sorted Array | Easy | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1) | Find largest element $\le$ target. |
| 5 | Search in Rotated Sorted Array | Medium | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Identify which half is sorted. |

---

### Solution 1: Binary Search (Exact Match)

**Complexity:**
- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int search(int[] nums, int target) {
    int low = 0;
    int high = nums.length - 1;
    while (low <= high) {
        // Safe middle calculation to prevent integer overflow
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            return mid; // Target found
        } else if (nums[mid] < target) {
            low = mid + 1; // Search right half
        } else {
            high = mid - 1; // Search left half
        }
    }
    return -1; // Not found
}
```

#### Python
```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        # '//' is integer division in Python
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

#### C++
```cpp
int search(vector<int>& nums, int target) {
    int low = 0;
    int high = nums.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```
</details>

---

### Solution 2: Search Insert Position

**Intuition:** 
Run standard binary search. If the target is not found, the `low` pointer will end up pointing to the index where the target *should* be inserted to maintain sorted order.

**Complexity:**
- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int searchInsert(int[] nums, int target) {
    int low = 0;
    int high = nums.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low; // low represents the insertion position
}
```

#### Python
```python
def search_insert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
```

#### C++
```cpp
int searchInsert(vector<int>& nums, int target) {
    int low = 0, high = nums.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```
</details>

---

### Solution 3: First & Last Position of Element in Sorted Array

**Intuition:**
Run binary search twice.
1. First run finds the left boundary (first occurrence). When `nums[mid] == target`, save `mid` as a candidate but continue searching *left* by setting `high = mid - 1`.
2. Second run finds the right boundary (last occurrence). When `nums[mid] == target`, save `mid` but continue searching *right* by setting `low = mid + 1`.

**Complexity:**
- **Time:** $O(\log n)$ — Two independent binary searches.
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int[] searchRange(int[] nums, int target) {
    int first = findBound(nums, target, true);
    int last = findBound(nums, target, false);
    return new int[]{first, last};
}

private int findBound(int[] nums, int target, boolean isFirst) {
    int low = 0, high = nums.length - 1;
    int ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            ans = mid; // Record candidate
            if (isFirst) {
                high = mid - 1; // Keep searching left
            } else {
                low = mid + 1;  // Keep searching right
            }
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
```

#### Python
```python
def search_range(nums, target):
    def find_bound(is_first):
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                if is_first:
                    high = mid - 1  # Keep looking left
                else:
                    low = mid + 1   # Keep looking right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
    return [find_bound(True), find_bound(False)]
```

#### C++
```cpp
int findBound(vector<int>& nums, int target, bool isFirst) {
    int low = 0, high = nums.size() - 1;
    int ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            ans = mid;
            if (isFirst) {
                high = mid - 1; // Look left
            } else {
                low = mid + 1;  // Look right
            }
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

vector<int> searchRange(vector<int>& nums, int target) {
    return {findBound(nums, target, true), findBound(nums, target, false)};
}
```
</details>

---

### Solution 4: Floor in a Sorted Array

**Intuition:**
Use Template 2.
We seek the largest index `i` such that `arr[i] <= x`.
- If `arr[mid] <= x`, then `mid` is a valid candidate for the floor. We store `ans = mid` and search the right half (`low = mid + 1`) to check if there is an even larger element that is still $\le x$.
- If `arr[mid] > x`, the element is too large. We search the left half (`high = mid - 1`).

**Complexity:**
- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int findFloor(long[] arr, int n, long x) {
    int low = 0;
    int high = n - 1;
    int ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= x) {
            ans = mid;      // Valid floor candidate
            low = mid + 1;  // Try to find a larger value
        } else {
            high = mid - 1; // Element is too large, search left
        }
    }
    return ans;
}
```

#### Python
```python
def find_floor(arr, x):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= x:
            ans = mid
            low = mid + 1  # Seek larger valid candidates
        else:
            high = mid - 1 # Seek smaller values
    return ans
```

#### C++
```cpp
int findFloor(vector<long long>& arr, long long x) {
    int low = 0;
    int high = arr.size() - 1;
    int ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= x) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
```
</details>

---

### Solution 5: Search in Rotated Sorted Array

**Intuition:**
A sorted array that has been rotated contains two sorted sub-sections (e.g. `[4, 5, 6, 7, 0, 1, 2]`).
If we choose a pivot index `mid`, **at least one of the halves (left or right) is guaranteed to be normally sorted**.
1. Find if the left half is sorted: `nums[low] <= nums[mid]`.
   - If yes: check if `target` lies inside the left half range (`nums[low] <= target < nums[mid]`). If it does, search left (`high = mid - 1`); otherwise search right (`low = mid + 1`).
2. If the left half is not sorted, the right half must be sorted.
   - Check if `target` lies inside the right half range (`nums[mid] < target <= nums[high]`). If it does, search right (`low = mid + 1`); otherwise search left (`high = mid - 1`).

**Complexity:**
- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int search(int[] nums, int target) {
    int low = 0;
    int high = nums.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        
        // 1. Check if Left Half is Sorted
        if (nums[low] <= nums[mid]) {
            // Check if target lies within the sorted left half
            if (nums[low] <= target && target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } 
        // 2. Otherwise, Right Half must be Sorted
        else {
            // Check if target lies within the sorted right half
            if (nums[mid] < target && target <= nums[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    return -1;
}
```

#### Python
```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
            
        # Left half sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
```

#### C++
```cpp
int search(vector<int>& nums, int target) {
    int low = 0;
    int high = nums.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) return mid;
        
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else {
            if (nums[mid] < target && target <= nums[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    return -1;
}
```
</details>

<details>
<summary>📋 Step-by-Step Dry Run</summary>

Input: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

| Iteration | `low` | `high` | `mid` | `nums[mid]` | Sorted Half | Range Check for Target `0` | Next Pointers |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 6 | 3 | 7 | Left (`nums[0] <= 7`) | `4 <= 0 < 7` (False) | `low = mid + 1 = 4` |
| 2 | 4 | 6 | 5 | 1 | Right (`nums[5] <= 2`) | `1 < 0 <= 2` (False) | `high = mid - 1 = 4` |
| 3 | 4 | 4 | 4 | 0 | Match! (`nums[4] == 0`) | Return index `4` | - |

**Returned Index:** `4` ✅
</details>

---

## 🎓 Viva Questions & Answers

### Q1: Why must the input array be sorted for Binary Search?
**Answer:**
Binary Search relies on the **Monotonic Property** (orderly increasing or decreasing sequence). This guarantees that comparing the middle element with the target deterministically eliminates half of the remaining search space. If unsorted, comparing `nums[mid]` gives no guarantee about where the target lies.

### Q2: Why do we use `mid = low + (high - low) / 2` instead of `mid = (low + high) / 2`?
**Answer:**
In languages with bounded integer types (like C, C++, Java), if `low` and `high` are large positive integers (e.g. near $2 \times 10^9$), `low + high` overflows the 32-bit signed integer capacity into a negative number, producing an incorrect negative index or crash. `low + (high - low) / 2` mathematically avoids sum overflow.

### Q3: What is the Lower Bound and Upper Bound in Binary Search?
**Answer:**
- **Lower Bound:** The index of the **first element** in a sorted array that is $\ge$ `target`.
- **Upper Bound:** The index of the **first element** in a sorted array that is strictly $>$ `target`.

### Q4: How does Binary Search work on Rotated Sorted Arrays?
**Answer:**
At any `mid` index in a rotated sorted array, at least one of the two halves (`[low...mid]` or `[mid...high]`) is guaranteed to be completely sorted. We identify which half is sorted, check if the target falls within that sorted half's range, and adjust `low` or `high` accordingly.

### Q5: What is "Search on Answer Space" (Binary Search on Answer)?
**Answer:**
When the problem output is a monotonic numerical value bounded in a range $[L, R]$ (e.g. minimum eating speed, minimum capacity), we apply Binary Search over the potential answer range rather than an array. For each candidate answer `mid`, we test validity with a helper function `isPossible(mid)`.

---

## ⚠️ Beginner Pitfalls & Common Mistakes

1. **Integer Overflow:**
   - Writing `(low + high) / 2` can cause an overflow error if `low + high` exceeds the maximum value of a 32-bit signed integer ($2 \times 10^9$).
   - Always use: `low + (high - low) / 2`.

2. **Off-by-One Infinite Loops:**
   - If you write `while (low < high)` instead of `while (low <= high)`, your loop may terminate early, missing the element when `low == high`.
   - If you update pointers as `low = mid` or `high = mid`, you can get stuck in an infinite loop because `mid` might not change value. Always shift past `mid`: `low = mid + 1` or `high = mid - 1`.

---

> 👉 Next, open `05-Strings.md` to learn how character sequences are handled and optimized! 💪



---

## Supplementary Notes from 03_Binary Search.md

# Binary Search Algorithm 🔍

**Prerequisite**: The array must be sorted. Binary search is an efficient algorithm for finding a target value within a sorted array.

#include <iostream>
using namespace std;
// Binary Search function
int BinarySearch(int *arr, int n, int key) {
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == key) {
           return mid; // Key found at index mid
        }
        else if (arr[mid] < key) {
           start = mid + 1; // Search the right half
        }
        else {
           end = mid - 1; // Search the left half
        }
    }
    return -1;
}

int main() {
    // 🔑 ARRAY MUST BE SORTED
    int arr[] = {2, 3, 4, 5, 6, 33, 42};
    int n = sizeof(arr) / sizeof(int);
    cout << BinarySearch(arr, n, 4);
    return 0;
}



// ✔ Uses iterative binary search
// ✔ Uses overflow-safe mid calculation
// ✔ Correct termination condition
// ✔ Correct return values

// This is industry-standard binary search.
// 📝 Conceptual Explanation
// 🔧 Small Conceptual Cleanup (Comments)
// Your comment:


// // for even -> middle element =(first +end)/2
// // Last of first half
// Better and technically accurate version:

// Prerequisite: Array must be sorted
// mid = start + (end - start) / 2   (avoids overflow)
// If key < arr[mid] → search left half
// If key > arr[mid] → search right half

// ✅ Final Exam-Ready Version (Complete Program)
#include <iostream>
using namespace std;

int BinarySearch(int *arr, int n, int key) {
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == key)
           return mid; // Key found at index mid
        else if (arr[mid] < key)
           start = mid + 1; // Search the right half
        else
           end = mid - 1; // Search the left half
    }
    return -1; // key not found
}

int main() {
    int arr[] = {2, 5, 9, 13, 21, 30};
    int n = sizeof(arr) / sizeof(int);
    int key = 13;

   int result = BinarySearch(arr, n, key);
   if (result != -1)
       cout << "Element found at index: " << result << endl;
   else
        cout << "Element not found" << endl;

    return 0;
}
// 🧠 Binary Search Mental Model (Remember This)
// Always sorted array

// Divide → Compare → Discard half

// Loop continues until:

// Found → return index


// Range invalid → return -1

// ⏱ Time & Space Complexity (Must-Know)
// Metric	Value
// Time Complexity	O(log n)
// Space Complexity	O(1) (iterative)

// ❌ Returning wrong index or not returning -1

// time complexity of binary sort is log(n) -> 
// for 1st iteration n/2^0, for 2nd iteration n/n^1 ---> n/2^(x-1)
// by solving this x=log(base(2)n)=log(n)


// Override in array is not possible:
// int arr[5];
// cout<<arr<<'\n';
// int y=33;
// arr=&y;
// cout<<arr<<'\n';
// return 0;
// It will show error because pointers cannot be directly changed in an array 
// ❌ Why Error Occurs?
// arr is an array, not a pointer variable

// Array name represents a constant address

// You cannot change the base address of an array

// 👉 Array name = constant pointer

// ✅ Correct Explanation
// arr → base address of array

// &arr[0] → same as arr

// You cannot assign another address to arr

// ✅ Correct Example

// int arr[5] = {1,2,3,4,5};
// cout << arr << endl;      // address of first element
// cout << &arr[0] << endl; // same address

#include <iostream>
using namespace std;
int main(){
    int a=10;
    int *aptr=&a;
    cout<<aptr<<'\n';
    aptr++;
    cout<<aptr<<'\n';
    return 0;
}

// 📌 Explanation
// int takes 4 bytes

// aptr++ moves pointer by 4 bytes, not 1

// Addresses are in hexadecimal



// // integer exceed the memory by 4 bytes
// for example if address ending with 9 then next will be c due to increase in 4 bytes as here in hexadecimal format numbeing is like : 6789abcdefghijklmnop

// // ARITHEMATIC
// // adding constants
// if ptr+3 -> this statement means we adding  spaces of integer=12 spaces and /bytes 
// 3️⃣ Pointer Arithmetic Rules
// ✔ Allowed
// ptr + n

// ptr - n

// ptr2 - ptr1 (same array)

// ❌ Not Allowed
// ptr1 + ptr2

// ptr * ptr

// ptr / ptr

// 3️⃣ Pointer Arithmetic Rules
// ✔ Allowed
// ptr + n

// ptr - n

// ptr2 - ptr1 (same array)

// ❌ Not Allowed
// ptr1 + ptr2

// ptr * ptr

// ptr / ptr

int main(){
    int a=5;
    int *ptr=&a;
    cout<<ptr=&a;
    cout<<ptr<<"\n"; //first output
    ptr=ptr+3;
    cout<<(ptr-3)<<"\n"; //same value as previous output
    return 0;
}



void printArr(int *arr, int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    
}
int main(){
    int arr[]={2,4,55,323,21,32};
    int n=sizeof(arr)/sizeof(int);
    printArr(arr,n);
    return 0;
}
// elements printed
// 2 4 55 323 21 32
// 📌 Why It Works?
// arr → passed as pointer to first element

// arr[i] = *(arr + i)





//

// we can also write cout<<*(ptr+i)<<'\n'; for cout<<*ptr<<"\n";ptr=ptr+1;
// for
// add and subtract of pointers 
// addition of list address can not be happen because address cannot be added

int main(){
    int a=5;
    int *ptr=&a;
    int *ptr2=ptr1+3;
    cout<<ptr2<<"\n";
    cout<<ptr2-ptr1<<"\n";//it will give number of integer between them 
    return 0;
}
// if last digit of address is 64 then after subtraction  last digit will be 58 

// For array
int main(){
    int arr[20]={1,2,3,6,32,42,22};
    int ptr1=arr;
    int *ptr2=ptr1+3;
    cout<<*ptr2<<"\n"<<endl;
    cout<<*ptr1<<"\n"<<endl;
    cout<<ptr2-ptr1<<"\n"<<endl;
    return 0;


// Printing subarray 
#include<iostream>
using namespace std;
void printSubarray(int *arr,int n){
    for(int start=0;start<n;start++){
       for(int end=start;end<n;end++){
            cout<<"(" <<start<<","<<end<<")"<<"->"; //(0,0)->(0,1)->(0,2)....(1,1)->(1,2)....(n-1,n-1)
            for(int i=start;i<=end;i++){
                cout<<arr[i]<<" ";// for printing elements of subarray : (0,12,123,1234,12345   2,23,234,2345   3,34,345   6,32   32,42   42,22   22)
       }
            cout<<endl;
    }
}

// sum of elements of subarray
#include<iostream>
using namespace std;
void maxSubArraySum(int*arr,int n){
    int maxSum=INT_MIN;
    for(int start=0;start<n;start++){
       for(int end=start;end<n;end++){
            int Currsum=0;
            for(int i=start;i<=end;i++){
                Currsum+=arr[i];
            }
            maxSum=max(maxSum,Currsum);

    }
    cout<<"Maximum sum of subarray is: "<<maxSum<<endl;

}
int main(){
    int arr[]={2,4,55,323,21,32};
    int n=sizeof(arr)/sizeof(int);
    maxSubArraySum(arr,n);
    return 0;
}

// 🧠 Key Exam Summary (Memorize This)
// Arrays

// Array name = constant pointer

// Cannot reassign array

// Pointers
// Can change address

// Arithmetic depends on data type size

// Pointer Arithmetic
// ptr + n → jumps n elements

// ptr2 - ptr1 → number of elements

// Functions
// Array passed as pointer

// arr[i] == *(arr+i)
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
    int arr[] = {2, 4, 55, 323, 21, 32};
    int n = sizeof(arr) / sizeof(int);

    maxSubArraySum(arr, n);
    return 0;
}

// ⏱ Time Complexity
// O(n²)

// Improved from O(n³) by avoiding the inner re-summation loop.

// 🚀 BEST Approach: Kadane’s Algorithm (O(n))

// Either extend the current subarray

// Or start a new subarray at current element\




// ✅ Kadane’s Algorithm Code (Recommended)
#include <iostream>
#include <climits>
using namespace std;

void maxSubArraySum(int *arr, int n) {
    int currSum = 0;
    int maxSum = INT_MIN;

    for (int i = 0; i < n; i++) {
        currSum += arr[i];
        maxSum = max(maxSum, currSum);

        if (currSum < 0) {
            currSum = 0;
        }
    }

    cout << "Maximum sum of subarray is: " << maxSum << endl;
}

int main() {
    int arr[] = {2, 4, 55, 323, 21, 32};
    int n = sizeof(arr) / sizeof(int);

    maxSubArraySum(arr, n);
    return 0;
}

// ⏱ Time Complexity
// O(n)

// Best possible solution

// 🧠 Exam / Interview Memory Trick
// Approach	Time	Key Idea
// Brute Force	O(n³)	Check every subarray
// Optimized	O(n²)	Carry forward sum
// Kadane	O(n)	Drop negative sum
// Golden rule:

// If currentSum becomes negative → reset it

// ⚠️ Common Exam / Interview Traps
// ❌ Forgetting array must be sorted
// ❌ Using (start + end)/2 (overflow risk)
// ❌ Using start < end instead of start <= end
// ❌ Returning wrong index or not returning -1

// 📌 Key Points to Remember
// - Binary search requires a sorted array.
// - The middle element is calculated to divide the search space.
// - If the key is not found, the function returns -1.
// - Time complexity: O(log n), Space complexity: O(1).

---

## Supplementary Notes from Notes.md

# Binary Search on Arrays — Complete Striver-Style Guide

> **What You'll Learn**: Binary search on index, answer, rotated arrays, bounds, 2D arrays  
> **Prerequisites**: Array Basics, Complexity Analysis  
> **Time Required**: 8-10 hours  
> **Difficulty**: Beginner to Advanced  
> **Problems Coverage**: 35+ Problems (Easy → Medium → Hard)

---

## 1. 📌 Definition

**Binary Search** finds an element in a **sorted array** in O(log n) time by repeatedly dividing the search space in half.

**Core Idea**: If array is sorted, eliminate half the elements at each step!

---

## 2. 🌍 Real-World Analogy

### Analogy 1: Dictionary Search 📖

Looking for word "monkey" in dictionary:
- Open to middle → see "laptop"
- "monkey" comes after "laptop" → ignore first half
- Open middle of second half → see "ocean"
- "monkey" comes before "ocean" → ignore second half
- Continue until found!

### Analogy 2: Guessing Game 🎯

"I'm thinking of a number between 1-100"
- Guess 50 → "Too high!"
- Now you know it's 1-49
- Guess 25 → "Too low!"
- Now you know it's 26-49
- Each guess eliminates half the possibilities!

---

## 3. 🎨 Visual Diagram

### Binary Search Execution

```
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
Target: 23
Indices: 0   1   2   3   4   5   6   7   8   9   10

Step 1: left=0, right=10, mid=5
        arr[5] = 23 == target ✓ FOUND!

Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
Target: 12
Indices: 0   1   2   3   4   5   6   7   8   9   10

Step 1: left=0, right=10, mid=5
        arr[5] = 23 > 12 → target is in LEFT half
        right = mid - 1 = 4

Step 2: left=0, right=4, mid=2
        arr[2] = 8 < 12 → target is in RIGHT half
        left = mid + 1 = 3

Step 3: left=3, right=4, mid=3
        arr[3] = 12 == target ✓ FOUND!
```

---

## 4. 🔑 Pattern Recognition Keywords

**Look for these words in problems**:
- "Sorted array"
- "Find element"
- "Search"
- "Lower bound" / "Upper bound"
- "First/last occurrence"
- "Peak element"
- "Rotated sorted array"
- "Minimize/Maximize" (binary search on answer)

---

## 5. 📋 Complete Template Collection

### Template 1: Basic Binary Search (Find Element)

```cpp
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;  // Avoid overflow
        
        if(arr[mid] == target) {
            return mid;  // Found!
        } else if(arr[mid] < target) {
            left = mid + 1;  // Search right half
        } else {
            right = mid - 1;  // Search left half
        }
    }
    
    return -1;  // Not found
}
```

### Template 2: Lower Bound (First element ≥ target)

```cpp
int lowerBound(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int ans = arr.size();
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(arr[mid] >= target) {
            ans = mid;
            right = mid - 1;  // Try to find earlier occurrence
        } else {
            left = mid + 1;
        }
    }
    
    return ans;
}
```

### Template 3: Upper Bound (First element > target)

```cpp
int upperBound(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int ans = arr.size();
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(arr[mid] > target) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return ans;
}
```

### Template 4: Binary Search on Answer (Optimization)

```cpp
bool isFeasible(int mid, vector<int>& nums, int threshold) {
    // Check if 'mid' is a feasible answer
    // Return true if possible, false otherwise
}

int binarySearchOnAnswer(int left, int right, vector<int>& nums, int threshold) {
    int result = -1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(isFeasible(mid, nums, threshold)) {
            result = mid;
            right = mid - 1;  // Try to minimize (for minimization problems)
            // left = mid + 1;  // Try to maximize (for maximization problems)
        } else {
            left = mid + 1;
            // right = mid - 1;  // For maximization
        }
    }
    
    return result;
}
```

### Template 5: Search in Rotated Sorted Array

```cpp
int searchRotated(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(nums[mid] == target) return mid;
        
        // Determine which half is sorted
        if(nums[left] <= nums[mid]) {
            // Left half is sorted
            if(nums[left] <= target && target < nums[mid]) {
                right = mid - 1;  // Target in left half
            } else {
                left = mid + 1;   // Target in right half
            }
        } else {
            // Right half is sorted
            if(nums[mid] < target && target <= nums[right]) {
                left = mid + 1;   // Target in right half
            } else {
                right = mid - 1;  // Target in left half
            }
        }
    }
    
    return -1;
}
```

### Template 6: Find Peak Element

```cpp
int findPeakElement(vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;
    
    while(left < right) {
        int mid = left + (right - left) / 2;
        
        if(nums[mid] > nums[mid + 1]) {
            // Decreasing sequence, peak is on left (including mid)
            right = mid;
        } else {
            // Increasing sequence, peak is on right
            left = mid + 1;
        }
    }
    
    return left;  // or right (they're equal)
}
```

---

## 6. 🔍 Step-by-Step Example

### Problem: Binary Search

```cpp
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while(left <= right) {
        // Calculate mid (avoids overflow)
        int mid = left + (right - left) / 2;
        
        if(arr[mid] == target) {
            return mid;
        } else if(arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    vector<int> arr = {2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91};
    int target = 23;
    
    int result = binarySearch(arr, target);
    
    if(result != -1) {
        cout << "Found at index " << result << endl;  // 5
    } else {
        cout << "Not found!" << endl;
    }
    
    return 0;
}
```

**Dry Run** (searching for 12):
```
Array: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
        L                    M                    R

Iteration 1:
  left = 0, right = 10
  mid = 0 + (10-0)/2 = 5
  arr[5] = 23
  23 > 12 → go LEFT
  right = 5 - 1 = 4

Iteration 2:
  left = 0, right = 4
  mid = 0 + (4-0)/2 = 2
  arr[2] = 8
  8 < 12 → go RIGHT
  left = 2 + 1 = 3

Iteration 3:
  left = 3, right = 4
  mid = 3 + (4-3)/2 = 3
  arr[3] = 12
  12 == 12 ✓ FOUND!
  Return index 3
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Overflow in Mid Calculation
```cpp
// WRONG: Can overflow for large indices
int mid = (left + right) / 2;

// CORRECT: Safe from overflow
int mid = left + (right - left) / 2;
```

### Mistake 2: Wrong Loop Condition
```cpp
// WRONG: Misses single element case
while(left < right) {

// CORRECT: Include equality
while(left <= right) {
```

### Mistake 3: Infinite Loop
```cpp
// WRONG: May not converge
if(arr[mid] < target) {
    left = mid;  // Should be mid + 1!
}

// CORRECT: Always move past mid
if(arr[mid] < target) {
    left = mid + 1;
} else {
    right = mid - 1;
}
```

### Mistake 4: Not Handling Empty Array
```cpp
// WRONG: Will crash on empty array
int right = arr.size() - 1;  // -1 for empty array!

// CORRECT: Check first
if(arr.empty()) return -1;
```

---

## 8. ⏱️ Time & Space Complexity

| Variant | Time | Space | Reasoning |
|---------|------|-------|-----------|
| **Binary Search** | **O(log n)** | **O(1)** | Halve search space each step |
| **Linear Search** | O(n) | O(1) | Check each element |
| **Recursive BS** | O(log n) | O(log n) | Call stack depth |

**Why O(log n)?**
- Each step: n → n/2 → n/4 → ... → 1
- Number of steps = log₂(n)
- Example: 1024 elements → 10 steps (2¹⁰ = 1024)

---

## 9. 📝 Pattern Variations with Complete Solutions

### Variation 1: Floor and Ceil in Sorted Array

**Floor**: Largest element ≤ target  
**Ceil**: Smallest element ≥ target

```cpp
#include <iostream>
#include <vector>
using namespace std;

pair<int, int> getFloorAndCeil(vector<int>& arr, int target) {
    int n = arr.size();
    int floor = -1, ceil = -1;
    
    // Find Floor
    int left = 0, right = n - 1;
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(arr[mid] <= target) {
            floor = arr[mid];
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    // Find Ceil
    left = 0, right = n - 1;
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(arr[mid] >= target) {
            ceil = arr[mid];
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return {floor, ceil};
}
```

### Variation 2: First and Last Occurrence (Count Occurrences)

```cpp
#include <iostream>
#include <vector>
using namespace std;

int firstOccurrence(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    int first = -1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(arr[mid] == target) {
            first = mid;
            right = mid - 1;  // Keep searching left
        } else if(arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return first;
}

int lastOccurrence(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    int last = -1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(arr[mid] == target) {
            last = mid;
            left = mid + 1;  // Keep searching right
        } else if(arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return last;
}

int countOccurrences(vector<int>& arr, int target) {
    int first = firstOccurrence(arr, target);
    if(first == -1) return 0;
    
    int last = lastOccurrence(arr, target);
    return last - first + 1;
}
```

### Variation 3: Search Insert Position

```cpp
int searchInsert(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(nums[mid] == target) {
            return mid;
        } else if(nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return left;  // Insert position
}
```

### Variation 4: Single Element in Sorted Array

**Problem**: Every element appears twice except one. Find it in O(log n).

```cpp
int singleNonDuplicate(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    
    while(left < right) {
        int mid = left + (right - left) / 2;
        
        // Ensure mid is even for proper pairing
        if(mid % 2 == 1) mid--;
        
        // If pair is maintained, single element is on right
        if(nums[mid] == nums[mid + 1]) {
            left = mid + 2;
        } else {
            // Pair broken, single element is on left
            right = mid;
        }
    }
    
    return nums[left];
}
```

### Variation 5: Find Minimum in Rotated Sorted Array

```cpp
int findMin(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    
    while(left < right) {
        int mid = left + (right - left) / 2;
        
        if(nums[mid] > nums[right]) {
            // Minimum is in right half
            left = mid + 1;
        } else {
            // Minimum is in left half (including mid)
            right = mid;
        }
    }
    
    return nums[left];
}
```

### Variation 6: Find Rotation Count

```cpp
int findRotationCount(vector<int>& nums) {
    int n = nums.size();
    int left = 0, right = n - 1;
    
    // If array is not rotated
    if(nums[left] <= nums[right]) return 0;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        int next = (mid + 1) % n;
        int prev = (mid + n - 1) % n;
        
        // Check if mid is the minimum element
        if(nums[mid] <= nums[next] && nums[mid] <= nums[prev]) {
            return mid;  // Index of minimum = rotation count
        }
        
        if(nums[mid] <= nums[right]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return 0;
}
```

---

## 10. 💡 Pro Tips

1. **Always use** `left + (right - left) / 2` for mid
2. **Loop condition**: `left <= right` for standard search
3. **Movement**: Always `mid + 1` or `mid - 1` (never just `mid`)
4. **Sorted array required** — Or can be made sorted
5. **Binary search on answer** — When optimizing a value
6. **Handle edge cases** — Empty array, single element

---

## 11. 🎯 When to Use Binary Search

✅ **Use when**:
- Array is sorted (or can be sorted)
- Looking for specific element
- Need first/last occurrence
- Optimization problem (minimize/maximize)
- Search space can be halved
- Rotated sorted array

❌ **Don't use when**:
- Array is unsorted (use hash map or linear search)
- Need to find all occurrences (use two pointers after finding one)
- Elements change frequently (array not static)
- Small arrays (linear search is faster due to overhead)

---

## 12. 📚 Complete Problem List (Striver-Style)

### 🟢 BS on 1D Arrays - Basic (Easy)

1. **Binary Search** - Find element in sorted array
2. **Lower Bound** - First element ≥ target
3. **Upper Bound** - First element > target
4. **Search Insert Position** - Where to insert target
5. **Floor and Ceil** - Largest ≤ and smallest ≥ target
6. **First and Last Occurrence** - Find range of target
7. **Count Occurrences** - How many times target appears

### 🟡 BS on 1D Arrays - Advanced (Medium)

1. **Search in Rotated Sorted Array-I** - Unique elements
2. **Search in Rotated Sorted Array-II** - With duplicates
3. **Find Minimum in Rotated Sorted Array** - Find pivot
4. **Find Rotation Count** - How many times rotated
5. **Single Element in Sorted Array** - O(log n) solution
6. **Find Peak Element** - Element greater than neighbors

### 🔵 BS on Answers - Optimization Problems (Medium)

1. **Find Square Root** - Integer square root using BS
2. **Find Nth Root** - Nth root of a number
3. **Koko Eating Bananas** - Minimum speed to eat all
4. **Minimum Days to Make M Bouquets** - Time optimization
5. **Find the Smallest Divisor** - Sum ≤ threshold
6. **Capacity to Ship Packages** - Within D days
7. **Kth Missing Positive Number** - Find kth missing

### 🔴 BS on Answers - Hard Problems

1. **Aggressive Cows** - Maximize minimum distance
2. **Book Allocation Problem** - Minimize maximum pages
3. **Split Array - Largest Sum** - Similar to book allocation
4. **Painter's Partition** - Minimize painting time
5. **Minimize Max Distance to Gas Station** - Advanced hard

### 🟣 BS on 2D Arrays

1. **Find Row with Maximum 1's** - Binary matrix
2. **Search in a 2D Matrix** - Strictly sorted rows
3. **Search in 2D Matrix-II** - Row & column sorted
4. **Find Peak Element-II** - 2D peak finding
5. **Matrix Median** - Median of row-wise sorted matrix

### 🟠 Hard Classic Problems

1. **Median of 2 Sorted Arrays** - O(log(min(m,n)))
2. **Kth Element of 2 Sorted Arrays** - Find kth element

---

## 13. 🗺️ Binary Search Learning Roadmap (Striver-Style)

### Week 1: BS Fundamentals (Days 1-3)

**Day 1: Basic Binary Search**
- [ ] Understand binary search concept
- [ ] Learn basic template
- [ ] Solve: Binary Search (LC 704)
- [ ] Solve: Lower Bound
- [ ] Solve: Upper Bound
- **Time**: 2-3 hours

**Day 2: BS Variations on 1D Arrays**
- [ ] Search Insert Position (LC 35)
- [ ] Floor and Ceil
- [ ] First and Last Occurrence (LC 34)
- [ ] Count Occurrences
- **Time**: 3 hours

**Day 3: Rotated Sorted Arrays**
- [ ] Understand rotation concept
- [ ] Search in Rotated Array-I (LC 33)
- [ ] Search in Rotated Array-II (with duplicates)
- [ ] Find Minimum in Rotated Array (LC 153)
- [ ] Find Rotation Count
- **Time**: 3-4 hours

### Week 2: BS on Answers (Days 4-6)

**Day 4: Square Root & Nth Root**
- [ ] Find Square Root (LC 69)
- [ ] Find Nth Root
- [ ] Understand BS on answer pattern
- **Time**: 2-3 hours

**Day 5: Optimization Problems I**
- [ ] Koko Eating Bananas (LC 875)
- [ ] Minimum Days to Make M Bouquets (LC 1482)
- [ ] Find the Smallest Divisor (LC 1283)
- **Time**: 3 hours

**Day 6: Optimization Problems II**
- [ ] Capacity to Ship Packages (LC 1011)
- [ ] Kth Missing Positive Number (LC 1539)
- [ ] Single Element in Sorted Array (LC 540)
- **Time**: 3 hours

### Week 3: Advanced BS (Days 7-9)

**Day 7: Hard BS on Answers**
- [ ] Aggressive Cows (SPOJ)
- [ ] Book Allocation Problem (GFG)
- [ ] Split Array - Largest Sum (LC 410)
- **Time**: 4 hours

**Day 8: More Hard Problems**
- [ ] Painter's Partition
- [ ] Minimize Max Distance to Gas Station
- [ ] Find Peak Element (LC 162)
- **Time**: 3-4 hours

**Day 9: BS on 2D Arrays I**
- [ ] Find Row with Maximum 1's
- [ ] Search in a 2D Matrix (LC 74)
- [ ] Search in 2D Matrix-II (LC 240)
- **Time**: 3 hours

### Week 4: Mastery (Days 10-12)

**Day 10: BS on 2D Arrays II**
- [ ] Find Peak Element-II (LC 1901)
- [ ] Matrix Median
- **Time**: 3 hours

**Day 11: Classic Hard Problems**
- [ ] Median of 2 Sorted Arrays (LC 4) ⭐⭐⭐
- [ ] Kth Element of 2 Sorted Arrays
- **Time**: 4 hours

**Day 12: Revision & Mock Test**
- [ ] Revise all templates
- [ ] Solve 5 random BS problems
- [ ] Time yourself: 30 min per medium, 45 min per hard
- **Time**: 4 hours

---

## 14. 🎯 Key Takeaways

1. **Binary search requires sorted array** (or monotonic property)
2. **Time complexity**: O(log n) — extremely fast!
3. **Mid formula**: `left + (right - left) / 2` (avoid overflow)
4. **Loop condition**: `left <= right` for standard search
5. **Always move past mid**: `mid + 1` or `mid - 1`
6. **Binary search on answer** — Powerful optimization technique
7. **Rotated arrays** — Determine which half is sorted
8. **Lower/Upper bound** — Find first/last occurrences
9. **2D arrays** — Can treat as 1D or use row/column properties
10. **Peak finding** — Follow increasing direction

---

## 15. 💡 Pro Tips from Striver

1. **Master the templates** — Don't memorize, understand
2. **Practice pattern recognition** — Keywords → Pattern mapping
3. **Dry run on paper** — Essential for rotated arrays
4. **Handle edge cases** — Empty array, single element, all same
5. **BS on answer** — If problem asks minimize/maximize, think BS
6. **Monotonicity** — Key to BS on answer (if x works, x+1 also works)
7. **Search space** — Identify min and max possible answers
8. **Feasibility function** — Write clean check function
9. **Time yourself** — Build speed for interviews
10. **Revise weekly** — Revisit old problems

---

## 16. 🎓 When to Use Binary Search

✅ **Use when**:
- Array is sorted (or can be sorted)
- Looking for specific element
- Need first/last occurrence
- Optimization problem (minimize/maximize)
- Search space can be halved
- Rotated sorted array
- Monotonic function/property
- 2D sorted matrix

❌ **Don't use when**:
- Array is unsorted (use hash map or linear search)
- Need to find all occurrences (use two pointers after finding one)
- Elements change frequently (array not static)
- Small arrays (linear search is faster due to overhead)
- No monotonic property (for BS on answer)

---

**Next**: Solve problems in `Problems/` folder! →

[← Back to README](../README.md) | [Easy Problems →](../../03-Arrays-and-Strings/problems/001-two-sum-pair-sum.md) | [Medium Problems →](../../03-Arrays-and-Strings/problems/002-majority-element.md) | [Hard Problems →](../../03-Arrays-and-Strings/problems/004-maximum-subarray-kadane.md)
