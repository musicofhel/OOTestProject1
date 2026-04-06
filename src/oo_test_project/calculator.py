"""Calculator utilities for oo-test-project."""


def power(base: float, exponent: int) -> float:
    """Return base raised to the exponent.

    Handles positive integers, zero exponent (returns 1),
    and negative exponent (returns float).
    """
    return base ** exponent
