
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