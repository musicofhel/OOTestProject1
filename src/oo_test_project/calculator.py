"""Calculator utilities for oo-test-project."""

import ast
import operator
import re


class InvalidInputError(ValueError):
    """Raised when calculator input fails sanitization."""


def sanitize_input(expression: str) -> str:
    """Validate and sanitize a calculator input expression.

    Accepts numeric values and basic arithmetic expressions containing
    digits, decimal points, spaces, and operators (+, -, *, /, parentheses).
    Rejects anything else to prevent code injection via eval().

    Args:
        expression: The raw input string to validate.

    Returns:
        The stripped, validated expression.

    Raises:
        InvalidInputError: If the input contains disallowed characters
            or patterns.
    """
    if not isinstance(expression, str):
        raise InvalidInputError("Input must be a string")

    stripped = expression.strip()
    if not stripped:
        raise InvalidInputError("Input must not be empty")

    # Only allow digits, decimal points, whitespace, and basic arithmetic operators
    if not re.fullmatch(r'[\d\s\+\-\*/\.\(\)]+', stripped):
        raise InvalidInputError(
            "Input contains invalid characters. "
            "Only digits, decimal points, and operators (+, -, *, /, parentheses) are allowed."
        )

    # Reject double dots (not a valid number)
    if '..' in stripped:
        raise InvalidInputError("Invalid numeric format")

    return stripped


# Allowed AST node-to-operator mapping for safe evaluation
_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _eval_node(node: ast.AST) -> float:
    """Recursively evaluate an AST node containing only arithmetic."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_func = _OPERATORS[type(node.op)]
        if isinstance(node.op, ast.Div) and right == 0:
            raise InvalidInputError("Division by zero")
        return op_func(left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval_node(node.operand))
    raise InvalidInputError("Expression contains unsupported operations")


def safe_eval(expression: str) -> float:
    """Safely evaluate a simple arithmetic expression.

    Uses sanitize_input to validate the expression, then evaluates it
    using AST parsing instead of eval() to prevent code injection.

    Args:
        expression: A string containing a simple arithmetic expression.

    Returns:
        The numeric result of the expression.

    Raises:
        InvalidInputError: If the input fails sanitization or evaluation.
    """
    sanitized = sanitize_input(expression)
    try:
        tree = ast.parse(sanitized, mode="eval")
    except SyntaxError as e:
        raise InvalidInputError(f"Invalid expression: {e}") from e
    return _eval_node(tree)


# TB-2 will add a factorial function here
