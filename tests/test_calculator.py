"""Tests for calculator module."""
import pytest
from oo_test_project.calculator import divide


class TestDivide:
    def test_normal_division(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)
