"""bec agent-setup — Symlink agent orientation files to repo root."""

import json
import sys
from pathlib import Path

import click

from bec.lib.repo import find_repo_root

# Files to symlink: (source relative to repo root, link name at repo root)
AGENT_FILES = [
    ("docs/agents/AGENTS.md", "AGENTS.md"),
    ("docs/agents/CLAUDE.md", "CLAUDE.md"),
]


def run_agent_setup(*, json_output: bool = False) -> None:
    """Create symlinks for AGENTS.md and CLAUDE.md at repo root."""
    try:
        repo_root = find_repo_root()
    except FileNotFoundError:
        click.echo("Error: cannot find repo root (no content-types.yml found).", err=True)
        raise SystemExit(1)

    results = []

    for source_rel, link_name in AGENT_FILES:
        source = repo_root / source_rel
        link_path = repo_root / link_name

        if not source.exists():
            click.echo(f"Error: source file not found: {source_rel}", err=True)
            raise SystemExit(1)

        # Compute relative path from repo root to source
        target = Path(source_rel)

        status = _create_symlink(link_path, target, link_name)
        results.append({"file": link_name, "target": source_rel, "status": status})

    if json_output:
        click.echo(json.dumps({"symlinks": results}, indent=2))
    else:
        for r in results:
            icon = "ok" if r["status"] in ("created", "already_correct") else "updated"
            click.echo(f"  {icon}: {r['file']} -> {r['target']} ({r['status']})")
        click.echo("\nAgent orientation files are ready at repo root.")


def _create_symlink(link_path: Path, target: Path, name: str) -> str:
    """Create or update a symlink. Returns status string."""
    if link_path.is_symlink():
        existing_target = link_path.readlink()
        if existing_target == target:
            return "already_correct"
        # Remove stale symlink and recreate
        link_path.unlink()
        link_path.symlink_to(target)
        return "updated"

    if link_path.exists():
        # A real file exists — back it up and replace
        backup = link_path.with_suffix(link_path.suffix + ".bak")
        link_path.rename(backup)
        link_path.symlink_to(target)
        return "replaced"

    link_path.symlink_to(target)
    return "created"
