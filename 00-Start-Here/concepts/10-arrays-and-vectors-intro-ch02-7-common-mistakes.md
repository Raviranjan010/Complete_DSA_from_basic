[← Chapter 01](10-arrays-and-vectors-intro-ch01-array-basics-complete-beginner.md) · [Chapter Index](10-arrays-and-vectors-intro.md) · [Module Overview](../README.md) · [Chapter 03 →](10-arrays-and-vectors-intro-ch03-vector-vs-array-decision-guide.md)

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
