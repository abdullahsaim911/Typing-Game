from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import time
import random
from datetime import datetime
import os

app = Flask(__name__)

# Sample texts for typing practice
TYPING_TEXTS = [
    "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet at least once.",
    "Python is a high-level programming language known for its simplicity and readability. It's widely used in web development, data science, and artificial intelligence.",
    "The internet is a global system of interconnected computer networks that use the standard Internet protocol suite to link devices worldwide.",
    "Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions without being explicitly programmed.",
    "Cloud computing is the delivery of computing services over the internet, including servers, storage, databases, networking, software, and analytics.",
    "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks, damage, or unauthorized access.",
    "Data science combines statistics, programming, and domain expertise to extract meaningful insights from large datasets.",
    "Blockchain is a distributed ledger technology that maintains a continuously growing list of records, called blocks, which are linked and secured using cryptography.",
    "Virtual reality creates immersive, computer-generated environments that simulate physical presence in real or imagined worlds.",
    "The future of technology lies in the convergence of artificial intelligence, internet of things, and renewable energy solutions."
]

def init_db():
    """Initialize the database with the leaderboard table"""
    conn = sqlite3.connect('typing_leaderboard.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            wpm REAL NOT NULL,
            accuracy REAL NOT NULL,
            score INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def calculate_wpm(text, time_taken):
    """Calculate words per minute"""
    words = len(text.split())
    minutes = time_taken / 60.0
    return round(words / minutes, 1) if minutes > 0 else 0

def calculate_accuracy(original_text, typed_text):
    """Calculate typing accuracy percentage"""
    if not original_text or not typed_text:
        return 0
    
    original_words = original_text.split()
    typed_words = typed_text.split()
    
    if len(original_words) == 0:
        return 100
    
    correct_words = 0
    for i, typed_word in enumerate(typed_words):
        if i < len(original_words) and typed_word == original_words[i]:
            correct_words += 1
    
    return round((correct_words / len(original_words)) * 100, 1)

def calculate_score(wpm, accuracy):
    """Calculate overall score based on WPM and accuracy"""
    return int(wpm * (accuracy / 100))

@app.route('/')
def index():
    """Main game page"""
    return render_template('index.html')

@app.route('/get_text')
def get_text():
    """Get a random typing text"""
    text = random.choice(TYPING_TEXTS)
    return jsonify({'text': text})

@app.route('/submit_score', methods=['POST'])
def submit_score():
    """Submit player score to leaderboard"""
    data = request.get_json()
    
    player_name = data.get('player_name', 'Anonymous')
    original_text = data.get('original_text', '')
    typed_text = data.get('typed_text', '')
    time_taken = data.get('time_taken', 0)
    
    # Calculate metrics
    wpm = calculate_wpm(original_text, time_taken)
    accuracy = calculate_accuracy(original_text, typed_text)
    score = calculate_score(wpm, accuracy)
    
    # Save to database
    conn = sqlite3.connect('typing_leaderboard.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leaderboard (player_name, wpm, accuracy, score)
        VALUES (?, ?, ?, ?)
    ''', (player_name, wpm, accuracy, score))
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'wpm': wpm,
        'accuracy': accuracy,
        'score': score
    })

@app.route('/leaderboard')
def leaderboard():
    """Display the leaderboard"""
    conn = sqlite3.connect('typing_leaderboard.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT player_name, wpm, accuracy, score, timestamp
        FROM leaderboard
        ORDER BY score DESC
        LIMIT 20
    ''')
    entries = cursor.fetchall()
    conn.close()
    
    return render_template('leaderboard.html', entries=entries)

@app.route('/api/leaderboard')
def api_leaderboard():
    """API endpoint for leaderboard data"""
    conn = sqlite3.connect('typing_leaderboard.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT player_name, wpm, accuracy, score, timestamp
        FROM leaderboard
        ORDER BY score DESC
        LIMIT 10
    ''')
    entries = cursor.fetchall()
    conn.close()
    
    leaderboard_data = []
    for entry in entries:
        leaderboard_data.append({
            'player_name': entry[0],
            'wpm': entry[1],
            'accuracy': entry[2],
            'score': entry[3],
            'timestamp': entry[4]
        })
    
    return jsonify(leaderboard_data)

if __name__ == '__main__':
    init_db()
    print("🚀 Starting Typing Speed Game Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🏆 Leaderboard available at: http://localhost:5000/leaderboard")
    
    # Get port from environment variable (for deployment) or use 5000
    port = int(os.environ.get('PORT', 5000))
    
    app.run(debug=False, host='0.0.0.0', port=port) 