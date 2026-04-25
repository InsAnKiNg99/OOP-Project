@echo off

echo.
echo ======================================
echo UOT Admission Portal - Web Application
echo ======================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
)

call venv\Scripts\activate.bat

pip show Flask >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Dependencies installed successfully.
)

echo.
echo Starting UOT Admission Portal...
echo Application will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python main.py

pause
