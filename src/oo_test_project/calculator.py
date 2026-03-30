"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a: int, b: int) -> int:
    """Return a % b using floor-division convention.

    The result has the same sign as the divisor b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b
