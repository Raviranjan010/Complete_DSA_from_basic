#!/usr/bin/env python3
"""
tools/tests/test_check_template.py
Self-test suite for tools/check_template.py.
Proves that the checker:
1. FAILS on legacy dump 03/problems/001-two-sum-pair-sum.md (multi-problem, missing metadata).
2. FAILS on 02-Math stub 02-Math-for-DSA/problems/001-gcd-and-lcm-euclidean.md (stub with missing sections).
3. FAILS on an empty-section file.
4. PASSES on a known-good Tier A file (tools/tests/sample_valid_tier_a.md).
"""

import sys
from pathlib import Path

# Add tools to sys.path
repo_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(repo_root / 'tools'))

from check_template import validate_problem_file

def run_self_tests():
    tests_passed = True
    print("=== RUNNING check_template.py SELF-TESTS ===")

    # Test 1: Legacy multi-problem dump in 03
    p1 = repo_root / '03-Arrays-and-Strings' / 'problems' / '001-two-sum-pair-sum.md'
    valid1, tier1, errs1 = validate_problem_file(p1)
    if not valid1:
        print("  [TEST 1 PASS] 03 legacy dump correctly FAILED validation.")
    else:
        print("  [TEST 1 FAIL] 03 legacy dump unexpectedly passed validation!")
        tests_passed = False

    # Test 2: 02-Math stub
    p2 = repo_root / '02-Math-for-DSA' / 'problems' / '001-gcd-and-lcm-euclidean.md'
    valid2, tier2, errs2 = validate_problem_file(p2)
    if not valid2:
        print("  [TEST 2 PASS] 02-Math stub correctly FAILED validation.")
    else:
        print("  [TEST 2 FAIL] 02-Math stub unexpectedly passed validation!")
        tests_passed = False

    # Test 3: Temporary empty-section file
    empty_sec_file = repo_root / 'tools' / 'tests' / 'temp_empty_section.md'
    empty_sec_content = """# Title
| Field | Value |
|---|---|
| **Difficulty** | Easy |
| **Tier** | Tier A |
| **Pattern** | #math |

## 1. Problem Statement
Some statement.

## 2. Constraints
---

## 3. Examples
Example content here.
"""
    empty_sec_file.write_text(empty_sec_content, encoding='utf-8')
    valid3, tier3, errs3 = validate_problem_file(empty_sec_file)
    empty_sec_file.unlink(missing_ok=True)
    if not valid3:
        print("  [TEST 3 PASS] Empty-section file correctly FAILED validation.")
    else:
        print("  [TEST 3 FAIL] Empty-section file unexpectedly passed validation!")
        tests_passed = False

    # Test 4: Known-good Tier A file
    p4 = repo_root / 'tools' / 'tests' / 'sample_valid_tier_a.md'
    valid4, tier4, errs4 = validate_problem_file(p4)
    if valid4 and tier4 == 'A':
        print("  [TEST 4 PASS] Known-good Tier A sample correctly PASSED validation.")
    else:
        print(f"  [TEST 4 FAIL] Known-good Tier A sample failed validation! Errors: {errs4}")
        tests_passed = False

    print("=" * 45)
    if tests_passed:
        print(">>> ALL check_template SELF-TESTS PASSED <<<")
    else:
        print(">>> SELF-TEST FAILURES DETECTED <<<")
    return tests_passed

if __name__ == '__main__':
    ok = run_self_tests()
    sys.exit(0 if ok else 1)
