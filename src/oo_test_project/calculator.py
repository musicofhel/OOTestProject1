"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a: int, b: int) -> int:
    """Return a mod b using floor division (Python semantics).

    Unlike truncation-division modulo, the result has the same sign as b.
    This is the mathematically standard definition and matches Python's % operator.
    """
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a % b
