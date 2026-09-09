@echo off
echo Starting local server for testing...
echo Navigate to http://localhost:8000 in your browser

cd web
python -m http.server 8000