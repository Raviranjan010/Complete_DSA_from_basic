[← Chapter 06](09-pointers-and-memory-model-ch06-69-pointers-and-const-in-funct.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 08 →](09-pointers-and-memory-model-ch08-94-pointer-recursion-connectio.md)

---

# 82. Common Pointer Mistakes

## Mistake 1

```cpp
int *ptr;
cout << *ptr;
```

Problem:

```text
Uninitialized pointer
```

---

## Mistake 2

```cpp
int *ptr = nullptr;
cout << *ptr;
```

Problem:

```text
Dereferencing null
```

---

## Mistake 3

```cpp
int *ptr = new int(10);

delete ptr;

cout << *ptr;
```

Problem:

```text
Use-after-free
```

---

## Mistake 4

```cpp
int *ptr = new int[10];

delete ptr;
```

Problem:

```text
Mismatched allocation/deallocation
```

Correct:

```cpp
delete[] ptr;
```

---

## Mistake 5

```cpp
int a = 10;
int *p = &a;

p = nullptr;

cout << *p;
```

Problem:

```text
Null dereference
```

---

## Mistake 6

Confusing:

```cpp
ptr
```

with:

```cpp
*ptr
```

Remember:

```text
ptr  = address
*ptr = value at that address
```

---

# 83. `*p++` vs `(*p)++`

These are different.

## `*p++`

Operator precedence means this is interpreted as:

```cpp
*(p++)
```

So:

```text
Use current pointer value, then increment pointer.
```

## `(*p)++`

Means:

```text
Increment the value pointed to by p.
```

Example:

```cpp
int arr[] = {10,20};
int *p = arr;

(*p)++;
```

Now:

```text
arr = {11,20}
```

But:

```cpp
*p++;
```

moves the pointer.

This is a very common pointer question.

---

# 84. `*p + 1` vs `*(p + 1)`

Also different.

### `*p + 1`

Means:

```text
value pointed to by p + 1
```

### `*(p + 1)`

Means:

```text
value at the next pointer position
```

Example:

```cpp
int arr[] = {10,20,30};

int *p = arr;
```

Then:

```cpp
*p + 1
```

gives:

```text
11
```

while:

```cpp
*(p + 1)
```

gives:

```text
20
```

---

# 85. Operator Precedence Matters

Expressions involving pointers can become confusing.

When unsure, add parentheses.

Instead of:

```cpp
*p++
```

write:

```cpp
*(p++)
```

if that is what you mean.

Instead of:

```cpp
*p + 1
```

use:

```cpp
(*p) + 1
```

for clarity.

---

# 86. Pointer to Struct

Example:

```cpp
struct Student {
    int age;
};

Student s;

Student *ptr = &s;

ptr->age = 20;
```

Equivalent:

```cpp
(*ptr).age = 20;
```

Remember:

```text
`.`  → object
`->` → pointer to object
```

---

# 87. Pointers in Linked List — Basic Example

```cpp
struct Node {
    int data;
    Node* next;

    Node(int value) {
        data = value;
        next = nullptr;
    }
};
```

Create:

```cpp
Node* head = new Node(10);
head->next = new Node(20);
head->next->next = new Node(30);
```

Structure:

```text
head
 ↓
10 → 20 → 30 → nullptr
```

This is the foundation of a singly linked list.

---

# 88. Traversing a Linked List

```cpp
Node* temp = head;

while(temp != nullptr) {

    cout << temp->data << " ";

    temp = temp->next;
}
```

This pattern is extremely important.

### Mental model

```text
temp
 ↓
current node
 ↓
print
 ↓
temp = temp->next
 ↓
next node
```

---

# 89. Pointer as a DSA Tool

Pointers allow us to create relationships:

```text
Node A
   ↓
Node B
   ↓
Node C
```

This is why linked lists, trees, and many graph structures are possible.

Instead of storing all objects contiguously, one object can store a reference/address to another object.

---

# 90. Pointer-Based DSA Structures

Pointers commonly appear in:

```text
Singly Linked List
Doubly Linked List
Circular Linked List
Binary Tree
Binary Search Tree
AVL Tree
Heap implementations
Graph nodes
Trie implementations
Dynamic stacks
Dynamic queues
```

---

# 91. Doubly Linked List

A doubly linked list node typically has:

```cpp
struct Node {
    int data;
    Node* prev;
    Node* next;
};
```

Conceptually:

```text
nullptr ← 10 ⇄ 20 ⇄ 30 → nullptr
```

`prev` points backward.

`next` points forward.

---

# 92. Circular Linked List

A circular list can have:

```text
10 → 20 → 30
↑         ↓
└─────────┘
```

The final node points back to the first node.

Pointers make this possible.

---

# 93. Tree Node

```cpp
struct Node {
    int data;
    Node* left;
    Node* right;
};
```

Conceptually:

```text
          10
         /  \
        5    15
```

The `left` and `right` pointers connect nodes.

---
