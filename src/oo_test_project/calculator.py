"""Calculator utilities for oo-test-project."""


# TB-2 will add a factorial function here


def power(base: float, exponent: float) -> float:
    """Raise base to the given exponent.

    Args:
        base: The base value.
        exponent: The exponent value.

    Returns:
        The result of base ** exponent.

    Raises:
        ValueError: If the result would be a complex number (e.g., negative base
            with fractional exponent).
        OverflowError: If the result is too large to represent.
    """
    if base < 0 and exponent != int(exponent):
        raise ValueError(
            "Negative base with fractional exponent produces a complex result"
        )
    try:
        result = base**exponent
    except OverflowError:
        raise OverflowError("Result too large to represent")
    if isinstance(result, float) and (result == float("inf") or result == float("-inf")):
        raise OverflowError("Result too large to represent")
    return result
