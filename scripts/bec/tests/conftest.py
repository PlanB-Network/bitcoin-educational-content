"""Shared test fixtures for bec tests."""

from pathlib import Path

import pytest


@pytest.fixture
def repo_root() -> Path:
    """Return the real repo root (parent of scripts/bec/)."""
    return Path(__file__).resolve().parent.parent.parent.parent


@pytest.fixture
def fixtures_dir() -> Path:
    """Return the test fixtures directory."""
    return Path(__file__).resolve().parent / "fixtures"
