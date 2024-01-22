#!/usr/bin/env python3
"""Compute the Monte-Carlo policy gradient"""

import numpy as np


def policy_gradient(state, weight):
    """ function that computes the Monte-Carlo policy gradient based on a
            state and a weight matrix.
        state: matrix representing the current observation of the environment.
        weight: matrix of random weight.
        Return: the action and the gradient (in this order)."""
