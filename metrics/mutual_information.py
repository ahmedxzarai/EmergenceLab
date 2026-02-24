# =============================================================================
# 🛡️ EmergenceLab v5 — Information Theory Utilities
# File        : mutual_information.py
# Author      : AHMED ZARAI
# Purpose     : Compute mutual information between agents and states
# =============================================================================

import numpy as np


# =============================================================================
# 🔎 Mutual Information Function
# =============================================================================
def compute_mutual_information(beliefs):
    """
    Compute mutual information I(A;S) between agents and states.

    Parameters
    ----------
    beliefs : array-like
        Agent belief distributions over states. Shape: (num_agents, num_states)

    Returns
    -------
    float
        Mutual information value.

    Notes
    -----
    - Uses base-e logarithm; adds small epsilon to prevent log(0).
    - H_s: entropy of mean belief across agents
    - H_cond: average conditional entropy per agent
    - Mutual information: I(A;S) = H_s - H_cond
    """
    beliefs = np.array(beliefs)
    mean_belief = beliefs.mean(axis=0)

    # -------------------------------------------------------------------------
    # Entropy of mean state distribution
    # -------------------------------------------------------------------------
    H_s = -np.sum(mean_belief * np.log(mean_belief + 1e-12))

    # -------------------------------------------------------------------------
    # Average conditional entropy across agents
    # -------------------------------------------------------------------------
    H_cond = 0.0
    for b in beliefs:
        H_cond += -np.sum(b * np.log(b + 1e-12))
    H_cond /= beliefs.shape[0]

    # -------------------------------------------------------------------------
    # Mutual Information: I(A;S) = H(S) - H(S|A)
    # -------------------------------------------------------------------------
    return float(H_s - H_cond)