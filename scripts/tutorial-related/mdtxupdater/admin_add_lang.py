#!/usr/bin/env python3
"""
admin_add_lang.py — Admin-only helper to add a new language code to the app.

This script updates:
- src/mdtxupdater/core.py       (SUPPORTED_LANGS, optionally REF_LANG_CHOICES)
- src/mdtxupdater/prompt.py     (LANGUAGE_NAMES_EN, ORDERED_CODES)

It asks:
- language code (exact file code, e.g., "pt-BR" or "nb-NO")
- full English name (e.g., "Portuguese (Brazil)")
- whether it should be selectable as a reference language in the GUI (optional)

Backups of the modified files are written next to originals with a ".bak" suffix.

Usage:
    python admin_add_lang.py
"""

import re
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent
CORE_PATH = BASE / "src" / "mdtxupdater" / "core.py"
PROMPT_PATH = BASE / "src" / "mdtxupdater" / "prompt.py"


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _write_backup(p: Path) -> None:
    dest = p.with_suffix(p.suffix + ".bak")
    if not dest.exists():
        dest.write_text(_read(p), encoding="utf-8")


def _write(p: Path, content: str) -> None:
    p.write_text(content, encoding="utf-8")


def _ensure_item_in_list(code_text: str, var_name: str, item_literal: str) -> str:
    """
    Append a string item to a top-level Python list variable if not already present.
    Keeps formatting simple by inserting before the closing bracket.
    """
    # Matches: VAR: List[str] = [ ... ]
    pat = re.compile(rf"({re.escape(var_name)}\s*:\s*List\[str\]\s*=\s*\[)(.*?)(\])", re.DOTALL)
    m = pat.search(code_text)
    if not m:
        # Try without annotated type (fallback)
        pat = re.compile(rf"({re.escape(var_name)}\s*=\s*\[)(.*?)(\])", re.DOTALL)
        m = pat.search(code_text)
    if not m:
        raise RuntimeError(f"Could not find list variable {var_name} in file.")

    head, body, tail = m.group(1), m.group(2), m.group(3)

    # Quick check for presence
    if re.search(rf'["\']{re.escape(item_literal)}["\']', body):
        return code_text  # already present

    # Insert with a trailing comma
    new_body = body.rstrip()
    if new_body and not new_body.endswith(","):
        new_body += ","
    new_body += f'\n        "{item_literal}"'

    return code_text[:m.start()] + head + new_body + tail + code_text[m.end():]


def _ensure_item_in_dict(code_text: str, dict_name: str, key: str, value: str) -> str:
    """
    Insert or update a key/value in a top-level Python dict.
    """
    # Matches: DICT: Dict[str, str] = { ... }
    pat = re.compile(rf"({re.escape(dict_name)}\s*:\s*Dict\[str,\s*str\]\s*=\s*\{{)(.*?)(\}})", re.DOTALL)
    m = pat.search(code_text)
    if not m:
        # Fallback without annotated type
        pat = re.compile(rf"({re.escape(dict_name)}\s*=\s*\{{)(.*?)(\}})", re.DOTALL)
        m = pat.search(code_text)
    if not m:
        raise RuntimeError(f"Could not find dict variable {dict_name} in file.")

    head, body, tail = m.group(1), m.group(2), m.group(3)

    # If key exists, replace its value, else append
    key_pat = re.compile(rf'(\s*["\']{re.escape(key)}["\']\s*:\s*)(["\'])(.*?)\2\s*(,?)')
    if key_pat.search(body):
        body = key_pat.sub(rf'\1"\g<3>"\4', body)  # keep existing (no change)
        # Actually replace value:
        body = key_pat.sub(lambda mm: f'{mm.group(1)}"{value}"{mm.group(4)}', body, count=1)
    else:
        body = body.rstrip()
        if body and not body.endswith(","):
            body += ","
        body += f'\n    "{key}": "{value}"'

    return code_text[:m.start()] + head + body + tail + code_text[m.end():]


def main() -> None:
    print("=== Admin: Add a new language ===\n")
    code = input("Language code (e.g., 'pt-BR', 'nb-NO', 'ga', 'eu'): ").strip()
    if not code:
        print("Aborted: empty code.")
        return
    name = input("Full English name (e.g., 'Portuguese (Brazil)'): ").strip()
    if not name:
        print("Aborted: empty language name.")
        return
    ref_choice = input("Add this language as a reference option in GUI? [y/N]: ").strip().lower()
    add_as_ref = (ref_choice == "y")

    # --- Update core.py ---
    core_src = _read(CORE_PATH)
    _write_backup(CORE_PATH)

    core_src = _ensure_item_in_list(core_src, "SUPPORTED_LANGS", code)
    if add_as_ref:
        core_src = _ensure_item_in_list(core_src, "REF_LANG_CHOICES", code)

    _write(CORE_PATH, core_src)
    print(f"[OK] core.py updated ({'with' if add_as_ref else 'without'} reference choice).")

    # --- Update prompt.py ---
    prompt_src = _read(PROMPT_PATH)
    _write_backup(PROMPT_PATH)

    prompt_src = _ensure_item_in_dict(prompt_src, "LANGUAGE_NAMES_EN", code, name)
    prompt_src = _ensure_item_in_list(prompt_src, "ORDERED_CODES", code)

    _write(PROMPT_PATH, prompt_src)
    print("[OK] prompt.py updated (LANGUAGE_NAMES_EN and ORDERED_CODES).")

    print("\nDone. Review diffs, run tests, and commit changes.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(2)
