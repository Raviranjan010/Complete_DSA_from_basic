@echo off
echo Building Student Record Management System with Emscripten...

REM Check if emcc is available
where emcc >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: emcc not found. Please install Emscripten SDK first.
    echo Visit: https://emscripten.org/docs/getting_started/downloads.html
    exit /b 1
)

REM Compile the C++ code to WebAssembly
echo Compiling C++ code to WebAssembly...
emcc src/student.cpp -o web/student.js -lembind -sALLOW_MEMORY_GROWTH=1 -O2

if %errorlevel% equ 0 (
    echo Build successful!
    echo.
    echo To test locally:
    echo   1. Navigate to the web directory: cd web
    echo   2. Start a local server: python -m http.server 8000
    echo   3. Open your browser to: http://localhost:8000
    echo.
    echo To deploy to GitHub Pages:
    echo   1. Create a new GitHub repository
    echo   2. Push the contents of the web directory to the repository
    echo   3. Enable GitHub Pages in the repository settings
) else (
    echo Build failed. Please check the error messages above.
)