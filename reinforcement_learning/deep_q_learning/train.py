#!/usr/bin/env python3
"""Utilizes keras, keras-rl, and gym to train an agent that can
    play Atari’s Breakout."""

import tensorflow as tf
import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from keras.callbacks import Callback
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


ENV_NAME = 'Breakout-v4'

env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))

policy = EpsGreedyQPolicy()
memory = SequentialMemory(limit=50000, window_length=1)
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory,
               nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])


class CustomCallback(Callback):
    def on_step_end(self, step, logs={}):
        if step % 100 == 0:
            print('Average reward at step {}: {}'.format(
                step, logs.get('episode_reward')))


dqn.fit(env, nb_steps=5000, visualize=False, verbose=2, callbacks=[
    CustomCallback()])

dqn.save_weights('/content/drive/MyDrive/dqn/weights.h5', overwrite=True)
