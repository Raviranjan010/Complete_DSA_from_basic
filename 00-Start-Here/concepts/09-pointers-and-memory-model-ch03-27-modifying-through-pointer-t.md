[← Chapter 02](09-pointers-and-memory-model-ch02-13-pointer-and-variable-are-di.md) · [Chapter Index](09-pointers-and-memory-model.md) · [Module Overview](../README.md) · [Chapter 04 →](09-pointers-and-memory-model-ch04-42-pass-by-value-vs-pointer.md)

---

# 27. Modifying Through Pointer-to-Pointer

Example:

```cpp
int a = 12;

int *ptr = &a;

int **ptr2 = &ptr;

**ptr2 = 100;
```

Now:

```text
a = 100
```

because:

```text
ptr2
 ↓
ptr
 ↓
a
```

and:

```text
**ptr2
```

reaches `a`.

---

# 28. Pointer Arithmetic

Pointers support arithmetic when they point into an array or one-past its end.

Example:

```cpp
int arr[] = {10,20,30,40};

int *ptr = arr;
```

Initially:

```text
ptr → arr[0]
```

Then:

```cpp
ptr++;
```

Now:

```text
ptr → arr[1]
```

Another:

```cpp
ptr++;
```

Now:

```text
ptr → arr[2]
```

---

# 29. Important Pointer Arithmetic Rule

If:

```cpp
int *ptr;
```

then:

```cpp
ptr + 1
```

does **not** necessarily mean:

```text
address + 1 byte
```

It means:

> Move to the next `int` object.

If `sizeof(int) == 4`, the underlying byte address typically changes by 4 bytes.

Example conceptually:

```text
1000 → arr[0]
1004 → arr[1]
1008 → arr[2]
1012 → arr[3]
```

But actual addresses depend on the implementation.

---

# 30. Pointer Arithmetic With Arrays

```cpp
int arr[] = {10,20,30,40};

int *ptr = arr;

cout << *ptr << endl;       // 10
cout << *(ptr + 1) << endl; // 20
cout << *(ptr + 2) << endl; // 30
cout << *(ptr + 3) << endl; // 40
```

This is a fundamental relationship:

```text
arr[i] == *(arr + i)
```

---

# 31. Array Name and Pointer

For most expressions, an array name can decay into a pointer to its first element.

Example:

```cpp
int arr[] = {10,20,30};

int *ptr = arr;
```

This is equivalent to:

```cpp
int *ptr = &arr[0];
```

Therefore:

```text
arr → address of first element in many expressions
```

But an array is **not itself a pointer**.

This distinction is very important.

---

# 32. Array vs Pointer

```cpp
int arr[5];
int *ptr = arr;
```

They are not the same type.

```text
arr → array of 5 int
ptr → pointer to int
```

For example:

```cpp
sizeof(arr)
```

returns the size of the entire array when `arr` is an actual array in that scope.

But:

```cpp
sizeof(ptr)
```

returns the size of the pointer.

This is one of the easiest ways to see that arrays and pointers are different.

---

# 33. Pointer Increment

Example:

```cpp
int arr[] = {10,20,30};

int *ptr = arr;

cout << *ptr << endl;

ptr++;

cout << *ptr << endl;
```

Output:

```text
10
20
```

Pointer increment changes which array element it points to.

It does not modify the array element itself.

---

# 34. Pointer Decrement

```cpp
ptr--;
```

moves the pointer to the previous element.

Example:

```text
arr[0] ← arr[1] ← arr[2]
```

If:

```text
ptr → arr[2]
```

then:

```cpp
ptr--;
```

gives:

```text
ptr → arr[1]
```

---

# 35. Pointer + Integer

```cpp
ptr + 3
```

means:

> Move three elements forward.

Example:

```cpp
int arr[] = {10,20,30,40,50};

int *ptr = arr;

cout << *(ptr + 3);
```

Output:

```text
40
```

---

# 36. Pointer - Integer

```cpp
ptr - 2
```

means:

> Move two elements backward.

Example:

```cpp
int *ptr = &arr[4];

cout << *(ptr - 2);
```

This accesses:

```text
arr[2]
```

---

# 37. Pointer Difference

If two pointers point into the same array, subtracting them gives the number of elements between them.

Example:

```cpp
int arr[] = {10,20,30,40,50};

int *p = &arr[1];
int *q = &arr[4];

cout << q - p;
```

Output:

```text
3
```

Because:

```text
arr[4] - arr[1]
```

represents three element positions.

---

# 38. Comparing Pointers

Pointers can be compared.

For pointers into the same array, relational comparisons can be used meaningfully:

```cpp
p < q
p > q
p <= q
p >= q
```

Equality comparisons are also common:

```cpp
p == q
p != q
```

For example:

```cpp
if(ptr == nullptr) {
}
```

---

# 39. One-Past-the-End Pointer

For an array:

```cpp
int arr[5];
```

the pointer:

```cpp
arr + 5
```

is allowed as a pointer value for one-past-the-end.

But:

```cpp
*(arr + 5)
```

is invalid because there is no element at index `5`.

This is why loops often use:

```cpp
for(int *p = arr; p != arr + 5; p++) {
    cout << *p;
}
```

---

# 40. Pointer Traversal of an Array

```cpp
int arr[] = {10,20,30,40};

int *ptr = arr;

for(int i = 0; i < 4; i++) {
    cout << *(ptr + i) << " ";
}
```

Output:

```text
10 20 30 40
```

Another form:

```cpp
for(int *p = arr; p != arr + 4; p++) {
    cout << *p << " ";
}
```

---

# 41. Pointers and Functions

Pointers allow a function to modify the caller's object.

Example:

```cpp
void change(int *ptr) {
    *ptr = 100;
}

int main() {

    int a = 10;

    change(&a);

    cout << a;
}
```

Output:

```text
100
```

---
