import sqlite3

conn = sqlite3.connect('datt.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Create history table

cursor.execute('''
               CREATE TABLE if not exists history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    message TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp TEXT NOT NULL);
''')


conn.commit()
conn.close()
print("Database initialized successfully.")
