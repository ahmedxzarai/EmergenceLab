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
    """

    def __init__(self):
        os.makedirs(RESULTS_DIR, exist_ok=True)

    def train(self):
        step = 0
        print("🚀 Evolution Engine Started... (Infinite Loop Active)")
        
        while True:
            # Simulated research metrics
            entropy = float(np.random.rand())
            kl = float(np.random.rand())
            connectivity = float(np.random.rand())
            beliefs = [
                {"agent": f"A{i+1}", "belief": np.random.rand(8).tolist()} 
                for i in range(5)
            ]
            kl_matrix = np.random.rand(5, 5).tolist()

            # Log to Render console
            print(f"RESEARCH: Step {step} | H={entropy:.4f} | KL={kl:.4f} | C={connectivity:.4f}")

            # Update live dashboard JSON via Atomic Swap
            self._write_dashboard(step, entropy, kl, connectivity, beliefs, kl_matrix)

            step += 1
            time.sleep(1.0) # Safety delay for CPU stability

    def _write_dashboard(self, step, entropy, kl, connectivity, beliefs, kl_matrix):
        """
        ATOMIC WRITE: Writes to a temporary file then renames it instantly.
        Prevents the dashboard from ever reading an empty/corrupted file.
        """
        final_path = LIVE_JSON
        temp_path = final_path + ".tmp" 

        data = {
            "step": step,
            "entropy": entropy,
            "kl": kl,
            "connectivity": connectivity,
            "beliefs": beliefs,
            "kl_matrix": kl_matrix,
            "last_update": time.ctime() 
        }

        try:
            # 1. Write data to the temporary file first
            with open(temp_path, "w") as f:
                json.dump(data, f)
            
            # 2. Atomic Rename: This swap is instantaneous at the OS level
            # The dashboard either sees the old version or the new version.
            os.replace(temp_path, final_path)

        except (PermissionError, OSError):
            # If the file is locked by the OS, we skip this frame
            if os.path.exists(temp_path):
                try: os.remove(temp_path)
                except: pass
            pass