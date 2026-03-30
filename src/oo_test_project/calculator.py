"""Calculator utilities for oo-test-project."""

import re

# TB-2 will add a factorial function here


def sanitize_input(value: str) -> float:
    """Validate and sanitize calculator input.

    Accepts numeric strings (integers, floats, negative numbers, scientific
    notation). Rejects anything else, preventing code injection via eval().

    Args:
        value: The raw input string to validate.

    Returns:
        The parsed numeric value as a float.

    Raises:
        ValueError: If the input is not a valid numeric string.
    """
    if not isinstance(value, str):
        raise ValueError(f"Expected string input, got {type(value).__name__}")

    stripped = value.strip()
    if not stripped:
        raise ValueError("Input must not be empty")

    # Allow only valid numeric patterns: optional sign, digits, optional
    # decimal, optional scientific notation.  This rejects any string that
    # could be used for code injection (e.g. "__import__", "eval", etc.).
    if not re.fullmatch(r"[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?", stripped):
        raise ValueError(f"Invalid numeric input: {stripped!r}")

    return float(stripped)
