"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def modulo(a, b):
    """Return the remainder of a divided by b using truncated division."""
    if b == 0:
        raise ValueError("divisor cannot be zero")
    result = a % b
    # Python's % uses floor division (result sign matches b).
    # Adjust to truncated division semantics (result sign matches a).
    if result != 0 and (result < 0) != (a < 0):
        result -= b
    return result
