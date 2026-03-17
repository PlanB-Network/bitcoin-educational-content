"""Tests for bec.lib.repo."""

from pathlib import Path

import pytest

from bec.lib.repo import find_repo_root, resolve_content_path


def test_find_repo_root_from_repo(repo_root):
    """Finding repo root from within the repo should succeed."""
    found = find_repo_root(repo_root)
    assert found == repo_root
    assert (found / "content-types.yml").is_file()


def test_find_repo_root_from_subdirectory(repo_root):
    """Finding repo root from a deep subdirectory should work."""
    subdir = repo_root / "scripts" / "bec" / "src"
    found = find_repo_root(subdir)
    assert found == repo_root


def test_find_repo_root_not_found(tmp_path):
    """Should raise FileNotFoundError when no repo root exists."""
    with pytest.raises(FileNotFoundError):
        find_repo_root(tmp_path)


def test_resolve_content_path_relative(repo_root):
    """Relative paths should be resolved against repo root."""
    result = resolve_content_path("courses/btc101", repo_root)
    assert result == (repo_root / "courses" / "btc101").resolve()


def test_resolve_content_path_absolute(repo_root):
    """Absolute paths should be returned as-is."""
    abs_path = repo_root / "courses" / "btc101"
    result = resolve_content_path(str(abs_path), repo_root)
    assert result == abs_path
