@echo off
echo Verifying Student Record Management System project structure...

echo Checking for required directories...
if exist "src" (
    echo [OK] src directory found
) else (
    echo [ERROR] src directory not found
    exit /b 1
)

if exist "web" (
    echo [OK] web directory found
) else (
    echo [ERROR] web directory not found
    exit /b 1
)

echo.
echo Checking for required source files...
if exist "src\student.cpp" (
    echo [OK] src/student.cpp found
) else (
    echo [ERROR] src/student.cpp not found
    exit /b 1
)

echo.
echo Checking for required web files...
if exist "web\index.html" (
    echo [OK] web/index.html found
) else (
    echo [ERROR] web/index.html not found
    exit /b 1
)

if exist "web\app.js" (
    echo [OK] web/app.js found
) else (
    echo [ERROR] web/app.js not found
    exit /b 1
)

if exist "web\style.css" (
    echo [OK] web/style.css found
) else (
    echo [ERROR] web/style.css not found
    exit /b 1
)

echo.
echo Checking for documentation and helper files...
if exist "README.md" (
    echo [OK] README.md found
) else (
    echo [WARNING] README.md not found
)

if exist ".gitignore" (
    echo [OK] .gitignore found
) else (
    echo [WARNING] .gitignore not found
)

if exist "build.bat" (
    echo [OK] build.bat found
) else (
    echo [WARNING] build.bat not found
)

if exist "serve.bat" (
    echo [OK] serve.bat found
) else (
    echo [WARNING] serve.bat not found
)

echo.
echo Verification complete! The project structure is ready.
echo.
echo Next steps:
echo 1. Install Emscripten SDK
echo 2. Run build.bat to compile the C++ code to WebAssembly
echo 3. Run serve.bat to test locally
echo 4. Run deploy.bat to prepare for GitHub deployment