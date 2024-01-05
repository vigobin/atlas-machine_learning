#!/usr/bin/env python3
"""Epsilon Greedy"""


def epsilon_greedy(Q, state, epsilon):
    """Uses epsilon-greedy to determine the next action:
    Q is a numpy.ndarray containing the q-table
    state is the current state
    epsilon is the epsilon to use for the calculation
    Sample p with numpy.random.uniformn to determine if
        algorithm should explore or exploit.
    If exploring, pick the next action with numpy.random.randint
        from all possible actions.
    Returns: the next action index."""

