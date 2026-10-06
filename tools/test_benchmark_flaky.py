#!/usr/bin/env python3
"""
tools/test_benchmark_flaky.py
Compiles and executes the benchmark suite in 01-Complexity-Analysis 5 consecutive times
across C++17, Python3, and Java17 to prove there is zero test flakiness.
"""

import os
import subprocess
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent

# Set up toolchain
sys.path.insert(0, str(repo_root / 'tools'))
import env_setup
env_setup.setup_toolchain()

code_dir = repo_root / '01-Complexity-Analysis' / 'code' / '001-time-complexity-benchmarking'
cpp_src = code_dir / 'solution.cpp'
py_src = code_dir / 'solution.py'
java_src = code_dir / 'Solution.java'
target_dir = repo_root / 'target'
target_dir.mkdir(exist_ok=True)
cpp_bin = target_dir / 'bench_cpp.exe'
java_classes = target_dir / 'classes'
java_classes.mkdir(exist_ok=True)

# 1. Compile C++
print("--- Compiling C++17 Benchmark ---")
res = subprocess.run(['g++', '-std=c++17', '-O2', str(cpp_src), '-o', str(cpp_bin)], capture_output=True, text=True)
if res.returncode != 0:
    print(f"C++ Compilation failed:\n{res.stderr}")
    sys.exit(1)
print("C++ Compilation SUCCESS.")

# 2. Compile Java
print("--- Compiling Java17 Benchmark ---")
res = subprocess.run(['javac', '--release', '17', '-d', str(java_classes), str(java_src)], capture_output=True, text=True)
if res.returncode != 0:
    print(f"Java Compilation failed:\n{res.stderr}")
    sys.exit(1)
print("Java Compilation SUCCESS.")

# 3. Run 5 consecutive iterations
print("\n=== RUNNING 5 CONSECUTIVE TRIALS (FLAKY-TEST VERIFICATION) ===")
for trial in range(1, 6):
    print(f"\n[Trial {trial}/5]")

    # Run C++
    res_cpp = subprocess.run([str(cpp_bin)], capture_output=True, text=True)
    if res_cpp.returncode != 0:
        print(f"  [FAIL] C++ trial {trial} crashed:\n{res_cpp.stderr}")
        sys.exit(1)
    print(f"  [C++17] PASS: {res_cpp.stdout.strip()}")

    # Run Python
    res_py = subprocess.run(['python', str(py_src)], capture_output=True, text=True)
    if res_py.returncode != 0:
        print(f"  [FAIL] Python trial {trial} crashed:\n{res_py.stderr}")
        sys.exit(1)
    print(f"  [Python3] PASS: {res_py.stdout.strip()}")

    # Run Java (with -ea to enable asserts)
    res_java = subprocess.run(['java', '-ea', '-cp', str(java_classes), 'Solution'], capture_output=True, text=True)
    if res_java.returncode != 0:
        print(f"  [FAIL] Java trial {trial} crashed:\n{res_java.stderr}")
        sys.exit(1)
    print(f"  [Java17] PASS: {res_java.stdout.strip()}")

print("\n>>> ALL 5 TRIALS PASSED FLAWLESSLY. ZERO FLAKINESS DETECTED. <<<")
