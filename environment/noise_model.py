# =============================================================================
# 🛡️ EmergenceLab v5 — Noise Model
# File        : noise_model.py
# Author      : AHMED ZARAI
# Purpose     : Stochastic noise generator for entropy field simulation
# =============================================================================

import numpy as np


# =============================================================================
# 🔎 NoiseModel Class
# =============================================================================
class NoiseModel:
    """
    Represents additive Gaussian noise for the entropy field.

    Attributes
    ----------
    noise_level : float
        Standard deviation of the Gaussian noise.
    state_dim : int
        Dimensionality of the state vector.
    """

    # -------------------------------------------------------------------------
    # 🧰 Initialization
    # -------------------------------------------------------------------------
    def __init__(self, noise_level=0.05, state_dim=5):
        self.noise_level = noise_level
        self.state_dim = state_dim

    # -------------------------------------------------------------------------
    # 🎲 Sample Noise
    # -------------------------------------------------------------------------
    def sample(self, dim):
        """
        Generate a noise vector of specified dimension.

        Parameters
        ----------
        dim : int
            Dimension of the noise vector.

        Returns
        -------
        np.ndarray
            Gaussian noise vector scaled by `noise_level`.
        """
        return np.random.randn(dim) * self.noise_level