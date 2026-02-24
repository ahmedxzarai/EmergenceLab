# =============================================================================
# 🛡️ EmergenceLab v5 — Entropy Utilities
# File        : entropy.py
# Author      : AHMED ZARAI
# Purpose     : Shannon entropy calculation for discrete and continuous data
# =============================================================================

import numpy as np


# =============================================================================
# 🔎 Shannon Entropy Function
# =============================================================================
def shannon_entropy(data):
    """
    Compute Shannon entropy for discrete actions or continuous state vectors.

    Parameters
    ----------
    data : list or np.ndarray
        Input data representing either discrete categories or continuous values.

    Returns
    -------
    float
        Shannon entropy value.
    
    Notes
    -----
    - Continuous data are normalized to a probability distribution.
    - Discrete data frequencies are used for probability estimation.
    - Small epsilon (1e-9) prevents log2(0) issues.
    """
    arr = np.array(data)

    # -------------------------------------------------------------------------
    # Continuous data: normalize absolute values to probability distribution
    # -------------------------------------------------------------------------
    if arr.dtype == float or np.issubdtype(arr.dtype, np.floating):
        p = np.abs(arr) / (np.sum(np.abs(arr)) + 1e-9)
    
    # -------------------------------------------------------------------------
    # Discrete data: frequency-based probability
    # -------------------------------------------------------------------------
    else:
        _, counts = np.unique(arr, return_counts=True)
        p = counts / counts.sum()

    # -------------------------------------------------------------------------
    # Shannon formula: H = -sum(p * log2(p))
    # -------------------------------------------------------------------------
    return -np.sum(p * np.log2(p + 1e-9))