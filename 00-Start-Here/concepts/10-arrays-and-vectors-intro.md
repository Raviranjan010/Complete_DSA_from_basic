# Array Basics — Complete Beginner's Guide

> **What You'll Learn**: What arrays are, how they work, and why they're fundamental to programming  
> **Prerequisites**: Basic C++ syntax (variables, loops) from Topic 00  
> **Time Required**: 2-3 hours  
> **Importance**: 🌟🌟🌟🌟🌟 (Foundation of all data structures)

---

## 1. 📌 What is an Array? (Simple Definition)

An **array** is a collection of items stored in **contiguous (side-by-side) memory locations**, where each item can be accessed using an **index number**.

Think of it as a **row of lockers** in a school:
- Each locker has a **number** (index)
- All lockers are **the same size**
- Lockers are **next to each other** (contiguous)
- You can **quickly find** any locker if you know its number

**Key Properties**:
1. **Fixed size** (for static arrays) — size determined at creation
2. **Same data type** — all elements must be the same type (all integers, all characters, etc.)
3. **Contiguous memory** — elements stored one after another
4. **Fast access** — O(1) time to access any element by index

---

## 2. 🌍 Real-World Analogies

### Analogy 1: Egg Carton 🥚

```
┌───┬───┬───┬───┬───┬───┐
│ 🥚│ 🥚│ 🥚│ 🥚│ 🥚│ 🥚│  ← 6 eggs (elements)
└───┴───┴───┴───┴───┴───┘
  0   1   2   3   4   5    ← Position numbers (indices)
```

- Carton holds **exactly 6 eggs** (fixed size)
- All slots are **identical** (same data type)
- Slots are **arranged in a row** (contiguous)
- You say "give me egg #3" (indexing)

### Analogy 2: Apartment Building 🏢

```
Floor 5: [501] [502] [503] [504] [505]
Floor 4: [401] [402] [403] [404] [405]
Floor 3: [301] [302] [303] [304] [305]
Floor 2: [201] [202] [203] [204] [205]
Floor 1: [101] [102] [103] [104] [105]
```

- Each apartment has a **unique number**
- Apartments are **numbered systematically**
- You can **directly go** to apartment 305 without checking others
- **Same structure** for all apartments

---

## 3. 🎨 Visual Diagram: Memory Layout

### How Arrays Look in Computer Memory

```
Declaration: int arr[5] = {10, 20, 30, 40, 50};

Memory Addresses (simplified):
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│   10    │   20    │   30    │   40    │   50    │  ← Values
└─────────┴─────────┴─────────┴─────────┴─────────┘
  1000      1004      1008      1012      1016     ← Memory Addresses
   [0]       [1]       [2]       [3]       [4]     ← Indices
```

**Why addresses increase by 4?**
- Each `int` takes **4 bytes** in C++
- Address of `arr[i]` = Base Address + (i × size of element)
- Example: `arr[2]` = 1000 + (2 × 4) = 1008

💡 **TRICK**: Array indexing is just **math**! The computer calculates: `Address = Start + (Index × Element_Size)`

---

## 4. 📋 Array Declaration in C++

### Method 1: Declare without initializing
```cpp
int arr[5];  // Creates array with 5 integers (garbage values)
```

### Method 2: Declare and initialize
```cpp
int arr[5] = {10, 20, 30, 40, 50};  // Explicit size
```

### Method 3: Let compiler count elements
```cpp
int arr[] = {10, 20, 30, 40, 50};  // Compiler knows size is 5
```

### Method 4: Initialize with zeros
```cpp
int arr[5] = {0};  // All elements become 0
// Or
int arr[5] = {};   // Same effect
```

### Complete Example with Explanation
```cpp
#include <iostream>
using namespace std;

int main() {
    // Declare array of 5 integers
    int marks[5] = {85, 92, 78, 90, 88};
    
    // Access elements (0-indexed!)
    cout << "First mark: " << marks[0] << endl;    // 85
    cout << "Third mark: " << marks[2] << endl;    // 78
    cout << "Last mark: " << marks[4] << endl;     // 88
    
    // Modify elements
    marks[2] = 82;  // Change 78 to 82
    cout << "New third mark: " << marks[2] << endl; // 82
    
    // Get array size
    int size = sizeof(marks) / sizeof(marks[0]);
    cout << "Array size: " << size << endl;  // 5
    
    return 0;
}
```

---

## 5. 🔑 0-Based Indexing Explained

### Why Start at 0? (Not 1!)

**Historical Reason**: In C/C++, an array name is actually a **pointer to the first element**.

```
Array: int arr[5] = {10, 20, 30, 40, 50};

arr is a pointer to address 1000

arr[0] means: *(arr + 0) → Go to address 1000 + (0×4) = 1000 → Get value 10
arr[1] means: *(arr + 1) → Go to address 1000 + (1×4) = 1004 → Get value 20
arr[2] means: *(arr + 2) → Go to address 1000 + (2×4) = 1008 → Get value 30
```

**Visual Explanation**:
```
Think of array name as "starting point":
arr → points to beginning

To get element, you say "how many steps from start":
0 steps → first element
1 step  → second element
2 steps → third element
```

### Step-by-Step Trace: Accessing Elements

```cpp
int arr[5] = {10, 20, 30, 40, 50};
// Index:   0    1    2    3    4

// Access arr[2]:
// Step 1: Start at arr (address 1000)
// Step 2: Calculate offset: 2 × 4 bytes = 8 bytes
// Step 3: Go to address 1000 + 8 = 1008
// Step 4: Read value at 1008 → 30
```

---

## 6. 📚 Basic Array Operations

### Operation 1: Access (Read)
**Time Complexity**: O(1) — Instant!

```cpp
int arr[5] = {10, 20, 30, 40, 50};
int value = arr[3];  // Directly get 40 — no searching needed!
```

### Operation 2: Update (Modify)
**Time Complexity**: O(1) — Instant!

```cpp
int arr[5] = {10, 20, 30, 40, 50};
arr[2] = 35;  // Change 30 to 35 — direct access!
// Array becomes: {10, 20, 35, 40, 50}
```

### Operation 3: Insert (at end)
**Time Complexity**: O(1) — If space available

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[10] = {10, 20, 30};  // Size 10, but only 3 elements used
    int count = 3;  // Track how many elements are actually used
    
    // Insert 40 at the end
    arr[count] = 40;  // arr[3] = 40
    count++;  // Now 4 elements
    
    return 0;
}
```

### Operation 4: Insert (at specific position)
**Time Complexity**: O(n) — Need to shift elements

```cpp
#include <iostream>
using namespace std;

// Insert value at given position
void insert(int arr[], int &count, int position, int value) {
    // Shift elements to the right
    for(int i = count; i > position; i--) {
        arr[i] = arr[i-1];
    }
    
    // Insert new value
    arr[position] = value;
    count++;  // Increase element count
}

int main() {
    int arr[10] = {10, 20, 30, 40, 50};
    int count = 5;
    
    // Insert 25 at position 2
    insert(arr, count, 2, 25);
    
    // Array: {10, 20, 25, 30, 40, 50}
    for(int i = 0; i < count; i++) {
        cout << arr[i] << " ";
    }
    
    return 0;
}
```

**Visual Trace**:
```
Original:  [10] [20] [30] [40] [50]
Indices:    0    1    2    3    4

Insert 25 at position 2:

Step 1: Shift elements from position 2 onwards
        [10] [20] [30] [30] [40] [50]
                            ↑ moved right

Step 2: Shift more
        [10] [20] [30] [40] [40] [50]
                                 ↑ moved right

Step 3: Insert at position 2
        [10] [20] [25] [30] [40] [50]
                     ↑ inserted!
```

### Operation 5: Delete
**Time Complexity**: O(n) — Need to shift elements

```cpp
#include <iostream>
using namespace std;

// Delete element at given position
void deleteElement(int arr[], int &count, int position) {
    // Shift elements to the left
    for(int i = position; i < count - 1; i++) {
        arr[i] = arr[i+1];
    }
    
    count--;  // Decrease element count
}

int main() {
    int arr[10] = {10, 20, 30, 40, 50};
    int count = 5;
    
    // Delete element at position 2 (value 30)
    deleteElement(arr, count, 2);
    
    // Array: {10, 20, 40, 50}
    for(int i = 0; i < count; i++) {
        cout << arr[i] << " ";
    }
    
    return 0;
}
```

### Operation 6: Search (Linear Search)
**Time Complexity**: O(n) — Check each element

```cpp
#include <iostream>
using namespace std;

// Find position of a value
int linearSearch(int arr[], int count, int target) {
    for(int i = 0; i < count; i++) {
        if(arr[i] == target) {
            return i;  // Found! Return index
        }
    }
    return -1;  // Not found
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int count = 5;
    
    int target = 30;
    int position = linearSearch(arr, count, target);
    
    if(position != -1) {
        cout << "Found " << target << " at index " << position << endl;
    } else {
        cout << "Not found!" << endl;
    }
    
    return 0;
}
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Out of Bounds Access
```cpp
int arr[5] = {10, 20, 30, 40, 50};
cout << arr[5];  // ERROR! Valid indices: 0-4, NOT 5!
```

✅ **Fix**: Always check: `if(index >= 0 && index < size)`

### Mistake 2: Forgetting 0-Based Indexing
```cpp
int arr[5] = {10, 20, 30, 40, 50};

// WRONG: Trying to access "first" element with index 1
cout << arr[1];  // Prints 20 (second element), not 10!

// CORRECT: First element is at index 0
cout << arr[0];  // Prints 10 ✓
```

### Mistake 3: Array Size Confusion
```cpp
int arr[5] = {10, 20, 30};

// This is WRONG!
for(int i = 0; i <= 5; i++) {  // <= causes out of bounds!
    cout << arr[i] << " ";
}

// CORRECT: Use < not <=
for(int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
```

### Mistake 4: Using Uninitialized Arrays
```cpp
int arr[5];  // Contains garbage values!
cout << arr[0];  // Random value (undefined behavior)

// CORRECT: Initialize
int arr[5] = {0};  // All zeros
// Or
int arr[5] = {};   // All zeros
```

---

## 8. ⏱️ Time & Space Complexity Summary

| Operation | Time Complexity | Space Complexity | Reasoning |
|-----------|----------------|------------------|-----------|
| Access by index | **O(1)** | **O(1)** | Direct calculation, no iteration |
| Update by index | **O(1)** | **O(1)** | Direct access and modify |
| Insert at end | **O(1)** | **O(1)** | Just place at next position |
| Insert at position | **O(n)** | **O(1)** | Must shift elements |
| Delete from end | **O(1)** | **O(1)** | Just decrease count |
| Delete from position | **O(n)** | **O(1)** | Must shift elements |
| Search (unsorted) | **O(n)** | **O(1)** | May need to check all |
| Search (sorted, binary) | **O(log n)** | **O(1)** | Divide and conquer |

**Space Complexity**: Arrays use **O(n)** space total (n elements × size of each element)

---

## 9. 📝 Practice Examples

### Example 1: Find Sum of All Elements
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {5, 10, 15, 20, 25};
    int n = 5;
    int sum = 0;
    
    // Traverse and add each element
    for(int i = 0; i < n; i++) {
        sum += arr[i];
    }
    
    cout << "Sum: " << sum << endl;  // 75
    
    return 0;
}
```

### Example 2: Find Maximum Element
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {12, 45, 23, 67, 34};
    int n = 5;
    
    // Assume first element is maximum
    int maxVal = arr[0];
    
    // Compare with each element
    for(int i = 1; i < n; i++) {
        if(arr[i] > maxVal) {
            maxVal = arr[i];  // Update maximum
        }
    }
    
    cout << "Maximum: " << maxVal << endl;  // 67
    
    return 0;
}
```

### Example 3: Reverse Array
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    
    // Use two pointers
    int left = 0;
    int right = n - 1;
    
    while(left < right) {
        // Swap elements
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        
        // Move pointers
        left++;
        right--;
    }
    
    // Print reversed array
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";  // 5 4 3 2 1
    }
    
    return 0;
}
```

---

## 10. 💡 Key Takeaways

1. **Arrays store elements in contiguous memory** — like lockers in a row
2. **Indexing starts at 0** — first element is `arr[0]`, not `arr[1]`
3. **Access is instant** — O(1) time using index
4. **Size is fixed** (for static arrays) — can't change after creation
5. **All elements same type** — can't mix integers and strings
6. **Watch boundaries** — never access `arr[size]`, only `arr[0]` to `arr[size-1]`

---

## 11. 🎯 What's Next?

Now that you understand array basics, continue learning:
1. ✅ **Memory Model** — How arrays are stored in RAM
2. ✅ **Indexing and Traversal** — Different ways to navigate arrays
3. ✅ **Complexity Analysis** — Understanding performance
4. ✅ **Vector vs Array** — When to use which

**Next File**: [Memory Model](09-pointers-and-memory-model.md) →

---

**🎉 Congratulations! You've learned Array Basics!**

*Remember: Arrays are the foundation. Master them, and everything else becomes easier!*


---

## Supplementary Reference from 03_Operations_Complexity.md

# Complexity Analysis for Arrays

> **What You'll Learn**: Time/space complexity for all array operations  
> **Prerequisites**: Array Basics, Indexing  
> **Time Required**: 1 hour

---

## 1. 📌 Time Complexity Summary Table

| Operation | Best Case | Average Case | Worst Case | Reasoning |
|-----------|-----------|--------------|------------|-----------|
| **Access by index** | O(1) | O(1) | O(1) | Direct address calculation |
| **Search (unsorted)** | O(1) | O(n) | O(n) | May need to check all elements |
| **Search (sorted, binary)** | O(1) | O(log n) | O(log n) | Halve search space each step |
| **Insert at end** | O(1) | O(1) | O(1) | Just place at next position |
| **Insert at position** | O(1) | O(n) | O(n) | Must shift n-i elements |
| **Delete from end** | O(1) | O(1) | O(1) | Just decrease count |
| **Delete from position** | O(1) | O(n) | O(n) | Must shift n-i-1 elements |
| **Update by index** | O(1) | O(1) | O(1) | Direct access and modify |

---

## 2. 🔍 Step-by-Step Complexity Calculation

### Example 1: Single Loop
```cpp
for(int i = 0; i < n; i++) {
    cout << arr[i] << endl;  // O(1) operation
}
// Total: n × O(1) = O(n)
```

### Example 2: Nested Loops
```cpp
for(int i = 0; i < n; i++) {           // Runs n times
    for(int j = 0; j < n; j++) {       // Runs n times
        cout << arr[i][j] << " ";      // O(1) operation
    }
}
// Total: n × n × O(1) = O(n²)
```

### Example 3: Two Separate Loops
```cpp
for(int i = 0; i < n; i++) {           // O(n)
    sum += arr[i];
}

for(int i = 0; i < n; i++) {           // O(n)
    product *= arr[i];
}
// Total: O(n) + O(n) = O(n) [Not O(2n), constants dropped]
```

---

## 3. 📊 Space Complexity

### O(1) Space — No Extra Memory
```cpp
int findMax(int arr[], int n) {
    int maxVal = arr[0];  // O(1) extra space
    for(int i = 1; i < n; i++) {
        if(arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}
```

### O(n) Space — Auxiliary Array
```cpp
void createCopy(int arr[], int n) {
    int* copy = new int[n];  // O(n) extra space
    for(int i = 0; i < n; i++) {
        copy[i] = arr[i];
    }
    delete[] copy;
}
```

---

## 4. 💡 Optimization Tips

### Tip 1: Use Binary Search on Sorted Arrays
```cpp
// O(n) → O(log n)
int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(arr[mid] == target) return mid;
        else if(arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    
    return -1;
}
```

### Tip 2: Avoid Unnecessary Copies
```cpp
// BAD: O(n) space
void process(int arr[], int n) {
    int temp[n];
    for(int i = 0; i < n; i++) {
        temp[i] = arr[i];  // Unnecessary copy
    }
    // ... process temp ...
}

// GOOD: O(1) space
void process(int arr[], int n) {
    // ... process arr directly ...
}
```

---

## 5. 📝 Practice Problems

1. What is the complexity of finding duplicates in an unsorted array? **Answer**: O(n²) brute force, O(n) with hash map
2. What is the space complexity of reversing an array in-place? **Answer**: O(1)
3. What is the complexity of merging two sorted arrays? **Answer**: O(n+m) time, O(n+m) space

---

**🎯 Next**: Apply these concepts in pattern-specific folders!


---

## Supplementary Reference from 04_Vector_vs_Array.md

# Vector vs Array — Decision Guide

> **What You'll Learn**: When to use vector vs static array, trade-offs, performance  
> **Prerequisites**: Array Basics, Vector Basics  
> **Time Required**: 30 minutes

---

## 1. 📌 Quick Comparison

| Feature | Static Array | std::vector |
|---------|--------------|-------------|
| **Size** | Fixed at compile time | Dynamic, changes at runtime |
| **Declaration** | `int arr[10]` | `vector<int> v` |
| **Memory** | Stack (usually) | Heap |
| **Resizing** | ❌ Not possible | ✅ Automatic |
| **Performance** | Slightly faster | Minimal overhead |
| **Safety** | No bounds checking | `at()` method available |
| **STL Algorithms** | Limited | Full support |
| **Size Tracking** | Manual | `size()` method |

---

## 2. 🎯 Decision Tree

```
Do you know the size at compile time?
├─ YES → Do you need to resize?
│  ├─ NO → Use Static Array
│  └─ YES → Use Vector
│
└─ NO → Use Vector
```

---

## 3. 💡 When to Use Static Arrays

### ✅ Use Arrays When:

1. **Fixed, known size**
```cpp
int daysInMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
// Size will never change
```

2. **Performance critical** (embedded systems, competitive programming)
```cpp
// Array: No overhead
int arr[1000000];  // Fast allocation on stack

// Vector: Slight overhead
vector<int> v(1000000);  // Heap allocation + tracking
```

3. **Memory constrained**
```cpp
// Array: Exact memory usage
int arr[100];  // Exactly 400 bytes

// Vector: Extra memory for capacity tracking
vector<int> v(100);  // 400+ bytes (capacity might be larger)
```

4. **C compatibility**
```cpp
// C function expects array
void process(int arr[], int size);

int arr[100];
process(arr, 100);  // Works directly
```

---

## 4. 💡 When to Use Vectors

### ✅ Use Vectors When:

1. **Unknown size**
```cpp
vector<int> numbers;
int n;
while(cin >> n && n != -1) {
    numbers.push_back(n);  // Grows as needed
}
```

2. **Frequent insertions/deletions**
```cpp
vector<int> v = {1, 2, 3, 4, 5};
v.push_back(6);      // Easy!
v.pop_back();        // Easy!
// Try this with static array...
```

3. **Need STL algorithms**
```cpp
vector<int> v = {5, 2, 8, 1, 9};
sort(v.begin(), v.end());           // Sort
reverse(v.begin(), v.end());        // Reverse
unique(v.begin(), v.end());         // Remove duplicates
// Much easier than manual implementation!
```

4. **Safety matters**
```cpp
vector<int> v = {1, 2, 3};
cout << v.at(5);  // Throws exception (safe!)

int arr[3] = {1, 2, 3};
cout << arr[5];   // Undefined behavior (unsafe!)
```

5. **Need to track size**
```cpp
vector<int> v;
v.push_back(10);
v.push_back(20);
cout << v.size();  // 2 (automatic tracking)

int arr[100];
int count = 0;     // Manual tracking required!
arr[0] = 10;
arr[1] = 20;
count = 2;
```

---

## 5. 📊 Performance Comparison

### Benchmark: Adding 1 Million Elements

```cpp
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    // Test 1: Static array
    auto start = high_resolution_clock::now();
    int arr[1000000];
    for(int i = 0; i < 1000000; i++) {
        arr[i] = i;
    }
    auto end = high_resolution_clock::now();
    cout << "Array: " << duration_cast<milliseconds>(end - start).count() << " ms" << endl;
    
    // Test 2: Vector without reserve
    start = high_resolution_clock::now();
    vector<int> v1;
    for(int i = 0; i < 1000000; i++) {
        v1.push_back(i);
    }
    end = high_resolution_clock::now();
    cout << "Vector (no reserve): " << duration_cast<milliseconds>(end - start).count() << " ms" << endl;
    
    // Test 3: Vector with reserve
    start = high_resolution_clock::now();
    vector<int> v2;
    v2.reserve(1000000);
    for(int i = 0; i < 1000000; i++) {
        v2.push_back(i);
    }
    end = high_resolution_clock::now();
    cout << "Vector (with reserve): " << duration_cast<milliseconds>(end - start).count() << " ms" << endl;
    
    return 0;
}
```

**Typical Results**:
```
Array:                2 ms
Vector (no reserve):  8 ms  (4x slower due to resizing)
Vector (with reserve): 3 ms  (almost as fast as array!)
```

**Key Insight**: Using `reserve()` makes vectors nearly as fast as arrays!

---

## 6. 🔄 Migration: Array → Vector

### Converting Array Code to Vector

**Before (Array)**:
```cpp
int arr[100];
int count = 0;

// Add element
if(count < 100) {
    arr[count] = value;
    count++;
}

// Iterate
for(int i = 0; i < count; i++) {
    cout << arr[i] << " ";
}
```

**After (Vector)**:
```cpp
vector<int> v;
v.reserve(100);  // Optional optimization

// Add element
v.push_back(value);  // No size checking needed!

// Iterate
for(int x : v) {
    cout << x << " ";
}
```

---

## 7. ⚠️ Common Mistakes

### Mistake 1: Using Vector When Array is Better
```cpp
// UNNECESSARY: Size is fixed and known
vector<int> scores = {95, 87, 92, 88, 91};  // Overhead!

// BETTER: Use array
int scores[] = {95, 87, 92, 88, 91};  // No overhead
```

### Mistake 2: Using Array When Vector is Better
```cpp
// DANGEROUS: Unknown number of inputs
int inputs[1000];  // What if more than 1000?
int count = 0;

// SAFER: Use vector
vector<int> inputs;  // Grows automatically
```

### Mistake 3: Not Reserving Vector Size
```cpp
// INEFFICIENT
vector<int> v;
for(int i = 0; i < 100000; i++) {
    v.push_back(i);  // Multiple reallocations!
}

// EFFICIENT
vector<int> v;
v.reserve(100000);  // Allocate once
for(int i = 0; i < 100000; i++) {
    v.push_back(i);  // No reallocations!
}
```

---

## 8. 🎯 Best Practices

### For Arrays:
1. Use for fixed-size data
2. Initialize with zeros: `int arr[100] = {0}`
3. Track size manually
4. Watch bounds carefully
5. Use for performance-critical code

### For Vectors:
1. Use `reserve()` when size is known
2. Pass by reference: `void func(vector<int>& v)`
3. Use `at()` for bounds checking
4. Prefer `push_back()` over `insert()`
5. Use STL algorithms (sort, unique, etc.)
6. Use range-based for loops

---

## 9. 📝 Quick Reference

### Array Syntax
```cpp
// Declaration
int arr[10];
int arr[] = {1, 2, 3};

// Access
arr[0] = 10;

// Size
int size = sizeof(arr) / sizeof(arr[0]);

// Iterate
for(int i = 0; i < size; i++) {
    cout << arr[i] << " ";
}
```

### Vector Syntax
```cpp
// Declaration
vector<int> v;
vector<int> v = {1, 2, 3};

// Access
v[0] = 10;
v.at(0) = 10;  // Safer

// Size
int size = v.size();

// Iterate
for(int x : v) {
    cout << x << " ";
}
```

---

## 10. 🎯 Key Takeaways

1. **Arrays** — Fixed size, faster, less safe
2. **Vectors** — Dynamic size, slightly slower, safer
3. **Use reserve()** — Makes vectors nearly as fast as arrays
4. **Default to vectors** — Unless you have a specific reason for arrays
5. **Know both** — You'll encounter both in real code
6. **Performance difference** — Usually negligible in practice
7. **Safety matters** — Vectors prevent many bugs

---

**Summary**: Use **vectors by default**, use **arrays for optimization**!

[← Back to README](../README.md) | [Next: Two Pointer →](../../05-Two-Pointers-and-Sliding-Window/concepts/01-two-pointers-technique-guide.md)


---

## Supplementary Reference from 01_Arrays_Complete_DSA_Notes.md

# Arrays in C++ — Complete DSA Notes

> Detailed notes based on the uploaded array material, expanded with additional concepts, examples, edge cases, mistakes, patterns, and practice questions.

---

# 1. What is an Array?

## Definition

An **array** is a collection of elements of the **same type** stored in a fixed-size contiguous block of memory.

Example:

```cpp
int arr[5] = {10, 20, 30, 40, 50};
```

Conceptually:

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Array:   [10] [20] [30] [40] [50]
```

The first element is at index `0`.

```text
arr[0] → 10
arr[1] → 20
arr[2] → 30
arr[3] → 40
arr[4] → 50
```

The uploaded notes correctly identify zero-based indexing and show basic input/output, minimum, maximum, searching, reversing, and function-based array operations.

---

# 2. Homogeneous Nature of Arrays

A normal C++ array stores elements of one element type.

```cpp
int arr[4] = {10, 20, 30, 40};
```

All elements are `int`.

Similarly:

```cpp
double prices[3] = {10.5, 20.5, 30.5};
```

All elements are `double`.

```cpp
char letters[3] = {'A', 'B', 'C'};
```

All elements are `char`.

### Important correction

The statement:

> "An array having different types of data is called a heterogeneous array."

is not the normal definition of a built-in C++ array.

A standard C++ array is **homogeneous**.

If you need different types together, consider:

- `struct`
- `class`
- `std::tuple`
- `std::variant`

---

# 3. Why Do We Need Arrays?

Without an array:

```cpp
int marks1 = 80;
int marks2 = 75;
int marks3 = 90;
int marks4 = 65;
int marks5 = 88;
```

With an array:

```cpp
int marks[5] = {80, 75, 90, 65, 88};
```

Now we can process all values using a loop:

```cpp
for (int i = 0; i < 5; i++) {
    cout << marks[i] << " ";
}
```

This is one of the biggest advantages of arrays:

> **They allow many related values to be stored and processed using one name and an index.**

---

# 4. Array Indexing

C++ arrays use **zero-based indexing**.

For:

```cpp
int arr[5];
```

valid indices are:

```text
0
1
2
3
4
```

General rule:

```text
valid index = 0 to n - 1
```

where `n` is the array size.

### Example

```cpp
int arr[5] = {10, 20, 30, 40, 50};

cout << arr[0]; // 10
cout << arr[4]; // 50
```

---

# 5. Why Does Indexing Start at 0?

Arrays are stored contiguously.

If the starting address is represented as `base`, the address of an element can be calculated conceptually as:

```text
address(arr[i]) = base + i × sizeof(element)
```

For example, if an `int` occupies 4 bytes:

```text
arr[0] → base
arr[1] → base + 4
arr[2] → base + 8
arr[3] → base + 12
```

The index represents an **offset from the first element**.

This is one reason zero-based indexing fits naturally with memory addressing.

---

# 6. Array Declaration

### Syntax

```cpp
data_type array_name[size];
```

Example:

```cpp
int arr[5];
```

This creates an array capable of storing 5 integers.

---

# 7. Array Initialization

## Method 1 — Full initialization

```cpp
int arr[5] = {10, 20, 30, 40, 50};
```

## Method 2 — Size inferred

```cpp
int arr[] = {10, 20, 30, 40, 50};
```

C++ determines the size as `5`.

## Method 3 — Partial initialization

```cpp
int arr[5] = {10, 20};
```

The remaining elements are initialized to zero:

```text
10 20 0 0 0
```

---

# 8. Array Size

For a built-in array:

```cpp
int arr[] = {10, 20, 30, 40, 50};
```

you can calculate the number of elements using:

```cpp
int n = sizeof(arr) / sizeof(arr[0]);
```

If `int` is 4 bytes:

```text
sizeof(arr)    = 20
sizeof(arr[0]) = 4

20 / 4 = 5
```

Therefore:

```cpp
n = 5;
```

### Important

This works when `arr` is actually an array in that scope.

It does **not** work the same way after an array has decayed to a pointer when passed to a normal function parameter.

---

# 9. Input into an Array

A common pattern:

```cpp
int n;
cin >> n;

int arr[n];

for (int i = 0; i < n; i++) {
    cin >> arr[i];
}
```

### Important C++ note

`int arr[n];` where `n` is determined at runtime is a **variable-length array (VLA)**. It is not part of standard C++.

Some compilers accept it as an extension, but portable C++ should use:

```cpp
vector<int> arr(n);
```

For beginner DSA on platforms that specifically permit VLAs, you may see the original form, but understand the standard C++ distinction.

---

# 10. Printing an Array

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
```

Example:

```text
10 20 30 40 50
```

---

# 11. Traversal

## Definition

**Array traversal** means visiting each element of an array, usually from the first element to the last.

Example:

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

assuming no additional array is created.

---

# 12. Forward Traversal

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
```

Traversal:

```text
0 → 1 → 2 → 3 → ... → n-1
```

---

# 13. Reverse Traversal

```cpp
for (int i = n - 1; i >= 0; i--) {
    cout << arr[i] << " ";
}
```

Traversal:

```text
n-1 → n-2 → ... → 2 → 1 → 0
```

---

# 14. Accessing an Element

Array access:

```cpp
arr[index]
```

Example:

```cpp
int arr[] = {10, 20, 30};

cout << arr[1];
```

Output:

```text
20
```

Access by index is:

```text
Time = O(1)
```

because the address can be calculated directly.

---

# 15. Updating an Element

```cpp
int arr[] = {10, 20, 30};

arr[1] = 100;
```

Array becomes:

```text
10 100 30
```

Complexity:

```text
O(1)
```

---

# 16. Searching in an Array

Searching means finding whether a target value exists and, often, finding its index.

There are two major approaches:

```text
Linear Search
Binary Search
```

---

# 17. Linear Search

## Definition

**Linear search** checks elements sequentially until the target is found or the array ends.

Example:

```cpp
int linearSearch(int arr[], int n, int target) {

    for (int i = 0; i < n; i++) {

        if (arr[i] == target) {
            return i;
        }
    }

    return -1;
}
```

Example:

```text
Array:   10  20  30  40  50
Index:    0   1   2   3   4

Target = 40
```

Checks:

```text
10 → no
20 → no
30 → no
40 → yes
```

Returns:

```text
3
```

---

# 18. Why Return `-1`?

Array indices are normally:

```text
0 to n-1
```

So `-1` cannot be a valid index.

Therefore it is commonly used as a sentinel value meaning:

> Target was not found.

Example:

```cpp
int index = linearSearch(arr, n, target);

if (index == -1) {
    cout << "Not found";
}
else {
    cout << "Found at index " << index;
}
```

---

# 19. Linear Search Complexity

### Best case

Target is at index `0`.

```text
O(1)
```

### Worst case

Target is at the end or absent.

```text
O(n)
```

### Average case

```text
O(n)
```

### Space

```text
O(1)
```

---

# 20. Binary Search

## Definition

**Binary search** repeatedly divides the search range into two halves.

### Critical requirement

The array must be **sorted** according to the ordering being searched.

Example:

```text
1 3 5 7 9 11 13
```

Search for:

```text
9
```

Instead of checking every element, binary search checks the middle and eliminates half of the remaining search space.

---

# 21. Binary Search Dry Run

Array:

```text
1 3 5 7 9 11 13
```

Target:

```text
9
```

Initial:

```text
low = 0
high = 6
mid = 3
```

```text
arr[mid] = 7
```

Since:

```text
9 > 7
```

ignore the left half.

Now:

```text
low = 4
high = 6
```

Middle:

```text
arr[5] = 11
```

Since:

```text
9 < 11
```

search left.

Now:

```text
low = 4
high = 4
```

`arr[4] = 9`

Found.

---

# 22. Binary Search Complexity

```text
Best case  = O(1)
Worst case = O(log n)
Average    = O(log n)
Space      = O(1) for iterative implementation
```

---

# 23. Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|---|---|---|
| Requires sorted array? | No | Yes |
| Approach | Sequential | Divide and conquer |
| Worst-case | O(n) | O(log n) |
| Easy to implement | Yes | Moderate |
| Works on unsorted array | Yes | No |
| Good for small arrays | Yes | Yes |
| Good for large sorted arrays | Sometimes | Excellent |

---

# 24. Minimum Element

A common array problem is finding the smallest element.

### Approach

Start with the first element:

```cpp
int smallest = arr[0];
```

Then compare every element:

```cpp
for (int i = 1; i < n; i++) {

    if (arr[i] < smallest) {
        smallest = arr[i];
    }
}
```

### Why start with `arr[0]`?

Because it guarantees that the initial value actually belongs to the array.

---

# 25. Using `INT_MAX`

Another approach:

```cpp
int smallest = INT_MAX;

for (int i = 0; i < n; i++) {
    if (arr[i] < smallest) {
        smallest = arr[i];
    }
}
```

`INT_MAX` is larger than every representable `int` value.

Therefore the first array element will replace it.

### Header

Use:

```cpp
#include <climits>
```

for `INT_MAX` and `INT_MIN`.

### Preferred beginner approach

```cpp
int smallest = arr[0];
```

is often simpler and also handles the important idea that the array must be non-empty.

---

# 26. Maximum Element

```cpp
int largest = arr[0];

for (int i = 1; i < n; i++) {

    if (arr[i] > largest) {
        largest = arr[i];
    }
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

---

# 27. `INT_MIN` and `INT_MAX`

You can use:

```cpp
INT_MIN
```

as an initial value for maximum.

And:

```cpp
INT_MAX
```

as an initial value for minimum.

Example:

```cpp
int largest = INT_MIN;
int smallest = INT_MAX;
```

But for a non-empty array, this is often simpler:

```cpp
int largest = arr[0];
int smallest = arr[0];
```

---

# 28. Sum of Array Elements

### Problem

Find the sum of all elements.

```cpp
int sum = 0;

for (int i = 0; i < n; i++) {
    sum += arr[i];
}

cout << sum;
```

Example:

```text
Array: 1 2 3 4 5

sum = 1 + 2 + 3 + 4 + 5
    = 15
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 29. Product of Array Elements

```cpp
long long product = 1;

for (int i = 0; i < n; i++) {
    product *= arr[i];
}
```

### Why `1`?

Because `1` is the multiplicative identity:

```text
1 × x = x
```

Starting with `0` would make the entire product zero.

### Important

Use a sufficiently large integer type if the product can exceed `int`.

Even `long long` can overflow for sufficiently large products.

---

# 30. Count Even and Odd Elements

```cpp
int even = 0;
int odd = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] % 2 == 0)
        even++;
    else
        odd++;
}
```

---

# 31. Count Positive, Negative, and Zero

```cpp
int positive = 0;
int negative = 0;
int zero = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] > 0)
        positive++;
    else if (arr[i] < 0)
        negative++;
    else
        zero++;
}
```

---

# 32. Reverse an Array

## Definition

Reversing an array means changing:

```text
1 2 3 4 5
```

into:

```text
5 4 3 2 1
```

The uploaded material uses the correct **two-pointer/in-place** approach.

---

# 33. Two-Pointer Reverse

```cpp
void reverseArr(int arr[], int n) {

    int start = 0;
    int end = n - 1;

    while (start < end) {

        swap(arr[start], arr[end]);

        start++;
        end--;
    }
}
```

### Dry Run

Array:

```text
1 2 3 4 5
```

Initial:

```text
start = 0
end   = 4
```

Swap:

```text
5 2 3 4 1
```

Move:

```text
start = 1
end = 3
```

Swap:

```text
5 4 3 2 1
```

Move:

```text
start = 2
end = 2
```

Stop.

---

# 34. Why `start < end`?

We only need to swap pairs until the pointers meet.

If:

```text
start == end
```

there is a single middle element, which does not need swapping.

Therefore:

```cpp
while (start < end)
```

is the correct condition.

---

# 35. Reverse Complexity

```text
Time  = O(n)
Space = O(1)
```

It is an **in-place** reversal because no second array is created.

---

# 36. Swapping Maximum and Minimum

### Problem

Given:

```text
5 2 9 1 7
```

minimum:

```text
1
```

maximum:

```text
9
```

After swapping their positions:

```text
5 2 1 9 7
```

### Approach

1. Find minimum value and its index.
2. Find maximum value and its index.
3. Swap the two positions.

```cpp
int minIndex = 0;
int maxIndex = 0;

for (int i = 1; i < n; i++) {

    if (arr[i] < arr[minIndex])
        minIndex = i;

    if (arr[i] > arr[maxIndex])
        maxIndex = i;
}

swap(arr[minIndex], arr[maxIndex]);
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 37. Important Question: What If Minimum = Maximum?

Example:

```text
5 5 5 5
```

Both minimum and maximum are `5`.

Swapping their positions changes nothing.

Result:

```text
5 5 5 5
```

This is an important edge case.

---

# 38. Unique Elements

## What Does "Unique" Mean?

There are two common interpretations.

### Interpretation 1

Print elements that appear **exactly once**.

Example:

```text
Input:
1 2 2 3 4 4 5

Output:
1 3 5
```

### Interpretation 2

Print each distinct value only once.

Example:

```text
Input:
1 2 2 3 4 4 5

Output:
1 2 3 4 5
```

These are **different problems**.

Always determine which meaning the question intends.

---

# 39. Print Elements Appearing Exactly Once

Simple approach using nested loops:

```cpp
for (int i = 0; i < n; i++) {

    int count = 0;

    for (int j = 0; j < n; j++) {

        if (arr[i] == arr[j]) {
            count++;
        }
    }

    if (count == 1) {
        cout << arr[i] << " ";
    }
}
```

Complexity:

```text
Time  = O(n²)
Space = O(1)
```

---

# 40. Distinct Elements Using `set`

If you want each value only once:

```cpp
set<int> s;

for (int i = 0; i < n; i++) {
    s.insert(arr[i]);
}
```

Then:

```cpp
for (int x : s) {
    cout << x << " ";
}
```

Note:

> `set` stores unique values and keeps them ordered.

If you need insertion-order-like behavior or faster average lookup, other approaches may be appropriate.

---

# 41. Frequency of an Element

### Problem

Count how many times `target` occurs.

```cpp
int count = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] == target) {
        count++;
    }
}
```

Example:

```text
Array:
1 2 2 3 2 4

target = 2

count = 3
```

---

# 42. First Occurrence

The first occurrence is the smallest index at which the target appears.

```cpp
int index = -1;

for (int i = 0; i < n; i++) {

    if (arr[i] == target) {
        index = i;
        break;
    }
}
```

---

# 43. Last Occurrence

```cpp
int index = -1;

for (int i = 0; i < n; i++) {

    if (arr[i] == target) {
        index = i;
    }
}
```

Example:

```text
Array: 1 2 3 2 4 2

target = 2
```

Last occurrence:

```text
index = 5
```

---

# 44. Check if Array is Sorted

Suppose:

```text
1 2 3 4 5
```

is sorted in non-decreasing order.

We check adjacent elements.

```cpp
bool sorted = true;

for (int i = 1; i < n; i++) {

    if (arr[i] < arr[i - 1]) {
        sorted = false;
        break;
    }
}
```

If `sorted` remains true, the array is sorted.

### Complexity

```text
O(n)
```

---

# 45. Ascending vs Strictly Increasing

These are different.

### Non-decreasing

```text
1 2 2 3 4
```

Duplicates allowed.

Condition:

```cpp
arr[i] >= arr[i - 1]
```

### Strictly increasing

```text
1 2 3 4 5
```

Duplicates are not allowed.

Condition:

```cpp
arr[i] > arr[i - 1]
```

---

# 46. Copy an Array

```cpp
for (int i = 0; i < n; i++) {
    copy[i] = arr[i];
}
```

Complexity:

```text
Time  = O(n)
Space = O(n)
```

because a second array is created.

---

# 47. In-Place vs Extra-Space Operations

### In-place

Modifies the original array.

Example:

```cpp
swap(arr[i], arr[j]);
```

Extra space:

```text
O(1)
```

### Extra array

Creates another array.

```cpp
int copy[n];
```

Extra space:

```text
O(n)
```

This distinction becomes very important in DSA interviews.

---

# 48. Passing Arrays to Functions

Example:

```cpp
void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
```

Call:

```cpp
int arr[] = {1, 2, 3, 4, 5};

printArray(arr, 5);
```

### Important correction

It is misleading to simply say:

> "An array is passed by reference."

For a built-in array parameter written as:

```cpp
void func(int arr[], int n)
```

the parameter is adjusted to a pointer type.

Conceptually:

```cpp
void func(int* arr, int n)
```

So the function receives access to the original array elements.

Therefore:

```cpp
arr[i] = 100;
```

inside the function changes the original array.

---

# 49. Modifying an Array in a Function

```cpp
void changeArr(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        arr[i] *= 2;
    }
}
```

Main:

```cpp
int arr[] = {1, 2, 3, 4, 5};

changeArr(arr, 5);
```

Array becomes:

```text
2 4 6 8 10
```

---

# 50. Why Does the Array Change?

Because the function receives access to the same underlying array storage.

Conceptually:

```text
main array
   ↓
[1][2][3][4][5]
   ↑
   |
function accesses same elements
```

So:

```cpp
arr[i] *= 2;
```

modifies the original elements.

---

# 51. `const` Array Parameter

If a function should only read the array and must not modify it:

```cpp
void printArray(const int arr[], int n) {

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
```

This gives the function a read-only view of the elements.

This is a very good habit for functions that do not need to modify the array.

---

# 52. Array of Characters

An array can store characters:

```cpp
char letters[] = {'A', 'B', 'C'};
```

It can also represent a C-style string:

```cpp
char name[] = "Ravi";
```

The second form contains an additional null terminator:

```text
R a v i \0
```

---

# 53. Two-Dimensional Array

A two-dimensional array is an array arranged in rows and columns.

```cpp
int matrix[3][4];
```

This means:

```text
3 rows
4 columns
```

Conceptually:

```text
[ ][ ][ ][ ]
[ ][ ][ ][ ]
[ ][ ][ ][ ]
```

Access:

```cpp
matrix[row][column]
```

Example:

```cpp
matrix[1][2]
```

means:

```text
row = 1
column = 2
```

---

# 54. Traversing a 2D Array

```cpp
for (int i = 0; i < rows; i++) {

    for (int j = 0; j < cols; j++) {

        cout << matrix[i][j] << " ";
    }

    cout << "\n";
}
```

Complexity:

```text
O(rows × cols)
```

---

# 55. Row Sum

For a matrix:

```cpp
for (int i = 0; i < rows; i++) {

    int sum = 0;

    for (int j = 0; j < cols; j++) {
        sum += matrix[i][j];
    }

    cout << "Row " << i << ": " << sum << "\n";
}
```

---

# 56. Column Sum

```cpp
for (int j = 0; j < cols; j++) {

    int sum = 0;

    for (int i = 0; i < rows; i++) {
        sum += matrix[i][j];
    }

    cout << "Column " << j << ": " << sum << "\n";
}
```

---

# 57. Primary Diagonal

For a square matrix:

```text
1 2 3
4 5 6
7 8 9
```

Primary diagonal:

```text
1
  5
    9
```

Condition:

```cpp
i == j
```

Example:

```cpp
for (int i = 0; i < n; i++) {
    cout << matrix[i][i] << " ";
}
```

Output:

```text
1 5 9
```

---

# 58. Secondary Diagonal

For:

```text
1 2 3
4 5 6
7 8 9
```

Secondary diagonal:

```text
    3
  5
7
```

Condition:

```text
i + j = n - 1
```

Code:

```cpp
for (int i = 0; i < n; i++) {
    cout << matrix[i][n - 1 - i] << " ";
}
```

---

# 59. Array Rotation

Rotation is different from reversal.

### Left rotation by 1

```text
1 2 3 4 5
```

becomes:

```text
2 3 4 5 1
```

### Right rotation by 1

```text
1 2 3 4 5
```

becomes:

```text
5 1 2 3 4
```

Rotation is a very common array interview problem.

---

# 60. Left Rotation by One

Simple approach:

```cpp
int first = arr[0];

for (int i = 0; i < n - 1; i++) {
    arr[i] = arr[i + 1];
}

arr[n - 1] = first;
```

Example:

```text
Before:
1 2 3 4 5

After:
2 3 4 5 1
```

---

# 61. Right Rotation by One

```cpp
int last = arr[n - 1];

for (int i = n - 1; i > 0; i--) {
    arr[i] = arr[i - 1];
}

arr[0] = last;
```

Example:

```text
Before:
1 2 3 4 5

After:
5 1 2 3 4
```

---

# 62. Move Zeros to the End

### Problem

Input:

```text
0 1 0 3 12
```

Output:

```text
1 3 12 0 0
```

A common two-pointer approach:

```cpp
int j = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] != 0) {
        swap(arr[i], arr[j]);
        j++;
    }
}
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 63. Find Second Largest Element

Do not simply sort the array unless sorting is actually allowed.

A one-pass approach:

```cpp
long long largest = LLONG_MIN;
long long secondLargest = LLONG_MIN;

for (int i = 0; i < n; i++) {

    if (arr[i] > largest) {
        secondLargest = largest;
        largest = arr[i];
    }
    else if (arr[i] > secondLargest && arr[i] != largest) {
        secondLargest = arr[i];
    }
}
```

### Important

Clarify whether "second largest" means:

- second largest **distinct** value
- second element after sorting, where duplicates may count

These are different problems.

---

# 64. Find Missing Number

Suppose the array contains numbers from:

```text
0 to n
```

with exactly one missing.

Example:

```text
0 1 3 4
```

Missing:

```text
2
```

One mathematical approach:

```cpp
long long expected = 1LL * n * (n + 1) / 2;

long long actual = 0;

for (int x : arr) {
    actual += x;
}

cout << expected - actual;
```

---

# 65. Duplicate Element

Example:

```text
1 3 4 2 2
```

The duplicate is:

```text
2
```

There are multiple approaches depending on constraints:

- nested loops
- sorting
- frequency array
- `set` / `unordered_set`
- Floyd's cycle detection for special problem constraints

Do not automatically choose one method without checking the constraints.

---

# 66. Intersection of Two Arrays

The uploaded file includes this as a practice problem.

Example:

```text
A = 1 2 3 4
B = 3 4 5 6
```

Intersection:

```text
3 4
```

### Important ambiguity

"Intersection" may mean:

1. distinct common values
2. common values respecting duplicates/multiset frequency

Example:

```text
A = 1 2 2 3
B = 2 2 4
```

Distinct intersection:

```text
2
```

Multiset intersection:

```text
2 2
```

Always clarify the intended definition.

---

# 67. Brute-Force Intersection

For distinct values, a simple approach can use nested loops plus duplicate checking.

Basic complexity can be:

```text
O(n × m)
```

where:

- `n` = size of first array
- `m` = size of second array

For larger constraints, hashing or sorting-based solutions are usually better.

---

# 68. Prefix Sum

## Definition

A **prefix sum array** stores cumulative sums.

For:

```text
arr = [2, 4, 1, 3, 5]
```

prefix sums:

```text
[2, 6, 7, 10, 15]
```

Because:

```text
2
2+4 = 6
2+4+1 = 7
2+4+1+3 = 10
2+4+1+3+5 = 15
```

---

# 69. Why Prefix Sum Is Important

Suppose we need many range-sum queries.

For example:

```text
sum from index 1 to 3
```

Without prefix sums, repeatedly summing can take:

```text
O(n)
```

With prefix sums, each range sum can be answered in:

```text
O(1)
```

after:

```text
O(n)
```

preprocessing.

---

# 70. Range Sum Formula

If:

```text
prefix[i] = arr[0] + ... + arr[i]
```

then:

```text
sum(l, r) = prefix[r] - prefix[l - 1]
```

when `l > 0`.

For `l = 0`:

```text
sum(0, r) = prefix[r]
```

A cleaner implementation often uses a prefix array of size `n + 1`:

```cpp
vector<long long> prefix(n + 1, 0);

for (int i = 0; i < n; i++) {
    prefix[i + 1] = prefix[i] + arr[i];
}
```

Then:

```cpp
sum(l, r) = prefix[r + 1] - prefix[l];
```

This avoids a special `l == 0` case.

---

# 71. Kadane's Algorithm — Maximum Subarray Sum

### Problem

Find the maximum sum of a contiguous subarray.

Example:

```text
[-2,1,-3,4,-1,2,1,-5,4]
```

Maximum-sum subarray:

```text
[4,-1,2,1]
```

Sum:

```text
6
```

A common implementation:

```cpp
long long current = arr[0];
long long best = arr[0];

for (int i = 1; i < n; i++) {

    current = max(1LL * arr[i], current + arr[i]);

    best = max(best, current);
}
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

This is one of the most important array algorithms for interviews.

---

# 72. Subarray vs Subsequence vs Subset

These are commonly confused.

## Subarray

Elements must be **contiguous**.

```text
[2, 3, 4]
```

from:

```text
1 2 3 4 5
```

is a subarray.

## Subsequence

Order is preserved, but elements do not need to be contiguous.

```text
1 3 5
```

is a subsequence of:

```text
1 2 3 4 5
```

## Subset

Order generally does not matter.

For:

```text
{1, 2, 3}
```

possible subsets include:

```text
{}
{1}
{2}
{1,3}
{1,2,3}
```

This distinction becomes very important in DSA.

---

# 73. Time Complexity of Common Array Operations

| Operation | Complexity |
|---|---:|
| Access by index | O(1) |
| Update by index | O(1) |
| Traverse | O(n) |
| Linear search | O(n) |
| Binary search | O(log n), sorted data required |
| Find min/max | O(n) |
| Reverse | O(n) |
| Copy | O(n) |
| Insert at end of fixed array if free position exists | O(1) |
| Insert at beginning | O(n) |
| Insert in middle | O(n) |
| Delete from beginning | O(n) |
| Delete from middle | O(n) |

---

# 74. Why Array Access Is O(1)

Suppose:

```text
arr = [10,20,30,40,50]
```

To access:

```cpp
arr[3]
```

we don't need to inspect:

```text
arr[0]
arr[1]
arr[2]
```

The address is calculated directly from the base address and index.

Therefore:

```text
arr[i] → O(1)
```

This is one of the biggest strengths of arrays.

---

# 75. Why Insertion at the Beginning Is O(n)

Suppose:

```text
10 20 30 40
```

Insert `5` at index `0`.

We must shift:

```text
10 → 1
20 → 2
30 → 3
40 → 4
```

Result:

```text
5 10 20 30 40
```

Potentially many elements must move.

Therefore:

```text
O(n)
```

---

# 76. Array vs Linked List

| Feature | Array | Linked List |
|---|---|---|
| Memory layout | Contiguous | Nodes can be non-contiguous |
| Random access | O(1) | O(n) |
| Search | O(n) generally | O(n) |
| Insert beginning | O(n) | O(1) with head |
| Delete beginning | O(n) | O(1) with head |
| Cache locality | Usually good | Usually weaker |
| Fixed built-in array size | Yes | Dynamic node structure |
| Extra pointer memory | No | Yes |

This comparison becomes important when you study linked lists.

---

# 77. Array vs `vector`

A built-in array:

```cpp
int arr[5];
```

has a fixed size.

A `vector`:

```cpp
vector<int> arr;
```

is a dynamic array abstraction.

Example:

```cpp
vector<int> arr = {1, 2, 3};

arr.push_back(4);
```

Now:

```text
1 2 3 4
```

For modern C++ DSA, `vector` is usually preferred when the size is determined at runtime.

---

# 78. Common Array Mistakes

## Mistake 1 — Out-of-bounds access

For:

```cpp
int arr[5];
```

valid indices:

```text
0,1,2,3,4
```

This is invalid:

```cpp
arr[5]
```

---

## Mistake 2 — Loop boundary error

Wrong:

```cpp
for (int i = 0; i <= n; i++)
```

Correct:

```cpp
for (int i = 0; i < n; i++)
```

Because the last valid index is:

```text
n - 1
```

---

## Mistake 3 — Starting maximum at zero

This fails for an all-negative array.

Example:

```text
-5 -10 -2
```

If:

```cpp
int largest = 0;
```

you may incorrectly get:

```text
0
```

which isn't even in the array.

Prefer:

```cpp
int largest = arr[0];
```

for a non-empty array.

---

## Mistake 4 — Starting product at zero

Wrong:

```cpp
int product = 0;
```

Then:

```text
0 × anything = 0
```

Correct:

```cpp
long long product = 1;
```

---

## Mistake 5 — Binary search on an unsorted array

Binary search requires appropriate sorted ordering.

Do not apply binary search blindly to:

```text
8 2 10 1 5
```

---

## Mistake 6 — Forgetting empty-array cases

Code like:

```cpp
int smallest = arr[0];
```

requires at least one element.

If `n == 0`, there is no `arr[0]`.

Always understand the problem's constraints.

---

## Mistake 7 — Integer overflow

This can overflow:

```cpp
int sum = 0;
```

if the values and `n` are large.

Sometimes use:

```cpp
long long sum = 0;
```

depending on constraints.

---

# 79. Edge Cases You Must Check

Whenever solving an array problem, ask:

### Case 1 — Empty array

```text
[]
```

Is it allowed?

### Case 2 — One element

```text
[5]
```

### Case 3 — All equal

```text
[7,7,7,7]
```

### Case 4 — All negative

```text
[-5,-2,-10]
```

### Case 5 — All positive

```text
[1,5,9]
```

### Case 6 — Duplicate values

```text
[1,2,2,3]
```

### Case 7 — Already sorted

```text
[1,2,3,4,5]
```

### Case 8 — Reverse sorted

```text
[5,4,3,2,1]
```

### Case 9 — Target absent

```text
target = 100
```

### Case 10 — Target occurs multiple times

```text
[2,5,2,7,2]
```

These cases reveal many bugs.

---

# 80. Array Problem-Solving Checklist

Before coding, ask:

```text
1. Is the array sorted?
2. Are duplicates allowed?
3. Do I need the value or index?
4. Do I need first occurrence or last occurrence?
5. Is the answer based on contiguous elements?
6. Is extra space allowed?
7. Can I use hashing?
8. Can I use two pointers?
9. Can I use prefix sums?
10. Can I use binary search?
11. Are negative numbers possible?
12. Can values overflow int?
13. Can n be zero?
14. Is the result required modulo something?
15. What is the expected complexity?
```

---

# 81. Important Array Patterns

You should eventually recognize these patterns:

## Pattern 1 — Simple Traversal

```cpp
for (int i = 0; i < n; i++)
```

Used for:

- sum
- count
- min/max
- search
- frequency

---

## Pattern 2 — Two Pointers

```cpp
int left = 0;
int right = n - 1;
```

Used for:

- reverse
- pair problems
- sorted-array problems
- partitioning
- removing duplicates

---

## Pattern 3 — Sliding Window

Used for:

- subarray problems
- fixed-size windows
- longest/shortest valid ranges

---

## Pattern 4 — Prefix Sum

Used for:

- repeated range-sum queries
- subarray sum calculations
- cumulative information

---

## Pattern 5 — Hashing

Used for:

- frequency
- duplicates
- two-sum type problems
- distinct elements

---

## Pattern 6 — Binary Search

Used when:

- search space is ordered
- answer has a monotonic property
- sorted data is available
- "binary search on answer" is applicable

---

# 82. Practice Questions — Beginner

## Q1. Print all array elements

Input:

```text
5
10 20 30 40 50
```

Output:

```text
10 20 30 40 50
```

---

## Q2. Find the sum

Input:

```text
5
1 2 3 4 5
```

Output:

```text
15
```

---

## Q3. Find minimum

Input:

```text
5
8 3 10 2 6
```

Output:

```text
2
```

---

## Q4. Find maximum

Input:

```text
5
8 3 10 2 6
```

Output:

```text
10
```

---

## Q5. Count even numbers

Input:

```text
6
1 2 4 7 8 9
```

Output:

```text
3
```

---

## Q6. Count positive, negative, and zero

Input:

```text
7
-2 0 5 -1 0 8 3
```

Expected:

```text
Positive = 3
Negative = 2
Zero = 2
```

---

# 83. Practice Questions — Searching

## Q7. Linear search

Find the index of `30`:

```text
10 20 30 40 50
```

Expected:

```text
2
```

---

## Q8. Search for a missing value

```text
Array = 10 20 30 40
Target = 50
```

Expected:

```text
-1
```

---

## Q9. First occurrence

```text
Array = 2 5 2 7 2
Target = 2
```

Expected:

```text
0
```

---

## Q10. Last occurrence

Same array:

```text
2 5 2 7 2
```

Expected:

```text
4
```

---

## Q11. Count occurrences

```text
Array = 1 2 2 3 2 4
Target = 2
```

Expected:

```text
3
```

---

# 84. Practice Questions — Reverse & Manipulation

## Q12. Reverse an array

Input:

```text
1 2 3 4 5
```

Output:

```text
5 4 3 2 1
```

Constraint:

> Do it in-place.

---

## Q13. Swap minimum and maximum

Input:

```text
5 2 9 1 7
```

Output:

```text
5 2 1 9 7
```

---

## Q14. Left rotate by one

Input:

```text
1 2 3 4 5
```

Output:

```text
2 3 4 5 1
```

---

## Q15. Right rotate by one

Input:

```text
1 2 3 4 5
```

Output:

```text
5 1 2 3 4
```

---

# 85. Practice Questions — Duplicates & Uniqueness

## Q16. Print elements occurring exactly once

Input:

```text
1 2 2 3 4 4 5
```

Output:

```text
1 3 5
```

---

## Q17. Print each distinct value once

Input:

```text
1 2 2 3 4 4 5
```

Output:

```text
1 2 3 4 5
```

---

## Q18. Find duplicate values

Input:

```text
1 2 3 2 4 1
```

Expected duplicate values:

```text
1 2
```

---

# 86. Practice Questions — Sorted Arrays

## Q19. Check whether array is sorted

Input:

```text
1 2 3 4 5
```

Output:

```text
Sorted
```

---

## Q20. Check non-decreasing order

Input:

```text
1 2 2 3 4
```

Output:

```text
Sorted
```

---

## Q21. Check strictly increasing order

Input:

```text
1 2 2 3
```

Output:

```text
Not strictly increasing
```

---

# 87. Practice Questions — Intermediate

## Q22. Find second largest distinct element

Input:

```text
10 5 20 8 20
```

Expected:

```text
10
```

---

## Q23. Move all zeros to the end

Input:

```text
0 1 0 3 12
```

Expected:

```text
1 3 12 0 0
```

Try to solve in:

```text
O(n) time
O(1) extra space
```

---

## Q24. Find missing number

Numbers are from `0` to `n`.

Input:

```text
0 1 3 4
```

Expected:

```text
2
```

---

## Q25. Find intersection

```text
A = 1 2 3 4
B = 3 4 5 6
```

Expected:

```text
3 4
```

---

## Q26. Find union of two arrays

```text
A = 1 2 3
B = 2 3 4
```

Distinct union:

```text
1 2 3 4
```

---

# 88. Practice Questions — Prefix Sum

## Q27. Build prefix sum

Input:

```text
2 4 1 3 5
```

Expected:

```text
2 6 7 10 15
```

---

## Q28. Range sum

Array:

```text
2 4 1 3 5
```

Find sum from index `1` to `3`.

Calculation:

```text
4 + 1 + 3 = 8
```

Expected:

```text
8
```

---

# 89. Practice Questions — Two Pointers

## Q29. Reverse in-place

Constraint:

```text
Do not create another array.
```

---

## Q30. Two Sum in Sorted Array

Given:

```text
1 2 4 6 8 9
```

Target:

```text
10
```

Find two elements whose sum is `10`.

Expected pair:

```text
2 + 8
```

A two-pointer approach can solve this in:

```text
O(n)
```

because the array is sorted.

---

# 90. Practice Questions — Subarrays

## Q31. Maximum subarray sum

Input:

```text
-2 1 -3 4 -1 2 1 -5 4
```

Expected:

```text
6
```

---

## Q32. Print all subarrays

Input:

```text
1 2 3
```

Subarrays:

```text
[1]
[1,2]
[1,2,3]
[2]
[2,3]
[3]
```

Number of non-empty subarrays:

```text
n(n+1)/2
```

For `n = 3`:

```text
3 × 4 / 2 = 6
```

---

# 91. Practice Questions — 2D Arrays

## Q33. Print matrix

Input:

```text
1 2 3
4 5 6
7 8 9
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

---

## Q34. Row sums

For:

```text
1 2 3
4 5 6
7 8 9
```

Expected:

```text
6
15
24
```

---

## Q35. Column sums

Expected:

```text
12
15
18
```

---

## Q36. Primary diagonal

Expected:

```text
1 5 9
```

---

## Q37. Secondary diagonal

Expected:

```text
3 5 7
```

---

# 92. Interview-Level Questions

### Q38. Why is array access O(1)?

Explain using:

```text
base address + index × element size
```

---

### Q39. Why does array indexing start at zero?

Explain the index as an offset from the first element.

---

### Q40. Why is insertion at the beginning O(n)?

Explain element shifting.

---

### Q41. Why is binary search O(log n)?

Explain how the search space becomes approximately:

```text
n
n/2
n/4
n/8
...
1
```

---

### Q42. What is the difference between an array and a vector?

Discuss:

- size
- memory
- resizing
- insertion
- C++ usage

---

### Q43. What is array decay?

Explain why:

```cpp
void func(int arr[])
```

behaves like:

```cpp
void func(int* arr)
```

for a function parameter.

---

### Q44. Why can't a function automatically know the length of a raw array parameter?

Because the array parameter is adjusted to a pointer, so the size information is not carried with that parameter.

That's why we commonly pass:

```cpp
func(arr, n);
```

---

### Q45. What happens if we access `arr[n]`?

For an array with `n` elements, `arr[n]` is outside the valid index range.

Accessing it results in **undefined behavior**.

---

# 93. Array Problem Recognition Guide

When you see:

### "Find maximum/minimum"

Think:

```text
single traversal
```

### "Find whether target exists"

Think:

```text
linear search
```

### "Sorted array + search"

Think:

```text
binary search
```

### "Reverse array"

Think:

```text
two pointers
```

### "Pair sum in sorted array"

Think:

```text
two pointers
```

### "Repeated range sums"

Think:

```text
prefix sum
```

### "Frequency / duplicates"

Think:

```text
hashing / frequency array / set
```

### "Contiguous segment"

Think:

```text
subarray
sliding window
prefix sum
Kadane
```

### "Rotate"

Think:

```text
shifting
or
reversal algorithm
```

---

# 94. Most Important Array Concepts to Master

Before moving to advanced DSA, make sure you understand:

```text
1. Array definition
2. Homogeneous storage
3. Contiguous memory
4. Zero-based indexing
5. Declaration
6. Initialization
7. Traversal
8. Access
9. Update
10. Searching
11. Linear search
12. Binary search
13. Minimum
14. Maximum
15. Sum
16. Product
17. Frequency
18. Reverse
19. Two pointers
20. In-place operations
21. Passing arrays to functions
22. const array parameters
23. 2D arrays
24. Row/column traversal
25. Diagonals
26. Rotation
27. Duplicates
28. Unique elements
29. Prefix sums
30. Subarrays
31. Kadane's algorithm
32. Array complexity
33. Edge cases
34. Overflow
35. Array vs vector
36. Array vs linked list
```

---

# 95. Final Array Cheat Sheet

```text
Array
│
├── Same element type
├── Contiguous storage
├── Zero-based indexing
├── Fixed size for built-in array
│
├── Access → O(1)
├── Update → O(1)
├── Traverse → O(n)
├── Search → O(n)
├── Binary Search → O(log n)
├── Reverse → O(n)
├── Min/Max → O(n)
│
├── Patterns
│   ├── Traversal
│   ├── Two pointers
│   ├── Sliding window
│   ├── Prefix sum
│   ├── Hashing
│   └── Binary search
│
└── Important problems
    ├── Sum
    ├── Min/Max
    ├── Search
    ├── Reverse
    ├── Rotate
    ├── Duplicates
    ├── Unique elements
    ├── Intersection
    ├── Missing number
    ├── Second largest
    ├── Move zeros
    ├── Two Sum
    ├── Prefix Sum
    └── Maximum Subarray
```

---

# 96. Recommended Learning Order

Study arrays in this order:

```text
1. What is an Array?
        ↓
2. Indexing & Memory
        ↓
3. Declaration & Initialization
        ↓
4. Input / Output
        ↓
5. Traversal
        ↓
6. Min / Max
        ↓
7. Sum / Product
        ↓
8. Linear Search
        ↓
9. Reverse
        ↓
10. Frequency / Duplicates
        ↓
11. Sorted Array
        ↓
12. Binary Search
        ↓
13. Two Pointers
        ↓
14. Rotation
        ↓
15. Prefix Sum
        ↓
16. Sliding Window
        ↓
17. Kadane's Algorithm
        ↓
18. 2D Arrays
        ↓
19. Array Interview Problems
        ↓
20. LeetCode / Coding Problems
```

> **Goal:** Do not memorize solutions. Learn to identify the pattern behind the problem. Once you can recognize whether a problem requires traversal, two pointers, hashing, prefix sum, sliding window, or binary search, solving array problems becomes much easier.


---

## Supplementary Reference from 02_Cpp_Vectors_and_Advanced_Array_DSA_Notes.md

# C++ Vectors & Advanced Array Patterns — DSA Notes

> These notes continue the Array chapter and cover **`vector`, vector functions, size vs capacity, dynamic growth, Kadane's Algorithm, Pair Sum, Two Pointers, Hashing, Majority Element, and Moore's Voting Algorithm** with detailed explanations, dry runs, complexity, mistakes, and practice questions.

---

# 1. Vector in C++

## Definition

A **vector** is a dynamic sequence container provided by the C++ Standard Library.

Unlike a built-in array whose size is fixed after creation, a vector can automatically grow or shrink as elements are added or removed.

```cpp
#include <vector>
using namespace std;

vector<int> nums;
```

A vector:

- stores elements of the same type
- supports index-based access
- manages its own memory
- can dynamically change its size
- provides many built-in functions
- is implemented as a class template

---

# 2. Why Do We Need Vectors?

Consider a built-in array:

```cpp
int arr[5];
```

Its capacity is fixed at 5 elements.

You cannot simply do:

```cpp
arr.push_back(10);
```

because a built-in array does not have `push_back()`.

A vector solves this:

```cpp
vector<int> arr;

arr.push_back(10);
arr.push_back(20);
arr.push_back(30);
```

Now:

```text
10 20 30
```

The vector automatically manages the storage required for its elements.

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

# 19. `front()`

`front()` returns a reference to the first element.

```cpp
vector<int> v = {10, 20, 30};

cout << v.front();
```

Output:

```text
10
```

---

# 20. `back()`

`back()` returns a reference to the last element.

```cpp
cout << v.back();
```

Output:

```text
30
```

---

# 21. Important Safety Rule for `front()` and `back()`

Do not call:

```cpp
v.front();
v.back();
```

on an empty vector.

Example:

```cpp
vector<int> v;

cout << v.front(); // invalid
```

Always understand whether the vector can be empty.

---

# 22. Accessing Elements with `[]`

You can access vector elements using the same index syntax as arrays.

```cpp
vector<int> v = {10, 20, 30};

cout << v[1];
```

Output:

```text
20
```

Complexity:

```text
O(1)
```

---

# 23. `at()`

`at()` accesses an element using an index.

```cpp
cout << v.at(1);
```

For a valid index:

```text
0 <= index < size
```

the element is returned.

Unlike `operator[]`, `at()` performs bounds checking and throws `std::out_of_range` when the index is invalid.

Example:

```cpp
vector<int> v = {10, 20, 30};

cout << v.at(5);
```

This throws an exception.

---

# 24. `[]` vs `at()`

| Feature | `v[index]` | `v.at(index)` |
|---|---|---|
| Access | Yes | Yes |
| Bounds checking | No | Yes |
| Invalid index | Undefined behavior | Throws `std::out_of_range` |
| Typical overhead | Lower | Bounds check |
| Complexity | O(1) | O(1) |

### DSA habit

Use `[]` when you know the index is valid and performance/simple syntax matters.

Use `at()` when explicit bounds checking is useful.

---

# 25. `clear()`

`clear()` removes all elements.

```cpp
vector<int> v = {10, 20, 30};

v.clear();
```

Now:

```text
size = 0
```

### Important

`clear()` destroys/removes the elements but does not necessarily reduce the vector's capacity.

So:

```text
size → 0
capacity → may remain unchanged
```

---

# 26. `empty()`

Use:

```cpp
v.empty()
```

It returns:

```text
true
```

if the vector contains no elements.

Example:

```cpp
if (v.empty()) {
    cout << "Vector is empty";
}
```

This is usually clearer than:

```cpp
if (v.size() == 0)
```

although both can express the same condition.

---

# 27. `insert()`

`insert()` inserts elements at a specified position.

Example:

```cpp
vector<int> v = {10, 20, 30};

v.insert(v.begin() + 1, 15);
```

Result:

```text
10 15 20 30
```

Why?

```text
v.begin()     → iterator to index 0
v.begin() + 1 → iterator to index 1
```

The new element is inserted before the element at index 1.

---

# 28. Inserting Multiple Copies

```cpp
vector<int> v = {10, 20, 30};

v.insert(v.begin() + 1, 3, 99);
```

Result:

```text
10 99 99 99 20 30
```

Syntax:

```cpp
insert(position, count, value)
```

---

# 29. `erase()`

Although not in the original function list, `erase()` is essential for vector DSA.

Remove one element:

```cpp
vector<int> v = {10, 20, 30};

v.erase(v.begin() + 1);
```

Result:

```text
10 30
```

The element at index 1 was removed.

---

# 30. Erasing a Range

```cpp
v.erase(v.begin() + 1, v.begin() + 3);
```

The range is:

```text
[first, last)
```

The first iterator is included, but the last iterator is excluded.

Example:

```text
10 20 30 40 50
```

Erase:

```cpp
v.erase(v.begin() + 1, v.begin() + 4);
```

Removes:

```text
20 30 40
```

Result:

```text
10 50
```

---

# 31. `resize()`

`resize()` changes the vector's size.

Example:

```cpp
vector<int> v = {1, 2, 3};

v.resize(5);
```

Result:

```text
1 2 3 0 0
```

For `int`, newly created elements are value-initialized to zero.

---

# 32. Resize to a Smaller Size

```cpp
vector<int> v = {1, 2, 3, 4, 5};

v.resize(3);
```

Result:

```text
1 2 3
```

The last two elements are removed.

---

# 33. `reserve()`

`reserve()` changes the **capacity**, not the size.

Example:

```cpp
vector<int> v;

v.reserve(100);
```

After this:

```text
size = 0
capacity >= 100
```

There are still **zero elements**.

This is a very important distinction:

```cpp
reserve(100);
```

does not create 100 elements.

---

# 34. `reserve()` vs `resize()`

| `reserve()` | `resize()` |
|---|---|
| Changes capacity | Changes size |
| Does not create elements | Creates/removes elements |
| `size` remains unchanged | `size` changes |
| Useful before many `push_back()` calls | Useful when you actually need a specific number of elements |

Example:

```cpp
vector<int> a;
a.reserve(5);
```

```text
size = 0
capacity >= 5
```

But:

```cpp
vector<int> b(5);
```

```text
size = 5
```

---

# 35. Range-Based For Loop

A vector can be traversed using:

```cpp
for (int x : vec) {
    cout << x << " ";
}
```

Example:

```cpp
vector<int> vec = {10, 20, 30};

for (int x : vec) {
    cout << x << " ";
}
```

Output:

```text
10 20 30
```

---

# 36. Modify Elements Using Reference

This:

```cpp
for (int x : vec) {
    x *= 2;
}
```

does not modify the vector because `x` is a copy.

Use:

```cpp
for (int &x : vec) {
    x *= 2;
}
```

Now the vector changes.

Example:

```text
Before:
1 2 3

After:
2 4 6
```

---

# 37. `auto` with Vector

You can write:

```cpp
for (auto x : vec) {
    cout << x << " ";
}
```

Or for modification:

```cpp
for (auto &x : vec) {
    x *= 2;
}
```

For read-only access without copying:

```cpp
for (const auto &x : vec) {
    cout << x << " ";
}
```

---

# 38. Vector Iterators

Vectors support iterators.

```cpp
vector<int> v = {10, 20, 30};

auto it = v.begin();

cout << *it;
```

Output:

```text
10
```

`begin()` points to the first element.

`end()` points **one position past the last element**.

Important:

```text
begin() → first element
end()   → one-past-last position
```

Do not dereference `end()`.

---

# 39. `begin()` and `end()`

Example:

```cpp
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";
}
```

Output:

```text
10 20 30
```

This is the basis for many STL algorithms.

---

# 40. Vector and `sort()`

Include:

```cpp
#include <algorithm>
```

Then:

```cpp
sort(v.begin(), v.end());
```

Example:

```cpp
vector<int> v = {5, 2, 9, 1, 4};

sort(v.begin(), v.end());
```

Result:

```text
1 2 4 5 9
```

Typical complexity:

```text
O(n log n)
```

---

# 41. Descending Sort

```cpp
sort(v.begin(), v.end(), greater<int>());
```

Result:

```text
9 5 4 2 1
```

---

# 42. Vector vs Array

| Feature | Built-in Array | Vector |
|---|---|---|
| Size | Fixed | Dynamic |
| `push_back()` | ❌ | ✅ |
| `pop_back()` | ❌ | ✅ |
| `size()` member | ❌ | ✅ |
| `capacity()` | ❌ | ✅ |
| `front()` | ❌ | ✅ |
| `back()` | ❌ | ✅ |
| `at()` | ❌ | ✅ |
| Automatic growth | ❌ | ✅ |
| STL integration | Limited | Excellent |

---

# 43. Static vs Dynamic Allocation — Important Correction

A common beginner statement is:

> "Static is compile time and allocation is runtime."

This is too simplified.

There are several different concepts:

- compile time vs runtime
- storage duration
- stack vs heap
- fixed-size arrays vs dynamic containers

For DSA, remember the practical distinction:

```text
Built-in array with fixed size
    ↓
size cannot dynamically grow

vector
    ↓
can dynamically manage its storage
```

A vector itself is an object with automatic/dynamic storage depending on how it is created, while its element storage is managed dynamically by the vector.

---

# 44. XOR Properties

The uploaded material introduces XOR.

XOR operator:

```cpp
^
```

Important properties:

```text
x ^ x = 0
x ^ 0 = x
```

Also:

```text
x ^ y ^ x = y
```

because:

```text
x ^ x = 0
0 ^ y = y
```

XOR is extremely useful in array problems.

---

# 45. Example — Find Single Element

Suppose every number occurs twice except one:

```text
2 4 1 4 2
```

Answer:

```text
1
```

Using XOR:

```cpp
int ans = 0;

for (int x : nums) {
    ans ^= x;
}
```

Why?

```text
2 ^ 4 ^ 1 ^ 4 ^ 2

(2 ^ 2) ^ (4 ^ 4) ^ 1

0 ^ 0 ^ 1

= 1
```

Complexity:

```text
Time  = O(n)
Space = O(1)
```

### Important condition

This simple XOR technique requires the intended frequency property, typically:

> Every element appears exactly twice except one element that appears once.

---

# 46. Kadane's Algorithm

## Problem

Find the **maximum sum of a contiguous subarray**.

Example:

```text
arr = [-2, 3, -1, 5, -6]
```

Possible subarrays include:

```text
[-2]
[3]
[3,-1]
[3,-1,5]
[-1,5]
...
```

The maximum sum is:

```text
3 + (-1) + 5 = 7
```

---

# 47. Brute-Force Maximum Subarray Sum

The uploaded code uses nested loops.

Correct form:

```cpp
vector<int> arr = {2, 33, 4, 63, 12};

int n = arr.size();
int maxSum = INT_MIN;

for (int st = 0; st < n; st++) {

    int currSum = 0;

    for (int en = st; en < n; en++) {

        currSum += arr[en];

        maxSum = max(maxSum, currSum);
    }
}

cout << maxSum << endl;
```

---

# 48. Why Does the Brute-Force Code Work?

For every starting position:

```cpp
st
```

we extend the ending position:

```cpp
en
```

Example:

```text
1 2 3
```

For:

```text
st = 0
```

we calculate:

```text
1
1+2
1+2+3
```

For:

```text
st = 1
```

we calculate:

```text
2
2+3
```

For:

```text
st = 2
```

we calculate:

```text
3
```

Thus every contiguous subarray is considered.

---

# 49. Brute-Force Complexity

Number of start/end combinations is approximately:

```text
n²
```

Therefore:

```text
Time = O(n²)
Space = O(1)
```

This is much better than calculating every subarray sum from scratch with a third loop, which can become O(n³).

---

# 50. Kadane's Core Idea

Kadane's Algorithm improves the maximum-subarray problem to:

```text
O(n)
```

The key question at every element is:

> Should I extend the current subarray, or start a new subarray here?

For each element:

```text
current = max(current + arr[i], arr[i])
```

Meaning:

```text
Either:
1. Continue previous subarray
or
2. Start fresh from arr[i]
```

---

# 51. Kadane's Algorithm

```cpp
long long current = arr[0];
long long best = arr[0];

for (int i = 1; i < n; i++) {

    current = max(1LL * arr[i], current + arr[i]);

    best = max(best, current);
}

cout << best;
```

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

# 91. Pair Sum Pattern Recognition

When you see:

> "Find two numbers whose sum equals target"

Ask:

### Is the array sorted?

If yes:

```text
Two pointers
```

### Is it unsorted?

Consider:

```text
Hashing
```

### Are constraints tiny?

Brute force may be acceptable:

```text
O(n²)
```

### Do you need original indices?

Be careful if sorting because sorting changes positions.

---

# 92. Kadane Pattern Recognition

When you see:

> "Maximum sum of a contiguous subarray"

Think:

```text
Kadane's Algorithm
```

Keywords:

```text
maximum subarray
largest contiguous sum
maximum sum contiguous segment
```

---

# 93. XOR Pattern Recognition

When you see:

> Every number appears twice except one.

Think:

```text
XOR
```

Because:

```text
x ^ x = 0
x ^ 0 = x
```

---

# 94. Majority Element Pattern Recognition

When you see:

> Element appears more than n/2 times.

Think:

```text
Moore's Voting Algorithm
```

If no majority is guaranteed:

```text
candidate + verification
```

---

# 95. Questions You Must Be Able to Answer

## Vector Basics

1. What is a vector?
2. Why is vector called a dynamic array?
3. How is vector different from a built-in array?
4. What does `vector<int> v(5)` create?
5. What does `vector<int> v(5, 10)` create?
6. What is the difference between `size()` and `capacity()`?
7. What does `push_back()` do?
8. What does `pop_back()` do?
9. Does `pop_back()` return the removed value?
10. What does `front()` return?
11. What does `back()` return?
12. What happens when `at()` receives an invalid index?
13. What does `clear()` do?
14. Does `clear()` necessarily reduce capacity?
15. What does `empty()` do?
16. What does `reserve()` do?
17. Difference between `reserve()` and `resize()`?
18. What is reallocation?
19. Why can `push_back()` sometimes be O(n)?
20. Why is `push_back()` amortized O(1)?

---

# 96. Algorithm Questions

21. What is Kadane's Algorithm?
22. What problem does Kadane solve?
23. Why is brute-force maximum subarray O(n²)?
24. What does `current` represent in Kadane?
25. What does `best` represent?
26. Why should Kadane handle all-negative arrays carefully?
27. What is Pair Sum?
28. What is the brute-force complexity?
29. Why does two-pointer Pair Sum require sorting?
30. Why do we move `right` when sum is too large?
31. Why do we move `left` when sum is too small?
32. How can hashing solve Pair Sum in O(n) average time?
33. What is the space complexity of hashing Pair Sum?
34. What is a majority element?
35. Why is the threshold `> n/2`?
36. How does sorting help find majority?
37. What is Moore's Voting Algorithm?
38. Why does cancellation work?
39. What is the difference between a candidate and a verified majority?
40. When should Moore's result be verified?

---

# 97. Coding Questions — Easy

### Q1. Create an empty vector and add five numbers using `push_back()`.

### Q2. Print the vector using a normal `for` loop.

### Q3. Print the vector using a range-based loop.

### Q4. Print first and last elements.

### Q5. Remove the last element.

### Q6. Insert `100` at index `2`.

### Q7. Delete the element at index `3`.

### Q8. Find the minimum element.

### Q9. Find the maximum element.

### Q10. Find the sum of all elements.

---

# 98. Coding Questions — Intermediate

### Q11. Reverse a vector in-place.

### Q12. Find the first occurrence of a target.

### Q13. Find the last occurrence.

### Q14. Count target frequency.

### Q15. Move all zeros to the end.

### Q16. Find the second largest distinct element.

### Q17. Check whether a vector is sorted.

### Q18. Find duplicate elements.

### Q19. Find the unique element using XOR.

### Q20. Rotate a vector left by `k`.

---

# 99. Coding Questions — Advanced

### Q21. Maximum subarray sum using brute force.

### Q22. Maximum subarray sum using Kadane.

### Q23. Return the actual maximum-sum subarray.

### Q24. Two Sum using nested loops.

### Q25. Two Sum using hashing.

### Q26. Two Sum on sorted array using two pointers.

### Q27. Find majority element using brute force.

### Q28. Find majority element using sorting.

### Q29. Find majority element using Moore's Voting.

### Q30. Find majority element and verify whether it actually exists.

---

# 100. Final Mental Map

```text
VECTOR
│
├── Dynamic sequence
│
├── Creation
│   ├── vector<int> v;
│   ├── vector<int> v = {};
│   ├── vector<int> v(5);
│   ├── vector<int> v(5, 10);
│   └── vector<int> v = {1,2,3};
│
├── Access
│   ├── []
│   ├── at()
│   ├── front()
│   └── back()
│
├── Modification
│   ├── push_back()
│   ├── pop_back()
│   ├── insert()
│   ├── erase()
│   ├── clear()
│   └── resize()
│
├── Memory
│   ├── size()
│   ├── capacity()
│   ├── reserve()
│   └── reallocation
│
└── DSA Patterns
    ├── XOR
    ├── Kadane
    ├── Two Pointers
    ├── Hashing
    └── Moore's Voting
```

---

# 101. Final Complexity Cheat Sheet

```text
Vector access              → O(1)
Vector size                → O(1)
Vector front/back          → O(1)
push_back                  → amortized O(1)
pop_back                   → O(1)
middle insertion           → O(n)
middle deletion            → O(n)

Brute-force Pair Sum       → O(n²)
Hashing Pair Sum           → O(n) average, O(n) space
Sorted Two-Pointer PairSum → O(n), O(1) extra space

Brute-force Max Subarray   → O(n²)
Kadane                     → O(n), O(1)

Brute-force Majority       → O(n²)
Sorting Majority           → O(n log n)
Moore's Voting             → O(n), O(1)

XOR unique-element problem → O(n), O(1)
```

---

# 102. The Most Important Things to Remember

```text
1. Vector = dynamic sequence container.
2. size = actual number of elements.
3. capacity = allocated storage available for elements.
4. reserve() changes capacity, not size.
5. resize() changes size.
6. push_back() is amortized O(1), not guaranteed O(1) every time.
7. at() performs bounds checking.
8. [] does not perform bounds checking.
9. pop_back() removes the last element and returns nothing.
10. x ^ x = 0.
11. x ^ 0 = x.
12. Kadane = maximum contiguous subarray sum.
13. Two pointers Pair Sum requires sorted data.
14. Hashing Pair Sum works on unsorted data in O(n) average time.
15. Majority = frequency > n/2.
16. Moore's Voting = O(n) time and O(1) extra space.
17. Moore's candidate must be verified if majority existence is not guaranteed.
18. Pass large vectors using const reference when you only need to read them.
19. Always inspect constraints before choosing an algorithm.
20. Do not memorize code without understanding the pattern.
```

---

# 103. Recommended Study Sequence

Study these concepts in this exact order:

```text
Vector basics
    ↓
size vs capacity
    ↓
push_back / pop_back
    ↓
front / back / at
    ↓
insert / erase
    ↓
clear / empty
    ↓
resize / reserve
    ↓
iterators
    ↓
sorting
    ↓
XOR problems
    ↓
Brute-force subarray problems
    ↓
Kadane's Algorithm
    ↓
Pair Sum brute force
    ↓
Pair Sum hashing
    ↓
Pair Sum two pointers
    ↓
Majority brute force
    ↓
Majority sorting
    ↓
Moore's Voting
    ↓
Mixed array problems
```

> **DSA rule:** First understand the brute-force solution, then identify what repeated work is happening, and finally optimize it using the correct pattern. This is how you move from `O(n²)` to `O(n)` instead of merely memorizing an "optimal" code template.
