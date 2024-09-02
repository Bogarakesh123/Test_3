@echo off
REM Check Python version
"C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\python.exe" --version
REM Run pytest
"C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\Scripts\pytest.exe" -v -s testcases\test_03.py
