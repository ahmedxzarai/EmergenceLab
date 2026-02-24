# =============================================================================
# 🛡️ EmergenceLab v5 — Research-Grade Logger
# File        : logger.py
# Author      : AHMED ZARAI
# Purpose     : Structured logging for multi-agent simulation & dashboard
# =============================================================================

import logging
import os


# =============================================================================
# 🔎 Logger Setup Function
# =============================================================================
def setup_logger() -> logging.Logger:
    """
    Initializes a structured logger for EmergenceLab v5.

    Features:
    - Logs both to console and file
    - Stores logs in 'results/system.log'
    - Timestamped entries for research reproducibility
    """

    # -------------------------------------------------------------------------
    # 📂 Ensure logging directory exists
    # -------------------------------------------------------------------------
    os.makedirs("results", exist_ok=True)

    # -------------------------------------------------------------------------
    # 🧰 Create Logger Instance
    # -------------------------------------------------------------------------
    logger = logging.getLogger("EmergenceLab")
    logger.setLevel(logging.INFO)

    # -------------------------------------------------------------------------
    # 📝 Formatter for Timestamps & Log Level
    # -------------------------------------------------------------------------
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    # -------------------------------------------------------------------------
    # 📄 File Handler — Persistent Logging
    # -------------------------------------------------------------------------
    fh = logging.FileHandler("results/system.log")
    fh.setFormatter(formatter)

    # -------------------------------------------------------------------------
    # 🖥️ Console Handler — Real-Time Feedback
    # -------------------------------------------------------------------------
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # -------------------------------------------------------------------------
    # 🔗 Attach Handlers
    # -------------------------------------------------------------------------
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger