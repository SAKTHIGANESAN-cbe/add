# How to Run the Plastic Waste Management Application

## Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

## Installation Steps

### 1. Install Required Dependencies
Open PowerShell in the project directory and run:
```powershell
pip install Flask
pip install Werkzeug
```

Or install all at once:
```powershell
pip install flask werkzeug
```

### 2. Navigate to Project Directory
```powershell
cd c:\Users\sakth\OneDrive\Documents\Desktop\api
```

### 3. Run the Flask Application
```powershell
python app.py
```

You should see output like:
```
Database initialized successfully!
Sample data inserted successfully!
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 4. Access the Application
Open your browser and go to:
```
http://127.0.0.1:5000
```

### 5. Login with Demo Credentials
- **Username:** demo_user
- **Password:** password123

## Folder Structure
```
api/
├── app.py                 # Main Flask application
├── database.db           # SQLite database (auto-created)
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add.html
│   ├── view.html
│   ├── update.html
│   └── error.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Routes Available
- `/` - Home (redirects to login or dashboard)
- `/login` - Login page
- `/register` - Register new account
- `/dashboard` - Main dashboard (requires login)
- `/add` - Add new waste entry
- `/view` - View all records
- `/update/<id>` - Update a record
- `/delete/<id>` - Delete a record

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Install Flask using:
```powershell
pip install flask
```

### Error: "Database file not found"
**Solution:** The database will be created automatically when you run the app.

### Error: "Templates not found"
**Solution:** Make sure you run `python app.py` from the `api` directory where `templates/` and `static/` folders are located.

### Port 5000 already in use
**Solution:** Edit `app.py` line and change the port:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Use different port
```

## Stop the Server
Press `Ctrl + C` in the PowerShell terminal to stop the Flask server.
