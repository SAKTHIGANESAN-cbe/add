# Plastic Waste Management System - PowerShell Startup Script

Write-Host ""
Write-Host "===================================" -ForegroundColor Green
Write-Host "Plastic Waste Management System" -ForegroundColor Green
Write-Host "===================================" -ForegroundColor Green
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[✓] Python is installed: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[✗] ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Check if Flask is installed
$flaskCheck = pip show flask 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[!] Flask not found. Installing required packages..." -ForegroundColor Yellow
    Write-Host ""
    pip install flask werkzeug
    Write-Host ""
    Write-Host "[✓] Packages installed successfully" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "[✓] Flask is already installed" -ForegroundColor Green
    Write-Host ""
}

# Display connection info
Write-Host "Starting Flask server..." -ForegroundColor Cyan
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "Application URL: http://127.0.0.1:5000" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "Demo Credentials:" -ForegroundColor Cyan
Write-Host "  👤 Username: demo_user" -ForegroundColor White
Write-Host "  🔐 Password: password123" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""

# Run Flask app
python app.py
