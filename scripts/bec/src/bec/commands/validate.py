"""bec validate — validate content against JSON schemas."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import click

from bec.lib.content_types import ContentRegistry, ContentType, load_registry
from bec.lib.repo import find_repo_root, resolve_content_path
from bec.lib.schema import (
    ValidationResult,
    load_json_schema,
    validate_markdown_frontmatter,
    validate_yaml_against_schema,
    validate_yml_content,
)
from bec.lib.yaml_utils import load_yaml

# ANSI codes
_RED = "\033[91m"
_GREEN = "\033[92m"
_YELLOW = "\033[93m"
_CYAN = "\033[96m"
_BOLD = "\033[1m"
_END = "\033[0m"


def _validate_folder(
    folder: Path,
    registry: ContentRegistry,
    repo_root: Path,
) -> list[ValidationResult]:
    """Validate a single content folder. Returns a list of results."""
    if not folder.exists():
        r = ValidationResult(path=str(folder))
        r.add_error("Folder does not exist")
        return [r]

    if not folder.is_dir():
        r = ValidationResult(path=str(folder))
        r.add_error("Path is not a directory")
        return [r]

    ct = registry.detect_type_from_path(folder, repo_root)
    if ct is None:
        r = ValidationResult(path=str(folder))
        r.add_error(
            f"Could not detect content type. Supported: {list(registry.content_types.keys())}"
        )
        return [r]

    results: list[ValidationResult] = []

    # Validate main metadata YAML
    yaml_path = folder / ct.metadata_file
    if not yaml_path.exists():
        r = ValidationResult(path=str(yaml_path))
        r.add_warning(f"Missing metadata file: {ct.metadata_file}")
        results.append(r)
        return results

    schema_abs = repo_root / ct.schema
    if not schema_abs.exists():
        r = ValidationResult(path=str(yaml_path))
        r.add_warning(f"Schema file not found: {ct.schema}")
        results.append(r)
    else:
        schema = load_json_schema(schema_abs)
        yaml_data = load_yaml(yaml_path)
        if yaml_data is None:
            yaml_data = {}
        result = validate_yaml_against_schema(yaml_data, schema, str(yaml_path))
        results.append(result)

        # Semantic validation for events
        if ct.key == "event":
            sem = _validate_event_semantics(yaml_data, str(yaml_path))
            if sem.errors or sem.warnings:
                results.append(sem)

    # Validate content files
    if ct.has_markdown_content:
        content_schema_path = (
            (repo_root / ct.content_schema) if ct.content_schema else None
        )
        content_schema = (
            load_json_schema(content_schema_path)
            if content_schema_path and content_schema_path.exists()
            else None
        )

        if ct.content_uses_yml:
            for yml_file in folder.glob("*.yml"):
                if yml_file.name != ct.metadata_file:
                    if content_schema:
                        results.append(validate_yml_content(yml_file, content_schema))
                    else:
                        r = ValidationResult(path=str(yml_file))
                        r.add_warning("Content schema not found — skipping")
                        results.append(r)
        else:
            for md_file in folder.glob("*.md"):
                if md_file.name == "presentation.md":
                    continue
                if content_schema:
                    results.append(
                        validate_markdown_frontmatter(md_file, content_schema)
                    )
                else:
                    r = ValidationResult(path=str(md_file))
                    r.add_warning("Content schema not found — skipping")
                    results.append(r)

    # Validate quizzes
    if ct.has_quizzes:
        results.extend(_validate_quizzes(folder, registry, repo_root))

    return results


def _validate_event_semantics(yaml_data: dict, file_path: str) -> ValidationResult:
    """Semantic checks for events beyond schema type validation."""
    result = ValidationResult(path=file_path)

    booking = yaml_data.get("book_online") is True or yaml_data.get("book_in_person") is True

    if booking and "available_seats" not in yaml_data:
        result.add_warning("Booking enabled but available_seats not set")

    if booking and "project_id" not in yaml_data:
        result.add_warning("Booking enabled but no project_id")

    if not booking and yaml_data.get("price_dollars", 0) > 0:
        result.add_warning("Price set but booking is disabled")

    return result


def _validate_quizzes(
    folder: Path,
    registry: ContentRegistry,
    repo_root: Path,
) -> list[ValidationResult]:
    """Validate quizz/ subfolder."""
    results: list[ValidationResult] = []
    quizz_dir = folder / "quizz"

    if not quizz_dir.exists():
        return results

    if not quizz_dir.is_dir():
        r = ValidationResult(path=str(quizz_dir))
        r.add_error("'quizz' exists but is not a directory")
        return [r]

    # Load quiz schemas
    q_schema_path = registry.quiz_schemas.get("question")
    t_schema_path = registry.quiz_schemas.get("translation")
    q_schema = load_json_schema(repo_root / q_schema_path) if q_schema_path else None
    t_schema = load_json_schema(repo_root / t_schema_path) if t_schema_path else None

    sub_folders = sorted(
        d for d in quizz_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
    )

    if not sub_folders:
        r = ValidationResult(path=str(quizz_dir))
        r.add_warning("Quiz folder exists but contains no quiz subfolders")
        return [r]

    for qf in sub_folders:
        question_file = qf / "question.yml"
        if not question_file.exists():
            r = ValidationResult(path=str(question_file))
            r.add_error("Missing required file: question.yml")
            results.append(r)
            continue

        # Validate question.yml against schema
        if q_schema:
            data = load_yaml(question_file)
            if data is None:
                data = {}
            result = validate_yaml_against_schema(data, q_schema, str(question_file))
            results.append(result)
        else:
            # Fallback manual validation
            results.append(_validate_question_manual(question_file))

        # Validate translation files
        trans_files = [f for f in qf.glob("*.yml") if f.name != "question.yml"]
        if not trans_files:
            r = ValidationResult(path=str(qf))
            r.add_error("No translation files found (e.g., en.yml, fr.yml)")
            results.append(r)
        else:
            for tf in trans_files:
                if t_schema:
                    data = load_yaml(tf)
                    if data is None:
                        data = {}
                    result = validate_yaml_against_schema(data, t_schema, str(tf))
                    results.append(result)
                else:
                    results.append(_validate_quiz_translation_manual(tf))

    return results


def _validate_question_manual(question_file: Path) -> ValidationResult:
    """Manual validation when no quiz schema is available."""
    result = ValidationResult(path=str(question_file))
    try:
        data = load_yaml(question_file)
        if data is None:
            data = {}
        for f in ("chapterId", "difficulty", "author"):
            if f not in data:
                result.add_error(f"Missing required field: '{f}'")
    except Exception as e:
        result.add_error(f"Failed to parse: {e}")
    return result


def _validate_quiz_translation_manual(trans_file: Path) -> ValidationResult:
    """Manual validation for quiz translation files."""
    result = ValidationResult(path=str(trans_file))
    try:
        data = load_yaml(trans_file)
        if data is None:
            data = {}
        for f in ("question", "answer", "wrong_answers"):
            if f not in data:
                result.add_error(f"Missing required field: '{f}'")
        wa = data.get("wrong_answers")
        if wa is not None and not isinstance(wa, list):
            result.add_error("Field 'wrong_answers' must be a list")
    except Exception as e:
        result.add_error(f"Failed to parse: {e}")
    return result


def _print_results(
    results: list[ValidationResult],
    repo_root: Path,
) -> None:
    """Print human-readable validation output."""
    total_errors = sum(len(r.errors) for r in results)
    total_warnings = sum(len(r.warnings) for r in results)

    click.echo(f"\n{_BOLD}{'=' * 60}{_END}")
    click.echo(f"{_BOLD}Validation Results{_END}")
    click.echo(f"{'=' * 60}\n")

    for r in results:
        # Make path relative to repo root where possible
        try:
            rel = str(Path(r.path).relative_to(repo_root))
        except ValueError:
            rel = r.path

        if r.errors or r.warnings:
            status = f"{_RED}FAILED{_END}" if r.errors else f"{_YELLOW}WARNINGS{_END}"
            click.echo(f"{_CYAN}{rel}{_END} — {status}")
            for e in r.errors:
                click.echo(f"  {_RED}ERROR:{_END} {e}")
            for w in r.warnings:
                click.echo(f"  {_YELLOW}WARNING:{_END} {w}")
            click.echo()
        else:
            click.echo(f"{_CYAN}{rel}{_END} — {_GREEN}PASSED{_END}")

    click.echo(f"\n{'=' * 60}")
    if total_errors == 0 and total_warnings == 0:
        click.echo(f"{_GREEN}{_BOLD}All validations passed!{_END}")
    elif total_errors == 0:
        click.echo(f"{_YELLOW}{_BOLD}Passed with {total_warnings} warning(s){_END}")
    else:
        click.echo(
            f"{_RED}{_BOLD}Validation failed:{_END} "
            f"{total_errors} error(s), {total_warnings} warning(s)"
        )
    click.echo(f"{'=' * 60}\n")


def run_validate(
    path: str | None,
    json_output: bool,
) -> None:
    """Core validate logic, called from the CLI command."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if path is None:
        click.echo("Error: provide a content path to validate.", err=True)
        raise SystemExit(1)

    folder = resolve_content_path(path, repo_root)
    results = _validate_folder(folder, registry, repo_root)

    total_errors = sum(len(r.errors) for r in results)
    total_warnings = sum(len(r.warnings) for r in results)

    if json_output:
        output = {
            "path": path,
            "results": [r.to_dict() for r in results],
            "total_errors": total_errors,
            "total_warnings": total_warnings,
        }
        click.echo(json.dumps(output, indent=2))
    else:
        _print_results(results, repo_root)

    # Exit codes: 0=pass, 1=errors, 2=warnings only
    if total_errors > 0:
        raise SystemExit(1)
    elif total_warnings > 0:
        raise SystemExit(2)
