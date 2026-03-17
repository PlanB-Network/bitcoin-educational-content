"""Scaffold new content items."""

from __future__ import annotations

import json
import re
import uuid
from datetime import date
from pathlib import Path

import click

from bec.lib.content_types import load_registry
from bec.lib.repo import find_repo_root
from bec.lib.schema import load_json_schema
from bec.lib.yaml_utils import dump_yaml


# --- Course ID validation ---

# Pattern: 3-letter discipline code + 3-digit number (e.g., btc101, dev301)
COURSE_ID_RE = re.compile(r"^[a-z]{3}\d{3}$")


def validate_course_id(course_id: str, registry) -> str | None:
    """Validate a course ID. Returns error message or None if valid."""
    if not COURSE_ID_RE.match(course_id):
        return (
            f"Invalid course ID '{course_id}'. "
            "Must be 3-letter discipline code + 3-digit number (e.g., btc101, dev301)."
        )
    prefix = course_id[:3]
    if prefix not in registry.discipline_codes:
        valid = ", ".join(sorted(registry.discipline_codes.keys()))
        return (
            f"Unknown discipline code '{prefix}'. "
            f"Valid codes: {valid}"
        )
    number = int(course_id[3:])
    min_val = int(registry.level_range["min"])
    max_val = int(registry.level_range["max"])
    if number < min_val or number > max_val:
        return (
            f"Course number {number} is out of range. "
            f"Must be between {min_val} and {max_val}."
        )
    return None


def level_from_number(number: int, registry) -> str:
    """Infer level from the course number using level_range config."""
    for level_name in ("beginner", "intermediate", "advanced", "expert"):
        range_str = registry.level_range.get(level_name, "")
        if "-" in range_str:
            lo, hi = range_str.split("-")
            if int(lo) <= number <= int(hi):
                return level_name
    return "beginner"


# --- Schema introspection ---

def get_enum_values(schema: dict, field_name: str) -> list[str]:
    """Extract enum values for a field from a JSON schema."""
    props = schema.get("properties", {})
    field_schema = props.get(field_name, {})
    return field_schema.get("enum", [])


# --- YAML generation ---

def build_course_yml(
    course_uuid: str,
    topic: str,
    subtopic: str,
    level: str,
    lang: str,
    professor_id: str,
    hours: int = 1,
    course_type: str = "theory",
) -> dict:
    """Build the course.yml data dict."""
    return {
        "id": course_uuid,
        "topic": topic,
        "subtopic": subtopic,
        "type": course_type,
        "level": level,
        "hours": hours,
        "teaching_format": "self_paced",
        "professors_id": [professor_id],
        "contributor_names": ["TODO"],
        "published_at": date.today().strftime("%Y-%m-%d"),
        "original_language": lang,
        "proofreading": [
            {
                "language": lang,
                "last_contribution_date": date.today().strftime("%Y-%m-%d"),
                "urgency": 1,
                "contributor_names": ["TODO"],
                "reward": 0,
            }
        ],
        "tags": ["TODO"],
    }


def build_course_md(course_id: str, lang: str) -> str:
    """Build the course markdown content with frontmatter and skeleton structure."""
    return f"""---
name: "TODO: Course Title"
goal: "TODO: Describe the main goal of the course in one sentence"
objectives:
  - "TODO: First learning objective"
  - "TODO: Second learning objective"
  - "TODO: Third learning objective"
---

# TODO: Course Description Title

TODO: Write a description of {course_id.upper()} here. This section appears before the first part separator.

+++

# Part 1 — TODO: Part Title

<partId>{uuid.uuid4()}</partId>

## Chapter 1 — TODO: Chapter Title

<chapterId>{uuid.uuid4()}</chapterId>

TODO: Write chapter content here.
"""


# --- Interactive prompts ---

def prompt_course_id(registry) -> str:
    """Interactively prompt for a valid course ID."""
    codes = ", ".join(f"{k} ({v})" for k, v in sorted(registry.discipline_codes.items()))
    click.echo(f"\nDiscipline codes: {codes}")
    click.echo(f"Number range: {registry.level_range['min']}-{registry.level_range['max']}")

    while True:
        course_id = click.prompt("Course ID (e.g., btc101)").strip().lower()
        err = validate_course_id(course_id, registry)
        if err:
            click.echo(f"Error: {err}", err=True)
            continue
        return course_id


def prompt_enum(field_name: str, choices: list[str], default: str | None = None) -> str:
    """Prompt user to pick from enum values."""
    click.echo(f"\n{field_name} options: {', '.join(choices)}")
    while True:
        value = click.prompt(field_name, default=default or "").strip().lower()
        if value in choices:
            return value
        click.echo(f"Invalid. Choose from: {', '.join(choices)}", err=True)


def prompt_language(registry) -> str:
    """Prompt for a valid language code."""
    click.echo(f"\nLanguages: {', '.join(registry.languages)}")
    while True:
        lang = click.prompt("Language", default="en").strip()
        if lang in registry.languages:
            return lang
        click.echo(f"Invalid language. Choose from: {', '.join(registry.languages)}", err=True)


def prompt_professor_id() -> str:
    """Prompt for a professor UUID."""
    while True:
        pid = click.prompt("Professor ID (UUID)").strip()
        uuid_re = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
        if uuid_re.match(pid):
            return pid
        click.echo("Invalid UUID format. Expected: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", err=True)


# --- Main command logic ---

def run_new_course(
    course_id: str | None,
    topic: str | None,
    subtopic: str | None,
    level: str | None,
    lang: str | None,
    professor_id: str | None,
    json_output: bool,
) -> None:
    """Create a new course scaffold."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    # Load schema for enum introspection
    schema_path = repo_root / registry.content_types["course"].schema
    schema = load_json_schema(schema_path)

    topics = get_enum_values(schema, "topic")
    subtopics = get_enum_values(schema, "subtopic")
    levels = get_enum_values(schema, "level")

    # Interactive fallback for missing args
    if course_id is None:
        course_id = prompt_course_id(registry)
    else:
        course_id = course_id.strip().lower()
        err = validate_course_id(course_id, registry)
        if err:
            click.echo(f"Error: {err}", err=True)
            raise SystemExit(1)

    if topic is None:
        topic = prompt_enum("topic", topics)
    elif topic not in topics:
        click.echo(f"Error: invalid topic '{topic}'. Allowed: {', '.join(topics)}", err=True)
        raise SystemExit(1)

    if subtopic is None:
        subtopic = prompt_enum("subtopic", subtopics, default=topic)
    elif subtopic not in subtopics:
        click.echo(f"Error: invalid subtopic '{subtopic}'. Allowed: {', '.join(subtopics)}", err=True)
        raise SystemExit(1)

    if level is None:
        # Infer default from course number
        default_level = level_from_number(int(course_id[3:]), registry)
        level = prompt_enum("level", levels, default=default_level)
    elif level not in levels:
        click.echo(f"Error: invalid level '{level}'. Allowed: {', '.join(levels)}", err=True)
        raise SystemExit(1)

    if lang is None:
        lang = prompt_language(registry)
    elif lang not in registry.languages:
        click.echo(f"Error: invalid language '{lang}'. Allowed: {', '.join(registry.languages)}", err=True)
        raise SystemExit(1)

    if professor_id is None:
        professor_id = prompt_professor_id()
    else:
        uuid_re = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
        if not uuid_re.match(professor_id):
            click.echo(f"Error: invalid professor ID '{professor_id}'. Must be a UUID.", err=True)
            raise SystemExit(1)

    # Check if course directory already exists
    course_dir = repo_root / "courses" / course_id
    if course_dir.exists():
        click.echo(f"Error: course directory already exists: {course_dir}", err=True)
        raise SystemExit(1)

    # Generate UUID for course
    course_uuid = str(uuid.uuid4())

    # Build files
    course_yml_data = build_course_yml(
        course_uuid=course_uuid,
        topic=topic,
        subtopic=subtopic,
        level=level,
        lang=lang,
        professor_id=professor_id,
    )
    course_md_content = build_course_md(course_id, lang)

    # Write files
    course_dir.mkdir(parents=True)
    yml_path = course_dir / "course.yml"
    md_path = course_dir / f"{lang}.md"
    assets_dir = course_dir / "assets"
    assets_dir.mkdir()

    dump_yaml(course_yml_data, yml_path)
    md_path.write_text(course_md_content, encoding="utf-8")

    created_files = [
        str(yml_path.relative_to(repo_root)),
        str(md_path.relative_to(repo_root)),
        str(assets_dir.relative_to(repo_root)) + "/",
    ]

    if json_output:
        click.echo(json.dumps({
            "course_id": course_id,
            "uuid": course_uuid,
            "directory": str(course_dir.relative_to(repo_root)),
            "files": created_files,
        }, indent=2))
    else:
        click.echo(f"Created course '{course_id}' at {course_dir.relative_to(repo_root)}/")
        click.echo(f"  UUID: {course_uuid}")
        for f in created_files:
            click.echo(f"  - {f}")
        click.echo("\nNext steps:")
        click.echo(f"  1. Edit {yml_path.relative_to(repo_root)} — fill in contributor_names, tags")
        click.echo(f"  2. Edit {md_path.relative_to(repo_root)} — write course content")
        click.echo(f"  3. Add thumbnail to {assets_dir.relative_to(repo_root)}/thumbnail.webp")
        click.echo(f"  4. Run: bec validate courses/{course_id}")
