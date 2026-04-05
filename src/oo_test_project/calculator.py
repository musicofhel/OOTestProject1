"""Calculator utilities for oo-test-project."""


def factorial(n):
    """Return n! for non-negative integers.

    Raises TypeError if n is not an integer.
    Raises ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("factorial requires an integer")
    if n < 0:
        raise ValueError("factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def modulo(a, b):
    """Return a % b using floor division semantics.

    Result has the same sign as b (the divisor).
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b
