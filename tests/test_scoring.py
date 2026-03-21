"""Tests for scoring utilities."""
from oo_test_project.scoring import normalize_score, weighted_average
import pytest


class TestNormalizeScore:
    def test_middle_value(self):
        assert normalize_score(50, 0, 100) == 0.5

    def test_at_min(self):
        assert normalize_score(0, 0, 100) == 0.0

    def test_at_max(self):
        assert normalize_score(100, 0, 100) == 1.0

    def test_clamp_above(self):
        assert normalize_score(150, 0, 100) == 1.0

    def test_clamp_below(self):
        assert normalize_score(-10, 0, 100) == 0.0

    def test_equal_min_max(self):
        assert normalize_score(5, 5, 5) == 0.0


class TestWeightedAverage:
    def test_equal_weights(self):
        assert weighted_average([0.8, 0.6]) == 0.7

    def test_custom_weights(self):
        result = weighted_average([1.0, 0.0], weights=[3.0, 1.0])
        assert result == 0.75

    def test_empty(self):
        assert weighted_average([]) == 0.0

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError):
            weighted_average([1.0], weights=[1.0, 2.0])
