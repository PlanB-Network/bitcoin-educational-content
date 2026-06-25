"""Repo root detection and path resolution."""

from pathlib import Path

MARKER_FILE = "content-types.yml"


def find_repo_root(start: Path | None = None) -> Path:
    """Walk up from start (default: cwd) to find the repo root.

    The repo root is identified by the presence of content-types.yml.

    Raises:
        FileNotFoundError: If no repo root is found.
    """
    current = (start or Path.cwd()).resolve()
    for directory in [current, *current.parents]:
        if (directory / MARKER_FILE).is_file():
            return directory
    raise FileNotFoundError(
        f"Cannot find repo root (no {MARKER_FILE} found above {start or Path.cwd()})"
    )


def resolve_content_path(path_str: str, repo_root: Path | None = None) -> Path:
    """Resolve a content path relative to the repo root.

    Accepts both absolute and relative paths. Relative paths are resolved
    against the repo root.
    """
    path = Path(path_str)
    if path.is_absolute():
        return path
    root = repo_root or find_repo_root()
    return (root / path).resolve()
