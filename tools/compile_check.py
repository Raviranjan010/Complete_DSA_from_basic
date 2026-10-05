import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(__file__))
import env_setup
env_setup.setup_toolchain()

def check_file(fp):
    cmd = ['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-fsyntax-only', fp]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return fp, res.returncode == 0, res.stderr

def main():
    target_files = []
    for root, dirs, files in os.walk('.'):
        parts = [p for p in root.split(os.sep) if p and p != '.']
        if any(p.startswith('.') or p in ('_meta', '_archive', '_extras', 'target') for p in parts):
            continue
        for f in files:
            if f.endswith('.cpp'):
                target_files.append(os.path.join(root, f))
    
    print(f"Checking {len(target_files)} C++ files in parallel...", flush=True)
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(check_file, target_files))
    
    passed = [r[0] for r in results if r[1]]
    failed = [(r[0], r[2]) for r in results if not r[1]]

    print(f"Passed: {len(passed)}/{len(target_files)}", flush=True)
    if failed:
        print(f"Failed: {len(failed)}", flush=True)
        for fp, err in failed:
            print(f"\n--- FAILED: {fp} ---\n{err.strip()}", flush=True)
        sys.exit(1)
    else:
        print("All C++ files compiled successfully without syntax errors!", flush=True)

if __name__ == '__main__':
    main()
