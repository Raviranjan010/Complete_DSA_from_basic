[← Chapter 02](01-getting-started-basics-ch02-formula-approach-time-o1-space.md) · [Chapter Index](01-getting-started-basics.md) · [Module Overview](../README.md) · [Chapter 04 →](01-getting-started-basics-ch04-4-visual-diagram-c-memory-layo.md)

---

# 00 — C++ Prerequisites — Complete Notes

> **What You'll Learn**: C++ basics needed for DSA — variables, data types, pointers, references, functions, OOP, and STL introduction  
> **Prerequisites**: Basic programming knowledge (any language)  
> **Time Required**: 1 week (10-15 hours)

---

## 1. What is C++? (Real-World Analogy)

Imagine you're building a house:
- **C** is like having basic tools (hammer, saw) — powerful but you do everything manually
- **C++** is like having a complete workshop with power tools — same power, but with helpful machines that do repetitive work for you
- **Python/Java** are like hiring contractors — easier but slower and less control

**C++ gives you**:
- ⚡ **Speed**: Runs very fast (used in game engines, trading systems)
- 🎮 **Control**: You manage memory, optimize performance
- 🏗️ **Structure**: Object-oriented programming for large projects
- 📦 **STL (Standard Template Library)**: Pre-built data structures and algorithms

💡 **TRICK**: Think of C++ as a sports car — powerful and fast, but you need to learn to drive it properly!

---

## 2. Why Do We Need C++ for DSA?

1. **Speed**: DSA interviews often have time limits. C++ is 10-100x faster than Python
2. **STL**: Built-in vectors, maps, sets, stacks, queues — implement algorithms quickly
3. **Industry Standard**: Most competitive programmers use C++
4. **Memory Control**: Understand how data structures work under the hood
5. **Interview Preference**: Many interviewers expect C++/Java for coding rounds

---

## 3. Core Concepts & Terminology

### 3.1 Your First C++ Program

```cpp
#include <iostream>  // Include input/output library
using namespace std; // Use standard namespace (avoid typing std::)

int main() {         // Main function - program starts here
    cout << "Hello, DSA!" << endl;  // Print to console
    return 0;        // Return 0 means program succeeded
}
```

**Line-by-Line Explanation**:
- `#include <iostream>`: Tells compiler to include input/output functionality
- `using namespace std;`: Allows us to write `cout` instead of `std::cout`
- `int main()`: Every C++ program must have a main function
- `cout <<`: Prints to console (character output)
- `endl`: Ends the line (like pressing Enter)
- `return 0;`: Tells operating system program ran successfully

---

### 3.2 Variables & Data Types

**What is a Variable?**  
A variable is like a **labeled box** that stores data.

```
┌─────────────────┐
│   age = 25      │  ← Variable name: age, Value: 25
└─────────────────┘
```

**Basic Data Types**:

| Type | Size | Range | Example | Use Case |
|------|------|-------|---------|----------|
| `int` | 4 bytes | -2B to +2B | `int age = 25;` | Counting, indexing |
| `float` | 4 bytes | 7 decimal digits | `float pi = 3.14f;` | Approximate decimals |
| `double` | 8 bytes | 15 decimal digits | `double pi = 3.14159;` | Precise decimals |
| `char` | 1 byte | Single character | `char grade = 'A';` | Single characters |
| `bool` | 1 byte | true/false | `bool pass = true;` | Conditions, flags |
| `long long` | 8 bytes | -9Q to +9Q | `long long big = 1e18;` | Very large numbers |

**Complete Example**:

```cpp
#include <iostream>
using namespace std;

int main() {
    // Integer variables
    int age = 20;                    // Store whole numbers
    int students_count = 100;        // Descriptive names are good
    
    // Floating-point variables
    float temperature = 36.6f;       // 'f' means float
    double precise_pi = 3.14159265;  // More precise than float
    
    // Character variable
    char first_letter = 'A';         // Single quotes for char
    
    // Boolean variable
    bool is_student = true;          // true or false (1 or 0)
    
    // Print all variables
    cout << "Age: " << age << endl;
    cout << "Temperature: " << temperature << endl;
    cout << "First Letter: " << first_letter << endl;
    cout << "Is Student: " << is_student << endl;  // Prints 1 for true
    
    return 0;
}
```

**Output**:
```
Age: 20
Temperature: 36.6
First Letter: A
Is Student: 1
```

💡 **TRICK**: **Mnemonic for data type sizes**: "C F D" → **C**har (1), **F**loat (4), **D**ouble (8) — doubles in size!

---

### 3.3 Operators

**Types of Operators**:

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;
    
    // 1. Arithmetic Operators
    cout << "Addition: " << (a + b) << endl;        // 13
    cout << "Subtraction: " << (a - b) << endl;     // 7
    cout << "Multiplication: " << (a * b) << endl;  // 30
    cout << "Division: " << (a / b) << endl;        // 3 (integer division!)
    cout << "Modulo: " << (a % b) << endl;          // 1 (remainder)
    
    // 2. Comparison Operators (return bool)
    cout << "a == b: " << (a == b) << endl;  // 0 (false)
    cout << "a != b: " << (a != b) << endl;  // 1 (true)
    cout << "a > b: " << (a > b) << endl;    // 1 (true)
    cout << "a < b: " << (a < b) << endl;    // 0 (false)
    
    // 3. Logical Operators
    bool x = true, y = false;
    cout << "x AND y: " << (x && y) << endl;  // 0 (both must be true)
    cout << "x OR y: " << (x || y) << endl;   // 1 (at least one true)
    cout << "NOT x: " << (!x) << endl;        // 0 (opposite)
    
    // 4. Assignment Operators
    int c = 5;
    c += 3;  // Same as: c = c + 3
    cout << "c += 3: " << c << endl;  // 8
    
    c *= 2;  // Same as: c = c * 2
    cout << "c *= 2: " << c << endl;  // 16
    
    return 0;
}
```

⚠️ **Common Mistake**: Integer division!
```cpp
int result = 10 / 3;      // Result is 3, NOT 3.333
double result2 = 10.0 / 3; // Result is 3.333 (one operand is double)
```

---

### 3.4 Control Flow (if/else, loops)

#### Conditional Statements

```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 85;
    
    // Simple if
    if (score >= 90) {
        cout << "Grade: A" << endl;
    }
    
    // if-else
    if (score >= 50) {
        cout << "Passed!" << endl;
    } else {
        cout << "Failed!" << endl;
    }
    
    // if-else if-else chain
    if (score >= 90) {
        cout << "Grade: A" << endl;
    } else if (score >= 80) {
        cout << "Grade: B" << endl;
    } else if (score >= 70) {
        cout << "Grade: C" << endl;
    } else {
        cout << "Grade: F" << endl;
    }
    
    // Ternary operator (shorthand if-else)
    string result = (score >= 50) ? "Pass" : "Fail";
    cout << "Result: " << result << endl;
    
    return 0;
}
```

#### Loops

**For Loop** (when you know number of iterations):
```cpp
// Print numbers 1 to 5
for (int i = 1; i <= 5; i++) {
    cout << i << " ";
}
// Output: 1 2 3 4 5
```

**While Loop** (when condition-based):
```cpp
int count = 1;
while (count <= 5) {
    cout << count << " ";
    count++;  // Don't forget to increment!
}
// Output: 1 2 3 4 5
```

**Do-While Loop** (executes at least once):
```cpp
int num = 10;
do {
    cout << num << " ";
    num++;
} while (num <= 5);  // Condition false, but runs once
// Output: 10
```

💡 **TRICK**: **Loop Selection Mnemonic**:
- **FOR** = **F**ixed number of iterations
- **WHILE** = **W**ait for condition to change
- **DO-WHILE** = **D**o it at least once

---

### 3.5 Functions

**What is a Function?**  
A function is like a **recipe** — you give it ingredients (inputs), it does something, and returns a dish (output).

```cpp
#include <iostream>
using namespace std;

// Function definition
int add(int a, int b) {        // Return type: int, Parameters: a, b
    int sum = a + b;           // Do the calculation
    return sum;                // Return the result
}

// Function with no return value
void greet(string name) {      // void means no return
    cout << "Hello, " << name << "!" << endl;
}

// Function with default parameter
int power(int base, int exp = 2) {  // exp defaults to 2
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    // Call add function
    int result = add(5, 3);
    cout << "5 + 3 = " << result << endl;  // 8
    
    // Call void function
    greet("Alice");  // Hello, Alice!
    
    // Call with default parameter
    cout << "3^2 = " << power(3) << endl;      // 9 (uses default exp=2)
    cout << "3^3 = " << power(3, 3) << endl;   // 27
    
    return 0;
}
```

**Pass by Value vs Pass by Reference**:

```cpp
#include <iostream>
using namespace std;

// Pass by VALUE (creates a copy)
void increment_value(int x) {
    x++;  // Only changes the copy
}

// Pass by REFERENCE (modifies original)
void increment_reference(int &x) {  // & means reference
    x++;  // Changes the original variable
}

int main() {
    int a = 10, b = 10;
    
    increment_value(a);
    cout << "After pass by value: " << a << endl;    // Still 10
    
    increment_reference(b);
    cout << "After pass by reference: " << b << endl; // Now 11
    
    return 0;
}
```

💡 **TRICK**: **Reference Trick**: `&` = "**A**ddress of" or "**A**lter original" — both start with A!

---

### 3.6 Pointers (The Scary Part Made Simple!)

**What is a Pointer?**  
A pointer is a variable that **stores the memory address** of another variable.

**Real-World Analogy**:  
- **Variable** = House with people inside  
- **Pointer** = Address of the house (not the house itself)

```
┌──────────────┐         ┌──────────────┐
│   int age    │         │   int *ptr   │
│   Value: 25  │         │   Value:     │
│   Address:   │────────→│   0x7ffd...  │
│   0x7ffd...  │         │   (points to │
└──────────────┘         │    age)      │
                         └──────────────┘
```

**Pointer Basics**:

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 25;           // Regular variable
    int *ptr = &age;        // Pointer stores address of age (& = address-of operator)
    
    cout << "Value of age: " << age << endl;        // 25
    cout << "Address of age: " << &age << endl;     // 0x7ffd...
    cout << "Value of ptr: " << ptr << endl;        // 0x7ffd... (same address)
    cout << "Value at ptr: " << *ptr << endl;       // 25 (* = dereference, get value)
    
    // Modify value through pointer
    *ptr = 30;  // Change value at address ptr points to
    cout << "New age: " << age << endl;  // 30 (age changed!)
    
    return 0;
}
```

**Key Operators**:
- `&` = **Address-of** (get memory address)
- `*` = **Dereference** (get value at address)

💡 **TRICK**: **Pointer Mnemonic**:
- `&` looks like a twisted "**A**" → **A**ddress
- `*` looks like a star pointing down → **V**alue at location (star = V in Roman numerals!)

**Pointer Arithmetic**:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // ptr points to first element (arr[0])
    
    cout << "*ptr: " << *ptr << endl;         // 10
    cout << "*(ptr+1): " << *(ptr+1) << endl; // 20 (next element)
    cout << "*(ptr+2): " << *(ptr+2) << endl; // 30
    
    // ptr + 1 moves by sizeof(int) = 4 bytes
    cout << "ptr: " << ptr << endl;           // 0x1000
    cout << "ptr+1: " << (ptr+1) << endl;     // 0x1004 (4 bytes ahead)
    
    return 0;
}
```

---

### 3.7 References (Easier Alternative to Pointers)

**What is a Reference?**  
A reference is an **alias** (nickname) for an existing variable.

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 25;
    int &ref = age;  // ref is now an alias for age
    
    cout << "age: " << age << endl;      // 25
    cout << "ref: " << ref << endl;      // 25 (same as age)
    
    ref = 30;  // Changing ref changes age
    cout << "age after ref=30: " << age << endl;  // 30
    
    // References MUST be initialized when declared
    // int &bad_ref;  // ERROR: must initialize
    
    return 0;
}
```

**References vs Pointers**:

| Feature | Reference | Pointer |
|---------|-----------|---------|
| Syntax | `int &ref = var;` | `int *ptr = &var;` |
| Initialization | Must initialize | Can be NULL |
| Reassignment | Cannot change target | Can point elsewhere |
| Null value | Cannot be null | Can be nullptr |
| Usage | Easier, safer | More flexible |

💡 **TRICK**: When in doubt, use **references** over pointers — they're safer and easier!

---

### 3.8 Arrays (Fixed-Size)

```cpp
#include <iostream>
using namespace std;

int main() {
    // Declare and initialize
    int arr[5] = {10, 20, 30, 40, 50};
    
    // Access elements (0-indexed!)
    cout << "First: " << arr[0] << endl;   // 10
    cout << "Last: " << arr[4] << endl;    // 50
    
    // Modify elements
    arr[2] = 35;
    cout << "Modified: " << arr[2] << endl;  // 35
    
    // Loop through array
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    // Output: 10 20 35 40 50
    
    // Size of array
    cout << "\nSize: " << sizeof(arr) / sizeof(arr[0]) << endl;  // 5
    
    return 0;
}
```

⚠️ **Common Mistake**: Array indices start at 0, not 1!
```cpp
int arr[5];
arr[5] = 100;  // ERROR! Valid indices: 0, 1, 2, 3, 4
```

---

### 3.9 Strings

```cpp
#include <iostream>
#include <string>  // Include string library
using namespace std;

int main() {
    // Create strings
    string name = "Alice";
    string greeting = "Hello, " + name + "!";  // Concatenation
    
    cout << greeting << endl;  // Hello, Alice!
    
    // String operations
    cout << "Length: " << name.length() << endl;     // 5
    cout << "Size: " << name.size() << endl;         // 5 (same as length)
    cout << "Empty: " << name.empty() << endl;       // 0 (false)
    
    // Access characters
    cout << "First char: " << name[0] << endl;       // A
    cout << "Last char: " << name[name.size()-1] << endl;  // e
    
    // Substring
    cout << "Substring: " << name.substr(0, 3) << endl;  // Ali
    
    // Find
    string text = "Hello, World!";
    cout << "Position of 'World': " << text.find("World") << endl;  // 7
    
    return 0;
}
```

---

### 3.10 Object-Oriented Programming Basics

**Class**: Blueprint for creating objects  
**Object**: Instance of a class

```cpp
#include <iostream>
using namespace std;

// Define a class
class Student {
public:  // Access modifier: public means accessible outside
    // Member variables (attributes)
    string name;
    int age;
    double gpa;
    
    // Member function (method)
    void introduce() {
        cout << "Hi, I'm " << name << ", age " << age 
             << ", GPA: " << gpa << endl;
    }
    
    // Constructor (called when object is created)
    Student(string n, int a, double g) {
        name = n;
        age = a;
        gpa = g;
    }
};

int main() {
    // Create object
    Student s1("Alice", 20, 3.8);
    
    // Access members
    s1.introduce();  // Hi, I'm Alice, age 20, GPA: 3.8
    
    // Modify members
    s1.gpa = 3.9;
    cout << "New GPA: " << s1.gpa << endl;  // 3.9
    
    return 0;
}
```

---
