"""Scoring utilities for oo-test-project."""


def normalize_score(raw: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Normalize a raw score to [0, 1] range.

    Args:
        raw: The raw score value.
        min_val: Minimum possible value.
        max_val: Maximum possible value.

    Returns:
        Normalized score between 0.0 and 1.0.
    """
    if max_val == min_val:
        return 0.0
    return max(0.0, min(1.0, (raw - min_val) / (max_val - min_val)))


def weighted_average(scores: list[float], weights: list[float] | None = None) -> float:
    """Compute weighted average of scores.

    Args:
        scores: List of score values.
        weights: Optional weights (defaults to equal weighting).

    Returns:
        Weighted average score.
    """
    if not scores:
        return 0.0
    if weights is None:
        weights = [1.0] * len(scores)
    if len(weights) != len(scores):
        raise ValueError("scores and weights must have same length")
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    return sum(s * w for s, w in zip(scores, weights)) / total_weight
