"""User database operations."""

import sqlite3


# TB-3 will add search_users() here


def insert_users(users: list[dict], conn: sqlite3.Connection | None = None) -> int:
    """Insert multiple users in a single transaction.

    Args:
        users: List of dicts with 'name' and 'email' fields.
        conn: Optional sqlite3 connection. If None, uses an in-memory database.

    Returns:
        Count of inserted rows.
    """
    if not users:
        return 0

    own_conn = conn is None
    if own_conn:
        conn = sqlite3.connect(":memory:")

    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (name TEXT NOT NULL, email TEXT NOT NULL)"
    )

    try:
        cursor.executemany(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            [(u["name"], u["email"]) for u in users],
        )
        conn.commit()
        return cursor.rowcount
    except Exception:
        conn.rollback()
        raise
    finally:
        if own_conn:
            conn.close()
