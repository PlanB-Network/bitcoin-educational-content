"""Markdown manipulation and BIP39 chapter ID generation."""

from __future__ import annotations

import random
from importlib import resources as pkg_resources
from pathlib import Path

_WORDLIST: list[str] | None = None


def _load_wordlist() -> list[str]:
    """Load the BIP39 English wordlist (2048 words), cached on first call."""
    global _WORDLIST
    if _WORDLIST is not None:
        return _WORDLIST

    # Use importlib.resources for package data (works with installed packages)
    try:
        ref = pkg_resources.files("bec") / "data" / "bip39_wordlist.txt"
        text = ref.read_text(encoding="utf-8")
    except (TypeError, FileNotFoundError):
        # Fallback: resolve relative to this file
        data_path = Path(__file__).resolve().parent.parent / "data" / "bip39_wordlist.txt"
        text = data_path.read_text(encoding="utf-8")

    _WORDLIST = [w.strip() for w in text.splitlines() if w.strip()]
    return _WORDLIST


def generate_chapter_id() -> str:
    """Generate a 3-word BIP39 chapter ID (e.g., 'father-loop-frog')."""
    words = _load_wordlist()
    return "-".join(random.sample(words, 3))


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
        chapter_id: Optional chapter ID. Auto-generated BIP39 ID if None.

    Returns:
        String like: ## Title\\n\\n<chapterId>word-word-word</chapterId>
    """
    cid = chapter_id or generate_chapter_id()
    return f"## {title}\n\n<chapterId>{cid}</chapterId>\n"


def append_to_markdown(filepath: Path, block: str) -> None:
    """Append a content block to the end of a markdown file.

    Ensures exactly one blank line before the appended block.
    """
    content = filepath.read_text(encoding="utf-8")

    # Ensure trailing newline separation
    if content and not content.endswith("\n\n"):
        if content.endswith("\n"):
            content += "\n"
        else:
            content += "\n\n"

    content += block
    filepath.write_text(content, encoding="utf-8")
