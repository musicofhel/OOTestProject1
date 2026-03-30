"""Calculator utilities for oo-test-project."""

# TB-2 will add a factorial function here


def divide(a, b):
    """Divide a by b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
