from flask import Flask, render_template, request, redirect, session, url_for, jsonify, send_file
import sqlite3
import os
import csv
from datetime import datetime
from pexels import get_place_images
from ai import get_groq_response
import init_db

app = Flask(__name__)
app.secret_key = '' #create your own key

DATABASE = 'datt.db'

# Helper to connect DB
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect('/chat')
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        existing_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if existing_user:
            error = 'Username already taken'
        else:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect('/login')
        conn.close()
    return render_template('register.html', error=error)



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect('/login')
    return render_template('chat.html', username=session['username'])

@app.route('/ask', methods=['POST'])
def ask():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    message = request.json.get('message')
    username = session['username']

    full_prompt = f"""User prompt - {{{message}}}
Act as a place suggestion chatbot. Give top 5 places for the category. For each place, follow this format:
1. Place Name - One-line description. Wikipedia link (if available). Entry fee info.
This will help in extracting both name and description easily.
If user prompt defines a trip for more than a day, suggest hotels near the suggested places."""

    ai_response = get_groq_response(full_prompt)

    # Save full chat
    conn = get_db_connection()
    conn.execute('INSERT INTO history (username, message, response, timestamp) VALUES (?, ?, ?, ?)',
                 (username, message, ai_response, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

    # Parse top 5 places with name + description
    places = []
    for line in ai_response.split("\n"):
        if line.strip().startswith(("1.", "2.", "3.", "4.", "5.")):
            try:
                split_line = line.split(".", 1)[1].strip()
                name, desc = split_line.split("-", 1)
                name = name.strip()
                desc = desc.strip()
                images = get_place_images(name)
                places.append({'name': name, 'description': desc, 'images': images})
            except Exception as e:
                continue  # Skip malformed lines

    return jsonify({'ai_response': ai_response, 'places': places})

@app.route('/history')
def history():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    conn = get_db_connection()
    rows = conn.execute('SELECT message AS user_message, response AS ai_response FROM history WHERE username = ? ORDER BY timestamp DESC', (username,)).fetchall()
    conn.close()

    return render_template('history.html', username=username, history=rows)


@app.route('/export_history')
def export_history():
    if 'username' not in session:
        return redirect('/login')

    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM history WHERE username = ?', (session['username'],)).fetchall()
    conn.close()

    csv_path = f"{session['username']}_history.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username', 'Message', 'Response', 'Timestamp'])
        for row in rows:
            writer.writerow([row['username'], row['message'], row['response'], row['timestamp']])

    return send_file(csv_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)


