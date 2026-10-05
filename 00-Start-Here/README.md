# Module 00: Start Here — Programming Foundations & Language Core

[← Back to Root Roadmap](../README.md) · [Next Module: 01 Complexity Analysis →](../01-Complexity-Analysis/README.md) · [Cheatsheet: C++ Core Syntax](../20-Cheatsheets/cpp-stl-cheatsheet.md)

---

## 1. What This Module Is & Why It Matters
Before diving into algorithmic abstractions, dynamic programming, or asymptotic complexity, every software engineer must build an intuitive, concrete mental model of **how computers execute programs**, **how memory is addressed**, and **how code maps to machine architecture**.

This module is the zero-prerequisite launchpad designed to take learners from absolute zero to fluent command of program structure, memory layout, control flow, functions, pointers, references, and modern standard library abstractions.

### Core Objectives
1. **Understand Machine Execution:** Understand how source code transforms via preprocessor, compiler, assembler, and linker into machine instructions.
2. **Master the Memory Model:** Grasp the distinction between the Stack (automatic allocation, call frames) and Heap (dynamic allocation, free store).
3. **Internalize Pointers & References:** Eliminate confusion around the address-of operator (`&`), dereferencing (`*`), pointer arithmetic, and reference aliasing.
4. **Acquire Multi-Language Literacy:** Primary focus on modern standard C++17, with complete cross-language translations in Python 3 and Java 17.

---

## 2. Recommended Study Order

```text
+------------------------------------+
| 01. Getting Started & Git          | -> Read: 01-getting-started-basics.md, 02-git-and-github.md
+------------------------------------+
                  |
                  v
+------------------------------------+
| 02. Language Syntax & Types        | -> Read: 03-cpp-fundamentals.md, 04-python-basics.md, 05-java-basics.md
+------------------------------------+
                  |
                  v
+------------------------------------+
| 03. Control Flow & Operators       | -> Read: 06-type-casting-and-operators.md, 07-conditionals-and-loops.md
+------------------------------------+
                  |
                  v
+------------------------------------+
| 04. Functions & Parameter Passing  | -> Read: 08-functions-and-parameter-passing.md
|                                    |    Problem: 002-pass-by-value-vs-reference
+------------------------------------+
                  |
                  v
+------------------------------------+
| 05. Memory Model & Pointers        | -> Read: 09-pointers-and-memory-model.md
|                                    |    Problem: 001-pointers-and-memory-basics
+------------------------------------+
                  |
                  v
+------------------------------------+
| 06. Arrays, Vectors & Bit Basics   | -> Read: 10-arrays-and-vectors-intro.md, 11-binary-number-system.md
|                                    |    Problem: 003-array-decay-and-dynamic-allocation
+------------------------------------+
                  |
                  v
+------------------------------------+
| 07. Self-Assessment Quiz           | -> Read: 12-mcqs-and-self-check.md
+------------------------------------+
```

---

## 3. Concept Guides Directory

| # | Concept Guide | Core Topics Covered | Read Time |
|---|---|---|---|
| 01 | [Getting Started & Basics](concepts/01-getting-started-basics.md) | Compilation cycle, tooling, environment setup, CLI | 15 min |
| 02 | [Git and GitHub Foundations](concepts/02-git-and-github.md) | Version control, staging, branching, merging | 10 min |
| 03 | [C++ Fundamentals](concepts/03-cpp-fundamentals.md) | Primitives, types, I/O streams, headers, scopes | 20 min |
| 04 | [Python Basics](concepts/04-python-basics.md) | Dynamic typing, lists, dicts, Python memory model | 10 min |
| 05 | [Java Basics](concepts/05-java-basics.md) | Classes, JVM memory, primitive vs reference types | 10 min |
| 06 | [Type Casting & Operators](concepts/06-type-casting-and-operators.md) | Arithmetic, bitwise, logic, explicit vs implicit casting | 12 min |
| 07 | [Conditionals & Loops](concepts/07-conditionals-and-loops.md) | `if/else`, `switch`, `for`, `while`, loop invariants | 15 min |
| 08 | [Functions & Parameter Passing](concepts/08-functions-and-parameter-passing.md) | Pass-by-value, reference, `const &`, call stack frames | 15 min |
| 09 | [Pointers & Memory Model](concepts/09-pointers-and-memory-model.md) | Virtual addresses, stack vs heap, pointer arithmetic | 25 min |
| 10 | [Arrays & Vectors Intro](concepts/10-arrays-and-vectors-intro.md) | Contiguous allocation, vector growth, array decay | 25 min |
| 11 | [Binary Number System](concepts/11-binary-number-system.md) | Two's complement, binary representation, overflow | 10 min |
| 12 | [MCQs & Self-Check](concepts/12-mcqs-and-self-check.md) | Comprehensive 25-question conceptual self-test | 20 min |

---

## 4. Problem & Code Portfolio

| # | Problem Name | Difficulty | Tier | Key Patterns | Solutions | Reference Link |
|---|---|---|---|---|---|---|
| 001 | [Pointers & Memory Basics](problems/001-pointers-and-memory-basics.md) | 🟢 Easy | Tier A | `#memory-model`, `#pointers` | [C++17](code/001-pointers-and-memory-basics/solution.cpp) · [Python3](code/001-pointers-and-memory-basics/solution.py) · [Java17](code/001-pointers-and-memory-basics/Solution.java) | [GeeksforGeeks](https://www.geeksforgeeks.org/cpp-pointers/) |
| 002 | [Pass-by-Value vs Reference](problems/002-pass-by-value-vs-reference.md) | 🟢 Easy | Tier A | `#functions`, `#parameter-passing` | [C++17](code/002-pass-by-value-vs-reference/solution.cpp) · [Python3](code/002-pass-by-value-vs-reference/solution.py) · [Java17](code/002-pass-by-value-vs-reference/Solution.java) | [GeeksforGeeks](https://www.geeksforgeeks.org/pass-by-value-and-pass-by-reference-in-cpp/) |
| 003 | [Array Decay & Dynamic Memory](problems/003-array-decay-and-dynamic-allocation.md) | 🟢 Easy | Tier A | `#memory-model`, `#arrays`, `#dynamic-allocation` | [C++17](code/003-array-decay-and-dynamic-allocation/solution.cpp) · [Python3](code/003-array-decay-and-dynamic-allocation/solution.py) · [Java17](code/003-array-decay-and-dynamic-allocation/Solution.java) | [GeeksforGeeks](https://www.geeksforgeeks.org/what-is-array-decay-in-c-how-can-it-be-prevented/) |

---

## 5. Top 5 Beginner Pitfalls & Interview Traps
1. **Accidental Deep Copies:** Passing large containers (`vector<int>`, `string`, `unordered_map`) by value into functions creates an $\mathcal{O}(N)$ hidden copy on every call. Always pass by `const Type&` when read-only.
2. **Returning Pointers/References to Stack Variables:** Variables allocated on the stack are destroyed when their enclosing function returns. Returning `&local_var` produces undefined behavior.
3. **Array Decay in C-Style Arrays:** `sizeof(arr)` inside a function accepting `int arr[]` evaluates to the size of a pointer (`sizeof(int*)`), not the total array length. Always pass `n` explicitly or use `std::vector` / `std::array`.
4. **Integer Overflow in Signed Types:** In 32-bit signed integers, `2 * 10^9 + 2 * 10^9` overflows into negative numbers. Use `long long` (or `int64_t`) for accumulator sums.
5. **Dangling Pointers & Uninitialized Pointers:** Declaring `int* p;` without initializing it leaves `p` holding random garbage. Always initialize pointers to `nullptr` or a valid address immediately.

---

## 6. What's Next
Now that you have mastered memory models, pointer mechanics, and fundamental syntax, proceed to the mathematical foundation of all algorithm evaluation:
👉 **[Module 01: Complexity Analysis (Big-O, Space-Time Tradeoffs, Asymptotics)](../01-Complexity-Analysis/README.md)**
