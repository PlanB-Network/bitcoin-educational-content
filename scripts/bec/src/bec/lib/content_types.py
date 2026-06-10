"""Parse and query the content-types.yml registry."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from bec.lib.repo import find_repo_root
from bec.lib.yaml_utils import load_yaml

REGISTRY_FILENAME = "content-types.yml"


@dataclass
class ContentType:
    """A single content type definition."""

    key: str
    name: str
    path_pattern: str
    metadata_file: str
    schema: str
    content_schema: str | None = None
    has_markdown_content: bool = True
    has_quizzes: bool = False
    content_uses_yml: bool = False
    example: str = ""


@dataclass
class ContentRegistry:
    """The full parsed content-types.yml registry."""

    content_types: dict[str, ContentType] = field(default_factory=dict)
    tutorial_categories: list[str] = field(default_factory=list)
    discipline_codes: dict[str, str] = field(default_factory=dict)
    level_range: dict[str, str] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    quiz_schemas: dict[str, str] = field(default_factory=dict)

    def get_type(self, key: str) -> ContentType:
        """Get a content type by key. Raises KeyError if not found."""
        return self.content_types[key]

    def get_schema_path(self, key: str, repo_root: Path | None = None) -> Path:
        """Get the absolute schema path for a content type."""
        root = repo_root or find_repo_root()
        return root / self.content_types[key].schema

    def get_content_schema_path(
        self, key: str, repo_root: Path | None = None
    ) -> Path | None:
        """Get the absolute content schema path, or None if not applicable."""
        ct = self.content_types[key]
        if ct.content_schema is None:
            return None
        root = repo_root or find_repo_root()
        return root / ct.content_schema

    def detect_type_from_path(self, path: Path, repo_root: Path | None = None) -> ContentType | None:
        """Detect the content type from a filesystem path.

        Matches the path against known path patterns.
        """
        root = repo_root or find_repo_root()
        try:
            rel = path.resolve().relative_to(root.resolve())
        except ValueError:
            return None

        parts = rel.parts

        if not parts:
            return None

        # courses/{id}
        if parts[0] == "courses" and len(parts) >= 2:
            return self.content_types.get("course")

        # tutorials/{category}/{id}
        if parts[0] == "tutorials" and len(parts) >= 3:
            return self.content_types.get("tutorial")

        # professors/{id}
        if parts[0] == "professors" and len(parts) >= 2:
            return self.content_types.get("professor")

        # events/{id}
        if parts[0] == "events" and len(parts) >= 2:
            return self.content_types.get("event")

        # resources/{subtype}/{id}
        if parts[0] == "resources" and len(parts) >= 3:
            subtype = parts[1]
            type_map = {
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
            return self.content_types.get(type_map.get(subtype, ""))

        return None


def load_registry(repo_root: Path | None = None) -> ContentRegistry:
    """Load and parse the content-types.yml file.

    Args:
        repo_root: Repo root directory. Auto-detected if None.

    Returns:
        A ContentRegistry with all parsed data.

    Raises:
        FileNotFoundError: If content-types.yml is not found.
    """
    root = repo_root or find_repo_root()
    registry_path = root / REGISTRY_FILENAME
    data = load_yaml(registry_path)
    if data is None:
        raise ValueError(f"Empty registry file: {registry_path}")

    content_types = {}
    for key, ct_data in data.get("content_types", {}).items():
        content_types[key] = ContentType(
            key=key,
            name=ct_data["name"],
            path_pattern=ct_data["path_pattern"],
            metadata_file=ct_data["metadata_file"],
            schema=ct_data["schema"],
            content_schema=ct_data.get("content_schema"),
            has_markdown_content=ct_data.get("has_markdown_content", True),
            has_quizzes=ct_data.get("has_quizzes", False),
            content_uses_yml=ct_data.get("content_uses_yml", False),
            example=ct_data.get("example", ""),
        )

    return ContentRegistry(
        content_types=content_types,
        tutorial_categories=data.get("tutorial_categories", []),
        discipline_codes=data.get("discipline_codes", {}),
        level_range=data.get("level_range", {}),
        tags=data.get("tags", []),
        languages=data.get("languages", []),
        quiz_schemas=data.get("quiz_schemas", {}),
    )
