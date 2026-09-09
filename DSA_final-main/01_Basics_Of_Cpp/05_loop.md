# 🔄 Loops in C++

## 🔹 Introduction
Loops allow a program to execute a block of code repeatedly until a specific condition is met. They are essential for handling repetitive tasks efficiently.

### Types of Loops
1.  **for loop**: Best when the number of iterations is known.
2.  **while loop**: Best when the number of iterations is unknown (depends on a condition).
3.  **do-while loop**: Best when the code must execute **at least once**.

---

## 1️⃣ For Loop
Used to iterate a specific number of times.

### Syntax
```cpp
for (initialization; condition; update) {
    // Code to be executed
}
```

### Example: Sum of First n Natural Numbers
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    cout << "Sum = " << sum << endl;
    return 0;
}
```

---

## 2️⃣ While Loop
Used when the termination condition is known, but the number of iterations is not.

### Syntax
```cpp
while (condition) {
    // Code to be executed
    // Update condition variable
}
```

### Example: Printing 1 to n
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int count = 1;
    while (count <= n) {
        cout << count << " ";
        count++;
    }
    return 0;
}
```

### 🔹 Important Pattern: Digit Extraction
Common in interview questions (Palindrome, Armstrong, Reverse).

*   **Get last digit**: `num % 10`
*   **Remove last digit**: `num / 10`

#### Example: Sum of Digits
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int sum = 0;
    while (n > 0) {
        int lastDigit = n % 10;
        sum += lastDigit;
        n /= 10;
    }

    cout << "Sum of digits = " << sum << endl;
    return 0;
}
```

#### Example: Reverse a Number
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int res = 0;
    while (n > 0) {
        int lastDigit = n % 10;
        res = res * 10 + lastDigit;
        n /= 10;
    }

    cout << "Reversed: " << res << endl;
    return 0;
}
```

---

## 3️⃣ Do-While Loop
Executes the block **once** before checking the condition.

### Syntax
```cpp
do {
    // Code to be executed
} while (condition);
```

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 1;
    do {
        cout << i << " ";
        i++;
    } while (i <= 5);
    return 0;
}
```

---

## 4️⃣ Loop Control & Conditionals
Conditional statements (`if`, `if-else`) are often used inside loops to control execution flow.

### Break Statement
Terminates the loop immediately.

```cpp
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        break; // Exit loop when i is 3
    }
    cout << i << " ";
}
// Output will be 1 2
```

### Continue Statement
Skips the current iteration and moves to the next one.

```cpp
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue; // Skip printing 3
    }
    cout << i << " ";
}
// Output will be 1 2 4 5
```

---

## 5️⃣ Advanced Examples (Interview Questions)

### ✅ Check Prime Number
A prime number has only two factors: 1 and itself.

#### Optimized Approach (Square Root)
Instead of checking up to `n`, we check up to `sqrt(n)`. If `n` has a factor larger than `sqrt(n)`, the corresponding co-factor must be smaller than `sqrt(n)`.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;

    bool isPrime = true;
    if (n <= 1) isPrime = false;

    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime) cout << "Prime" << endl;
    else cout << "Not Prime" << endl;

    return 0;
}
```

### ✅ Check Armstrong Number
An Armstrong number (for 3 digits) is equal to the sum of the cubes of its digits.
*   Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int originalN = n; // Store original value
    int sum = 0;

    while (n > 0) {
        int lastDigit = n % 10;
        sum += (lastDigit * lastDigit * lastDigit);
        n /= 10;
    }

    if (sum == originalN) {
        cout << "Armstrong number";
    } else {
        cout << "Not an Armstrong number";
    }
    return 0;
}
```

### ✅ Fibonacci Series
Sequence where each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5...

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of terms: ";
    cin >> n;

    int first = 0, second = 1;
    cout << first << " " << second << " ";

    for (int i = 2; i < n; i++) {
        int next = first + second;
        cout << next << " ";
        first = second;
        second = next;
    }
    return 0;
}
