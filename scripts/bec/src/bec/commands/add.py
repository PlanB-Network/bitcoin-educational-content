"""Add content parts to existing course files (part, chapter, quiz, language)."""

from __future__ import annotations

import json
import re
import uuid
from datetime import date
from pathlib import Path

import click

from bec.lib.content_types import load_registry
from bec.lib.markdown import (
    append_to_markdown,
    build_chapter_block,
    build_part_block,
    generate_chapter_id,
)
from bec.lib.repo import find_repo_root
from bec.lib.yaml_utils import dump_yaml


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


# --- Quiz ---


def _next_quiz_number(quizz_dir: Path) -> int:
    """Find the next quiz number by scanning existing quizz/{nnn}/ folders."""
    if not quizz_dir.is_dir():
        return 0
    existing = []
    for d in quizz_dir.iterdir():
        if d.is_dir() and re.match(r"^\d{3}$", d.name):
            existing.append(int(d.name))
    return max(existing) + 1 if existing else 0


def _list_chapter_ids(course_id: str, repo_root: Path) -> list[str]:
    """Extract all chapterIds from course markdown files."""
    course_dir = repo_root / "courses" / course_id
    if not course_dir.is_dir():
        return []
    chapter_ids = []
    for md_path in sorted(course_dir.glob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        chapter_ids.extend(re.findall(r"<chapterId>(.+?)</chapterId>", text))
    # Deduplicate while preserving order
    seen = set()
    result = []
    for cid in chapter_ids:
        if cid not in seen:
            seen.add(cid)
            result.append(cid)
    return result


def run_add_quiz(
    course: str | None,
    chapter_id: str | None,
    lang: str | None,
    difficulty: str | None,
    author: str | None,
    json_output: bool,
) -> None:
    """Add a quiz question folder to a course."""
    repo_root = find_repo_root()

    # Interactive prompts for missing args
    if not course:
        ids = _list_course_ids(repo_root)
        if ids:
            click.echo(f"Available courses: {', '.join(ids)}")
        course = click.prompt("Course ID")

    course_dir = repo_root / "courses" / course
    if not course_dir.is_dir():
        raise click.ClickException(f"Course not found: courses/{course}")

    if not chapter_id:
        cids = _list_chapter_ids(course, repo_root)
        if cids:
            click.echo(f"Available chapterIds: {', '.join(cids)}")
        chapter_id = click.prompt("Chapter ID")

    if not lang:
        langs = _list_course_langs(course, repo_root)
        if langs:
            click.echo(f"Available languages: {', '.join(langs)}")
        lang = click.prompt("Language code", default="en")

    valid_difficulties = ["easy", "intermediate", "hard", "expert"]
    if not difficulty:
        difficulty = click.prompt(
            f"Difficulty ({', '.join(valid_difficulties)})", default="easy"
        )
    if difficulty not in valid_difficulties:
        raise click.ClickException(
            f"Invalid difficulty '{difficulty}'. Choose from: {', '.join(valid_difficulties)}"
        )

    if not author:
        author = click.prompt("Author (contributor ID)", default="TODO")

    # Find next quiz number
    quizz_dir = course_dir / "quizz"
    next_num = _next_quiz_number(quizz_dir)
    quiz_folder_name = f"{next_num:03d}"
    quiz_dir = quizz_dir / quiz_folder_name

    # Create quiz folder
    quiz_dir.mkdir(parents=True)

    # Build question.yml
    question_uuid = str(uuid.uuid4())
    question_data = {
        "chapterId": chapter_id,
        "difficulty": difficulty,
        "author": author,
        "tags": ["software"],
    }
    question_path = quiz_dir / "question.yml"
    dump_yaml(question_data, question_path)

    # Build language translation file
    translation_data = {
        "question": "TODO: Write the question text",
        "answer": "TODO: Write the correct answer",
        "wrong_answers": [
            "TODO: First wrong answer",
            "TODO: Second wrong answer",
            "TODO: Third wrong answer",
        ],
        "explanation": "TODO: Explain why the answer is correct.\n",
        "reviewed": False,
    }
    translation_path = quiz_dir / f"{lang}.yml"
    dump_yaml(translation_data, translation_path)

    created_files = [
        str(question_path.relative_to(repo_root)),
        str(translation_path.relative_to(repo_root)),
    ]

    if json_output:
        click.echo(json.dumps({
            "action": "add_quiz",
            "course": course,
            "quiz_number": quiz_folder_name,
            "chapter_id": chapter_id,
            "lang": lang,
            "difficulty": difficulty,
            "directory": str(quiz_dir.relative_to(repo_root)),
            "files": created_files,
        }, indent=2))
    else:
        click.echo(f"Created quiz {quiz_folder_name} in courses/{course}/quizz/")
        click.echo(f"  chapterId: {chapter_id}")
        click.echo(f"  difficulty: {difficulty}")
        for f in created_files:
            click.echo(f"  - {f}")


# --- Language ---


def _detect_content_path(path_str: str, repo_root: Path) -> tuple[Path, str]:
    """Resolve a content path and detect its type.

    Returns (content_dir, content_type_key).
    Raises click.ClickException on invalid paths.
    """
    content_dir = (repo_root / path_str).resolve()
    if not content_dir.is_dir():
        raise click.ClickException(f"Content directory not found: {path_str}")

    registry = load_registry(repo_root)
    ct = registry.detect_type_from_path(content_dir, repo_root)
    if ct is None:
        raise click.ClickException(f"Cannot detect content type for: {path_str}")
    return content_dir, ct.key


def _find_source_lang(content_dir: Path) -> str | None:
    """Find the first available language file (md or yml) in a content directory."""
    # Prefer en if available
    if (content_dir / "en.md").is_file():
        return "en"
    if (content_dir / "en.yml").is_file():
        return "en"
    # Otherwise pick the first .md or .yml that looks like a language code
    for f in sorted(content_dir.iterdir()):
        if f.suffix == ".md" and re.match(r"^[a-z]{2}$", f.stem):
            return f.stem
        if f.suffix == ".yml" and re.match(r"^[a-z]{2}$", f.stem):
            return f.stem
    return None


def _create_language_md(
    source_path: Path, target_path: Path, target_lang: str
) -> None:
    """Create a new language markdown file from a source.

    Preserves: frontmatter keys, heading structure, chapterId/partId tags,
    +++ separators. Replaces: prose content with TODO placeholders,
    frontmatter values with TODO.
    """
    source_text = source_path.read_text(encoding="utf-8")

    # Split frontmatter from body
    if source_text.startswith("---\n"):
        end_idx = source_text.index("\n---\n", 4)
        frontmatter_block = source_text[4:end_idx]
        body = source_text[end_idx + 5:]
    else:
        frontmatter_block = ""
        body = source_text

    # Replace frontmatter values with TODO
    new_fm_lines = []
    for line in frontmatter_block.splitlines():
        if line.startswith("  - "):
            # List item — replace value with TODO
            new_fm_lines.append('  - "TODO"')
        elif ":" in line and not line.startswith(" "):
            key = line.split(":", 1)[0]
            value = line.split(":", 1)[1].strip()
            if value and value != "|":
                new_fm_lines.append(f'{key}: "TODO"')
            else:
                new_fm_lines.append(line)
        else:
            new_fm_lines.append(line)

    # Process body: preserve structure, replace prose with TODO
    new_body_lines = []
    for line in body.splitlines():
        # Preserve part separators
        if line.strip() == "+++":
            new_body_lines.append(line)
        # Preserve heading structure
        elif line.startswith("#"):
            new_body_lines.append(line.split(" ", 1)[0] + " TODO")
        # Preserve chapterId/partId tags
        elif "<chapterId>" in line or "<partId>" in line:
            new_body_lines.append(line)
        # Preserve image references (just update lang path if needed)
        elif line.strip().startswith("!["):
            new_body_lines.append(line)
        # Preserve empty lines
        elif not line.strip():
            new_body_lines.append("")
        # Preserve video embeds and other special tags
        elif line.strip().startswith(":::") or line.strip().startswith("<"):
            new_body_lines.append(line)
        else:
            # Replace prose with TODO
            new_body_lines.append("TODO")

    new_frontmatter = "\n".join(new_fm_lines)
    new_body = "\n".join(new_body_lines)

    if new_frontmatter:
        result = f"---\n{new_frontmatter}\n---\n{new_body}\n"
    else:
        result = f"{new_body}\n"

    target_path.write_text(result, encoding="utf-8")


def _create_language_yml(
    source_path: Path, target_path: Path
) -> None:
    """Create a new language YML file from a source.

    Replaces string values with TODO, preserves structure.
    """
    from bec.lib.yaml_utils import load_yaml

    data = load_yaml(source_path)
    if data is None:
        data = {}

    def _replace_values(obj):
        if isinstance(obj, dict):
            return {k: _replace_values(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [_replace_values(item) for item in obj]
        elif isinstance(obj, str):
            return "TODO"
        elif isinstance(obj, bool):
            return obj
        elif isinstance(obj, (int, float)):
            return obj
        return obj

    new_data = _replace_values(data)
    dump_yaml(new_data, target_path)


def run_add_language(
    content_path: str | None,
    lang: str | None,
    json_output: bool,
) -> None:
    """Add a new language file to existing content."""
    repo_root = find_repo_root()

    if not content_path:
        content_path = click.prompt("Content path (e.g., courses/btc101)")

    content_dir, ct_key = _detect_content_path(content_path, repo_root)
    rel_dir = str(content_dir.relative_to(repo_root))

    registry = load_registry(repo_root)

    if not lang:
        click.echo(f"Available languages: {', '.join(registry.languages)}")
        lang = click.prompt("Target language code")

    if lang not in registry.languages:
        raise click.ClickException(
            f"Invalid language '{lang}'. Choose from: {', '.join(registry.languages)}"
        )

    # Find source language to copy structure from
    source_lang = _find_source_lang(content_dir)
    if source_lang is None:
        raise click.ClickException(
            f"No source language file found in {rel_dir}. "
            "Need at least one existing language file to copy structure from."
        )

    created_files = []

    # Determine file type (md or yml) based on source
    source_md = content_dir / f"{source_lang}.md"
    source_yml = content_dir / f"{source_lang}.yml"

    if source_md.is_file():
        target_md = content_dir / f"{lang}.md"
        if target_md.exists():
            raise click.ClickException(
                f"Language file already exists: {target_md.relative_to(repo_root)}"
            )
        _create_language_md(source_md, target_md, lang)
        created_files.append(str(target_md.relative_to(repo_root)))

    if source_yml.is_file():
        target_yml = content_dir / f"{lang}.yml"
        if target_yml.exists():
            raise click.ClickException(
                f"Language file already exists: {target_yml.relative_to(repo_root)}"
            )
        _create_language_yml(source_yml, target_yml)
        created_files.append(str(target_yml.relative_to(repo_root)))

    if not created_files:
        raise click.ClickException(
            f"No language file found for '{source_lang}' in {rel_dir}"
        )

    if json_output:
        click.echo(json.dumps({
            "action": "add_language",
            "content_path": rel_dir,
            "content_type": ct_key,
            "source_lang": source_lang,
            "target_lang": lang,
            "files": created_files,
        }, indent=2))
    else:
        click.echo(f"Added language '{lang}' to {rel_dir} (from '{source_lang}')")
        for f in created_files:
            click.echo(f"  - {f}")
