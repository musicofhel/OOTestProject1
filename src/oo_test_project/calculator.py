"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return a mod b, always in the range [0, abs(b)).

    Fixes the edge case where a negative divisor causes Python's % operator
    to return a negative result (e.g. 7 % -3 == -2 in Python, but this
    function returns 1).
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a % abs(b)
