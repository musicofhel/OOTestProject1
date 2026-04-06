"""Regression tests for calculator.py — modulo edge cases."""
import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_basic(self):
        assert modulo(7, 3) == 1

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_exact_division(self):
        assert modulo(9, 3) == 0

    def test_negative_dividend(self):
        assert modulo(-7, 3) == 2

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError, match="zero"):
            modulo(5, 0)

    def test_negative_divisor(self):
        """Regression: negative divisor should follow Python's floored-division semantics."""
        assert modulo(10, -3) == -2

    def test_negative_divisor_negative_dividend(self):
        assert modulo(-10, -3) == -1
