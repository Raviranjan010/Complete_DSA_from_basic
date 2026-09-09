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
