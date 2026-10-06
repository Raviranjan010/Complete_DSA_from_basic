[← Chapter 07](03-cpp-fundamentals-ch07-9-how-else-if-works.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 09 →](03-cpp-fundamentals-ch09-35-character-to-integer-conver.md)

---

# 21. Can `switch` Replace Every `if-else`?

**No.**

For example:

``` cpp
if (age >= 18) {
    cout << "Adult";
}
```

is naturally expressed with `if`.

`switch` is designed around matching an expression against case labels,
not arbitrary relational conditions.

Do not force `switch` into situations where `if` is clearer.

------------------------------------------------------------------------

# 22. Ternary Operator `?:`

## Definition

The **conditional operator**, also called the **ternary operator**,
evaluates one of two expressions depending on a condition.

### Syntax

``` cpp
condition ? expression1 : expression2;
```

Meaning:

``` text
condition true
      ↓
expression1

condition false
      ↓
expression2
```

------------------------------------------------------------------------

# 23. Basic Ternary Example

``` cpp
int age = 20;

string result = (age >= 18) ? "Adult" : "Minor";
```

Since:

``` text
20 >= 18 → true
```

we get:

``` text
result = "Adult"
```

------------------------------------------------------------------------

# 24. Ternary vs `if-else`

### `if-else`

``` cpp
if (age >= 18) {
    result = "Adult";
}
else {
    result = "Minor";
}
```

### Ternary

``` cpp
result = (age >= 18) ? "Adult" : "Minor";
```

Use ternary when the logic is **simple and produces a value**.

Avoid deeply nested ternary expressions because they reduce readability.

------------------------------------------------------------------------

# 25. Ternary Is an Expression

The ternary operator produces a value.

Example:

``` cpp
int maximum = (a > b) ? a : b;
```

This is why it can be directly assigned to a variable.

------------------------------------------------------------------------

# 26. Finding Maximum of Two Numbers

``` cpp
int a = 10;
int b = 20;

int maximum = (a > b) ? a : b;

cout << maximum;
```

Output:

``` text
20
```

This pattern appears frequently in DSA.

------------------------------------------------------------------------

# 27. `break`

## Definition

`break` terminates the nearest enclosing loop or `switch`.

Example:

``` cpp
for (int i = 1; i <= 10; i++) {

    if (i == 5) {
        break;
    }

    cout << i << " ";
}
```

Output:

``` text
1 2 3 4
```

### Meaning

``` text
break
  ↓
stop loop completely
```

It does **not** mean "skip this iteration."

------------------------------------------------------------------------

# 28. `continue`

## Definition

`continue` skips the remaining statements of the current loop iteration
and proceeds to the next iteration.

Example:

``` cpp
for (int i = 1; i <= 5; i++) {

    if (i == 3) {
        continue;
    }

    cout << i << " ";
}
```

Output:

``` text
1 2 4 5
```

### Meaning

``` text
continue
   ↓
skip current iteration
   ↓
go to next iteration
```

### Important correction

`continue` must be used within an iteration statement such as:

-   `for`
-   `while`
-   `do-while`

It cannot be used as an independent statement outside a loop.

------------------------------------------------------------------------

# 29. `break` vs `continue`

Memorize this:

``` text
BREAK
 ↓
Terminate the loop/switch

CONTINUE
 ↓
Skip current loop iteration
 ↓
Continue with next iteration
```

Example:

``` cpp
for (int i = 1; i <= 5; i++) {

    if (i == 3)
        continue;

    cout << i << " ";
}
```

Output:

``` text
1 2 4 5
```

But:

``` cpp
for (int i = 1; i <= 5; i++) {

    if (i == 3)
        break;

    cout << i << " ";
}
```

Output:

``` text
1 2
```

------------------------------------------------------------------------

# 30. `return`

## Definition

`return` exits a function and can optionally provide a value to the
caller.

Example:

``` cpp
int add(int a, int b) {
    return a + b;
}
```

Then:

``` cpp
int result = add(10, 20);
```

gives:

``` text
30
```

In:

``` cpp
int main() {
    return 0;
}
```

`return 0` indicates successful termination to the environment.

------------------------------------------------------------------------

# 31. `goto`

## Definition

`goto` transfers execution to a labeled statement.

Example:

``` cpp
goto start;

cout << "This is skipped";

start:
cout << "Hello";
```

Output:

``` text
Hello
```

### Should you use `goto` in DSA?

Generally, **no**.

Prefer structured control flow:

-   `if`
-   loops
-   functions
-   `break`
-   `continue`
-   `return`

because these are easier to understand and maintain.

------------------------------------------------------------------------

# 32. `try-catch` and `throw`

These belong to **exception handling**, not ordinary conditional
statements.

Example:

``` cpp
try {
    throw runtime_error("Something went wrong");
}
catch (const exception& e) {
    cout << e.what();
}
```

Conceptually:

``` text
try
 ↓
exception occurs
 ↓
throw
 ↓
matching catch
 ↓
handle exception
```

For normal beginner DSA problems, exception handling is usually not a
major focus.

------------------------------------------------------------------------

# 33. `switch`, `case`, and `default` Relationship

Think of them like this:

``` text
switch
  │
  ├── case
  │
  ├── case
  │
  └── default
```

A `case` label belongs to a `switch`.

A `default` label belongs to a `switch`.

Example:

``` cpp
switch(x) {

    case 1:
        cout << "One";
        break;

    case 2:
        cout << "Two";
        break;

    default:
        cout << "Other";
}
```

------------------------------------------------------------------------

# 34. ASCII

## Definition

**ASCII** stands for:

> American Standard Code for Information Interchange.

ASCII assigns numeric codes to common characters.

  Character     ASCII
  ----------- -------
  `'0'`            48
  `'1'`            49
  `'9'`            57
  `'A'`            65
  `'B'`            66
  `'Z'`            90
  `'a'`            97
  `'b'`            98
  `'z'`           122
  `' '`            32
  `'\n'`           10
  `'\t'`            9
  `'\r'`           13
  `'\b'`            8
  `'\0'`            0

------------------------------------------------------------------------
