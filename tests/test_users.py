"""Tests for user database search."""

import sqlite3

from oo_test_project.db.users import search_users_by_name


def _create_test_db(path: str) -> None:
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
    conn.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
    conn.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice2@example.com')")
    conn.commit()
    conn.close()


class TestSearchUsersByName:
    def test_finds_matching_users(self, tmp_path):
        db = str(tmp_path / "test.db")
        _create_test_db(db)
        results = search_users_by_name("Alice", db_path=db)
        assert len(results) == 2
        assert all(r["name"] == "Alice" for r in results)

    def test_returns_empty_for_no_match(self, tmp_path):
        db = str(tmp_path / "test.db")
        _create_test_db(db)
        results = search_users_by_name("Charlie", db_path=db)
        assert results == []

    def test_returns_user_dicts(self, tmp_path):
        db = str(tmp_path / "test.db")
        _create_test_db(db)
        results = search_users_by_name("Bob", db_path=db)
        assert len(results) == 1
        assert results[0]["name"] == "Bob"
        assert results[0]["email"] == "bob@example.com"

    def test_sql_injection_prevented(self, tmp_path):
        """Verify parameterized query prevents SQL injection (CWE-89)."""
        db = str(tmp_path / "test.db")
        _create_test_db(db)
        malicious = "' OR '1'='1"
        results = search_users_by_name(malicious, db_path=db)
        assert results == []
