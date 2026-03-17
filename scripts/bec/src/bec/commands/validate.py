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

# Schema cache — avoids re-reading the same JSON file hundreds of times
_schema_cache: dict[str, dict] = {}


def _load_schema_cached(path: Path) -> dict:
    """Load a JSON schema with caching."""
    key = str(path)
    if key not in _schema_cache:
        _schema_cache[key] = load_json_schema(path)
    return _schema_cache[key]


# ANSI codes
_RED = "\033[91m"
_GREEN = "\033[92m"
_YELLOW = "\033[93m"
_CYAN = "\033[96m"
_BOLD = "\033[1m"
_END = "\033[0m"

# Maps top-level dir / resource subtype to content type key
_RESOURCE_DIR_TO_KEY = {
    "bet": "bet",
    "books": "book",
    "channels": "channel",
    "conferences": "conference",
    "glossary": "glossary",
    "movies": "movie",
    "newsletters": "newsletter",
    "papers": "paper",
    "podcasts": "podcast",
    "projects": "project",
}


# ---------------------------------------------------------------------------
# Content discovery
# ---------------------------------------------------------------------------


def _discover_content_folders(
    repo_root: Path,
    registry: ContentRegistry,
    type_filter: str | None = None,
) -> list[tuple[Path, str]]:
    """Discover all content folders in the repo.

    Args:
        repo_root: Repository root.
        registry: Loaded content registry.
        type_filter: Optional filter — a content type key (e.g. "course", "book"),
            a top-level dir ("courses", "tutorials"), or a resource path
            ("resources/books"). Special values: "courses", "tutorials".

    Returns:
        Sorted list of (folder_path, content_type_key) tuples.
    """
    folders: list[tuple[Path, str]] = []

    # Determine which content type keys to scan
    keys_to_scan = _resolve_type_filter(registry, type_filter)

    for key in keys_to_scan:
        ct = registry.content_types.get(key)
        if ct is None:
            continue
        folders.extend(_discover_for_type(repo_root, ct))

    folders.sort(key=lambda t: t[0])
    return folders


def _resolve_type_filter(
    registry: ContentRegistry,
    type_filter: str | None,
) -> list[str]:
    """Resolve a type_filter string to a list of content type keys."""
    all_keys = list(registry.content_types.keys())

    if type_filter is None:
        return all_keys

    f = type_filter.lower().strip("/")

    # Direct key match (e.g. "course", "book", "glossary")
    if f in registry.content_types:
        return [f]

    # Plural top-level dir match: "courses" → "course", "tutorials" → "tutorial"
    singular = f.rstrip("s") if f.endswith("s") and not f.endswith("ss") else f
    if singular in registry.content_types:
        return [singular]

    # "professors" → "professor", "events" → "event"
    if singular in registry.content_types:
        return [singular]

    # Resource path: "resources/books" → "book"
    if f.startswith("resources/"):
        subtype = f.split("/", 1)[1].rstrip("/")
        mapped = _RESOURCE_DIR_TO_KEY.get(subtype)
        if mapped:
            return [mapped]

    # Group shortcuts
    if f in ("course", "courses"):
        return ["course"]
    if f in ("tutorial", "tutorials"):
        return ["tutorial"]
    if f in ("professor", "professors"):
        return ["professor"]
    if f in ("event", "events"):
        return ["event"]

    # If nothing matched, return empty (will produce zero results)
    return []


def _discover_for_type(
    repo_root: Path,
    ct: ContentType,
) -> list[tuple[Path, str]]:
    """Discover all content folders for a single content type."""
    folders: list[tuple[Path, str]] = []
    pattern = ct.path_pattern  # e.g. "courses/{id}/" or "tutorials/{category}/{id}/"

    parts = pattern.strip("/").split("/")
    base = repo_root / parts[0]

    if not base.exists() or not base.is_dir():
        return folders

    # Count how many path segments after the first static prefix
    # "courses/{id}" → depth 1 under courses/
    # "tutorials/{category}/{id}" → depth 2 under tutorials/
    # "resources/books/{id}" → depth 1 under resources/books/

    # Determine the static prefix (dirs before any {placeholder})
    static_parts: list[str] = []
    for p in parts:
        if "{" in p:
            break
        static_parts.append(p)

    depth_after_static = len(parts) - len(static_parts)
    prefix_dir = repo_root / "/".join(static_parts)

    if not prefix_dir.exists() or not prefix_dir.is_dir():
        return folders

    if depth_after_static == 1:
        # Direct children (courses/{id}, events/{id}, resources/books/{id}, etc.)
        for d in sorted(prefix_dir.iterdir()):
            if d.is_dir() and not d.name.startswith("."):
                folders.append((d, ct.key))
    elif depth_after_static == 2:
        # Two levels deep (tutorials/{category}/{id})
        for cat_dir in sorted(prefix_dir.iterdir()):
            if not cat_dir.is_dir() or cat_dir.name.startswith("."):
                continue
            for d in sorted(cat_dir.iterdir()):
                if d.is_dir() and not d.name.startswith("."):
                    folders.append((d, ct.key))

    return folders


# ---------------------------------------------------------------------------
# Single-folder validation (unchanged from Phase 2)
# ---------------------------------------------------------------------------


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
        schema = _load_schema_cached(schema_abs)
        yaml_data = load_yaml(yaml_path)
        if yaml_data is None:
            yaml_data = {}
        result = validate_yaml_against_schema(
            yaml_data, schema, str(yaml_path), schema_dir=schema_abs.parent,
        )
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
            _load_schema_cached(content_schema_path)
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

    price = yaml_data.get("price_dollars")
    if not booking and price is not None and price > 0:
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
    q_schema = _load_schema_cached(repo_root / q_schema_path) if q_schema_path else None
    t_schema = _load_schema_cached(repo_root / t_schema_path) if t_schema_path else None

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
            schemas_dir = (repo_root / q_schema_path).parent
            result = validate_yaml_against_schema(
                data, q_schema, str(question_file), schema_dir=schemas_dir,
            )
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
                    schemas_dir = (repo_root / t_schema_path).parent
                    result = validate_yaml_against_schema(
                        data, t_schema, str(tf), schema_dir=schemas_dir,
                    )
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


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


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


def _print_summary(
    items: list[dict],
    repo_root: Path,
) -> None:
    """Print summary-only output for --all --summary-only."""
    total = len(items)
    passed = sum(1 for i in items if i["status"] == "passed")
    with_errors = sum(1 for i in items if i["status"] == "error")
    with_warnings = sum(1 for i in items if i["status"] == "warning")

    click.echo(f"\n{_BOLD}{'=' * 60}{_END}")
    click.echo(f"{_BOLD}Validation Summary{_END}")
    click.echo(f"{'=' * 60}\n")
    click.echo(f"  Total items:  {total}")
    click.echo(f"  {_GREEN}Passed:{_END}       {passed}")
    click.echo(f"  {_RED}Errors:{_END}       {with_errors}")
    click.echo(f"  {_YELLOW}Warnings:{_END}     {with_warnings}")
    click.echo(f"\n{'=' * 60}\n")


# ---------------------------------------------------------------------------
# Public entry points
# ---------------------------------------------------------------------------


def run_validate(
    path: str | None,
    json_output: bool,
) -> None:
    """Core validate logic for a single path, called from the CLI command."""
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


def run_validate_all(
    json_output: bool,
    summary_only: bool,
    type_filter: str | None,
) -> None:
    """Validate all content in the repo with optional filters."""
    from tqdm import tqdm

    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    content_folders = _discover_content_folders(repo_root, registry, type_filter)

    if not content_folders:
        msg = "No content found"
        if type_filter:
            msg += f" for type filter '{type_filter}'"
        click.echo(msg, err=True)
        raise SystemExit(1)

    # Aggregate per-item results
    items: list[dict] = []
    total_errors = 0
    total_warnings = 0

    # Use tqdm for progress (only in non-JSON mode)
    iterator = content_folders
    if not json_output:
        iterator = tqdm(
            content_folders,
            desc="Validating",
            unit="item",
            ncols=80,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
        )

    for folder, ct_key in iterator:
        try:
            rel_path = str(folder.relative_to(repo_root))
        except ValueError:
            rel_path = str(folder)

        results = _validate_folder(folder, registry, repo_root)
        item_errors = sum(len(r.errors) for r in results)
        item_warnings = sum(len(r.warnings) for r in results)
        total_errors += item_errors
        total_warnings += item_warnings

        if item_errors > 0:
            status = "error"
        elif item_warnings > 0:
            status = "warning"
        else:
            status = "passed"

        items.append({
            "path": rel_path,
            "type": ct_key,
            "status": status,
            "errors": [
                e for r in results for e in r.errors
            ],
            "warnings": [
                w for r in results for w in r.warnings
            ],
        })

    # Build summary
    summary = {
        "total": len(items),
        "passed": sum(1 for i in items if i["status"] == "passed"),
        "errors": sum(1 for i in items if i["status"] == "error"),
        "warnings": sum(1 for i in items if i["status"] == "warning"),
    }

    if json_output:
        output: dict = {"summary": summary, "items": items}
        click.echo(json.dumps(output, indent=2))
    elif summary_only:
        _print_summary(items, repo_root)
    else:
        # Print items with issues, then summary
        click.echo(f"\n{_BOLD}{'=' * 60}{_END}")
        click.echo(f"{_BOLD}Validation Results{_END}")
        click.echo(f"{'=' * 60}\n")

        for item in items:
            if item["status"] == "error":
                click.echo(f"{_CYAN}{item['path']}{_END} [{item['type']}] — {_RED}FAILED{_END}")
                for e in item["errors"]:
                    click.echo(f"  {_RED}ERROR:{_END} {e}")
                for w in item["warnings"]:
                    click.echo(f"  {_YELLOW}WARNING:{_END} {w}")
                click.echo()
            elif item["status"] == "warning":
                click.echo(f"{_CYAN}{item['path']}{_END} [{item['type']}] — {_YELLOW}WARNINGS{_END}")
                for w in item["warnings"]:
                    click.echo(f"  {_YELLOW}WARNING:{_END} {w}")
                click.echo()

        # Summary line
        click.echo(f"{'=' * 60}")
        click.echo(
            f"Total: {summary['total']} | "
            f"{_GREEN}Passed: {summary['passed']}{_END} | "
            f"{_RED}Errors: {summary['errors']}{_END} | "
            f"{_YELLOW}Warnings: {summary['warnings']}{_END}"
        )
        click.echo(f"{'=' * 60}\n")

    # Exit codes: 0=pass, 1=errors, 2=warnings only
    if total_errors > 0:
        raise SystemExit(1)
    elif total_warnings > 0:
        raise SystemExit(2)
