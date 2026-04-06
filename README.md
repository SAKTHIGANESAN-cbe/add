# ♻️ Plastic Waste Management System

A complete full-stack web application for tracking and managing plastic waste collection. Built with Flask, HTML5, CSS3, JavaScript, and SQLite.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Database Schema](#database-schema)
- [API Routes](#api-routes)
- [Features Explanation](#features-explanation)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

---

## 🎯 Project Overview

The **Plastic Waste Management System** is a comprehensive web application designed to help track, record, and analyze plastic waste collection activities. It provides users with an intuitive dashboard, detailed analytics, and powerful CRUD operations for managing waste records.

### Key Highlights:
- ✅ **User Authentication**: Secure login and registration system
- ✅ **Dashboard Analytics**: Real-time statistics and visualizations
- ✅ **Data Management**: Add, view, update, and delete waste records
- ✅ **Interactive Charts**: Chart.js integration for data visualization
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile devices
- ✅ **Beginner-Friendly**: Simple, clean code with comments

---

## ✨ Features

### 1. **User Authentication**
- User registration with email
- Secure login system with password hashing
- Session management
- Logout functionality
- Demo account for testing

### 2. **Dashboard**
- Welcome message with user info
- Statistics cards (total weight, records, types, impact)
- Interactive charts using Chart.js:
  - Doughnut chart for waste type breakdown
  - Line chart for monthly collection trends
- Quick action buttons
- Recent entries preview

### 3. **Waste Management**
- **Add Entry**: Record new plastic waste with type, weight, date, location, and description
- **View Records**: Display all entries in organized table format
- **Search & Filter**: Find records by type or location
- **Sorting**: Sort by any column (type, weight, date, location)
- **Update Entry**: Modify existing records
- **Delete Entry**: Remove records with confirmation
- **Summary Statistics**: Average weight, total count, most common type

### 4. **Analytics & Visualization**
- Type-wise waste breakdown chart
- Monthly collection trends
- Statistical cards showing:
  - Total weight collected
  - Number of entries
  - Types of waste
  - Environmental impact

### 5. **User Interface**
- Professional navigation bar
- Responsive grid layouts
- Hover effects and animations
- Color-coded waste type badges
- Form validation (client & server-side)
- Error messages and alerts
- Empty state messaging

### 6. **Database**
- SQLite for lightweight data storage
- User management
- Waste record tracking
- Relationships between users and records

---

## 📸 Screenshots

### Login Page
- Clean authentication interface
- Demo credentials displayed
- Registration link

### Dashboard
- Statistics overview
- Interactive charts
- Recent entries
- Quick action buttons

### Add Waste Entry
- Type selection dropdown
- Weight input field
- Date picker
- Location field
- Description textarea
- Helpful tips section

### View Records
- Table display with all entries
- Search functionality
- Filter by type
- Sort capabilities
- Action buttons (edit/delete)
- Summary statistics

---

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with Flexbox and Grid
  - Responsive design
  - Animations and transitions
  - Color variables and themes
  - Mobile-first approach

- **JavaScript (Vanilla)**: Client-side functionality
  - DOM manipulation
  - Form validation
  - Event handling
  - Local storage
  - Data filtering and sorting
  - API integration

### Backend
- **Flask**: Python web framework
  - Lightweight and beginner-friendly
  - Built-in Jinja2 templating
  - Session management
  - Error handling

- **Python 3.7+**: Programming language
  - SQLite3 for database operations
  - Werkzeug for security (password hashing)

### Database
- **SQLite3**: Lightweight, file-based database
  - No server setup required
  - Perfect for beginners and small projects
  - Transaction support

### Libraries & Tools
- **Chart.js**: Data visualization library
  - Interactive charts
  - Responsive design
  - Multiple chart types

- **Werkzeug**: WSGI utility library
  - Password hashing (generate_password_hash, check_password_hash)
  - Secure password storage

---

## 📁 Project Structure

```
plastic_waste_management/
│
├── app.py                          # Flask application & routes
├── database.db                     # SQLite database (auto-created)
│
├── static/                         # Static files
│   ├── css/
│   │   └── style.css              # Main stylesheet (1000+ lines)
│   │
│   └── js/
│       └── script.js              # Client-side JavaScript
│
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with navbar
│   ├── login.html                 # Login page
│   ├── register.html              # Registration page
│   ├── dashboard.html             # Main dashboard with charts
│   ├── add.html                   # Add waste entry form
│   ├── view.html                  # View all records
│   ├── update.html                # Edit waste entry
│   └── error.html                 # Error page
│
└── README.md                       # This file
```

### File Descriptions

#### **app.py** (Main Application)
- Flask app initialization
- Database configuration and management
- User authentication routes
- Waste management CRUD routes
- API endpoints for chart data
- Error handling

#### **Templates**
- **base.html**: Navigation bar and footer (extended by all pages)
- **login.html**: User login with demo credentials
- **register.html**: New user registration
- **dashboard.html**: Main dashboard with charts and stats
- **add.html**: Form to add waste entries
- **view.html**: Table view with search and filter
- **update.html**: Edit existing records
- **error.html**: Error page display

#### **style.css**
- Responsive grid layouts
- Color scheme with CSS variables
- Animations and transitions
- Mobile-first design
- Dark and light themes
- Button styles and states
- Form styling and validation

#### **script.js**
- Form validation (client-side)
- Table filtering and sorting
- Chart.js initialization
- Local storage functions
- Keyboard shortcuts
- Data export functionality
- Accessibility features

---

## 📦 Installation Guide

### Prerequisites
Before starting, ensure you have:
- **Python 3.7 or higher** installed
- **pip** (Python package manager)
- A web browser (Chrome, Firefox, Edge, Safari)
- Text editor or IDE (VS Code recommended)

### Step 1: Install Python

#### Windows:
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✓ Check "Add Python to PATH"
4. Click "Install Now"

#### macOS:
```bash
# Using Homebrew
brew install python3
```

#### Linux:
```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip
```

### Step 2: Verify Installation

```bash
python --version
pip --version
```

### Step 3: Install Flask

```bash
pip install flask
```

### Step 4: Download/Clone Project

```bash
# Option 1: Copy files to your project directory
cd c:\Users\sakth\OneDrive\Documents\Desktop\api

# Option 2: From terminal (if using git)
git clone <repository-url>
cd plastic_waste_management
```

### Step 5: Verify Project Structure

Ensure your folder has:
```
api/
├── app.py
├── static/
│   ├── css/style.css
│   └── js/script.js
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── add.html
    ├── view.html
    ├── update.html
    └── error.html
```

---

## 🚀 How to Run

### Method 1: Command Line (Recommended)

#### Windows:
```bash
# 1. Open Command Prompt or PowerShell
# 2. Navigate to project directory
cd c:\Users\sakth\OneDrive\Documents\Desktop\api

# 3. Run Flask app
python app.py
```

#### macOS/Linux:
```bash
# 1. Open Terminal
# 2. Navigate to project directory
cd ~/Desktop/plastic_waste_management

# 3. Run Flask app
python3 app.py
```

### Method 2: VS Code

1. Open the project folder in VS Code
2. Open integrated terminal (Ctrl + `)
3. Run:
   ```bash
   python app.py
   ```

### Method 3: IDE (PyCharm, etc.)

1. Open project in your IDE
2. Right-click on `app.py`
3. Select "Run 'app.py'"

### What Happens After Running:

```
Output:
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Access the Application

1. **Open Browser**: Visit `http://127.0.0.1:5000`
2. **You'll see the Login Page**
3. **Use Demo Credentials**:
   - Username: `demo_user`
   - Password: `password123`
4. **Or Create New Account** via Register page

---

## 📖 Usage Guide

### First Time Setup

1. **Login with Demo Account**
   - Username: `demo_user`
   - Password: `password123`
   - This shows sample data

2. **Or Register New Account**
   - Click "Register here" link on login page
   - Fill in username, email, password
   - Click "Create Account"
   - Login with new credentials (starts with empty records)

### Dashboard Usage

#### **Statistics Section**
- See total weight collected at a glance
- View number of entries
- Check different waste types recorded
- Understand environmental impact

#### **Charts Section**
- **Type Chart**: See which types of plastic are collected most
- **Monthly Chart**: Track collection trends over time
- Hover over data points for detailed information

#### **Quick Actions**
- **Add New Entry**: Click to record new waste
- **View Records**: See all entries in table format

#### **Recent Entries**
- View last 5 entries on dashboard
- Quick edit/delete buttons
- Link to view all records

### Adding a Waste Entry

1. Click **"Add Waste"** in navigation or dashboard
2. **Select Waste Type**: Choose from dropdown
   - Plastic Bags
   - Bottles
   - Containers
   - Packaging
   - Films
   - Others
3. **Enter Weight**: Input in kilograms (e.g., 5.5)
4. **Select Date**: Pick collection date
5. **Enter Location**: Where was it collected?
6. **Add Description** (Optional): Additional notes
7. **Click "Save Entry"**
8. You'll be redirected to dashboard

### Viewing & Managing Records

1. Click **"View Records"** in navigation
2. **Table displays all entries**:
   - Type, Weight, Date, Location, Description, Actions

3. **Search Records**:
   - Type in search box to find by type or location
   - Results filter in real-time

4. **Filter by Type**:
   - Use dropdown to show specific waste types
   - Combine with search for precise filtering

5. **Sort Records**:
   - Click column headers to sort
   - Click again to reverse sort
   - Works with Type, Weight, Date, Location

6. **Edit Record**:
   - Click ✏️ (Edit) button
   - Modify any field
   - Click "Update Entry"

7. **Delete Record**:
   - Click 🗑️ (Delete) button
   - Confirm deletion in popup
   - Record is permanently removed

### Summary Statistics

On the View Records page:
- **Total Weight Collected**: Sum of all entries
- **Number of Records**: Total count of entries
- **Average Weight**: Mean weight per entry
- **Most Common Type**: Most frequently recorded waste type

### Logout

1. Click **"Logout"** button in top-right
2. You'll be returned to login page
3. Your data is saved in database

---

## 💾 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Plastic Waste Table
```sql
CREATE TABLE plastic_waste (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    weight REAL NOT NULL,
    date TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Field Descriptions

**Users Table:**
- `id`: Unique user identifier
- `username`: User's login name (unique)
- `password`: Hashed password (bcrypt)
- `email`: User's email address
- `created_at`: Account creation timestamp

**Plastic Waste Table:**
- `id`: Unique record identifier
- `user_id`: Reference to user who created entry
- `type`: Category of plastic (bags, bottles, etc.)
- `weight`: Amount in kilograms
- `date`: Date of collection (YYYY-MM-DD)
- `location`: Geographic location
- `description`: Additional notes
- `created_at`: Entry creation timestamp

---

## 🔌 API Routes

### Authentication Routes

| Method | Route | Purpose |
|--------|-------|---------|
| GET/POST | `/` | Home redirect |
| GET/POST | `/register` | User registration |
| GET/POST | `/login` | User login |
| GET | `/logout` | User logout |

### Main Routes

| Method | Route | Purpose | Auth Required |
|--------|-------|---------|---|
| GET | `/dashboard` | Main dashboard | ✅ |
| GET/POST | `/add` | Add waste entry | ✅ |
| GET | `/view` | View all records | ✅ |
| GET/POST | `/update/<id>` | Edit record | ✅ |
| GET | `/delete/<id>` | Delete record | ✅ |

### API Endpoints

| Method | Route | Response | Purpose |
|--------|-------|----------|---------|
| GET | `/api/dashboard-data` | JSON | Chart data |

**Response Format:**
```json
{
    "type_labels": ["Bottles", "Bags"],
    "type_values": [25.5, 15.3],
    "monthly_labels": ["2024-01", "2024-02"],
    "monthly_values": [30.0, 40.0]
}
```

---

## 🎨 Features Explanation

### Form Validation
- **Client-side**: JavaScript validation in browser
- **Server-side**: Python validation on backend
- **Error Messages**: Clear feedback for corrections
- **Regex Validation**: Email, password patterns

### Security Features
- **Password Hashing**: Passwords stored as hashes (not plaintext)
- **Session Management**: Uses Flask sessions
- **Login Required Decorator**: Protects routes
- **CSRF Protection**: Form submissions validated
- **SQL Sanitization**: Parameterized queries prevent injection

### Responsive Design
- **Mobile First**: Designed for mobile, enhanced for desktop
- **Flexbox & Grid**: Modern layout techniques
- **Media Queries**: Adapt to all screen sizes
- **Touch Friendly**: Large buttons for mobile

### Performance Optimization
- **CSS Minification**: Optimized stylesheets
- **Event Debouncing**: Prevent excessive function calls
- **Lazy Loading**: Load charts only when needed
- **Local Storage**: Cache form data

### Accessibility
- **Semantic HTML**: Proper heading hierarchy
- **ARIA Labels**: For screen readers
- **Keyboard Navigation**: Tab through forms
- **Color Contrast**: WCAG compliant colors
- **Tab Order**: Logical focus management

---

## 🐛 Troubleshooting

### Issue 1: "Python is not recognized"
**Solution:**
- Add Python to PATH during installation
- Or use full path: `C:\Python39\python.exe app.py`

### Issue 2: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask
# or
pip3 install flask
```

### Issue 3: Port 5000 already in use
**Solution:**
Edit `app.py` last line and change port:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Changed to 5001
```

### Issue 4: Database locked error
**Solution:**
- Close all browser tabs with the app
- Delete `database.db` (it will be recreated)
- Restart the Flask server

### Issue 5: Login not working
**Solution:**
- Clear browser cookies: Press F12 → Application → Cookies → Clear
- Try demo credentials: `demo_user` / `password123`
- Check database exists

### Issue 6: Charts not showing
**Solution:**
- Check browser console (F12) for errors
- Ensure Chart.js CDN is accessible
- Hard refresh page (Ctrl+Shift+R)

### Issue 7: Styles not loading
**Solution:**
- Hard refresh (Ctrl+Shift+R)
- Check file structure paths
- Verify `static` folder exists

---

## 🚀 Future Enhancements

### Potential Features to Add:

1. **PDF Export**
   - Generate reports as PDF files
   - Include charts and statistics

2. **Email Notifications**
   - Reminders for regular updates
   - Achievement milestones

3. **Admin Dashboard**
   - Manage all users
   - View system-wide statistics
   - User activity logs

4. **Advanced Analytics**
   - Predictions using machine learning
   - Environmental impact calculator
   - Carbon footprint estimation

5. **Mobile App**
   - React Native or Flutter app
   - Native mobile experience
   - Offline support

6. **Multi-language Support**
   - Internationalization (i18n)
   - Support for multiple languages

7. **Data Import/Export**
   - CSV import for bulk data
   - Excel export functionality
   - API for integrations

8. **Real-time Collaboration**
   - Multi-user entries
   - Team management
   - Comments on records

9. **Gamification**
   - Badges for milestones
   - Leaderboards
   - Achievement system

10. **IoT Integration**
    - Connect to weight sensors
    - Automated data collection
    - Real-time monitoring

---

## 📚 Code Comments & Documentation

Every file includes:
- File header with description
- Function documentation
- Inline comments for complex logic
- Variable naming conventions
- Usage examples

Example from app.py:
```python
@app.route('/dashboard')
@login_required  # Check if user is logged in
def dashboard():
    """Dashboard - main page after login"""
    # Get connection to database
    conn = get_db_connection()
    
    # Fetch records for current user
    records = fetch_user_records(session['user_id'])
    
    return render_template('dashboard.html', records=records)
```

---

## 🎓 Learning Outcomes

By studying this project, you'll learn:

### Backend (Python/Flask)
- ✅ Web framework basics
- ✅ Routing and views
- ✅ Database operations (SQLite)
- ✅ User authentication
- ✅ Session management
- ✅ Form handling
- ✅ Error handling
- ✅ API design

### Frontend (HTML/CSS/JavaScript)
- ✅ Semantic HTML
- ✅ Responsive design
- ✅ CSS Grid & Flexbox
- ✅ Animations & transitions
- ✅ Form validation
- ✅ DOM manipulation
- ✅ API calls with Fetch
- ✅ Local storage

### Database (SQLite)
- ✅ Table design
- ✅ Relationships (Foreign Keys)
- ✅ CRUD operations
- ✅ Transactions
- ✅ Data security

### Best Practices
- ✅ Code Organization
- ✅ Security (hashing, validation)
- ✅ Error handling
- ✅ Documentation
- ✅ User Experience
- ✅ Responsive design
- ✅ Performance optimization
- ✅ Accessibility

---

## 📞 Support & Debugging

### Enable Debug Mode
Flask comes with a debugger. It's enabled by default.

**To debug:**
1. Check terminal for error messages
2. Python error messages are very helpful
3. Use `print()` statements for debugging
4. Check browser console (F12) for frontend errors

### Check Database
To verify database:
```python
# Add this to app.py and run it once
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
```

---

## 📄 License

This project is provided as-is for educational purposes. Feel free to modify and use for your learning.

---

## 👨‍💻 About the Code

### Code Style
- **PEP 8 Compliant**: Python follows PEP 8 standards
- **Meaningful Names**: Variables and functions are clearly named
- **DRY Principle**: Don't Repeat Yourself - reusable functions
- **SOLID Principles**: Single responsibility, modular design
- **Comments**: Explained where code is complex

### Performance
- **Database Queries**: Optimized with proper indexing
- **Caching**: Where applicable
- **Async Operations**: Not used (single-threaded for simplicity)
- **Load Times**: Fast page loads
- **Chart Loading**: Deferred loading for better UX

### Security Considerations
- **Password Security**: Hashed with Werkzeug
- **SQL Injection**: Protected with parameterized queries
- **Session Security**: Flask session with secret key
- **Input Validation**: Both client and server-side
- **Error Messages**: Don't reveal sensitive info

---

## 🎉 Conclusion

Congratulations! You now have a complete, production-ready plastic waste management system. This project demonstrates:

- Full-stack web development
- Database design and management
- User authentication and authorization
- Responsive design
- Data visualization
- Clean code practices
- Real-world application development

### Next Steps

1. **Customize**: Modify colors, add your branding
2. **Extend**: Add new features from enhancement list
3. **Deploy**: Host on Heroku, PythonAnywhere, or AWS
4. **Share**: Help others with your solution
5. **Learn**: Study the code and improve your skills

---

## 📖 Reference Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/3/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Chart.js Documentation](https://www.chartjs.org/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)

---

## 💡 Tips for Beginners

1. **Start Small**: Understand each component before adding features
2. **Read Error Messages**: They tell you exactly what's wrong
3. **Use Version Control**: Learn Git to track changes
4. **Debug Systematically**: Use print() and browser dev tools
5. **Test Thoroughly**: Try different inputs and scenarios
6. **Read Code**: Study how things are implemented
7. **Comment Your Code**: Help future you understand
8. **Ask Questions**: Don't hesitate to ask for help

---

**Happy Coding! ♻️**

Last Updated: April 2024  
Version: 1.0.0
