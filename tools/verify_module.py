import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
import env_setup
env_setup.setup_toolchain()

def verify_module(module_path):
    code_dir = os.path.join(module_path, 'code')
    if not os.path.isdir(code_dir):
        print(f"No code directory found in {module_path}")
        return True

    all_passed = True
    os.makedirs('target/classes', exist_ok=True)

    for item in sorted(os.listdir(code_dir)):
        item_path = os.path.join(code_dir, item)
        if not os.path.isdir(item_path):
            continue

        print(f"\n--- Checking Problem: {item} ---")
        cpp_file = os.path.join(item_path, 'solution.cpp')
        py_file = os.path.join(item_path, 'solution.py')
        java_file = os.path.join(item_path, 'Solution.java')

        if os.path.exists(cpp_file):
            cmd = ['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-fsyntax-only', cpp_file]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print("  [C++17] PASS")
            else:
                print(f"  [C++17] FAIL:\n{res.stderr}")
                all_passed = False

        if os.path.exists(py_file):
            cmd = ['python', py_file]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print("  [Python3] PASS")
            else:
                print(f"  [Python3] FAIL:\n{res.stderr}")
                all_passed = False

        if os.path.exists(java_file):
            cmd = ['javac', '--release', '17', '-d', 'target/classes', java_file]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print("  [Java17] PASS")
            else:
                print(f"  [Java17] FAIL (rc={res.returncode}):\nStdout: {res.stdout}\nStderr: {res.stderr}")
                all_passed = False

    return all_passed

if __name__ == '__main__':
    mod = sys.argv[1] if len(sys.argv) > 1 else '00-Start-Here'
    success = verify_module(mod)
    sys.exit(0 if success else 1)
