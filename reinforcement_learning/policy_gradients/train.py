#!/usr/bin/env python3
"""Implement the training"""


def train(env, nb_episodes, alpha=0.000045, gamma=0.98):
    """function that implements a full training
        env: initial environment.
        nb_episodes: number of episodes used for training.
        alpha: the learning rate.
        gamma: the discount factor.
        Return: all values of the score
            (sum of all rewards during one episode loop)."""
