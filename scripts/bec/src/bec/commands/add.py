"""Add content parts to existing course files (part, chapter)."""

from __future__ import annotations

import json
import uuid
from pathlib import Path

import click

from bec.lib.markdown import (
    append_to_markdown,
    build_chapter_block,
    build_part_block,
    generate_chapter_id,
)
from bec.lib.repo import find_repo_root


def _resolve_course_md(course_id: str, lang: str, repo_root: Path) -> Path:
    """Resolve the markdown file path for a course + language.

    Raises click.ClickException if the file doesn't exist.
    """
    md_path = repo_root / "courses" / course_id / f"{lang}.md"
    if not md_path.is_file():
        raise click.ClickException(
            f"Course markdown not found: {md_path.relative_to(repo_root)}"
        )
    return md_path


def _list_course_ids(repo_root: Path) -> list[str]:
    """List available course IDs from the courses/ directory."""
    courses_dir = repo_root / "courses"
    if not courses_dir.is_dir():
        return []
    return sorted(
        d.name for d in courses_dir.iterdir()
        if d.is_dir() and (d / "course.yml").is_file()
    )


def _list_course_langs(course_id: str, repo_root: Path) -> list[str]:
    """List available language codes for a course."""
    course_dir = repo_root / "courses" / course_id
    if not course_dir.is_dir():
        return []
    return sorted(
        p.stem for p in course_dir.glob("*.md")
    )


# --- Part ---


def run_add_part(
    course: str | None,
    lang: str | None,
    title: str | None,
    json_output: bool,
) -> None:
    """Add a part separator to a course markdown file."""
    repo_root = find_repo_root()

    # Interactive prompts for missing args
    if not course:
        ids = _list_course_ids(repo_root)
        if ids:
            click.echo(f"Available courses: {', '.join(ids)}")
        course = click.prompt("Course ID")

    if not lang:
        langs = _list_course_langs(course, repo_root)
        if langs:
            click.echo(f"Available languages: {', '.join(langs)}")
        lang = click.prompt("Language code", default="en")

    if not title:
        title = click.prompt("Part title")

    md_path = _resolve_course_md(course, lang, repo_root)

    part_id = str(uuid.uuid4())
    block = build_part_block(title, part_id)
    append_to_markdown(md_path, block)

    rel_path = str(md_path.relative_to(repo_root))
    if json_output:
        click.echo(json.dumps({
            "action": "add_part",
            "course": course,
            "lang": lang,
            "title": title,
            "part_id": part_id,
            "file": rel_path,
        }, indent=2))
    else:
        click.echo(f"Added part '{title}' to {rel_path}")
        click.echo(f"  partId: {part_id}")


# --- Chapter ---


def run_add_chapter(
    course: str | None,
    lang: str | None,
    title: str | None,
    json_output: bool,
) -> None:
    """Add a chapter heading with auto-generated BIP39 chapterId."""
    repo_root = find_repo_root()

    # Interactive prompts for missing args
    if not course:
        ids = _list_course_ids(repo_root)
        if ids:
            click.echo(f"Available courses: {', '.join(ids)}")
        course = click.prompt("Course ID")

    if not lang:
        langs = _list_course_langs(course, repo_root)
        if langs:
            click.echo(f"Available languages: {', '.join(langs)}")
        lang = click.prompt("Language code", default="en")

    if not title:
        title = click.prompt("Chapter title")

    md_path = _resolve_course_md(course, lang, repo_root)

    chapter_id = generate_chapter_id()
    block = build_chapter_block(title, chapter_id)
    append_to_markdown(md_path, block)

    rel_path = str(md_path.relative_to(repo_root))
    if json_output:
        click.echo(json.dumps({
            "action": "add_chapter",
            "course": course,
            "lang": lang,
            "title": title,
            "chapter_id": chapter_id,
            "file": rel_path,
        }, indent=2))
    else:
        click.echo(f"Added chapter '{title}' to {rel_path}")
        click.echo(f"  chapterId: {chapter_id}")
