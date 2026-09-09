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