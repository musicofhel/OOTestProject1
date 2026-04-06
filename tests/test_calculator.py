"""Tests for calculator utilities."""
from oo_test_project.calculator import abs


class TestAbs:
    def test_positive_int(self):
        assert abs(5) == 5

    def test_negative_int(self):
        assert abs(-5) == 5

    def test_zero(self):
        assert abs(0) == 0

    def test_positive_float(self):
        assert abs(3.14) == 3.14

    def test_negative_float(self):
        assert abs(-3.14) == 3.14

    def test_zero_float(self):
        assert abs(0.0) == 0.0
