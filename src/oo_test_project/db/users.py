"""User database operations."""

from dataclasses import dataclass


@dataclass
class User:
    """A user record."""
    id: int
    name: str
    email: str


def get_user(user_id: int, db_path: str = ":memory:") -> User | None:
    """Get a user by ID."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(id=row[0], name=row[1], email=row[2])
    return None
