# 04 — Recursion & Backtracking — Complete Notes

> **What You'll Learn**: Recursion fundamentals, recursion trees, backtracking template, permutations, combinations, N-Queens, Sudoku solver  
> **Prerequisites**: Arrays & Strings (Topics 02-03), Functions  
> **Time Required**: 1.5 weeks (15-20 hours)  
> **Importance**: 🌟🌟🌟🌟🌟 (Foundation for DP, Trees, Graphs)

---

## 1. What is Recursion? (Real-World Analogy)

### The Russian Doll Analogy 🪆

Imagine you have a set of **Russian nesting dolls** — each doll contains a smaller doll inside it.

```
┌─────────────────────────────────────┐
│  Big Doll (n=5)                     │
│  ┌───────────────────────────────┐  │
│  │  Medium Doll (n=4)            │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │  Small Doll (n=3)       │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │ Tiny Doll (n=2)   │  │  │  │
│  │  │  │ ┌───────────────┐ │  │  │  │
│  │  │  │ │ Smallest(n=1) │ │  │  │  │
│  │  │  │ └───────────────┘ │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘

To open the biggest doll:
1. Open doll #5
2. Open doll #4 (inside #5)
3. Open doll #3 (inside #4)
4. Open doll #2 (inside #3)
5. Open doll #1 (smallest, base case!)
6. Now close them back in reverse order
```

**Recursion is exactly this!**
- A function that **calls itself** to solve a smaller version of the same problem
- Keeps calling itself with smaller inputs until it reaches the **smallest case** (base case)
- Then builds up the solution as it returns

💡 **TRICK**: Think of recursion as **"divide and conquer by making the problem smaller and smaller"**!

---

## 2. Why Do We Need Recursion?

### Real-World Problems That Use Recursion:

1. **File System Navigation**: Folders inside folders inside folders
2. **Organizational Charts**: Manager → Team Lead → Employee hierarchy
3. **Family Trees**: Your parents → their parents → their parents...
4. **Mathematical Calculations**: Factorial, Fibonacci, powers
5. **Game AI**: Chess engine exploring move trees
6. **Parsing Code**: Compilers breaking down expressions

### Why Recursion is Powerful:
- ✅ **Elegant**: Cleaner code for complex problems
- ✅ **Natural**: Some problems are inherently recursive
- ✅ **Foundation**: Trees, Graphs, DP all use recursion
- ✅ **Interview Favorite**: Tests problem-solving thinking

---

## 3. Core Concepts & Terminology

### 3.1 The Three Pillars of Recursion

Every recursive function MUST have:

1. **Base Case**: When to STOP (prevents infinite recursion)
2. **Recursive Case**: How to break problem into smaller subproblem
3. **Progress**: Each call must get closer to base case

```cpp
#include <iostream>
using namespace std;

// Example: Countdown function
void countdown(int n) {
    // 1. BASE CASE: When to stop
    if(n == 0) {
        cout << "Blastoff! 🚀" << endl;
        return;
    }
    
    // 2. Do work
    cout << n << "... ";
    
    // 3. RECURSIVE CASE: Call with smaller problem
    countdown(n - 1);  // Progress: n decreases by 1
}

int main() {
    countdown(5);
    // Output: 5... 4... 3... 2... 1... Blastoff! 🚀
    return 0;
}
```

---

### 3.2 How Recursion Works: The Call Stack

**Real-World Analogy**: Think of recursion like a **stack of plates** at a cafeteria.

```
Function Calls (Stack):

countdown(5)  ← Bottom plate (first called)
countdown(4)  ← Second plate
countdown(3)  ← Third plate
countdown(2)  ← Fourth plate
countdown(1)  ← Fifth plate
countdown(0)  ← Top plate (base case reached!)

After base case, plates are removed one by one (LIFO - Last In First Out)
```

**Memory Visualization**:
```
┌──────────────────────────────────────┐
│           CALL STACK                 │
├──────────────────────────────────────┤
│ countdown(0)  ← Top (executing now)  │
│ countdown(1)  ← Waiting              │
│ countdown(2)  ← Waiting              │
│ countdown(3)  ← Waiting              │
│ countdown(4)  ← Waiting              │
│ countdown(5)  ← Bottom (first call)  │
└──────────────────────────────────────┘

Each function call is a "stack frame" storing:
- Local variables
- Parameters
- Return address
```

---

### 3.3 Factorial: Classic Example

**Mathematical Definition**:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- n! = n × (n-1)!
- Base case: 0! = 1

```cpp
#include <iostream>
using namespace std;

// Recursive factorial
// Time: O(n), Space: O(n) for call stack
int factorial(int n) {
    // BASE CASE: 0! = 1, 1! = 1
    if(n <= 1) {
        return 1;
    }
    
    // RECURSIVE CASE: n! = n × (n-1)!
    return n * factorial(n - 1);
}

int main() {
    int n = 5;
    cout << n << "! = " << factorial(n) << endl;  // 120
    return 0;
}
```

**Dry Run** (factorial(5)):
```
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))           ← Base case reached!
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120 ✓

Stack depth: 5 (space complexity O(n))
```

**Recursion Tree**:
```
        factorial(5)
            |
        5 * factorial(4)
            |
        4 * factorial(3)
            |
        3 * factorial(2)
            |
        2 * factorial(1)
            |
            1  ← Base case
```

---

## 4. Visual Diagram: Recursion vs Iteration

```
┌─────────────────────────────────────────────────────────────┐
│              RECURSION vs ITERATION                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PROBLEM: Calculate sum from 1 to n                         │
│                                                              │
│  ITERATIVE APPROACH (Loop):                                 │
│  ─────────────────────────                                  │
│  int sum = 0;                                               │
│  for(int i = 1; i <= n; i++) {                              │
│      sum += i;                                              │
│  }                                                          │
│                                                              │
│  Flow: 1 → 2 → 3 → 4 → 5 → Done                            │
│  Space: O(1)  ← Only one variable!                          │
│                                                              │
│  RECURSIVE APPROACH:                                        │
│  ───────────────                                            │
│  int sum(int n) {                                           │
│      if(n == 0) return 0;  // Base case                     │
│      return n + sum(n-1);   // Recursive case               │
│  }                                                          │
│                                                              │
│  Flow: sum(5) → sum(4) → sum(3) → sum(2) → sum(1) → sum(0) │
│        Then unwind: 0+1+2+3+4+5 = 15                        │
│  Space: O(n)  ← n stack frames!                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

💡 **TRICK**: **When to use recursion?**
- Use recursion when problem has **overlapping subproblems** or **tree-like structure**
- Use iteration for **simple loops** (better space complexity)

---

## 5. C++ Implementation: Essential Recursion Patterns

### Pattern 1: Fibonacci Sequence

**Real-World Example**: Rabbit population growth, sunflower spirals, golden ratio in nature!

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Method 1: Naive Recursion (BAD - exponential time!)
// Time: O(2^n), Space: O(n)
int fibonacciNaive(int n) {
    // Base cases
    if(n <= 1) {
        return n;
    }
    
    // Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacciNaive(n - 1) + fibonacciNaive(n - 2);
}

// Method 2: Memoization (Top-Down DP)
// Time: O(n), Space: O(n)
int fibonacciMemo(int n, vector<int>& memo) {
    // Base case
    if(n <= 1) {
        return n;
    }
    
    // Check if already computed
    if(memo[n] != -1) {
        return memo[n];
    }
    
    // Compute and store result
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
    return memo[n];
}

// Method 3: Iterative (BEST for space)
// Time: O(n), Space: O(1)
int fibonacciIterative(int n) {
    if(n <= 1) return n;
    
    int prev2 = 0;  // F(0)
    int prev1 = 1;  // F(1)
    int current;
    
    for(int i = 2; i <= n; i++) {
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}

int main() {
    int n = 10;
    
    cout << "Fibonacci sequence:" << endl;
    for(int i = 0; i <= n; i++) {
        cout << "F(" << i << ") = " << fibonacciIterative(i) << endl;
    }
    /*
    Output:
    F(0) = 0
    F(1) = 1
    F(2) = 1
    F(3) = 2
    F(4) = 3
    F(5) = 5
    F(6) = 8
    F(7) = 13
    F(8) = 21
    F(9) = 34
    F(10) = 55
    */
    
    return 0;
}
```

**Recursion Tree** (fibonacciNaive(5)) - Shows why it's slow:
```
                    fib(5)
                   /      \
              fib(4)      fib(3)
             /     \      /     \
         fib(3)  fib(2) fib(2) fib(1)
        /     \
    fib(2)  fib(1)
    /     \
fib(1) fib(0)

Notice: fib(3) computed 2 times, fib(2) computed 3 times!
This is why we need memoization!
```

**Visualization with Memoization**:
```
fib(5) calls fib(4) and fib(3)
  fib(4) computes fib(3) and fib(2), stores results
  fib(3) REUSES stored result! No re-computation!
  
Result: Each value computed exactly ONCE
Time: O(n) instead of O(2^n)
```

💡 **TRICK**: **Fibonacci Mnemonic**: "Each number is the sum of the two before it" — like a financial compound interest pattern!

---

### Pattern 2: Power Function

```cpp
#include <iostream>
using namespace std;

// Calculate x^n using recursion
// Time: O(log n) with optimization, Space: O(log n)
double power(double x, int n) {
    // Base case: x^0 = 1
    if(n == 0) {
        return 1;
    }
    
    // Handle negative powers
    if(n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    // Recursive case
    double half = power(x, n / 2);
    
    // If n is even: x^n = (x^(n/2))^2
    // If n is odd: x^n = x * (x^(n/2))^2
    if(n % 2 == 0) {
        return half * half;
    } else {
        return x * half * half;
    }
}

int main() {
    cout << "2^10 = " << power(2, 10) << endl;  // 1024
    cout << "3^5 = " << power(3, 5) << endl;    // 243
    cout << "2^-3 = " << power(2, -3) << endl;  // 0.125
    
    return 0;
}
```

**Dry Run** (power(2, 10)):
```
power(2, 10)
= power(2, 5)^2
= (2 * power(2, 2)^2)^2
= (2 * (power(2, 1)^2)^2)^2
= (2 * ((2 * power(2, 0)^2)^2))^2
= (2 * ((2 * 1^2)^2))^2
= (2 * (2^2))^2
= (2 * 4)^2
= 8^2
= 1024 ✓

Only 4 recursive calls instead of 10! (log₂(10) ≈ 4)
```

---

### Pattern 3: Sum of Array Elements

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Sum array elements recursively
// Time: O(n), Space: O(n)
int sumArray(const vector<int>& arr, int index) {
    // Base case: reached end of array
    if(index >= arr.size()) {
        return 0;
    }
    
    // Recursive case: current element + sum of rest
    return arr[index] + sumArray(arr, index + 1);
}

// Wrapper function for cleaner interface
int sumArray(const vector<int>& arr) {
    return sumArray(arr, 0);  // Start from index 0
}

int main() {
    vector<int> nums = {1, 2, 3, 4, 5};
    cout << "Sum: " << sumArray(nums) << endl;  // 15
    return 0;
}
```

**Dry Run** (sumArray([1,2,3])):
```
sumArray([1,2,3], 0)
= 1 + sumArray([1,2,3], 1)
= 1 + (2 + sumArray([1,2,3], 2))
= 1 + (2 + (3 + sumArray([1,2,3], 3)))
= 1 + (2 + (3 + 0))        ← Base case
= 1 + (2 + 3)
= 1 + 5
= 6 ✓
```

---

## 6. Backtracking: The Art of Trial and Error

### What is Backtracking?

**Real-World Analogy**: Solving a **maze**!

```
Entrance → ┌───┬───┬───┬───┐
           │   │   │   │   │
           ├───┼───┼───┼───┤
           │   │███│   │   │
           ├───┼───┼───┼───┤
           │   │   │   │███│
           ├───┼───┼───┼───┤
           │███│███│   │   │
           └───┴───┴───┴───┘
                         ↑
                       Exit

Strategy:
1. Try going right → Dead end
2. BACKTRACK to last decision point
3. Try going down → Dead end
4. BACKTRACK again
5. Try different path → Success! 🎉
```

**Backtracking = Recursion + Trial & Error + Undo**

---

### The Backtracking Template (MEMORIZE THIS!)

```cpp
void backtrack(parameters) {
    // 1. BASE CASE: Check if solution found
    if(isValidSolution()) {
        addSolution();
        return;
    }
    
    // 2. TRY ALL POSSIBILITIES
    for(each possible choice) {
        // 3. MAKE CHOICE
        makeChoice();
        
        // 4. RECURSE
        backtrack(newParameters);
        
        // 5. UNDO CHOICE (BACKTRACK)
        undoChoice();
    }
}
```

---

### Pattern 4: Generate All Permutations

**Problem**: Generate all arrangements of [1, 2, 3]

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Time: O(n! × n), Space: O(n)
void permute(vector<int>& nums, int start, vector<vector<int>>& result) {
    // BASE CASE: Reached end, one permutation complete
    if(start == nums.size()) {
        result.push_back(nums);
        return;
    }
    
    // TRY all possible elements at position 'start'
    for(int i = start; i < nums.size(); i++) {
        // MAKE CHOICE: Swap elements
        swap(nums[start], nums[i]);
        
        // RECURSE: Generate permutations for remaining positions
        permute(nums, start + 1, result);
        
        // UNDO CHOICE: Backtrack (swap back)
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> generatePermutations(vector<int>& nums) {
    vector<vector<int>> result;
    permute(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = generatePermutations(nums);
    
    cout << "All permutations of [1, 2, 3]:" << endl;
    for(const auto& perm : result) {
        cout << "[";
        for(int i = 0; i < perm.size(); i++) {
            cout << perm[i] << (i < perm.size()-1 ? ", " : "");
        }
        cout << "]" << endl;
    }
    /*
    Output:
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 2, 1]
    [3, 1, 2]
    */
    
    return 0;
}
```

**Recursion Tree** (permutations of [1,2,3]):
```
                  [1,2,3]
              /      |      \
         swap(0,0) swap(0,1) swap(0,2)
           [1,2,3]  [2,1,3]   [3,2,1]
          /    \      /  \      /    \
     [1,2,3][1,3,2][2,1,3][2,3,1][3,2,1][3,1,2]
       ✓      ✓      ✓      ✓      ✓      ✓

Total: 3! = 6 permutations
```

💡 **TRICK**: **Permutation Formula**: n elements = n! permutations
- 3 elements = 6 permutations
- 5 elements = 120 permutations
- 10 elements = 3,628,800 permutations (exponential growth!)

---

### Pattern 5: Generate All Subsets

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Time: O(2^n × n), Space: O(n)
void generateSubsets(const vector<int>& nums, int index, 
                    vector<int>& current, vector<vector<int>>& result) {
    // BASE CASE: Processed all elements
    if(index == nums.size()) {
        result.push_back(current);
        return;
    }
    
    // OPTION 1: INCLUDE current element
    current.push_back(nums[index]);
    generateSubsets(nums, index + 1, current, result);
    
    // BACKTRACK: Remove element
    current.pop_back();
    
    // OPTION 2: EXCLUDE current element
    generateSubsets(nums, index + 1, current, result);
}

vector<vector<int>> subsets(const vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> current;
    generateSubsets(nums, 0, current, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = subsets(nums);
    
    cout << "All subsets of [1, 2, 3]:" << endl;
    for(const auto& subset : result) {
        cout << "[";
        for(int i = 0; i < subset.size(); i++) {
            cout << subset[i] << (i < subset.size()-1 ? ", " : "");
        }
        cout << "]" << endl;
    }
    /*
    Output:
    [1, 2, 3]
    [1, 2]
    [1, 3]
    [1]
    [2, 3]
    [2]
    [3]
    []
    */
    
    return 0;
}
```

**Decision Tree** (subsets of [1,2,3]):
```
                    []
                   /  \
              include 1  exclude 1
                /          \
             [1]            []
            /   \          /   \
       include 2 exclude 2     ...
          /         \
       [1,2]        [1]
       /   \        /   \
   incl 3 excl 3  incl 3 excl 3
     /       \      /       \
  [1,2,3]   [1,2] [1,3]    [1]
    ✓        ✓      ✓       ✓

Total: 2^3 = 8 subsets
```

💡 **TRICK**: **Subset Formula**: n elements = 2^n subsets (each element: include OR exclude)

---

### Pattern 6: N-Queens Problem

**Problem**: Place N queens on N×N chessboard so no two queens attack each other.

**Real-World Example**: Like placing security cameras so they don't overlap in coverage!

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Check if placing queen at (row, col) is safe
bool isSafe(const vector<string>& board, int row, int col, int n) {
    // Check left in current row
    for(int i = 0; i < col; i++) {
        if(board[row][i] == 'Q') return false;
    }
    
    // Check upper-left diagonal
    for(int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if(board[i][j] == 'Q') return false;
    }
    
    // Check lower-left diagonal
    for(int i = row, j = col; i < n && j >= 0; i++, j--) {
        if(board[i][j] == 'Q') return false;
    }
    
    return true;
}

// Solve N-Queens using backtracking
bool solveNQueens(vector<string>& board, int col, int n) {
    // BASE CASE: All queens placed
    if(col >= n) {
        return true;
    }
    
    // Try placing queen in each row of current column
    for(int row = 0; row < n; row++) {
        if(isSafe(board, row, col, n)) {
            // MAKE CHOICE: Place queen
            board[row][col] = 'Q';
            
            // RECURSE: Place remaining queens
            if(solveNQueens(board, col + 1, n)) {
                return true;
            }
            
            // UNDO CHOICE: Remove queen (backtrack)
            board[row][col] = '.';
        }
    }
    
    return false;  // No solution found
}

void printBoard(const vector<string>& board) {
    for(const string& row : board) {
        cout << row << endl;
    }
    cout << endl;
}

int main() {
    int n = 4;
    vector<string> board(n, string(n, '.'));
    
    cout << n << "-Queens Solution:" << endl;
    if(solveNQueens(board, 0, n)) {
        printBoard(board);
    } else {
        cout << "No solution exists" << endl;
    }
    /*
    Output for 4-Queens:
    .Q..
    ...Q
    Q...
    ..Q.
    */
    
    return 0;
}
```

**Visualization** (4-Queens solution):
```
. Q . .    ← Queen at (0,1)
. . . Q    ← Queen at (1,3)
Q . . .    ← Queen at (2,0)
. . Q .    ← Queen at (3,2)

✓ No two queens share same row, column, or diagonal!
```

---

## 7. All Operations with Time & Space Complexity

| Problem | Time Complexity | Space Complexity | Notes |
|---------|----------------|------------------|-------|
| Factorial | O(n) | O(n) | Call stack depth |
| Fibonacci (naive) | O(2^n) | O(n) | Exponential! |
| Fibonacci (memo) | O(n) | O(n) | Each value once |
| Power (optimized) | O(log n) | O(log n) | Divide by 2 |
| Permutations | O(n! × n) | O(n) | n! solutions |
| Subsets | O(2^n × n) | O(n) | 2^n solutions |
| N-Queens | O(n!) | O(n²) | Pruning helps |

---

## 8. Common Patterns & Tricks

### 💡 TRICK 1: Recursion to Iteration Conversion
```cpp
// Recursive
int sum(int n) {
    if(n == 0) return 0;
    return n + sum(n-1);
}

// Equivalent Iterative
int sum(int n) {
    int result = 0;
    for(int i = 1; i <= n; i++) {
        result += i;
    }
    return result;
}
```

### 💡 TRICK 2: Tail Recursion (Optimized by Compiler)
```cpp
// NOT tail recursive (does work after call)
int factorial(int n) {
    if(n <= 1) return 1;
    return n * factorial(n-1);  // Multiplication after call
}

// Tail recursive (no work after call)
int factorialTail(int n, int acc = 1) {
    if(n <= 1) return acc;
    return factorialTail(n-1, n * acc);  // Last operation is recursive call
}
```

### 💡 TRICK 3: Memoization Template
```cpp
int solve(int n, vector<int>& memo) {
    // Base case
    if(n <= 0) return baseValue;
    
    // Check memo
    if(memo[n] != -1) return memo[n];
    
    // Compute and store
    memo[n] = recursiveCall();
    return memo[n];
}
```

---

## 9. Common Mistakes & How to Avoid Them

### ❌ Mistake 1: Missing Base Case
```cpp
int factorial(int n) {
    return n * factorial(n-1);  // INFINITE RECURSION!
}
```
✅ **Fix**: Always define base case first!

### ❌ Mistake 2: No Progress Toward Base Case
```cpp
void badFunction(int n) {
    if(n == 0) return;
    badFunction(n);  // Same value, never reaches base case!
}
```
✅ **Fix**: Ensure parameters change: `badFunction(n-1)`

### ❌ Mistake 3: Stack Overflow
```cpp
void recurse(int n) {
    if(n == 0) return;
    int arr[1000];  // Large local variable
    recurse(n-1);
}
```
✅ **Fix**: Minimize local variables in recursive functions

### ❌ Mistake 4: Forgetting to Backtrack
```cpp
void permute(vector<int>& nums) {
    swap(nums[i], nums[j]);
    permute(nums);
    // FORGOT to swap back!
}
```
✅ **Fix**: Always undo changes after recursive call

---

## 10. Interview Tips & What Companies Ask

### Most Common Questions:
1. **Fibonacci Number** 🏢 [Adobe, TCS]
2. **Subsets** 🏢 [Amazon, Google]
3. **Permutations** 🏢 [Microsoft, Meta]
4. **Combination Sum** 🏢 [Amazon] 📅 [Very High]
5. **N-Queens** 🏢 [Google] 📅 [High]
6. **Word Search** 🏢 [Amazon, Microsoft]
7. **Sudoku Solver** 🏢 [Google, Meta]

### What Interviewers Look For:
- ✅ Can you identify recursive structure?
- ✅ Do you define base cases correctly?
- ✅ Can you optimize with memoization?
- ✅ Backtracking: make choice → recurse → undo

---

## 11. Practice Problems

### 🟢 Easy:
1. **Factorial** — Basic recursion
2. **Fibonacci** — With memoization
3. **Sum of Digits** — Recursive sum
4. **Power of Two** — Check if power of 2
5. **Reverse String** — Recursive reversal

### 🟡 Medium:
6. **Subsets** 🏢 [Amazon] 📅 [Very High]
7. **Permutations** 🏢 [Microsoft] 📅 [High]
8. **Combination Sum** 🏢 [Amazon] 📅 [Very High]
9. **Letter Combinations of Phone Number** 🏢 [Meta]
10. **Generate Parentheses** 🏢 [Google]

### 🔴 Hard:
11. **N-Queens** 🏢 [Google] 📅 [High]
12. **Sudoku Solver** 🏢 [Google, Meta]
13. **Word Search II** 🏢 [Amazon]

---

## 12. Glossary

| Term | Definition |
|------|------------|
| **Recursion** | Function that calls itself to solve smaller subproblems |
| **Base Case** | Condition that stops recursion |
| **Recursive Case** | Part where function calls itself |
| **Call Stack** | Memory structure storing function calls |
| **Stack Frame** | Memory for one function call's local variables |
| **Backtracking** | Try → Recurse → Undo pattern |
| **Memoization** | Caching results to avoid re-computation |
| **Recursion Tree** | Visual representation of recursive calls |
| **Tail Recursion** | Recursive call is last operation (compiler optimizes) |
| **Stack Overflow** | Error when call stack exceeds memory limit |

---

## 13. Future Questions & Competitive Programming

### Advanced Topics:
1. **Recursion with Bitmasking** — Subset generation optimization
2. **Dancing Links** — Exact cover problems
3. **Alpha-Beta Pruning** — Game tree optimization
4. **Meet-in-the-Middle** — Split recursion for large inputs

### CP Template:
```cpp
// Fast recursion with memoization
vector<int> memo(1000, -1);
int solve(int n) {
    if(n <= 0) return 0;
    if(memo[n] != -1) return memo[n];
    return memo[n] = recursiveFormula();
}
```

---

**🎉 Congratulations! You've mastered Recursion & Backtracking!**

**Next Steps**:
1. ✅ Complete all MCQs in `04_mcqs.md`
2. ✅ Solve 15 recursion problems
3. ✅ Practice backtracking template
4. ✅ Move to **05_Sorting_and_Searching**

[← Back to README](../README.md) | [Next: Sorting →](../../04-Searching-and-Sorting/concepts/03-sorting-algorithms-theory.md)


---

## Supplementary Notes from 06-Recursion.md

# 🔁 06 — Recursion

> **Explain Like I'm 5:** Stand between two mirrors facing each other. You see yourself, inside a smaller you, inside a smaller you… forever. Each reflection is the *same picture, just smaller.* That's recursion — **a function that calls a smaller copy of itself.**
>
> But mirrors going on forever never finish. So recursion needs a **wall to stop at.** That stopping point is called the **base case.**

---

## 💻 Under the Hood: The Execution Call Stack

To understand recursion, you must understand how the computer executes function calls.
Whenever a function is called, the computer allocates a block of memory called a **Stack Frame** (or Activation Record) on top of the **Call Stack**.

### What's inside a Stack Frame?
1. **Local Variables:** Variables declared inside the function.
2. **Parameters:** Values passed into the function (e.g. `n`).
3. **Return Address:** The line of code to jump back to once the function finishes.

### Visualizing Stack Frames for `factorial(3)`
Each function call pushes a new frame. They sit on top of each other. The computer can only interact with the frame on the very top.

```
Pushes (Calls)                          Pops (Returns)
┌───────────────────────┐               ┌───────────────────────┐
│ factorial(1) [n=1]    │               │ factorial(1) returns 1│ (Popped!)
├───────────────────────┤               ├───────────────────────┤
│ factorial(2) [n=2]    │               │ factorial(2) returns 2│ (2 * 1)
├───────────────────────┤               ├───────────────────────┤
│ factorial(3) [n=3]    │               │ factorial(3) returns 6│ (3 * 2)
└───────────────────────┘               └───────────────────────┘
     Call Stack (GROWING)                   Call Stack (SHRINKING)
```

If your code doesn't hit a base case, it keeps pushing frames until it runs out of memory, causing a **`StackOverflowError`**.

---

## 🧮 The Leap of Faith: Mathematical Induction

Writing recursion is about **trust**. Do not try to trace all the calls in your head. Instead, think of it like **Mathematical Induction**:

1. **Prove the Base Case:** Show that the code works for the smallest input (e.g. $n = 0$ or $n = 1$).
2. **Assume the Hypothesis:** Assume that the recursive call `solve(n - 1)` works correctly. (Do not trace it; trust that it returns the correct value.)
3. **Write the Inductive Step:** Use the result of `solve(n - 1)` to build the answer for `solve(n)`.

*Example (Factorial):*
- Base Case: `factorial(1) = 1`
- Hypothesis: Assume `factorial(n - 1)` correctly computes $(n-1)!$
- Inductive Step: `factorial(n) = n * factorial(n - 1)` (Correct!)

---

## 🪜 The Staircase Analogy: "Down vs. Up"

The position of your code relative to the recursive call determines when it runs:

- **Work written BEFORE the recursive call:** Executed on the way **DOWN** (top-to-bottom).
- **Work written AFTER the recursive call:** Postponed and executed on the way **UP** (bottom-to-top).

```
          [Call Stack Entry]
                  │
        (1. Work on way DOWN)
                  │
        [Recursive call solve(n-1)] ──► (Dives deeper)
                  │
        (2. Work on way UP)
                  │
         [Call Stack Exit]
```

---

## 🎨 Tree Recursion: Fibonacci

When a function calls itself **twice**, the execution path forms a **Recursion Tree** rather than a straight line.

```
                                 fib(4)
                               /        \
                            fib(3)      fib(2)  (Wasted duplicate work!)
                           /      \     /    \
                       fib(2)   fib(1) fib(1) fib(0)
                       /    \
                    fib(1) fib(0)
```

- **Time Complexity:** $O(2^n)$ — The tree roughly doubles in size at each level.
- **Space Complexity:** $O(n)$ — The maximum stack depth matches the height of the tree. Only one branch is stored in the call stack at any single moment.

---

## 🎯 Practice Problems & Worked Solutions

Verify your recursion logic with these 8 foundational problems.

| # | Problem | Type | Link | Key Idea |
|---|---|---|---|---|
| 1 | Print 1 to N | Linear (Up) | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1) | Print after the recursive call. |
| 2 | Factorial | Linear (Return) | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/factorial5739/1) | $N \times (N-1)!$ |
| 3 | Sum of first N | Linear (Return) | [GeeksforGeeks](https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1) | $N + Sum(N-1)$ |
| 4 | Power(x, n) | Linear/Log | [LeetCode](https://leetcode.com/problems/powx-n/) | Divide and conquer exponents. |
| 5 | Fibonacci Number | Tree | [LeetCode](https://leetcode.com/problems/fibonacci-number/) | Sum of two previous states. |
| 6 | Reverse a String | Linear | [LeetCode](https://leetcode.com/problems/reverse-string/) | `reverse(rest) + first`. |
| 7 | Valid Palindrome | Two-Pointer | [LeetCode](https://leetcode.com/problems/valid-palindrome/) | Pointers checking inward recursively. |
| 8 | Binary Search | Divide & Conquer | [LeetCode](https://leetcode.com/problems/binary-search/) | Search bounds halved recursively. |

---

### Solution 1: Print 1 to N

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(n)$ stack frames.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public void print1toN(int n) {
    if (n == 0) return; // Base case
    print1toN(n - 1);   // Go down the stack first
    System.out.println(n); // Print on the way UP
}
```

#### Python
```python
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)  # Go down the stack first
    print(n)            # Print on the way UP
```

#### C++
```cpp
void print1toN(int n) {
    if (n == 0) return;
    print1toN(n - 1);   // Go down the stack first
    cout << n << endl;  // Print on the way UP
}
```
</details>

---

### Solution 2: Factorial

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int factorial(int n) {
    if (n <= 1) return 1; // Base case (prevents infinite loop for n=0)
    return n * factorial(n - 1); // Inductive step
}
```

#### Python
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

#### C++
```cpp
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```
</details>

---

### Solution 3: Sum of First N

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}
```

#### Python
```python
def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)
```

#### C++
```cpp
int sum(int n) {
    if (n == 0) return 0;
    return n + sum(n - 1);
}
```
</details>

---

### Solution 4: Power(x, n) (Optimized Binary Exponentiation)

**Intuition:** 
Instead of calculating $x^n$ linearily ($O(n)$), we can divide the exponent in half at each step:
- If $n$ is even: $x^n = (x^{n/2})^2$
- If $n$ is odd: $x^n = x \times (x^{n/2})^2$
This reduces the time complexity from $O(n)$ to $O(\log n)$.

**Complexity:**
- **Time:** $O(\log n)$
- **Space:** $O(\log n)$ stack memory.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public double myPow(double x, int n) {
    long N = n;
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }
    return fastPow(x, N);
}

private double fastPow(double x, long n) {
    if (n == 0) return 1.0;
    double half = fastPow(x, n / 2);
    if (n % 2 == 0) {
        return half * half;
    } else {
        return half * half * x;
    }
}
```

#### Python
```python
def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    
    def fast_pow(val, exp):
        if exp == 0:
            return 1.0
        half = fast_pow(val, exp // 2)
        if exp % 2 == 0:
            return half * half
        else:
            return half * half * val
            
    return fast_pow(x, n)
```

#### C++
```cpp
double fastPow(double x, long long n) {
    if (n == 0) return 1.0;
    double half = fastPow(x, n / 2);
    if (n % 2 == 0) {
        return half * half;
    } else {
        return half * half * x;
    }
}

double myPow(double x, int n) {
    long long N = n;
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }
    return fastPow(x, N);
}
```
</details>

---

### Solution 5: Fibonacci Number

**Complexity:**
- **Time:** $O(2^n)$
- **Space:** $O(n)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

#### Python
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

#### C++
```cpp
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```
</details>

---

### Solution 6: Reverse a String

**Intuition:** 
Reverse the substring starting at index 1, and append the first character to the end of that reversed substring.
`reverse("abc")` = `reverse("bc")` + `'a'`.

**Complexity:**
- **Time:** $O(n^2)$ (due to string slicing and copying in Java/Python).
- **Space:** $O(n)$

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public String reverse(String s) {
    if (s.length() <= 1) return s;
    return reverse(s.substring(1)) + s.charAt(0);
}
```

#### Python
```python
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]
```

#### C++
```cpp
string reverseString(string s) {
    if (s.length() <= 1) return s;
    return reverseString(s.substr(1)) + s[0];
}
```
</details>

---

### Solution 7: Valid Palindrome (Recursive Two-Pointer)

**Complexity:**
- **Time:** $O(n)$
- **Space:** $O(n)$ stack frames.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public boolean isPalindrome(String s) {
    return checkPalindrome(s, 0, s.length() - 1);
}

private boolean checkPalindrome(String s, int left, int right) {
    if (left >= right) return true;
    if (s.charAt(left) != s.charAt(right)) return false;
    return checkPalindrome(s, left + 1, right - 1);
}
```

#### Python
```python
def is_palindrome(s):
    def check_palindrome(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return check_palindrome(left + 1, right - 1)
        
    return check_palindrome(0, len(s) - 1)
```

#### C++
```cpp
bool checkPalindrome(const string& s, int left, int right) {
    if (left >= right) return true;
    if (s[left] != s[right]) return false;
    return checkPalindrome(s, left + 1, right - 1);
}

bool isPalindrome(string s) {
    return checkPalindrome(s, 0, s.size() - 1);
}
```
</details>

---

### Solution 8: Binary Search (Recursive)

**Complexity:**
- **Time:** $O(\log n)$
- **Space:** $O(\log n)$ stack frames.

<details>
<summary>💻 Multi-Language Code</summary>

#### Java
```java
public int search(int[] nums, int target) {
    return binarySearch(nums, 0, nums.length - 1, target);
}

private int binarySearch(int[] nums, int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (nums[mid] == target) return mid;
    if (nums[mid] < target) {
        return binarySearch(nums, mid + 1, high, target);
    } else {
        return binarySearch(nums, low, mid - 1, target);
    }
}
```

#### Python
```python
def search(nums, target):
    def binary_search(low, high):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return binary_search(mid + 1, high)
        else:
            return binary_search(low, mid - 1)
            
    return binary_search(0, len(nums) - 1)
```

#### C++
```cpp
int binarySearch(const vector<int>& nums, int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (nums[mid] == target) return mid;
    if (nums[mid] < target) {
        return binarySearch(nums, mid + 1, high, target);
    } else {
        return binarySearch(nums, low, mid - 1, target);
    }
}

int search(vector<int>& nums, int target) {
    return binarySearch(nums, 0, nums.size() - 1, target);
}
```
</details>

<details>
<summary>📋 Step-by-Step Call Stack Dry Run</summary>

Input: `nums = [2, 5, 8, 12, 16]`, `target = 12`

1. `binarySearch(nums, low=0, high=4, target=12)`
   - `mid = 0 + (4 - 0) / 2 = 2`
   - `nums[2] = 8 < 12` $\rightarrow$ Recurse on right half (`low = 3, high = 4`)
2. `binarySearch(nums, low=3, high=4, target=12)`
   - `mid = 3 + (4 - 3) / 2 = 3`
   - `nums[3] = 12 == 12` $\rightarrow$ Found! Return `3`
3. Returns `3` up the call stack.

**Result:** `3` ✅
</details>

---

## 🎓 Viva Questions & Answers

### Q1: What are the two mandatory components of every recursive function?
**Answer:**
1. **Base Case:** The condition under which the function stops calling itself and returns a value directly, preventing infinite recursion.
2. **Recursive Step:** The logic that breaks the problem into smaller sub-problems and makes a self-call moving closer to the base case.

### Q2: What causes a StackOverflow Error during recursion?
**Answer:**
A `StackOverflowError` occurs when the recursive function exceeds the maximum allocated memory limit of the call stack. Common causes include:
- Missing or unreachable base case.
- Recursive step failing to reduce the problem size toward the base case.
- Excessively deep recursion depth ($n > 10^5$).

### Q3: What is Tail Recursion, and what is Tail Call Optimization (TCO)?
**Answer:**
- **Tail Recursion:** A form of recursion where the recursive call is the **very last operation** performed in the function (no extra math or operations after the call returns).
- **Tail Call Optimization (TCO):** A compiler optimization where the current stack frame is reused for the recursive call instead of pushing a new frame, turning $O(n)$ call stack memory into $O(1)$.

### Q4: Compare Recursion vs Iteration in terms of memory and performance.
**Answer:**
- **Recursion:** More elegant and readable for hierarchical structures (Trees, Graphs, Backtracking), but incurs **call stack memory overhead** $O(depth)$ and function-call CPU overhead.
- **Iteration:** Uses loops with $O(1)$ auxiliary space and no call stack overhead, making it faster and memory-efficient for simple linear repetitions.

### Q5: How does the Call Stack store local variables during recursive calls?
**Answer:**
Each time a recursive function is invoked, a new **Stack Frame** (Activation Record) is pushed onto the system Stack. It contains local variables, parameters, and the return address. When the base case is reached, stack frames pop off one by one in LIFO order.

---

## ⚠️ Beginner Pitfalls & Common Mistakes

1. **Incorrect/Missing Base Case:**
   - If the base case is missing or cannot be reached, the code loops forever until it throws a `StackOverflowError`. Always verify that every path moves closer to the base case.

2. **Tail Recursion & Memory:**
   - In some languages like C++, tail-call optimization can reuse stack frames for functions that return the result of their recursive call directly (e.g. Solution 8). However, Java and Python do not support this optimization natively. Recursion is always constrained by the stack depth limit (typically ~1000 in Python).

---

> 👉 Next, open `07-Hashing.md` to learn how we index keys and values in constant time! 💪

