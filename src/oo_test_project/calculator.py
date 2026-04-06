"""Calculator utilities for oo-test-project."""


def factorial(n: int) -> int:
    """Return n! for non-negative integers. Raises ValueError for negative inputs."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
