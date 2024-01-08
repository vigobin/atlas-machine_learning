#!/usr/bin/env python3
"""Play function"""

import numpy as np


def play(env, Q, max_steps=100):
    """Has the trained agent play an episode:
        env is the FrozenLakeEnv instance.
        Q is a numpy.ndarray containing the Q-table.
        max_steps is the maximum number of steps in the episode.
        Each state of the board should be displayed via the console.
        Always exploit the Q-table.
        Returns: the total rewards for the episode."""
    state = env.reset()
    total_rewards = 0
    for step in range(max_steps):
        action = np.argmax(Q[state, :])
        state, reward, done, _ = env.step(action)
        total_rewards += reward
        env.render()
        if done:
            break
    return total_rewards
