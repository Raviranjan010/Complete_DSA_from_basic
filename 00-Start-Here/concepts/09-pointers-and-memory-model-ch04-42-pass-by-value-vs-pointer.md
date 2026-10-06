[← Chapter 03](09-pointers-and-memory-model-ch03-27-modifying-through-pointer-t.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 05 →](09-pointers-and-memory-model-ch05-56-double-delete.md)

---

# 42. Pass by Value vs Pointer

## Pass by Value

```cpp
void change(int x) {
    x = 100;
}
```

Calling:

```cpp
int a = 10;
change(a);
```

does not change `a`.

Why?

A copy is passed.

---

## Pass by Pointer

```cpp
void change(int *x) {
    *x = 100;
}
```

Call:

```cpp
change(&a);
```

Now the original `a` changes.

---

# 43. Pass by Reference vs Pointer

C++ also has references.

### Pointer

```cpp
void change(int *x) {
    *x = 100;
}

change(&a);
```

### Reference

```cpp
void change(int &x) {
    x = 100;
}

change(a);
```

Both can modify the original object.

### Major difference

A pointer:

```text
can be nullptr
can be reassigned
requires dereferencing to access the pointed object
```

A reference:

```text
must be bound to an object when initialized
cannot be null in normal use
cannot be reseated to refer to another object
is used like the referred object
```

---

# 44. Pointer Reassignment

A pointer can point to different objects.

```cpp
int a = 10;
int b = 20;

int *ptr = &a;

cout << *ptr; // 10

ptr = &b;

cout << *ptr; // 20
```

The pointer changed what it points to.

The variables themselves did not move.

---

# 45. Pointer vs Changing the Pointed Value

These are different:

```cpp
*ptr = 50;
```

and:

```cpp
ptr = &b;
```

### `*ptr = 50`

Changes the value of the object being pointed to.

### `ptr = &b`

Changes which object the pointer points to.

This distinction is critical.

---

# 46. Pointer to Constant

```cpp
const int a = 10;

const int *ptr = &a;
```

This means:

> Pointer to a const int.

You cannot modify the object through `ptr`:

```cpp
*ptr = 20; // ERROR
```

But the pointer itself can be changed:

```cpp
int b = 30;

ptr = &b;
```

---

# 47. Constant Pointer

```cpp
int a = 10;

int *const ptr = &a;
```

This means:

> `ptr` itself cannot be changed to point somewhere else.

This is invalid:

```cpp
int b = 20;

ptr = &b; // ERROR
```

But the pointed value can be modified:

```cpp
*ptr = 50;
```

---

# 48. Constant Pointer to Constant

```cpp
const int a = 10;

const int *const ptr = &a;
```

Now:

```text
The pointer cannot change.
The pointed value cannot be changed through the pointer.
```

Therefore neither is allowed:

```cpp
ptr = &b;  // ERROR
*ptr = 20; // ERROR
```

---

# 49. Easy Way to Read `const` Pointer Declarations

### `const int *p`

Read:

> Pointer to const int.

```text
value cannot be changed through p
p can change
```

### `int *const p`

Read:

> Const pointer to int.

```text
p cannot change
value can change
```

### `const int *const p`

Read:

> Const pointer to const int.

```text
p cannot change
value cannot change through p
```

---

# 50. Dynamic Memory Allocation

Pointers become especially important when memory is allocated dynamically.

Modern C++ generally prefers:

```text
std::vector
std::string
smart pointers
RAII
```

over raw `new`/`delete` for most application code.

However, understanding raw dynamic memory is important for DSA and interviews.

---

# 51. `new`

Example:

```cpp
int *ptr = new int;
```

This dynamically allocates an `int`.

We can initialize it:

```cpp
int *ptr = new int(10);
```

Now:

```cpp
cout << *ptr;
```

prints:

```text
10
```

---

# 52. `delete`

Memory allocated using:

```cpp
new
```

must eventually be released using:

```cpp
delete
```

Example:

```cpp
int *ptr = new int(10);

cout << *ptr;

delete ptr;

ptr = nullptr;
```

After deletion, do not dereference `ptr`.

---

# 53. Dynamic Array

Allocate:

```cpp
int *arr = new int[5];
```

Use:

```cpp
arr[0] = 10;
arr[1] = 20;
```

Release:

```cpp
delete[] arr;
```

### Important

For:

```cpp
new int
```

use:

```cpp
delete
```

For:

```cpp
new int[5]
```

use:

```cpp
delete[]
```

Do not mix them.

---

# 54. Memory Leak

A memory leak occurs when dynamically allocated memory is no longer reachable but has not been released.

Example:

```cpp
int *ptr = new int(10);

ptr = nullptr;
```

The allocated memory is now lost.

There is no pointer through which it can be deleted.

That memory is leaked.

Correct:

```cpp
int *ptr = new int(10);

delete ptr;
ptr = nullptr;
```

---

# 55. Use-After-Free

Example:

```cpp
int *ptr = new int(10);

delete ptr;

cout << *ptr;
```

This is invalid.

After:

```cpp
delete ptr;
```

the object no longer exists.

A useful defensive pattern is:

```cpp
delete ptr;
ptr = nullptr;
```

Then:

```cpp
if(ptr != nullptr) {
    cout << *ptr;
}
```

---
