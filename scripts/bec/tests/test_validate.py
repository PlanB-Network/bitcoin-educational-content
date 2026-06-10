"""Tests for bec validate command — CLI integration and folder validation."""

from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.validate import (
    _resolve_type_filter,
    _validate_event_semantics,
    _validate_folder,
)
from bec.lib.content_types import load_registry


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def registry(repo_root):
    return load_registry(repo_root)


@pytest.fixture
def tmp_repo(tmp_path, repo_root):
    """A minimal repo root with the real content-types.yml but no schemas."""
    import shutil

    shutil.copy(repo_root / "content-types.yml", tmp_path / "content-types.yml")
    return tmp_path


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

    def test_missing_metadata_file_is_error(self, registry, tmp_repo):
        """A folder without its metadata file must FAIL, not pass with a warning."""
        d = tmp_repo / "events" / "misnamed"
        d.mkdir(parents=True)
        (d / "events.yml").write_text("name: oops\n")  # wrong name, should be event.yml
        results = _validate_folder(d, registry, tmp_repo)
        assert len(results) == 1
        assert not results[0].is_valid
        assert "Missing metadata file" in results[0].errors[0]

    def test_malformed_metadata_yaml_is_error_not_crash(self, registry, tmp_repo):
        """Broken YAML in the metadata file becomes an error result, not a traceback."""
        d = tmp_repo / "courses" / "broken"
        d.mkdir(parents=True)
        (d / "course.yml").write_text("foo: [unclosed\n")
        results = _validate_folder(d, registry, tmp_repo)
        assert any(
            "Failed to parse YAML" in e for r in results for e in r.errors
        )

    def test_malformed_quiz_yaml_is_error_not_crash(self, registry, repo_root, tmp_repo):
        """Broken YAML in a quiz file becomes an error result for that file only."""
        import shutil

        d = tmp_repo / "courses" / "quizbroken"
        quiz = d / "quizz" / "001"
        quiz.mkdir(parents=True)
        (d / "course.yml").write_text("id: x\n")
        # Real schemas so the schema-backed quiz path runs
        shutil.copytree(repo_root / "schemas", tmp_repo / "schemas")
        (quiz / "question.yml").write_text("foo: [unclosed\n")
        (quiz / "en.yml").write_text("question: [unclosed\n")
        results = _validate_folder(d, registry, tmp_repo)
        parse_errors = [
            e for r in results for e in r.errors if "Failed to parse YAML" in e
        ]
        assert len(parse_errors) == 2


# ---------------------------------------------------------------------------
# Event semantics
# ---------------------------------------------------------------------------


class TestValidateEventSemantics:
    def test_non_dict_root_does_not_crash(self):
        result = _validate_event_semantics(["not", "a", "dict"], "event.yml")
        assert result.errors == []
        assert result.warnings == []

    def test_non_numeric_price_does_not_crash(self):
        result = _validate_event_semantics({"price_dollars": "free"}, "event.yml")
        assert result.errors == []

    def test_numeric_price_without_booking_warns(self):
        result = _validate_event_semantics({"price_dollars": 10}, "event.yml")
        assert any("booking is disabled" in w for w in result.warnings)

    def test_bool_price_ignored(self):
        result = _validate_event_semantics({"price_dollars": True}, "event.yml")
        assert result.warnings == []


# ---------------------------------------------------------------------------
# Type filter resolution
# ---------------------------------------------------------------------------


class TestResolveTypeFilter:
    def test_none_returns_all(self, registry):
        assert _resolve_type_filter(registry, None) == list(registry.content_types.keys())

    def test_direct_key(self, registry):
        assert _resolve_type_filter(registry, "course") == ["course"]

    def test_plural(self, registry):
        assert _resolve_type_filter(registry, "courses") == ["course"]
        assert _resolve_type_filter(registry, "events") == ["event"]

    def test_resources_returns_all_resource_types(self, registry):
        keys = _resolve_type_filter(registry, "resources")
        assert "book" in keys
        assert "glossary" in keys
        assert "course" not in keys
        assert "tutorial" not in keys

    def test_resource_path(self, registry):
        assert _resolve_type_filter(registry, "resources/books") == ["book"]

    def test_unknown_returns_empty(self, registry):
        assert _resolve_type_filter(registry, "bogus") == []


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

    def test_validate_all_errors_include_file_paths(
        self, runner, registry, tmp_repo, monkeypatch
    ):
        """Aggregated --all errors are prefixed with the originating file path."""
        import json

        d = tmp_repo / "courses" / "broken"
        d.mkdir(parents=True)
        (d / "course.yml").write_text("foo: [unclosed\n")
        monkeypatch.setattr("bec.commands.validate.find_repo_root", lambda: tmp_repo)

        result = runner.invoke(cli, ["validate", "--all", "--json"])
        assert result.exit_code == 1
        data = json.loads(result.output)
        item = next(i for i in data["items"] if i["path"] == "courses/broken")
        assert item["status"] == "error"
        assert all(e.startswith("courses/broken/course.yml: ") for e in item["errors"])

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
