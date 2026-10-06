[← Chapter 03](01-getting-started-basics-ch03-00-c-prerequisites-complete-no.md) · [Chapter Index](01-getting-started-basics.md) · [Module Overview](../README.md) · [Chapter 05 →](01-getting-started-basics-ch05-10-interview-tips-what-compani.md)

---

## 4. Visual Diagram: C++ Memory Layout

```
┌──────────────────────────────────────────────────────┐
│                  C++ Memory Layout                    │
├──────────────────────────────────────────────────────┤
│                                                       │
│  High Address                                         │
│  ┌──────────────────────────────────┐                 │
│  │         Stack                    │                 │
│  │  • Local variables               │                 │
│  │  • Function calls                │                 │
│  │  • Automatic memory              │                 │
│  └──────────────────────────────────┘                 │
│                      ↓ grows down                     │
│                                                       │
│                      ↑ grows up                       │
│  ┌──────────────────────────────────┐                 │
│  │         Heap                     │                 │
│  │  • Dynamic memory (new/delete)   │                 │
│  │  • Vectors, dynamic arrays       │                 │
│  │  • Manual memory management      │                 │
│  └──────────────────────────────────┘                 │
│                                                       │
│  ┌──────────────────────────────────┐                 │
│  │     Global/Static Data           │                 │
│  │  • Global variables              │                 │
│  │  • Static variables              │                 │
│  └──────────────────────────────────┘                 │
│                                                       │
│  ┌──────────────────────────────────┐                 │
│  │     Code (Program Instructions)  │                 │
│  └──────────────────────────────────┘                 │
│                                                       │
│  Low Address                                          │
└──────────────────────────────────────────────────────┘
```

---

## 5. Introduction to STL (Standard Template Library)

**What is STL?**  
STL is C++'s **built-in toolbox** of data structures and algorithms. Instead of implementing everything from scratch, you use pre-built, optimized versions.

**Why Use STL?**
- ✅ **Fast**: Highly optimized by experts
- ✅ **Reliable**: Tested thoroughly
- ✅ **Easy**: Less code to write
- ✅ **Standard**: Works everywhere

### 5.1 Vector (Dynamic Array)

```cpp
#include <iostream>
#include <vector>  // Include vector library
using namespace std;

int main() {
    // Create vectors
    vector<int> nums;                    // Empty vector
    vector<int> scores = {90, 85, 92};   // Initialize with values
    
    // Add elements
    nums.push_back(10);   // Add to end: [10]
    nums.push_back(20);   // Add to end: [10, 20]
    nums.push_back(30);   // Add to end: [10, 20, 30]
    
    // Access elements (like arrays)
    cout << "First: " << nums[0] << endl;    // 10
    cout << "Second: " << nums.at(1) << endl; // 20 (safer)
    
    // Size and capacity
    cout << "Size: " << nums.size() << endl;       // 3
    cout << "Empty: " << nums.empty() << endl;     // 0 (false)
    
    // Remove elements
    nums.pop_back();  // Remove last: [10, 20]
    
    // Iterate through vector
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;  // 10 20
    
    // Range-based for loop (easier)
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;  // 10 20
    
    return 0;
}
```

**Vector Operations Complexity**:
| Operation | Time Complexity |
|-----------|----------------|
| Access by index | O(1) |
| push_back | O(1) amortized |
| pop_back | O(1) |
| insert/delete at end | O(1) |
| insert/delete at beginning | O(n) |
| Search | O(n) |

---

### 5.2 Pair

```cpp
#include <iostream>
#include <utility>  // Include pair library
using namespace std;

int main() {
    // Create pair
    pair<int, string> student = {1, "Alice"};
    
    // Access elements
    cout << "ID: " << student.first << endl;   // 1
    cout << "Name: " << student.second << endl; // Alice
    
    // Modify
    student.first = 2;
    student.second = "Bob";
    
    // Make pair (shorthand)
    auto p = make_pair(10, 20);
    cout << p.first << ", " << p.second << endl;  // 10, 20
    
    return 0;
}
```

---

### 5.3 Map (Key-Value Pairs)

```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    // Create map
    map<string, int> ages;
    
    // Insert elements
    ages["Alice"] = 25;
    ages["Bob"] = 30;
    ages["Charlie"] = 22;
    
    // Access elements
    cout << "Alice's age: " << ages["Alice"] << endl;  // 25
    
    // Check if key exists
    if (ages.count("Bob")) {
        cout << "Bob exists!" << endl;
    }
    
    // Iterate through map
    for (auto pair : ages) {
        cout << pair.first << ": " << pair.second << endl;
    }
    // Output (sorted by key):
    // Alice: 25
    // Bob: 30
    // Charlie: 22
    
    // Delete element
    ages.erase("Charlie");
    
    return 0;
}
```

**Map Operations Complexity**:
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Delete | O(log n) |
| Search | O(log n) |
| Access | O(log n) |

---

### 5.4 Set (Unique Elements)

```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    // Create set
    set<int> numbers;
    
    // Insert elements
    numbers.insert(30);
    numbers.insert(10);
    numbers.insert(20);
    numbers.insert(10);  // Duplicate - ignored!
    
    // Set automatically sorts and removes duplicates
    for (int num : numbers) {
        cout << num << " ";
    }
    // Output: 10 20 30 (sorted, no duplicates)
    
    // Check if element exists
    if (numbers.count(20)) {
        cout << "\n20 exists!" << endl;
    }
    
    // Delete element
    numbers.erase(10);
    
    return 0;
}
```

---

### 5.5 Stack (LIFO - Last In First Out)

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    
    // Push elements
    s.push(10);
    s.push(20);
    s.push(30);
    
    // Top element
    cout << "Top: " << s.top() << endl;  // 30
    
    // Size
    cout << "Size: " << s.size() << endl;  // 3
    
    // Pop element (remove top)
    s.pop();
    cout << "After pop, top: " << s.top() << endl;  // 20
    
    return 0;
}
```

💡 **TRICK**: **Stack = Stack of plates** — you add/remove from the top only!

---

### 5.6 Queue (FIFO - First In First Out)

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    
    // Push elements (enqueue)
    q.push(10);
    q.push(20);
    q.push(30);
    
    // Front and back
    cout << "Front: " << q.front() << endl;  // 10
    cout << "Back: " << q.back() << endl;    // 30
    
    // Pop element (dequeue)
    q.pop();
    cout << "After pop, front: " << q.front() << endl;  // 20
    
    return 0;
}
```

💡 **TRICK**: **Queue = Real-life queue** — first person gets served first!

---

## 6. Dry Run: Understanding Pointers

Let's trace this code step-by-step:

```cpp
int a = 10;
int b = 20;
int *ptr = &a;
*ptr = 30;
ptr = &b;
*ptr = 40;
```

**Step-by-Step Trace**:

```
Step 1: int a = 10;
┌─────┐
│ a   │ = 10
│Addr:│ = 0x1000
└─────┘

Step 2: int b = 20;
┌─────┐     ┌─────┐
│ a   │     │ b   │
│  10 │     │  20 │
│0x1000│    │0x2000│
└─────┘     └─────┘

Step 3: int *ptr = &a;
┌─────┐     ┌─────┐     ┌──────┐
│ a   │     │ b   │     │ ptr  │
│  10 │     │  20 │     │0x1000│ → points to a
│0x1000│    │0x2000│    └──────┘
└─────┘     └─────┘

Step 4: *ptr = 30; (change value at ptr's address)
┌─────┐     ┌─────┐     ┌──────┐
│ a   │     │ b   │     │ ptr  │
│  30 │←────│  20 │     │0x1000│
│0x1000│    │0x2000│    └──────┘
└─────┘     └─────┘

Step 5: ptr = &b; (ptr now points to b)
┌─────┐     ┌─────┐     ┌──────┐
│ a   │     │ b   │     │ ptr  │
│  30 │     │  20 │     │0x2000│ → now points to b
│0x1000│    │0x2000│    └──────┘
└─────┘     └─────┘

Step 6: *ptr = 40; (change value at ptr's address)
┌─────┐     ┌─────┐     ┌──────┐
│ a   │     │ b   │     │ ptr  │
│  30 │     │  40 │←────│0x2000│
│0x1000│    │0x2000│    └──────┘
└─────┘     └─────┘

Final Result: a = 30, b = 40
```

---

## 7. Operations Summary Table

| Concept | Operation | Syntax | Time Complexity |
|---------|-----------|--------|----------------|
| **Vector** | Access | `v[i]` | O(1) |
| | Push back | `v.push_back(x)` | O(1) |
| | Pop back | `v.pop_back()` | O(1) |
| | Size | `v.size()` | O(1) |
| **Map** | Insert | `m[key] = value` | O(log n) |
| | Search | `m.count(key)` | O(log n) |
| | Delete | `m.erase(key)` | O(log n) |
| **Set** | Insert | `s.insert(x)` | O(log n) |
| | Search | `s.count(x)` | O(log n) |
| | Delete | `s.erase(x)` | O(log n) |
| **Stack** | Push | `s.push(x)` | O(1) |
| | Pop | `s.pop()` | O(1) |
| | Top | `s.top()` | O(1) |
| **Queue** | Push | `q.push(x)` | O(1) |
| | Pop | `q.pop()` | O(1) |
| | Front | `q.front()` | O(1) |

---

## 8. Common Patterns & Tricks

### 💡 TRICK 1: Fast I/O for Competitive Programming
```cpp
ios_base::sync_with_stdio(false);
cin.tie(NULL);
```
This makes `cin`/`cout` as fast as `scanf`/`printf`!

### 💡 TRICK 2: Auto Keyword
```cpp
auto x = 10;           // int
auto y = 3.14;         // double
auto z = "hello";      // const char*
for (auto it : vec)    // Automatically detects type
```

### 💡 TRICK 3: Range-Based For Loop
```cpp
vector<int> nums = {1, 2, 3, 4, 5};

// Old way
for (int i = 0; i < nums.size(); i++) {
    cout << nums[i] << " ";
}

// New way (cleaner)
for (int num : nums) {
    cout << num << " ";
}

// Modify elements (use reference)
for (int &num : nums) {
    num *= 2;  // Doubles each element
}
```

### 💡 TRICK 4: Initialize Vector Quickly
```cpp
vector<int> v1(10, 0);        // 10 zeros: [0, 0, ..., 0]
vector<int> v2 = {1, 2, 3};   // Direct initialization
vector<int> v3(v2);           // Copy v2
```

### 💡 TRICK 5: Swap Two Variables
```cpp
int a = 5, b = 10;
swap(a, b);  // Built-in function
cout << a << " " << b;  // 10 5
```

---

## 9. Common Mistakes & How to Avoid Them

### ❌ Mistake 1: Forgetting Semicolons
```cpp
int x = 10  // ERROR: missing semicolon
int y = 20; // Correct
```
✅ **Fix**: Always end statements with `;`

### ❌ Mistake 2: Array Index Out of Bounds
```cpp
int arr[5] = {1, 2, 3, 4, 5};
cout << arr[5];  // ERROR! Valid indices: 0-4
```
✅ **Fix**: Remember indices are 0 to size-1

### ❌ Mistake 3: Uninitialized Variables
```cpp
int x;
cout << x;  // ERROR: x has garbage value
```
✅ **Fix**: Always initialize variables: `int x = 0;`

### ❌ Mistake 4: Integer Division
```cpp
double result = 10 / 3;  // Result: 3.0 (not 3.333!)
```
✅ **Fix**: Make one operand double: `double result = 10.0 / 3;`

### ❌ Mistake 5: Using = Instead of ==
```cpp
if (x = 5) {  // ERROR: assigns 5 to x, always true
    cout << "x is 5";
}
```
✅ **Fix**: Use `==` for comparison: `if (x == 5)`

### ❌ Mistake 6: Forgetting to Include Headers
```cpp
vector<int> v;  // ERROR: missing #include <vector>
```
✅ **Fix**: Always include required headers

---
