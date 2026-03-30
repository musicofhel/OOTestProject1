"""Calculator utilities for oo-test-project.

Includes input sanitization to prevent code injection via eval() (CWE-95).
"""

import re


class InvalidInputError(ValueError):
    """Raised when calculator input fails sanitization."""


def sanitize_input(expression: str) -> str:
    """Validate and sanitize a calculator expression.

    Accepts expressions containing digits, decimal points, parentheses,
    whitespace, and basic arithmetic operators (+, -, *, /).
    Rejects anything else to prevent injection via eval().

    Args:
        expression: A string representing a math expression.

    Returns:
        The stripped expression if valid.

    Raises:
        InvalidInputError: If the expression is empty or contains
            disallowed characters.
    """
    if not isinstance(expression, str):
        raise InvalidInputError("Input must be a string")

    stripped = expression.strip()
    if not stripped:
        raise InvalidInputError("Input must not be empty")

    # Only allow digits, decimal points, parentheses, whitespace, and +-*/
    if not re.fullmatch(r"[\d\s\+\-\*/\.\(\)]+", stripped):
        raise InvalidInputError(
            "Input contains disallowed characters: only digits, "
            "arithmetic operators (+, -, *, /), decimal points, "
            "and parentheses are allowed"
        )

    return stripped


def safe_eval(expression: str) -> float:
    """Safely evaluate a simple arithmetic expression.

    Sanitizes the input first, then evaluates using a restricted
    environment with no builtins or name access.

    Args:
        expression: A string math expression (e.g. "2 + 3 * 4").

    Returns:
        The numeric result of the expression.

    Raises:
        InvalidInputError: If the input fails sanitization.
        ArithmeticError: If evaluation fails (e.g. division by zero).
    """
    sanitized = sanitize_input(expression)
    try:
        result = eval(sanitized, {"__builtins__": {}}, {})  # nosec B307  # noqa: S307
    except ZeroDivisionError:
        raise
    except Exception as e:
        raise InvalidInputError(f"Failed to evaluate expression: {e}") from e

    if not isinstance(result, (int, float)):
        raise InvalidInputError("Expression did not produce a numeric result")

    return float(result)
