"""Calculator utilities for oo-test-project."""

def factorial(n):
    """Compute factorial of a non-negative integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("factorial requires an integer")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
