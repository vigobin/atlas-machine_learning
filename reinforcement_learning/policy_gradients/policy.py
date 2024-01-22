#!/usr/bin/env python3
"""Simple Policy function"""

import numpy as np


def policy(matrix, weight):
    """Function that computes to policy with a weight of a matrix."""
    weighted_matrix = matrix.dot(weight)
    input_exp = np.exp(weighted_matrix)
    policy = input_exp / np.sum(input_exp)

    return policy
