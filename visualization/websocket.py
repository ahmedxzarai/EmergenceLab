# =============================================================================
# 🛡️ EmergenceLab v5 — Real-Time WebSocket Dashboard
# File        : websocket.py
# Author      : AHMED ZARAI
# Purpose     : Serve live cognitive dashboard updates via Flask-SocketIO
# =============================================================================

import os
import json
import time
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO

# -----------------------------------------------------------------------------
# 🌐 Flask Application & SocketIO Server Initialization
# -----------------------------------------------------------------------------
app = Flask(
    __name__, 
    template_folder="templates", 
    static_folder="static"
)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode='gevent'  # Change 'threading' to 'gevent'
)

# -----------------------------------------------------------------------------
# 📊 Live Dashboard JSON Path
# -----------------------------------------------------------------------------
DATA_PATH = "results/live_dashboard.json"


# =============================================================================
# 🔎 JSON Watcher — Emits Updates in Real-Time
# =============================================================================
def watch_json():
    """
    Continuously monitor 'live_dashboard.json' for changes and
    emit updates to connected WebSocket clients.
    """
    last_mtime = 0
    
    # Ensure directory exists to prevent crashes
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    
    while True:
        if os.path.exists(DATA_PATH):
            try:
                mtime = os.path.getmtime(DATA_PATH)
                if mtime > last_mtime:
                    with open(DATA_PATH, "r") as f:
                        content = f.read()
                        if content:  # Skip empty files
                            data = json.loads(content)
                            socketio.emit("update", data)
                    last_mtime = mtime

            except (json.JSONDecodeError, PermissionError):
                # File may be partially written; ignore transient errors
                pass
            except Exception as e:
                print(f"⚠️ JSON update error: {e}")
        
        # Maintain a consistent 20Hz heartbeat
        socketio.sleep(0.05)


# =============================================================================
# 🌐 Flask Routes
# =============================================================================
@app.route("/")
def index():
    """Render the main dashboard interface."""
    return render_template("index.html")


# =============================================================================
# 🧵 Start Watcher Thread Automatically
# =============================================================================
socketio.start_background_task(watch_json)