"""Calculator utilities for oo-test-project.

Includes input sanitization to prevent code injection via eval() (CWE-95).
"""

import ast
import operator
import re


class InvalidInputError(ValueError):
    """Raised when calculator input fails sanitization."""


# Supported binary operators
_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

# Supported unary operators
_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def sanitize_input(expression: str) -> str:
    """Validate and sanitize a calculator expression.

    Rejects non-numeric/non-operator strings and prevents code injection
    via eval() (CWE-95, B307).

    Args:
        expression: A string containing a mathematical expression.

    Returns:
        The sanitized expression string.

    Raises:
        InvalidInputError: If the expression contains disallowed characters
            or patterns.
    """
    if not isinstance(expression, str):
        raise InvalidInputError("Expression must be a string")

    stripped = expression.strip()
    if not stripped:
        raise InvalidInputError("Expression must not be empty")

    # Only allow digits, decimal points, whitespace, and basic math operators
    if not re.fullmatch(r'[\d\s\+\-\*\/\.\(\)]+', stripped):
        raise InvalidInputError(
            f"Expression contains invalid characters: {stripped!r}"
        )

    return stripped


def _eval_node(node: ast.AST) -> float:
    """Recursively evaluate an AST node containing only arithmetic."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
        return _UNARY_OPERATORS[type(node.op)](_eval_node(node.operand))
    raise InvalidInputError(f"Unsupported expression node: {ast.dump(node)}")


def safe_eval(expression: str) -> float:
    """Safely evaluate a mathematical expression.

    Uses sanitize_input to validate the expression, then evaluates via
    AST walking — never calls eval() — preventing arbitrary code
    execution (CWE-95).

    Args:
        expression: A string containing a mathematical expression.

    Returns:
        The numeric result of the expression.

    Raises:
        InvalidInputError: If the expression is not a valid math expression.
    """
    sanitized = sanitize_input(expression)
    try:
        tree = ast.parse(sanitized, mode="eval")
    except SyntaxError as e:
        raise InvalidInputError(f"Invalid expression: {e}") from e
    try:
        return _eval_node(tree)
    except ZeroDivisionError as e:
        raise InvalidInputError(f"Invalid expression: {e}") from e
