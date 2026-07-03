#!/usr/bin/env python3
"""Deterministic gap-check: which content is missing a translation?

Walks the configured content roots, finds every English source file
(``en.md`` / ``en.yml``) and, for each supported target language, checks whether
the sibling ``{lang}.{ext}`` exists in the same folder. Every missing sibling is
a work item ``(source, target_lang)``.

No LLM, no network — pure filesystem truth.

Usage:
    python3 find_missing.py                         # human summary of all gaps
    python3 find_missing.py --langs fr,de --content courses
    python3 find_missing.py --json                  # machine-readable work list
    python3 find_missing.py --limit 20 --json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_REPO_ROOT = SCRIPT_DIR.parents[1]  # scripts/agent-translate -> repo root
SOURCE_FILENAMES = ("en.md", "en.yml")


@dataclass(frozen=True)
class WorkItem:
    src: str          # repo-relative path of en.{md,yml}
    dst: str          # repo-relative path of {lang}.{ext} to create
    lang: str         # target language code
    lang_name: str    # human name (for prompt)
    ext: str          # "md" | "yml"
    content_type: str # courses | tutorials | resources | professors | events
    subtype: str      # course | quizz | tutorial | resource | professor | event
    src_bytes: int    # size of the English source
    long_form: bool   # markdown above the long_form threshold -> chunk by chapter


def load_config(path: Path | None = None) -> dict:
    cfg_path = path or (SCRIPT_DIR / "config.yml")
    with open(cfg_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _classify(rel: Path, ext: str) -> tuple[str, str]:
    parts = rel.parts
    content_type = parts[0] if parts else "unknown"
    if content_type == "courses":
        subtype = "quizz" if "quizz" in parts else "course"
    elif content_type == "tutorials":
        subtype = "tutorial"
    elif content_type == "resources":
        subtype = "resource"
    elif content_type == "professors":
        subtype = "professor"
    elif content_type == "events":
        subtype = "event"
    else:
        subtype = content_type
    return content_type, subtype


def scan(
    config: dict,
    repo_root: Path,
    langs: list[str] | None = None,
    content: list[str] | None = None,
    subtype: list[str] | None = None,
    limit: int | None = None,
) -> list[WorkItem]:
    lang_map = {l["code"]: l["name"] for l in config["languages"]}
    target_langs = langs or list(lang_map.keys())
    unknown = [l for l in target_langs if l not in lang_map]
    if unknown:
        raise SystemExit(f"Unknown language codes: {unknown}. Known: {sorted(lang_map)}")

    roots = content or config["content_roots"]
    exclude = tuple(config.get("exclude_paths", []))
    threshold = int(config.get("long_form_threshold_bytes", 40000))

    items: list[WorkItem] = []
    for root in roots:
        root_dir = repo_root / root
        if not root_dir.is_dir():
            continue
        for name in SOURCE_FILENAMES:
            for src_path in sorted(root_dir.rglob(name)):
                rel = src_path.relative_to(repo_root)
                rel_str = str(rel)
                if any(frag in rel_str for frag in exclude):
                    continue
                ext = name.split(".")[1]
                content_type, sub = _classify(rel, ext)
                if subtype and sub not in subtype:
                    continue
                try:
                    src_bytes = src_path.stat().st_size
                except OSError:
                    src_bytes = 0
                long_form = ext == "md" and src_bytes >= threshold
                for lang in target_langs:
                    dst_path = src_path.parent / f"{lang}.{ext}"
                    if dst_path.exists():
                        continue
                    items.append(
                        WorkItem(
                            src=rel_str,
                            dst=str(dst_path.relative_to(repo_root)),
                            lang=lang,
                            lang_name=lang_map[lang],
                            ext=ext,
                            content_type=content_type,
                            subtype=sub,
                            src_bytes=src_bytes,
                            long_form=long_form,
                        )
                    )
    # Stable, useful ordering: heavy long-form first so the slow work starts early.
    items.sort(key=lambda w: (not w.long_form, w.content_type, w.src, w.lang))
    if limit is not None:
        items = items[:limit]
    return items


def summarize(items: list[WorkItem]) -> dict:
    by_lang: dict[str, int] = {}
    by_type: dict[str, int] = {}
    long_form = 0
    for w in items:
        by_lang[w.lang] = by_lang.get(w.lang, 0) + 1
        by_type[w.subtype] = by_type.get(w.subtype, 0) + 1
        long_form += int(w.long_form)
    return {"total": len(items), "by_lang": by_lang, "by_type": by_type, "long_form": long_form}


def _parse_csv(val: str | None) -> list[str] | None:
    if not val:
        return None
    return [x.strip() for x in val.split(",") if x.strip()]


def main() -> None:
    p = argparse.ArgumentParser(description="Find content missing a translation.")
    p.add_argument("--langs", help="comma-separated language codes (default: all)")
    p.add_argument("--content", help="comma-separated content roots (default: all)")
    p.add_argument("--subtype", help="comma-separated subtypes: course,quizz,tutorial,resource,professor,event")
    p.add_argument("--limit", type=int, help="cap the number of work items")
    p.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    p.add_argument("--config", type=Path, help="path to config.yml")
    p.add_argument("--json", action="store_true", help="emit the work list as JSON")
    args = p.parse_args()

    config = load_config(args.config)
    items = scan(
        config,
        repo_root=args.repo_root.resolve(),
        langs=_parse_csv(args.langs),
        content=_parse_csv(args.content),
        subtype=_parse_csv(args.subtype),
        limit=args.limit,
    )

    if args.json:
        json.dump([asdict(w) for w in items], sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    s = summarize(items)
    print(f"Missing translations: {s['total']} work items  ({s['long_form']} long-form md)")
    if not items:
        print("Nothing to translate. \u2705")
        return
    print("\nBy content type:")
    for t, n in sorted(s["by_type"].items(), key=lambda kv: -kv[1]):
        print(f"  {t:<10} {n}")
    print("\nBy language:")
    for l, n in sorted(s["by_lang"].items(), key=lambda kv: -kv[1]):
        print(f"  {l:<8} {n}")


if __name__ == "__main__":
    main()
