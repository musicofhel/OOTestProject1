"""Tests for the calculator module."""
import pytest
from oo_test_project.calculator import divide


class TestDivide:
    def test_basic_division(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero_raises_value_error(self):
        with pytest.raises(ValueError, match="zero"):
            divide(10, 0)
