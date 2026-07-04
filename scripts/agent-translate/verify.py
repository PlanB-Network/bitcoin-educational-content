#!/usr/bin/env python3
"""Deterministic verification of a translated file against its English source.

This is the safety net that replaces the old ``find_untranslated.py`` heuristic.
It does NOT trust the model — it computes structural parity between source and
translation and rejects mismatches.

Severity:
  FAIL  — structural break: missing/empty output, invalid YAML, heading or code
          count mismatch, YAML key-structure mismatch, changed verbatim identifier.
  WARN  — soft signal: link/image count drift, high identical-line ratio
          (possible untranslated content).
  PASS  — all checks clean.

Usage:
    python3 verify.py <src> <dst>                 # one pair, human output
    python3 verify.py --pairs work.json --json    # batch, JSON report
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent

# Values of these keys must be byte-identical between source and translation.
VERBATIM_KEYS = {
    "partId", "chapterId", "video_id", "isCourseExam", "isCourseReview",
    "isCourseConclusion", "contributors", "cover", "original", "reviewed",
    "website", "github", "telegram", "twitter", "nostr", "lightning_address",
    "isbn", "publication_year", "author", "url", "id", "level", "tags",
}

_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")



# ---------- markdown helpers ----------

def _split_frontmatter(text: str) -> tuple[dict | None, str]:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_block = text[text.find("\n") + 1 : end]
            body = text[end + 4 :]
            try:
                return (yaml.safe_load(fm_block) or {}), body
            except yaml.YAMLError:
                return None, text
    return {}, text


def _md_signature(text: str) -> dict:
    headings = sum(1 for ln in text.splitlines() if _HEADING_RE.match(ln))
    fence_lines = sum(1 for ln in text.splitlines() if ln.lstrip().startswith("```"))
    return {
        "headings": headings,
        "fence_lines": fence_lines,
        "images": text.count("!["),
        "link_parens": text.count("]("),
    }


def _identical_ratio(src: str, dst: str) -> float:
    """Ratio of dst text lines that appear verbatim in src (untranslated signal)."""
    def texty(s: str) -> list[str]:
        out = []
        for ln in s.splitlines():
            t = ln.strip()
            if len(t) >= 12 and not t.startswith(("|", "#", "```", "![", "-", "*", ">")):
                out.append(t)
        return out
    dst_lines = texty(dst)
    if not dst_lines:
        return 0.0
    src_set = set(texty(src))
    same = sum(1 for ln in dst_lines if ln in src_set)
    return same / len(dst_lines)


# ---------- yaml helpers ----------

def _structure_sig(obj):
    if isinstance(obj, dict):
        return {k: _structure_sig(obj[k]) for k in sorted(obj)}
    if isinstance(obj, list):
        return [_structure_sig(x) for x in obj]
    return type(obj).__name__


def _collect_verbatim(obj, out: dict, path: str = "") -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in VERBATIM_KEYS and not isinstance(v, (dict, list)):
                out[f"{path}/{k}"] = v
            _collect_verbatim(v, out, f"{path}/{k}")
    elif isinstance(obj, list):
        for i, x in enumerate(obj):
            _collect_verbatim(x, out, f"{path}[{i}]")


# ---------- pair check ----------


def check_pair(src_path: Path, dst_path: Path, ext: str) -> dict:
    checks: list[dict] = []

    def add(name, sev, detail):
        checks.append({"name": name, "severity": sev, "detail": detail})

    if not dst_path.exists():
        add("output_exists", "FAIL", "translated file was not created")
        return _finalize(dst_path, checks)

    src = src_path.read_text(encoding="utf-8", errors="replace")
    dst = dst_path.read_text(encoding="utf-8", errors="replace")

    if not dst.strip():
        add("non_empty", "FAIL", "translated file is empty")
        return _finalize(dst_path, checks)

    if ext == "yml":
        try:
            src_obj = yaml.safe_load(src)
        except yaml.YAMLError as e:
            src_obj = None
            add("src_yaml", "WARN", f"source YAML did not parse: {e}")
        try:
            dst_obj = yaml.safe_load(dst)
        except yaml.YAMLError as e:
            add("dst_yaml_valid", "FAIL", f"translated YAML does not parse: {e}")
            return _finalize(dst_path, checks)
        if src_obj is not None:
            if _structure_sig(src_obj) != _structure_sig(dst_obj):
                add("yaml_structure", "FAIL", "key structure / list lengths differ from source")
            src_vb, dst_vb = {}, {}
            _collect_verbatim(src_obj, src_vb)
            _collect_verbatim(dst_obj, dst_vb)
            if src_vb != dst_vb:
                diff = [k for k in src_vb if src_vb.get(k) != dst_vb.get(k)]
                add("verbatim_ids", "FAIL", f"non-translatable values changed: {diff[:6]}")
    else:  # markdown
        src_fm, src_body = _split_frontmatter(src)
        dst_fm, dst_body = _split_frontmatter(dst)
        if src_fm is None or dst_fm is None:
            add("frontmatter_parse", "WARN", "frontmatter did not parse cleanly")
        else:
            if set(src_fm.keys()) != set(dst_fm.keys()):
                add("frontmatter_keys", "FAIL",
                    f"frontmatter keys differ: +{set(dst_fm)-set(src_fm)} -{set(src_fm)-set(dst_fm)}")
            src_vb, dst_vb = {}, {}
            _collect_verbatim(src_fm, src_vb)
            _collect_verbatim(dst_fm, dst_vb)
            if src_vb != dst_vb:
                diff = [k for k in src_vb if src_vb.get(k) != dst_vb.get(k)]
                add("verbatim_ids", "FAIL", f"non-translatable frontmatter changed: {diff[:6]}")

        s, d = _md_signature(src), _md_signature(dst)
        if s["headings"] != d["headings"]:
            add("headings", "FAIL", f"heading count {d['headings']} != source {s['headings']}")
        if s["fence_lines"] != d["fence_lines"]:
            add("code_fences", "FAIL", f"code-fence lines {d['fence_lines']} != source {s['fence_lines']}")
        if s["images"] != d["images"]:
            add("images", "WARN", f"image count {d['images']} != source {s['images']}")
        if s["link_parens"] != d["link_parens"]:
            add("links", "WARN", f"link count {d['link_parens']} != source {s['link_parens']}")

        ratio = _identical_ratio(src, dst)
        if ratio > 0.5:
            add("untranslated", "WARN", f"{ratio:.0%} of text lines identical to English")

    return _finalize(dst_path, checks)


def _finalize(dst_path: Path, checks: list[dict]) -> dict:
    sev = "PASS"
    if any(c["severity"] == "FAIL" for c in checks):
        sev = "FAIL"
    elif any(c["severity"] == "WARN" for c in checks):
        sev = "WARN"
    return {"path": str(dst_path), "status": sev, "checks": checks}


def main() -> None:
    p = argparse.ArgumentParser(description="Verify translated files structurally.")
    p.add_argument("src", nargs="?", help="source en.{md,yml}")
    p.add_argument("dst", nargs="?", help="translated {lang}.{ext}")
    p.add_argument("--pairs", type=Path, help="JSON list of {src,dst,ext} (repo-relative)")
    p.add_argument("--repo-root", type=Path, default=Path.cwd())
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    results: list[dict] = []

    if args.pairs:
        items = json.loads(args.pairs.read_text())
        root = args.repo_root.resolve()
        for it in items:
            ext = it.get("ext") or it["src"].rsplit(".", 1)[-1]
            results.append(check_pair(root / it["src"], root / it["dst"], ext))
    elif args.src and args.dst:
        src, dst = Path(args.src), Path(args.dst)
        ext = dst.suffix.lstrip(".")
        results.append(check_pair(src, dst, ext))
    else:
        p.error("provide <src> <dst> or --pairs FILE")

    if args.json:
        json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        tally = {"PASS": 0, "WARN": 0, "FAIL": 0}
        for r in results:
            tally[r["status"]] += 1
            if r["status"] != "PASS":
                print(f"[{r['status']}] {r['path']}")
                for c in r["checks"]:
                    if c["severity"] != "PASS":
                        print(f"    {c['severity']}: {c['name']} — {c['detail']}")
        print(f"\n{tally['PASS']} PASS · {tally['WARN']} WARN · {tally['FAIL']} FAIL")

    if any(r["status"] == "FAIL" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
