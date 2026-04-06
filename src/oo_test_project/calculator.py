"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return a % b using Python's floored-division semantics.

    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a % b
