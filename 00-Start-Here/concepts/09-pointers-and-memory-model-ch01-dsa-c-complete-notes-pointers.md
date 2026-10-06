[Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 02 →](09-pointers-and-memory-model-ch02-13-pointer-and-variable-are-di.md)

---

# 📘 DSA / C++ Complete Notes: Pointers

> **Goal:** Build a strong, confusion-free understanding of C++ pointers from the basics to DSA-level usage.

---

# 1. What Is a Pointer?

A **pointer is a variable that stores the memory address of another variable**.

Example:

```cpp
int a = 12;
int *ptr = &a;
```

Here:

```text
a      → stores the value 12
ptr    → stores the address of a
```

So:

```text
a  = value
ptr = address
```

### Core Definition

> A pointer is a variable whose value is the memory address of another object.

---

# 2. Why Do We Need Pointers?

Pointers are important because they allow us to:

- access memory directly
- modify another variable through its address
- pass variables efficiently to functions
- dynamically allocate memory
- build linked lists
- build trees
- build graphs
- implement dynamic data structures
- work with arrays and strings
- use dynamic memory
- understand references and memory management
- implement many DSA structures

Pointers are especially important in:

```text
Linked List
Tree
Graph
Dynamic Memory
Stack / Queue implementations
Hash tables
Function arguments
```

---

# 3. Memory Basics

Suppose:

```cpp
int a = 12;
```

Conceptually, memory may look like:

```text
Address        Value
1000           12
```

The exact address is determined by the system and may differ every time.

If:

```cpp
int *ptr = &a;
```

then:

```text
ptr
 ↓
1000
```

and:

```text
1000
 ↓
12
```

So:

```text
ptr stores address of a
```

---

# 4. Address-of Operator `&`

The operator:

```cpp
&
```

is called the **address-of operator** when used before a variable.

Example:

```cpp
int a = 12;

cout << &a;
```

This prints the memory address of `a`.

Example output might look like:

```text
0x7ffd1234abcd
```

The exact address is not predictable and can change between executions.

---

# 5. Pointer Declaration

Syntax:

```cpp
dataType *pointerName;
```

Examples:

```cpp
int *ptr;
float *ptr;
char *ptr;
double *ptr;
```

The pointer type should generally correspond to the type of object it points to.

Example:

```cpp
int a = 12;
int *ptr = &a;
```

---

# 6. Important Syntax Understanding

These are equivalent declarations:

```cpp
int* ptr;
```

and:

```cpp
int *ptr;
```

The `*` belongs syntactically to the declarator.

This becomes important when declaring multiple variables:

```cpp
int *p, q;
```

This means:

```text
p → pointer to int
q → ordinary int
```

It does **not** mean both are pointers.

If both should be pointers:

```cpp
int *p, *q;
```

### Recommendation

Prefer:

```cpp
int *ptr;
```

or declare pointers separately for clarity.

---

# 7. Dereference Operator `*`

The `*` operator has another important meaning.

When used with a pointer expression, it is the **dereference operator**.

Example:

```cpp
int a = 12;
int *ptr = &a;

cout << *ptr;
```

Output:

```text
12
```

Why?

Because:

```text
ptr  → address of a
*ptr → value stored at that address
```

---

# 8. `&` vs `*`

This is one of the most important concepts.

```cpp
int a = 12;
int *ptr = &a;
```

### `&a`

Means:

```text
Address of a
```

### `ptr`

Means:

```text
Address stored inside ptr
```

### `*ptr`

Means:

```text
Value located at the address stored in ptr
```

Therefore:

```text
&a  → address
ptr → address
*ptr → value
```

---

# 9. Basic Example

```cpp
#include <iostream>
using namespace std;

int main() {

    int a = 12;

    int *ptr = &a;

    cout << a << endl;
    cout << &a << endl;
    cout << ptr << endl;
    cout << *ptr << endl;

    return 0;
}
```

Conceptually:

```text
a       = 12
&a      = address of a
ptr     = address of a
*ptr    = 12
```

Therefore:

```text
ptr == &a
*ptr == a
```

for this valid pointer setup.

---

# 10. Pointer Diagram

Suppose:

```cpp
int a = 12;
int *ptr = &a;
```

Conceptually:

```text
       a
   ┌─────────┐
   │   12    │
   └─────────┘
       ↑
       │
       │ address
   ┌─────────┐
   │   ptr   │
   └─────────┘
```

More precisely:

```text
ptr ───────────────► a
                     12
```

The arrow represents:

```text
ptr contains the address of a
```

---

# 11. Modifying a Variable Through a Pointer

This is one of the most useful properties of pointers.

```cpp
int a = 12;

int *ptr = &a;

*ptr = 50;
```

Now:

```text
a = 50
```

Why?

Because:

```text
*ptr
```

refers to the actual object stored at that address.

So:

```cpp
*ptr = 50;
```

means:

> Go to the memory location pointed to by `ptr` and store `50` there.

---

# 12. Example

```cpp
int a = 12;

int *ptr = &a;

cout << a << endl;

*ptr = 100;

cout << a << endl;
```

Output:

```text
12
100
```

The pointer modified `a`.

---
