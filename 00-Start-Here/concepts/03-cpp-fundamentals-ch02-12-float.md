[← Chapter 01](03-cpp-fundamentals-ch01-c-fundamentals-for-dsa.md) · [Chapter Index](03-cpp-fundamentals.md) · [Module Overview](../README.md) · [Chapter 03 →](03-cpp-fundamentals-ch03-25-main-categories-of-operator.md)

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
