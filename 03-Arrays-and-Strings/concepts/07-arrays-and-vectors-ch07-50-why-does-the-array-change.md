[← Chapter 06](07-arrays-and-vectors-ch06-36-swapping-maximum-and-minimu.md) · [Chapter Index](07-arrays-and-vectors-guide.md) · [Module Overview](../README.md) · [Chapter 08 →](07-arrays-and-vectors-ch08-66-intersection-of-two-arrays.md)

---

# 50. Why Does the Array Change?

Because the function receives access to the same underlying array storage.

Conceptually:

```text
main array
   ↓
[1][2][3][4][5]
   ↑
   |
function accesses same elements
```

So:

```cpp
arr[i] *= 2;
```

modifies the original elements.

---

# 51. `const` Array Parameter

If a function should only read the array and must not modify it:

```cpp
void printArray(const int arr[], int n) {

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}
```

This gives the function a read-only view of the elements.

This is a very good habit for functions that do not need to modify the array.

---

# 52. Array of Characters

An array can store characters:

```cpp
char letters[] = {'A', 'B', 'C'};
```

It can also represent a C-style string:

```cpp
char name[] = "Ravi";
```

The second form contains an additional null terminator:

```text
R a v i \0
```

---

# 53. Two-Dimensional Array

A two-dimensional array is an array arranged in rows and columns.

```cpp
int matrix[3][4];
```

This means:

```text
3 rows
4 columns
```

Conceptually:

```text
[ ][ ][ ][ ]
[ ][ ][ ][ ]
[ ][ ][ ][ ]
```

Access:

```cpp
matrix[row][column]
```

Example:

```cpp
matrix[1][2]
```

means:

```text
row = 1
column = 2
```

---

# 54. Traversing a 2D Array

```cpp
for (int i = 0; i < rows; i++) {

    for (int j = 0; j < cols; j++) {

        cout << matrix[i][j] << " ";
    }

    cout << "\n";
}
```

Complexity:

```text
O(rows × cols)
```

---

# 55. Row Sum

For a matrix:

```cpp
for (int i = 0; i < rows; i++) {

    int sum = 0;

    for (int j = 0; j < cols; j++) {
        sum += matrix[i][j];
    }

    cout << "Row " << i << ": " << sum << "\n";
}
```

---

# 56. Column Sum

```cpp
for (int j = 0; j < cols; j++) {

    int sum = 0;

    for (int i = 0; i < rows; i++) {
        sum += matrix[i][j];
    }

    cout << "Column " << j << ": " << sum << "\n";
}
```

---

# 57. Primary Diagonal

For a square matrix:

```text
1 2 3
4 5 6
7 8 9
```

Primary diagonal:

```text
1
  5
    9
```

Condition:

```cpp
i == j
```

Example:

```cpp
for (int i = 0; i < n; i++) {
    cout << matrix[i][i] << " ";
}
```

Output:

```text
1 5 9
```

---

# 58. Secondary Diagonal

For:

```text
1 2 3
4 5 6
7 8 9
```

Secondary diagonal:

```text
    3
  5
7
```

Condition:

```text
i + j = n - 1
```

Code:

```cpp
for (int i = 0; i < n; i++) {
    cout << matrix[i][n - 1 - i] << " ";
}
```

---

# 59. Array Rotation

Rotation is different from reversal.

### Left rotation by 1

```text
1 2 3 4 5
```

becomes:

```text
2 3 4 5 1
```

### Right rotation by 1

```text
1 2 3 4 5
```

becomes:

```text
5 1 2 3 4
```

Rotation is a very common array interview problem.

---

# 60. Left Rotation by One

Simple approach:

```cpp
int first = arr[0];

for (int i = 0; i < n - 1; i++) {
    arr[i] = arr[i + 1];
}

arr[n - 1] = first;
```

Example:

```text
Before:
1 2 3 4 5

After:
2 3 4 5 1
```

---

# 61. Right Rotation by One

```cpp
int last = arr[n - 1];

for (int i = n - 1; i > 0; i--) {
    arr[i] = arr[i - 1];
}

arr[0] = last;
```

Example:

```text
Before:
1 2 3 4 5

After:
5 1 2 3 4
```

---

# 62. Move Zeros to the End

### Problem

Input:

```text
0 1 0 3 12
```

Output:

```text
1 3 12 0 0
```

A common two-pointer approach:

```cpp
int j = 0;

for (int i = 0; i < n; i++) {

    if (arr[i] != 0) {
        swap(arr[i], arr[j]);
        j++;
    }
}
```

### Complexity

```text
Time  = O(n)
Space = O(1)
```

---

# 63. Find Second Largest Element

Do not simply sort the array unless sorting is actually allowed.

A one-pass approach:

```cpp
long long largest = LLONG_MIN;
long long secondLargest = LLONG_MIN;

for (int i = 0; i < n; i++) {

    if (arr[i] > largest) {
        secondLargest = largest;
        largest = arr[i];
    }
    else if (arr[i] > secondLargest && arr[i] != largest) {
        secondLargest = arr[i];
    }
}
```

### Important

Clarify whether "second largest" means:

- second largest **distinct** value
- second element after sorting, where duplicates may count

These are different problems.

---

# 64. Find Missing Number

Suppose the array contains numbers from:

```text
0 to n
```

with exactly one missing.

Example:

```text
0 1 3 4
```

Missing:

```text
2
```

One mathematical approach:

```cpp
long long expected = 1LL * n * (n + 1) / 2;

long long actual = 0;

for (int x : arr) {
    actual += x;
}

cout << expected - actual;
```

---

# 65. Duplicate Element

Example:

```text
1 3 4 2 2
```

The duplicate is:

```text
2
```

There are multiple approaches depending on constraints:

- nested loops
- sorting
- frequency array
- `set` / `unordered_set`
- Floyd's cycle detection for special problem constraints

Do not automatically choose one method without checking the constraints.

---
