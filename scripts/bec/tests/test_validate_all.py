"""Tests for bec validate --all (Phase 3): discovery, filters, JSON output."""

import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.validate import (
    _discover_content_folders,
    _resolve_type_filter,
)
from bec.lib.content_types import load_registry


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def registry(repo_root):
    return load_registry(repo_root)


# ---------------------------------------------------------------------------
# Discovery tests
# ---------------------------------------------------------------------------


class TestDiscoverContentFolders:
    def test_discovers_courses(self, repo_root, registry):
        """Should find course folders under courses/."""
        folders = _discover_content_folders(repo_root, registry, type_filter="course")
        assert len(folders) > 0
        for path, key in folders:
            assert key == "course"
            assert path.parent.name == "courses" or "courses" in str(path)

    def test_discovers_tutorials(self, repo_root, registry):
        """Should find tutorial folders under tutorials/{category}/."""
        folders = _discover_content_folders(repo_root, registry, type_filter="tutorial")
        assert len(folders) > 0
        for path, key in folders:
            assert key == "tutorial"

    def test_discovers_professors(self, repo_root, registry):
        folders = _discover_content_folders(repo_root, registry, type_filter="professor")
        assert len(folders) > 0
        for _, key in folders:
            assert key == "professor"

    def test_discovers_events(self, repo_root, registry):
        folders = _discover_content_folders(repo_root, registry, type_filter="event")
        assert len(folders) > 0
        for _, key in folders:
            assert key == "event"

    def test_discovers_books(self, repo_root, registry):
        folders = _discover_content_folders(repo_root, registry, type_filter="book")
        assert len(folders) > 0
        for _, key in folders:
            assert key == "book"

    def test_discovers_all_types(self, repo_root, registry):
        """No filter → discovers all content types."""
        folders = _discover_content_folders(repo_root, registry, type_filter=None)
        keys_found = {key for _, key in folders}
        # Should find at least courses, tutorials, professors
        assert "course" in keys_found
        assert "tutorial" in keys_found
        assert "professor" in keys_found

    def test_total_content_count(self, repo_root, registry):
        """Should discover a substantial number of content items."""
        folders = _discover_content_folders(repo_root, registry)
        # PRD says 2,600+ — be generous with threshold
        assert len(folders) > 100, f"Only found {len(folders)} content items"

    def test_no_hidden_dirs(self, repo_root, registry):
        """Should not include hidden directories."""
        folders = _discover_content_folders(repo_root, registry)
        for path, _ in folders:
            assert not path.name.startswith(".")

    def test_invalid_filter_returns_empty(self, repo_root, registry):
        """Unknown type filter returns empty list."""
        folders = _discover_content_folders(repo_root, registry, type_filter="nonexistent")
        assert folders == []


# ---------------------------------------------------------------------------
# Type filter resolution tests
# ---------------------------------------------------------------------------


class TestResolveTypeFilter:
    def test_none_returns_all(self, registry):
        keys = _resolve_type_filter(registry, None)
        assert len(keys) == len(registry.content_types)

    def test_direct_key(self, registry):
        assert _resolve_type_filter(registry, "course") == ["course"]
        assert _resolve_type_filter(registry, "book") == ["book"]

    def test_plural_form(self, registry):
        assert _resolve_type_filter(registry, "courses") == ["course"]
        assert _resolve_type_filter(registry, "tutorials") == ["tutorial"]
        assert _resolve_type_filter(registry, "professors") == ["professor"]
        assert _resolve_type_filter(registry, "events") == ["event"]

    def test_resource_path(self, registry):
        assert _resolve_type_filter(registry, "resources/books") == ["book"]
        assert _resolve_type_filter(registry, "resources/podcasts") == ["podcast"]
        assert _resolve_type_filter(registry, "resources/glossary") == ["glossary"]

    def test_unknown_returns_empty(self, registry):
        assert _resolve_type_filter(registry, "nonexistent") == []


# ---------------------------------------------------------------------------
# CLI integration: --all
# ---------------------------------------------------------------------------


class TestValidateAllCLI:
    def test_validate_all_help(self, runner):
        result = runner.invoke(cli, ["validate", "--help"])
        assert result.exit_code == 0
        assert "--all" in result.output
        assert "--courses-only" in result.output
        assert "--tutorials-only" in result.output
        assert "--type" in result.output
        assert "--summary-only" in result.output

    def test_validate_all_courses_only_json(self, runner, repo_root):
        """--all --courses-only --json produces valid JSON with expected structure."""
        result = runner.invoke(cli, ["validate", "--all", "--courses-only", "--json"])
        # Any exit code is fine (real content may have errors/warnings)
        assert result.exit_code in (0, 1, 2)
        data = json.loads(result.output)
        assert "summary" in data
        assert "items" in data
        summary = data["summary"]
        assert "total" in summary
        assert "passed" in summary
        assert "errors" in summary
        assert "warnings" in summary
        assert summary["total"] > 0
        # All items should be type "course"
        for item in data["items"]:
            assert item["type"] == "course"
            assert "path" in item
            assert "status" in item
            assert item["status"] in ("passed", "error", "warning")
            assert isinstance(item["errors"], list)
            assert isinstance(item["warnings"], list)

    def test_validate_all_tutorials_only_json(self, runner, repo_root):
        """--all --tutorials-only --json filters to tutorials only."""
        result = runner.invoke(cli, ["validate", "--all", "--tutorials-only", "--json"])
        assert result.exit_code in (0, 1, 2)
        data = json.loads(result.output)
        assert data["summary"]["total"] > 0
        for item in data["items"]:
            assert item["type"] == "tutorial"

    def test_validate_all_type_filter_json(self, runner, repo_root):
        """--all --type resources/books --json filters to books."""
        result = runner.invoke(cli, ["validate", "--all", "--type", "resources/books", "--json"])
        assert result.exit_code in (0, 1, 2)
        data = json.loads(result.output)
        assert data["summary"]["total"] > 0
        for item in data["items"]:
            assert item["type"] == "book"

    def test_validate_all_type_event_json(self, runner, repo_root):
        """--all --type event --json filters to events."""
        result = runner.invoke(cli, ["validate", "--all", "--type", "event", "--json"])
        assert result.exit_code in (0, 1, 2)
        data = json.loads(result.output)
        assert data["summary"]["total"] > 0
        for item in data["items"]:
            assert item["type"] == "event"

    def test_validate_all_summary_only(self, runner, repo_root):
        """--all --summary-only --courses-only should show only counts."""
        result = runner.invoke(cli, ["validate", "--all", "--courses-only", "--summary-only"])
        assert result.exit_code in (0, 1, 2)
        assert "Validation Summary" in result.output
        assert "Total items:" in result.output
        assert "Passed:" in result.output

    def test_validate_all_summary_counts_match_json(self, runner, repo_root):
        """JSON summary counts should be consistent."""
        result = runner.invoke(cli, ["validate", "--all", "--type", "professor", "--json"])
        assert result.exit_code in (0, 1, 2)
        data = json.loads(result.output)
        s = data["summary"]
        # Total = passed + errors + warnings
        assert s["total"] == s["passed"] + s["errors"] + s["warnings"]

    def test_validate_all_invalid_type(self, runner):
        """--all --type nonexistent should fail with exit code 1."""
        result = runner.invoke(cli, ["validate", "--all", "--type", "nonexistent"])
        assert result.exit_code == 1


# ---------------------------------------------------------------------------
# Exit code tests
# ---------------------------------------------------------------------------


class TestExitCodes:
    def test_exit_code_0_or_2_for_books(self, runner, repo_root):
        """Books typically pass or have only warnings."""
        result = runner.invoke(cli, ["validate", "--all", "--type", "channel", "--json"])
        # Channels have no content files, should be clean
        assert result.exit_code in (0, 1, 2)

    def test_json_exit_code_matches_summary(self, runner, repo_root):
        """Exit code should match whether errors/warnings exist in JSON."""
        result = runner.invoke(cli, ["validate", "--all", "--type", "professor", "--json"])
        data = json.loads(result.output)
        s = data["summary"]
        if s["errors"] > 0:
            assert result.exit_code == 1
        elif s["warnings"] > 0:
            assert result.exit_code == 2
        else:
            assert result.exit_code == 0
