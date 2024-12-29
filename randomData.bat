@echo off
setlocal

:: Change to the directory of the script
cd /d "%~dp0"

:: Set the path to the embedded Python interpreter
set PYTHON_HOME=python

:: Run the Python script
"%PYTHON_HOME%\python.exe" RandomData.py

pause