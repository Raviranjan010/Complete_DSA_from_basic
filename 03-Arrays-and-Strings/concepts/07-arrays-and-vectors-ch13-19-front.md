[← Chapter 12](07-arrays-and-vectors-ch12-3-vector-header-file.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 14 →](07-arrays-and-vectors-ch14-37-auto-with-vector.md)

---

# 19. `front()`

`front()` returns a reference to the first element.

```cpp
vector<int> v = {10, 20, 30};

cout << v.front();
```

Output:

```text
10
```

---

# 20. `back()`

`back()` returns a reference to the last element.

```cpp
cout << v.back();
```

Output:

```text
30
```

---

# 21. Important Safety Rule for `front()` and `back()`

Do not call:

```cpp
v.front();
v.back();
```

on an empty vector.

Example:

```cpp
vector<int> v;

cout << v.front(); // invalid
```

Always understand whether the vector can be empty.

---

# 22. Accessing Elements with `[]`

You can access vector elements using the same index syntax as arrays.

```cpp
vector<int> v = {10, 20, 30};

cout << v[1];
```

Output:

```text
20
```

Complexity:

```text
O(1)
```

---

# 23. `at()`

`at()` accesses an element using an index.

```cpp
cout << v.at(1);
```

For a valid index:

```text
0 <= index < size
```

the element is returned.

Unlike `operator[]`, `at()` performs bounds checking and throws `std::out_of_range` when the index is invalid.

Example:

```cpp
vector<int> v = {10, 20, 30};

cout << v.at(5);
```

This throws an exception.

---

# 24. `[]` vs `at()`

| Feature | `v[index]` | `v.at(index)` |
|---|---|---|
| Access | Yes | Yes |
| Bounds checking | No | Yes |
| Invalid index | Undefined behavior | Throws `std::out_of_range` |
| Typical overhead | Lower | Bounds check |
| Complexity | O(1) | O(1) |

### DSA habit

Use `[]` when you know the index is valid and performance/simple syntax matters.

Use `at()` when explicit bounds checking is useful.

---

# 25. `clear()`

`clear()` removes all elements.

```cpp
vector<int> v = {10, 20, 30};

v.clear();
```

Now:

```text
size = 0
```

### Important

`clear()` destroys/removes the elements but does not necessarily reduce the vector's capacity.

So:

```text
size → 0
capacity → may remain unchanged
```

---

# 26. `empty()`

Use:

```cpp
v.empty()
```

It returns:

```text
true
```

if the vector contains no elements.

Example:

```cpp
if (v.empty()) {
    cout << "Vector is empty";
}
```

This is usually clearer than:

```cpp
if (v.size() == 0)
```

although both can express the same condition.

---

# 27. `insert()`

`insert()` inserts elements at a specified position.

Example:

```cpp
vector<int> v = {10, 20, 30};

v.insert(v.begin() + 1, 15);
```

Result:

```text
10 15 20 30
```

Why?

```text
v.begin()     → iterator to index 0
v.begin() + 1 → iterator to index 1
```

The new element is inserted before the element at index 1.

---

# 28. Inserting Multiple Copies

```cpp
vector<int> v = {10, 20, 30};

v.insert(v.begin() + 1, 3, 99);
```

Result:

```text
10 99 99 99 20 30
```

Syntax:

```cpp
insert(position, count, value)
```

---

# 29. `erase()`

Although not in the original function list, `erase()` is essential for vector DSA.

Remove one element:

```cpp
vector<int> v = {10, 20, 30};

v.erase(v.begin() + 1);
```

Result:

```text
10 30
```

The element at index 1 was removed.

---

# 30. Erasing a Range

```cpp
v.erase(v.begin() + 1, v.begin() + 3);
```

The range is:

```text
[first, last)
```

The first iterator is included, but the last iterator is excluded.

Example:

```text
10 20 30 40 50
```

Erase:

```cpp
v.erase(v.begin() + 1, v.begin() + 4);
```

Removes:

```text
20 30 40
```

Result:

```text
10 50
```

---

# 31. `resize()`

`resize()` changes the vector's size.

Example:

```cpp
vector<int> v = {1, 2, 3};

v.resize(5);
```

Result:

```text
1 2 3 0 0
```

For `int`, newly created elements are value-initialized to zero.

---

# 32. Resize to a Smaller Size

```cpp
vector<int> v = {1, 2, 3, 4, 5};

v.resize(3);
```

Result:

```text
1 2 3
```

The last two elements are removed.

---

# 33. `reserve()`

`reserve()` changes the **capacity**, not the size.

Example:

```cpp
vector<int> v;

v.reserve(100);
```

After this:

```text
size = 0
capacity >= 100
```

There are still **zero elements**.

This is a very important distinction:

```cpp
reserve(100);
```

does not create 100 elements.

---

# 34. `reserve()` vs `resize()`

| `reserve()` | `resize()` |
|---|---|
| Changes capacity | Changes size |
| Does not create elements | Creates/removes elements |
| `size` remains unchanged | `size` changes |
| Useful before many `push_back()` calls | Useful when you actually need a specific number of elements |

Example:

```cpp
vector<int> a;
a.reserve(5);
```

```text
size = 0
capacity >= 5
```

But:

```cpp
vector<int> b(5);
```

```text
size = 5
```

---

# 35. Range-Based For Loop

A vector can be traversed using:

```cpp
for (int x : vec) {
    cout << x << " ";
}
```

Example:

```cpp
vector<int> vec = {10, 20, 30};

for (int x : vec) {
    cout << x << " ";
}
```

Output:

```text
10 20 30
```

---

# 36. Modify Elements Using Reference

This:

```cpp
for (int x : vec) {
    x *= 2;
}
```

does not modify the vector because `x` is a copy.

Use:

```cpp
for (int &x : vec) {
    x *= 2;
}
```

Now the vector changes.

Example:

```text
Before:
1 2 3

After:
2 4 6
```

---
