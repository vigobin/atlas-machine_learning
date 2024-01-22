#!/usr/bin/env python3
"""Compute the Monte-Carlo policy gradient"""

import numpy as np


def policy_gradient(state, weight):
    """ function that computes the Monte-Carlo policy gradient based on a
            state and a weight matrix.
        state: matrix representing the current observation of the environment.
        weight: matrix of random weight.
        Return: the action and the gradient (in this order)."""
    weighted_matrix = state.dot(weight)
    input_exp = np.exp(weighted_matrix)
    softmax_output = input_exp / np.sum(input_exp)

    action = np.argmax(softmax_output)
    dsoftmax = softmax_grad(softmax_output)[action, :]
    dlog = dsoftmax / softmax_output[0, action]
    gradient = state.T.dot(dlog[None, :])

    return action, gradient


def softmax_grad(softmax):
    s = softmax.reshape(-1, 1)
    return np.diagflat(s) - np.dot(s, s.T)
