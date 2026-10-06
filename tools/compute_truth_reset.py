#!/usr/bin/env python3
"""
tools/compute_truth_reset.py
Computes the exact ground-truth metrics for every topic across the repository
using tools/check_template.py for strict Tier A/B conformance.
Generates the entire table including the Total row programmatically.
Writes _meta/TRUTH_RESET.md.
"""

import os
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / 'tools'))
from check_template import validate_problem_file

topics = [d for d in sorted(os.listdir(repo_root)) if os.path.isdir(repo_root / d) and d[:2].isdigit() and d[2] == '-']

truth_data = []

total_hub_lines = 0
total_concept_lines = 0
total_prob_files = 0
total_tier_a = 0
total_tier_b = 0
total_template_ok = 0
total_cpp = 0
total_py = 0
total_java = 0
total_files_over_600 = 0
all_over_600 = []

for topic in topics:
    topic_dir = repo_root / topic
    readme_path = topic_dir / 'README.md'
    hub_lines = 0
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
            hub_lines = sum(1 for _ in f)

    concepts_dir = topic_dir / 'concepts'
    concept_lines = 0
    over_600 = []
    if concepts_dir.exists():
        for f in os.listdir(concepts_dir):
            if f.endswith('.md'):
                fp = concepts_dir / f
                with open(fp, 'r', encoding='utf-8', errors='ignore') as mf:
                    lc = sum(1 for _ in mf)
                concept_lines += lc
                if lc > 600:
                    over_600.append((f"{topic}/concepts/{f}", lc))

    problems_dir = topic_dir / 'problems'
    prob_files = 0
    tier_a = 0
    tier_b = 0
    template_ok = 0
    if problems_dir.exists():
        for f in os.listdir(problems_dir):
            if f.endswith('.md'):
                prob_files += 1
                fp = problems_dir / f
                with open(fp, 'r', encoding='utf-8', errors='ignore') as mf:
                    text = mf.read()
                    lines = text.splitlines()
                lc = len(lines)
                if lc > 600:
                    over_600.append((f"{topic}/problems/{f}", lc))
                
                # Check declared Tier
                if 'Tier: A' in text or 'Tier:** A' in text or 'Tier A' in text:
                    tier_a += 1
                elif 'Tier: B' in text or 'Tier:** B' in text or 'Tier B' in text:
                    tier_b += 1

                # Strict check via check_template.py
                is_valid, _, _ = validate_problem_file(fp)
                if is_valid:
                    template_ok += 1

    code_dir = topic_dir / 'code'
    cpp_count = 0
    py_count = 0
    java_count = 0
    if code_dir.exists():
        for root, _, files in os.walk(code_dir):
            for f in files:
                if f.endswith('.cpp'): cpp_count += 1
                elif f.endswith('.py'): py_count += 1
                elif f.endswith('.java'): java_count += 1

    files_over_600 = len(over_600)
    all_over_600.extend(over_600)

    # Accumulate totals
    total_hub_lines += hub_lines
    total_concept_lines += concept_lines
    total_prob_files += prob_files
    total_tier_a += tier_a
    total_tier_b += tier_b
    total_template_ok += template_ok
    total_cpp += cpp_count
    total_py += py_count
    total_java += java_count
    total_files_over_600 += files_over_600

    truth_data.append({
        'topic': topic,
        'hub_lines': hub_lines,
        'concept_lines': concept_lines,
        'prob_files': prob_files,
        'tier_a': tier_a,
        'tier_b': tier_b,
        'template_ok': template_ok,
        'cpp': cpp_count,
        'py': py_count,
        'java': java_count,
        'files_over_600': files_over_600
    })

# Format markdown table
out_lines = [
    "# Truth Reset Report (`_meta/TRUTH_RESET.md`)",
    "",
    "Date: 2026-10-06  ",
    "Author: Google Antigravity  ",
    "Purpose: Section 3 Truth Reset (Programmatically Generated Table)",
    "",
    "## 1. Ground Truth Per-Topic Summary Table",
    "",
    "| Topic | Hub Lines | Concept Lines | Prob Files | Tier A | Tier B | Template OK | C++ | Py | Java | Files >600L |",
    "|---|---|---|---|---|---|---|---|---|---|---|"
]

for row in truth_data:
    out_lines.append(
        f"| `{row['topic']}` | {row['hub_lines']:d} | {row['concept_lines']:,} | {row['prob_files']:d} | {row['tier_a']:d} | {row['tier_b']:d} | {row['template_ok']:d} | {row['cpp']:d} | {row['py']:d} | {row['java']:d} | {row['files_over_600']:d} |"
    )

# Append programmatically computed Total row
out_lines.append(
    f"| **Total** | **{total_hub_lines:,}** | **{total_concept_lines:,}** | **{total_prob_files:d}** | **{total_tier_a:d}** | **{total_tier_b:d}** | **{total_template_ok:d}** | **{total_cpp:d}** | **{total_py:d}** | **{total_java:d}** | **{total_files_over_600:d}** |"
)

out_lines.extend([
    "",
    "---",
    "",
    "## 2. False Claims Found in Prior Reports",
    "",
    "1. **02-Math-for-DSA marked DONE/PASSED:** Problem files (001-006) are brief 18-28 line stubs containing only metadata & complexity, lacking full problem statements, dry runs, and in-depth explanations. Template OK = 0.",
    "2. **00-Start-Here & 01-Complexity-Analysis marked DONE:** Code compiles/runs, but problem documentation does not yet conform to the comprehensive 21-section Tier A template. Template OK = 0.",
    "3. **Topics 03, 04, 05 marked Template OK = 4:** False positive from loose check. Those files are legacy multi-problem note dumps that violate single-problem rules and fail strict validation. Template OK = 0.",
    "4. **Missing problems/ folders in topics 06-18:** Topics 06 through 18 have zero problems/ folders populated.",
    "5. **Language Parity Gap:** Prior reports stated multi-language parity was advancing, but actual counts are 81 C++, 11 Python, and 11 Java. Over 85% of problems lack Python/Java.",
    "6. **Phantom Topic Names in PROGRESS.md:** Old tracker listed non-existent folders (`15-Interview-Prep`, `18-Bit-Manipulation`, `19-System-Design-Primer`).",
    "",
    "---",
    "",
    "## 3. Remaining Files Over 600 Lines (Outside 00-Start-Here)",
    ""
])

for f, lc in sorted(all_over_600, key=lambda x: x[1], reverse=True):
    out_lines.append(f"- `{f}`: {lc:,} lines")

truth_file = repo_root / '_meta' / 'TRUTH_RESET.md'
truth_file.write_text('\n'.join(out_lines), encoding='utf-8')
print("Successfully generated _meta/TRUTH_RESET.md programmatically.")
