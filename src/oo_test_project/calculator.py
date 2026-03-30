"""Calculator utilities for oo-test-project."""


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("factorial requires an integer")
    if n < 0:
        raise ValueError("factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
