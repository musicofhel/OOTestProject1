"""Tests for nonexistent_module.process_data."""
from oo_test_project.nonexistent_module import process_data


class TestProcessData:
    def test_none_returns_empty_dict(self):
        assert process_data(None) == {}

    def test_dict_passthrough(self):
        assert process_data({"a": 1}) == {"a": 1}
