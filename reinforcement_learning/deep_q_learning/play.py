#!/usr/bin/env python3
"""Scrip to display a game played by the agent trained by train.py."""

dqn.load_weights('/content/drive/MyDrive/dqn/weights.h5')

dqn.test(env, nb_episodes=5, visualize=True)
