[← Chapter 04](09-pointers-and-memory-model-ch04-42-pass-by-value-vs-pointer.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 06 →](09-pointers-and-memory-model-ch06-69-pointers-and-const-in-funct.md)

---

# 56. Double Delete

This is also invalid:

```cpp
int *ptr = new int(10);

delete ptr;
delete ptr;
```

The second deletion attempts to release an already-deleted object.

Safer:

```cpp
delete ptr;
ptr = nullptr;
```

Then:

```cpp
delete ptr;
```

is harmless because deleting a null pointer is permitted.

Still, ownership should be designed clearly rather than relying on this.

---

# 57. Smart Pointers

Modern C++ provides smart pointers:

```cpp
unique_ptr
shared_ptr
weak_ptr
```

They manage dynamic lifetime automatically.

Example:

```cpp
#include <memory>

unique_ptr<int> ptr = make_unique<int>(10);
```

No explicit:

```cpp
delete
```

is needed.

For modern C++, prefer RAII and smart pointers when dynamic ownership is actually required.

---

# 58. Pointer and Linked List

Pointers are fundamental to linked lists.

Example node:

```cpp
struct Node {
    int data;
    Node* next;
};
```

Here:

```text
data → stores value
next → stores address of another Node
```

Example:

```text
10 → 20 → 30 → nullptr
```

Conceptually:

```text
┌───────┬──────┐
│  10   │  ─────────► Node 20
└───────┴──────┘
```

This is one of the most important DSA applications of pointers.

---

# 59. Creating a Linked List Node

```cpp
Node* newNode = new Node;

newNode->data = 10;
newNode->next = nullptr;
```

Notice:

```cpp
newNode->data
```

instead of:

```cpp
(*newNode).data
```

These are equivalent:

```cpp
newNode->data
```

and:

```cpp
(*newNode).data
```

---

# 60. Arrow Operator `->`

The arrow operator is used when accessing a member through a pointer to an object.

If:

```cpp
Node *ptr;
```

then:

```cpp
ptr->data
```

means:

```cpp
(*ptr).data
```

### Rule

```text
object:
    object.member

pointer:
    pointer->member
```

Example:

```cpp
Node node;

node.data = 10;
```

Pointer:

```cpp
Node *ptr = &node;

ptr->data = 20;
```

---

# 61. `.` vs `->`

| Situation | Operator |
|---|---|
| Object | `.` |
| Pointer to object | `->` |

Example:

```cpp
Node n;

n.data = 10;
```

Pointer:

```cpp
Node *p = &n;

p->data = 20;
```

Equivalent:

```cpp
(*p).data = 20;
```

---

# 62. Pointers in Trees

A binary tree node commonly looks like:

```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
};
```

Conceptually:

```text
          10
         /  \
        5    20
       / \
      2   7
```

The pointers connect nodes:

```text
left  → left child
right → right child
```

If there is no child:

```cpp
left = nullptr;
```

or:

```cpp
right = nullptr;
```

---

# 63. Pointers in Graphs

Graphs can also use pointers.

For example, adjacency structures may contain:

```text
nodes
edges
linked structures
dynamic objects
```

Pointers allow one object to reference another.

However, modern C++ graph implementations often use:

```cpp
vector<vector<int>>
```

or other containers instead of raw pointers.

---

# 64. Double Pointers in DSA

Pointer-to-pointer is especially useful when a function needs to modify a pointer itself.

Example:

```cpp
void changePointer(int **p) {

    static int x = 100;

    *p = &x;
}
```

Caller:

```cpp
int *ptr = nullptr;

changePointer(&ptr);
```

Now `ptr` points to `x`.

This concept appears in linked-list operations such as modifying the head pointer.

---

# 65. Why `Node**` Can Be Useful in Linked Lists

Suppose:

```cpp
Node* head;
```

If a function needs to change:

```cpp
head
```

it can receive:

```cpp
Node** head
```

Example:

```cpp
void insertAtBeginning(Node** head, int value);
```

The function can then modify:

```cpp
*head
```

Modern C++ often provides cleaner alternatives using:

```cpp
Node*& head
```

or returning the new head, but understanding `Node**` is important.

---

# 66. Pointer to Function

Pointers can also point to functions.

Example:

```cpp
int add(int a, int b) {
    return a + b;
}

int (*ptr)(int, int) = add;
```

Call:

```cpp
cout << ptr(2,3);
```

Output:

```text
5
```

This is called a **function pointer**.

---

# 67. Function Pointer Syntax

General form:

```cpp
returnType (*pointerName)(parameterTypes);
```

Example:

```cpp
int (*ptr)(int, int);
```

means:

> `ptr` is a pointer to a function taking two `int`s and returning an `int`.

Function pointers are useful for:

- callbacks
- generic algorithms
- event systems
- low-level programming

Modern C++ often uses lambdas and `std::function` where appropriate.

---

# 68. Pointer to Pointer vs Reference

Consider:

```cpp
int *ptr;
```

and:

```cpp
int &ref;
```

A pointer:

```text
stores an address
can be null
can be reassigned
supports pointer arithmetic in applicable cases
```

A reference:

```text
aliases an existing object
normally must be initialized
cannot be null in normal language semantics
cannot be reseated
```

Example:

```cpp
int a = 10;
int b = 20;

int *p = &a;
p = &b;
```

Pointer now refers to `b`.

Reference:

```cpp
int &r = a;
```

You cannot make `r` start referring to `b` by assignment:

```cpp
r = b;
```

This assigns `b`'s value to `a`; it does not reseat the reference.

---
