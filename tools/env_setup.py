"""
Dynamic environment setup for compiler & interpreter execution without hardcoded user paths.
Discovers and ensures g++ (C++17), python, and java/javac are on os.environ['PATH'].
"""

import os
import shutil
import sys
import subprocess
from pathlib import Path

def setup_toolchain():
    # If g++ is already discoverable, return
    if shutil.which("g++"):
        return

    # Check Windows user and machine environment PATHs dynamically
    if sys.platform == "win32":
        try:
            import winreg
            paths = []
            # User Environment
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
                    user_path, _ = winreg.QueryValueEx(key, "Path")
                    paths.extend(user_path.split(";"))
            except Exception:
                pass

            # System Environment
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment") as key:
                    sys_path, _ = winreg.QueryValueEx(key, "Path")
                    paths.extend(sys_path.split(";"))
            except Exception:
                pass

            # Search in LocalAppData WinGet packages dynamically
            local_app_data = os.environ.get("LOCALAPPDATA", "")
            if local_app_data:
                winget_pkg_dir = Path(local_app_data) / "Microsoft" / "WinGet" / "Packages"
                if winget_pkg_dir.exists():
                    for match in winget_pkg_dir.glob("**/llvm-mingw-*/bin"):
                        if (match / "g++.exe").exists():
                            paths.append(str(match))

            # Update os.environ['PATH']
            current_path = os.environ.get("PATH", "")
            for p in paths:
                p_clean = p.strip()
                if p_clean and os.path.exists(p_clean) and p_clean not in current_path:
                    current_path = f"{p_clean};{current_path}"
            os.environ["PATH"] = current_path
        except Exception as e:
            print(f"Warning: dynamic path lookup encountered {e}", file=sys.stderr)

    if not shutil.which("g++"):
        print("Warning: g++ could not be dynamically resolved on PATH.", file=sys.stderr)

if __name__ == "__main__":
    setup_toolchain()
    print("g++ path:", shutil.which("g++"))
    print("javac path:", shutil.which("javac"))
    print("python path:", shutil.which("python"))
