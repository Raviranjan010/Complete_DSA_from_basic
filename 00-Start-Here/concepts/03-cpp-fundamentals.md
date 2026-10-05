# C++ Fundamentals for DSA
## Variables, Data Types, Type Casting & Operators

Before learning DSA, you need a strong understanding of these C++ fundamentals because almost every DSA program uses **variables, data types, operators, conditions, loops, arrays, pointers, and functions**.

---

# 1. Preprocessor Directive

```cpp
#include <iostream>
```

### What is `#include <iostream>`?

`#include` is a **preprocessor directive**.

It tells the C++ preprocessor to include the contents of the specified header file before compilation.

`iostream` stands for:

> **Input Output Stream**

It provides objects such as:

- `cout` → output
- `cin` → input
- `cerr` → error output
- `clog` → logging output

Example:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World";
    return 0;
}
```

---

# 2. Namespace

```cpp
using namespace std;
```

The C++ Standard Library contains many names inside the `std` namespace.

For example:

```cpp
std::cout
std::cin
std::endl
std::string
```

If we write:

```cpp
using namespace std;
```

we can directly write:

```cpp
cout
cin
endl
string
```

### Without `using namespace std`

```cpp
#include <iostream>

int main() {
    std::cout << "Hello";
    return 0;
}
```

### With it

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello";
    return 0;
}
```

### Important recommendation

For small DSA programs, this is commonly used:

```cpp
using namespace std;
```

But in larger projects, it is generally safer to avoid importing the entire namespace and instead use:

```cpp
std::cout
std::vector
std::string
```

This prevents **name conflicts**.

---

# 3. `main()` Function

Every normal C++ executable program needs an entry point.

```cpp
int main() {

    return 0;
}
```

Program execution starts from:

```cpp
main()
```

### Why `int`?

`main()` returns an integer to the operating system.

```cpp
return 0;
```

generally means:

> Program executed successfully.

---

# 4. Printing Output

C++ uses `cout` for standard output.

```cpp
cout << "Hello";
```

The `<<` operator sends data to `cout`.

Example:

```cpp
int age = 20;

cout << age;
```

Output:

```text
20
```

You can print multiple things:

```cpp
cout << "Age: " << age;
```

Output:

```text
Age: 20
```

---

# 5. New Line: `endl` vs `\n`

There are two common ways to move to the next line.

## Using `endl`

```cpp
cout << "Hello" << endl;
cout << "World";
```

Output:

```text
Hello
World
```

## Using `\n`

```cpp
cout << "Hello\n";
cout << "World";
```

Output:

```text
Hello
World
```

### Important difference

`endl`:

1. Inserts a new line.
2. Flushes the output buffer.

`\n`:

1. Inserts a new line.
2. Does not force a flush.

Therefore, in competitive programming and DSA, `\n` is generally preferred when you only need a new line.

```cpp
cout << "Hello\n";
```

---

# 6. Variables

## Definition

A **variable** is a named memory location used to store a value that can be accessed and, depending on its declaration, modified during program execution.

Example:

```cpp
int age = 20;
```

Here:

| Part | Meaning |
|---|---|
| `int` | Data type |
| `age` | Variable name |
| `=` | Assignment operator |
| `20` | Initial value |

Conceptually:

```text
Memory
┌──────────────┐
│ age = 20     │
└──────────────┘
```

The variable `age` gives us a convenient name through which we can access the stored value.

---

# 7. Declaration vs Initialization

These two concepts are different.

## Declaration

```cpp
int age;
```

We are telling C++:

> Create a variable named `age` of type `int`.

## Initialization

```cpp
int age = 20;
```

The variable is created and given its initial value.

### Assignment

```cpp
int age = 20;

age = 25;
```

Here:

```cpp
age = 25;
```

is **assignment**, not initialization.

So:

```cpp
int age = 20;   // initialization
age = 25;       // assignment
```

---

# 8. Identifiers

## Definition

An **identifier** is a name used to identify programming entities such as:

- variables
- functions
- classes
- objects
- structures
- namespaces

Example:

```cpp
int age;

void calculateSum();

class Student;
```

Here:

```text
age          → identifier
calculateSum → identifier
Student      → identifier
```

---

# 9. Rules for Identifiers

An identifier:

### Rule 1 — Can contain letters

```cpp
int age;
int studentName;
```

### Rule 2 — Can contain digits

```cpp
int student1;
int marks2026;
```

But it **cannot start with a digit**.

❌ Invalid:

```cpp
int 1student;
```

✅ Valid:

```cpp
int student1;
```

### Rule 3 — Underscore is allowed

```cpp
int student_name;
```

### Rule 4 — Spaces are not allowed

❌

```cpp
int student name;
```

✅

```cpp
int student_name;
```

### Rule 5 — C++ is case-sensitive

These are different:

```cpp
age
Age
AGE
```

### Rule 6 — Keywords cannot be used as identifiers

❌

```cpp
int class;
```

because `class` is a C++ keyword.

---

# 10. Data Types

## Definition

A **data type** tells the compiler:

1. What kind of value a variable can store.
2. How that value should be interpreted.
3. Usually, how much memory is required for the object.

Common C++ data types include:

```text
int
float
double
char
bool
string
```

---

# 11. Fundamental Data Types

## 11.1 `int`

Used for whole numbers.

```cpp
int age = 20;
int marks = 95;
int temperature = -5;
```

Examples:

```text
10
0
-20
1000
```

Not appropriate for:

```text
10.5
3.14
```

---

# 12. `float`

Used for floating-point/decimal values.

```cpp
float price = 10.5f;
```

The `f` suffix explicitly makes the literal a `float`.

Example:

```cpp
float percentage = 85.5f;
```

---

# 13. `double`

Also stores floating-point values, generally with more precision than `float`.

```cpp
double price = 10.5;
```

Example:

```cpp
double pi = 3.141592653589793;
```

In many programs, `double` is preferred over `float` when you need ordinary floating-point calculations.

---

# 14. `char`

Stores a single character.

```cpp
char grade = 'A';
```

Characters use **single quotes**:

```cpp
'A'
'b'
'7'
'#'
```

This is different from a string.

```cpp
char ch = 'A';        // one character
string name = "Ravi"; // multiple characters
```

---

# 15. `bool`

Stores a logical value:

```cpp
true
false
```

Example:

```cpp
bool isLoggedIn = true;
bool isPassed = false;
```

When printed normally:

```cpp
cout << true;
```

the output is:

```text
1
```

and:

```cpp
cout << false;
```

outputs:

```text
0
```

You can use:

```cpp
cout << boolalpha;
```

to display:

```text
true
false
```

---

# 16. `string`

`string` is used to store text.

```cpp
string name = "Ravi";
```

You normally need:

```cpp
#include <string>
```

although `iostream` may indirectly make it available in some implementations.

Example:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {

    string name = "Ravi";

    cout << name;

    return 0;
}
```

---

# 17. Typical Size of Data Types

You can use:

```cpp
sizeof()
```

to determine the size of an object/type in bytes.

Example:

```cpp
cout << sizeof(int);
```

On many modern systems:

| Data Type | Typical Size |
|---|---:|
| `char` | 1 byte |
| `bool` | typically 1 byte |
| `int` | 4 bytes |
| `float` | 4 bytes |
| `double` | 8 bytes |

### Important

Do **not** memorize these as universal guarantees.

The C++ standard defines minimum requirements and relationships, while the actual size depends on the implementation/platform.

For example:

```cpp
cout << sizeof(int);
```

is better than assuming:

```text
int = always 4 bytes
```

---

# 18. `sizeof()` Operator

`sizeof` determines the size of an object or type in bytes.

Example:

```cpp
int x = 10;

cout << sizeof(x);
```

You can also use:

```cpp
cout << sizeof(int);
```

For arrays:

```cpp
int arr[5];

cout << sizeof(arr);
```

If `int` is 4 bytes, then:

```text
5 × 4 = 20 bytes
```

This becomes extremely important in DSA when working with:

- arrays
- structures
- memory
- pointers
- dynamic allocation

---

# 19. Type Conversion

## Definition

**Type conversion** means converting a value from one data type to another.

For example:

```cpp
int x = 10;
double y = x;
```

Here:

```text
int → double
```

---

# 20. Implicit Type Conversion

When C++ automatically converts one type to another, it is called **implicit conversion**.

Example:

```cpp
int x = 10;

double y = x;
```

Conceptually:

```text
10 (int)
 ↓
10.0 (double)
```

Another example:

```cpp
int a = 10;
double b = 3.5;

double result = a + b;
```

C++ converts `a` to a suitable floating-point type for the operation.

---

# 21. Explicit Type Conversion / Type Casting

When we explicitly tell C++ to convert a value, it is called **explicit conversion** or **type casting**.

Example:

```cpp
double price = 10.5;

int newPrice = static_cast<int>(price);
```

Result:

```text
newPrice = 10
```

The fractional part is discarded.

It does **not** round:

```text
10.5 → 10
10.9 → 10
10.1 → 10
```

---

# 22. C++ Type-Casting Styles

There are several casts in C++.

## 1. `static_cast`

Used for many ordinary compile-time conversions.

```cpp
double price = 10.5;

int x = static_cast<int>(price);
```

Preferred for ordinary numeric conversions.

---

## 2. C-style cast

```cpp
int x = (int)price;
```

This is older C/C++ syntax.

It works, but modern C++ generally prefers:

```cpp
int x = static_cast<int>(price);
```

because the conversion is more explicit.

---

## 3. `dynamic_cast`

Used primarily for safe runtime casting within polymorphic class hierarchies.

Example:

```cpp
Base* ptr = new Derived();

Derived* d = dynamic_cast<Derived*>(ptr);
```

This is **not** a general-purpose numeric conversion tool.

So saying:

> "Use dynamic_cast to convert int to float"

is incorrect.

---

## 4. `const_cast`

Used to add/remove `const` qualification from a type.

```cpp
const int x = 10;
```

`const_cast` is mainly relevant to advanced C++ programming and should not be confused with ordinary numeric conversion.

---

## 5. `reinterpret_cast`

Used for low-level reinterpretation of object representations/pointer types.

It is an advanced and potentially dangerous operation.

It is **not** a normal way to convert:

```text
int → float
```

---

# 23. Important Correction About Type Conversion

It is incorrect to say:

> "Conversion is only possible between compatible types."

C++ has many conversion rules, and some conversions are allowed even when the result may be surprising or lossy.

For example:

```cpp
int x = 65;

char ch = static_cast<char>(x);
```

Depending on the character encoding, this can represent `'A'`.

Also:

```cpp
double x = 10.9;

int y = static_cast<int>(x);
```

produces:

```text
10
```

So the important question is not simply:

> "Can C++ convert these types?"

but:

> **"What conversion rules apply, and what information might be lost?"**

---

# 24. Operators

## Definition

An **operator** is a symbol or syntactic construct that tells C++ to perform an operation on one or more operands.

Example:

```cpp
a + b
```

Here:

```text
a, b → operands
+    → operator
```

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

# ⚡ C++ Syntax for DSA — Your Cheat Sheet

> Keep this open while solving. Includes the tricky bits — `sort(rbegin, rend)`, maps, sets, priority queues — all explained with the "why."

---

## 1. The Boilerplate (every program starts here)

```cpp
#include <bits/stdc++.h>     // includes EVERYTHING (vector, map, set, algorithm...)
using namespace std;         // so you write cout, not std::cout

int main() {
    // optimize cin/cout speed for fast input/output (Crucial for online judges)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // your code here
    cout << "Hello" << "\n";
    return 0;
}
```

> 🔑 `#include <bits/stdc++.h>` is a shortcut header that pulls in all standard libraries at once.

---

## 2. Variables & Types

```cpp
int a = 5;                   // 32-bit whole number
long long big = 1000000000;  // 64-bit huge whole number (use for big sums!)
double d = 3.14;             // 64-bit decimal
char c = 'a';                // single character (single quotes)
bool flag = true;            // true / false
string s = "hello";          // text (double quotes)
```

> ⚠️ Use `long long` when sums might exceed $\approx 2 \times 10^9$, otherwise, your calculations will overflow.

---

## 3. Printing & Reading

```cpp
cout << x << endl;           // print with new line (and flushes buffer, slower)
cout << a << " " << b << "\n";  // faster, preferred for coding platforms

cin >> x;                    // read one value
cin >> a >> b;               // read multiple values
```

---

## 4. Vectors (dynamic arrays)

```cpp
vector<int> v;               // empty
vector<int> v(5);            // 5 zeros
vector<int> v(5, 1);         // five 1's
vector<int> v = {10, 20, 30};// direct values

v.push_back(99);             // append to end
v.size();                    // number of elements
v[0] = 5;                    // set
int x = v[2];                // read
v.pop_back();                // remove last from end

// loops
for (int i = 0; i < v.size(); i++) { ... }
for (int x : v) { ... }      // read-only walk
for (int& x : v) { ... }     // write-enabled walk (by reference)

// 2D vector (grid)
vector<vector<int>> grid(3, vector<int>(4, 0));  // 3x4 of zeros
grid[1][2] = 7;
```

---

## 5. Strings

```cpp
string s = "hello";
s.size();  // or s.length()   — both work
s[2];                        // character at index 2 (like an array)
s.substr(1, 3);              // 3 chars starting at index 1: "ell"
s + "world";                 // concatenation (creates new copy)
s.push_back('!');            // append char to end
reverse(s.begin(), s.end()); // reverse in-place
sort(s.begin(), s.end());    // sort characters ascending
s == "hello";                // compares contents directly (returns bool)
```

> ✅ Unlike Java, in C++ you **can** use `==` to compare string contents directly.

---

## 6. The `char` ↔ `int` Trick (crucial for strings)

```cpp
int pos = c - 'a';                   // 'a'→0, 'b'→1, ... 'z'→25
char back = 'a' + pos;               // 0→'a', 1→'b', ...
int digit = c - '0';                 // '7' → 7

// 26-size frequency array
vector<int> freq(26, 0);
freq[c - 'a']++;                     // count this letter
```

---

## 7. unordered_map (key → value) & unordered_set

```cpp
// 1. unordered_map: O(1) average lookup
unordered_map<char, int> mp;
mp['a'] = 1;                         // add / overwrite
mp['a'];                             // read (auto-creates with value 0 if missing!)
mp.count('a');                       // returns 1 if key exists, else 0
mp.erase('a');                       // delete key

// counting loop
mp[c]++;                             // if c is new, it auto-initializes to 0, then increments to 1

// 2. unordered_set: O(1) uniqueness check
unordered_set<int> st;
st.insert(5);                        // add
st.count(5);                         // returns 1 if present, else 0
st.erase(5);
```

---

## 8. Advanced STL Collections for DSA

### A. deque (Double-Ended Queue)
Supports $O(1)$ insertions and deletions at both the front and the back.
```cpp
deque<int> dq;
dq.push_back(10);
dq.push_front(20);
dq.pop_back();
dq.pop_front();
dq.front();                          // peek front
dq.back();                           // peek back
```

### B. priority_queue (Heap)
```cpp
// 1. Max Heap (Default): largest element on top
priority_queue<int> maxHeap;
maxHeap.push(10);
maxHeap.push(5);
maxHeap.top();                       // Returns 10 (largest)
maxHeap.pop();                       // Removes 10

// 2. Min Heap: smallest element on top
priority_queue<int, vector<int>, greater<int>> minHeap;
minHeap.push(10);
minHeap.push(5);
minHeap.top();                       // Returns 5 (smallest)
```

### C. set & map (Sorted Set / Map)
Implemented using red-black trees under the hood. Keeps elements sorted at all times.
```cpp
// 1. set
set<int> s;
s.insert(10);
s.insert(5);
*s.begin();                          // Returns 5 (smallest)
*s.rbegin();                         // Returns 10 (largest)

// 2. map
map<int, string> m;
m[10] = "apple";
m[5] = "banana";
m.begin()->first;                    // Returns 5 (smallest key)
```

---

## 9. Time Complexities STL Cheat-Sheet

| Structure | Method | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| **vector** | `operator[]` | Index access | $O(1)$ |
| | `push_back` / `pop_back` | End insert/delete | $O(1)$ amortized |
| | `insert` / `erase` | Middle insert/delete | $O(n)$ |
| **unordered_map/set**| `count` / `insert` / `erase` | HashTable access | $O(1)$ average, $O(n)$ worst |
| **map / set** | `find` / `insert` / `erase` | Balanced Tree access | $O(\log n)$ |
| **priority_queue** | `push` / `pop` | Heap update | $O(\log n)$ |
| | `top` | Heap peek | $O(1)$ |

---

## 10. Sorting Algorithms & Comparators

```cpp
sort(v.begin(), v.end());            // ascending (smallest first)
sort(v.rbegin(), v.rend());          // DESCENDING (largest first)
```

### Visualizing Iterators
- `v.begin()` points to the first element; `v.end()` points to one slot past the last element.
- `v.rbegin()` and `v.rend()` are reverse iterators. Sorting backwards yields descending order.

### Custom Comparators (Lambda syntax)
```cpp
// Sort a vector of intervals (pairs) in ascending order of their start values
vector<pair<int, int>> intervals = {{1,3}, {2,6}, {8,10}};
sort(intervals.begin(), intervals.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
    return a.first < b.first; // Return true if 'a' should come BEFORE 'b'
});
```

---

## 11. Handy Utilities

```cpp
max(a, b);   min(a, b);   abs(x);
swap(a, b);                          // swap two variables
INT_MAX;   INT_MIN;                  // for min/max tracking (need <climits>)
to_string(123);                      // number → string
stoi("123");                         // string → number
*max_element(v.begin(), v.end());    // biggest in a vector
*min_element(v.begin(), v.end());    // smallest in a vector
accumulate(v.begin(), v.end(), 0);   // sum of a vector (need <numeric>)
```

---

## 12. Pairs (combining two values)

```cpp
pair<int, char> p = {5, 'a'};
p.first;    // 5
p.second;   // 'a'

vector<pair<int,int>> vp;
vp.push_back({3, 4});
```

---

## 📋 Step-by-Step Dry Run: C++ Frequency Counter

```cpp
string s = "cba";
vector<int> freq(26, 0);
for (char c : s) {
    freq[c - 'a']++;
}
```

- Initial state: `freq` is array of 26 zeros `[0, 0, ..., 0]`
- **Iteration 1 (`c = 'c'`):** `pos = 'c' - 'a' = 99 - 97 = 2`. `freq[2]` becomes `1`.
- **Iteration 2 (`c = 'b'`):** `pos = 'b' - 'a' = 98 - 97 = 1`. `freq[1]` becomes `1`.
- **Iteration 3 (`c = 'a'`):** `pos = 'a' - 'a' = 97 - 97 = 0`. `freq[0]` becomes `1`.

**Final State:** `freq[0]=1, freq[1]=1, freq[2]=1` (Corresponds to 'a': 1, 'b': 1, 'c': 1). ✅

---

## 🎓 C++ Viva Questions & Answers

### Q1: What is the difference between Pointers and References in C++?
**Answer:**
- **Pointer (`int* p`):** Holds the memory address of another variable. Can be `nullptr`, can be reassigned to point to different variables, and requires dereferencing (`*p`).
- **Reference (`int& r`):** An alias for an existing variable. Must be initialized upon declaration, cannot be `null`, and cannot be reassigned to refer to another object.

### Q2: Why pass vectors as `const vector<int>&` in function signatures?
**Answer:**
Passing by value (`vector<int> v`) copies all elements of the vector into the function frame ($O(n)$ time & space). Passing by reference (`vector<int>& v`) avoids copying ($O(1)$). Adding `const` guarantees the function cannot accidentally mutate the original vector.

### Q3: What is the difference between `std::unordered_map` and `std::map` in C++?
**Answer:**
- **`std::unordered_map`:** Implemented using a Hash Table. Unordered keys, average $O(1)$ time complexity for search/insert/delete.
- **`std::map`:** Implemented using a Self-Balancing Red-Black Tree. Keys are kept strictly sorted, $O(\log n)$ guaranteed time complexity for search/insert/delete.

### Q4: Why is `cin.tie(NULL); ios_base::sync_with_stdio(false);` used in C++ competitive programming?
**Answer:**
- `ios_base::sync_with_stdio(false)` disables synchronization between C++ standard streams (`cin`/`cout`) and C stdio streams (`scanf`/`printf`), speeding up I/O.
- `cin.tie(NULL)` unties `cin` from `cout`, preventing `cout` from flushing automatically before `cin` reads input.

### Q5: How does `std::vector` manage memory capacity during expansion?
**Answer:**
When a `vector` exceeds its `capacity`, it allocates a new contiguous block of memory with double the capacity ($2\times$), moves existing elements over, and deallocates old memory. This ensures an **Amortized Time Complexity of $O(1)$** per push.

