[← Chapter 09](03-cpp-fundamentals-ch09-35-character-to-integer-conver.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 11 →](03-cpp-fundamentals-ch11-c-syntax-for-dsa-your-cheat-sh.md)

---

# 50. DSA Pattern: Conditional Filtering

Suppose:

``` cpp
int arr[] = {10, 25, 30, 45, 50};
```

Print only even numbers:

``` cpp
for (int i = 0; i < 5; i++) {

    if (arr[i] % 2 == 0) {
        cout << arr[i] << " ";
    }
}
```

Output:

``` text
10 30 50
```

Conceptually:

``` text
array
  ↓
loop
  ↓
condition
  ↓
modulus
  ↓
comparison
  ↓
output
```

This pattern appears constantly in DSA.

------------------------------------------------------------------------

# 51. DSA Pattern: Find Maximum

``` cpp
int arr[] = {10, 40, 20, 80, 30};

int maximum = arr[0];

for (int i = 1; i < 5; i++) {

    if (arr[i] > maximum) {
        maximum = arr[i];
    }
}

cout << maximum;
```

Output:

``` text
80
```

The key decision is:

``` cpp
if (arr[i] > maximum)
```

This simple pattern becomes the foundation for many array problems.

------------------------------------------------------------------------

# 52. DSA Pattern: Character Classification

``` cpp
char ch;

cin >> ch;

if (ch >= 'A' && ch <= 'Z') {
    cout << "Uppercase";
}
else if (ch >= 'a' && ch <= 'z') {
    cout << "Lowercase";
}
else if (ch >= '0' && ch <= '9') {
    cout << "Digit";
}
else {
    cout << "Special character";
}
```

This combines:

-   input
-   character data
-   ASCII ranges
-   relational operators
-   `if`
-   `else if`
-   `else`

------------------------------------------------------------------------

# 53. Important Mental Models

## `if`

``` text
If condition is true
       ↓
execute block
```

## `if-else`

``` text
condition
 /      \
true    false
 ↓        ↓
if      else
```

## `else-if`

``` text
condition 1?
 ↓
condition 2?
 ↓
condition 3?
 ↓
else
```

## `switch`

``` text
expression
    ↓
case 1?
case 2?
case 3?
    ↓
default
```

## Ternary

``` text
condition ? true_value : false_value
```

## `break`

``` text
EXIT
```

## `continue`

``` text
SKIP CURRENT ITERATION
```

## `return`

``` text
EXIT FUNCTION
```

------------------------------------------------------------------------

# 54. Quick Revision Sheet

### Conditional Statements

``` cpp
if
if-else
else if
nested if
switch-case
```

### Conditional Operator

``` cpp
condition ? expression1 : expression2;
```

### Loop Control

``` cpp
break
continue
```

### Function Control

``` cpp
return
```

### Exception Handling

``` cpp
try
catch
throw
```

### Character Ranges

``` text
'0' → 48
'9' → 57

'A' → 65
'Z' → 90

'a' → 97
'z' → 122
```

### Escape Characters

``` text
\n → newline
\t → horizontal tab
\r → carriage return
\b → backspace
\0 → null character
```

------------------------------------------------------------------------

# 55. Final Comparison

  Construct           Purpose
  ------------------- -----------------------------------------------------------
  `if`                Execute code when condition is true
  `else`              Execute alternative when previous `if` condition is false
  `else if`           Test additional conditions
  Nested `if`         Put one decision inside another
  `switch`            Select based on a discrete expression value
  `case`              Specify a possible switch value
  `default`           Handle unmatched switch values
  `break`             Exit nearest loop/switch
  `continue`          Skip current loop iteration
  `return`            Exit a function and optionally return a value
  `goto`              Jump to a label
  `?:`                Simple conditional expression
  `try/catch/throw`   Exception handling

------------------------------------------------------------------------

# 56. What You Must Master Before Moving to DSA

Make sure these are completely clear:

``` text
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
Data Structures
    ↓
Algorithms
```

Especially master:

``` text
if / else
else-if
switch
ternary
break
continue
integer vs character
ASCII
'\n' vs '\0'
'0' vs 0
'0' vs '\0'
&& vs &
|| vs |
== vs =
```

These concepts will repeatedly appear in:

-   Arrays
-   Searching
-   Sorting
-   Linked Lists
-   Stacks
-   Queues
-   Trees
-   Graphs
-   Recursion
-   Dynamic Programming
-   Bit Manipulation
-   Competitive Programming


---

## Supplementary Reference from Cpp-Basics.md
