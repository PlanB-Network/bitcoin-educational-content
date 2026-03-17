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
@click.option("--courses-only", is_flag=True, help="Validate only courses (requires --all).")
@click.option("--tutorials-only", is_flag=True, help="Validate only tutorials (requires --all).")
@click.option("--type", "content_type", default=None, help="Validate a specific content type (requires --all).")
@click.option("--summary-only", is_flag=True, help="Show only aggregate counts (requires --all).")
def validate(path, validate_all, json_output, courses_only, tutorials_only, content_type, summary_only):
    """Validate content against schemas."""
    if validate_all:
        from bec.commands.validate import run_validate_all

        # Resolve filter: explicit --type wins, then shortcut flags
        type_filter = content_type
        if courses_only:
            type_filter = "course"
        elif tutorials_only:
            type_filter = "tutorial"

        run_validate_all(
            json_output=json_output,
            summary_only=summary_only,
            type_filter=type_filter,
        )
    else:
        from bec.commands.validate import run_validate

        run_validate(path=path, json_output=json_output)


@cli.group()
def new():
    """Scaffold new content (course, tutorial, professor, event, resource)."""
    pass


@new.command("course")
@click.option("--id", "course_id", default=None, help="Course ID (e.g., btc101, dev301).")
@click.option("--topic", default=None, help="Main topic (e.g., bitcoin, mining, security).")
@click.option("--subtopic", default=None, help="Subtopic (e.g., bitcoin, lightning, cryptography).")
@click.option("--level", default=None, help="Difficulty level (beginner, intermediate, advanced, expert).")
@click.option("--lang", default=None, help="Original language code (e.g., en, fr).")
@click.option("--professor-id", default=None, help="Professor UUID.")
@click.option("--json", "json_output", is_flag=True, help="Output created file paths as JSON.")
def new_course(course_id, topic, subtopic, level, lang, professor_id, json_output):
    """Scaffold a new course."""
    from bec.commands.new import run_new_course

    run_new_course(
        course_id=course_id,
        topic=topic,
        subtopic=subtopic,
        level=level,
        lang=lang,
        professor_id=professor_id,
        json_output=json_output,
    )


@new.command("tutorial")
@click.option("--category", "folder_category", default=None, help="Tutorial folder category (e.g., wallet, mining, node).")
@click.option("--id", "tutorial_id", default=None, help="Tutorial ID slug (e.g., sparrow, ledger-flex).")
@click.option("--lang", default=None, help="Original language code (e.g., en, fr).")
@click.option("--level", default=None, help="Difficulty level (beginner, intermediate, advanced, expert).")
@click.option("--professor-id", default=None, help="Professor UUID.")
@click.option("--license", "license_type", default=None, help="License type (CC-BY-SA-V4, MIT).")
@click.option("--tool-type", "schema_category", default=None, help="Tool type category (desktop, hardware, mobile, etc.).")
@click.option("--json", "json_output", is_flag=True, help="Output created file paths as JSON.")
def new_tutorial(folder_category, tutorial_id, lang, level, professor_id, license_type, schema_category, json_output):
    """Scaffold a new tutorial."""
    from bec.commands.new import run_new_tutorial

    run_new_tutorial(
        folder_category=folder_category,
        tutorial_id=tutorial_id,
        lang=lang,
        level=level,
        professor_id=professor_id,
        license_type=license_type,
        schema_category=schema_category,
        json_output=json_output,
    )


@new.command("professor")
@click.option("--id", "professor_slug", default=None, help="Professor slug ID (e.g., satoshi-nakamoto).")
@click.option("--name", default=None, help="Professor display name.")
@click.option("--lang", default=None, help="Initial language code (e.g., en, fr).")
@click.option("--json", "json_output", is_flag=True, help="Output created file paths as JSON.")
def new_professor(professor_slug, name, lang, json_output):
    """Scaffold a new professor profile."""
    from bec.commands.new import run_new_professor

    run_new_professor(
        professor_slug=professor_slug,
        name=name,
        lang=lang,
        json_output=json_output,
    )


@new.command("event")
@click.option("--id", "event_id", default=None, help="Event ID slug (e.g., bitcoin-paris-2025).")
@click.option("--name", default=None, help="Event name (include year).")
@click.option("--type", "event_type", default=None, help="Event type (workshop, course, conference, lecture, meetup).")
@click.option("--start-date", default=None, help="Start datetime (YYYY-MM-DD HH:MM:SS).")
@click.option("--end-date", default=None, help="End datetime (YYYY-MM-DD HH:MM:SS).")
@click.option("--timezone", default=None, help="IANA timezone (e.g., Europe/Paris, US/Central).")
@click.option("--city", default=None, help="City and country (e.g., Paris, France).")
@click.option("--lang", default=None, help="Event language code.")
@click.option("--json", "json_output", is_flag=True, help="Output created file paths as JSON.")
def new_event(event_id, name, event_type, start_date, end_date, timezone, city, lang, json_output):
    """Scaffold a new event."""
    from bec.commands.new import run_new_event

    run_new_event(
        event_id=event_id,
        name=name,
        event_type=event_type,
        start_date=start_date,
        end_date=end_date,
        timezone=timezone,
        city=city,
        lang=lang,
        json_output=json_output,
    )


@new.command("resource")
@click.option("--type", "resource_type", default=None, help="Resource type (book, podcast, channel, conference, movie, newsletter, paper, project, bet, glossary).")
@click.option("--id", "resource_id", default=None, help="Resource ID slug.")
@click.option("--lang", default=None, help="Language code (e.g., en, fr).")
@click.option("--json", "json_output", is_flag=True, help="Output created file paths as JSON.")
def new_resource(resource_type, resource_id, lang, json_output):
    """Scaffold a new resource (book, podcast, channel, etc.)."""
    from bec.commands.new import run_new_resource

    run_new_resource(
        resource_type=resource_type,
        resource_id=resource_id,
        lang=lang,
        json_output=json_output,
    )


@cli.group()
def add():
    """Add content parts (part, chapter, quiz, language)."""
    pass


@add.command("part")
@click.option("--course", default=None, help="Course ID (e.g., btc101).")
@click.option("--lang", default=None, help="Language code (e.g., en, fr).")
@click.option("--title", default=None, help="Part title.")
@click.option("--json", "json_output", is_flag=True, help="Output result as JSON.")
def add_part(course, lang, title, json_output):
    """Add a part separator to a course."""
    from bec.commands.add import run_add_part

    run_add_part(course=course, lang=lang, title=title, json_output=json_output)


@add.command("chapter")
@click.option("--course", default=None, help="Course ID (e.g., btc101).")
@click.option("--lang", default=None, help="Language code (e.g., en, fr).")
@click.option("--title", default=None, help="Chapter title.")
@click.option("--json", "json_output", is_flag=True, help="Output result as JSON.")
def add_chapter(course, lang, title, json_output):
    """Add a chapter with auto-generated BIP39 chapterId."""
    from bec.commands.add import run_add_chapter

    run_add_chapter(course=course, lang=lang, title=title, json_output=json_output)


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
