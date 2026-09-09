# 📘 Functions in C++ — Complete Guide

## 1️⃣ What is a Function?
A function is a reusable block of code that performs a specific task. It runs only when it is called.

### 👉 Why use Functions?
*   **Reusability**: Write once, use multiple times (DRY Principle - Don't Repeat Yourself).
*   **Readability**: Breaks complex problems into smaller, manageable chunks.
*   **Maintenance**: Easy to debug and update logic in one place.

---

## 2️⃣ Basic Syntax

```cpp
return_type functionName(parameters) {
    // Body of the function
    return value;
}
```

### 🔹 Components
1.  **Return Type**: Data type of the value returned (e.g., `int`, `bool`, `void` if nothing is returned).
2.  **Function Name**: Unique name to identify the function.
3.  **Parameters**: Inputs passed to the function (optional).
4.  **Body**: Code to be executed.

---

## 3️⃣ Declaration vs Definition
C++ executes code line-by-line. If you call a function before defining it, the compiler will throw an error unless you **declare** it first.

### ✅ The Correct Pattern
```cpp
#include <iostream>
using namespace std;

// 1. Declaration (Prototype) - Tells compiler "This exists"
void sayHello();

int main() {
    // 2. Function Call - Execution
    sayHello();
    return 0;
}

// 3. Definition - The actual code
void sayHello() {
    cout << "Hello World\n";
}
```

---

## 4️⃣ Default Arguments
You can provide default values for parameters. If an argument is missing during the call, the default value is used.

### ⚠️ The Golden Rule (Right-to-Left)
Default arguments must be assigned starting from the **rightmost** parameter.

| Syntax | Valid? | Reason |
| :--- | :--- | :--- |
| `void func(int a, int b = 10)` | ✅ | Default is at the end. |
| `void func(int a = 5, int b = 10)` | ✅ | All defaults from right. |
| `void func(int a = 5, int b)` | ❌ | **ERROR**: `b` (right) has no default, but `a` (left) does. |

### Example
```cpp
int sum(int a = 5, int b = 10) {
    return a + b;
}

// Calls:
sum(20, 30); // Returns 50 (a=20, b=30)
sum(20);     // Returns 30 (a=20, b=10 default)
sum();       // Returns 15 (a=5 default, b=10 default)
```

---

## 5️⃣ Using Conditional Statements in Functions
Functions often use conditional logic (`if-else`, `switch`) to make decisions or validate input.

### 🔹 1. Early Return (Guard Clauses)
Instead of wrapping the entire function in a big `if-else`, use `return` to exit early. This makes code cleaner.

**Bad Practice (Nested):**
```cpp
void checkAge(int age) {
    if (age >= 0) {
        if (age >= 18) {
            cout << "Adult";
        } else {
            cout << "Minor";
        }
    } else {
        cout << "Invalid Age";
    }
}
```

**Good Practice (Guard Clause):**
```cpp
void checkAge(int age) {
    if (age < 0) {
        cout << "Invalid Age";
        return; // 🛑 Stop execution here
    }
    
    if (age >= 18) {
        cout << "Adult";
        return;
    }
    
    cout << "Minor";
}
```

### 🔹 2. Switch inside Functions
Useful for menu-driven logic or mapping values.

```cpp
string getDayName(int day) {
    switch(day) {
        case 1: return "Monday";
        case 2: return "Tuesday";
        case 3: return "Wednesday";
        default: return "Invalid Day";
    }
}
```

### 🔹 3. Ternary Operator in Return
For simple conditions, return the result directly.

```cpp
bool isEven(int n) {
    return (n % 2 == 0) ? true : false;
    // Or simply: return (n % 2 == 0);
}
```

---

## 6️⃣ Pass by Value vs Pass by Reference
This is a **critical** concept in C++.

### 🅰️ Pass by Value (Copy)
*   The function gets a **copy** of the variable.
*   Changes inside the function **DO NOT** affect the original variable.

```cpp
void update(int n) {
    n = n + 5; // Modifies local copy only
}

int main() {
    int a = 10;
    update(a);
    cout << a; // Output: 10 (Unchanged)
}
```

### 🅱️ Pass by Reference (Original)
*   The function gets the **address/reference** of the variable using `&`.
*   Changes inside the function **DO** affect the original variable.

```cpp
void update(int &n) { // Note the '&'
    n = n + 5; // Modifies original memory
}

int main() {
    int a = 10;
    update(a);
    cout << a; // Output: 15 (Changed!)
}
```

---

## 7️⃣ Function Overloading
You can have multiple functions with the **same name** but **different parameters** (type or number).

```cpp
// Function 1: Sum of two ints
int sum(int a, int b) {
    return a + b;
}

// Function 2: Sum of three ints
int sum(int a, int b, int c) {
    return a + b + c;
}

// Function 3: Sum of doubles
double sum(double a, double b) {
    return a + b;
}
```
*   ❌ You cannot overload based on **return type** alone.

---

## 8️⃣ Common Examples & Interview Questions

### ✅ Check Prime Number (Optimized)
Logic: Check divisibility from `2` to `sqrt(n)`.

```cpp
bool isPrime(int n) {
    if (n <= 1) return false; // 0 and 1 are not prime

    for (int i = 2; i * i <= n; i++) { // i*i <= n is same as i <= sqrt(n)
        if (n % i == 0) return false;
    }
    return true;
}
```

### ✅ Factorial of a Number
Logic: `n! = 1 * 2 * ... * n`

```cpp
int factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}
```

### ✅ Even or Odd
```cpp
bool isEven(int n) {
    return (n % 2 == 0);
}
```

---

## 9️⃣ Scope: Local vs Global

| Type | Scope | Lifetime |
| :--- | :--- | :--- |
| **Local Variable** | Inside `{}` block. | Created when block starts, destroyed when block ends. |
| **Global Variable** | Outside all functions. | Accessible everywhere, lasts until program ends. |

### ❌ Common Mistake
```cpp
void sum(int a, int b) {
    int s = a + b; // 's' is local to sum()
}

int main() {
    // cout << s; // ❌ ERROR: 's' is not defined in main()
    return 0;
}
```

---

## 🔟 Summary & Memory Tricks

1.  **Declare before Call**: Always declare functions above `main()` or use a prototype.
2.  **Defaults go Right**: `(int a, int b=0)` is valid; `(int a=0, int b)` is NOT.
3.  **Return ≠ Print**: `return` gives a value back to the caller; `cout` just shows it on screen.
4.  **Pass by Reference (`&`)**: Use when you want to modify the original variable.
5.  **Guard Clauses**: Use `if (bad) return;` at the start of functions to reduce nesting.