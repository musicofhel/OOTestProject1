"""Tests for calculator input sanitizer."""

import pytest

from oo_test_project.calculator import sanitize_input


class TestSanitizeInput:
    """Tests for sanitize_input."""

    @pytest.mark.parametrize(
        "value, expected",
        [
            ("42", 42.0),
            ("-7", -7.0),
            ("3.14", 3.14),
            ("-0.5", -0.5),
            (".5", 0.5),
            ("+3", 3.0),
            ("1e10", 1e10),
            ("2.5E-3", 2.5e-3),
            ("  42  ", 42.0),
        ],
    )
    def test_valid_numeric_inputs(self, value, expected):
        assert sanitize_input(value) == expected

    @pytest.mark.parametrize(
        "value",
        [
            "",
            "abc",
            "12abc",
            "__import__('os').system('rm -rf /')",
            "eval('1+1')",
            "1 + 1",
            "0x1A",
            "inf",
            "nan",
            "; DROP TABLE users",
        ],
    )
    def test_rejects_non_numeric(self, value):
        with pytest.raises(ValueError):
            sanitize_input(value)

    def test_rejects_non_string(self):
        with pytest.raises(ValueError, match="Expected string input"):
            sanitize_input(42)  # type: ignore[arg-type]
