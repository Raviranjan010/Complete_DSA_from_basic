[← Chapter 02](03-cpp-fundamentals-ch02-12-float.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 04 →](03-cpp-fundamentals-ch04-40-bitwise-xor.md)

---

# 25. Main Categories of Operators

C++ operators can broadly be classified into:

1. Arithmetic
2. Relational / Comparison
3. Logical
4. Assignment
5. Increment / Decrement
6. Bitwise
7. Conditional
8. Unary
9. Other/special operators

---

# 26. Arithmetic Operators

Arithmetic operators perform mathematical operations.

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus/remainder |
| `++` | Increment |
| `--` | Decrement |

Example:

```cpp
int a = 10;
int b = 3;

cout << a + b; // 13
cout << a - b; // 7
cout << a * b; // 30
cout << a / b; // 3
cout << a % b; // 1
```

---

# 27. Integer Division — VERY IMPORTANT

This is one of the most important concepts for DSA.

If both operands are integers:

```cpp
int a = 10;
int b = 3;

cout << a / b;
```

Output:

```text
3
```

Not:

```text
3.333333
```

Why?

Because both operands are integers, so the operation uses integer division.

Conceptually:

```text
10 / 3 = 3 remainder 1
```

The fractional part is discarded.

---

# 28. Floating-Point Division

If at least one operand is floating-point:

```cpp
double a = 10;
double b = 3;

cout << a / b;
```

Result is approximately:

```text
3.33333
```

Similarly:

```cpp
int a = 10;
double b = 3;

cout << a / b;
```

produces floating-point division.

### Remember

```text
int / int       → integer division
int / double    → floating-point result
double / int    → floating-point result
double / double → floating-point result
```

More generally, the exact result type follows C++'s usual arithmetic conversions.

---

# 29. Modulus `%`

The modulus operator gives the remainder of integer division.

```cpp
10 % 3
```

Result:

```text
1
```

Because:

```text
10 = 3 × 3 + 1
```

Another example:

```cpp
17 % 5
```

Result:

```text
2
```

### DSA applications

`%` is extremely important.

It is commonly used for:

- checking even/odd
- digit extraction
- circular arrays
- hashing
- cyclic indexing
- mathematical problems

Example:

```cpp
if (n % 2 == 0)
    cout << "Even";
else
    cout << "Odd";
```

---

# 30. Relational / Comparison Operators

These compare two values.

| Operator | Meaning |
|---|---|
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

Example:

```cpp
int a = 10;
int b = 20;

cout << (a < b);
```

Output:

```text
1
```

because:

```text
10 < 20
```

is true.

---

# 31. `=` vs `==`

This is one of the most common beginner mistakes.

### `=`

Assignment:

```cpp
x = 10;
```

Means:

> Put 10 into x.

### `==`

Comparison:

```cpp
x == 10
```

Means:

> Is x equal to 10?

Example:

```cpp
if (x == 10) {
    cout << "Yes";
}
```

Do not confuse:

```cpp
x = 10;
```

with:

```cpp
x == 10;
```

---

# 32. Logical Operators

Logical operators combine or modify conditions.

| Operator | Meaning |
|---|---|
| `&&` | AND |
| `||` | OR |
| `!` | NOT |

---

# 33. Logical AND `&&`

Both conditions must be true.

```cpp
int age = 20;

if (age >= 18 && age <= 60) {
    cout << "Valid";
}
```

Truth table:

| A | B | A && B |
|---|---|---|
| false | false | false |
| false | true | false |
| true | false | false |
| true | true | true |

---

# 34. Logical OR `||`

At least one condition must be true.

```cpp
if (marks >= 90 || attendance >= 90) {
    cout << "Eligible";
}
```

Truth table:

| A | B | A \|\| B |
|---|---|---|
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | true |

---

# 35. Logical NOT `!`

Reverses a boolean condition.

```cpp
bool isReady = true;

cout << !isReady;
```

Result:

```text
false
```

Conceptually:

```text
true  → ! → false
false → ! → true
```

---

# 36. Short-Circuit Evaluation

This is an important concept for DSA.

For:

```cpp
A && B
```

if `A` is false, C++ may not evaluate `B`.

For:

```cpp
A || B
```

if `A` is true, C++ may not evaluate `B`.

Example:

```cpp
if (ptr != nullptr && ptr->data == 10) {
    ...
}
```

The first condition:

```cpp
ptr != nullptr
```

is checked first.

If it is false, C++ does not evaluate:

```cpp
ptr->data
```

This can prevent invalid pointer access.

---

# 37. Bitwise Operators

Bitwise operators operate on the individual bits of integral values.

| Operator | Meaning |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left shift |
| `>>` | Right shift |

These are extremely important in advanced DSA, competitive programming, and low-level programming.

---

# 38. Binary Representation

Consider:

```text
5 = 0101
3 = 0011
```

### Bitwise AND

```text
0101
0011
----
0001
```

Therefore:

```cpp
5 & 3
```

gives:

```text
1
```

---

# 39. Bitwise OR

```text
0101
0011
----
0111
```

Therefore:

```cpp
5 | 3
```

gives:

```text
7
```

---
