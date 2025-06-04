from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Terabox Bot Admin Panel</h1><p>Visit /admin for stats.</p>"

@app.route("/admin")
def admin():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    return f"<h2>Total Users: {count}</h2>"
