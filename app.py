# Plastic Waste Management System
# Flask Backend with SQLite Database
# Author: Full Stack Developer
# Date: 2024

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import sqlite3
import os
from datetime import datetime
from functools import wraps
import base64
import json

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Note: python-dotenv not installed. Set OPENAI_API_KEY environment variable manually.")

# AI/ML Imports
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'plastic_waste_management_secret_key_2024'

# Database configuration
DATABASE = 'database.db'

# File upload configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# OpenAI Configuration
if OPENAI_AVAILABLE:
    openai.api_key = os.getenv('OPENAI_API_KEY', '')
    
# ============================================
# AI HELPER FUNCTIONS
# ============================================

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def classify_plastic_image(image_path):
    """Use OpenAI Vision to classify plastic waste from image"""
    if not OPENAI_AVAILABLE or not openai.api_key:
        return None
    
    try:
        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode()
        
        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this image of plastic waste. Identify the type of plastic waste (e.g., Plastic Bags, Bottles, Containers, Packaging, Films, etc.) and estimate the weight in kg. Return ONLY a JSON object like: {\"type\": \"...\", \"weight\": 0.0, \"confidence\": 0.95}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_data}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=200
        )
        
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(f"Error classifying image: {e}")
        return None

def calculate_eco_impact(total_weight):
    """Calculate environmental impact metrics"""
    impact = {
        'plastic_saved_kg': round(total_weight, 2),
        'co2_prevented_kg': round(total_weight * 0.85, 2),  # 850g CO2 per kg plastic
        'landfill_years_delayed': round(total_weight * 0.01, 2),  # 1kg = 0.01 years
        'water_saved_liters': round(total_weight * 2.5, 2),  # 2.5L water per kg
        'trees_preserved': round(total_weight * 0.1, 2),  # Estimate 0.1 trees per kg
        'oil_saved_liters': round(total_weight * 1.5, 2)  # 1.5L oil per kg
    }
    return impact

def get_ai_recommendations(total_weight, type_breakdown):
    """Get personalized AI recommendations based on collection patterns"""
    if not OPENAI_AVAILABLE or not openai.api_key:
        return {
            "recommendations": [
                "📌 Keep tracking your plastic waste collection regularly",
                "♻️ Consider sharing your environmental efforts with friends",
                "🎯 Set a monthly goal for plastic waste reduction"
            ]
        }
    
    try:
        # Create a summary of the user's collection pattern
        types_summary = ", ".join([f"{t['type']}: {t['total']}kg" for t in type_breakdown])
        
        prompt = f"""Based on a user's plastic waste collection data:
        - Total weight collected: {total_weight}kg
        - Types collected: {types_summary}
        
        Provide 3-4 specific, actionable recommendations to help them reduce plastic waste and improve their collection habits. Format as a JSON object with a "recommendations" array of strings. Keep each recommendation under 100 characters."""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an environmental expert providing waste management recommendations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        
        result_text = response.choices[0].message.content
        # Try to parse as JSON
        try:
            return json.loads(result_text)
        except:
            # If not valid JSON, return as recommendations text
            return {"recommendations": result_text.split('\n')}
    
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return {
            "recommendations": [
                "🌱 Continue your plastic waste collection efforts",
                "💡 Track which plastic types you collect most",
                "🌍 Share your impact with the community"
            ]
        }

def chat_with_ai(user_message, conversation_history=[]):
    """AI Chatbot for waste management questions"""
    if not OPENAI_AVAILABLE or not openai.api_key:
        return "Chatbot feature requires OpenAI API configuration. Please set your OPENAI_API_KEY environment variable."
    
    try:
        messages = [
            {"role": "system", "content": """You are a helpful AI assistant for a Plastic Waste Management System. 
            You provide advice on:
            - How to properly recycle and dispose of plastic waste
            - Environmental impact of plastic waste
            - Tips for reducing plastic consumption
            - Best practices for waste collection
            Keep responses concise and practical. Always encourage environmental responsibility."""}
        ]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error in chatbot: {e}")
        return f"Sorry, I encountered an error: {str(e)}"

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
        
        # Calculate eco-impact
        eco_impact = calculate_eco_impact(total_weight)
        
        # Get AI recommendations
        ai_recommendations = get_ai_recommendations(total_weight, type_breakdown)
        
        return render_template('dashboard.html', 
                             records=records,
                             total_weight=round(total_weight, 2),
                             total_records=total_records,
                             type_breakdown=type_breakdown,
                             eco_impact=eco_impact,
                             ai_recommendations=ai_recommendations)
    
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


# ============================================
# AI FEATURE ROUTES
# ============================================

@app.route('/api/classify-image', methods=['POST'])
@login_required
def classify_image():
    """API endpoint to classify plastic waste from image using AI"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed: png, jpg, jpeg, gif'}), 400
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Classify using AI
        classification = classify_plastic_image(filepath)
        
        # Clean up
        if os.path.exists(filepath):
            os.remove(filepath)
        
        if classification:
            return jsonify({
                'success': True,
                'type': classification.get('type', 'Unknown'),
                'weight': classification.get('weight', 0),
                'confidence': classification.get('confidence', 0)
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Could not classify image. Please check your OpenAI API key.',
                'note': 'Ensure OPENAI_API_KEY environment variable is set'
            }), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/eco-impact', methods=['GET'])
@login_required
def get_eco_impact():
    """API endpoint to get eco-impact data"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        c.execute('SELECT SUM(weight) FROM plastic_waste WHERE user_id = ?', (session['user_id'],))
        total_weight = c.fetchone()[0] or 0
        
        c.execute('''
        SELECT type, SUM(weight) as total 
        FROM plastic_waste 
        WHERE user_id = ? 
        GROUP BY type
        ''', (session['user_id'],))
        type_breakdown = c.fetchall()
        
        conn.close()
        
        impact = calculate_eco_impact(total_weight)
        recommendations = get_ai_recommendations(total_weight, type_breakdown)
        
        return jsonify({
            'impact': impact,
            'recommendations': recommendations.get('recommendations', [])
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat', methods=['POST'])
@login_required
def chatbot():
    """API endpoint for AI chatbot"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Get conversation history if session storage is used
        conversation_history = session.get('chat_history', [])
        
        # Get AI response
        response = chat_with_ai(user_message, conversation_history)
        
        # Update conversation history
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": response})
        
        # Keep only last 10 messages in history
        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]
        
        session['chat_history'] = conversation_history
        
        return jsonify({
            'success': True,
            'message': response
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
