"""Scaffold new content items."""

from __future__ import annotations

import json
import re
import uuid
from datetime import date, datetime
from pathlib import Path

import click

from bec.lib.content_types import ContentRegistry, load_registry
from bec.lib.repo import find_repo_root
from bec.lib.schema import load_json_schema
from bec.lib.yaml_utils import dump_yaml

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

# Minimal 1x1 WebP placeholder (40 bytes) for scaffold cover images
import base64 as _b64
_PLACEHOLDER_WEBP = _b64.b64decode(
    b"UklGRiAAAABXRUJQVlA4IBMAAAAwAQCdASoBAAEAAUAlpAADcAAAAA=="
)

# Resource type keys that live under resources/
RESOURCE_TYPE_KEYS = frozenset({
    "bet", "book", "channel", "conference", "glossary",
    "movie", "newsletter", "paper", "podcast", "project",
})

# --- Shared helpers ---


def _make_proofreading_entry(lang: str) -> dict:
    """Build a single proofreading entry for a language."""
    return {
        "language": lang,
        "last_contribution_date": date.today().strftime("%Y-%m-%d"),
        "urgency": 1,
        "contributor_names": ["TODO"],
        "reward": 0,
    }


def _validate_uuid(value: str) -> bool:
    return bool(UUID_RE.match(value))


def _validate_slug(value: str) -> str | None:
    """Validate a content slug ID. Returns error message or None."""
    if not re.match(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$", value) and len(value) > 1:
        return f"Invalid ID '{value}'. Use lowercase letters, digits, and hyphens (e.g., my-content-name)."
    if len(value) < 2:
        return f"ID '{value}' is too short. Minimum 2 characters."
    return None


def _prompt_slug(label: str) -> str:
    """Prompt for a valid slug ID."""
    while True:
        value = click.prompt(f"{label} ID (slug)").strip().lower()
        err = _validate_slug(value)
        if err:
            click.echo(f"Error: {err}", err=True)
            continue
        return value


def _dir_from_path_pattern(path_pattern: str, **kwargs: str) -> str:
    """Resolve a path_pattern with the given placeholders."""
    result = path_pattern.rstrip("/")
    for key, val in kwargs.items():
        result = result.replace(f"{{{key}}}", val)
    return result


def _scaffold_output(
    content_type: str,
    content_id: str,
    content_uuid: str,
    content_dir: Path,
    created_files: list[str],
    repo_root: Path,
    json_output: bool,
    extra_json: dict | None = None,
) -> None:
    """Print creation output in human or JSON format."""
    if json_output:
        data = {
            "type": content_type,
            "id": content_id,
            "uuid": content_uuid,
            "directory": str(content_dir.relative_to(repo_root)),
            "files": created_files,
        }
        if extra_json:
            data.update(extra_json)
        click.echo(json.dumps(data, indent=2))
    else:
        click.echo(f"Created {content_type} '{content_id}' at {content_dir.relative_to(repo_root)}/")
        click.echo(f"  UUID: {content_uuid}")
        for f in created_files:
            click.echo(f"  - {f}")
        click.echo(f"\nNext: bec validate {content_dir.relative_to(repo_root)}")


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
        "tags": ["software"],
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


def prompt_uuid(label: str = "Professor ID") -> str:
    """Prompt for a valid UUID."""
    while True:
        pid = click.prompt(f"{label} (UUID)").strip()
        if _validate_uuid(pid):
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
        professor_id = prompt_uuid("Professor ID")
    else:
        if not _validate_uuid(professor_id):
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


# ========================================================================
# Tutorial scaffolding
# ========================================================================


def build_tutorial_yml(
    tutorial_uuid: str,
    level: str,
    schema_category: str,
    professor_id: str,
    license_type: str,
    lang: str,
) -> dict:
    """Build the tutorial.yml data dict."""
    return {
        "id": tutorial_uuid,
        "level": level,
        "category": schema_category,
        "professor_id": professor_id,
        "license": license_type,
        "original_language": lang,
        "proofreading": [_make_proofreading_entry(lang)],
        "tags": ["software"],
    }


def build_tutorial_md(tutorial_id: str) -> str:
    """Build the tutorial markdown content with frontmatter."""
    return f"""---
name: "TODO: Tutorial Title"
description: "TODO: Describe {tutorial_id} in one sentence"
---
![cover](assets/cover.webp)

## Introduction

TODO: Write tutorial content here.
"""


def run_new_tutorial(
    folder_category: str | None,
    tutorial_id: str | None,
    lang: str | None,
    level: str | None,
    professor_id: str | None,
    license_type: str | None,
    schema_category: str | None,
    json_output: bool,
) -> None:
    """Create a new tutorial scaffold."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    # Load schema for enum introspection
    schema_path = repo_root / registry.content_types["tutorial"].schema
    schema = load_json_schema(schema_path)
    levels = get_enum_values(schema, "level")
    categories_schema = get_enum_values(schema, "category")
    licenses = get_enum_values(schema, "license")

    valid_folder_categories = registry.tutorial_categories

    # --- Validate / prompt folder category ---
    if folder_category is None:
        click.echo(f"\nTutorial folder categories: {', '.join(valid_folder_categories)}")
        while True:
            folder_category = click.prompt("Folder category").strip().lower()
            if folder_category in valid_folder_categories:
                break
            click.echo(f"Invalid. Choose from: {', '.join(valid_folder_categories)}", err=True)
    elif folder_category not in valid_folder_categories:
        click.echo(
            f"Error: invalid tutorial category '{folder_category}'. "
            f"Valid categories: {', '.join(valid_folder_categories)}",
            err=True,
        )
        raise SystemExit(1)

    # --- Validate / prompt ID ---
    if tutorial_id is None:
        tutorial_id = _prompt_slug("Tutorial")
    else:
        tutorial_id = tutorial_id.strip().lower()
        err = _validate_slug(tutorial_id)
        if err:
            click.echo(f"Error: {err}", err=True)
            raise SystemExit(1)

    # Check duplicate
    tuto_dir = repo_root / "tutorials" / folder_category / tutorial_id
    if tuto_dir.exists():
        click.echo(f"Error: tutorial directory already exists: {tuto_dir}", err=True)
        raise SystemExit(1)

    # --- Validate / prompt remaining fields ---
    if lang is None:
        lang = prompt_language(registry)
    elif lang not in registry.languages:
        click.echo(f"Error: invalid language '{lang}'. Allowed: {', '.join(registry.languages)}", err=True)
        raise SystemExit(1)

    if level is None:
        level = prompt_enum("level", levels, default="beginner")
    elif level not in levels:
        click.echo(f"Error: invalid level '{level}'. Allowed: {', '.join(levels)}", err=True)
        raise SystemExit(1)

    if professor_id is None:
        professor_id = prompt_uuid("Professor ID")
    elif not _validate_uuid(professor_id):
        click.echo(f"Error: invalid professor ID '{professor_id}'. Must be a UUID.", err=True)
        raise SystemExit(1)

    if license_type is None:
        license_type = prompt_enum("license", licenses, default="CC-BY-SA-V4")
    elif license_type not in licenses:
        click.echo(f"Error: invalid license '{license_type}'. Allowed: {', '.join(licenses)}", err=True)
        raise SystemExit(1)

    if schema_category is None:
        schema_category = prompt_enum("tool category", categories_schema, default="desktop")
    elif schema_category not in categories_schema:
        click.echo(
            f"Error: invalid tool category '{schema_category}'. "
            f"Allowed: {', '.join(categories_schema)}",
            err=True,
        )
        raise SystemExit(1)

    # Generate
    tuto_uuid = str(uuid.uuid4())
    tuto_yml_data = build_tutorial_yml(
        tutorial_uuid=tuto_uuid,
        level=level,
        schema_category=schema_category,
        professor_id=professor_id,
        license_type=license_type,
        lang=lang,
    )
    tuto_md = build_tutorial_md(tutorial_id)

    # Write files
    tuto_dir.mkdir(parents=True)
    yml_path = tuto_dir / "tutorial.yml"
    md_path = tuto_dir / f"{lang}.md"
    assets_dir = tuto_dir / "assets"
    assets_dir.mkdir()

    dump_yaml(tuto_yml_data, yml_path)
    md_path.write_text(tuto_md, encoding="utf-8")
    # Placeholder cover so scaffold passes validation
    (assets_dir / "cover.webp").write_bytes(_PLACEHOLDER_WEBP)

    created_files = [
        str(yml_path.relative_to(repo_root)),
        str(md_path.relative_to(repo_root)),
        str(assets_dir.relative_to(repo_root)) + "/",
    ]

    _scaffold_output(
        content_type="tutorial",
        content_id=tutorial_id,
        content_uuid=tuto_uuid,
        content_dir=tuto_dir,
        created_files=created_files,
        repo_root=repo_root,
        json_output=json_output,
        extra_json={"folder_category": folder_category},
    )


# ========================================================================
# Professor scaffolding
# ========================================================================


def build_professor_yml(professor_uuid: str, name: str) -> dict:
    """Build the professor.yml data dict."""
    return {
        "id": professor_uuid,
        "name": name,
        "links": {
            "twitter": "https://twitter.com/TODO",
        },
        "tags": ["software"],
    }


def build_professor_lang_yml() -> dict:
    """Build a professor language YML (e.g., en.yml)."""
    return {
        "bio": "TODO: Write professor bio here.\n",
        "short_bio": "TODO: Short bio",
    }


def run_new_professor(
    professor_slug: str | None,
    name: str | None,
    lang: str | None,
    json_output: bool,
) -> None:
    """Create a new professor profile scaffold."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if professor_slug is None:
        professor_slug = _prompt_slug("Professor")
    else:
        professor_slug = professor_slug.strip().lower()
        err = _validate_slug(professor_slug)
        if err:
            click.echo(f"Error: {err}", err=True)
            raise SystemExit(1)

    prof_dir = repo_root / "professors" / professor_slug
    if prof_dir.exists():
        click.echo(f"Error: professor directory already exists: {prof_dir}", err=True)
        raise SystemExit(1)

    if name is None:
        name = click.prompt("Display name").strip()
    if not name:
        click.echo("Error: name cannot be empty.", err=True)
        raise SystemExit(1)

    if lang is None:
        lang = prompt_language(registry)
    elif lang not in registry.languages:
        click.echo(f"Error: invalid language '{lang}'. Allowed: {', '.join(registry.languages)}", err=True)
        raise SystemExit(1)

    prof_uuid = str(uuid.uuid4())
    prof_yml = build_professor_yml(prof_uuid, name)
    lang_yml = build_professor_lang_yml()

    prof_dir.mkdir(parents=True)
    yml_path = prof_dir / "professor.yml"
    lang_path = prof_dir / f"{lang}.yml"
    assets_dir = prof_dir / "assets"
    assets_dir.mkdir()

    dump_yaml(prof_yml, yml_path)
    dump_yaml(lang_yml, lang_path)

    created_files = [
        str(yml_path.relative_to(repo_root)),
        str(lang_path.relative_to(repo_root)),
        str(assets_dir.relative_to(repo_root)) + "/",
    ]

    _scaffold_output(
        content_type="professor",
        content_id=professor_slug,
        content_uuid=prof_uuid,
        content_dir=prof_dir,
        created_files=created_files,
        repo_root=repo_root,
        json_output=json_output,
    )


# ========================================================================
# Event scaffolding
# ========================================================================

EVENT_TYPES = ["workshop", "course", "conference", "lecture", "meetup"]


def build_event_yml(
    event_uuid: str,
    name: str,
    event_type: str,
    start_date: str,
    end_date: str,
    timezone: str,
    city: str,
    lang: str,
) -> dict:
    """Build the event.yml data dict."""
    return {
        "id": event_uuid,
        "name": name,
        "type": event_type,
        "start_date": start_date,
        "end_date": end_date,
        "timezone": timezone,
        "address_city_country": city,
        "description": "TODO: Event description",
        "language": [lang],
        "links": {
            "website": "TODO: https://example.com",
            "replay_url": None,
            "live_url": None,
        },
        "tags": ["software"],
        "book_online": False,
        "book_in_person": False,
        "price_dollars": 0,
    }


def run_new_event(
    event_id: str | None,
    name: str | None,
    event_type: str | None,
    start_date: str | None,
    end_date: str | None,
    timezone: str | None,
    city: str | None,
    lang: str | None,
    json_output: bool,
) -> None:
    """Create a new event scaffold."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if event_id is None:
        event_id = _prompt_slug("Event")
    else:
        event_id = event_id.strip().lower()
        err = _validate_slug(event_id)
        if err:
            click.echo(f"Error: {err}", err=True)
            raise SystemExit(1)

    event_dir = repo_root / "events" / event_id
    if event_dir.exists():
        click.echo(f"Error: event directory already exists: {event_dir}", err=True)
        raise SystemExit(1)

    if name is None:
        name = click.prompt("Event name").strip()
    if not name:
        click.echo("Error: name cannot be empty.", err=True)
        raise SystemExit(1)

    if event_type is None:
        event_type = prompt_enum("type", EVENT_TYPES, default="meetup")
    elif event_type not in EVENT_TYPES:
        click.echo(f"Error: invalid event type '{event_type}'. Allowed: {', '.join(EVENT_TYPES)}", err=True)
        raise SystemExit(1)

    if start_date is None:
        start_date = click.prompt("Start date (YYYY-MM-DD HH:MM:SS)", default="2025-01-01 09:00:00").strip()
    if end_date is None:
        end_date = click.prompt("End date (YYYY-MM-DD HH:MM:SS)", default="2025-01-01 17:00:00").strip()
    if timezone is None:
        timezone = click.prompt("Timezone (IANA)", default="UTC").strip()
    if city is None:
        city = click.prompt("City, Country").strip()
    if not city:
        click.echo("Error: city cannot be empty.", err=True)
        raise SystemExit(1)

    if lang is None:
        lang = prompt_language(registry)
    elif lang not in registry.languages:
        click.echo(f"Error: invalid language '{lang}'. Allowed: {', '.join(registry.languages)}", err=True)
        raise SystemExit(1)

    event_uuid = str(uuid.uuid4())
    event_yml = build_event_yml(
        event_uuid=event_uuid,
        name=name,
        event_type=event_type,
        start_date=start_date,
        end_date=end_date,
        timezone=timezone,
        city=city,
        lang=lang,
    )

    event_dir.mkdir(parents=True)
    yml_path = event_dir / "event.yml"
    assets_dir = event_dir / "assets"
    assets_dir.mkdir()

    dump_yaml(event_yml, yml_path)

    created_files = [
        str(yml_path.relative_to(repo_root)),
        str(assets_dir.relative_to(repo_root)) + "/",
    ]

    _scaffold_output(
        content_type="event",
        content_id=event_id,
        content_uuid=event_uuid,
        content_dir=event_dir,
        created_files=created_files,
        repo_root=repo_root,
        json_output=json_output,
    )


# ========================================================================
# Resource scaffolding
# ========================================================================


def _resource_dir_prefix(registry: ContentRegistry, resource_type: str) -> str:
    """Get the directory prefix for a resource type (e.g., 'resources/books')."""
    ct = registry.content_types[resource_type]
    # path_pattern like "resources/books/{id}/" -> "resources/books"
    return ct.path_pattern.split("/{id}")[0]


def _build_resource_metadata(resource_type: str, resource_uuid: str, lang: str) -> dict:
    """Build metadata YAML dict for a given resource type."""
    today = date.today().strftime("%Y-%m-%d")

    builders = {
        "bet": lambda: {
            "id": resource_uuid,
            "type": "Educational Content",
            "contributor_names": ["TODO"],
            "original_language": lang,
            "proofreading": [_make_proofreading_entry(lang)],
            "tags": ["software"],
            "license": "CC-BY-SA-V4",
        },
        "book": lambda: {
            "author": "TODO: Author Name",
            "level": "beginner",
            "tags": ["software"],
            "original_language": lang,
        },
        "channel": lambda: {
            "id": resource_uuid,
            "name": "TODO: Channel Name",
            "language": lang,
            "links": {"channel": "TODO: https://youtube.com/..."},
            "description": "TODO: Channel description\n",
            "tags": ["software"],
            "contributor_names": ["TODO"],
        },
        "conference": lambda: {
            "name": "TODO: Conference Name 2025",
            "year": today[:7],
            "builder": "TODO: Builder Name",
            "location": "TODO: City, Country",
            "language": [lang],
            "links": {"website": "TODO: https://example.com"},
            "tags": ["software"],
        },
        "glossary": lambda: {
            "id": resource_uuid,
            "en_word": "TODO",
            "original_language": lang,
            "proofreading": [_make_proofreading_entry(lang)],
        },
        "movie": lambda: {
            "id": resource_uuid,
            "title": "TODO: Movie Title",
            "author": "TODO: Director Name",
            "publication_year": date.today().year,
            "duration": 90,
            "language": lang,
            "links": {"platform": "TODO: https://example.com"},
            "description": "TODO: Movie description\n",
            "contributor_names": ["TODO"],
            "tags": ["software"],
        },
        "newsletter": lambda: {
            "id": resource_uuid,
            "title": "TODO: Newsletter Title",
            "author": "TODO: Author Name",
            "level": "beginner",
            "publication_date": today,
            "link": [{"website": "TODO: https://example.com"}],
            "language": lang,
            "description": "TODO: Newsletter description\n",
            "contributor_names": ["TODO"],
            "tags": ["software"],
        },
        "paper": lambda: {
            "id": resource_uuid,
            "title": "TODO: Paper Title",
            "original_language": lang,
            "authors": ["TODO: Author Name"],
            "abstract": "TODO: Paper abstract describing the research.",
            "paper_type": "whitepaper",
            "topics": ["bitcoin"],
            "pdf_url": "TODO: https://example.com/paper.pdf",
        },
        "podcast": lambda: {
            "id": resource_uuid,
            "name": "TODO: Podcast Name",
            "host": "TODO: Host Name",
            "language": lang,
            "links": {"podcast": "TODO: https://example.com"},
            "description": "TODO: Podcast description\n",
            "tags": ["software"],
            "contributor_names": ["TODO"],
        },
        "project": lambda: {
            "id": resource_uuid,
            "name": "TODO: Project Name",
            "category": "education",
            "links": {"website": "TODO: https://example.com"},
            "original_language": lang,
            "proofreading": [_make_proofreading_entry(lang)],
        },
    }
    return builders[resource_type]()


def _build_resource_content(resource_type: str, lang: str) -> dict | str | None:
    """Build language content file for resource types that need one.

    Returns dict for YML content, str for MD content, None if no content needed.
    """
    builders = {
        "bet": lambda: {
            "name": "TODO: Content Name",
            "description": "TODO: Content description\n",
        },
        "book": lambda: {
            "title": "TODO: Book Title",
            "publication_year": date.today().year,
            "cover": f"cover_{lang}.webp",
            "original": True,
            "description": "TODO: Book description\n",
        },
        "glossary": lambda: f"""---
term: "TODO: Term"
definition: "TODO: Definition of the glossary word"
---

TODO: Extended definition and explanation of this term.
""",
        "project": lambda: {
            "description": "TODO: Project description\n",
        },
    }
    builder = builders.get(resource_type)
    return builder() if builder else None


def run_new_resource(
    resource_type: str | None,
    resource_id: str | None,
    lang: str | None,
    json_output: bool,
) -> None:
    """Create a new resource scaffold."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    # --- Validate / prompt resource type ---
    valid_types = sorted(RESOURCE_TYPE_KEYS)
    if resource_type is None:
        resource_type = prompt_enum("resource type", valid_types)
    elif resource_type not in RESOURCE_TYPE_KEYS:
        click.echo(
            f"Error: invalid resource type '{resource_type}'. "
            f"Valid types: {', '.join(valid_types)}",
            err=True,
        )
        raise SystemExit(1)

    # --- Validate / prompt ID ---
    if resource_id is None:
        resource_id = _prompt_slug("Resource")
    else:
        resource_id = resource_id.strip().lower()
        err = _validate_slug(resource_id)
        if err:
            click.echo(f"Error: {err}", err=True)
            raise SystemExit(1)

    # Resolve directory
    dir_prefix = _resource_dir_prefix(registry, resource_type)
    resource_dir = repo_root / dir_prefix / resource_id
    if resource_dir.exists():
        click.echo(f"Error: resource directory already exists: {resource_dir}", err=True)
        raise SystemExit(1)

    if lang is None:
        lang = prompt_language(registry)
    elif lang not in registry.languages:
        click.echo(f"Error: invalid language '{lang}'. Allowed: {', '.join(registry.languages)}", err=True)
        raise SystemExit(1)

    resource_uuid = str(uuid.uuid4())
    metadata = _build_resource_metadata(resource_type, resource_uuid, lang)
    content = _build_resource_content(resource_type, lang)

    # Write files
    resource_dir.mkdir(parents=True)
    meta_filename = registry.content_types[resource_type].metadata_file
    yml_path = resource_dir / meta_filename
    dump_yaml(metadata, yml_path)

    created_files = [str(yml_path.relative_to(repo_root))]

    # Write content file if applicable
    if content is not None:
        ct = registry.content_types[resource_type]
        if isinstance(content, str):
            # Markdown content
            content_path = resource_dir / f"{lang}.md"
            content_path.write_text(content, encoding="utf-8")
        else:
            # YML content
            content_path = resource_dir / f"{lang}.yml"
            dump_yaml(content, content_path)
        created_files.append(str(content_path.relative_to(repo_root)))

    assets_dir = resource_dir / "assets"
    assets_dir.mkdir()
    created_files.append(str(assets_dir.relative_to(repo_root)) + "/")

    _scaffold_output(
        content_type=f"resource/{resource_type}",
        content_id=resource_id,
        content_uuid=resource_uuid,
        content_dir=resource_dir,
        created_files=created_files,
        repo_root=repo_root,
        json_output=json_output,
        extra_json={"resource_type": resource_type},
    )
