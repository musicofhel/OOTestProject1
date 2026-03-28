"""User database operations."""

import sqlite3
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """User model for the evaluation framework."""

    id: int
    name: str
    email: str
    role: str = "evaluator"


def get_connection(db_path: str = "users.db") -> sqlite3.Connection:
    """Get a database connection."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def search_users(query: str, db_path: str = "users.db") -> list[User]:
    """Search users by name using parameterized query."""
    conn = get_connection(db_path)
    try:
        cursor = conn.execute(
            "SELECT id, name, email, role FROM users WHERE name LIKE ?",
            (f"%{query}%",),
        )
        return [User(**dict(row)) for row in cursor.fetchall()]
    finally:
        conn.close()
