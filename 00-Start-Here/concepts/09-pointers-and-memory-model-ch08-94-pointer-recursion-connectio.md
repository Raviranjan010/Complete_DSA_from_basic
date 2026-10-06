[← Chapter 07](09-pointers-and-memory-model-ch07-82-common-pointer-mistakes.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 09 →](09-pointers-and-memory-model-ch09-103-pointer-mindset.md)

---

# 94. Pointer Recursion Connection

Tree algorithms often use pointers:

```cpp
void preorder(Node* root) {

    if(root == nullptr)
        return;

    cout << root->data;

    preorder(root->left);
    preorder(root->right);
}
```

Notice:

```cpp
Node* root
```

and:

```cpp
root->left
root->right
```

Pointers are therefore essential for understanding recursive tree algorithms.

---

# 95. `const` and DSA

A common function:

```cpp
void print(Node* root)
```

If the function should not modify the node through the pointer, you may use:

```cpp
void print(const Node* root)
```

Then:

```cpp
root->data
```

can be read, but modification through `root` is prohibited.

This is useful for expressing intent.

---

# 96. Important Pointer Relationships

Given:

```cpp
int a = 12;
int *ptr = &a;
int **ptr2 = &ptr;
```

Memorize:

```text
&a       → address of a
ptr      → address of a
*ptr     → a's value

&ptr     → address of ptr
ptr2     → address of ptr
*ptr2    → ptr
**ptr2   → a's value
```

---

# 97. Golden Pointer Table

| Expression | Meaning |
|---|---|
| `a` | Value of `a` |
| `&a` | Address of `a` |
| `ptr` | Address stored in `ptr` |
| `*ptr` | Value at address stored in `ptr` |
| `&ptr` | Address of pointer `ptr` |
| `ptr2` | Address stored in `ptr2` |
| `*ptr2` | Pointer `ptr` |
| `**ptr2` | Value of `a` |

---

# 98. Pointer Levels

```text
int a
```

One ordinary integer.

```text
int *p
```

Pointer to integer.

```text
int **pp
```

Pointer to pointer to integer.

```text
int ***ppp
```

Pointer to pointer to pointer to integer.

Think:

```text
***ppp
 ↓
**pp
 ↓
*p
 ↓
value
```

---

# 99. Pointer Questions You Must Be Able to Answer

### Q1
What is a pointer?

**Answer:**

A variable that stores the address of another object.

---

### Q2
What does `&a` mean?

**Answer:**

Address of `a`.

---

### Q3
What does `*ptr` mean?

**Answer:**

The object/value at the address stored in `ptr`.

---

### Q4
What does `int **ptr2` mean?

**Answer:**

A pointer to a pointer to an `int`.

---

### Q5
What does `nullptr` mean?

**Answer:**

A null pointer value that represents no valid pointed-to object.

---

### Q6
Can we dereference `nullptr`?

**Answer:**

No. Doing so is undefined behavior.

---

### Q7
What is a dangling pointer?

**Answer:**

A pointer whose pointed-to object's lifetime has ended or whose target is otherwise no longer valid.

---

### Q8
What is pointer arithmetic?

**Answer:**

Arithmetic on pointers to elements of an array/object sequence, where movement is measured in elements rather than raw bytes.

---

### Q9
What is `ptr + 1`?

**Answer:**

For a pointer into an array, a pointer to the next element.

---

### Q10
What is `arr[i]` equivalent to?

**Answer:**

```cpp
*(arr + i)
```

for ordinary array indexing.

---

# 100. Interview-Level Questions

### Q11
Difference between:

```cpp
int *p;
int **p;
```

### Q12
Difference between:

```cpp
p
*p
&p
```

### Q13
Difference between:

```cpp
*p++
(*p)++
```

### Q14
Difference between:

```cpp
*p + 1
*(p + 1)
```

### Q15
Difference between:

```cpp
.
->
```

### Q16
Difference between:

```cpp
int *p
const int *p
int *const p
const int *const p
```

### Q17
Why is:

```cpp
delete[]
```

used with:

```cpp
new[]
```

### Q18
Why can array pointers become invalid after vector reallocation?

### Q19
Why can a pointer become dangling?

### Q20
Why are pointers important in linked lists?

---

# 101. Pointer Practice Programs

## Program 1 — Print Value Through Pointer

```cpp
#include <iostream>
using namespace std;

int main() {

    int a = 25;

    int *ptr = &a;

    cout << *ptr;

    return 0;
}
```

Expected:

```text
25
```

---

## Program 2 — Modify Through Pointer

```cpp
int a = 10;

int *ptr = &a;

*ptr = 50;

cout << a;
```

Output:

```text
50
```

---

## Program 3 — Pointer to Pointer

```cpp
int a = 10;

int *p = &a;

int **pp = &p;

cout << **pp;
```

Output:

```text
10
```

---

## Program 4 — Array Traversal

```cpp
int arr[] = {10,20,30,40};

int *p = arr;

for(int i = 0; i < 4; i++) {
    cout << *(p + i) << " ";
}
```

Output:

```text
10 20 30 40
```

---

## Program 5 — Swap Using Pointers

```cpp
void swapValues(int *a, int *b) {

    int temp = *a;

    *a = *b;

    *b = temp;
}
```

Usage:

```cpp
int x = 10;
int y = 20;

swapValues(&x, &y);
```

Now:

```text
x = 20
y = 10
```

---

# 102. Swap — Why Pointers Work

Initially:

```text
x = 10
y = 20
```

Pass:

```cpp
&x
&y
```

Function receives their addresses.

Therefore:

```cpp
*a
```

refers to `x`.

And:

```cpp
*b
```

refers to `y`.

So:

```cpp
*a = *b;
```

can directly modify the caller's variables.

---
