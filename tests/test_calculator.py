"""Tests for calculator utilities."""
from oo_test_project.calculator import power
import pytest


class TestPower:
    def test_positive_integer_exponent(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_one_exponent(self):
        assert power(7, 1) == 7

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_fractional_exponent(self):
        assert power(9, 0.5) == 3.0

    def test_zero_base(self):
        assert power(0, 5) == 0

    def test_negative_base_integer_exponent(self):
        assert power(-2, 3) == -8

    def test_negative_base_even_exponent(self):
        assert power(-3, 2) == 9

    def test_negative_base_fractional_exponent_raises(self):
        with pytest.raises(ValueError):
            power(-4, 0.5)

    def test_large_result_overflow(self):
        with pytest.raises(OverflowError):
            power(10.0, 1000)

    def test_one_base(self):
        assert power(1, 100) == 1

    def test_float_base_and_exponent(self):
        result = power(2.5, 2)
        assert result == pytest.approx(6.25)
