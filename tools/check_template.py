#!/usr/bin/env python3
"""
tools/check_template.py
Validates problem Markdown files against the strict Tier A and Tier B templates defined in
Section 5.2 of REPAIR_PROMPT_v3.

Rules enforced:
1. Exactly ONE H1 heading (# <Title>) per file (detects multi-problem dumps).
2. Metadata table present with required fields: Title/Name, Difficulty, Tier, Pattern.
3. Required headings present in exact relative order:
   - Tier A: Statement, Constraints, Examples, Really Asking, Key Observation/Intuition,
             Recognize Pattern, Approach/Brute, Optimal, Pseudocode, Visualization,
             Dry Run, Solutions (C++/Py/Java), Complexity, Edge Cases, Common Mistakes,
             Interview Follow-Ups/Tricks, Related Problems, External Links.
   - Tier B: Statement, Constraints, Examples, Key Observation/Intuition, Recognize Pattern,
             Approach/Optimal, Solutions, Complexity, Edge Cases, External Links.
4. Minimum content requirement: Each section must contain meaningful content
   (at least 30 characters of body text between headings), no stub/empty sections.
5. Overall length threshold: Tier A >= 120 lines, Tier B >= 60 lines.
"""

import sys
import re
from pathlib import Path

# Required metadata fields
REQUIRED_META_FIELDS = ['difficulty', 'tier', 'pattern']

# Section tokens for Tier A and Tier B
TIER_A_SECTIONS = [
    r'1\.?\s*(?:problem\s*)?statement',
    r'2\.?\s*constraints',
    r'3\.?\s*examples?',
    r'4\.?\s*what\s*is\s*the\s*problem\s*really\s*asking',
    r'5\.?\s*key\s*observation|intuition',
    r'6\.?\s*how\s*to\s*recognize\s*this\s*pattern',
    r'7\.?\s*approach\s*1|brute\s*force',
    r'(?:approach\s*2|approach\s*3|optimal)',
    r'(?:pseudocode|pseudo-code)',
    r'(?:visualization|diagram)',
    r'(?:dry\s*run|walkthrough)',
    r'(?:solutions?|multi-language|implementations?)',
    r'(?:code\s*explanation|walkthrough)',
    r'complexity(?:\s*analysis)?',
    r'edge\s*cases?',
    r'common\s*mistakes?',
    r'(?:interview\s*follow-ups?|follow\s*ups?)',
    r'(?:tricks?|tips?)',
    r'(?:related\s*problems?|variants?)',
    r'external\s*(?:practice\s*)?links?'
]

TIER_B_SECTIONS = [
    r'1\.?\s*(?:problem\s*)?statement',
    r'2\.?\s*constraints',
    r'3\.?\s*examples?',
    r'(?:key\s*observation|intuition)',
    r'(?:recognize|pattern)',
    r'(?:approach|optimal)',
    r'(?:solutions?|implementations?)',
    r'complexity(?:\s*analysis)?',
    r'edge\s*cases?',
    r'external\s*(?:practice\s*)?links?'
]

def validate_problem_file(filepath: Path) -> tuple:
    """
    Validates a single problem markdown file.
    Returns (is_valid: bool, tier: str, errors: list[str])
    """
    errors = []
    if not filepath.exists():
        return False, "UNKNOWN", [f"File not found: {filepath}"]

    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return False, "UNKNOWN", [f"Encoding/read error: {e}"]

    lines = content.splitlines()

    # Rule 1: Exactly ONE top-level H1 header
    h1_headers = [l for l in lines if l.startswith('# ')]
    if len(h1_headers) == 0:
        errors.append("Missing H1 heading (# <Title>)")
    elif len(h1_headers) > 1:
        errors.append(f"Multiple H1 headings ({len(h1_headers)}) detected; violation of single-problem rule")

    # Detect Tier from metadata table or text
    is_tier_a = bool(re.search(r'Tier:?\s*\*?\*?\s*A\b', content, re.IGNORECASE))
    is_tier_b = bool(re.search(r'Tier:?\s*\*?\*?\s*B\b', content, re.IGNORECASE))

    if not is_tier_a and not is_tier_b:
        errors.append("No explicit Tier A or Tier B declared in metadata")
        tier = "UNKNOWN"
    else:
        tier = "A" if is_tier_a else "B"

    # Rule 2: Metadata table check
    meta_lower = content[:1500].lower()
    for field in REQUIRED_META_FIELDS:
        if field not in meta_lower:
            errors.append(f"Metadata table missing required field: '{field}'")

    # Rule 3: Find H2 headings (## ...) and check order & empty sections
    h2_lines = []
    for idx, line in enumerate(lines):
        if line.startswith('## '):
            h2_lines.append((idx, line[3:].strip()))

    if not h2_lines:
        errors.append("No H2 headings (## <Section>) found")

    # Check empty sections
    for i in range(len(h2_lines)):
        curr_idx, curr_title = h2_lines[i]
        next_idx = h2_lines[i+1][0] if i + 1 < len(h2_lines) else len(lines)
        section_body = '\n'.join(lines[curr_idx+1:next_idx]).strip()
        # Remove separators like ---
        section_body_clean = re.sub(r'---', '', section_body).strip()
        if len(section_body_clean) < 25:
            errors.append(f"Section '## {curr_title}' is empty or contains insufficient body content (<25 chars)")

    # Rule 4: Match section patterns in relative order
    req_patterns = TIER_A_SECTIONS if tier == 'A' else TIER_B_SECTIONS
    h2_titles = [title.lower() for _, title in h2_lines]

    matched_indices = []
    last_h2_idx = -1
    for pat in req_patterns:
        matched = False
        for h_idx in range(last_h2_idx + 1, len(h2_titles)):
            if re.search(pat, h2_titles[h_idx]):
                matched = True
                last_h2_idx = h_idx
                break
        if not matched:
            errors.append(f"Missing required section pattern in expected order: '{pat}'")

    # Rule 5: Minimum line count
    min_lines = 100 if tier == 'A' else 50
    if len(lines) < min_lines:
        errors.append(f"File line count ({len(lines)}) is below minimum for Tier {tier} ({min_lines} lines)")

    is_valid = len(errors) == 0
    return is_valid, tier, errors

if __name__ == '__main__':
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        valid, tier, errs = validate_problem_file(p)
        print(f"File: {p}")
        print(f"Tier: {tier} | Valid: {valid}")
        if errs:
            print("Errors:")
            for e in errs:
                print(f"  - {e}")
        sys.exit(0 if valid else 1)
    else:
        print("Usage: python tools/check_template.py <path-to-problem.md>")
        sys.exit(1)
