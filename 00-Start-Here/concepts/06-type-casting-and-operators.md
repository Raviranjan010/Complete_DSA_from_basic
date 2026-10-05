## Operators in C++

### What is an Operator?
An operator is a symbol that performs an operation on one or more operands (values or variables).

```cpp
a + b   // '+' is an operator
```

### 1. Assignment Operators
Assignment operators are used to assign or update values of variables.

| Operator | Description | Example | Equivalent |
| :--- | :--- | :--- | :--- |
| `=` | Assign | `a = 5` | `a = 5` |
| `+=` | Add & assign | `a += 2` | `a = a + 2` |
| `-=` | Subtract & assign | `a -= 2` | `a = a - 2` |
| `*=` | Multiply & assign | `a *= 2` | `a = a * 2` |
| `/=` | Divide & assign | `a /= 2` | `a = a / 2` |
| `%=` | Modulus & assign | `a %= 2` | `a = a % 2` |

> **⚠️ Important**: `**=` (exponentiation) and `//=` (floor division) are **NOT** valid in C++ (they are Python operators).

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 7;
    int b = a;
    cout << b << endl;   // Output: 7

    a += 2;
    cout << a << endl;   // Output: 9
    return 0;
}
```

### 2. Arithmetic Operators
Used for mathematical calculations.

#### (A) Binary Arithmetic Operators (Two Operands)

| Operator | Operation | Example (`a=5, b=2`) | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `a + b` | `7` |
| `-` | Subtraction | `a - b` | `3` |
| `*` | Multiplication | `a * b` | `10` |
| `/` | Division | `a / b` | `2` |
| `%` | Modulus | `a % b` | `1` |

> **Note**:
> *   `/` gives the quotient. Integer division truncates decimals (`5/2 = 2`).
> *   `%` gives the remainder. It works **only** with integers.

#### (B) Unary Arithmetic Operators (One Operand)

| Operator | Meaning |
| :--- | :--- |
| `++` | Increment (Add 1) |
| `--` | Decrement (Subtract 1) |

#### Pre-Increment vs Post-Increment

| Type | Syntax | Behavior |
| :--- | :--- | :--- |
| **Pre-Increment** | `++a` | Increment **first**, then use the value. |
| **Post-Increment** | `a++` | Use the value **first**, then increment. |

```cpp
int c = 7;
cout << ++c << endl; // Output: 8 (Incremented first)
cout << c++ << endl; // Output: 8 (Printed first, then incremented to 9)
cout << c-- << endl; // Output: 9 (Printed first, then decremented to 8)
cout << --c << endl; // Output: 7 (Decremented first)
```

#### 🔹 Tricky Interview Question
```cpp
int d = 7;
int e = d++;
// Result: e = 7, d = 8 (Post-increment: assign old d to e, then increment d)

d = 7;
e = ++d;
// Result: e = 8, d = 8 (Pre-increment: increment d, then assign to e)
```

### 3. Relational Operators
Used to compare two values. They return `true` (1) or `false` (0).

| Operator | Meaning | Example (`a=4, b=6`) | Result |
| :--- | :--- | :--- | :--- |
| `==` | Equal to | `a == b` | `0` (false) |
| `!=` | Not equal | `a != b` | `1` (true) |
| `>` | Greater than | `a > b` | `0` (false) |
| `<` | Less than | `a < b` | `1` (true) |
| `>=` | Greater than or equal | `a >= b` | `0` (false) |
| `<=` | Less than or equal | `a <= b` | `1` (true) |

### 4. Logical Operators
Used to combine conditions.

| Operator | Name | Description |
| :--- | :--- | :--- |
| `&&` | Logical AND | True if **both** are true. |
| `\|\|` | Logical OR | True if **at least one** is true. |
| `!` | Logical NOT | Reverses the boolean value. |

#### Truth Tables

**AND (`&&`)**
| A | B | Result |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

**OR (`||`)**
| A | B | Result |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

**NOT (`!`)**
| A | Result |
| :--- | :--- |
| 1 | 0 |
| 0 | 1 |

```cpp
int a = 33, b = 44;
// In C++, non-zero is true, 0 is false.
cout << (a && b) << endl; // Output: 1 (true && true)
cout << (a || b) << endl; // Output: 1
cout << (!a) << endl;     // Output: 0
```

#### 🔹 Short-Circuit Evaluation
*   **AND (`&&`)**: If the first operand is `false`, the second is **not evaluated** (result is definitely false).
    *   `false && function()` -> `function()` is not called.
*   **OR (`||`)**: If the first operand is `true`, the second is **not evaluated** (result is definitely true).
    *   `true || function()` -> `function()` is not called.

### 5. Operator Precedence
Determines the order in which operators are evaluated.
*   `*`, `/`, `%` have higher precedence than `+`, `-`.

```cpp
int x = 5 + 2 * 3;
// Step 1: 2 * 3 = 6
// Step 2: 5 + 6 = 11
// Result: 11
```

### Summary & Common Mistakes

#### Common Mistakes
*   ❌ Using `=` (assignment) instead of `==` (comparison).
*   ❌ Expecting `%` to work with floats (integers only).
*   ❌ Forgetting integer division (`10/3 = 3`).
*   ❌ Confusing `++a` (pre) and `a++` (post).

#### Interview Questions
1.  **Difference between `=` and `==`?**
    *   `=` assigns, `==` compares.
2.  **Output of `cout << 10 / 3;`?**
    *   `3`.
3.  **Output of `cout << (5 && 0);`?**
    *   `0` (true AND false is false).

---

## Supplementary Reference from 02_Type_Casting.md

## Type Casting in C++

Type casting is the process of converting one data type into another. In C++, this can happen automatically (implicit) or manually (explicit).

### 1. Implicit Type Casting (Automatic)
Also known as type promotion. This happens automatically when a smaller data type is converted to a larger data type to prevent data loss, or when types are mixed in an expression.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    float b = a; // int -> float automatically
    cout << b << endl; // Output: 10

    char c = 'A';
    int x = c + 1; // char -> int automatically (ASCII value used)
    cout << x << endl; // Output: 66
    return 0;
}
```

*   **Type Promotion**: Small data types (like `char`, `short`) are promoted to `int` during arithmetic operations.
*   **Hierarchy**: `bool` -> `char` -> `int` -> `long` -> `float` -> `double` -> `long double`.

### 2. Explicit Type Casting (Manual)
This is when the programmer manually converts one type to another. This is necessary when converting larger types to smaller types (which might cause data loss) or when specific arithmetic behavior is needed.

#### C-Style Casting
Syntax: `(type) expression`

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 45;
    float b = 23.3;

    cout << (int)b << endl;          // Output: 23 (Decimal part discarded)
    cout << (float)10 / 3 << endl;   // Output: 3.33333 (Floating point division)
    cout << (char)('A' + 4) << endl; // Output: E (65 + 4 = 69 -> 'E')
    return 0;
}
```

*   `(int)b`: Converts 23.3 to 23. The decimal part is truncated, not rounded.
*   `(float)10 / 3`: Converts integer 10 to 10.0, forcing floating-point division. Integer division `10/3` would result in `3`.

#### C++ Style Casting
C++ introduces specific casting operators for safer conversions.

*   `static_cast`: Safe numeric conversion (e.g., `float` to `int`).
*   `dynamic_cast`: Used for runtime polymorphism.
*   `const_cast`: Used to remove `const` qualification.
*   `reinterpret_cast`: Low-level memory casting.

```cpp
float x = 10.7;
int y = static_cast<int>(x); // y becomes 10
```

### 3. Character Arithmetic & ASCII
Characters in C++ are stored internally as ASCII integer values. When arithmetic is performed on `char`, it is implicitly converted to `int`.

```cpp
cout << ('A' + 1) << endl;   // Output: 66
cout << ('A' + 0) << endl;   // Output: 65
cout << ('b' + 0) << endl;   // Output: 98
```

*   **'A'**: ASCII value 65.
*   **'b'**: ASCII value 98.
*   **'A' + 1**: 65 + 1 = 66. Since the result is an `int`, it prints 66.

### 4. Boolean Type Casting
Boolean values are treated as integers in arithmetic expressions.

```cpp
cout << ((bool)3 + 2) << endl; // Output: 3
```

*   `bool(0)` is `false` (0).
*   `bool(non-zero)` is `true` (1).
*   In the example: `(bool)3` becomes `true` (1). `1 + 2 = 3`.

### 5. Mixed Data Types & Common Errors

#### Valid Mixed Arithmetic
```cpp
cout << (22.2 + 3 + 'A') << endl; // Output: 90.2
```
*   'A' is promoted to 65.
*   22.2 (double) + 3 (int) + 65 (int) -> Result is `double` (90.2).

#### Invalid String Arithmetic
```cpp
// cout << (22.2 + 3 + "A") << endl; // ERROR
```
*   `'A'` (Single Quotes): Character literal (char). Stored as ASCII number. Arithmetic allowed.
*   `"A"` (Double Quotes): String literal. Stored as a memory address (`const char*`). You cannot add numbers directly to a string pointer in this way.

### Summary Table

| Expression | Type | Explanation |
| :--- | :--- | :--- |
| `'A'` | `char` | Character 'A' (ASCII 65) |
| `"A"` | `const char*` | String containing "A" and null terminator |
| `(int)23.9` | `int` | 23 (Truncated) |
| `10 / 3` | `int` | 3 (Integer division) |
| `10.0 / 3` | `double` | 3.3333... (Float division) |