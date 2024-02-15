#!/usr/bin/env python3
"""From Numpy"""
import numpy as np
import pandas as pd


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray:
        array is the np.ndarray from which you should create the pd.DataFrame.
    The columns of the pd.DataFrame should be labeled in alphabetical order
        and capitalized. There will not be more than 26 columns.
    Returns: the newly created pd.DataFrame."""
    columns = [chr(i) for i in range(65, 65 + array.shape[1])]

    df = pd.DataFrame(array, columns=columns)
    return df
