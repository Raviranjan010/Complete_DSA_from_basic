# 🔢 Number Systems & Binary Logic (Complete Guide)

## 1️⃣ What is a Number System?
A number system defines how numbers are represented using digits and a base (radix).

| Number System | Base | Digits Used | Example |
| :--- | :--- | :--- | :--- |
| **Decimal** | 10 | 0–9 | 12, 99, 105 |
| **Binary** | 2 | 0, 1 | 101, 1100 |
| **Octal** | 8 | 0–7 | 17, 24 |
| **Hexadecimal** | 16 | 0–9, A–F | 1A, F2, B5 |

---

## 2️⃣ Decimal Number System (Base-10)
The decimal system uses 10 digits (0–9).
Each digit’s position represents a power of 10.

### Example
`739` breakdown:
*   $7 \times 10^2 = 700$
*   $3 \times 10^1 = 30$
*   $9 \times 10^0 = 9$
*   **Total**: 739

### Why do computers use Binary?
Computers are made of transistors which act as switches. They have only two stable states:
*   **ON** (High Voltage) = **1**
*   **OFF** (Low Voltage) = **0**

---

## 3️⃣ Binary Number System (Base-2)
Uses only two digits: **0** and **1**.

### Place Values (Powers of 2)
| Position | Power | Value |
| :--- | :--- | :--- |
| 0 (Rightmost) | $2^0$ | 1 |
| 1 | $2^1$ | 2 |
| 2 | $2^2$ | 4 |
| 3 | $2^3$ | 8 |
| 4 | $2^4$ | 16 |
| 5 | $2^5$ | 32 |

### Binary Counting (0 to 10)
| Decimal | Binary | Logic |
| :--- | :--- | :--- |
| 0 | 0 | |
| 1 | 1 | |
| 2 | 10 | (1 reset to 0, carry over 1) |
| 3 | 11 | |
| 4 | 100 | (11 reset to 00, carry over 1) |
| 5 | 101 | |
| 6 | 110 | |
| 7 | 111 | |
| 8 | 1000 | |
| 9 | 1001 | |
| 10 | 1010 | |

---

## 4️⃣ Conversions

### A. Binary to Decimal
**Rule**: Multiply each bit by $2^n$ (based on its position) and sum them up.

**Example**: `100101`
```text
1  0  0  1  0  1
│  │  │  │  │  └─ 1 × 2⁰ = 1
│  │  │  │  └─── 0 × 2¹ = 0
│  │  │  └────── 1 × 2² = 4
│  │  └───────── 0 × 2³ = 0
│  └──────────── 0 × 2⁴ = 0
└─────────────── 1 × 2⁵ = 32
---------------------------
Total = 37
```

#### C++ Code (Binary to Decimal)
```cpp
#include <iostream>
#include <cmath>
using namespace std;

int binaryToDecimal(int n) {
    int ans = 0;
    int i = 0;
    while(n != 0) {
        int digit = n % 10;
        if(digit == 1) {
            ans = ans + pow(2, i);
        }
        n = n / 10;
        i++;
    }
    return ans;
}
```

### B. Decimal to Binary
**Rule**: Divide by 2 repeatedly, store the remainder, then reverse the remainders.

**Example**: `37`
1.  37 / 2 = 18, Remainder = **1**
2.  18 / 2 = 9,  Remainder = **0**
3.  9 / 2  = 4,  Remainder = **1**
4.  4 / 2  = 2,  Remainder = **0**
5.  2 / 2  = 1,  Remainder = **0**
6.  1 / 2  = 0,  Remainder = **1**

Reverse Remainders: **100101**

#### C++ Code (Decimal to Binary)
```cpp
#include <iostream>
#include <cmath>
using namespace std;

int decimalToBinary(int n) {
    int ans = 0;
    int i = 0;
    while(n != 0) {
        int bit = n & 1; // Get last bit
        ans = (bit * pow(10, i)) + ans; // Store in reverse order visually
        n = n >> 1; // Right shift (divide by 2)
        i++;
    }
    return ans;
}
```

---

## 5️⃣ How Negative Numbers are Stored (Two's Complement)
Computers store negative numbers using **Two's Complement**.

### Steps to store -5:
1.  **Take positive value**: 5 → `0000 0101` (8-bit)
2.  **1's Complement**: Invert all bits (0→1, 1→0).
    *   `1111 1010`
3.  **2's Complement**: Add 1 to the result.
    *   `1111 1010 + 1 = 1111 1011`

So, `-5` in memory is `11111011`.

### Why?
It allows the CPU to perform subtraction using addition logic.
`5 + (-5) = 0`
`0000 0101 + 1111 1011 = 1 0000 0000` (The carry is discarded, result is 0).

---

## 6️⃣ Bitwise Operators (The Tools)
These operators work directly on bits. They are faster than arithmetic operators.

| Operator | Name | Description | Example (A=5 `101`, B=3 `011`) |
| :--- | :--- | :--- | :--- |
| `&` | **AND** | 1 if both bits are 1. | `5 & 3` → `101 & 011` = `001` (1) |
| `\|` | **OR** | 1 if at least one bit is 1. | `5 \| 3` → `101 \| 011` = `111` (7) |
| `^` | **XOR** | 1 if bits are different. | `5 ^ 3` → `101 ^ 011` = `110` (6) |
| `~` | **NOT** | Inverts all bits. | `~5` → `~...000101` = `...111010` |
| `<<` | **Left Shift** | Shifts bits left (Multiply by 2). | `5 << 1` → `1010` (10) |
| `>>` | **Right Shift** | Shifts bits right (Divide by 2). | `5 >> 1` → `10` (2) |

---

## 7️⃣ Important Binary Tricks 💡 (Interview Favorites)

### 🔹 1. Check if Number is Even or Odd
Check the last bit (Least Significant Bit - LSB).
*   If LSB is `0` → Even
*   If LSB is `1` → Odd

```cpp
if (n & 1) cout << "Odd";
else cout << "Even";
```

### 🔹 2. Multiply/Divide by 2 (Fast)
*   `n << 1` is equivalent to `n * 2`
*   `n >> 1` is equivalent to `n / 2`

### 🔹 3. Swap two numbers without temp variable
Using XOR property (`a ^ a = 0` and `a ^ 0 = a`).
```cpp
a = a ^ b;
b = a ^ b;
a = a ^ b;
```

### 🔹 4. Check if Number is Power of 2
A power of 2 has exactly one `1` in binary (e.g., 8 is `1000`).
`n & (n-1)` removes the last set bit. If result is 0, it was a power of 2.

```cpp
bool isPowerOfTwo(int n) {
    return (n > 0) && ((n & (n - 1)) == 0);
}
```

### 🔹 5. Find the Unique Number
Given an array where every number appears twice except one.
Logic: `X ^ X = 0`. All pairs cancel out.

```cpp
int unique = 0;
for(int x : arr) unique ^= x;
return unique;
```

---

## 8️⃣ Data Type Modifiers & Ranges

| Modifier | Size (Typical) | Range |
| :--- | :--- | :--- |
| `short` | 2 bytes | -32,768 to 32,767 |
| `int` | 4 bytes | -2e9 to +2e9 |
| `long long` | 8 bytes | Very large |
| `unsigned int` | 4 bytes | 0 to 4e9 (No negatives) |

### ⚠️ Common Mistake: Unsigned
`unsigned int x = -5;`
This will not store -5. It will store a huge positive number (the 2's complement interpretation of -5 as an unsigned integer).

---

## 9️⃣ Concepts Students Usually Forget ❌

1.  **MSB (Most Significant Bit)**:
    *   The leftmost bit.
    *   In **signed** numbers, `0` = Positive, `1` = Negative.

2.  **Operator Precedence**:
    *   `5 + 2 << 1` evaluates as `5 + (2 << 1)`? **NO!**
    *   `+` has higher precedence than `<<`.
    *   It evaluates as `(5 + 2) << 1` → `7 << 1` → `14`.
    *   **Fix**: Always use parentheses: `5 + (2 << 1)`.

3.  **Infinite Loop with Unsigned**:
    ```cpp
    for(unsigned int i = 5; i >= 0; i--) { ... }
    ```
    *   This is an **infinite loop**. `i` can never be negative. When `0` is decremented, it wraps around to the maximum positive value (underflow).

4.  **Reverse Logic**:
    *   When converting Decimal to Binary manually, remember to read remainders from **Bottom to Top**.

---

## 🔟 Summary Cheat Sheet

| Concept | Key |
| :--- | :--- |
| **Binary Base** | 2 (0, 1) |
| **Decimal Base** | 10 (0-9) |
| **Even Number** | Ends in 0 |
| **Odd Number** | Ends in 1 |
| **Negative Num** | Stored as 2's Complement |
| **Left Shift (<<)** | Multiply by 2 |
| **Right Shift (>>)** | Divide by 2 |
| **XOR (^)** | Difference detector (1 if diff) |

---

### 📝 Example Code: Binary to Decimal
```cpp
#include <iostream>
using namespace std;

void binToDec(int binNum) {
    int decNum = 0;
    int pow = 1;

    while (binNum > 0) {
        int lastDigit = binNum % 10;
        decNum += lastDigit * pow;
        pow *= 2;
        binNum /= 10;
    }

    cout << decNum << endl;
}

int main() {
    binToDec(100101);
    return 0;
}
```
