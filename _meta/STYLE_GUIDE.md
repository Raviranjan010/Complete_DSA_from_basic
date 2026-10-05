# DSA Repository Style & Design Guide (`STYLE_GUIDE.md`)

## 1. Directory & File Naming Conventions
- Root folders: `NN-Topic-Name` (two-digit zero-padded prefix, Title-Case with hyphens, e.g., `03-Arrays/`).
- Subtopic folders: `kebab-case` (e.g., `two-pointers/`, `sliding-window/`).
- Problem markdown files: `NNN-problem-title-kebab-case.md` (three-digit per-topic sequence number, e.g., `001-two-sum.md`).
- Code directories: `code/<problem-slug>/` containing:
  - `solution.cpp` (C++17)
  - `solution.py` (Python 3)
  - `Solution.java` (Java 24)
  - `test_cases.json` or `tests/` directory with test cases.

## 2. Problem File Templates

### Tier A (Flagship Problem)
Every Tier A problem must contain:
1. Metadata Table (Title, Level L0–L6, Difficulty, Topic, Subtopic, Pattern, Tier A, Companies or NA, Prerequisites, External Links, Registry ID).
2. Problem Statement (Original paraphrase, verified constraints).
3. Verified Examples (At least 2, including edge cases).
4. What Is The Problem Really Asking?
5. Key Observation & Intuition.
6. How To Recognize This Pattern (Signal phrases).
7. Approach 1 — Brute Force (Idea, complexity, why it's slow).
8. Approach 2 — Better (If distinct, what improves).
9. Approach 3 — Optimal (Core insight, complexity, mathematical invariant).
10. Dry Run (Concrete table or ASCII trace step-by-step).
11. Verified Multi-Language Solutions (Embedded from `code/`):
    - C++17 Solution
    - Python 3 Solution
    - Java 24 Solution
12. Code Explanation & Invariants.
13. Complexity Analysis (Derived from code: Time & Space, worst/average/best).
14. Edge Cases (Empty, single element, duplicates, negatives, overflow).
15. Common Mistakes & Interview Follow-Ups.
16. Related Problems & Variants Table.

### Tier B (Practice Problem)
Compact format:
1. Metadata Table.
2. Problem Statement & Constraints.
3. Key Observation & Pattern.
4. Optimal Approach Summary.
5. Complexity Analysis.
6. Verified Code in C++, Python, and Java.
7. Edge Cases & External Links.

## 3. Code Standards
- **C++**: Modern C++17/20, `std::vector`, `std::string`, `std::unordered_map`, type-safe identifiers, explicit `long long` for overflow prevention.
- **Python**: Pythonic 3.12+, PEP 8 compliant, type hints (`from typing import List, Dict, Optional`).
- **Java**: Idiomatic Java 17+, class named `Solution`, appropriate collections (`HashMap`, `ArrayList`, `ArrayDeque`).
