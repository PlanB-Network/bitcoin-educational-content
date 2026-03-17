"""bec CLI — Bitcoin Educational Content tooling."""

import click

from bec import __version__


@click.group()
@click.version_option(version=__version__, prog_name="bec")
def cli():
    """bec — Bitcoin Educational Content CLI.

    Agent-first tooling for validation, scaffolding, and reporting.
    """
    pass


@cli.command()
@click.argument("path", required=False)
@click.option("--all", "validate_all", is_flag=True, help="Validate all content in the repo.")
@click.option("--json", "json_output", is_flag=True, help="Output results as JSON.")
def validate(path, validate_all, json_output):
    """Validate content against schemas."""
    click.echo("validate: not yet implemented")
    raise SystemExit(1)


@cli.group()
def new():
    """Scaffold new content (course, tutorial, professor, event, resource)."""
    pass


@new.command("course")
def new_course():
    """Scaffold a new course."""
    click.echo("new course: not yet implemented")
    raise SystemExit(1)


@new.command("tutorial")
def new_tutorial():
    """Scaffold a new tutorial."""
    click.echo("new tutorial: not yet implemented")
    raise SystemExit(1)


@new.command("professor")
def new_professor():
    """Scaffold a new professor profile."""
    click.echo("new professor: not yet implemented")
    raise SystemExit(1)


@new.command("event")
def new_event():
    """Scaffold a new event."""
    click.echo("new event: not yet implemented")
    raise SystemExit(1)


@new.command("resource")
def new_resource():
    """Scaffold a new resource (book, podcast, channel, etc.)."""
    click.echo("new resource: not yet implemented")
    raise SystemExit(1)


@cli.group()
def add():
    """Add content parts (part, chapter, quiz, language)."""
    pass


@add.command("part")
def add_part():
    """Add a part separator to a course."""
    click.echo("add part: not yet implemented")
    raise SystemExit(1)


@add.command("chapter")
def add_chapter():
    """Add a chapter with auto-generated BIP39 chapterId."""
    click.echo("add chapter: not yet implemented")
    raise SystemExit(1)


@add.command("quiz")
def add_quiz():
    """Add a quiz to a course chapter."""
    click.echo("add quiz: not yet implemented")
    raise SystemExit(1)


@add.command("language")
def add_language():
    """Add a new language file to existing content."""
    click.echo("add language: not yet implemented")
    raise SystemExit(1)


@cli.group()
def proofread():
    """Manage proofreading metadata."""
    pass


@proofread.command("update")
def proofread_update():
    """Update proofreading metadata for a content item."""
    click.echo("proofread update: not yet implemented")
    raise SystemExit(1)


@proofread.command("reward")
def proofread_reward():
    """Calculate proofreading rewards."""
    click.echo("proofread reward: not yet implemented")
    raise SystemExit(1)


@proofread.command("batch-add")
def proofread_batch_add():
    """Bulk-update proofreading metadata."""
    click.echo("proofread batch-add: not yet implemented")
    raise SystemExit(1)


@proofread.command("status")
def proofread_status():
    """Show proofreading status for a content item."""
    click.echo("proofread status: not yet implemented")
    raise SystemExit(1)


@cli.group()
def report():
    """Generate HTML/JSON reports."""
    pass


@report.command("translation")
def report_translation():
    """Generate markdown translation coverage report."""
    click.echo("report translation: not yet implemented")
    raise SystemExit(1)


@report.command("images")
def report_images():
    """Generate image translation progress report."""
    click.echo("report images: not yet implemented")
    raise SystemExit(1)


@report.command("video")
def report_video():
    """Generate video deployment status report."""
    click.echo("report video: not yet implemented")
    raise SystemExit(1)


@report.command("proofreading")
def report_proofreading():
    """Generate proofreading dashboard."""
    click.echo("report proofreading: not yet implemented")
    raise SystemExit(1)


@report.command("analytics")
def report_analytics():
    """Generate course analytics report."""
    click.echo("report analytics: not yet implemented")
    raise SystemExit(1)


@cli.command("agent-setup")
def agent_setup():
    """Symlink AGENTS.md and CLAUDE.md to repo root."""
    click.echo("agent-setup: not yet implemented")
    raise SystemExit(1)
