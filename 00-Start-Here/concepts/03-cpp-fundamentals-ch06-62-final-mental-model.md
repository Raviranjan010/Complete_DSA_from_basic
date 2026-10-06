[← Chapter 05](03-cpp-fundamentals-ch05-55-operator-classification-by.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 07 →](03-cpp-fundamentals-ch07-9-how-else-if-works.md)

---

# 62. Final Mental Model

Think of a C++ program like this:

```text
                    C++ PROGRAM
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      VARIABLES       FUNCTIONS       OBJECTS
          │
          ↓
     DATA TYPES
          │
     ┌────┼────┐
     ↓    ↓    ↓
    int double char
     │
     ↓
    VALUES
     │
     ↓
  OPERATORS
     │
 ┌───┼───────────────┐
 ↓   ↓       ↓       ↓
+ - * /    < > ==   && ||
              │
              ↓
          CONDITIONS
              │
              ↓
            LOOPS
              │
              ↓
          DATA STRUCTURES
              │
              ↓
              DSA
```

The important point is that **DSA is not isolated from C++ fundamentals**.

When you later write:

```cpp
for (int i = 0; i < n; i++) {
    if (arr[i] % 2 == 0) {
        cout << arr[i] << "\n";
    }
}
```

you are simultaneously using:

- variable declaration
- `int`
- initialization
- comparison
- increment
- loop
- array indexing
- modulus
- equality comparison
- `if`
- output

So mastering these fundamentals will make the actual DSA concepts much easier.

---

## Supplementary Reference from 02_Cpp_Control_Flow_Conditional_Statements_DSA_Notes.md

# C++ Control Flow & Conditional Statements

## DSA Foundation Notes

These notes cover **conditional statements, control flow, `switch-case`,
ternary operator, loop-control statements, exception handling basics,
and ASCII characters**.

------------------------------------------------------------------------

# 1. What is Control Flow?

### Definition

**Control flow** is the order in which statements of a program are
executed.

Normally, a C++ program executes statements from:

``` text
top → bottom
```

But real programs need to make decisions, repeat operations, skip
operations, or exit from a section of code.

For example:

``` text
If marks >= 40
    Student passes
Otherwise
    Student fails
```

C++ provides control-flow constructs that allow us to:

-   make decisions
-   repeat operations
-   skip operations
-   terminate loops
-   return from functions
-   jump to labels
-   handle exceptions

For DSA, conditional statements are extremely important because almost
every algorithm contains decision-making.

------------------------------------------------------------------------

# 2. Decision-Making Statements

The main decision-making constructs are:

``` text
if
if-else
else-if ladder
nested if
switch-case
ternary operator
```

### Important terminology correction

It is better to distinguish between:

-   `if`, `else`, `else if` → conditional/control-flow statements
-   `switch`, `case`, `default` → selection/control-flow constructs
-   `?:` → conditional/ternary operator

------------------------------------------------------------------------

# 3. `if` Statement

## Definition

The `if` statement executes a block of code **only when its condition
evaluates to true**.

### Syntax

``` cpp
if (condition) {
    // statements
}
```

### Example

``` cpp
int age = 20;

if (age >= 18) {
    cout << "Adult";
}
```

### Dry Run

``` text
age = 20

20 >= 18 ?
     ↓
   true
     ↓
execute if block
     ↓
"Adult"
```

Output:

``` text
Adult
```

If:

``` cpp
int age = 15;
```

then:

``` text
15 >= 18 → false
```

The body of `if` is skipped.

------------------------------------------------------------------------

# 4. What is a Condition?

A **condition** is an expression whose result can be interpreted as true
or false.

Example:

``` cpp
age >= 18
```

The result is either:

``` text
true
```

or:

``` text
false
```

Conditions commonly use relational operators:

``` cpp
<
>
<=
>=
==
!=
```

and logical operators:

``` cpp
&&
||
!
```

Example:

``` cpp
if (age >= 18 && age <= 60) {
    cout << "Valid";
}
```

------------------------------------------------------------------------

# 5. Boolean Conditions in C++

C++ does not require an `if` condition to literally have type `bool`.

For example:

``` cpp
if (5) {
    cout << "Hello";
}
```

This executes because a nonzero value is treated as true.

Conceptually:

``` text
0        → false
non-zero → true
```

Example:

``` cpp
if (0) {
    cout << "A";
}
```

Nothing is printed.

But:

``` cpp
if (-10) {
    cout << "B";
}
```

prints:

``` text
B
```

This is useful when reading DSA code.

------------------------------------------------------------------------

# 6. `if-else`

## Definition

`if-else` provides two possible execution paths.

### Syntax

``` cpp
if (condition) {
    // true block
}
else {
    // false block
}
```

### Example

``` cpp
int number = 7;

if (number % 2 == 0) {
    cout << "Even";
}
else {
    cout << "Odd";
}
```

### Dry Run

``` text
number = 7

7 % 2 == 0
      ↓
    1 == 0
      ↓
    false
      ↓
else executes
      ↓
    "Odd"
```

Output:

``` text
Odd
```

------------------------------------------------------------------------

# 7. `else`

`else` is associated with an `if`.

Invalid:

``` cpp
else {
    cout << "Hello";
}
```

Correct:

``` cpp
if (condition) {
    ...
}
else {
    ...
}
```

### Important

You cannot have an independent `else` without a corresponding `if`.

------------------------------------------------------------------------

# 8. `else if`

When there are multiple possible conditions, use an **else-if ladder**.

### Syntax

``` cpp
if (condition1) {

}
else if (condition2) {

}
else if (condition3) {

}
else {

}
```

### Example

``` cpp
int marks = 75;

if (marks >= 90) {
    cout << "A";
}
else if (marks >= 80) {
    cout << "B";
}
else if (marks >= 70) {
    cout << "C";
}
else {
    cout << "D";
}
```

Output:

``` text
C
```

------------------------------------------------------------------------
