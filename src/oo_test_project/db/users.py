"""User database operations."""

import sqlite3
from typing import Any


def search_users_by_name(name: str, db_path: str = ":memory:") -> list[dict[str, Any]]:
    """Search users by name using parameterized queries to prevent SQL injection."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.execute(
            "SELECT * FROM users WHERE name = ?", (name,)
        )
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()
