[← Chapter 04](01-getting-started-basics-ch04-4-visual-diagram-c-memory-layo.md) · [Chapter Index](01-getting-started-basics.md) · [Module Overview](../README.md)

---

## 10. Interview Tips & What Companies Ask

### Common Interview Questions:
1. **What is the difference between stack and heap memory?**
2. **Explain pass by value vs pass by reference**
3. **What are pointers? When would you use them?**
4. **Difference between array and vector?**
5. **What is the STL? Name some containers**

### What Interviewers Look For:
- ✅ Understanding of memory management
- ✅ Knowing when to use references vs pointers
- ✅ Familiarity with STL containers
- ✅ Ability to write clean, bug-free code

### Pro Tips:
- Mention **time complexity** when discussing operations
- Explain **why** you chose a specific data structure
- Show you understand **trade-offs** (e.g., array vs vector)

---

## 11. Practice Problems

### 🟢 Easy Problems:
1. **Swap Two Numbers** — Swap without third variable
2. **Factorial** — Calculate factorial using loop
3. **Fibonacci Series** — Print first N Fibonacci numbers
4. **Palindrome Check** — Check if number is palindrome
5. **Prime Check** — Check if number is prime

### 🟡 Medium Problems:
6. **Reverse Array** — Reverse array in-place
7. **Find Max/Min** — Find max and min in array
8. **Remove Duplicates** — Remove duplicates from sorted array
9. **Rotate Array** — Rotate array by K positions
10. **Two Sum** — Find two numbers that add to target 🏢 [Google]

### Problem Links:
- LeetCode Two Sum: https://leetcode.com/problems/two-sum/
- GeeksforGeeks Array Problems: https://geeksforgeeks.org/array-data-structure/

---

## 12. Solved Example Problems

### Example 1: Find Maximum in Array

**Problem**: Find the maximum element in an array.

**Solution**:
```cpp
#include <iostream>
#include <vector>
using namespace std;

int findMax(vector<int>& arr) {
    int max_val = arr[0];  // Assume first element is max
    
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > max_val) {  // Found new max
            max_val = arr[i];
        }
    }
    
    return max_val;
}

int main() {
    vector<int> nums = {3, 7, 2, 9, 5, 1};
    cout << "Maximum: " << findMax(nums) << endl;  // 9
    return 0;
}
```

**Time Complexity**: O(n) — visit each element once  
**Space Complexity**: O(1) — only one variable used

---

### Example 2: Reverse a String

**Problem**: Reverse a string without using built-in functions.

**Solution**:
```cpp
#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    int left = 0;              // Start pointer
    int right = s.size() - 1;  // End pointer
    
    while (left < right) {
        swap(s[left], s[right]);  // Swap characters
        left++;                    // Move left pointer right
        right--;                   // Move right pointer left
    }
    
    return s;
}

int main() {
    string text = "hello";
    cout << "Reversed: " << reverseString(text) << endl;  // olleh
    return 0;
}
```

**Time Complexity**: O(n) — swap n/2 pairs  
**Space Complexity**: O(1) — in-place modification

---

### Example 3: Count Frequency Using Map

**Problem**: Count frequency of each element in array.

**Solution**:
```cpp
#include <iostream>
#include <vector>
#include <map>
using namespace std;

void countFrequency(vector<int>& arr) {
    map<int, int> freq;  // key = number, value = count
    
    for (int num : arr) {
        freq[num]++;  // Increment count for this number
    }
    
    // Print frequencies
    for (auto pair : freq) {
        cout << pair.first << ": " << pair.second << " times" << endl;
    }
}

int main() {
    vector<int> nums = {1, 2, 2, 3, 1, 4, 2, 3};
    countFrequency(nums);
    /* Output:
       1: 2 times
       2: 3 times
       3: 2 times
       4: 1 times
    */
    return 0;
}
```

**Time Complexity**: O(n log n) — map insertions take O(log n)  
**Space Complexity**: O(n) — store frequencies in map

---

## 13. Glossary

| Term | Definition |
|------|------------|
| **Variable** | Named storage location in memory |
| **Data Type** | Specifies what kind of data a variable holds |
| **Pointer** | Variable that stores memory address of another variable |
| **Reference** | Alias (nickname) for an existing variable |
| **Function** | Reusable block of code that performs a task |
| **Array** | Fixed-size collection of elements of same type |
| **Vector** | Dynamic array that can grow/shrink (STL) |
| **STL** | Standard Template Library — pre-built data structures and algorithms |
| **Map** | Associative container storing key-value pairs |
| **Set** | Container storing unique elements in sorted order |
| **Stack** | LIFO data structure (Last In First Out) |
| **Queue** | FIFO data structure (First In First Out) |
| **Class** | Blueprint for creating objects (OOP) |
| **Object** | Instance of a class |
| **Constructor** | Special function called when object is created |
| **Amortized** | Average cost over multiple operations |

---

## 14. Future Questions (Predictions)

Based on current interview trends:
1. **Smart Pointers** — `unique_ptr`, `shared_ptr` (modern C++)
2. **Lambda Functions** — Anonymous functions for STL algorithms
3. **Move Semantics** — `std::move` for efficient resource transfer
4. **Auto and Type Inference** — When to use `auto` keyword
5. **Range-Based Algorithms** — STL algorithms with iterators

---

## 15. Competitive Programming Section

### Fast I/O Template:
```cpp
#include <iostream>
#include <vector>
using namespace std;

void solve() {
    // Your code here
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;  // Number of test cases
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}
```

### Common CP Shortcuts:
```cpp
#define ll long long
#define vi vector<int>
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
```

### Useful One-Liners:
```cpp
// Sort in descending order
sort(v.rbegin(), v.rend());

// Count occurrences
int cnt = count(v.begin(), v.end(), target);

// Find maximum element
int mx = *max_element(v.begin(), v.end());

// Accumulate (sum)
int sum = accumulate(v.begin(), v.end(), 0);
```

---

**🎉 Congratulations! You've completed the C++ Prerequisites topic!**

**Next Steps**:
1. ✅ Complete all MCQs in `00_mcqs.md`
2. ✅ Solve 10 practice problems
3. ✅ Move to **01_Complexity_Analysis**

[← Back to README](../README.md) | [Next: Complexity Analysis →](../../01-Complexity-Analysis/concepts/01-asymptotic-analysis-and-big-o.md)
