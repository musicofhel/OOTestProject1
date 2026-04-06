"""Tests for calculator utilities."""
import pytest
from oo_test_project.calculator import factorial


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_small(self):
        assert factorial(5) == 120

    def test_larger(self):
        assert factorial(10) == 3628800

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_negative_large_raises(self):
        with pytest.raises(ValueError):
            factorial(-100)
