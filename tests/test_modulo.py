"""Regression tests for modulo edge cases."""

import pytest

from oo_test_project.calculator import modulo


class TestModulo:
    def test_positive_divisor(self):
        assert modulo(10, 3) == 1

    def test_negative_divisor(self):
        # Result should follow sign of divisor (Python semantics)
        assert modulo(10, -3) == -2

    def test_negative_dividend(self):
        assert modulo(-10, 3) == 2

    def test_both_negative(self):
        assert modulo(-10, -3) == -1

    def test_zero_dividend(self):
        assert modulo(0, 5) == 0

    def test_zero_divisor_raises(self):
        with pytest.raises(ValueError, match="zero"):
            modulo(5, 0)
