# tests/test_lib.py
from statistics import harmonic_mean
from mlproject.distance import haversine

def test_distance_positive():
    assert haversine(0, 1, 2, 3) > 0
