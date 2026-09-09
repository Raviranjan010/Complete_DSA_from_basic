# Pointers and Arrays in C++ 🧠

Understanding the relationship between pointers and arrays is fundamental in C++ programming, as arrays often "decay" into pointers in various contexts.

## 1️⃣ Array Name as a Constant Pointer

In C++, an array's name, when used in an expression (except when used with `sizeof`, `&` operator, or to initialize a `std::string` or `std::vector`), **decays into a pointer** to its first element. This means the array name essentially holds the memory address of its first element.

*   **Core Idea**: The array name itself is a constant pointer to the first element of the array.
*   **Behavior**: You cannot reassign an array name to point to a different memory location.

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(int);

    cout << "Address of array (arr): " << arr << endl;         // Output: Address of the first element
    cout << "Address of first element (&arr): " << &arr << endl; // Output: Same address as above
    cout << "Value at first index (*arr): " << *arr << endl;   // Output: 10
    cout << "Value at second index (*(arr+1)): " << *(arr + 1) << endl; // Output: 20

    // arr = some_other_address; // ❌ ERROR: Cannot assign to an array type (arr is a constant pointer)

    return 0;
}
```

### ❌ Why `arr = &y;` (or similar) is an Error
When you declare `int arr[5];`, `arr` is a fixed-size block of memory, and its name `arr` is a constant pointer to the beginning of that block. You cannot change what `arr` points to.

## 2️⃣ Pointer Variables vs. Array Names

| Feature           | Pointer Variable (e.g., `int* ptr`) | Array Name (e.g., `int arr[]`) |
| :---------------- | :---------------------------------- | :----------------------------- |
| **Type**          | A variable that stores an address   | A constant pointer to its first element |
| **Reassignment**  | Can be reassigned to point to other addresses | Cannot be reassigned |
| **`sizeof`**      | Returns size of the pointer itself (e.g., 4 or 8 bytes) | Returns total size of the array in bytes |

## 3️⃣ Pointer Arithmetic
Pointer arithmetic is performed based on the size of the data type the pointer points to. When you increment a pointer, it moves to the next memory location of that data type, not just the next byte.

### Rules
*   **`ptr + n`**: Moves the pointer `n` positions forward, where each position is `sizeof(data_type)` bytes.
*   **`ptr - n`**: Moves the pointer `n` positions backward.
*   **`ptr2 - ptr1`**: Calculates the number of elements between `ptr2` and `ptr1` (only valid if both pointers point to elements within the same array).

### ❌ Not Allowed
*   `ptr1 + ptr2` (Adding two addresses doesn't make sense).
*   `ptr * ptr`
*   `ptr / ptr`

### Example: Pointer Increment
```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int *aptr = &a;

    cout << "Address of 'a': " << aptr << endl; // e.g., 0x7ffee5a0a9c4
    aptr++; // Increments by sizeof(int), typically 4 bytes
    cout << "Address after aptr++: " << aptr << endl; // e.g., 0x7ffee5a0a9c8 (original + 4 bytes)

    char c = 'X';
    char *cptr = &c;
    cout << "Address of 'c': " << (void*)cptr << endl; // Cast to void* for char* address output
    cptr++; // Increments by sizeof(char), typically 1 byte
    cout << "Address after cptr++: " << (void*)cptr << endl; // e.g., original + 1 byte

    return 0;
}
```

### Example: Pointer Subtraction
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *ptr1 = arr;        // Points to arr
    int *ptr2 = arr + 3;    // Points to arr

    cout << "Value at ptr1: " << *ptr1 << endl; // Output: 1
    cout << "Value at ptr2: " << *ptr2 << endl; // Output: 4

    // Difference between pointers (number of elements)
    cout << "Number of elements between ptr2 and ptr1: " << ptr2 - ptr1 << endl; // Output: 3

    return 0;
}
```

## 4️⃣ Accessing Array Elements with Pointers
The square bracket notation `arr[i]` is syntactic sugar for pointer arithmetic: `*(arr + i)`.

### Example
```cpp
#include <iostream>
using namespace std;

void printArray(int *arr, int n) { // arr is received as a pointer
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";      // Equivalent to *(arr + i)
    }
    cout << endl;
}

int main() {
    int myArr[] = {2, 4, 55, 323, 21, 32};
    int n = sizeof(myArr) / sizeof(int);
    
    printArray(myArr, n); // Output: 2 4 55 323 21 32
    return 0;
}
```

## 5️⃣ Passing Arrays to Functions
When an array is passed to a function in C++, it is always passed by reference (specifically, the array name decays to a pointer to its first element). This means any modifications made to the array inside the function will affect the original array.

*   **Syntax**: Both `void func(int arr[], int n)` and `void func(int *arr, int n)` are equivalent.
*   **`sizeof()` Limitation**: Inside a function, `sizeof(arr)` (where `arr` is a parameter) will return the size of a pointer, not the size of the actual array. Therefore, you must always pass the array's logical size as a separate argument.

### Example
```cpp
#include <iostream>
using namespace std;

void modifyArray(int arr[], int n) { // arr is a pointer here
    arr = 99; // Modifies the original array
    // cout << "Size of arr inside function: " << sizeof(arr) << endl; // This would print size of pointer (e.g., 8), not the array size
}

int main() {
    int myArr[] = {1, 2, 3};
    int n = sizeof(myArr) / sizeof(int); // n will be 3

    cout << "Original myArr: " << myArr << endl; // Output: 1
    modifyArray(myArr, n);
    cout << "Modified myArr: " << myArr << endl; // Output: 99

    return 0;
}
```

## 6️⃣ Key Takeaways
*   An array name is a **constant pointer** to its first element.
*   Pointers are **variables** that store addresses and can be reassigned.
*   Pointer arithmetic scales by the **size of the data type**.
*   `arr[i]` is equivalent to `*(arr + i)`.
*   Arrays are passed to functions **by reference** (via pointer decay), so changes persist.
*   Always pass the **size of the array** as a separate argument to functions.
```