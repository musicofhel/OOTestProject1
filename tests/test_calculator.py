"""Tests for calculator utilities."""
from oo_test_project.calculator import power
import pytest


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_negative_exponent_float_result(self):
        assert power(2, -3) == 0.125

    def test_base_zero(self):
        assert power(0, 5) == 0

    def test_base_one(self):
        assert power(1, 100) == 1

    def test_large_exponent(self):
        assert power(2, 10) == 1024

    def test_negative_base_even_exponent(self):
        assert power(-2, 4) == 16

    def test_negative_base_odd_exponent(self):
        assert power(-2, 3) == -8
