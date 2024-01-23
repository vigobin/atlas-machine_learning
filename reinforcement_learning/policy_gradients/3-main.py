#!/usr/bin/env python3
"""
Main file
"""
import gym

from train_render import train_render

env = gym.make('CartPole-v1')

scores = train_render(env, 10000, 0.000045, 0.98, True)

env.close()
