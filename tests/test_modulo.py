"""Regression tests for modulo edge cases — negative divisor fix."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_divisor(self):
        assert modulo(7, 3) == 1

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_negative_dividend_positive_divisor(self):
        assert modulo(-7, 3) == 2

    def test_negative_divisor(self):
        # Regression: result must follow sign of divisor (floor-division convention)
        assert modulo(7, -3) == -2

    def test_both_negative(self):
        assert modulo(-7, -3) == -1

    def test_zero_divisor_raises(self):
        with pytest.raises(ZeroDivisionError):
            modulo(5, 0)
