[← Chapter 03](03-cpp-fundamentals-ch03-25-main-categories-of-operator.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 05 →](03-cpp-fundamentals-ch05-55-operator-classification-by.md)

---

# 40. Bitwise XOR

XOR produces `1` when the corresponding bits are different.

```text
0101
0011
----
0110
```

Therefore:

```cpp
5 ^ 3
```

gives:

```text
6
```

### XOR truth table

| A | B | A ^ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR becomes very important in DSA problems involving:

- unique elements
- duplicate cancellation
- bit manipulation
- subsets
- XOR tricks

---

# 41. Bitwise NOT `~`

`~` flips every bit of its operand.

```text
0 → 1
1 → 0
```

Example:

```cpp
int x = 5;

cout << ~x;
```

The exact result involves the representation of signed integers and should not be memorized using a simplistic "just flip the four visible bits" model.

For typical two's-complement systems:

```text
~x = -x - 1
```

so:

```text
~5 = -6
```

---

# 42. Left Shift `<<`

Left shift moves bits toward the left.

```cpp
5 << 1
```

Binary:

```text
0101
```

Shift left:

```text
1010
```

which represents:

```text
10
```

For suitable nonnegative values and within the relevant range:

```text
x << 1 ≈ x × 2
```

---

# 43. Right Shift `>>`

Right shift moves bits toward the right.

```cpp
10 >> 1
```

Binary:

```text
1010
```

After shifting:

```text
0101
```

Result:

```text
5
```

For suitable nonnegative values:

```text
x >> 1 ≈ x / 2
```

But be careful with signed negative values because right-shift behavior depends on the language rules and implementation details.

---

# 44. Unary Operators

## Definition

A **unary operator** operates on a single operand.

Example:

```cpp
-x
```

Here:

```text
-  → operator
x  → operand
```

Common unary operators include:

```text
+
-
++
--
!
~
```

But classification depends on context: operators such as `+`, `-`, `*`, `&`, and `<<` can have different meanings depending on how they are used.

---

# 45. Unary Plus and Minus

```cpp
int x = 10;

cout << +x; // 10
cout << -x; // -10
```

`-x` changes the sign of the value.

---

# 46. Increment Operator `++`

Increases a variable by 1.

```cpp
int x = 5;

x++;
```

Now:

```text
x = 6
```

There are two forms:

```cpp
++x;  // pre-increment
x++;  // post-increment
```

---

# 47. Pre-Increment

```cpp
int x = 5;

int y = ++x;
```

Execution:

```text
x = 5
     ↓
++x
     ↓
x = 6
     ↓
y = 6
```

Final:

```text
x = 6
y = 6
```

### Rule

> **Pre-increment: increment first, then use the value.**

---

# 48. Post-Increment

```cpp
int x = 5;

int y = x++;
```

Execution:

```text
x = 5
     ↓
use old value → y = 5
     ↓
increment x
     ↓
x = 6
```

Final:

```text
x = 6
y = 5
```

### Rule

> **Post-increment: use the old value first, then increment.**

---

# 49. Pre vs Post Increment

| Expression | What happens first? | Example result |
|---|---|---|
| `++x` | Increment | `y` gets new value |
| `x++` | Use old value | `y` gets old value |

Example:

```cpp
int x = 10;

cout << ++x;
```

Output:

```text
11
```

But:

```cpp
int x = 10;

cout << x++;
```

Output:

```text
10
```

Afterward:

```text
x = 11
```

---

# 50. Decrement Operator `--`

Decreases a variable by 1.

```cpp
int x = 5;

x--;
```

Now:

```text
x = 4
```

Just like increment, it has:

```cpp
--x;  // pre-decrement
x--;  // post-decrement
```

---

# 51. Pre-Decrement

```cpp
int x = 5;

int y = --x;
```

Final:

```text
x = 4
y = 4
```

The variable is decremented before its value is used.

---

# 52. Post-Decrement

```cpp
int x = 5;

int y = x--;
```

Final:

```text
x = 4
y = 5
```

The old value is used first, then the variable is decremented.

---

# 53. Assignment Operators

Assignment operators assign values to variables.

Basic assignment:

```cpp
=
```

Example:

```cpp
int x = 10;
```

Compound assignment operators:

| Operator | Meaning |
|---|---|
| `=` | Assign |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `%=` | Modulus and assign |
| `&=` | Bitwise AND and assign |
| `|=` | Bitwise OR and assign |
| `^=` | XOR and assign |
| `<<=` | Left shift and assign |
| `>>=` | Right shift and assign |

Example:

```cpp
int x = 10;

x += 5;
```

Equivalent to:

```cpp
x = x + 5;
```

Result:

```text
15
```

---

# 54. Conditional / Ternary Operator

The ternary operator is:

```cpp
condition ? value1 : value2
```

Example:

```cpp
int age = 20;

string result = (age >= 18) ? "Adult" : "Minor";
```

If condition is true:

```text
Adult
```

Otherwise:

```text
Minor
```

It is called the **ternary operator** because it operates on three expressions.

---
