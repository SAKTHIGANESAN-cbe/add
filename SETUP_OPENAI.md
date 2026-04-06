# OPENAI_API_KEY Setup Instructions

## Quick Setup (3 Steps)

### Step 1: Get Your API Key
1. Go to: https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)

### Step 2: Create .env File
Create a new file called `.env` in this folder with:

```
OPENAI_API_KEY=sk-paste-your-key-here
```

### Step 3: Restart Flask
Stop the server and run again:
```
python app.py
```

---

## Troubleshooting

### Check if .env file exists:
Run in PowerShell:
```powershell
Test-Path .env
```
Should return: **True**

### Check if API key is being read:
Run in PowerShell:
```powershell
$env:OPENAI_API_KEY
```
Should show your key (or part of it)

### Check if module is installed:
```powershell
python -c "import openai; print('openai installed')"
python -c "import dotenv; print('dotenv installed')"
```
Both should print success messages

---

## Windows Environment Variable (Alternative Method)

If .env doesn't work, try:
```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
```

Or permanently (admin):
```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-your-key-here", "User")
```

Then restart PowerShell and Flask.
