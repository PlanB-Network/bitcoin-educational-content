"""Tests for bec validate command — CLI integration and folder validation."""

from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.validate import _validate_folder
from bec.lib.content_types import load_registry


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def registry(repo_root):
    return load_registry(repo_root)


# ---------------------------------------------------------------------------
# _validate_folder unit tests
# ---------------------------------------------------------------------------


class TestValidateFolder:
    def test_nonexistent_folder(self, registry, repo_root, tmp_path):
        results = _validate_folder(tmp_path / "nope", registry, repo_root)
        assert len(results) == 1
        assert not results[0].is_valid
        assert "does not exist" in results[0].errors[0]

    def test_file_not_dir(self, registry, repo_root, tmp_path):
        f = tmp_path / "file.txt"
        f.write_text("hi")
        results = _validate_folder(f, registry, repo_root)
        assert not results[0].is_valid
        assert "not a directory" in results[0].errors[0]

    def test_unknown_content_type(self, registry, repo_root, tmp_path):
        d = tmp_path / "unknown"
        d.mkdir()
        results = _validate_folder(d, registry, repo_root)
        assert not results[0].is_valid
        assert "content type" in results[0].errors[0].lower()


# ---------------------------------------------------------------------------
# Real repo content validation
# ---------------------------------------------------------------------------


class TestValidateRealContent:
    def test_validate_btc101_metadata(self, repo_root, registry):
        """Validate courses/btc101 metadata — course.yml should pass schema."""
        folder = repo_root / "courses" / "btc101"
        if not folder.exists():
            pytest.skip("courses/btc101 not found")
        results = _validate_folder(folder, registry, repo_root)
        # course.yml is always the first result — metadata should be valid
        assert results[0].is_valid, f"course.yml errors: {results[0].errors}"

    def test_validate_btc101_returns_results(self, repo_root, registry):
        """btc101 validation produces results (may have quiz-level errors)."""
        folder = repo_root / "courses" / "btc101"
        if not folder.exists():
            pytest.skip("courses/btc101 not found")
        results = _validate_folder(folder, registry, repo_root)
        assert len(results) > 0

    def test_validate_tutorial(self, repo_root, registry):
        """Validate a known tutorial path — produces results."""
        folder = repo_root / "tutorials" / "wallet" / "sparrow"
        if not folder.exists():
            pytest.skip("tutorials/wallet/sparrow not found")
        results = _validate_folder(folder, registry, repo_root)
        assert len(results) > 0

    def test_validate_book(self, repo_root, registry):
        """Validate a known book resource — metadata should pass."""
        folder = repo_root / "resources" / "books" / "mastering-bitcoin"
        if not folder.exists():
            pytest.skip("resources/books/mastering-bitcoin not found")
        results = _validate_folder(folder, registry, repo_root)
        assert results[0].is_valid, f"book.yml errors: {results[0].errors}"


# ---------------------------------------------------------------------------
# CLI integration tests
# ---------------------------------------------------------------------------


class TestValidateCLI:
    def test_validate_no_path(self, runner):
        """Should fail when no path given."""
        result = runner.invoke(cli, ["validate"])
        assert result.exit_code != 0

    def test_validate_nonexistent_path(self, runner):
        result = runner.invoke(cli, ["validate", "/tmp/does-not-exist-xyz"])
        assert result.exit_code == 1

    def test_validate_help(self, runner):
        result = runner.invoke(cli, ["validate", "--help"])
        assert result.exit_code == 0
        assert "Validate" in result.output

    def test_validate_real_course_json(self, runner, repo_root):
        """Run bec validate courses/btc101 --json and check JSON structure."""
        folder = repo_root / "courses" / "btc101"
        if not folder.exists():
            pytest.skip("courses/btc101 not found")

        import json

        result = runner.invoke(cli, ["validate", str(folder), "--json"])
        # exit code 0/1/2 are all valid (real content may have errors)
        assert result.exit_code in (0, 1, 2)
        data = json.loads(result.output)
        assert "results" in data
        assert "total_errors" in data
        assert isinstance(data["results"], list)
        assert len(data["results"]) > 0
