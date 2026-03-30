"""Regression tests for the modulo function — negative divisor edge case."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_dividend_positive_divisor(self):
        assert modulo(7, 3) == 1

    def test_negative_dividend_positive_divisor(self):
        assert modulo(-7, 3) == -1

    def test_positive_dividend_negative_divisor(self):
        # Regression: naive `a % b` returns -2 here due to Python floor division
        assert modulo(7, -3) == 1

    def test_negative_dividend_negative_divisor(self):
        assert modulo(-7, -3) == -1

    def test_evenly_divisible_negative_divisor(self):
        assert modulo(6, -3) == 0

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError, match="zero"):
            modulo(7, 0)
