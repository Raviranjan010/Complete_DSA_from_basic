
# 📘 Conditional Statements in C++

## 🔹 Introduction
Conditional statements allow a program to make decisions and execute different blocks of code based on conditions.

In C++, a condition evaluates to a boolean value:
*   **true**: Any non-zero value.
*   **false**: 0.

### Why are they important?
*   Control program flow.
*   Implement logic (e.g., login validation, game rules).
*   Handle multiple scenarios.

---

## 🔹 Types of Conditional Statements
1.  `if` statement
2.  `if-else` statement
3.  `else-if` ladder
4.  Nested `if`
5.  Ternary operator (`?:`)
6.  `switch` statement

---

## 1️⃣ if Statement
Executes a block of code **only** if the condition is true.

### Syntax
```cpp
if (condition) {
    // Code to execute if condition is true
}
```

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter age: ";
    cin >> age;

    if (age >= 18) {
        cout << "Eligible to vote" << endl;
    }
    return 0;
}
```

---

## 2️⃣ if-else Statement
Used when there are two possible outcomes: one for success (true) and one for failure (false).

### Syntax
```cpp
if (condition) {
    // Executes if condition is true
} else {
    // Executes if condition is false
}
```

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cin >> age;

    if (age >= 18) {
        cout << "Eligible to vote";
    } else {
        cout << "Not eligible to vote";
    }
    return 0;
}
```

---

## 3️⃣ else-if Ladder
Used to check multiple conditions in sequence. The first condition that evaluates to true is executed, and the rest are skipped.

### Syntax
```cpp
if (condition1) {
    // Code for condition1
} else if (condition2) {
    // Code for condition2
} else {
    // Code if none of the above are true
}
```

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int marks;
    cin >> marks;

    if (marks >= 90) {
        cout << "Grade A";
    } else if (marks >= 75) {
        cout << "Grade B";
    } else if (marks >= 50) {
        cout << "Grade C";
    } else {
        cout << "Fail";
    }
    return 0;
}
```

---

## 4️⃣ Nested if Statement
An `if` statement inside another `if` statement. Used for hierarchical checks.

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    char hasVoterID;

    cout << "Enter age and Voter ID status (y/n): ";
    cin >> age >> hasVoterID;

    if (age >= 18) {
        if (hasVoterID == 'y' || hasVoterID == 'Y') {
            cout << "You can vote";
        } else {
            cout << "Voter ID required";
        }
    } else {
        cout << "Underage";
    }
    return 0;
}
```

---

## 5️⃣ Ternary Operator (?:)
A shorthand for `if-else`. It takes three operands.

### Syntax
```cpp
variable = (condition) ? expression1 : expression2;
```
*   If `condition` is true, `expression1` is executed.
*   If `condition` is false, `expression2` is executed.

### Example
```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 10;
    string result = (num % 2 == 0) ? "Even" : "Odd";
    cout << result << endl;
    return 0;
}
```

---

## 6️⃣ switch-case Statement
Used to select one of many code blocks to be executed. It is often cleaner than a long `else-if` ladder when checking a single variable against constant values.

### Syntax
```cpp
switch (expression) {
    case constant1:
        // code
        break;
    case constant2:
        // code
        break;
    default:
        // code if no case matches
}
```

### Key Points
*   **Expression**: Must evaluate to an integer or character type (no strings or floats).
*   **break**: Stops execution inside the switch block. Without it, execution "falls through" to the next case.
*   **default**: Optional. Runs if no cases match.

### Example: Calculator
```cpp
#include <iostream>
using namespace std;

int main() {
    char op;
    float num1, num2;

    cout << "Enter operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    switch (op) {
        case '+':
            cout << num1 + num2;
            break;
        case '-':
            cout << num1 - num2;
            break;
        case '*':
            cout << num1 * num2;
            break;
        case '/':
            if (num2 != 0)
                cout << num1 / num2;
            else
                cout << "Error! Division by zero.";
            break;
        default:
            cout << "Invalid operator";
    }
    return 0;
}
```

---

## 🔹 Advanced: if with Initializer (C++17)
C++17 introduced the ability to initialize a variable inside the `if` statement itself. This limits the scope of the variable to the `if` block.

```cpp
if (int x = getValue(); x > 10) {
    cout << "x is greater than 10: " << x;
} else {
    cout << "x is small: " << x;
}
// x is not accessible here
```

---

## 🔹 Comparison: if-else vs switch

| Feature | if-else | switch |
| :--- | :--- | :--- |
| **Condition Type** | Boolean expression (ranges, logic) | Constant values (equality only) |
| **Data Types** | All types (int, float, string, etc.) | Integer, char, enum only |
| **Performance** | Checks conditions sequentially | Often optimized (jump tables) |
| **Complexity** | Good for complex logic | Good for simple, fixed choices |
| **Fall-through** | No | Yes (if `break` is omitted) |

---

## 🔹 Common Mistakes
1.  **Assignment instead of Comparison**:
    ```cpp
    if (x = 5) { ... } // Always true (assigns 5 to x)
    // Correct: if (x == 5)
    ```
2.  **Missing Semicolons**:
    Do not put a semicolon after `if(condition)`; this terminates the statement immediately.
    ```cpp
    if (x > 5); // Wrong! The block below always runs.
    {
        cout << "High";
    }
    ```
3.  **Switch Range Checks**:
    `switch` cannot check ranges like `case > 10:`. Use `if-else` for that.

---

## 🔹 Frequently Asked Interview Questions

**Q1. What is the "dangling else" problem?**
It occurs when nested `if` statements are used without braces. An `else` attaches to the nearest preceding `if`.
*   *Fix*: Always use `{}` braces.

**Q2. Can we use duplicate case values in a switch?**
No, duplicate case values will cause a compilation error.

**Q3. Is `switch` faster than `if-else`?**
Generally, yes, for a large number of cases. Compilers can optimize `switch` using jump tables, whereas `if-else` requires sequential evaluation.

**Q4. What happens if `break` is missing in a switch case?**
Execution continues to the next case regardless of whether the condition matches. This is called **fall-through**.

```cpp
int x = 1;
switch(x) {
    case 1: cout << "One "; // No break
    case 2: cout << "Two";
}
// Output: One Two
```

---

## Supplementary Reference from 05_loop.md

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


---

## Supplementary Reference from 05_pattern.md

# 📘 Master C++ Pattern Printing

## 🔑 Core Concept (The Real Shortcut)
Every pattern program depends on only **3 decisions**. If you can answer these three questions, you can solve any pattern.

1.  **Rows (Outer Loop `i`)**: How many lines are there?
2.  **Columns (Inner Loop `j`)**: How many items are in each line?
3.  **Content**: What do we print? (`*`, `i`, `j`, `char`, or `space`)

### 🧪 The Universal Template
Use this structure for almost every pattern:

```cpp
for(int i = 0; i < n; i++) { // 1. Rows

    // 2. Spaces (Optional, for mirrored/pyramid patterns)
    for(int s = 0; s < something; s++) {
        cout << "  ";
    }

    // 3. Columns (The main pattern)
    for(int j = 0; j < something; j++) {
        cout << "* "; // 4. Content
    }

    cout << endl; // New line after each row
}
```

---

## 🧠 Golden Rules (Shortcuts)

| Pattern Type | Inner Loop Condition | Logic |
| :--- | :--- | :--- |
| **Square** | `j < n` | Constant number of items per row. |
| **Increasing Triangle** | `j <= i` | Items increase as row number increases. |
| **Decreasing Triangle** | `j < n - i` | Items decrease as row number increases. |
| **Row-wise Data** | `cout << i` | Prints the current row number. |
| **Column-wise Data** | `cout << j` | Prints the current column number. |
| **Diagonal** | `if (i == j)` | Matches row and column index. |
| **Anti-Diagonal** | `if (i + j == n - 1)` | Matches opposite diagonal. |

---

## 1️⃣ Square Patterns
**Logic**: The inner loop runs `n` times for every row.

### Pattern 1: Row Numbers
```text
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```
```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << i + 1 << " "; // Print row number (+1 for 1-based)
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 2: Row Numbers with Symbol
```text
1*1*1*1*
2*2*2*2*
3*3*3*3*
4*4*4*4*
```
```cpp
int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << i + 1 << "*";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 3: Column Numbers
```text
0*1*2*3*
0*1*2*3*
0*1*2*3*
0*1*2*3*
```
```cpp
int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << j << "*"; // Print column number
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 4: Basic Square of Stars
```text
* * * * 
* * * * 
* * * * 
* * * * 
```
```cpp
int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

---

## 2️⃣ Increasing Triangle Patterns
**Logic**: The inner loop runs `i` times (depends on current row).
**Shortcut**: `j <= i`

### Pattern 5: Star Triangle
```text
* 
* * 
* * * 
* * * *
```
```cpp
int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= i; j++) { // Run up to i
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 6: Number Triangle (Row-based)
```text
1 
2 2 
3 3 3 
4 4 4 4
```
```cpp
int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= i; j++) {
            cout << i + 1 << " ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 7: Number Triangle (Column-based)
```text
0 
0 1 
0 1 2 
0 1 2 3
```
```cpp
int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 11: Character Triangle (Continuous)
```text
A
B C
D E F
```
```cpp
int main() {
    char ch = 'A';
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= i; j++) {
            cout << ch << " ";
            ch++; // Increment character continuously
        }
        cout << endl;
    }
    return 0;
}
```

---

## 3️⃣ Decreasing Triangle Patterns
**Logic**: The inner loop runs `n - i` times.
**Shortcut**: `j < n - i`

### Pattern 8: Inverted Star Triangle
```text
* * * * 
* * * 
* * 
* 
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) { // Decrease count
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 9: Inverted Column Numbers
```text
0 1 2 3 
0 1 2 
0 1 
0 
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 10: Inverted Row Numbers
```text
0 0 0 0 
1 1 1 
2 2 
3 
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
```

---

## 4️⃣ Advanced & Conditional Patterns

### Pattern 12: Continuous Character Square
```text
A B C 
D E F 
G H I 
```
```cpp
int main() {
    char ch = 'A';
    int n = 3;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << ch << " ";
            ch++;
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 13: Hollow Square (Borders Only)
**Logic**: Print star ONLY if it's the first/last row OR first/last column.
```text
* * * *
*     *
*     *
* * * *
```
```cpp
int main() {
    int n = 4;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == 1 || i == n || j == 1 || j == n)
                cout << "* ";
            else
                cout << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 14: Diagonal Line
**Logic**: Print star when `i == j`.
```text
*       
  *     
    *   
      * 
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(i == j) cout << "* ";
            else cout << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 15: Reverse Diagonal (Space Diagonal)
**Logic**: Print space when `i == j`, else star.
```text
  * * * 
*   * * 
* *   * 
* * *   
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(i == j) cout << "  ";
            else cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

---

## 5️⃣ Mirrored & Space Patterns
These require **two inner loops**: one for spaces, one for stars.

### Pattern 16: Mirrored Triangle (Right Aligned)
```text
      *
    * *
  * * *
* * * *
```
```cpp
int main() {
    int n = 4;
    for (int i = 1; i <= n; i++) {
        // 1. Print Spaces
        for (int s = 1; s <= n - i; s++) {
            cout << "  ";
        }
        // 2. Print Stars
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 17: Mixed Symbols
```text
+ + + / 
+ + / - 
+ / - - 
/ - - - 
```
```cpp
int main() {
    int n = 4;
    for (int i = 1; i <= n; i++) {
        // Print +
        for (int j = 1; j <= n - i; j++) {
            cout << "+ ";
        }
        // Print /
        cout << "/ ";
        // Print -
        for (int j = 1; j < i; j++) {
            cout << "- ";
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 18: Inverted Mirrored Triangle
```text
* * * *   
  * * *     
    * *    
      *
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        // Spaces increase
        for (int s = 0; s < i; s++) {
            cout << "  ";
        }
        // Stars decrease
        for (int j = 0; j < n - i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

---

## 6️⃣ Pyramid & Diamond Patterns

### Pattern 19: Full Pyramid
```text
      *
    *   *
  *   *   *
*   *   *   *
```
```cpp
int main() {
    int n = 4;
    for (int i = 1; i <= n; i++) {
        // Leading spaces
        for (int s = i; s < n; s++) {
            cout << "  ";
        }
        // Stars with gaps
        for (int j = 1; j <= i; j++) {
            cout << "*";
            if (j < i) {
                cout << "   "; // 3 spaces for gap
            }
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 20: Inverted Pyramid
```text
*   *   *   *
  *   *   *
    *   *
      *
```
```cpp
int main() {
    int n = 4;
    for (int i = 0; i < n; i++) {
        // Leading spaces
        for (int s = 0; s < i; s++) {
            cout << "  ";
        }
        // Stars with gaps
        for (int j = 0; j < n - i; j++) {
            cout << "*";
            if (j < n - i - 1) {
                cout << "   ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

### Pattern 21: Diamond (Pyramid + Inverted)
```text
      *
    *   *
  *   *   *
*   *   *   *
  *   *   *
    *   *
      *
```
```cpp
int main() {
    int n = 4;

    // Top half
    for (int i = 1; i <= n; i++) {
        for (int s = i; s < n; s++) {
            cout << "  ";
        }
        for (int j = 1; j <= i; j++) {
            cout << "*";
            if (j < i) cout << "   ";
        }
        cout << endl;
    }

    // Bottom half
    for (int i = n - 1; i >= 1; i--) {
        for (int s = i; s < n; s++) {
            cout << "  ";
        }
        for (int j = 1; j <= i; j++) {
            cout << "*";
            if (j < i) cout << "   ";
        }
        cout << endl;
    }
    return 0;
}
```
