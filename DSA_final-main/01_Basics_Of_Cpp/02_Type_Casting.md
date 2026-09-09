## Type Casting in C++

Type casting is the process of converting one data type into another. In C++, this can happen automatically (implicit) or manually (explicit).

### 1. Implicit Type Casting (Automatic)
Also known as type promotion. This happens automatically when a smaller data type is converted to a larger data type to prevent data loss, or when types are mixed in an expression.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    float b = a; // int -> float automatically
    cout << b << endl; // Output: 10

    char c = 'A';
    int x = c + 1; // char -> int automatically (ASCII value used)
    cout << x << endl; // Output: 66
    return 0;
}
```

*   **Type Promotion**: Small data types (like `char`, `short`) are promoted to `int` during arithmetic operations.
*   **Hierarchy**: `bool` -> `char` -> `int` -> `long` -> `float` -> `double` -> `long double`.

### 2. Explicit Type Casting (Manual)
This is when the programmer manually converts one type to another. This is necessary when converting larger types to smaller types (which might cause data loss) or when specific arithmetic behavior is needed.

#### C-Style Casting
Syntax: `(type) expression`

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 45;
    float b = 23.3;

    cout << (int)b << endl;          // Output: 23 (Decimal part discarded)
    cout << (float)10 / 3 << endl;   // Output: 3.33333 (Floating point division)
    cout << (char)('A' + 4) << endl; // Output: E (65 + 4 = 69 -> 'E')
    return 0;
}
```

*   `(int)b`: Converts 23.3 to 23. The decimal part is truncated, not rounded.
*   `(float)10 / 3`: Converts integer 10 to 10.0, forcing floating-point division. Integer division `10/3` would result in `3`.

#### C++ Style Casting
C++ introduces specific casting operators for safer conversions.

*   `static_cast`: Safe numeric conversion (e.g., `float` to `int`).
*   `dynamic_cast`: Used for runtime polymorphism.
*   `const_cast`: Used to remove `const` qualification.
*   `reinterpret_cast`: Low-level memory casting.

```cpp
float x = 10.7;
int y = static_cast<int>(x); // y becomes 10
```

### 3. Character Arithmetic & ASCII
Characters in C++ are stored internally as ASCII integer values. When arithmetic is performed on `char`, it is implicitly converted to `int`.

```cpp
cout << ('A' + 1) << endl;   // Output: 66
cout << ('A' + 0) << endl;   // Output: 65
cout << ('b' + 0) << endl;   // Output: 98
```

*   **'A'**: ASCII value 65.
*   **'b'**: ASCII value 98.
*   **'A' + 1**: 65 + 1 = 66. Since the result is an `int`, it prints 66.

### 4. Boolean Type Casting
Boolean values are treated as integers in arithmetic expressions.

```cpp
cout << ((bool)3 + 2) << endl; // Output: 3
```

*   `bool(0)` is `false` (0).
*   `bool(non-zero)` is `true` (1).
*   In the example: `(bool)3` becomes `true` (1). `1 + 2 = 3`.

### 5. Mixed Data Types & Common Errors

#### Valid Mixed Arithmetic
```cpp
cout << (22.2 + 3 + 'A') << endl; // Output: 90.2
```
*   'A' is promoted to 65.
*   22.2 (double) + 3 (int) + 65 (int) -> Result is `double` (90.2).

#### Invalid String Arithmetic
```cpp
// cout << (22.2 + 3 + "A") << endl; // ERROR
```
*   `'A'` (Single Quotes): Character literal (char). Stored as ASCII number. Arithmetic allowed.
*   `"A"` (Double Quotes): String literal. Stored as a memory address (`const char*`). You cannot add numbers directly to a string pointer in this way.

### Summary Table

| Expression | Type | Explanation |
| :--- | :--- | :--- |
| `'A'` | `char` | Character 'A' (ASCII 65) |
| `"A"` | `const char*` | String containing "A" and null terminator |
| `(int)23.9` | `int` | 23 (Truncated) |
| `10 / 3` | `int` | 3 (Integer division) |
| `10.0 / 3` | `double` | 3.3333... (Float division) |