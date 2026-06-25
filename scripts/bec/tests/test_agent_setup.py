"""Tests for bec agent-setup command."""

import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.agent_setup import AGENT_FILES, _create_symlink, run_agent_setup


@pytest.fixture
def fake_repo(tmp_path):
    """Create a minimal fake repo with content-types.yml and agent docs."""
    # Create content-types.yml marker
    (tmp_path / "content-types.yml").write_text("content_types: {}\n")

    # Create agent source files
    agents_dir = tmp_path / "docs" / "agents"
    agents_dir.mkdir(parents=True)
    (agents_dir / "AGENTS.md").write_text("# AGENTS orientation\n")
    (agents_dir / "CLAUDE.md").write_text("# CLAUDE instructions\n")

    return tmp_path


# ── Unit tests for _create_symlink ──────────────────────────────────────


class TestCreateSymlink:
    def test_creates_new_symlink(self, tmp_path):
        target = Path("docs/agents/AGENTS.md")
        link = tmp_path / "AGENTS.md"
        # Create the actual target so readlink works
        (tmp_path / "docs" / "agents").mkdir(parents=True)
        (tmp_path / "docs" / "agents" / "AGENTS.md").write_text("# test")

        status = _create_symlink(link, target, "AGENTS.md")

        assert status == "created"
        assert link.is_symlink()
        assert link.readlink() == target

    def test_already_correct_symlink(self, tmp_path):
        target = Path("docs/agents/AGENTS.md")
        link = tmp_path / "AGENTS.md"
        link.symlink_to(target)

        status = _create_symlink(link, target, "AGENTS.md")

        assert status == "already_correct"
        assert link.is_symlink()

    def test_updates_stale_symlink(self, tmp_path):
        target = Path("docs/agents/AGENTS.md")
        link = tmp_path / "AGENTS.md"
        link.symlink_to(Path("old/path/AGENTS.md"))

        status = _create_symlink(link, target, "AGENTS.md")

        assert status == "updated"
        assert link.readlink() == target

    def test_replaces_real_file(self, tmp_path):
        target = Path("docs/agents/CLAUDE.md")
        link = tmp_path / "CLAUDE.md"
        link.write_text("not a symlink")

        status = _create_symlink(link, target, "CLAUDE.md")

        assert status == "replaced"
        assert link.is_symlink()
        assert link.readlink() == target
        assert (tmp_path / "CLAUDE.md.bak").exists()

    def test_backup_does_not_clobber_existing_bak(self, tmp_path):
        target = Path("docs/agents/CLAUDE.md")
        link = tmp_path / "CLAUDE.md"
        link.write_text("current content")
        (tmp_path / "CLAUDE.md.bak").write_text("old backup")

        status = _create_symlink(link, target, "CLAUDE.md")

        assert status == "replaced"
        assert (tmp_path / "CLAUDE.md.bak").read_text() == "old backup"
        assert (tmp_path / "CLAUDE.md.bak.1").read_text() == "current content"

    def test_symlink_error_raises_click_exception(self, tmp_path, monkeypatch):
        import click

        target = Path("docs/agents/AGENTS.md")
        link = tmp_path / "AGENTS.md"

        def boom(self, t):
            raise OSError("permission denied")

        monkeypatch.setattr(Path, "symlink_to", boom)
        with pytest.raises(click.ClickException, match="failed to create symlink AGENTS.md"):
            _create_symlink(link, target, "AGENTS.md")


# ── CLI integration tests ───────────────────────────────────────────────


class TestAgentSetupCLI:
    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["agent-setup", "--help"])
        assert result.exit_code == 0
        assert "Symlink AGENTS.md and CLAUDE.md" in result.output

    def test_creates_symlinks(self, fake_repo, monkeypatch):
        monkeypatch.chdir(fake_repo)
        runner = CliRunner()
        result = runner.invoke(cli, ["agent-setup"])

        assert result.exit_code == 0
        assert "Agent orientation files are ready" in result.output
        assert (fake_repo / "AGENTS.md").is_symlink()
        assert (fake_repo / "CLAUDE.md").is_symlink()

    def test_json_output(self, fake_repo, monkeypatch):
        monkeypatch.chdir(fake_repo)
        runner = CliRunner()
        result = runner.invoke(cli, ["agent-setup", "--json"])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "symlinks" in data
        assert len(data["symlinks"]) == 2
        for entry in data["symlinks"]:
            assert "file" in entry
            assert "target" in entry
            assert "status" in entry

    def test_idempotent(self, fake_repo, monkeypatch):
        monkeypatch.chdir(fake_repo)
        runner = CliRunner()

        # Run twice
        result1 = runner.invoke(cli, ["agent-setup"])
        assert result1.exit_code == 0

        result2 = runner.invoke(cli, ["agent-setup", "--json"])
        assert result2.exit_code == 0
        data = json.loads(result2.output)
        for entry in data["symlinks"]:
            assert entry["status"] == "already_correct"

    def test_missing_source_file(self, tmp_path, monkeypatch):
        """Error when source agent docs don't exist."""
        (tmp_path / "content-types.yml").write_text("content_types: {}\n")
        # Don't create docs/agents/ — sources will be missing
        monkeypatch.chdir(tmp_path)
        runner = CliRunner()
        result = runner.invoke(cli, ["agent-setup"])

        assert result.exit_code == 1
        assert "source file not found" in result.output


# ── Real repo tests ─────────────────────────────────────────────────────


class TestAgentSetupRealRepo:
    def test_source_files_exist(self, repo_root):
        """Both source files must exist in the real repo."""
        for source_rel, _ in AGENT_FILES:
            source = repo_root / source_rel
            assert source.exists(), f"Missing: {source_rel}"

    def test_agents_md_content(self, repo_root):
        """AGENTS.md should have key sections."""
        content = (repo_root / "docs" / "agents" / "AGENTS.md").read_text()
        assert "Content Types" in content
        assert "bec CLI" in content
        assert "Content Conventions" in content
        assert "Common Pitfalls" in content
        assert "content-types.yml" in content

    def test_claude_md_content(self, repo_root):
        """CLAUDE.md should reference AGENTS.md and have workflow."""
        content = (repo_root / "docs" / "agents" / "CLAUDE.md").read_text()
        assert "AGENTS.md" in content
        assert "bec validate" in content
        assert "Workflow" in content

    def test_agents_md_under_3000_tokens(self, repo_root):
        """AGENTS.md should be compact (<3,000 tokens ~ <12,000 chars)."""
        content = (repo_root / "docs" / "agents" / "AGENTS.md").read_text()
        # Rough token estimate: ~4 chars per token
        assert len(content) < 12000, f"AGENTS.md too large: {len(content)} chars"

    def test_combined_under_4000_tokens(self, repo_root):
        """AGENTS.md + content-types.yml should be under 4,000 tokens combined."""
        agents = (repo_root / "docs" / "agents" / "AGENTS.md").read_text()
        ct = (repo_root / "content-types.yml").read_text()
        combined = len(agents) + len(ct)
        # ~4 chars per token, 4000 tokens = 16000 chars
        assert combined < 16000, f"Combined too large: {combined} chars"

    def test_gitignore_entries(self, repo_root):
        """Both symlink names should be gitignored."""
        gitignore = (repo_root / ".gitignore").read_text()
        assert "AGENTS.md" in gitignore
        assert "CLAUDE.md" in gitignore
