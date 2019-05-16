"""
Unit tests for psbanalysis.py
"""

import numpy as np
import pdbanalysis
import pytest


def test_distance_1d():
    """
    Make sure a 1D distance is consistent.
    """
    first_point = np.array([0, 0, 0])
    second_point = np.array([0, 0, 3.3])
    distance = pdbanalysis.compute_euclidean_distance(
        first_point,
        second_point
    )
    assert np.allclose(distance, 3.3)


def test_get_carbon_alpha():
    """
    Make sure we find the carbon alpha.
    """
    input_array = np.array([
        ' DE ', 'CA', ' CA ', 'plop', ' CA ',
    ])
    expectation = np.array([2, 4])
    indices = pdbanalysis.get_carbon_alpha_index(input_array)
    assert np.all(indices == expectation)
