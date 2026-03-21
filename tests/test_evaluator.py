"""Tests for the evaluator module."""
from oo_test_project.evaluator import evaluate, batch_evaluate


class TestEvaluate:
    def test_exact_match(self):
        result = evaluate("What is 2+2?", expected="4", actual="4")
        assert result.score == 1.0
        assert result.passed is True

    def test_case_insensitive(self):
        result = evaluate("Capital?", expected="Paris", actual="paris")
        assert result.score == 1.0

    def test_no_match(self):
        result = evaluate("What is 2+2?", expected="4", actual="banana")
        assert result.score == 0.0
        assert result.passed is False

    def test_partial_match(self):
        result = evaluate("Describe Python", expected="a programming language", actual="a language")
        assert 0.0 < result.score < 1.0

    def test_default_actual(self):
        result = evaluate("test", expected="hello")
        assert result.score == 1.0  # actual defaults to expected

    def test_empty_expected(self):
        result = evaluate("test", expected="", actual="something")
        assert result.score == 0.0


class TestBatchEvaluate:
    def test_batch(self):
        pairs = [
            ("q1", "a", "a"),
            ("q2", "b", "c"),
        ]
        results = batch_evaluate(pairs)
        assert len(results) == 2
        assert results[0].passed is True
