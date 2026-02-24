# =============================================================================
# 🛡️ EmergenceLab v5 — Configuration Loader
# File        : loader.py
# Author      : AHMED ZARAI
# Purpose     : Load YAML experiment/stress-test configuration into structured dataclasses
# =============================================================================

import yaml
from dataclasses import dataclass
from typing import Any, Dict


# =============================================================================
# 🔎 Configuration Dataclasses
# =============================================================================
@dataclass
class EnvironmentConfig:
    """
    Configuration for the world environment.
    """
    state_dim: int
    steps: int
    noise_level: float
    seed: int


@dataclass
class AgentConfig:
    """
    Configuration for multi-agent system parameters.
    """
    num_agents: int
    coupling_alpha: float


@dataclass
class TrainingConfig:
    """
    Configuration for training/simulation parameters.
    """
    step_delay: float


@dataclass
class AppConfig:
    """
    Top-level configuration aggregating environment, agents, and training.
    """
    environment: EnvironmentConfig
    agents: AgentConfig
    training: TrainingConfig


# =============================================================================
# 🔧 Load YAML Config
# =============================================================================
def load_config(path: str) -> AppConfig:
    """
    Load a YAML configuration file and return an AppConfig dataclass.

    Parameters
    ----------
    path : str
        Path to the YAML configuration file.

    Returns
    -------
    AppConfig
        Structured configuration for environment, agents, and training.
    """
    with open(path, "r") as f:
        raw: Dict[str, Any] = yaml.safe_load(f)

    return AppConfig(
        environment=EnvironmentConfig(**raw["environment"]),
        agents=AgentConfig(**raw["agents"]),
        training=TrainingConfig(**raw["training"]),
    )