#!/usr/bin/env python3
"""
Creates clean, compact chapter index files (<40 lines) for the 5 split concept modules
in 00-Start-Here/concepts/ to ensure all incoming markdown links remain 100% valid.
"""

from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
cdir = repo_root / '00-Start-Here' / 'concepts'

indices = {
    '01-getting-started-basics.md': (
        "01: Getting Started Basics — Chapter Index",
        [
            ("Chapter 01: Absolute Basics & Algorithms", "01-getting-started-basics-ch01-00-start-here-absolute-basics.md"),
            ("Chapter 02: Formula Approaches & Complexity Intro", "01-getting-started-basics-ch02-formula-approach-time-o1-space.md"),
            ("Chapter 03: Complete C++ Prerequisites", "01-getting-started-basics-ch03-00-c-prerequisites-complete-no.md"),
            ("Chapter 04: Visual Memory Layout Diagram", "01-getting-started-basics-ch04-4-visual-diagram-c-memory-layo.md"),
            ("Chapter 05: Interview Tips & Company Patterns", "01-getting-started-basics-ch05-10-interview-tips-what-compani.md")
        ]
    ),
    '03-cpp-fundamentals.md': (
        "03: C++ Fundamentals for DSA — Chapter Index",
        [
            ("Chapter 01: Syntax & Preprocessor Directives", "03-cpp-fundamentals-ch01-c-fundamentals-for-dsa.md"),
            ("Chapter 02: Floating Point & Primitive Types", "03-cpp-fundamentals-ch02-12-float.md"),
            ("Chapter 03: Categories of Operators", "03-cpp-fundamentals-ch03-25-main-categories-of-operator.md"),
            ("Chapter 04: Bitwise Operations in Depth", "03-cpp-fundamentals-ch04-40-bitwise-xor.md"),
            ("Chapter 05: Operator Classification", "03-cpp-fundamentals-ch05-55-operator-classification-by.md"),
            ("Chapter 06: Mental Models & Type Evaluation", "03-cpp-fundamentals-ch06-62-final-mental-model.md"),
            ("Chapter 07: Control Flow & Else-If Ladder", "03-cpp-fundamentals-ch07-9-how-else-if-works.md"),
            ("Chapter 08: Switch-Case Statements", "03-cpp-fundamentals-ch08-21-can-switch-replace-every-if.md"),
            ("Chapter 09: Type Conversions & Casting", "03-cpp-fundamentals-ch09-35-character-to-integer-conver.md"),
            ("Chapter 10: Conditional Patterns in DSA", "03-cpp-fundamentals-ch10-50-dsa-pattern-conditional-fil.md"),
            ("Chapter 11: Fast Syntax Cheatsheet", "03-cpp-fundamentals-ch11-c-syntax-for-dsa-your-cheat-sh.md")
        ]
    ),
    '07-conditionals-and-loops.md': (
        "07: Conditionals and Loops — Chapter Index",
        [
            ("Chapter 01: Conditionals & Branching", "07-conditionals-and-loops-ch01-chapter.md"),
            ("Chapter 02: Loops & Iteration Mechanics", "07-conditionals-and-loops-ch02-loops-in-c.md"),
            ("Chapter 03: Pattern Printing Foundations", "07-conditionals-and-loops-ch03-master-c-pattern-printing.md"),
            ("Chapter 04: Advanced Space Patterns", "07-conditionals-and-loops-ch04-5-mirrored-space-patterns.md")
        ]
    ),
    '09-pointers-and-memory-model.md': (
        "09: Pointers & Memory Model — Chapter Index",
        [
            ("Chapter 01: Pointer Foundations & Address-of", "09-pointers-and-memory-model-ch01-dsa-c-complete-notes-pointers.md"),
            ("Chapter 02: Pointer Variables & Memory Slots", "09-pointers-and-memory-model-ch02-13-pointer-and-variable-are-di.md"),
            ("Chapter 03: Dereferencing & Mutation", "09-pointers-and-memory-model-ch03-27-modifying-through-pointer-t.md"),
            ("Chapter 04: Pass-by-Value vs Pass-by-Pointer", "09-pointers-and-memory-model-ch04-42-pass-by-value-vs-pointer.md"),
            ("Chapter 05: Dynamic Memory & Double Delete Guard", "09-pointers-and-memory-model-ch05-56-double-delete.md"),
            ("Chapter 06: Pointers and Const Qualifiers", "09-pointers-and-memory-model-ch06-69-pointers-and-const-in-funct.md"),
            ("Chapter 07: Common Pointer Pitfalls", "09-pointers-and-memory-model-ch07-82-common-pointer-mistakes.md"),
            ("Chapter 08: Pointer-Recursion Connection", "09-pointers-and-memory-model-ch08-94-pointer-recursion-connectio.md"),
            ("Chapter 09: The Pointer Mindset", "09-pointers-and-memory-model-ch09-103-pointer-mindset.md"),
            ("Chapter 10: Complete C++ Pointer Reference", "09-pointers-and-memory-model-ch10-pointers-in-c-complete-master.md"),
            ("Chapter 11: Array Memory Layout Under the Hood", "09-pointers-and-memory-model-ch11-memory-model-how-arrays-work-i.md"),
            ("Chapter 12: Pointers and Arrays Connection", "09-pointers-and-memory-model-ch12-pointers-and-arrays-in-c.md")
        ]
    ),
    '10-arrays-and-vectors-intro.md': (
        "10: Arrays and Vectors Intro — Chapter Index",
        [
            ("Chapter 01: Beginner Array Basics", "10-arrays-and-vectors-intro-ch01-array-basics-complete-beginner.md"),
            ("Chapter 02: Common Array Mistakes", "10-arrays-and-vectors-intro-ch02-7-common-mistakes.md"),
            ("Chapter 03: Vector vs Fixed Array Decision Guide", "10-arrays-and-vectors-intro-ch03-vector-vs-array-decision-guide.md"),
            ("Chapter 04: Indexing & Element Retrieval", "10-arrays-and-vectors-intro-ch04-4-array-indexing.md"),
            ("Chapter 05: Array Traversal & Binary Search Demo", "10-arrays-and-vectors-intro-ch05-21-binary-search-dry-run.md"),
            ("Chapter 06: Element Swapping & Min/Max Tracking", "10-arrays-and-vectors-intro-ch06-36-swapping-maximum-and-minimu.md"),
            ("Chapter 07: Memory Mutability During Traversal", "10-arrays-and-vectors-intro-ch07-50-why-does-the-array-change.md"),
            ("Chapter 08: Array Intersection & Subarrays", "10-arrays-and-vectors-intro-ch08-66-intersection-of-two-arrays.md"),
            ("Chapter 09: Array Pitfalls & Boundary Conditions", "10-arrays-and-vectors-intro-ch09-78-common-array-mistakes.md"),
            ("Chapter 10: Searching Practice Patterns", "10-arrays-and-vectors-intro-ch10-83-practice-questions-searchin.md"),
            ("Chapter 11: 2D Matrix Basics & Grid Layout", "10-arrays-and-vectors-intro-ch11-91-practice-questions-2d-array.md"),
            ("Chapter 12: STL Vector Header & Dynamic Resizing", "10-arrays-and-vectors-intro-ch12-3-vector-header-file.md"),
            ("Chapter 13: Vector Member Functions", "10-arrays-and-vectors-intro-ch13-19-front.md"),
            ("Chapter 14: Auto Keywords with Iterators", "10-arrays-and-vectors-intro-ch14-37-auto-with-vector.md"),
            ("Chapter 15: Subarray Sums & Kadane Basics", "10-arrays-and-vectors-intro-ch15-52-kadane-dry-run.md"),
            ("Chapter 16: Pair Sum on Arrays", "10-arrays-and-vectors-intro-ch16-66-pair-sum-on-an-unsorted-arr.md"),
            ("Chapter 17: Majority Element Mechanics", "10-arrays-and-vectors-intro-ch17-79-candidate-vs-verified-major.md"),
            ("Chapter 18: Array Pattern Recognition Guide", "10-arrays-and-vectors-intro-ch18-91-pair-sum-pattern-recognitio.md")
        ]
    )
}

for fname, (title, chaps) in indices.items():
    fp = cdir / fname
    lines = [
        f"# {title}",
        "",
        "[← Back to Module Overview](../README.md)",
        "",
        "---",
        "",
        "## Chapters Directory",
        ""
    ]
    for ch_title, ch_file in chaps:
        lines.append(f"- [{ch_title}]({ch_file})")
    lines.append("")
    fp.write_text('\n'.join(lines), encoding='utf-8')

print("Created index files successfully.")
