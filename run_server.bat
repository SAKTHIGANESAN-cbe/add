@echo off
REM Plastic Waste Management System - Startup Script for Windows

echo.
echo ===================================
echo Plastic Waste Management System
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 
)

echo [✓] Python is installed
echo.

REM Check if Flask is installed
python -m pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Flask not found. Installing required packages...
    echo.
    python -m pip install flask werkzeug
    echo.
    echo [✓] Packages installed successfully
    echo.
) else (
    echo [✓] Flask is already installed
    echo.
)

REM Run the Flask application
echo Starting Flask server...
echo.
echo The application will be available at: http://127.0.0.1:5000
echo.
echo Demo Credentials:
echo   Username: demo_user
echo   Password: password123
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
