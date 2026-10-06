[← Chapter 05](09-pointers-and-memory-model-ch05-56-double-delete.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 07 →](09-pointers-and-memory-model-ch07-82-common-pointer-mistakes.md)

---

# 69. Pointers and `const` in Function Parameters

Suppose:

```cpp
void print(const int *ptr) {
    cout << *ptr;
}
```

The function promises not to modify the pointed value through `ptr`.

This is useful when passing arrays or objects that should not be modified.

Example:

```cpp
void printArray(const int *arr, int n) {

    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
```

---

# 70. Passing Arrays to Functions

```cpp
void printArray(int *arr, int n) {

    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
```

Call:

```cpp
int arr[] = {10,20,30};

printArray(arr, 3);
```

The array name decays to a pointer to its first element.

Modern C++ alternatives include:

```cpp
std::span
std::array
std::vector
```

depending on the problem.

---

# 71. Important Array-Pointer Confusion

Inside:

```cpp
void printArray(int *arr)
```

you cannot determine the original array length using:

```cpp
sizeof(arr)
```

because `arr` is a pointer parameter.

Example:

```cpp
void func(int arr[]) {
    cout << sizeof(arr);
}
```

Here the parameter is adjusted to a pointer type.

Therefore, pass the size separately:

```cpp
void func(int *arr, int n)
```

or use modern containers such as:

```cpp
vector<int>
array<int, N>
span<int>
```

---

# 72. Pointer and String Literals

C-style strings use arrays of characters:

```cpp
char str[] = "Hello";
```

The array contains:

```text
H e l l o \0
```

A pointer can point to its first character:

```cpp
char *ptr = str;
```

Then:

```cpp
cout << ptr;
```

prints the C-string until the null terminator.

---

# 73. `char*` and String Literals

Be careful with:

```cpp
char *p = "Hello";
```

In modern C++, string literals are not modifiable and this should not be used as a mutable `char*`.

Prefer:

```cpp
const char *p = "Hello";
```

or:

```cpp
string s = "Hello";
```

for modern C++.

---

# 74. Pointers and Memory Layout

A useful mental model:

```text
Stack
----------------
local variables
----------------

Heap
----------------
dynamically allocated objects
----------------

Code / Static storage
----------------
program code / global and static objects
----------------
```

Pointers can point to objects in different storage areas, but the lifetime and validity rules matter.

Do not assume every pointer points to the heap.

For example:

```cpp
int a = 10;
int *p = &a;
```

`a` is typically an automatic local variable, not a heap allocation.

---

# 75. Stack vs Heap

## Stack / Automatic Storage

```cpp
int a = 10;
```

The object has automatic storage duration.

Its lifetime is generally tied to the scope in which it is created.

## Dynamic Storage

```cpp
int *p = new int(10);
```

The object has dynamic storage duration.

Its lifetime continues until released, or until ownership is managed by an appropriate RAII mechanism.

---

# 76. Pointer Lifetime Rule

A pointer is valid only when:

1. It contains an appropriate address.
2. The pointed object is still alive.
3. The access is permitted by the language rules.
4. The pointer has not been invalidated by an operation that changes the object's storage or lifetime.

This is why dangling pointers are dangerous.

---

# 77. Pointer Invalidation

Some operations can invalidate pointers.

For example, a `vector` may reallocate its storage when it grows.

Example:

```cpp
vector<int> v;

v.push_back(10);

int *p = &v[0];

v.push_back(20);
```

The second `push_back` may cause reallocation.

If reallocation occurs, `p` may no longer point to the valid element.

Therefore, don't assume pointers into containers remain valid after operations that can invalidate them.

---

# 78. `vector` and Pointers

Example:

```cpp
vector<int> v = {10,20,30};

int *p = v.data();
```

Then:

```cpp
cout << *p;
```

prints:

```text
10
```

And:

```cpp
cout << *(p + 1);
```

prints:

```text
20
```

But pointer validity must be considered after vector modifications.

---

# 79. Smart Pointer Overview

### `unique_ptr`

One owner.

```cpp
unique_ptr<Node> ptr;
```

Best when one object has a clear owner.

### `shared_ptr`

Multiple shared owners.

```cpp
shared_ptr<Node> ptr;
```

Uses reference counting.

### `weak_ptr`

Non-owning observer of an object managed by `shared_ptr`.

Useful for avoiding ownership cycles.

---

# 80. Raw Pointer vs Smart Pointer

| Feature | Raw Pointer | Smart Pointer |
|---|---|---|
| Automatic ownership | No | Yes |
| Can be null | Yes | Yes |
| Manual `delete` | If owning | Generally no |
| Ownership semantics | Not expressed | Expressed |
| Modern C++ preference | For non-owning / low-level cases | For owning dynamic objects |

For DSA interview implementations, raw pointers are still frequently taught because they make the underlying structure explicit.

---

# 81. Pointer Safety Rules

### Rule 1

Initialize pointers:

```cpp
int *p = nullptr;
```

when they don't immediately point to an object.

### Rule 2

Never dereference `nullptr`.

### Rule 3

Don't dereference dangling pointers.

### Rule 4

Don't use uninitialized pointers.

### Rule 5

Don't access outside an array.

### Rule 6

Match:

```text
new       ↔ delete
new[]     ↔ delete[]
```

### Rule 7

Prefer RAII and standard containers in modern C++.

### Rule 8

Understand ownership before using dynamic memory.

---
