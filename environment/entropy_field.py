# =============================================================================
# 🛡️ EmergenceLab v5 — Entropy Field Simulation
# File        : entropy_field.py
# Author      : AHMED ZARAI
# Purpose     : Model agent-driven entropy evolution with noise
# =============================================================================

import numpy as np


# =============================================================================
# 🔎 EntropyField Class
# =============================================================================
class EntropyField:
    """
    Represents the multi-agent entropy field with discrete action updates
    and stochastic noise modeling.

    Attributes
    ----------
    state_dim : int
        Dimensionality of the state vector.
    state : np.ndarray
        Current state of the entropy field.
    """

    # -------------------------------------------------------------------------
    # 🧰 Initialization
    # -------------------------------------------------------------------------
    def __init__(self, state_dim=10):
        self.state_dim = state_dim
        self.state = np.zeros(self.state_dim)

    # -------------------------------------------------------------------------
    # ♻️ Reset Field
    # -------------------------------------------------------------------------
    def reset(self):
        """
        Reset the entropy field to zero state.
        """
        self.state = np.zeros(self.state_dim)
        return self.state.copy()

    # -------------------------------------------------------------------------
    # 🔬 Compute Reward
    # -------------------------------------------------------------------------
    def compute_reward(self):
        """
        Reward function: higher reward for lower total uncertainty (L1 norm of state)
        """
        return -float(np.sum(np.abs(self.state)))

    # -------------------------------------------------------------------------
    # 🚀 Step Function — Update Field
    # -------------------------------------------------------------------------
    def step(self, actions, noise_model):
        """
        Update the entropy field based on agent actions and stochastic noise.

        Parameters
        ----------
        actions : list
            List of discrete actions taken by agents.
        noise_model : object
            Must implement `sample(state_dim)` to produce noise vector.

        Returns
        -------
        reward : float
            Current step reward based on updated state.
        state : np.ndarray
            Updated state of the entropy field.
        """
        # Map discrete actions to state indices
        actions_array = np.zeros(self.state_dim)
        for a in actions:
            idx = int(a) % self.state_dim
            actions_array[idx] += 1.0

        # Sample noise and evolve state
        noise_vector = noise_model.sample(self.state_dim)
        self.state = self.state * 0.9 + (actions_array * 0.1) + noise_vector

        reward = self.compute_reward()
        return reward, self.state.copy()