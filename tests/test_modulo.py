"""Regression tests for modulo edge case with negative divisors."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_dividend_positive_divisor(self):
        assert modulo(10, 3) == 1

    def test_positive_dividend_negative_divisor(self):
        # Edge case: negative divisor should not flip the sign of the result
        assert modulo(10, -3) == 1

    def test_negative_dividend_positive_divisor(self):
        assert modulo(-10, 3) == -1

    def test_negative_dividend_negative_divisor(self):
        assert modulo(-10, -3) == -1

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError, match="zero"):
            modulo(5, 0)
