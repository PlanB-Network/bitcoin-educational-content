"""Tests for bec.lib.yaml_utils."""

from pathlib import Path

import pytest

from bec.lib.yaml_utils import load_yaml, load_yaml_string, dump_yaml


def test_load_yaml_preserves_dates():
    """YAML dates should remain as strings, not datetime objects."""
    result = load_yaml_string("date: 2024-01-15")
    assert isinstance(result["date"], str)
    assert result["date"] == "2024-01-15"


def test_load_yaml_basic_dict():
    """Basic dict loading should work."""
    result = load_yaml_string("key: value\nnested:\n  a: 1")
    assert result == {"key": "value", "nested": {"a": 1}}


def test_load_yaml_list():
    """Lists should load correctly."""
    result = load_yaml_string("- one\n- two\n- three")
    assert result == ["one", "two", "three"]


def test_load_yaml_empty():
    """Empty YAML should return None."""
    result = load_yaml_string("")
    assert result is None


def test_load_yaml_file(tmp_path):
    """Loading from a file should work."""
    f = tmp_path / "test.yml"
    f.write_text("name: test\ndate: 2024-03-15\n", encoding="utf-8")
    result = load_yaml(f)
    assert result["name"] == "test"
    assert isinstance(result["date"], str)


def test_load_yaml_file_not_found(tmp_path):
    """Missing file should raise FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_yaml(tmp_path / "nonexistent.yml")


def test_dump_yaml_roundtrip(tmp_path):
    """Dumping and reloading should preserve data."""
    data = {"name": "test", "tags": ["bitcoin", "mining"], "date": "2024-01-15"}
    f = tmp_path / "out.yml"
    dump_yaml(data, f)
    result = load_yaml(f)
    assert result == data


def test_dump_yaml_unicode(tmp_path):
    """Unicode characters should be preserved."""
    data = {"name": "éàü", "description": "日本語テスト"}
    f = tmp_path / "unicode.yml"
    dump_yaml(data, f)
    result = load_yaml(f)
    assert result == data
