# =============================================================================
# 🛡️ EmergenceLab v5 — Multi-Agent Trainer
# File         : trainer.py
# Author       : AHMED ZARAI
# Purpose      : Generate live entropy, KL, connectivity, and beliefs for dashboard
# =============================================================================

import os
import json
import time
import numpy as np

# -----------------------------------------------------------------------------
# 📂 Results Path Configuration
# -----------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
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
        # self.steps is now handled by the infinite loop

    # -------------------------------------------------------------------------
    # 🚀 Training Loop (Infinite for Cloud Deployment)
    # -------------------------------------------------------------------------
    def train(self):
        step = 0
        print("🚀 Evolution Engine Started... (Infinite Loop Active)")
        
        while True:  # Simulation now runs 24/7
            entropy = float(np.random.rand())
            kl = float(np.random.rand())
            connectivity = float(np.random.rand())
            beliefs = [
                {"agent": f"A{i+1}", "belief": np.random.rand(8).tolist()} 
                for i in range(5)
            ]
            kl_matrix = np.random.rand(5, 5).tolist()

            # Log simulation progress to Render console
            print(f"RESEARCH: Step {step} | H={entropy:.4f} | KL={kl:.4f} | C={connectivity:.4f}")

            # Update live dashboard JSON
            self._write_dashboard(step, entropy, kl, connectivity, beliefs, kl_matrix)

            step += 1

            # 🛡️ SAFETY DELAY: 
            # 1 second prevents CPU overload on Render Free Tier 
            # and keeps the dashboard stable.
            time.sleep(1.0)

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
            "kl_matrix": kl_matrix,
            "last_update": time.ctime() # Helpful for debugging
        }

        try:
            # Overwrites the file so it never grows too large
            with open(final_path, "w") as f:
                json.dump(data, f)
        except PermissionError:
            # If the file is momentarily locked, skip to next step
            pass