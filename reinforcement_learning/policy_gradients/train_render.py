#!/usr/bin/env python3
"""Animate iteration"""
import numpy as np
from policy_gradient import policy_gradient


def train_render(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=False):
    """function that implements a full training
        env: initial environment.
        nb_episodes: number of episodes used for training.
        alpha: the learning rate.
        gamma: the discount factor.
        show_result (default: False). When this parameter is True,
          render the environment every 1000 episodes computed.
        Return: all values of the score
            (sum of all rewards during one episode loop)."""
    n_states = env.observation_space.shape[0]
    n_actions = env.action_space.n
    weight = np.random.rand(n_states, n_actions)

    scores = []

    for episode in range(nb_episodes):
        state = env.reset()[None, :]
        grads = []
        rewards = []
        score = 0

        while True:
            action, grad = policy_gradient(state, weight)

            next_state, reward, done, _ = env.step(action)

            grads.append(grad)
            rewards.append(reward)

            score += reward
            state = next_state[None, :]

            if done:
                break

        scores.append(score)

        for i in range(len(rewards) - 2, -1, -1):
            rewards[i] += rewards[i + 1] * gamma

        for grad, reward in zip(grads, rewards):
            weight += alpha * grad * reward

        if show_result and episode % 1000 == 0:
            print("Episode: {}, Score: {}".format(episode, score))
            env.render(mode='human')

    return scores
