from flask import Flask, request, render_template_string
from datetime import datetime
import json
import os

app = Flask(__name__)

DATA_FILE = "users.json"
ADMIN_ID = 7761064620  # your Telegram user ID

@app.route("/")
def index():
    return "Terabox Downloader Bot is running."

@app.route("/admin")
def admin():
    user_agent = request.headers.get("User-Agent", "")
    ip = request.remote_addr
    if not os.path.exists(DATA_FILE):
        users = {}
    else:
        with open(DATA_FILE, "r") as f:
            users = json.load(f)

    total_users = len(users)
    users_list = sorted(users.items(), key=lambda x: x[1]["joined"], reverse=True)

    html = """
    <h2>Terabox Bot Dashboard</h2>
    <p>Total Users: {{total}}</p>
    <table border="1" cellpadding="5">
        <tr><th>User ID</th><th>Username</th><th>First Name</th><th>Joined</th></tr>
        {% for user_id, info in users %}
        <tr>
            <td>{{user_id}}</td>
            <td>{{info.username}}</td>
            <td>{{info.first_name}}</td>
            <td>{{info.joined}}</td>
        </tr>
        {% endfor %}
    </table>
    """
    return render_template_string(html, total=total_users, users=users_list)

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
