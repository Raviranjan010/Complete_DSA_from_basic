[← Chapter 01](01-getting-started-basics-ch01-00-start-here-absolute-basics.md) · [Chapter Index](01-getting-started-basics.md) · [Module Overview](../README.md) · [Chapter 03 →](01-getting-started-basics-ch03-00-c-prerequisites-complete-no.md)

---

# Formula Approach: Time O(1), Space O(1)
def formula_sum(n):
    return n * (n + 1) // 2
```
</details>

<details>
<summary>⚡ C++ Solution</summary>

```cpp
// Loop Approach: Time O(N), Space O(1)
int loopSum(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

// Formula Approach: Time O(1), Space O(1)
int formulaSum(int n) {
    return n * (n + 1) / 2;
}
```
</details>


---

## 📋 Step-by-Step Dry Run Example

### Sum of First N Numbers (`n = 4`)

#### Loop Approach:
- **Input:** `n = 4`
- **Initial State:** `sum = 0`
- **Iteration 1 (`i = 1`):** `sum = 0 + 1 = 1`
- **Iteration 2 (`i = 2`):** `sum = 1 + 2 = 3`
- **Iteration 3 (`i = 3`):** `sum = 3 + 3 = 6`
- **Iteration 4 (`i = 4`):** `sum = 6 + 4 = 10`
- **Loop Terminates:** `i = 5 > n (4)`
- **Result:** `10` ✅

#### Formula Approach:
- **Formula:** `n * (n + 1) / 2`
- **Step 1:** `4 + 1 = 5`
- **Step 2:** `4 * 5 = 20`
- **Step 3:** `20 / 2 = 10`
- **Result:** `10` ✅ (Executes in 1 step regardless of $N$)

---

## 🎓 Viva Questions & Answers

### Q1: What is the primary difference between Stack memory and Heap memory?
**Answer:**
- **Stack Memory:** Used for static memory allocation, function call frames, and primitive local variables. Memory is allocated and deallocated automatically in a LIFO order. Access is extremely fast.
- **Heap Memory:** Used for dynamic memory allocation (objects, dynamic arrays). Access is slower because data is referenced via memory pointers/addresses on the stack, and memory must be managed manually or by a Garbage Collector.

### Q2: Why do array indices start at 0 instead of 1?
**Answer:**
Array indices represent a memory **offset** from the starting base address. The address of $arr[i]$ is calculated as:
$$\text{Address}(arr[i]) = \text{Base Address} + (i \times \text{Size of Type})$$
For index 0, offset is $0 \times \text{Size} = 0$, pointing directly to the base address. Zero-based indexing removes the extra subtraction step $(i - 1)$ during address calculation.

### Q3: What is the difference between Big-O, Big-Omega ($\Omega$), and Big-Theta ($\Theta$)?
**Answer:**
- **Big-O ($O$):** Upper bound of growth rate (worst-case scenario).
- **Big-Omega ($\Omega$):** Lower bound of growth rate (best-case scenario).
- **Big-Theta ($\Theta$):** Tight bound of growth rate (where worst-case and best-case match or bound the growth rate tightly).

### Q4: What is the difference between Auxiliary Space and Total Space Complexity?
**Answer:**
- **Total Space Complexity:** Includes both the input data size + extra memory used by the algorithm.
- **Auxiliary Space:** Measures **only the extra or temporary memory** allocated by the algorithm outside the original input. In DSA interviews, Auxiliary Space is usually what interviewers evaluate.

### Q5: In the formula `n * (n + 1) / 2`, what potential bug can occur for large values of `n` in languages like C++ or Java?
**Answer:**
For large $n$ (e.g., $n = 10^5$), $n \times (n + 1)$ evaluates to $\approx 10^{10}$, which exceeds the maximum value of a 32-bit signed integer ($2 \times 10^9$). This leads to **Integer Overflow**. To avoid this, cast to `long` (Java) or `long long` (C++): `(long long)n * (n + 1) / 2`.

---

> 👉 Once these basics feel clear, open `01-Git-And-GitHub.md` to learn how to store and track your code safely! 💪



---

## Supplementary Reference from 01_introcution.md

## Introduction to C++ Programming

### Boilerplate Code
#include <iostream>
using namespace std;

int main() {
    // Prints a welcome message to the console
    cout << "Welcome to C++ programming!" << endl;
    return 0;
}

This is a simple C++ program that includes the necessary headers, uses the standard namespace, and contains a `main` function that prints a welcome message to the console.

*   `#include <iostream>`: Includes the iostream library for input and output operations.
*   `using namespace std;`:  Allows the use of standard library features without the `std::` prefix.
*   `int main()`: The main function, where program execution begins.  The `cout` statement outputs the welcome message, and `endl` inserts a newline and flushes the output buffer.
*   `cout`:  The standard output stream object.
*   `endl`: Inserts a newline character and flushes the output buffer.

### Macros
Macros are symbolic names defined using the `#define` directive. They are processed by the preprocessor before compilation.
```cpp
#define PI 3.14159
#define SQUARE(x) ((x) * (x))
```
// // To run the compiled program, use the following command:
// // ./introcution
// // This will output: Welcome to C++ programming!

// Note: Ensure you have a C++ compiler installed to compile and run the program.

// you will get output with '%' sign because while saving the file in some editors like vim, it shows '%' at the end of the file to indicate that the file has been modified but not yet saved. we can print the output without '%' sign by saving the file before running the program.
### Data Types
// // float
// // double
// // char
// // bool
// // void
// // long
// // short
// // long long
### Variables
// Examples of variable declarations and initializations in C++:
// int age = 25;
// float pi = 3.14
// char grade = 'A';
// bool isStudent = true;
// double largeNumber = 1234567890.12345;
// long population = 7800000000;
// short smallNumber = 32000;
// long long bigNumber = 1234567890123456789;

Variables are used to store data that can be manipulated and accessed throughout the program. They are named memory locations holding values of specific data types.

*   `int`: Integer numbers (e.g., 10, -5).
*   `float`: Single-precision floating-point numbers (e.g., 3.14, -2.5).
*   `double`: Double-precision floating-point numbers (e.g., 3.14159265359, -2.5).
*   `char`: Single characters (e.g., 'A', 'z').
*   `bool`: Boolean values (true or false).
*   `void`: Represents the absence of a type.
*   `long`: Larger range integer.
*   `short`: Smaller range integer.
*   `long long`: Even larger range integer.

**Note:** Variable names must start with a letter or underscore, cannot contain spaces or special characters (except underscores), and are case-sensitive. Always initialize variables to avoid undefined behavior.

#### Uninitialized Variables

If you try to print an uninitialized variable, it may lead to undefined behavior.
```cpp
#include <iostream>
using namespace std;
int main(){
    int a; // uninitialized variable
    cout << a << endl; // may print garbage value
    return 0;
}

```
#### Constant Variables

```cpp
using namespace std;
int main() {
    const int a = 10; // constant variable
    cout << a << endl; // prints 10
}

// Note: In C++, local variables are not automatically initialized, so they may contain garbage values if not explicitly initialized.
// Macros didn't occupy any space in memory but constants do occupy space in memory.
// Note: It is important to include the return statement in the main function to indicate the program's exit status to the operating system.
```
Constant variables' values cannot be changed once assigned. They are declared using the `const` keyword.  They ensure a value remains unchanged throughout the program.

### Combining Macros and Constants
```cpp
#include<iostream>
#define CONSTANT_VALUE 100
#define ll long long
using namespace std;
int main(){
    const int a=10; // constant variable
    cout<<a<<endl; // prints 10
    cout<<CONSTANT_VALUE<<endl; // prints 100
    ll bigNumber = 10000000000;
    cout<<bigNumber<<endl; // prints 10000000000
    return 0;
}
```
### Type Conversion and Promotion
// Result of operating on two data types in C++ depends on the types involved and the operators used. C++ follows specific rules for type promotion and conversion during operations.
// // Result of operating two data types in C++ depends on the types involved in the operation. C++ follows certain rules for type promotion and conversion when performing operations between different data types. Here are some general guidelines:
// bool -> char -> int -> long -> float -> double -> long double


// If the operation involves a mix of signed and unsigned types, C++ will convert the signed type to unsigned if the unsigned type has a larger range. This can lead to unexpected results if not handled carefully.
// Example:
// int a = 10;
// float b = 5.5;
// auto result = a + b; // result will be of type float with value 15
// It is important to be aware of these type promotion rules to avoid unintended consequences when performing operations on different data types.

When operating on different data types, C++ promotes the smaller type to the larger type. For example: `int + float -> float`.  Be aware of type promotion rules to avoid unintended consequences.

---

# 🔢 Number Systems & Decimal Logic

Understanding number systems is foundational, especially when working with low-level concepts like memory and data representation. Computers fundamentally operate in binary.

## 1️⃣ What is a Number System?
A number system defines how numbers are represented using digits and a base (radix).

| Number System | Base | Digits Used | Example |
| :------------ | :--- | :---------- | :------ |
| **Decimal**   | 10   | 0–9         | 12, 99, 105 |
| **Binary**    | 2    | 0, 1        | 101, 1100 |
| **Octal**     | 8    | 0–7         | 17, 24  |
| **Hexadecimal** | 16   | 0–9, A–F    | 1A, F2, B5 |

## 2️⃣ Decimal Number System (Base-10)
The decimal system is the number system we use daily. It uses 10 unique digits (0–9). Each digit's position in a number represents a power of 10.

### Example: Breakdown of `739`
*   `7` is in the hundreds place: $7 \times 10^2 = 700$
*   `3` is in the tens place: $3 \times 10^1 = 30$
*   `9` is in the units place: $9 \times 10^0 = 9$
*   **Total**: $700 + 30 + 9 = 739$

### Why do computers use Binary?
Computers are built from transistors, which act as tiny switches. These switches have only two stable states:
*   **ON** (High Voltage) = **1**
*   **OFF** (Low Voltage) = **0**
This inherent two-state nature makes binary (base-2) the most natural and efficient number system for computers.


---

## Supplementary Reference from 00_notes.md
