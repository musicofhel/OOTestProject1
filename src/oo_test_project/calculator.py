"""Calculator utilities for oo-test-project."""


def factorial(n):
    """Return n! for non-negative integers.

    Raises TypeError for non-integer input.
    Raises ValueError for negative input.
    """
    if not isinstance(n, int):
        raise TypeError("integer input required")
    if n < 0:
        raise ValueError("negative input not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


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
