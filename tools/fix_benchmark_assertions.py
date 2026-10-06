from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
bench_dir = repo_root / '01-Complexity-Analysis' / 'code' / '001-time-complexity-benchmarking'

# 1. C++
cpp_file = bench_dir / 'solution.cpp'
cpp_text = cpp_file.read_text(encoding='utf-8')
cpp_text = cpp_text.replace(
    'assert(quadraticTimePairs(sample, 5) == 25);',
    'assert(quadraticTimePairs(sample, 5) == 5);\n    std::vector<int> sampleEq = {1, 1, 1, 1, 1};\n    assert(quadraticTimePairs(sampleEq, 5) == 25);'
)
cpp_file.write_text(cpp_text, encoding='utf-8')

# 2. Python
py_file = bench_dir / 'solution.py'
py_text = py_file.read_text(encoding='utf-8')
py_text = py_text.replace(
    'assert quadratic_pairs(sample, 5) == 25',
    'assert quadratic_pairs(sample, 5) == 5\n    sample_eq = [1, 1, 1, 1, 1]\n    assert quadratic_pairs(sample_eq, 5) == 25'
)
py_file.write_text(py_text, encoding='utf-8')

# 3. Java
java_file = bench_dir / 'Solution.java'
java_text = java_file.read_text(encoding='utf-8')
java_text = java_text.replace(
    'assert quadraticPairs(sample, 5) == 25 : "Quadratic pairs failed";',
    'assert quadraticPairs(sample, 5) == 5 : "Quadratic pairs failed";\n        int[] sampleEq = {1, 1, 1, 1, 1};\n        assert quadraticPairs(sampleEq, 5) == 25 : "Quadratic pairs equal failed";'
)
java_file.write_text(java_text, encoding='utf-8')

print("Fixed assertions in all 3 benchmark implementations.")
