"""Tests for bec.cli — basic smoke tests."""

from click.testing import CliRunner

from bec.cli import cli


def test_help():
    """bec --help should print help text and exit 0."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "bec" in result.output


def test_version():
    """bec --version should print version."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_subcommands_listed():
    """All expected subcommands should appear in help."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    for cmd in ["validate", "new", "add", "proofread", "report", "agent-setup"]:
        assert cmd in result.output, f"Subcommand '{cmd}' not in help output"


def test_new_subcommands():
    """bec new --help should list scaffold subcommands."""
    runner = CliRunner()
    result = runner.invoke(cli, ["new", "--help"])
    assert result.exit_code == 0
    for cmd in ["course", "tutorial", "professor", "event", "resource"]:
        assert cmd in result.output


def test_add_subcommands():
    """bec add --help should list add subcommands."""
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "--help"])
    assert result.exit_code == 0
    for cmd in ["part", "chapter", "quiz", "language"]:
        assert cmd in result.output


def test_proofread_subcommands():
    """bec proofread --help should list proofread subcommands."""
    runner = CliRunner()
    result = runner.invoke(cli, ["proofread", "--help"])
    assert result.exit_code == 0
    for cmd in ["update", "reward", "batch-add", "status"]:
        assert cmd in result.output


def test_report_subcommands():
    """bec report --help should list report subcommands."""
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "--help"])
    assert result.exit_code == 0
    for cmd in ["translation", "images", "video", "proofreading", "analytics"]:
        assert cmd in result.output


def test_report_no_subcommand_errors():
    """bec report with no subcommand and no --all prints help and exits non-zero."""
    runner = CliRunner()
    result = runner.invoke(cli, ["report"])
    assert result.exit_code == 2
    assert "Generate HTML/JSON reports" in result.output


def test_validate_type_conflicts_with_shortcut_flags():
    """--type combined with --courses-only/--tutorials-only is an error."""
    runner = CliRunner()
    for flag in ["--courses-only", "--tutorials-only"]:
        result = runner.invoke(cli, ["validate", "--all", "--type", "course", flag])
        assert result.exit_code == 2
        assert "--type cannot be combined" in result.output


def test_validate_shortcut_flags_mutually_exclusive():
    """--courses-only and --tutorials-only cannot be combined."""
    runner = CliRunner()
    result = runner.invoke(cli, ["validate", "--all", "--courses-only", "--tutorials-only"])
    assert result.exit_code == 2
    assert "mutually exclusive" in result.output
