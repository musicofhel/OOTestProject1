"""Tests for calculator input sanitization (CWE-95)."""

import pytest

from oo_test_project.calculator import InvalidInputError, safe_eval, sanitize_input


class TestSanitizeInput:
    """Tests for sanitize_input()."""

    def test_valid_simple_expression(self):
        assert sanitize_input("2 + 3") == "2 + 3"

    def test_valid_complex_expression(self):
        assert sanitize_input("(10 + 5) * 3 / 2.5") == "(10 + 5) * 3 / 2.5"

    def test_strips_whitespace(self):
        assert sanitize_input("  42  ") == "42"

    def test_rejects_empty_string(self):
        with pytest.raises(InvalidInputError, match="empty"):
            sanitize_input("")

    def test_rejects_whitespace_only(self):
        with pytest.raises(InvalidInputError, match="empty"):
            sanitize_input("   ")

    def test_rejects_non_string(self):
        with pytest.raises(InvalidInputError, match="string"):
            sanitize_input(42)  # type: ignore[arg-type]

    def test_rejects_letters(self):
        with pytest.raises(InvalidInputError, match="disallowed"):
            sanitize_input("abc")

    def test_rejects_eval_injection(self):
        with pytest.raises(InvalidInputError, match="disallowed"):
            sanitize_input("__import__('os').system('rm -rf /')")

    def test_rejects_dunder_access(self):
        with pytest.raises(InvalidInputError, match="disallowed"):
            sanitize_input("().__class__.__bases__")

    def test_rejects_semicolons(self):
        with pytest.raises(InvalidInputError, match="disallowed"):
            sanitize_input("1; import os")

    def test_rejects_equals(self):
        with pytest.raises(InvalidInputError, match="disallowed"):
            sanitize_input("x = 1")


class TestSafeEval:
    """Tests for safe_eval()."""

    def test_addition(self):
        assert safe_eval("2 + 3") == 5.0

    def test_multiplication(self):
        assert safe_eval("4 * 5") == 20.0

    def test_division(self):
        assert safe_eval("10 / 4") == 2.5

    def test_parentheses(self):
        assert safe_eval("(2 + 3) * 4") == 20.0

    def test_decimal(self):
        assert safe_eval("3.14 * 2") == pytest.approx(6.28)

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            safe_eval("1 / 0")

    def test_rejects_injection(self):
        with pytest.raises(InvalidInputError):
            safe_eval("__import__('os').system('echo pwned')")
