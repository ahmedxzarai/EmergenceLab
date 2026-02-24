# =============================================================================
# 🛡️ EmergenceLab v5
# Self-Organizing Multi-Agent Intelligence
# Entropy Constraints • Stochastic Uncertainty
# -----------------------------------------------------------------------------
# File    : app.py (Production Entry Point)
# Author  : AHMED ZARAI
# Role    : System Bootstrapper (Simulation Engine + Real-Time Dashboard)
# =============================================================================


# -----------------------------------------------------------------------------
# 📦 Standard Library
# -----------------------------------------------------------------------------
import threading


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
    1. Launch background multi-agent entropy simulation
    2. Start real-time WebSocket dashboard server
    3. Ensure graceful shutdown & crash logging
    """

    logger.info("CORE: Initializing EmergenceLab v5 Research Pipeline")

    try:
        # ---------------------------------------------------------------------
        # 🧠 Phase I — Launch Simulation Engine (Background Thread)
        # ---------------------------------------------------------------------
        # Runs entropy-driven multi-agent evolution independently
        # Keeps UI responsive while cognitive field evolves
        # ---------------------------------------------------------------------
        sim_thread = threading.Thread(
            target=run,
            daemon=True
        )
        sim_thread.start()

        logger.info("CORE: Simulation Engine started in background thread")

        # ---------------------------------------------------------------------
        # 🌐 Phase II — Launch Real-Time Cognitive Dashboard
        # ---------------------------------------------------------------------
        # host="0.0.0.0" → Required for Docker / Cloud deployment
        # use_reloader=False → Prevents duplicate thread execution
        # ---------------------------------------------------------------------
        logger.info("UI: Launching Real-Time Cognitive Dashboard on port 5000")

        socketio.run(
            app,
            host="0.0.0.0",
            port=5000,
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
        logger.info("CORE: EmergenceLab v5 process terminated.")


# =============================================================================
# 🏁 Entry Guard
# =============================================================================
if __name__ == "__main__":
    main()