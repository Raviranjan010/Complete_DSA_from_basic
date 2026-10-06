[← Chapter 04](03-cpp-fundamentals-ch04-40-bitwise-xor.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 06 →](03-cpp-fundamentals-ch06-62-final-mental-model.md)

---

# 55. Operator Classification by Number of Operands

Operators can also be classified based on the number of operands.

## Unary

One operand:

```cpp
-x
++x
!x
~x
```

## Binary

Two operands:

```cpp
a + b
a * b
a > b
a && b
```

## Ternary

Three operands:

```cpp
condition ? a : b
```

---

# 56. Operator Precedence

When multiple operators appear in one expression, C++ follows rules that determine which operations are performed first.

Example:

```cpp
int result = 2 + 3 * 4;
```

Multiplication happens before addition.

Therefore:

```text
3 × 4 = 12
2 + 12 = 14
```

Result:

```text
14
```

Not:

```text
20
```

---

# 57. Parentheses Remove Confusion

Instead of relying heavily on precedence:

```cpp
int result = 2 + (3 * 4);
```

Use parentheses when the expression may be difficult to read.

Example:

```cpp
if ((a > b) && (b > c)) {
    ...
}
```

This makes the logic clearer.

---

# 58. Common Mistakes

## Mistake 1 — Using `=` instead of `==`

❌

```cpp
if (x = 10)
```

This performs assignment.

Usually you wanted:

```cpp
if (x == 10)
```

---

## Mistake 2 — Expecting decimal output from integer division

❌

```cpp
int a = 5;
int b = 2;

cout << a / b;
```

Output:

```text
2
```

If you need:

```text
2.5
```

use:

```cpp
cout << static_cast<double>(a) / b;
```

---

## Mistake 3 — Thinking casting rounds

```cpp
double x = 9.99;

int y = static_cast<int>(x);
```

Result:

```text
9
```

It does not round to 10.

---

## Mistake 4 — Confusing `%` with percentage

```cpp
17 % 5
```

does not mean percentage.

It means:

> remainder after integer division.

Result:

```text
2
```

---

## Mistake 5 — Confusing `&&` and `&`

```cpp
&&
```

is **logical AND**.

```cpp
&
```

is **bitwise AND**.

Example:

```cpp
if (a > 0 && b > 0)
```

uses logical AND.

But:

```cpp
a & b
```

uses bitwise AND.

---

## Mistake 6 — Confusing `||` and `|`

```cpp
||
```

→ logical OR

```cpp
|
```

→ bitwise OR

---

## Mistake 7 — Confusing pre and post increment

```cpp
int x = 5;

cout << ++x;
```

prints:

```text
6
```

while:

```cpp
int x = 5;

cout << x++;
```

prints:

```text
5
```

but afterward:

```text
x = 6
```

---

## Mistake 8 — Assuming all data types have fixed sizes

Don't blindly assume:

```text
int = 4 bytes
long = 8 bytes
```

Always remember that exact sizes depend on the implementation.

Use:

```cpp
sizeof(type)
```

when the actual size matters.

---

# 59. Quick Comparison Table

| Concept | Meaning | Example |
|---|---|---|
| Variable | Named storage/object | `int x = 10;` |
| Identifier | Name used for a program entity | `x` |
| Data type | Defines type of value/object | `int` |
| Declaration | Introduces a variable | `int x;` |
| Initialization | Gives initial value | `int x = 10;` |
| Assignment | Changes/stores a value | `x = 20;` |
| Type conversion | Changes value to another type | `double → int` |
| Operator | Performs an operation | `+` |
| Operand | Value operated on | `a` in `a+b` |
| Unary | One operand | `++x` |
| Binary | Two operands | `a+b` |
| Ternary | Three expressions | `a ? b : c` |

---

# 60. Operator Cheat Sheet

| Category | Operators |
|---|---|
| Arithmetic | `+ - * / %` |
| Increment/Decrement | `++ --` |
| Relational | `< > <= >= == !=` |
| Logical | `&& || !` |
| Bitwise | `& \| ^ ~ << >>` |
| Assignment | `= += -= *= /= %= &= \|= ^= <<= >>=` |
| Conditional | `?:` |

---

# 61. DSA-Relevant Concepts You Must Master

Before moving deeply into DSA, make sure these are completely clear:

### Essential

```text
Variables
↓
Data Types
↓
Input / Output
↓
Operators
↓
Conditions
↓
Loops
↓
Functions
↓
Arrays
↓
Strings
↓
Pointers
↓
References
↓
Dynamic Memory
↓
Structures / Classes
```

Especially focus on:

### 1. Integer division

```cpp
7 / 2 = 3
```

### 2. Modulus

```cpp
7 % 2 = 1
```

### 3. Type casting

```cpp
static_cast<double>(a)
```

### 4. Increment/decrement

```cpp
++i
i++
--i
i--
```

### 5. Comparison

```cpp
==
!=
<
>
<=
>=
```

### 6. Logical operations

```cpp
&&
||
!
```

### 7. Bit manipulation

```cpp
&
|
^
~
<<
>>
```

These concepts will appear repeatedly when you study:

- Arrays
- Searching
- Sorting
- Linked Lists
- Stacks
- Queues
- Trees
- Graphs
- Recursion
- Dynamic Programming
- Bit Manipulation
- Competitive Programming

---
