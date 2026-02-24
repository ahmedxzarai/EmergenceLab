# =============================================================================
# 🛡️ EmergenceLab v5 — Experiment Runner
# File        : run_experiment.py
# Author      : AHMED ZARAI
# Purpose     : Orchestrate multi-agent simulation training pipeline
# =============================================================================

from simulation.trainer import Trainer


# =============================================================================
# 🔎 Run Simulation Experiment
# =============================================================================
def run():
    """
    Initialize the Trainer and execute the simulation training loop.

    Responsibilities:
    - Stepwise simulation of entropy, KL, connectivity, beliefs
    - Generate live dashboard updates for visualization
    """
    trainer = Trainer()
    trainer.train()