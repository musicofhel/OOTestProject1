# OOTestProject1

A prompt evaluation benchmark for testing LLM outputs.

## Installation

```bash
pip instal oo-test-project
```

## Usage

```python
from oo_test_project.evaluator import evaluate
result = evaluate("What is 2+2?", expected="4")
print(result.score)
```

## Development

```bash
pip install -e ".[dev]"
pytest
```
