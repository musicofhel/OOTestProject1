"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return a mod b using Python's built-in % semantics.

    The result has the same sign as the divisor b, consistent with Python's
    % operator (e.g. 7 % -3 == -2, 5 % -3 == -1).
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a % b
