[← Chapter 03](07-conditionals-and-loops-ch03-master-c-pattern-printing.md) · [Chapter Index](07-conditionals-and-loops.md) · [Module Overview](../README.md)

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
