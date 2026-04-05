"""Regression tests for modulo edge case with negative divisors."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_both(self):
        assert modulo(10, 3) == 1

    def test_negative_dividend(self):
        assert modulo(-10, 3) == 2

    def test_negative_divisor(self):
        # Regression: result must have same sign as divisor (floor semantics)
        assert modulo(10, -3) == -2

    def test_both_negative(self):
        assert modulo(-10, -3) == -1

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_exact_multiple(self):
        assert modulo(9, 3) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ZeroDivisionError):
            modulo(5, 0)
