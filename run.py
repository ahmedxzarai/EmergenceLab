

# =============================================================================
# 🛡️ EmergenceLab v5
# Self-Organizing Multi-Agent Intelligence
# Entropy Constraints • Stochastic Uncertainty
# -----------------------------------------------------------------------------
# File    : run.py (Production Entry Point)
# Author  : AHMED ZARAI
# Role    : System Bootstrapper (Multiprocessing Engine + Real-Time Dashboard)
# =============================================================================

# -----------------------------------------------------------------------------
# 📦 Standard Library
# -----------------------------------------------------------------------------
import multiprocessing
import os

# -----------------------------------------------------------------------------
# 🧠 Core Experiment Engine
# -----------------------------------------------------------------------------
from experiments.run_experiment import run

# -----------------------------------------------------------------------------
# 🌐 Real-Time Visualization Layer (Flask-SocketIO)
# -----------------------------------------------------------------------------
from visualization.websocket import socketio, app

# -----------------------------------------------------------------------------
# 📊 Observability Layer (Structured Research Logger)
# -----------------------------------------------------------------------------
from utils.logger import setup_logger

# =============================================================================
# 🔎 Initialize Research-Grade Logger
# =============================================================================
logger = setup_logger()

# =============================================================================
# 🚀 Main System Orchestration
# =============================================================================
def main():
    """
    EmergenceLab v5 — Production Execution Pipeline

    Responsibilities:
    1. Launch background multi-agent entropy simulation (Isolated Process)
    2. Start real-time WebSocket dashboard server (Main Process)
    3. Ensure graceful shutdown & crash logging across both layers
    """

    logger.info("CORE: Initializing EmergenceLab v5 Research Pipeline")

    try:
        # ---------------------------------------------------------------------
        # 🧠 Phase I — Launch Simulation Engine (Isolated Process)
        # ---------------------------------------------------------------------
        # Using Multiprocessing ensures the simulation and the web server
        # don't fight for the same CPU thread, preventing dashboard lag.
        # ---------------------------------------------------------------------
        sim_process = multiprocessing.Process(
            target=run,
            daemon=True
        )
        sim_process.start()

        logger.info(f"CORE: Simulation Engine started in isolated process (PID: {sim_process.pid})")

        # ---------------------------------------------------------------------
        # 🌐 Phase II — Launch Real-Time Cognitive Dashboard
        # ---------------------------------------------------------------------
        # host="0.0.0.0" → Required for Render / Docker cloud deployment
        # port=10000     → Standard Render port (or keep 5000)
        # ---------------------------------------------------------------------
        logger.info("UI: Launching Real-Time Cognitive Dashboard on Cloud Interface")

        socketio.run(
            app,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)), # Flex for Render's dynamic port
            use_reloader=False,
            log_output=False,
            allow_unsafe_werkzeug=True
        )

    except KeyboardInterrupt:
        logger.warning(
            "CORE: Manual interruption detected. Initiating graceful shutdown..."
        )

    except Exception as e:
        logger.error(f"FATAL: System crash detected: {e}")

    finally:
        # Cleanup: Ensure the simulation process dies when the web server does
        if 'sim_process' in locals() and sim_process.is_alive():
            sim_process.terminate()
            logger.info("CORE: Simulation process cleaned up.")
        
        logger.info("CORE: EmergenceLab v5 process terminated.")

# =============================================================================
# 🏁 Entry Guard
# =============================================================================
if __name__ == "__main__":
    main()
