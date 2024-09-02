@echo off
REM Set up environment (adjust paths as needed)
set CONDA_HOME=C:\ProgramData\anaconda3
set PATH=%CONDA_HOME%\Scripts;%PATH%

REM Check Python version
python --version

REM Run pytest
pytest -v -s testcases\test_03.py
