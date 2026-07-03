#!/usr/bin/env python3
"""One translation unit = one content file x one target language = one omp session.

The worker composes a task message (glossary filtered to the file, prior lessons,
chapter-chunking guidance for long courses) and drives a headless omp run that
translates the source in place and writes the sibling `{lang}` file.

It performs NO git operations — the release agent handles commit/push/PR.
"""
from __future__ import annotations

import subprocess
import time
import uuid
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
WORKER_TOOLS = "read,write,edit,grep,glob"


def _filter_glossary(src_text: str, terms: list[str]) -> list[str]:
    """Only inject glossary terms that actually occur in this file."""
    return [t for t in terms if t and t in src_text]


def build_message(
    item: dict,
    src_text: str,
    glossary_terms: list[str],
    lessons_text: str,
    lessons_scratch_rel: str,
    long_form_threshold: int,
) -> str:
    present = _filter_glossary(src_text, glossary_terms)
    gloss_block = "\n".join(f"- {t}" for t in present) if present else "(none present in this file)"
    lessons = lessons_text.strip() or "(none yet)"

    chunk = ""
    if item.get("long_form"):
        kb = item.get("src_bytes", 0) // 1024
        chunk = (
            f"\nThis source is large (~{kb} KB). Work section by section: write the "
            f"first section to `{item['dst']}`, then append each following section "
            f"with an edit, until the ENTIRE document is translated. Do not stop early; "
            f"re-read the destination at the end to confirm no section, code block or "
            f"image was dropped.\n"
        )

    return (
        f"TASK: Translate the file `{item['src']}` from English into "
        f"{item['lang_name']} ({item['lang']}).\n"
        f"Write the complete translation to `{item['dst']}` "
        f"(same folder, same format: .{item['ext']}). This is "
        f"{item['content_type']}/{item['subtype']} content.\n"
        f"Follow every rule in the system prompt exactly.\n"
        f"{chunk}"
        f"\n## GLOSSARY — keep these terms verbatim (never translate or transliterate):\n"
        f"{gloss_block}\n"
        f"\n## LESSONS so far for {item['lang_name']} (apply them):\n"
        f"{lessons}\n"
        f"\nWhen finished, if you made a non-obvious, reusable decision for "
        f"{item['lang_name']}, append 1-5 concise markdown bullets to "
        f"`{lessons_scratch_rel}` (create it if needed). Output nothing else."
    )


def translate_one(
    item: dict,
    *,
    worktree: Path,
    model: str,
    system_prompt: str,
    glossary_terms: list[str],
    knowledge_dir: Path,
    lessons_root: Path,
    long_form_threshold: int,
    timeout: int,
    thinking: str = "off",
) -> dict:
    started = time.time()
    src_abs = worktree / item["src"]
    result = {
        "item": item,
        "ok": False,
        "returncode": None,
        "duration": 0.0,
        "error": None,
        "stdout_tail": "",
    }

    if not src_abs.exists():
        result["error"] = f"source missing in worktree: {item['src']}"
        return result

    src_text = src_abs.read_text(encoding="utf-8", errors="replace")

    lessons_file = knowledge_dir / f"{item['lang']}.md"
    lessons_text = lessons_file.read_text(encoding="utf-8") if lessons_file.exists() else ""

    lessons_scratch_abs = lessons_root / item["lang"] / f"{uuid.uuid4().hex}.md"
    lessons_scratch_abs.parent.mkdir(parents=True, exist_ok=True)
    lessons_scratch_rel = str(lessons_scratch_abs.relative_to(worktree))

    message = build_message(
        item, src_text, glossary_terms, lessons_text, lessons_scratch_rel, long_form_threshold
    )

    cmd = [
        "omp", "-p",
        "--no-session",
        "--auto-approve",
        "--no-lsp",
        "--no-pty",
        "--no-title",
        "--cwd", str(worktree),
        "--model", model,
        "--thinking", thinking,
        "--tools", WORKER_TOOLS,
        "--append-system-prompt", system_prompt,
        message,
    ]

    try:
        proc = subprocess.run(
            cmd, cwd=str(worktree), capture_output=True, text=True, timeout=timeout
        )
        result["returncode"] = proc.returncode
        result["stdout_tail"] = (proc.stdout or "")[-800:]
        if proc.returncode != 0:
            result["error"] = (proc.stderr or proc.stdout or "omp non-zero exit")[-800:]
        else:
            result["ok"] = (worktree / item["dst"]).exists()
            if not result["ok"]:
                result["error"] = "omp exited 0 but destination file was not created"
    except subprocess.TimeoutExpired:
        result["error"] = f"timeout after {timeout}s"
    except Exception as e:  # noqa: BLE001
        result["error"] = f"{type(e).__name__}: {e}"

    result["duration"] = round(time.time() - started, 1)
    return result
