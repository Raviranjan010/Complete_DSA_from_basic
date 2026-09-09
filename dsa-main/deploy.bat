@echo off
echo Deploying Student Record Management System to GitHub...

REM This script assumes you have already compiled the project with build.bat
REM and that you're in the project root directory

echo Creating git repository...
git init
git add .
git commit -m "Initial commit: Student Record Management System with WebAssembly"

echo.
echo To deploy to GitHub:
echo 1. Create a new repository on GitHub
echo 2. Run the following commands:
echo    git remote add origin https://github.com/yourusername/your-repo-name.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Then enable GitHub Pages in your repository settings.