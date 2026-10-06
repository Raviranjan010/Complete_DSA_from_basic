#!/usr/bin/env python3
"""
tools/relocate_arrays_to_03.py
Moves the 18 array tutorial chapters from 00-Start-Here to 03-Arrays-and-Strings.
Updates navigation headers, updates MERGE_LEDGER.csv, and replaces 00-Start-Here array concept with a canonical link.
"""

import os
import re
import csv
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent

src_dir = repo_root / '00-Start-Here' / 'concepts'
dst_dir = repo_root / '03-Arrays-and-Strings' / 'concepts'

# List of 18 chapter files
ch_files = sorted([f for f in src_dir.glob('10-arrays-and-vectors-intro-ch*.md')])

print(f"Found {len(ch_files)} array chapter files to relocate from 00 to 03.")

# 1. Relocate files and rewrite header navigation
new_files = []
for f in ch_files:
    new_name = f.name.replace('10-arrays-and-vectors-intro-ch', '07-arrays-and-vectors-ch')
    dst_file = dst_dir / new_name
    
    content = f.read_text(encoding='utf-8')
    # Update navigation links inside file
    content = content.replace('10-arrays-and-vectors-intro-ch', '07-arrays-and-vectors-ch')
    content = content.replace('10-arrays-and-vectors-intro.md', '07-arrays-and-vectors-guide.md')
    
    dst_file.write_text(content, encoding='utf-8')
    f.unlink() # remove old file
    new_files.append((f.name, new_name, len(content.splitlines())))

# 2. Create 07-arrays-and-vectors-guide.md in 03-Arrays-and-Strings/concepts
guide_content = """# Arrays and Vectors — Complete Concept & Operations Guide

> **Module**: [03-Arrays-and-Strings](../README.md)  
> **Source**: Relocated from introductory dump to canonical Arrays & Strings module.

---

## 📚 Chapters Directory

"""

for old_n, new_n, lc in new_files:
    # Extract chapter title from file
    f_path = dst_dir / new_n
    lines = f_path.read_text(encoding='utf-8').splitlines()
    h1 = "Chapter"
    for l in lines:
        if l.startswith('# '):
            h1 = l.strip('# \t')
            break
    ch_num_match = re.search(r'ch(\d+)', new_n)
    ch_num = ch_num_match.group(1) if ch_num_match else "??"
    guide_content += f"- **Chapter {ch_num}**: [{h1}]({new_n}) ({lc} lines)\n"

(dst_dir / '07-arrays-and-vectors-guide.md').write_text(guide_content, encoding='utf-8')

# 3. Replace 00-Start-Here/concepts/10-arrays-and-vectors-intro.md with clean pointer
ptr_content = """# Arrays and Vectors — Foundational Transition Guide

Arrays and Vectors are foundational linear data structures. In this curriculum, comprehensive deep dives, algorithmic patterns, memory layout visualizations, and chapter tutorials for arrays and vectors are housed in their dedicated topic:

👉 **[Module 03: Arrays and Strings](../../03-Arrays-and-Strings/README.md)**  
👉 **[Arrays & Vectors Concept Hub](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-guide.md)**

---

## 📚 Direct Chapter References in Module 03

- [Ch 01: Array Basics — Complete Beginner Guide](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch01-array-basics-complete-beginner.md)
- [Ch 02: Complexity Analysis for Arrays](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch02-7-common-mistakes.md)
- [Ch 03: Vector vs Array — Decision Guide](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch03-vector-vs-array-decision-guide.md)
- [Ch 04: Array Indexing & Memory Offsets](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch04-4-array-indexing.md)
- [Ch 05: Binary Search Dry Run in Arrays](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch05-21-binary-search-dry-run.md)
- [Ch 06: Swapping, Min, and Max Values](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch06-36-swapping-maximum-and-minimu.md)
- [Ch 07: Array Decay & Parameter Passing](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch07-50-why-does-the-array-change.md)
- [Ch 08: Intersection of Two Arrays](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch08-66-intersection-of-two-arrays.md)
- [Ch 09: Common Array Pitfalls & Traps](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch09-78-common-array-mistakes.md)
- [Ch 10: Searching Practice Questions](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch10-83-practice-questions-searchin.md)
- [Ch 11: 2D Arrays & Matrix Fundamentals](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch11-91-practice-questions-2d-array.md)
- [Ch 12: Vector Header File & Dynamic Memory](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch12-3-vector-header-file.md)
- [Ch 13: Vector Modifiers & Iterators](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch13-19-front.md)
- [Ch 14: Modern C++ `auto` & Range-for](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch14-37-auto-with-vector.md)
- [Ch 15: Kadane's Algorithm Dry Run](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch15-52-kadane-dry-run.md)
- [Ch 16: Pair Sum / Two Sum on Unsorted Arrays](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch16-66-pair-sum-on-an-unsorted-arr.md)
- [Ch 17: Boyer-Moore Majority Element](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch17-79-candidate-vs-verified-major.md)
- [Ch 18: Pair Sum Pattern Recognition Guide](../../03-Arrays-and-Strings/concepts/07-arrays-and-vectors-ch18-91-pair-sum-pattern-recognitio.md)
"""
(src_dir / '10-arrays-and-vectors-intro.md').write_text(ptr_content, encoding='utf-8')

# 4. Log in _meta/MERGE_LEDGER.csv
ledger_path = repo_root / '_meta' / 'MERGE_LEDGER.csv'
with open(ledger_path, 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for old_n, new_n, lc in new_files:
        writer.writerow([
            f"03-Arrays-and-Strings/concepts/{new_n}",
            f"00-Start-Here/concepts/{old_n}",
            "DSA_server-main/DSA_ac-main arrays tutorial",
            f"Relocated {lc} lines of array/vector tutorial from 00-Start-Here to canonical 03-Arrays-and-Strings module (D13 audit)"
        ])
    writer.writerow([
        "03-Arrays-and-Strings/concepts/07-arrays-and-vectors-guide.md",
        "00-Start-Here/concepts/10-arrays-and-vectors-intro.md",
        "NA",
        "Created chapter hub in 03-Arrays-and-Strings for relocated array tutorial chapters"
    ])
    writer.writerow([
        "00-Start-Here/concepts/09-pointers-and-memory-model-ch10-pointers-in-c-complete-master.md",
        "00-Start-Here/concepts/11-binary-number-system.md",
        "NA",
        "Deduplicated 108 lines of Number Systems dump from pointers ch10; added cross-reference link"
    ])
    writer.writerow([
        "00-Start-Here/concepts/01-getting-started-basics-ch02-formula-approach-time-o1-space.md",
        "00-Start-Here/concepts/11-binary-number-system.md",
        "NA",
        "Deduplicated 33 lines of Number Systems dump from ch02; added cross-reference link"
    ])

print("Relocation complete and logged in MERGE_LEDGER.csv.")
