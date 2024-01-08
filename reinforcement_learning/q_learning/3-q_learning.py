#!/usr/bin/env python3
"""Q-learning function"""

import numpy as np


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99,
          epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """performs Q-learning:
    env is the FrozenLakeEnv instance.
    Q is a numpy.ndarray containing the Q-table.
    episodes is the total number of episodes to train over.
    max_steps is the maximum number of steps per episode.
    alpha is the learning rate.
    gamma is the discount rate.
    epsilon is the initial threshold for epsilon greedy.
    min_epsilon is the minimum value that epsilon should decay to.
    epsilon_decay is the decay rate for updating epsilon between episodes.
    When the agent falls in a hole, the reward should be updated to be -1.
    Returns: Q, total_rewards
        Q is the updated Q-table.
        total_rewards is a list containing the rewards per episode."""
    total_rewards = []
    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0

        for step in range(max_steps):
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state, :])

            result = env.step(action)
            next_state, reward, done, _ = result[:4]

            Q[state, action] = Q[state, action] + alpha * (
                reward + gamma * np.max(Q[next_state, :]) - Q[
                    state, action])

            state = next_state
            episode_reward += reward

            if done:
                break

        total_rewards.append(episode_reward)

        epsilon = max(min_epsilon, epsilon - epsilon_decay)

    return Q, total_rewards
