@echo off
REM Check Python installation
python --version
if %ERRORLEVEL% NEQ 0 (
    echo "Python is not installed or not in PATH."
    exit /b 1
)

REM Install pytest if it is not already installed
pip show pytest >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo "Installing pytest..."
    pip install pytest
)

REM Run pytest using full path
C:\Users\b.rakesh\AppData\Local\Microsoft\WindowsApps\python.exe -v -s testcases\test_03.py
if %ERRORLEVEL% NEQ 0 (
    echo "Pytest failed."
    exit /b 1
)
