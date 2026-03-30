"""Regression tests for modulo edge cases — negative divisor."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_dividend_positive_divisor(self):
        assert modulo(7, 3) == 1

    def test_positive_dividend_negative_divisor(self):
        # Floor-division modulo: result has same sign as divisor.
        # With truncation division this would be 1 (wrong).
        assert modulo(7, -3) == -2

    def test_negative_dividend_positive_divisor(self):
        assert modulo(-7, 3) == 2

    def test_negative_dividend_negative_divisor(self):
        assert modulo(-7, -3) == -1

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0
        assert modulo(0, -5) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError, match="zero"):
            modulo(5, 0)
