[Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 02 →](03-cpp-fundamentals-ch02-12-float.md)

---

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
