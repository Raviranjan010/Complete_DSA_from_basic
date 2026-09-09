# 📘 Arrays in C++ — Complete Master Guide

## 1️⃣ What is an Array? (Core Idea)
An array in C++ is a collection of elements of the same data type stored in contiguous memory locations, accessed using a single name and an index.

## 2️⃣ Why Use Arrays?
*   **Store Multiple Values**: Hold a collection of related data items of the same type under a single variable name.
*   **Fast Access**: Elements can be accessed directly and efficiently using their index (constant time O(1)).
*   **Code Clarity & Conciseness**: Reduces the need for many individual variables, making code shorter and easier to manage.
*   **Foundation for Data Structures**: Serve as the building blocks for more complex data structures like matrices.

## 3️⃣ Basic Syntax
```cpp
data_type array_name[size];
```
**Example:**
```cpp
int marks; // Declares an array named 'marks' that can hold 5 integers.
```

## 4️⃣ Array Initialization

### 🅰️ Full Initialization
All elements are explicitly assigned values.
```cpp
int a = {10, 20, 30, 40, 50};
```

### 🅱️ Partial Initialization
If fewer values are provided than the array size, the remaining elements are **zero-initialized**.
```cpp
int a = {10, 20}; // a will be {10, 20, 0, 0, 0}
```
**Note**: For local non-static arrays, if no initializer is provided at all (e.g., `int arr[5];`), the elements will contain **garbage values**. If you use `int arr[5] = {};` or `int arr[5] = {0};`, all elements will be zero-initialized.

### 🆎 Automatic Size Detection
The compiler determines the size of the array based on the number of initializers.
```cpp
int a[] = {1, 2, 3}; // 'a' will have a size of 3.
```

## 5️⃣ Accessing Array Elements
Elements are accessed using the array name followed by their index in square brackets `[]`.
```cpp
int arr[] = {10, 20, 30};
cout << arr;  // Output: 10 (the first element)
cout << arr;  // Output: 30 (the third element)
```
**⚠️ Important**: Array indices always start from `0`. The last element of an array of size `N` is at index `N-1`.

## 6️⃣ Types of Arrays in C++

### 🅰️ One-Dimensional Array
A linear collection of elements.
```cpp
int arr; // An array of 5 integers
```

### 🅱️ Two-Dimensional Array (Matrices)
An array of arrays, often used to represent tables or grids.
```cpp
int matrix; // A 3x3 matrix
```

### 🆎 Multi-Dimensional Array
Arrays with more than two dimensions.
```cpp
int data; // A 2x3x4 3D array
```

## 7️⃣ Traversing an Array
Loops are commonly used to process each element in an array.
```cpp
#include <iostream>
using namespace std; // Added for cout, endl

int main() {
    int a[] = {1, 2, 3, 4, 5}; // Array of 5 integers
    int n = sizeof(a) / sizeof(a[0]); // Calculate number of elements

    for(int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}
```

## 8️⃣ Memory Concept (Crucial for Understanding Pointers)
Arrays are stored in **contiguous memory locations**. This means elements are placed right next to each other in memory.

**Address Calculation:**
The memory address of an element can be calculated using its index:
`Address of arr[i] = base_address + i × sizeof(data_type)`

**Example:** If `int arr[5]` starts at address `1000` and `sizeof(int)` is `4` bytes:
*   `arr[0]` is at `1000`
*   `arr[1]` is at `1000 + 1 * 4 = 1004`
*   `arr[2]` is at `1000 + 2 * 4 = 1008`

## 9️⃣ `sizeof()` Operator with Arrays
The `sizeof()` operator can be used to determine the size of an array in bytes and the number of elements.
```cpp
#include <iostream>
using namespace std; // Added for cout, endl

int main() {
    int a[] = {2, 4, 14}; // Array of 3 integers

    cout << "Size of array 'a' in bytes: " << sizeof(a) << endl; // Output: 12 (3 elements * 4 bytes/int)
    cout << "Size of an int in bytes: " << sizeof(int) << endl;   // Output: 4

    // Calculate the number of elements in a static array
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Number of elements in 'a': " << n << endl; // Output: 3
    return 0;
}
```
**⚠️ Important**: This `sizeof(array) / sizeof(element)` trick **only works for statically-sized C-style arrays**. It does **NOT** work for dynamically allocated arrays (e.g., `int* arr = new int[N];`).

## 🔟 Understanding Out-of-Bounds Access (Undefined Behavior)
Accessing an array element using an index that is outside its valid range (0 to `size-1`) leads to **undefined behavior**.

```cpp
int arr = {1, 2, 3, 4, 5};
cout << arr; // ❌ Dangerous! Accessing arr is out of bounds for a size-5 array (valid indices 0-4).
```
**Consequences of Out-of-Bounds Access:**
*   It might print a garbage value.
*   It might print `0`.
*   It might crash your program (segmentation fault).
*   It might corrupt other parts of your program's memory, leading to subtle bugs that are hard to trace.

**✅ Best Practice**: **NEVER** access elements outside the declared bounds of an array.

## 1️⃣1️⃣ Invalid Declarations & Best Practices

### ❌ Not Allowed (Compile-time Error)
```cpp
int a; // Arrays must have a positive size.
```

### ❌ Uninitialized Local Array (Garbage Values)
```cpp
int a; // Local non-static array, elements contain garbage
cout << a; // Output will be an unpredictable garbage value.
```

### ✅ Zero Initialization (Recommended for C-style arrays)
```cpp
int a = {}; // All elements are initialized to 0.
```

## 1️⃣2️⃣ Dynamic Sizing (C-style Arrays)
C-style arrays require their size to be known at compile time. If you need an array whose size is determined at runtime (e.g., by user input), you typically use dynamic memory allocation with `new` and `delete` or, for modern C++, `std::vector`.

**⚠️ Variable Length Arrays (VLAs)**: `int arr[n];` where `n` is a variable, is a feature from C99 and is **not standard C++**. While some compilers support it as an extension, it's best to avoid it for portability and safety. For fixed-size arrays, `n` must be a compile-time constant.

### 🅰️ Taking Array Size as Input (using dynamic allocation)
```cpp
#include <iostream>

int main() {
    int n;
    std::cout << "Enter size of array: ";
    std::cin >> n;

    // Dynamically allocate memory for 'n' integers
    int* arr = new int[n];

    std::cout << "Elements (uninitialized, will contain garbage):\n";
    for(int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    delete[] arr; // Free the dynamically allocated memory
    arr = nullptr; // Good practice to avoid dangling pointers
    return 0;
}
```

### 🅱️ Taking Array Elements as Input (using dynamic allocation)
```cpp
#include <iostream>

int main() {
    int n;
    std::cout << "Enter number of elements: ";
    std::cin >> n;

    int* arr = new int[n]; // Dynamically allocate memory

    std::cout << "Enter " << n << " elements:\n";
    for(int i = 0; i < n; i++) {
        std::cin >> arr[i]; // Take input into the array
    }

    std::cout << "Elements entered:\n";
    for(int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    delete[] arr; // Free the dynamically allocated memory
    arr = nullptr;
    return 0;
}
```

## 1️⃣3️⃣ Advantages of Arrays
*   **Fast Access**: O(1) time complexity for accessing any element by index.
*   **Simple Structure**: Easy to understand and implement.
*   **Efficient Memory Usage**: Elements are stored contiguously, leading to good cache performance.
*   **Foundation**: Basis for many other data structures.

## 1️⃣4️⃣ Limitations of Arrays
*   **Fixed Size (C-style Arrays)**: Once declared, the size of a C-style array cannot be changed. This can lead to wasted memory or overflow issues. Dynamic allocation (`new`/`delete`) can mitigate this but adds complexity.
*   **Homogeneous Data**: Can only store elements of the same data type.
*   **Out-of-Bounds Errors**: No automatic bounds checking, making it prone to dangerous runtime errors.
*   **Insertion/Deletion**: Inefficient for inserting or deleting elements in the middle, as it requires shifting many elements.

---

# 🔢 Number Systems & Decimal Logic

Understanding number systems is foundational, especially when working with low-level concepts like memory and data representation. Computers fundamentally operate in binary.

## 1️⃣ What is a Number System?
A number system defines how numbers are represented using digits and a base (radix).

| Number System | Base | Digits Used | Example |
| :------------ | :--- | :---------- | :------ |
| **Decimal**   | 10   | 0–9         | 12, 99, 105 |
| **Binary**    | 2    | 0, 1        | 101, 1100 |
| **Octal**     | 8    | 0–7         | 17, 24  |
| **Hexadecimal** | 16   | 0–9, A–F    | 1A, F2, B5 |

## 2️⃣ Decimal Number System (Base-10)
The decimal system is the number system we use daily. It uses 10 unique digits (0–9). Each digit's position in a number represents a power of 10.

### Example: Breakdown of `739`
*   `7` is in the hundreds place: $7 \times 10^2 = 700$
*   `3` is in the tens place: $3 \times 10^1 = 30$
*   `9` is in the units place: $9 \times 10^0 = 9$
*   **Total**: $700 + 30 + 9 = 739$

### Why do computers use Binary?
Computers are built from transistors, which act as tiny switches. These switches have only two stable states:
*   **ON** (High Voltage) = **1**
*   **OFF** (Low Voltage) = **0**
This inherent two-state nature makes binary (base-2) the most natural and efficient number system for computers.

---

# 🧠 MASTER TRICKS & POINTS TO REMEMBER (Arrays)

*   **Homogeneous Elements**: Arrays store elements of the same data type only.
*   **Contiguous Memory**: Elements are stored sequentially in memory.
*   **Zero-Based Indexing**: The first element is at index `0`, the last at `size - 1`.
*   **Fixed Size (C-style)**: Once declared, the size of a C-style array cannot be changed. Use dynamic allocation (`new`/`delete`) for runtime sizing.
*   **`sizeof()` for Static Arrays**: `sizeof(arr) / sizeof(arr[0])` gives the number of elements for static C-style arrays.
*   **Pass by Pointer to Functions**: When passing C-style arrays to functions, they decay to pointers. To modify the original array, you typically pass a pointer and its size.
*   **Initialization**: Always initialize arrays to avoid garbage values. `int arr[5] = {};` initializes all to zero.

---

# ❌ Common Array Mistakes (Exam Traps & Pitfalls)

1.  **Out-of-Bounds Access**:
    ```cpp
    int arr;
    arr = 10; // ❌ CRASH/UNDEFINED BEHAVIOR
    ```
    **Fix**: Ensure indices are always within `0` to `size-1`.

2.  **Using Uninitialized Local Arrays**:
    ```cpp
    int arr;
    cout << arr; // ❌ Prints garbage value
    ```
    **Fix**: Always initialize arrays: `int arr[5] = {};` or `int arr[5] = {1,2,3,4,5};`.

3.  **Variable Length Arrays (VLAs) in C++**:
    ```cpp
    int n;
    cin >> n;
    int arr[n]; // ❌ Not standard C++ (C99 feature), use dynamic allocation (new/delete) instead.
    ```
    **Fix**: Use `int* arr = new int[n];` and remember `delete[] arr;`.

4.  **Incorrect `sizeof()` with Pointers**:
    ```cpp
    void func(int* arr, int size) {
        // int n = sizeof(arr) / sizeof(arr); // ❌ Incorrect! arr is a pointer here, not the array itself.
    }
    ```
    **Fix**: Pass size explicitly for C-style arrays in functions.

5.  **Initializing `max` with `0` for finding maximum**:
    ```cpp
    int arr[] = {-5, -2, -8};
    int max_val = 0; // ❌ If all numbers are negative, this is wrong.
    for (int x : arr) { if (x > max_val) max_val = x; }
    // Output: 0 (Incorrect)
    ```
    **Fix**: Initialize `max_val` with the first element of the array, or use `numeric_limits<int>::min()`.
    ```cpp
    #include <limits> // Required for numeric_limits
    // ...
    int max_val = arr; // Correct, assuming array is not empty
    // Or: int max_val = numeric_limits<int>::min();
    ```

6.  **Confusing Array Name with Pointer**:
    While an array name often decays to a pointer to its first element, they are not identical. You cannot reassign an array name.
    ```cpp
    int arr;
    // int* p = arr; // Valid
    // arr = some_other_array; // ❌ Invalid: Cannot assign to an array type
    ```

---

# 📘 Array Programs in C++ (Sum, Max, Reverse)

Below are clean, exam-ready, beginner-friendly array programs using C-style arrays.

## 1️⃣ Program to Find Sum of Array Elements

### 🔹 Logic
1.  Initialize a `sum` variable to `0`.
2.  Iterate through each element of the array.
3.  Add each element's value to `sum`.

### ✅ Using C-style Array
```cpp
#include <iostream>
using namespace std; // Added for cout, endl

int main() {
    int arr[] = {2, 4, 6, 8};
    int n = sizeof(arr) / sizeof(arr); // Calculate number of elements
    int sum = 0;

    for(int i = 0; i < n; i++) {
        sum += arr[i];
    }

    cout << "Sum = " << sum << endl; // Output: Sum = 20
    return 0;
}
```

## 2️⃣ Program to Find Maximum Element

### 🔹 Logic
1.  Assume the first element of the array is the maximum.
2.  Iterate through the rest of the array (from the second element).
3.  If any element is greater than the current maximum, update the maximum.

### ✅ Using C-style Array
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {15, 3, 22, 9, 10};

    // Correct way to calculate number of elements
    int n = sizeof(arr) / sizeof(arr[0]);

    // Assume first element is maximum
    int max_val = arr[0];

    // Start loop from index 1 (index 0 already used)
    for(int i = 1; i < n; i++) {
        if(arr[i] > max_val) {
            max_val = arr[i];
        }
    }

    cout << "Maximum = " << max_val << endl;
    return 0;
}

```
**⚠️ Important**: Never initialize `max_val` with `0` if the array might contain all negative numbers.

## 3️⃣ Program to Reverse an Array (In-Place)

### 🔹 Logic
1.  Use two pointers: `start` at the beginning and `end` at the end of the array.
2.  Swap the elements at `start` and `end`.
3.  Move `start` one step forward and `end` one step backward.
4.  Continue until `start` crosses `end`.

### ✅ Using C-style Array
```cpp
#include <iostream>
#include <algorithm> // Required for swap
using namespace std; // Added for cout, endl

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr);

    int start = 0;
    int end = n - 1;

    while(start < end) {
        // Swap elements at start and end
        swap(arr[start], arr[end]);
        // Or manually:
        // int temp = arr[start];
        // arr[start] = arr[end];
        // arr[end] = temp;

        start++;
        end--;
    }

    cout << "Reversed Array:\n";
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl; // Output: 5 4 3 2 1
    return 0;
}
```

## 🧠 Time & Space Complexity (Exam Point)

| Program           | Time Complexity | Extra Space Complexity |
| :---------------- | :-------------- | :--------------------- |
| Sum of Elements   | O(n)            | O(1)                   |
| Maximum Element   | O(n)            | O(1)                   |
| Reverse Array     | O(n)            | O(1)                   |

---