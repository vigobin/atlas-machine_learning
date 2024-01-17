#!/usr/bin/env python3
"""Monte Carlo function"""

import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                alpha=0.1, gamma=0.99):
    """Performs the Monte Carlo algorithm:
        env is the openAI environment instance.
        V is a numpy.ndarray of shape (s,) containing the value estimate.
        policy is a function that takes in a state and returns the
            next action to take.
        episodes is the total number of episodes to train over.
        max_steps is the maximum number of steps per episode.
        alpha is the learning rate.
        gamma is the discount rate.
        Returns: V, the updated value estimate."""
    for _ in range(episodes):
        state = env.reset()
        done = False
        steps = 0
        rewards = []
        states = []
        while not done and steps < max_steps:
            action = policy(state)
            next_state, reward, done, _ = env.step(action)
            states.append(state)
            rewards.append(reward)
            state = next_state
            steps += 1

        G = 0
        for t in range(steps-1, -1, -1):
            G = gamma * G + rewards[t]
            V[states[t]] = V[states[t]] + alpha * (G - V[states[t]])
    return V
