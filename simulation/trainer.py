# =============================================================================
# 🛡️ EmergenceLab v5 — Multi-Agent Trainer
# File        : trainer.py
# Author      : AHMED ZARAI
# Purpose     : Generate live entropy, KL, connectivity, and beliefs for dashboard
# =============================================================================

import os
import json
import time
import numpy as np

# -----------------------------------------------------------------------------
# 📂 Results Path Configuration
# -----------------------------------------------------------------------------
RESULTS_DIR = "results"
LIVE_JSON = os.path.join(RESULTS_DIR, "live_dashboard.json")


# =============================================================================
# 🔎 Trainer Class
# =============================================================================
class Trainer:
    """
    Simulates multi-agent dynamics and generates live dashboard updates.

    Features:
    - Stepwise simulation with entropy, KL, connectivity
    - Generates agent belief vectors and KL matrix
    - Writes live JSON safely for WebSocket dashboard
    """

    # -------------------------------------------------------------------------
    # 🧰 Initialization
    # -------------------------------------------------------------------------
    def __init__(self):
        os.makedirs(RESULTS_DIR, exist_ok=True)
        self.steps = 10000  # Total simulation steps

    # -------------------------------------------------------------------------
    # 🚀 Training Loop
    # -------------------------------------------------------------------------
    def train(self):
        for step in range(self.steps):
            entropy = float(np.random.rand())
            kl = float(np.random.rand())
            connectivity = float(np.random.rand())
            beliefs = [
                {"agent": f"A{i+1}", "belief": np.random.rand(8).tolist()} 
                for i in range(5)
            ]
            kl_matrix = np.random.rand(5, 5).tolist()

            # Log simulation progress to console
            print(f"Step {step} | H={entropy:.4f} | KL={kl:.4f} | C={connectivity:.4f}")

            # Update live dashboard JSON
            self._write_dashboard(step, entropy, kl, connectivity, beliefs, kl_matrix)

            # Simulation pacing (20Hz)
            time.sleep(0.05)

    # -------------------------------------------------------------------------
    # 💾 Safe JSON Write for Live Dashboard
    # -------------------------------------------------------------------------
    def _write_dashboard(self, step, entropy, kl, connectivity, beliefs, kl_matrix):
        """
        Writes dashboard data to JSON safely for both Windows and Linux.
        """
        final_path = LIVE_JSON

        data = {
            "step": step,
            "entropy": entropy,
            "kl": kl,
            "connectivity": connectivity,
            "beliefs": beliefs,
            "kl_matrix": kl_matrix
        }

        try:
            # On Windows, 'w' mode is safer than 'os.replace' when 
            # another process (websocket.py) is watching the file.
            with open(final_path, "w") as f:
                json.dump(data, f)
        except PermissionError:
            # If the file is momentarily locked by the watcher, 
            # we just skip this one frame rather than crashing.
            pass