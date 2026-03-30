"""Tests for bulk user insert."""
import sqlite3
import pytest
from oo_test_project.db.users import insert_users


@pytest.fixture
def db_conn():
    """Provide a fresh in-memory SQLite connection with users table."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT NOT NULL, email TEXT NOT NULL)")
    yield conn
    conn.close()


class TestInsertUsers:
    def test_insert_multiple(self, db_conn):
        users = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
        ]
        count = insert_users(users, conn=db_conn)
        assert count == 2
        rows = db_conn.execute("SELECT name, email FROM users").fetchall()
        assert rows == [("Alice", "alice@example.com"), ("Bob", "bob@example.com")]

    def test_insert_single(self, db_conn):
        count = insert_users([{"name": "Carol", "email": "carol@example.com"}], conn=db_conn)
        assert count == 1

    def test_insert_empty_list(self, db_conn):
        count = insert_users([], conn=db_conn)
        assert count == 0
        rows = db_conn.execute("SELECT * FROM users").fetchall()
        assert rows == []

    def test_insert_without_conn(self):
        users = [{"name": "Dave", "email": "dave@example.com"}]
        count = insert_users(users)
        assert count == 1

    def test_missing_field_raises(self, db_conn):
        with pytest.raises(KeyError):
            insert_users([{"name": "Eve"}], conn=db_conn)

    def test_transaction_rollback_on_error(self, db_conn):
        insert_users([{"name": "Frank", "email": "frank@example.com"}], conn=db_conn)
        with pytest.raises(KeyError):
            insert_users(
                [{"name": "Good", "email": "good@x.com"}, {"name": "Bad"}],
                conn=db_conn,
            )
        rows = db_conn.execute("SELECT name FROM users").fetchall()
        assert rows == [("Frank",)]
