# Plastic Waste Management System
# Flask Backend with SQLite Database
# Author: Full Stack Developer
# Date: 2024

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from datetime import datetime
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'plastic_waste_management_secret_key_2024'

# Database configuration
DATABASE = 'database.db'

# ============================================
# DATABASE FUNCTIONS
# ============================================

def get_db_connection():
    """Create a connection to the database"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn


def init_db():
    """Initialize the database with tables"""
    if os.path.exists(DATABASE):
        return
    
    conn = get_db_connection()
    c = conn.cursor()
    
    # Create users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create plastic_waste table
    c.execute('''
    CREATE TABLE IF NOT EXISTS plastic_waste (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        weight REAL NOT NULL,
        date TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")


def insert_sample_data():
    """Insert sample data for testing"""
    conn = get_db_connection()
    c = conn.cursor()
    
    try:
        # Check if data already exists
        c.execute('SELECT COUNT(*) FROM users')
        if c.fetchone()[0] > 0:
            return
        
        # Insert sample user
        hashed_password = generate_password_hash('password123')
        c.execute('''
        INSERT INTO users (username, password, email) 
        VALUES (?, ?, ?)
        ''', ('demo_user', hashed_password, 'demo@example.com'))
        
        user_id = 1
        
        # Insert sample waste records
        sample_data = [
            (user_id, 'Plastic Bags', 5.5, '2024-03-25', 'Downtown', 'Grocery bags collected'),
            (user_id, 'Bottles', 12.3, '2024-03-26', 'Park', 'Water and soda bottles'),
            (user_id, 'Containers', 8.7, '2024-03-27', 'Beach', 'Food containers from picnic'),
            (user_id, 'Plastic Bags', 3.2, '2024-03-28', 'Market', 'Shopping bags'),
            (user_id, 'Packaging', 15.8, '2024-03-29', 'Warehouse', 'Product packaging waste'),
        ]
        
        c.executemany('''
        INSERT INTO plastic_waste (user_id, type, weight, date, location, description)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_data)
        
        conn.commit()
        print("Sample data inserted successfully!")
        
    except Exception as e:
        print(f"Error inserting sample data: {e}")
    finally:
        conn.close()


# ============================================
# AUTHENTICATION DECORATORS
# ============================================

def login_required(f):
    """Decorator to check if user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# ============================================
# ROUTES
# ============================================

@app.route('/')
def home():
    """Home page - redirect to dashboard if logged in, else login"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm_password = request.form.get('confirm_password')
        
        error = None
        
        # Validation
        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif password != confirm_password:
            error = 'Passwords do not match'
        
        if error is None:
            try:
                conn = get_db_connection()
                c = conn.cursor()
                
                hashed_password = generate_password_hash(password)
                c.execute('''
                INSERT INTO users (username, password, email)
                VALUES (?, ?, ?)
                ''', (username, hashed_password, email))
                
                conn.commit()
                conn.close()
                
                return redirect(url_for('login'))
            
            except sqlite3.IntegrityError:
                error = 'Username already exists'
        
        return render_template('register.html', error=error)
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        error = None
        conn = get_db_connection()
        c = conn.cursor()
        
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if user is None:
            error = 'Username not found'
        elif not check_password_hash(user['password'], password):
            error = 'Invalid password'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        
        return render_template('login.html', error=error)
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """User logout route"""
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard - main page after login"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        user_id = session['user_id']
        
        # Get all waste records for this user
        c.execute('''
        SELECT * FROM plastic_waste 
        WHERE user_id = ? 
        ORDER BY date DESC
        ''', (user_id,))
        records = c.fetchall()
        
        # Calculate statistics
        c.execute('SELECT SUM(weight) FROM plastic_waste WHERE user_id = ?', (user_id,))
        total_weight = c.fetchone()[0] or 0
        
        c.execute('SELECT COUNT(*) FROM plastic_waste WHERE user_id = ?', (user_id,))
        total_records = c.fetchone()[0]
        
        # Get type-wise breakdown
        c.execute('''
        SELECT type, SUM(weight) as total 
        FROM plastic_waste 
        WHERE user_id = ? 
        GROUP BY type
        ''', (user_id,))
        type_breakdown = c.fetchall()
        
        conn.close()
        
        return render_template('dashboard.html', 
                             records=records,
                             total_weight=round(total_weight, 2),
                             total_records=total_records,
                             type_breakdown=type_breakdown)
    
    except Exception as e:
        print(f"Error in dashboard: {e}")
        return render_template('dashboard.html', error=str(e))


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_waste():
    """Add new plastic waste record"""
    if request.method == 'POST':
        try:
            waste_type = request.form.get('type')
            weight = request.form.get('weight')
            date = request.form.get('date')
            location = request.form.get('location')
            description = request.form.get('description', '')
            
            # Validation
            if not all([waste_type, weight, date, location]):
                return render_template('add.html', error='All fields are required')
            
            try:
                weight = float(weight)
                if weight <= 0:
                    return render_template('add.html', error='Weight must be greater than 0')
            except ValueError:
                return render_template('add.html', error='Weight must be a valid number')
            
            conn = get_db_connection()
            c = conn.cursor()
            
            c.execute('''
            INSERT INTO plastic_waste (user_id, type, weight, date, location, description)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], waste_type, weight, date, location, description))
            
            conn.commit()
            conn.close()
            
            return redirect(url_for('dashboard'))
        
        except Exception as e:
            return render_template('add.html', error=f'Error: {str(e)}')
    
    return render_template('add.html')


@app.route('/view')
@login_required
def view_waste():
    """View all waste records in table format"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        c.execute('''
        SELECT * FROM plastic_waste 
        WHERE user_id = ? 
        ORDER BY date DESC
        ''', (session['user_id'],))
        records = c.fetchall()
        conn.close()
        
        return render_template('view.html', records=records)
    
    except Exception as e:
        return render_template('view.html', error=str(e), records=[])


@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_waste(id):
    """Update a waste record"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        # Verify ownership
        c.execute('''
        SELECT * FROM plastic_waste 
        WHERE id = ? AND user_id = ?
        ''', (id, session['user_id']))
        record = c.fetchone()
        
        if record is None:
            return redirect(url_for('dashboard'))
        
        if request.method == 'POST':
            waste_type = request.form.get('type')
            weight = request.form.get('weight')
            date = request.form.get('date')
            location = request.form.get('location')
            description = request.form.get('description', '')
            
            # Validation
            if not all([waste_type, weight, date, location]):
                return render_template('update.html', record=record, error='All fields are required')
            
            try:
                weight = float(weight)
                if weight <= 0:
                    return render_template('update.html', record=record, error='Weight must be greater than 0')
            except ValueError:
                return render_template('update.html', record=record, error='Weight must be a valid number')
            
            c.execute('''
            UPDATE plastic_waste
            SET type = ?, weight = ?, date = ?, location = ?, description = ?
            WHERE id = ?
            ''', (waste_type, weight, date, location, description, id))
            
            conn.commit()
            conn.close()
            
            return redirect(url_for('dashboard'))
        
        conn.close()
        return render_template('update.html', record=record)
    
    except Exception as e:
        return render_template('update.html', error=str(e))


@app.route('/delete/<int:id>')
@login_required
def delete_waste(id):
    """Delete a waste record"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        # Verify ownership
        c.execute('''
        SELECT * FROM plastic_waste 
        WHERE id = ? AND user_id = ?
        ''', (id, session['user_id']))
        record = c.fetchone()
        
        if record is not None:
            c.execute('DELETE FROM plastic_waste WHERE id = ?', (id,))
            conn.commit()
        
        conn.close()
        return redirect(url_for('dashboard'))
    
    except Exception as e:
        print(f"Error deleting record: {e}")
        return redirect(url_for('dashboard'))


# ============================================
# API ROUTES (For Chart.js data)
# ============================================

@app.route('/api/dashboard-data')
@login_required
def api_dashboard_data():
    """API endpoint to get data for charts"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        user_id = session['user_id']
        
        # Get type-wise breakdown
        c.execute('''
        SELECT type, SUM(weight) as total 
        FROM plastic_waste 
        WHERE user_id = ? 
        GROUP BY type
        ''', (user_id,))
        type_data = c.fetchall()
        
        # Get monthly breakdown
        c.execute('''
        SELECT substr(date, 1, 7) as month, SUM(weight) as total 
        FROM plastic_waste 
        WHERE user_id = ? 
        GROUP BY substr(date, 1, 7)
        ORDER BY month DESC
        LIMIT 6
        ''', (user_id,))
        monthly_data = c.fetchall()
        
        conn.close()
        
        # Format data for charts
        type_labels = [row['type'] for row in type_data]
        type_values = [row['total'] for row in type_data]
        
        monthly_labels = [row['month'] for row in reversed(monthly_data)]
        monthly_values = [row['total'] for row in reversed(monthly_data)]
        
        return jsonify({
            'type_labels': type_labels,
            'type_values': type_values,
            'monthly_labels': monthly_labels,
            'monthly_values': monthly_values
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('error.html', error='Page not found'), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('error.html', error='Server error'), 500


# ============================================
# MAIN APPLICATION STARTUP
# ============================================

if __name__ == '__main__':
    # Initialize database
    init_db()
    insert_sample_data()
    
    # Run the application
    app.run(debug=True, host='127.0.0.1', port=5000)
