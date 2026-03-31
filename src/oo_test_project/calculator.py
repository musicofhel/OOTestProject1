"""Calculator utilities for oo-test-project."""

import math


def factorial(n):
    """Compute factorial of a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("factorial requires an integer")
    if n < 0:
        raise ValueError("factorial of negative number is undefined")
    return math.factorial(n)
