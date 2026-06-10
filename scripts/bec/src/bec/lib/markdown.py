"""Markdown manipulation and chapter ID generation."""

from __future__ import annotations

import uuid
from pathlib import Path


def generate_chapter_id() -> str:
    """Generate a UUID chapter ID (the LMS importer requires valid UUIDs)."""
    return str(uuid.uuid4())


def build_part_block(title: str, part_id: str) -> str:
    """Build the markdown block for a new part.

    Returns:
        String like: +++\\n\\n# Title\\n\\n<partId>uuid</partId>
    """
    return f"+++\n\n# {title}\n\n<partId>{part_id}</partId>\n"


def build_chapter_block(title: str, chapter_id: str | None = None) -> str:
    """Build the markdown block for a new chapter.

    Args:
        title: Chapter heading text.
        chapter_id: Optional chapter ID. Auto-generated UUID if None.

    Returns:
        String like: ## Title\\n\\n<chapterId>uuid</chapterId>
    """
    cid = chapter_id or generate_chapter_id()
    return f"## {title}\n\n<chapterId>{cid}</chapterId>\n"


def append_to_markdown(filepath: Path, block: str) -> None:
    """Append a content block to the end of a markdown file.

    Ensures exactly one blank line before the appended block.
    Existing line endings are preserved (no newline translation).
    """
    with filepath.open(encoding="utf-8", newline="") as f:
        content = f.read()

    # Ensure trailing newline separation
    separator = ""
    if content and not content.endswith("\n\n"):
        separator = "\n" if content.endswith("\n") else "\n\n"

    with filepath.open("a", encoding="utf-8", newline="") as f:
        f.write(separator + block)
