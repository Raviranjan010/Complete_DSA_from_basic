[← Chapter 06](03-cpp-fundamentals-ch06-62-final-mental-model.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 08 →](03-cpp-fundamentals-ch08-21-can-switch-replace-every-if.md)

---

# 9. How `else-if` Works

C++ checks conditions **from top to bottom**.

``` text
condition 1?
   ↓
 true → execute → stop checking chain
 false
   ↓
condition 2?
   ↓
 true → execute → stop
 false
   ↓
condition 3?
```

Once one condition is true, the remaining `else if` conditions are
skipped.

### Example

``` cpp
int x = 10;

if (x > 0) {
    cout << "Positive";
}
else if (x > 5) {
    cout << "Greater than 5";
}
```

Output:

``` text
Positive
```

Although `x > 5` is also true, the second condition is never checked
because the first condition already matched.

------------------------------------------------------------------------

# 10. Order of Conditions Matters

Consider:

``` cpp
int marks = 95;

if (marks >= 40) {
    cout << "Pass";
}
else if (marks >= 90) {
    cout << "Excellent";
}
```

Output:

``` text
Pass
```

The second condition never gets a chance.

### Correct ordering

``` cpp
if (marks >= 90) {
    cout << "Excellent";
}
else if (marks >= 40) {
    cout << "Pass";
}
else {
    cout << "Fail";
}
```

### DSA Lesson

When using an `else-if` ladder, **order your conditions carefully**.

------------------------------------------------------------------------

# 11. Nested `if`

## Definition

An `if` statement placed inside another `if` or `else` block is called a
**nested if**.

Example:

``` cpp
int age = 20;
bool hasID = true;

if (age >= 18) {

    if (hasID) {
        cout << "Entry allowed";
    }

}
```

Structure:

``` text
if age >= 18
│
└── if hasID
    │
    └── Entry allowed
```

------------------------------------------------------------------------

# 12. Nested `if` vs Logical `&&`

The same basic logic can often be written using `&&`.

### Nested version

``` cpp
if (age >= 18) {
    if (hasID) {
        cout << "Allowed";
    }
}
```

### Logical version

``` cpp
if (age >= 18 && hasID) {
    cout << "Allowed";
}
```

### Which should you use?

Use `&&` when the conditions naturally form **one combined condition**.

Use nested `if` when the second decision logically depends on entering
the first branch or when separate processing is required.

------------------------------------------------------------------------

# 13. `switch-case`

## Definition

`switch` is a selection statement used to choose among multiple branches
based on the value of an expression.

### Syntax

``` cpp
switch (expression) {

    case value1:
        // code
        break;

    case value2:
        // code
        break;

    default:
        // code
}
```

### Example

``` cpp
int day = 2;

switch (day) {

    case 1:
        cout << "Monday";
        break;

    case 2:
        cout << "Tuesday";
        break;

    case 3:
        cout << "Wednesday";
        break;

    default:
        cout << "Invalid day";
}
```

Output:

``` text
Tuesday
```

------------------------------------------------------------------------

# 14. How `switch` Works

Suppose:

``` cpp
int choice = 2;
```

Then:

``` text
switch(choice)
      ↓
choice = 2
      ↓
case 1? → No
      ↓
case 2? → YES
      ↓
execute case 2
      ↓
break
      ↓
exit switch
```

------------------------------------------------------------------------

# 15. `case`

A `case` specifies a possible value of the switch expression.

Example:

``` cpp
switch(choice) {

    case 1:
        cout << "Option 1";
        break;

    case 2:
        cout << "Option 2";
        break;
}
```

If:

``` text
choice = 2
```

then:

``` text
case 2
```

matches.

------------------------------------------------------------------------

# 16. `default`

`default` executes when no case matches.

Example:

``` cpp
int choice = 10;

switch(choice) {

    case 1:
        cout << "One";
        break;

    case 2:
        cout << "Two";
        break;

    default:
        cout << "Invalid choice";
}
```

Output:

``` text
Invalid choice
```

### Important

`default` is optional.

It is often useful for handling unexpected values.

------------------------------------------------------------------------

# 17. `break` in `switch`

This is one of the most important `switch` concepts.

Consider:

``` cpp
int x = 1;

switch(x) {

    case 1:
        cout << "A";

    case 2:
        cout << "B";

    case 3:
        cout << "C";
}
```

Output:

``` text
ABC
```

Why?

Because there is no `break`.

This behavior is called **fall-through**.

------------------------------------------------------------------------

# 18. Fall-Through

Normally:

``` cpp
case 1:
    cout << "A";
    break;
```

means:

``` text
execute case 1
      ↓
break
      ↓
exit switch
```

Without `break`:

``` text
case 1
 ↓
execute
 ↓
case 2
 ↓
execute
 ↓
case 3
 ↓
execute
```

### Normal usage

``` cpp
switch(x) {

    case 1:
        cout << "A";
        break;

    case 2:
        cout << "B";
        break;

    case 3:
        cout << "C";
        break;
}
```

------------------------------------------------------------------------

# 19. Intentional Fall-Through

Fall-through can be useful.

Example:

``` cpp
char ch = 'a';

switch(ch) {

    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        cout << "Vowel";
        break;

    default:
        cout << "Consonant";
}
```

Here multiple cases intentionally share the same code.

``` text
a ─┐
e ─┤
i ─┤
o ─┤ → Vowel
u ─┘
```

------------------------------------------------------------------------

# 20. `if-else` vs `switch`

  `if-else`                             `switch`
  ------------------------------------- ---------------------------------
  Best for conditions and ranges        Best for discrete choices
  Supports `<`, `>`, `&&`, `||`, etc.   Matches against case values
  Can naturally handle ranges           Not naturally suited for ranges
  More flexible                         Often cleaner for menus/options
  Good for complex conditions           Good for fixed choices

### Example suited for `if`

``` cpp
if (marks >= 90)
```

This is a range condition.

### Example suited for `switch`

``` cpp
switch(choice) {
    case 1:
    case 2:
    case 3:
}
```

This is selection among discrete values.

------------------------------------------------------------------------
