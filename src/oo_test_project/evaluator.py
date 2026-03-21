"""Core evaluation logic for oo-test-project."""
from dataclasses import dataclass


@dataclass
class EvalResult:
    """Result of a single prompt evaluation."""
    prompt: str
    expected: str
    actual: str
    score: float
    passed: bool


def evaluate(prompt: str, expected: str, actual: str | None = None) -> EvalResult:
    """Evaluate a prompt response against expected output.

    Args:
        prompt: The input prompt.
        expected: The expected response.
        actual: The actual response (if None, uses expected for testing).

    Returns:
        EvalResult with score between 0.0 and 1.0.
    """
    if actual is None:
        actual = expected

    # Simple exact-match scoring for now
    if actual.strip().lower() == expected.strip().lower():
        score = 1.0
    else:
        # Partial credit: ratio of matching words
        expected_words = set(expected.lower().split())
        actual_words = set(actual.lower().split())
        if not expected_words:
            score = 0.0
        else:
            score = len(expected_words & actual_words) / len(expected_words)

    return EvalResult(
        prompt=prompt,
        expected=expected,
        actual=actual,
        score=round(score, 2),
        passed=score >= 0.8,
    )


def batch_evaluate(pairs: list[tuple[str, str, str]]) -> list[EvalResult]:
    """Evaluate multiple prompt/expected/actual triples.

    Args:
        pairs: List of (prompt, expected, actual) tuples.

    Returns:
        List of EvalResult objects.
    """
    return [evaluate(p, e, a) for p, e, a in pairs]
