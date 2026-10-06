[← Chapter 01](09-pointers-and-memory-model-ch01-dsa-c-complete-notes-pointers.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 03 →](09-pointers-and-memory-model-ch03-27-modifying-through-pointer-t.md)

---

# 13. Pointer and Variable Are Different

Suppose:

```cpp
int a = 12;
int *ptr = &a;
```

These are different objects:

```text
a
ptr
```

`a` stores:

```text
12
```

`ptr` stores:

```text
address of a
```

Therefore:

```text
a ≠ ptr
```

But:

```text
*ptr == a
```

---

# 14. Pointer Size

A common misconception:

> "An `int*` is the same size as an `int`."

Not necessarily.

A pointer stores an address, so its size is generally determined by the platform's address representation.

On a typical 64-bit system:

```text
int     → commonly 4 bytes
int*    → commonly 8 bytes
double* → commonly 8 bytes
char*   → commonly 8 bytes
```

You can check:

```cpp
cout << sizeof(int) << endl;
cout << sizeof(int*) << endl;
cout << sizeof(double*) << endl;
```

The exact sizes are implementation-dependent.

---

# 15. Pointer Type Matters

Consider:

```cpp
int a = 10;
int *ptr = &a;
```

`ptr` is:

```text
pointer to int
```

This tells C++:

- what type of object is expected at the pointed address
- how dereferencing should interpret the memory
- how pointer arithmetic should work

---

# 16. Null Pointer

A pointer should not be left uninitialized.

Bad:

```cpp
int *ptr;
```

`ptr` contains an indeterminate value.

Using it before assigning a valid address can cause undefined behavior.

Prefer:

```cpp
int *ptr = nullptr;
```

`nullptr` means:

> This pointer currently points to no object.

Example:

```cpp
int *ptr = nullptr;
```

You can test:

```cpp
if(ptr == nullptr) {
    cout << "Pointer is null";
}
```

---

# 17. `nullptr` vs `NULL`

Modern C++:

```cpp
nullptr
```

is preferred.

Older code may use:

```cpp
NULL
```

or:

```cpp
0
```

Use:

```cpp
nullptr
```

in modern C++.

---

# 18. Dereferencing `nullptr`

This is dangerous:

```cpp
int *ptr = nullptr;

cout << *ptr;
```

There is no valid object at the address represented by `nullptr`.

Dereferencing it causes **undefined behavior**.

### Rule

```text
Never dereference a null pointer.
```

Check first when necessary:

```cpp
if(ptr != nullptr) {
    cout << *ptr;
}
```

---

# 19. Dangling Pointer

A **dangling pointer** is a pointer that refers to an object whose lifetime has ended.

Example:

```cpp
int *ptr;

{
    int a = 10;
    ptr = &a;
}

// a no longer exists here
```

Now:

```cpp
ptr
```

is dangling.

Do not dereference it.

---

# 20. Wild Pointer

A **wild pointer** is an uninitialized pointer.

Example:

```cpp
int *ptr;
```

Before assigning a valid address, `ptr` contains an indeterminate value.

Bad:

```cpp
cout << *ptr;
```

Better:

```cpp
int *ptr = nullptr;
```

---

# 21. Void Pointer

A `void*` is a pointer that can hold the address of an object of any object type.

Example:

```cpp
int a = 10;

void *ptr = &a;
```

However, you cannot directly dereference a `void*` because it does not specify the pointed-to type.

You need to convert it:

```cpp
cout << *static_cast<int*>(ptr);
```

For normal C++ programming, prefer typed pointers when possible.

---

# 22. Pointer to Pointer

A pointer can store the address of another pointer.

Example:

```cpp
int a = 12;

int *ptr = &a;

int **ptr2 = &ptr;
```

Now we have three levels:

```text
a
ptr
ptr2
```

---

# 23. Understanding `int **`

```cpp
int **ptr2;
```

means:

```text
ptr2 is a pointer to a pointer to an int
```

Not:

```text
ptr2 is an integer
```

The levels are:

```text
int
 ↓
int*
 ↓
int**
```

---

# 24. Pointer-to-Pointer Diagram

Given:

```cpp
int a = 12;
int *ptr = &a;
int **ptr2 = &ptr;
```

Conceptually:

```text
ptr2
  │
  ▼
 ptr
  │
  ▼
  a
  │
  ▼
 12
```

Therefore:

```text
ptr2  → ptr
ptr   → a
```

---

# 25. Dereferencing Multiple Levels

Given:

```cpp
int a = 12;
int *ptr = &a;
int **ptr2 = &ptr;
```

Then:

```cpp
*ptr2
```

gives:

```text
ptr
```

And:

```cpp
**ptr2
```

gives:

```text
a
```

Therefore:

```text
ptr2   → address of ptr
*ptr2  → ptr
**ptr2 → value of a
```

---

# 26. Three Levels of Pointers

You can technically have:

```cpp
int ***ptr3;
```

Example:

```cpp
int a = 12;

int *p = &a;
int **pp = &p;
int ***ppp = &pp;
```

Then:

```text
***ppp
```

gives:

```text
12
```

Conceptually:

```text
ppp
 ↓
pp
 ↓
p
 ↓
a
 ↓
12
```

Multiple levels are possible, although excessive indirection can make code harder to understand.

---
