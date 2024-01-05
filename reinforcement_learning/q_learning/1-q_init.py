#!/usr/bin/env python3
"""Initialize Q-table"""
import numpy as np


def q_init(env):
    """Initializes the Q-table:
    env is the FrozenLakeEnv instance.
    Returns: the Q-table as a numpy.ndarray of zeros."""
    q_table = np.zeros([env.observation_space.n, env.action_space.n])
    return q_table
