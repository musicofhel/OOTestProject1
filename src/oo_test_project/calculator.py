"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return a modulo b.

    Follows Python semantics: result has the same sign as b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a % b
