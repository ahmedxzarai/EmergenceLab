# =============================================================================
# 🛡️ EmergenceLab v5 — Real-Time WebSocket Dashboard
# File         : websocket.py
# Author       : AHMED ZARAI
# Purpose      : Serve live cognitive dashboard updates via Flask-SocketIO
# =============================================================================

import os
import json
import time
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="templates", static_folder="static")

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode='gevent'
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "results", "live_dashboard.json")

def watch_json():
    """
    RESILIENT WATCHER: Synchronized with the Atomic Trainer.
    Handles the micro-second 'file rotation' without crashing.
    """
    last_mtime = 0
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    
    while True:
        try:
            if os.path.exists(DATA_PATH):
                mtime = os.path.getmtime(DATA_PATH)
                if mtime > last_mtime:
                    with open(DATA_PATH, "r") as f:
                        # json.load is direct and memory-safe
                        data = json.load(f)
                        if data:
                            socketio.emit("update", data)
                    last_mtime = mtime

        except (json.JSONDecodeError, PermissionError, FileNotFoundError):
            # These occur momentarily during os.replace(); we ignore them.
            pass
        except Exception as e:
            print(f"⚠️ JSON update error: {e}")
        
        socketio.sleep(0.05) # 20Hz refresh for smooth physics

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