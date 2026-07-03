#!/usr/bin/env python3
"""Agent-driven translation orchestrator.

Pipeline:
  1. Deterministic gap-check (find_missing) -> work list of (content x language).
  2. Create a dedicated git worktree + branch for the batch (one batch = one PR).
  3. Dispatch a bounded pool of headless omp workers; small files batched per language.
  4. Verify every produced file structurally (verify.check_pair).
  5. Consolidate per-worker lessons into knowledge/<lang>.md (race-free).
  6. Hand the worktree to a final headless omp release agent: validate, commit,
     push, open ONE PR.

Examples:
  python3 translate.py --dry-run --langs fr,de
  python3 translate.py --langs fr --content courses --limit 3
  python3 translate.py --in-place --no-pr --langs fr --limit 1     # local smoke test
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import subprocess
import sys
import time
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import find_missing  # noqa: E402
import verify  # noqa: E402
import worker  # noqa: E402

KNOWLEDGE_SUBPATH = "scripts/agent-translate/knowledge"  # under the worktree -> lands in the PR
PROMPTS_DIR = SCRIPT_DIR / "prompts"
LESSONS_DIRNAME = ".translation-lessons"
REPORT_NAME = ".translation-report.json"


# ---------------- git worktree ----------------

def create_worktree(repo_root: Path, base: str, worktree_base: str, branch_prefix: str) -> tuple[Path, str]:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    branch = f"{branch_prefix}/{ts}"
    path = (repo_root / worktree_base.format(ts=ts)).resolve()
    subprocess.run(
        ["git", "worktree", "add", str(path), "-b", branch, base],
        cwd=str(repo_root), check=True, capture_output=True, text=True,
    )
    return path, branch


# ---------------- lessons consolidation ----------------

def _existing_bullets(text: str) -> set[str]:
    return {ln.strip() for ln in text.splitlines() if ln.strip().startswith("- ")}


def consolidate_lessons(lessons_root: Path, knowledge_dir: Path) -> dict[str, int]:
    """Merge per-worker scratch lessons into knowledge/<lang>.md, deduplicated."""
    added: dict[str, int] = {}
    if not lessons_root.exists():
        return added
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d")
    for lang_dir in sorted(lessons_root.iterdir()):
        if not lang_dir.is_dir():
            continue
        lang = lang_dir.name
        bullets: list[str] = []
        for scratch in sorted(lang_dir.glob("*.md")):
            for ln in scratch.read_text(encoding="utf-8", errors="replace").splitlines():
                if ln.strip().startswith("- "):
                    bullets.append(ln.strip())
        if not bullets:
            continue
        kfile = knowledge_dir / f"{lang}.md"
        prior = kfile.read_text(encoding="utf-8") if kfile.exists() else f"# Lessons — {lang}\n"
        seen = _existing_bullets(prior)
        fresh = [b for b in dict.fromkeys(bullets) if b not in seen]
        if not fresh:
            continue
        block = f"\n## {ts}\n" + "\n".join(fresh) + "\n"
        kfile.write_text(prior.rstrip() + "\n" + block, encoding="utf-8")
        added[lang] = len(fresh)
    return added


# ---------------- release agent ----------------

def run_pr_agent(worktree: Path, branch: str, base: str, summary_text: str,
                 report_rel: str, model: str, timeout: int) -> int:
    prompt = (PROMPTS_DIR / "pr_agent.md").read_text(encoding="utf-8")
    message = (
        f"Batch summary:\n{summary_text}\n\n"
        f"Verify report (JSON, repo-relative): {report_rel}\n"
        f"Branch '{branch}' is already checked out here. Base branch: '{base}'.\n"
        f"Validate the batch, drop FAIL files, commit, push, and open ONE PR against {base}."
    )
    cmd = [
        "omp", "-p", "--no-session", "--auto-approve", "--no-lsp", "--no-title",
        "--cwd", str(worktree), "--model", model, "--thinking", "low",
        "--tools", "read,grep,glob,bash",
        "--append-system-prompt", prompt, message,
    ]
    proc = subprocess.run(cmd, cwd=str(worktree), text=True)
    return proc.returncode


# ---------------- main ----------------

def route_for(config: dict, lang: str, override_model: str | None = None,
              override_thinking: str | None = None) -> list[dict]:
    """Ordered list of {model, thinking} for a language: [#1 primary, #2, #3 …].
    Retry walks down this chain, so a fallback model is tried on FAIL."""
    if override_model:
        return [{"model": override_model, "thinking": override_thinking or "medium"}]
    r = config["models"].get("routes", {}).get(lang) or config["models"]["default"]
    return [r] if isinstance(r, dict) else r


def pick(route: list[dict], attempt: int) -> tuple[str, str]:
    step = route[min(attempt, len(route) - 1)]
    return step["model"], step.get("thinking", "medium")


def make_jobs(items: list[dict], batch_size: int) -> list[list[dict]]:
    """Group work into omp sessions. Markdown (courses / long-form) = one file per
    job. Small YAML files are packed per-language into batches of `batch_size`."""
    singles: list[list[dict]] = []
    smalls: dict[str, list[dict]] = {}
    for it in items:
        if it["ext"] == "md":
            singles.append([it])
        else:
            smalls.setdefault(it["lang"], []).append(it)
    jobs = list(singles)
    for group in smalls.values():
        for i in range(0, len(group), batch_size):
            jobs.append(group[i:i + batch_size])
    return jobs


def main() -> None:
    p = argparse.ArgumentParser(description="Agent-driven translation orchestrator.")
    p.add_argument("--langs", help="comma-separated target languages (default: all)")
    p.add_argument("--content", help="comma-separated content roots (default: all)")
    p.add_argument("--subtype", help="comma-separated subtypes (course,quizz,tutorial,resource,professor,event)")
    p.add_argument("--path", help="scope to a specific content path (folder subtree or one en.md/en.yml)")
    p.add_argument("--limit", type=int, help="cap number of work items")
    p.add_argument("--concurrency", type=int, help="max parallel workers (default: config)")
    p.add_argument("--model", help="force one model for every worker (overrides routing)")
    p.add_argument("--thinking", help="thinking effort when --model is set (default: medium)")
    p.add_argument("--timeout", type=int, default=1200, help="per-worker timeout seconds")
    p.add_argument("--retries", type=int, default=2, help="retry passes over FAILs (walks the fallback chain)")
    p.add_argument("--base", default="dev", help="base branch for the worktree/PR")
    p.add_argument("--dry-run", action="store_true", help="show the work list and exit")
    p.add_argument("--in-place", action="store_true", help="translate in the current checkout (no worktree)")
    p.add_argument("--no-pr", action="store_true", help="skip the release agent / PR step")
    p.add_argument("--keep-worktree", action="store_true", help="do not remove the worktree afterward")
    p.add_argument("--max-items", type=int, default=500, help="safety cap; use --force to exceed")
    p.add_argument("--force", action="store_true", help="allow batches larger than --max-items")
    p.add_argument("--batch-size", type=int, help="small-file batch size per session (default: config 15)")
    p.add_argument("--repo-root", type=Path, default=find_missing.DEFAULT_REPO_ROOT)
    args = p.parse_args()

    config = find_missing.load_config()
    repo_root = args.repo_root.resolve()
    concurrency = args.concurrency or int(config.get("concurrency", 8))

    items = [asdict(w) for w in find_missing.scan(
        config, repo_root=repo_root,
        langs=find_missing._parse_csv(args.langs),
        content=find_missing._parse_csv(args.content),
        subtype=find_missing._parse_csv(args.subtype),
        path=args.path,
        limit=args.limit,
    )]

    s = find_missing.summarize([find_missing.WorkItem(**it) for it in items])
    print(f"Gap-check: {s['total']} work items ({s['long_form']} long-form).")
    for t, n in sorted(s["by_type"].items(), key=lambda kv: -kv[1]):
        print(f"  {t:<10} {n}")

    if args.dry_run:
        for it in items[:20]:
            m, th = pick(route_for(config, it["lang"], args.model, args.thinking), 0)
            print(f"  · {it['dst']}  [{m} · {th}]")
        if len(items) > 20:
            print(f"  … +{len(items)-20} more")
        return

    if not items:
        print("Nothing to translate. \u2705")
        return

    if len(items) > args.max_items and not args.force:
        sys.exit(f"Refusing to run {len(items)} items (> --max-items {args.max_items}). "
                 f"Scope with --langs/--content/--limit or pass --force.")

    # Workspace
    if args.in_place:
        worktree, branch = repo_root, None
        print(f"Translating in place at {worktree} (no worktree).")
    else:
        worktree, branch = create_worktree(
            repo_root, args.base, config["worktree_base"], config["branch_prefix"])
        print(f"Worktree {worktree} on branch {branch} (base {args.base}).")

    lessons_root = worktree / LESSONS_DIRNAME
    system_prompt = (PROMPTS_DIR / "translate.md").read_text(encoding="utf-8")
    knowledge_dir = worktree / KNOWLEDGE_SUBPATH
    batch_size = args.batch_size or int(config.get("batch_size", 15))

    # Group work into omp sessions; small YAML files are batched per language (a4).
    def dispatch(jobs: list[list[dict]], attempt: int = 0) -> None:
        done, total = 0, len(jobs)
        with cf.ThreadPoolExecutor(max_workers=concurrency) as pool:
            futures = {}
            for job in jobs:
                m, th = pick(route_for(config, job[0]["lang"], args.model, args.thinking), attempt)
                futures[pool.submit(
                    worker.translate_job, job,
                    worktree=worktree,
                    model=m,
                    thinking=th,
                    system_prompt=system_prompt,
                    knowledge_dir=knowledge_dir,
                    lessons_root=lessons_root,
                    timeout=args.timeout,
                )] = job
            for fut in cf.as_completed(futures):
                r = fut.result()
                done += 1
                job = r["items"]
                st = "ok" if r["ok"] else "FAIL"
                label = job[0]["dst"] if len(job) == 1 else f"{job[0]['lang']} batch×{len(job)}"
                note = "" if r["ok"] else f"  ({r['error']})"
                print(f"[{done}/{total}] {st:>4} {label} {r['duration']}s{note}")

    def verify_all() -> list[dict]:
        return [
            verify.check_pair(worktree / it["src"], worktree / it["dst"], it["ext"])
            for it in items
        ]

    t0 = time.time()
    dispatch(make_jobs(items, batch_size), 0)
    print("\nVerifying …")
    reports = verify_all()

    # Retry FAILs, walking down the model fallback chain (removes corrupt output first).
    for attempt in range(1, args.retries + 1):
        fails = [items[i] for i, r in enumerate(reports) if r["status"] == "FAIL"]
        if not fails:
            break
        print(f"\nRetry {attempt}/{args.retries} on {len(fails)} FAIL(s) …")
        for it in fails:
            (worktree / it["dst"]).unlink(missing_ok=True)
        dispatch(make_jobs(fails, batch_size), attempt)
        reports = verify_all()

    tally = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for r in reports:
        tally[r["status"]] += 1
    (worktree / REPORT_NAME).write_text(
        json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")

    # Consolidate lessons into the persistent knowledge base
    added = consolidate_lessons(lessons_root, knowledge_dir)

    dt = round(time.time() - t0)
    summary_text = (
        f"{len(items)} units in {dt}s · verify {tally['PASS']} PASS / "
        f"{tally['WARN']} WARN / {tally['FAIL']} FAIL · "
        f"types " + ", ".join(f"{k}:{v}" for k, v in s["by_type"].items())
    )
    print(f"\n{summary_text}")
    if added:
        print("Knowledge updated: " + ", ".join(f"{k}(+{v})" for k, v in added.items()))

    # Release agent
    if args.no_pr or args.in_place:
        print(f"\nSkipping PR. Report: {worktree / REPORT_NAME}")
        if branch:
            print(f"Worktree kept at {worktree} on {branch}.")
        return

    print("\nHanding off to release agent …")
    rc = run_pr_agent(worktree, branch, args.base, summary_text, REPORT_NAME,
                      model=route_for(config, "__default__")[0]["model"], timeout=args.timeout)
    if rc != 0:
        print(f"Release agent exited {rc}; worktree kept at {worktree} on {branch}.")
        return

    if not args.keep_worktree:
        subprocess.run(["git", "worktree", "remove", "--force", str(worktree)],
                       cwd=str(repo_root), capture_output=True, text=True)
        print(f"Worktree {worktree} removed. Branch {branch} pushed with PR.")


if __name__ == "__main__":
    main()
