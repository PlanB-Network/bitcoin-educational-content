#!/usr/bin/env python3
"""One omp session = one translation JOB = N files sharing ONE target language.

- A long-form markdown file (course) is its own job (translated chapter by chapter).
- Small files (quizz / resource / professor / event YAML) are packed into a job of
  ~10-20 files, still one language per session, to amortise session overhead.

The worker does NO git. Terminology is resolved by the agent on demand against the
repo's own glossary (`resources/glossary/`), sibling same-language content, or a web
search — see prompts/translate.md. Verification is deterministic and happens later.
"""
from __future__ import annotations

import subprocess
import time
import uuid
from pathlib import Path

WORKER_TOOLS = "read,write,edit,grep,glob,web_search"


def build_message(
    items: list[dict],
    lang: str,
    lang_name: str,
    lessons_text: str,
    lessons_scratch_rel: str,
) -> str:
    file_lines = []
    for i, it in enumerate(items, 1):
        kb = max(1, it.get("src_bytes", 0) // 1024)
        file_lines.append(f"{i}. `{it['src']}` -> `{it['dst']}`  ({it['subtype']}, ~{kb} KB)")
    files_block = "\n".join(file_lines)

    chunk = ""
    if any(it.get("long_form") for it in items):
        chunk = (
            "\nOne or more files are large: for those, translate section by section — "
            "write the first section to the destination, then append each following section "
            "with an edit until the ENTIRE document is translated. Never stop mid-document; "
            "re-read the destination at the end to confirm nothing was dropped.\n"
        )

    return (
        f"TASK: Translate {len(items)} file(s) from English into {lang_name} ({lang}). "
        f"Every file uses the SAME target language.\n"
        f"For EACH file below, read the English source and write the COMPLETE translation to "
        f"its destination path (same folder, same extension), following every rule in the "
        f"system prompt.\n\n"
        f"## Files\n{files_block}\n"
        f"{chunk}"
        f"\n## Lessons so far for {lang_name} (apply them)\n{lessons_text.strip() or '(none yet)'}\n"
        f"\nWhen finished, if you made a non-obvious, reusable decision for {lang_name} "
        f"(terminology, register, a structural gotcha), append 1-5 concise markdown bullets to "
        f"`{lessons_scratch_rel}` (create it if needed). Output nothing else."
    )


def translate_job(
    items: list[dict],
    *,
    worktree: Path,
    model: str,
    thinking: str,
    system_prompt: str,
    knowledge_dir: Path,
    lessons_root: Path,
    session_dir: Path,
    timeout: int,
) -> dict:
    started = time.time()
    lang = items[0]["lang"]
    lang_name = items[0]["lang_name"]
    result = {"items": items, "ok": False, "returncode": None, "duration": 0.0,
              "error": None, "stdout_tail": ""}

    missing_src = [it["src"] for it in items if not (worktree / it["src"]).exists()]
    if missing_src:
        result["error"] = f"source(s) missing in worktree: {missing_src[:3]}"
        return result

    lessons_file = knowledge_dir / f"{lang}.md"
    lessons_text = lessons_file.read_text(encoding="utf-8") if lessons_file.exists() else ""

    lessons_scratch_abs = lessons_root / lang / f"{uuid.uuid4().hex}.md"
    lessons_scratch_abs.parent.mkdir(parents=True, exist_ok=True)
    lessons_scratch_rel = str(lessons_scratch_abs.relative_to(worktree))

    message = build_message(items, lang, lang_name, lessons_text, lessons_scratch_rel)

    cmd = [
        "omp", "-p",
        "--session-dir", str(session_dir), "--auto-approve", "--no-lsp", "--no-pty", "--no-title",
        "--cwd", str(worktree),
        "--model", model,
        "--thinking", thinking,
        "--tools", WORKER_TOOLS,
        "--append-system-prompt", system_prompt,
        message,
    ]
    try:
        proc = subprocess.run(cmd, cwd=str(worktree), capture_output=True, text=True, timeout=timeout)
        result["returncode"] = proc.returncode
        result["stdout_tail"] = (proc.stdout or "")[-800:]
        produced = [it for it in items if (worktree / it["dst"]).exists()]
        result["ok"] = proc.returncode == 0 and len(produced) == len(items)
        if not result["ok"]:
            miss = [it["dst"] for it in items if not (worktree / it["dst"]).exists()]
            result["error"] = (proc.stderr or proc.stdout or "")[-500:] + (
                f" | not created: {miss[:3]}" if miss else "")
    except subprocess.TimeoutExpired:
        result["error"] = f"timeout after {timeout}s"
    except Exception as e:  # noqa: BLE001
        result["error"] = f"{type(e).__name__}: {e}"

    result["duration"] = round(time.time() - started, 1)
    return result
