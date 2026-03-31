"""Tests for calculator.divide rounding behavior."""

import pytest

from oo_test_project.calculator import divide


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_rounds_to_10_decimal_places_by_default(self):
        result = divide(10, 3)
        assert result == round(10 / 3, 10)
        assert result != 10 / 3  # raw float is not rounded

    def test_custom_precision(self):
        assert divide(10, 3, precision=2) == 3.33
        assert divide(10, 3, precision=4) == 3.3333

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)
