# =============================================================================
# 🛡️ EmergenceLab v5 — Divergence Utilities
# File        : Kl_divergence.py
# Author      : AHMED ZARAI
# Purpose     : Compute Kullback-Leibler divergence between two distributions
# =============================================================================

import numpy as np


# =============================================================================
# 🔎 KL Divergence Function
# =============================================================================
def kl_divergence(p: np.ndarray, q: np.ndarray) -> float:
    """
    Compute the Kullback-Leibler (KL) divergence D_KL(p || q) between two distributions.

    Parameters
    ----------
    p : np.ndarray
        Probability distribution array (source).
    q : np.ndarray
        Probability distribution array (target).

    Returns
    -------
    float
        KL divergence value.

    Notes
    -----
    - Inputs are clipped to avoid division by zero or log(0).
    - Returns a scalar float suitable for logging or analysis.
    """
    # -------------------------------------------------------------------------
    # Clip probabilities to valid range
    # -------------------------------------------------------------------------
    p = np.clip(p, 1e-12, 1)
    q = np.clip(q, 1e-12, 1)

    # -------------------------------------------------------------------------
    # KL Divergence Formula
    # -------------------------------------------------------------------------
    return float(np.sum(p * np.log(p / q)))