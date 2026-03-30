"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return a % b using floor division semantics.

    Result has the same sign as b (the divisor).
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b
