"""Tests for calculator input sanitization."""

import pytest

from oo_test_project.calculator import InvalidInputError, safe_eval, sanitize_input


class TestSanitizeInput:
    def test_valid_integer(self):
        assert sanitize_input("42") == "42"

    def test_valid_expression(self):
        assert sanitize_input("2 + 3 * 4") == "2 + 3 * 4"

    def test_valid_decimal(self):
        assert sanitize_input("3.14") == "3.14"

    def test_valid_parens(self):
        assert sanitize_input("(1 + 2) * 3") == "(1 + 2) * 3"

    def test_strips_whitespace(self):
        assert sanitize_input("  5 + 5  ") == "5 + 5"

    def test_rejects_empty(self):
        with pytest.raises(InvalidInputError, match="empty"):
            sanitize_input("")

    def test_rejects_non_string(self):
        with pytest.raises(InvalidInputError, match="must be a string"):
            sanitize_input(123)

    def test_rejects_alpha(self):
        with pytest.raises(InvalidInputError):
            sanitize_input("abc")

    def test_rejects_import(self):
        with pytest.raises(InvalidInputError):
            sanitize_input("__import__('os')")

    def test_rejects_exec(self):
        with pytest.raises(InvalidInputError):
            sanitize_input("exec('print(1)')")

    def test_rejects_semicolons(self):
        with pytest.raises(InvalidInputError):
            sanitize_input("1; import os")


class TestSafeEval:
    def test_addition(self):
        assert safe_eval("2 + 3") == 5.0

    def test_multiplication(self):
        assert safe_eval("4 * 5") == 20.0

    def test_division(self):
        assert safe_eval("10 / 4") == 2.5

    def test_complex_expression(self):
        assert safe_eval("(2 + 3) * 4") == 20.0

    def test_division_by_zero(self):
        with pytest.raises(InvalidInputError, match="Invalid expression"):
            safe_eval("1 / 0")

    def test_rejects_injection(self):
        with pytest.raises(InvalidInputError):
            safe_eval("__import__('os').system('echo pwned')")
