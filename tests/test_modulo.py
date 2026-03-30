"""Regression tests for the modulo function — negative divisor edge case."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_divisor(self):
        assert modulo(7, 3) == 1

    def test_zero_remainder(self):
        assert modulo(6, 3) == 0

    def test_negative_dividend(self):
        assert modulo(-7, 3) == 2

    def test_negative_divisor_edge_case(self):
        """Regression: negative divisor follows Python % semantics (result <= 0)."""
        assert modulo(7, -3) == -2
        assert modulo(5, -3) == -1
        assert modulo(7, -4) == -1

    def test_negative_dividend_negative_divisor(self):
        assert modulo(-7, -3) == -1
        assert modulo(-5, -3) == -2

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError, match="zero"):
            modulo(5, 0)
