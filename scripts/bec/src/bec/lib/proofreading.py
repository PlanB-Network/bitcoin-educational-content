"""Proofreading metadata: reward computation, contributor management, status queries."""

from __future__ import annotations

import os
from datetime import date
from pathlib import Path

from bec.lib.yaml_utils import load_yaml, dump_yaml

# ---- Constants ----------------------------------------------------------------

BASE_FEE = 0.1
DOLLARS_PER_WORD = 0.001
MAX_PAID_ITERATIONS = 2  # Reward drops to 0 after this many contributors

# Files that carry proofreading metadata
METADATA_FILES = {
    "course.yml",
    "question.yml",
    "tutorial.yml",
    "book.yml",
    "word.yml",
    "bet.yml",
    "builder.yml",
    "conference.yml",
}

# Language difficulty factors (how hard a language is to translate into)
LANGUAGE_FACTORS: dict[str, float] = {
    "en": 1.0, "fr": 1.0, "de": 1.0, "es": 1.0, "it": 1.0, "pt": 1.0,
    "ro": 1.0, "sv": 1.0,
    "cs": 1.5, "ru": 1.5, "fi": 1.5, "et": 1.5, "uk": 1.5, "nb-NO": 1.5,
    "pl": 1.5, "sw": 1.5, "fa": 1.5, "nl": 1.5, "bg": 1.5,
    "id": 2.0, "zh-Hans": 2.0, "tr": 2.0, "ha": 2.0, "sr-Latn": 2.0,
    "zh-Hant": 2.0, "ko": 2.0, "th": 2.0,
    "vi": 2.5, "ja": 2.5, "hi": 2.5, "rn": 2.5,
}

# Content difficulty multiplier by level
CONTENT_DIFFICULTY: dict[str, int] = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4,
}


# ---- Core helpers -------------------------------------------------------------

def find_metadata_file(content_path: Path) -> Path | None:
    """Find the metadata YAML file inside a content directory."""
    for name in METADATA_FILES:
        candidate = content_path / name
        if candidate.is_file():
            return candidate
    return None


def count_words(file_path: Path) -> int:
    """Count words in a file."""
    text = file_path.read_text(encoding="utf-8")
    return len(text.split())


def get_original_word_count(metadata_path: Path, data: dict) -> int:
    """Count words in the original-language content file."""
    original = data.get("original_language")
    if not original:
        raise ValueError(f"No 'original_language' field in {metadata_path}")

    directory = metadata_path.parent
    for ext in (".md", ".yml"):
        candidate = directory / f"{original}{ext}"
        if candidate.is_file():
            return count_words(candidate)

    raise FileNotFoundError(
        f"No content file for original language '{original}' in {directory}"
    )


def compute_reward(
    words: int,
    language_factor: float,
    urgency: int | float,
    proofread_iteration: int,
) -> float:
    """Compute the proofreading reward in dollars.

    Formula: (urgency * (0.001 * words * language_factor) + BASE_FEE) * 2^(-iteration)
    Returns 0 if iteration >= MAX_PAID_ITERATIONS.
    """
    if proofread_iteration >= MAX_PAID_ITERATIONS:
        return 0.0
    reward = (urgency * (DOLLARS_PER_WORD * words * language_factor) + BASE_FEE) * 2 ** (-proofread_iteration)
    return round(reward, 2)


def get_difficulty_factor(data: dict) -> float:
    """Get difficulty multiplier: 3.0 for glossary, else from level field."""
    if data.get("en_word"):
        return 3.0
    level = data.get("level")
    if level and level in CONTENT_DIFFICULTY:
        return float(CONTENT_DIFFICULTY[level])
    return 1.0


# ---- Proofreading entry helpers -----------------------------------------------

def get_proofreading_entries(data: dict) -> list[dict]:
    """Get the proofreading list from metadata, or empty list."""
    entries = data.get("proofreading")
    if entries is None:
        return []
    return list(entries)


def find_language_entry(data: dict, language: str) -> dict | None:
    """Find the proofreading entry for a specific language."""
    for entry in get_proofreading_entries(data):
        if entry.get("language", "").lower() == language.lower():
            return entry
    return None


def get_contributor_count(entry: dict) -> int:
    """Count existing contributors for a language entry."""
    names = entry.get("contributor_names")
    if names is None:
        return 0
    return len(names)


def add_contributor(data: dict, language: str, contributor: str) -> tuple[bool, str]:
    """Add a contributor to a language's proofreading entry.

    Returns (success, message).
    """
    entry = find_language_entry(data, language)
    if entry is None:
        available = [e.get("language", "?") for e in get_proofreading_entries(data)]
        return False, f"Language '{language}' not found. Available: {available}"

    if entry.get("contributor_names") is None:
        entry["contributor_names"] = []

    if contributor in entry["contributor_names"]:
        return False, f"'{contributor}' already listed for {language}"

    entry["contributor_names"].append(contributor)
    entry["last_contribution_date"] = str(date.today())
    return True, f"Added '{contributor}' to {language}"


def evaluate_reward_for_language(metadata_path: Path, data: dict, language: str) -> dict:
    """Evaluate the proofreading reward for a specific language.

    Returns a dict with reward details.
    """
    entry = find_language_entry(data, language)
    if entry is None:
        return {"error": f"Language '{language}' not in proofreading entries"}

    words = get_original_word_count(metadata_path, data)
    lang_factor = LANGUAGE_FACTORS.get(language, 1.0)
    urgency = entry.get("urgency", 1)
    iteration = get_contributor_count(entry)

    reward = compute_reward(words, lang_factor, urgency, iteration)
    remaining = max(0, MAX_PAID_ITERATIONS - iteration)

    return {
        "language": language,
        "words": words,
        "language_factor": lang_factor,
        "urgency": urgency,
        "iteration": iteration,
        "reward": reward,
        "remaining_paid_proofreadings": remaining,
        "contributors": entry.get("contributor_names") or [],
    }


def get_status_matrix(metadata_path: Path, data: dict) -> list[dict]:
    """Get proofreading status for all languages in a content item."""
    entries = get_proofreading_entries(data)
    if not entries:
        return []

    original_lang = data.get("original_language", "?")
    try:
        words = get_original_word_count(metadata_path, data)
    except (ValueError, FileNotFoundError):
        words = 0

    result = []
    for entry in entries:
        lang = entry.get("language", "?")
        contributors = entry.get("contributor_names") or []
        iteration = len(contributors)
        urgency = entry.get("urgency", 1)
        lang_factor = LANGUAGE_FACTORS.get(lang, 1.0)
        reward = compute_reward(words, lang_factor, urgency, iteration)
        remaining = max(0, MAX_PAID_ITERATIONS - iteration)

        result.append({
            "language": lang,
            "is_original": lang == original_lang,
            "contributors": contributors,
            "iteration": iteration,
            "remaining_paid_proofreadings": remaining,
            "urgency": urgency,
            "reward": reward,
            "last_contribution_date": entry.get("last_contribution_date"),
        })

    return result


def update_metadata_file(metadata_path: Path, data: dict) -> None:
    """Write updated metadata back to the YAML file.

    Uses line-level manipulation to only rewrite the proofreading section,
    preserving the rest of the file (comments, ordering, formatting).
    """
    original_content = metadata_path.read_text(encoding="utf-8")
    lines = original_content.split("\n")

    # Find proofreading section boundaries
    proof_start = -1
    proof_indent = ""
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "proofreading:" or stripped.startswith("proofreading:"):
            proof_start = i
            proof_indent = line[: len(line) - len(line.lstrip())]
            break

    if proof_start == -1:
        # No proofreading section — just dump normally
        dump_yaml(data, metadata_path)
        return

    # Find where proofreading section ends
    base_indent_len = len(proof_indent)
    proof_end = len(lines)
    for i in range(proof_start + 1, len(lines)):
        line = lines[i]
        if line.strip() == "":
            continue
        current_indent = len(line) - len(line.lstrip())
        if current_indent <= base_indent_len and line.strip():
            proof_end = i
            break

    # Build new proofreading section
    new_lines = [f"{proof_indent}proofreading:"]
    for entry in data.get("proofreading", []):
        new_lines.append(f"{proof_indent}  - language: {entry['language']}")

        # last_contribution_date
        lcd = entry.get("last_contribution_date")
        if lcd:
            new_lines.append(f"{proof_indent}    last_contribution_date: '{lcd}'")
        else:
            new_lines.append(f"{proof_indent}    last_contribution_date:")

        new_lines.append(f"{proof_indent}    urgency: {entry.get('urgency', 1)}")

        # contributor_names
        names = entry.get("contributor_names")
        if names and len(names) > 0:
            new_lines.append(f"{proof_indent}    contributor_names:")
            for name in names:
                new_lines.append(f"{proof_indent}      - {name}")
        else:
            new_lines.append(f"{proof_indent}    contributor_names:")

        new_lines.append(f"{proof_indent}    reward: {entry.get('reward', 0)}")

    # Reconstruct
    before = "\n".join(lines[:proof_start])
    after = "\n".join(lines[proof_end:])
    new_section = "\n".join(new_lines)

    if before:
        result = before + "\n" + new_section
    else:
        result = new_section
    if after.strip():
        result = result + "\n" + after
    else:
        result = result + "\n"

    metadata_path.write_text(result, encoding="utf-8")


def recalculate_rewards(metadata_path: Path, data: dict) -> None:
    """Recalculate rewards for all languages in a content item."""
    entries = get_proofreading_entries(data)
    if not entries:
        return

    try:
        words = get_original_word_count(metadata_path, data)
    except (ValueError, FileNotFoundError):
        return

    for entry in entries:
        lang = entry.get("language", "")
        lang_factor = LANGUAGE_FACTORS.get(lang, 1.0)
        urgency = entry.get("urgency", 1)
        iteration = get_contributor_count(entry)
        reward = compute_reward(words, lang_factor, urgency, iteration)
        entry["reward"] = reward
