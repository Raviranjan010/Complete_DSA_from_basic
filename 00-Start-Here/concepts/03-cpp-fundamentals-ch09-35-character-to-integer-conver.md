[← Chapter 08](03-cpp-fundamentals-ch08-21-can-switch-replace-every-if.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 10 →](03-cpp-fundamentals-ch10-50-dsa-pattern-conditional-fil.md)

---

# 35. Character to Integer Conversion

A character can be converted to its integer character code.

Example:

``` cpp
char ch = 'A';

cout << static_cast<int>(ch);
```

Output:

``` text
65
```

Similarly:

``` cpp
char ch = 'a';

cout << static_cast<int>(ch);
```

Output:

``` text
97
```

------------------------------------------------------------------------

# 36. Integer to Character

The reverse is also possible:

``` cpp
int x = 65;

cout << static_cast<char>(x);
```

Output:

``` text
A
```

Conceptually:

``` text
65 → 'A'
```

------------------------------------------------------------------------

# 37. Character Arithmetic

This is very useful in DSA.

``` cpp
char ch = 'A';

char next = ch + 1;

cout << next;
```

Output:

``` text
B
```

Conceptually:

``` text
'A' → 65
65 + 1 → 66
66 → 'B'
```

This is useful for character and string problems.

------------------------------------------------------------------------

# 38. Checking Uppercase Character

ASCII uppercase letters are:

``` text
'A' → 65
'Z' → 90
```

Therefore:

``` cpp
if (ch >= 'A' && ch <= 'Z') {
    cout << "Uppercase";
}
```

This is a common DSA/string technique.

------------------------------------------------------------------------

# 39. Checking Lowercase Character

Lowercase letters:

``` text
'a' → 97
'z' → 122
```

So:

``` cpp
if (ch >= 'a' && ch <= 'z') {
    cout << "Lowercase";
}
```

------------------------------------------------------------------------

# 40. Checking Digit Character

Digits:

``` text
'0' → 48
'9' → 57
```

Therefore:

``` cpp
if (ch >= '0' && ch <= '9') {
    cout << "Digit";
}
```

### Very important

Do not confuse:

``` cpp
'5'
```

with:

``` cpp
5
```

They are different.

``` text
'5' → character
5   → integer
```

------------------------------------------------------------------------

# 41. `'0'` vs `'\0'`

This is one of the most important character concepts.

They are completely different.

### `'0'`

Character zero:

``` text
ASCII = 48
```

### `'\0'`

Null character:

``` text
value = 0
```

Therefore:

``` text
'0' != '\0'
```

Remember this carefully.

------------------------------------------------------------------------

# 42. `'\n'`

`\n` represents a newline character.

Example:

``` cpp
cout << "Hello\nWorld";
```

Output:

``` text
Hello
World
```

Common ASCII value:

``` text
'\n' = 10
```

### Important correction

`\n` does **not** mean:

-   end of a string
-   end of a file
-   end of a program
-   end of a function
-   end of a class

It simply represents a **newline character**.

------------------------------------------------------------------------

# 43. `'\0'` in C-Style Strings

For a C-style character array:

``` cpp
char name[] = "Ravi";
```

Conceptually, memory contains:

``` text
R   a   v   i   \0
```

The `'\0'` is the **null character** marking the end of the C-style
string.

This becomes extremely important when studying:

-   character arrays
-   strings
-   pointers
-   memory
-   C-style string algorithms

------------------------------------------------------------------------

# 44. `'\t'`

`\t` represents horizontal tab.

Example:

``` cpp
cout << "Name\tAge";
```

Common ASCII value:

``` text
9
```

------------------------------------------------------------------------

# 45. `'\r'`

`\r` represents **carriage return**.

ASCII value:

``` text
13
```

Historically, it moves the cursor to the beginning of the current line.

Newline conventions differ by operating system:

``` text
Unix/Linux/macOS → \n
Windows           → \r\n
```

------------------------------------------------------------------------

# 46. `'\b'`

`\b` represents backspace.

ASCII value:

``` text
8
```

------------------------------------------------------------------------

# 47. ASCII vs Unicode

### ASCII

A character encoding covering a limited set of common characters.

### Unicode

A much larger character system designed to represent characters from
many writing systems.

For basic DSA problems involving English letters and digits, ASCII
relationships are commonly useful:

``` text
'A' to 'Z'
'a' to 'z'
'0' to '9'
```

------------------------------------------------------------------------

# 48. `if-else` vs `switch` vs Ternary

  -----------------------------------------------------------------------
  Feature           `if-else`         `switch`          Ternary
  ----------------- ----------------- ----------------- -----------------
  Main purpose      General           Match discrete    Simple
                    conditions        values            conditional
                                                        expression

  Range conditions  ✅                ❌ Not naturally  ✅

  Complex           ✅                Limited           Possible, but
  conditions                                            avoid complexity

  Multiple choices  ✅                ✅                ❌ Best for
                                                        simple two-way
                                                        choice

  Produces a value  Not inherently    Not inherently    ✅
  directly                                              

  Readability       High              High for menus    High for simple
                                                        cases

  DSA usage         ⭐⭐⭐⭐⭐        ⭐⭐⭐            ⭐⭐⭐
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 49. Common Beginner Mistakes

## Mistake 1 --- `=` vs `==`

Wrong when comparison is intended:

``` cpp
if (x = 10)
```

Correct:

``` cpp
if (x == 10)
```

------------------------------------------------------------------------

## Mistake 2 --- Wrong range expression

Incorrect:

``` cpp
if (x >= 10 && <= 20)
```

Correct:

``` cpp
if (x >= 10 && x <= 20)
```

------------------------------------------------------------------------

## Mistake 3 --- Incorrect OR condition

Incorrect:

``` cpp
if (x == 1 || 2)
```

Correct:

``` cpp
if (x == 1 || x == 2)
```

------------------------------------------------------------------------

## Mistake 4 --- Forgetting `break`

``` cpp
switch(x) {
    case 1:
        cout << "One";

    case 2:
        cout << "Two";
}
```

This may execute both cases because of fall-through.

------------------------------------------------------------------------

## Mistake 5 --- Confusing `break` and `continue`

``` text
break    → stop loop
continue → skip current iteration
```

------------------------------------------------------------------------

## Mistake 6 --- Confusing `'5'` and `5`

``` text
'5' → character
5   → integer
```

------------------------------------------------------------------------

## Mistake 7 --- Confusing `'0'` and `'\0'`

``` text
'0'  → character zero → ASCII 48
'\0' → null character → value 0
```

------------------------------------------------------------------------

## Mistake 8 --- Incorrect understanding of `\n`

``` text
\n → newline
```

It does not mark the end of a string.

For C-style strings:

``` text
\0 → null terminator
```

------------------------------------------------------------------------
