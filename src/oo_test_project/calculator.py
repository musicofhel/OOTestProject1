"""Calculator utilities for oo-test-project."""

import math

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return the remainder of a divided by b using truncated division.

    Unlike Python's % operator (which uses floored division), this function
    uses truncated division so the result has the same sign as the dividend,
    matching the behavior expected by most mathematical contexts.

    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return math.fmod(a, b)
