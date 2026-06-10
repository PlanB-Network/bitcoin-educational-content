"""Proofread command implementations: update, reward, batch-add, status."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from bec.lib.proofreading import (
    LANGUAGE_FACTORS,
    add_contributor,
    evaluate_reward_for_language,
    find_metadata_file,
    get_proofreading_entries,
    get_status_matrix,
    recalculate_rewards,
    update_metadata_file,
)
from bec.lib.repo import find_repo_root, resolve_content_path
from bec.lib.yaml_utils import load_yaml


# ---- Helpers ------------------------------------------------------------------

def _load_metadata(content_path_str: str) -> tuple[Path, dict]:
    """Resolve a content path and load its metadata YAML.

    Returns (metadata_file_path, parsed_data).
    Exits with code 1 on failure.
    """
    repo_root = find_repo_root()
    content_dir = resolve_content_path(content_path_str, repo_root)

    if not content_dir.is_dir():
        click.echo(f"Error: '{content_path_str}' is not a valid directory", err=True)
        raise SystemExit(1)

    metadata_path = find_metadata_file(content_dir)
    if metadata_path is None:
        click.echo(f"Error: no metadata YAML found in '{content_path_str}'", err=True)
        raise SystemExit(1)

    data = load_yaml(metadata_path)
    if data is None:
        click.echo(f"Error: empty metadata file '{metadata_path}'", err=True)
        raise SystemExit(1)

    return metadata_path, data


def _prompt_if_missing(value: str | None, prompt_text: str, choices: list[str] | None = None) -> str:
    """Prompt interactively if value is None."""
    if value is not None:
        return value
    if choices:
        click.echo(f"Available options: {', '.join(sorted(choices))}")
    return click.prompt(prompt_text)


def _list_content_paths(repo_root: Path) -> list[str]:
    """List content directories that have metadata YAML files."""
    results = []
    for top_dir in ["courses", "tutorials", "resources", "events"]:
        top = repo_root / top_dir
        if not top.is_dir():
            continue
        if top_dir == "tutorials":
            for category in sorted(top.iterdir()):
                if category.is_dir():
                    for item in sorted(category.iterdir()):
                        if item.is_dir() and find_metadata_file(item):
                            results.append(str(item.relative_to(repo_root)))
        elif top_dir == "resources":
            for subtype in sorted(top.iterdir()):
                if subtype.is_dir():
                    for item in sorted(subtype.iterdir()):
                        if item.is_dir() and find_metadata_file(item):
                            results.append(str(item.relative_to(repo_root)))
        else:
            for item in sorted(top.iterdir()):
                if item.is_dir() and find_metadata_file(item):
                    results.append(str(item.relative_to(repo_root)))
    return results


# ---- Subcommand: update -------------------------------------------------------

def run_proofread_update(
    path: str | None,
    lang: str | None,
    contributor: str | None,
    recalc: bool,
    json_output: bool,
) -> None:
    """Add a contributor to a content item's proofreading metadata."""
    repo_root = find_repo_root()

    # Interactive prompts for missing args
    if path is None:
        paths = _list_content_paths(repo_root)
        if paths:
            click.echo("Available content paths:")
            for i, p in enumerate(paths[:30], 1):
                click.echo(f"  {i}. {p}")
            if len(paths) > 30:
                click.echo(f"  ... and {len(paths) - 30} more")
        path = click.prompt("Content path")

    metadata_path, data = _load_metadata(path)

    # Show available languages from proofreading entries
    entries = get_proofreading_entries(data)
    available_langs = [e.get("language", "?") for e in entries]

    lang = _prompt_if_missing(lang, "Language code", available_langs)
    contributor = _prompt_if_missing(contributor, "Contributor GitHub username")

    # Add contributor
    success, message = add_contributor(data, lang, contributor)

    if not success:
        if json_output:
            click.echo(json.dumps({"success": False, "message": message}))
        else:
            click.echo(f"Warning: {message}", err=True)
        raise SystemExit(1)

    # Optionally recalculate rewards
    if recalc:
        recalculate_rewards(metadata_path, data)

    # Write back
    update_metadata_file(metadata_path, data)

    if json_output:
        click.echo(json.dumps({
            "success": True,
            "message": message,
            "path": path,
            "language": lang,
            "contributor": contributor,
            "file": str(metadata_path),
        }))
    else:
        click.echo(f"{message}")
        click.echo(f"Updated: {metadata_path.relative_to(repo_root)}")


# ---- Subcommand: reward -------------------------------------------------------

def run_proofread_reward(
    path: str | None,
    lang: str | None,
    json_output: bool,
) -> None:
    """Display proofreading reward information for a content item."""
    repo_root = find_repo_root()

    if path is None:
        path = click.prompt("Content path")

    metadata_path, data = _load_metadata(path)

    entries = get_proofreading_entries(data)
    if not entries:
        click.echo(f"No proofreading metadata in {path}", err=True)
        raise SystemExit(1)

    # If no language specified, show rewards for all languages
    if lang is None:
        results = []
        for entry in entries:
            entry_lang = entry.get("language", "?")
            info = evaluate_reward_for_language(metadata_path, data, entry_lang)
            results.append(info)

        if json_output:
            click.echo(json.dumps({"path": path, "rewards": results}, indent=2))
        else:
            content_name = Path(path).name
            click.echo(f"Proofreading rewards for {content_name}:")
            click.echo(f"{'Language':<10} {'Reward':>8} {'Iteration':>10} {'Remaining':>10} {'Contributors'}")
            click.echo("-" * 65)
            for r in results:
                if "error" in r:
                    continue
                contribs = ", ".join(r["contributors"]) if r["contributors"] else "-"
                click.echo(
                    f"{r['language']:<10} {r['reward']:>8.2f} {r['iteration']:>10} "
                    f"{r['remaining_paid_proofreadings']:>10} {contribs}"
                )
    else:
        info = evaluate_reward_for_language(metadata_path, data, lang)
        if "error" in info:
            click.echo(f"Error: {info['error']}", err=True)
            raise SystemExit(1)

        if json_output:
            click.echo(json.dumps({"path": path, "reward": info}, indent=2))
        else:
            click.echo(f"Reward for {Path(path).name} ({lang}):")
            click.echo(f"  Words: {info['words']}")
            click.echo(f"  Language factor: {info['language_factor']}")
            click.echo(f"  Urgency: {info['urgency']}")
            click.echo(f"  Iteration: {info['iteration']}")
            click.echo(f"  Reward: {info['reward']}")
            click.echo(f"  Remaining paid proofreadings: {info['remaining_paid_proofreadings']}")


# ---- Subcommand: batch-add ----------------------------------------------------

def run_proofread_batch_add(
    contributor: str | None,
    lang: str | None,
    paths: tuple[str, ...],
    recalc: bool,
    json_output: bool,
) -> None:
    """Add a contributor to multiple content items at once."""
    repo_root = find_repo_root()

    contributor = _prompt_if_missing(contributor, "Contributor GitHub username")
    lang = _prompt_if_missing(lang, "Language code", sorted(LANGUAGE_FACTORS.keys()))

    if not paths:
        paths_input = click.prompt("Content paths (space-separated)")
        paths = tuple(paths_input.split())

    results = []
    success_count = 0
    error_count = 0

    for content_path in paths:
        try:
            metadata_path, data = _load_metadata(content_path)
            success, message = add_contributor(data, lang, contributor)
            if success:
                if recalc:
                    recalculate_rewards(metadata_path, data)
                update_metadata_file(metadata_path, data)
                success_count += 1
            results.append({
                "path": content_path,
                "success": success,
                "message": message,
            })
            if not json_output:
                status = "ok" if success else "skip"
                click.echo(f"  [{status}] {content_path}: {message}")
        except SystemExit:
            error_count += 1
            results.append({
                "path": content_path,
                "success": False,
                "message": "Failed to load metadata",
            })
            if not json_output:
                click.echo(f"  [err] {content_path}: failed to load metadata")

    if json_output:
        click.echo(json.dumps({
            "contributor": contributor,
            "language": lang,
            "total": len(paths),
            "success": success_count,
            "errors": error_count,
            "results": results,
        }, indent=2))
    else:
        click.echo(f"\nProcessed {len(paths)} items: {success_count} updated, {error_count} errors")


# ---- Subcommand: status -------------------------------------------------------

def run_proofread_status(
    path: str | None,
    json_output: bool,
) -> None:
    """Show proofreading status for all languages of a content item."""
    repo_root = find_repo_root()

    if path is None:
        path = click.prompt("Content path")

    metadata_path, data = _load_metadata(path)

    matrix = get_status_matrix(metadata_path, data)
    if not matrix:
        click.echo(f"No proofreading metadata in {path}", err=True)
        raise SystemExit(1)

    original_lang = data.get("original_language", "?")

    if json_output:
        click.echo(json.dumps({
            "path": path,
            "original_language": original_lang,
            "languages": matrix,
        }, indent=2))
    else:
        content_name = Path(path).name
        click.echo(f"Proofreading status for {content_name} (original: {original_lang}):")
        click.echo(f"{'Language':<10} {'Status':<12} {'Reward':>8} {'Urgency':>8} {'Last Date':<12} {'Contributors'}")
        click.echo("-" * 80)
        for entry in matrix:
            contribs = ", ".join(entry["contributors"]) if entry["contributors"] else "-"
            if entry["is_original"]:
                status = "original"
            elif entry["iteration"] >= 2:
                status = "complete"
            elif entry["iteration"] > 0:
                status = f"{entry['iteration']}/2"
            else:
                status = "pending"
            lcd = entry["last_contribution_date"] or "-"
            click.echo(
                f"{entry['language']:<10} {status:<12} {entry['reward']:>8.2f} "
                f"{entry['urgency']:>8} {lcd:<12} {contribs}"
            )
