"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return a % b.

    Raises ValueError if b is zero or negative, to avoid confusing results
    from Python's floored-division modulo with negative divisors.
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    if b < 0:
        raise ValueError("divisor must be positive")
    return a % b
