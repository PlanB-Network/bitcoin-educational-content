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
import re
import shutil
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
import usage  # noqa: E402

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


def remove_worktree(repo_root: Path, worktree: Path) -> None:
    subprocess.run(["git", "worktree", "remove", "--force", str(worktree)],
                   cwd=str(repo_root), capture_output=True, text=True)


def _worktree_for_branch(repo_root: Path, branch: str) -> Path | None:
    """Path of an existing worktree that has `branch` checked out, or None."""
    out = subprocess.run(["git", "worktree", "list", "--porcelain"],
                         cwd=str(repo_root), capture_output=True, text=True).stdout
    cur: str | None = None
    for line in out.splitlines():
        if line.startswith("worktree "):
            cur = line[len("worktree "):].strip()
        elif line.strip() == f"branch refs/heads/{branch}":
            return Path(cur) if cur else None
    return None


def attach_worktree(repo_root: Path, branch: str, worktree_base: str) -> tuple[Path, bool]:
    """Check out an existing (published) branch in a worktree so we can update it.
    Reuses a worktree that already has the branch checked out; otherwise fetches
    origin and creates one (fast-forwarding a stale local branch to the PR head).
    Returns (path, reused)."""
    subprocess.run(["git", "fetch", "origin", branch], cwd=str(repo_root),
                   capture_output=True, text=True)  # best-effort; branch may be local-only
    existing = _worktree_for_branch(repo_root, branch)
    if existing and existing.exists():
        return existing.resolve(), True
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = (repo_root / worktree_base.format(ts=ts)).resolve()
    local = subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"refs/heads/{branch}"],
                           cwd=str(repo_root), capture_output=True, text=True).returncode == 0
    if local:
        subprocess.run(["git", "worktree", "add", str(path), branch],
                       cwd=str(repo_root), check=True, capture_output=True, text=True)
        subprocess.run(["git", "merge", "--ff-only", f"origin/{branch}"],
                       cwd=str(path), capture_output=True, text=True)  # sync to PR head if possible
    else:
        subprocess.run(["git", "worktree", "add", "--track", "-b", branch, str(path), f"origin/{branch}"],
                       cwd=str(repo_root), check=True, capture_output=True, text=True)
    return path, False


def find_pr_for_branch(repo_root: Path, branch: str) -> dict | None:
    """Open PR whose head is `branch` (via gh), or None."""
    r = subprocess.run(["gh", "pr", "list", "--head", branch, "--state", "open",
                        "--json", "number,url,title", "--limit", "1"],
                       cwd=str(repo_root), capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        arr = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    return arr[0] if arr else None


def resolve_resume_target(repo_root: Path, target: str, branch_prefix: str) -> tuple[str, dict | None]:
    """Map a --resume value (branch name | PR number | PR URL) to (branch, open_pr|None)."""
    t = target.strip()
    m = re.search(r"/pull/(\d+)", t)
    pr_num = t if t.isdigit() else (m.group(1) if m else None)
    if pr_num:
        r = subprocess.run(["gh", "pr", "view", pr_num, "--json", "number,url,title,headRefName"],
                           cwd=str(repo_root), capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f"Cannot resolve PR {pr_num}: {r.stderr.strip()}")
        pr = json.loads(r.stdout)
        return pr["headRefName"], {"number": pr["number"], "url": pr["url"], "title": pr["title"]}
    return t, find_pr_for_branch(repo_root, t)


def list_batches(repo_root: Path, branch_prefix: str) -> list[dict]:
    """Published auto-translate branches (local + remote) with open PR + local worktree."""
    branches: set[str] = set()
    for cmd in (["git", "branch", "--list", f"{branch_prefix}/*", "--format=%(refname:short)"],
                ["git", "branch", "-r", "--list", f"origin/{branch_prefix}/*", "--format=%(refname:short)"]):
        out = subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True).stdout
        for ln in out.splitlines():
            b = ln.strip().removeprefix("origin/")
            if b:
                branches.add(b)
    rows: list[dict] = []
    for b in sorted(branches):
        wt = _worktree_for_branch(repo_root, b)
        rows.append({"branch": b, "pr": find_pr_for_branch(repo_root, b),
                     "worktree": str(wt) if wt else None})
    return rows


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
                 report_path: Path, model: str, timeout: int,
                 existing_pr: dict | None = None) -> int:
    prompt = (PROMPTS_DIR / "pr_agent.md").read_text(encoding="utf-8")
    if existing_pr:
        pr_line = (
            f"A PR ALREADY EXISTS for this branch: #{existing_pr['number']} ({existing_pr['url']}). "
            f"Do NOT open a new PR. After committing and pushing, add a concise comment to PR "
            f"#{existing_pr['number']} summarising what changed (files added/retried, updated verify "
            f"tally) with `gh pr comment {existing_pr['number']} --body ...`."
        )
    else:
        pr_line = f"Validate the batch, drop FAIL files, commit, push, and open ONE PR against {base}."
    message = (
        f"Batch summary:\n{summary_text}\n\n"
        f"Verify report (JSON) is at this absolute path (read it, it is OUTSIDE the "
        f"worktree — do not commit it): {report_path}\n"
        f"Branch '{branch}' is already checked out here. Base branch: '{base}'.\n"
        f"{pr_line}"
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

PROVIDER_FALLBACK = {"anthropic": "sonnet", "openai": "gpt-5.5"}


def filter_route_by_provider(route: list[dict], provider: str | None, config: dict) -> list[dict]:
    """Keep only steps whose model belongs to `provider` (anthropic|openai).
    `both`/None -> unchanged. If the chain has no model for the provider (e.g. the
    `default` chain under --provider openai), fall back to the provider's default
    model (config `models.provider_fallback`), preserving the primary step's effort."""
    if not provider or provider == "both":
        return route
    kept = [s for s in route if usage.provider_of(s["model"]) == provider]
    if kept:
        return kept
    fallback = config["models"].get("provider_fallback", PROVIDER_FALLBACK).get(provider)
    if not fallback:
        return route
    return [{"model": fallback, "thinking": route[0].get("thinking", "medium")}]


def route_for(config: dict, lang: str, override_model: str | None = None,
              override_thinking: str | None = None, provider: str | None = None) -> list[dict]:
    """Ordered list of {model, thinking} for a language: [#1 primary, #2, #3 …].
    Retry walks down this chain, so a fallback model is tried on FAIL. `provider`
    (anthropic|openai) restricts the chain to that provider's models; both/None = full chain."""
    if override_model:
        return [{"model": override_model, "thinking": override_thinking or "medium"}]
    r = config["models"].get("routes", {}).get(lang) or config["models"]["default"]
    route = [r] if isinstance(r, dict) else r
    return filter_route_by_provider(route, provider, config)


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


def _prompt_provider(args) -> None:
    print("\nProvider :")
    print("  1) both — chaîne de routage complète (défaut)")
    print("  2) anthropic — sonnet/opus")
    print("  3) openai — gpt-5.5")
    args.provider = {"2": "anthropic", "3": "openai"}.get(input("Choix [1-3] : ").strip(), "both")


def _manage_menu(args, config: dict) -> None:
    """List published batches; retry (update the PR) or remove a local worktree."""
    repo_root = args.repo_root.resolve()
    rows = list_batches(repo_root, config["branch_prefix"])
    if not rows:
        sys.exit("Aucun batch auto-translate publié trouvé.")
    print("\nBatchs publiés :")
    for i, row in enumerate(rows, 1):
        pr = row["pr"]
        pr_s = f"PR #{pr['number']} {pr['title']}" if pr else "aucune PR ouverte"
        wt_s = "  · worktree local" if row["worktree"] else ""
        print(f"  {i}) {row['branch']}  ({pr_s}){wt_s}")
    sel = input(f"Batch [1-{len(rows)}] : ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(rows)):
        sys.exit("Sélection invalide.")
    row = rows[int(sel) - 1]
    print("\nAction :")
    print("  1) Relancer les fichiers manquants (retry) → met à jour la PR")
    print("  2) Supprimer le worktree local (cleanup)")
    if input("Choix [1-2] : ").strip() == "2":
        if not row["worktree"]:
            sys.exit("Pas de worktree local à supprimer pour ce batch.")
        remove_worktree(repo_root, Path(row["worktree"]))
        sys.exit(f"Worktree supprimé : {row['worktree']}")
    args.resume = row["branch"]
    args.langs = input("Langues csv (vide=toutes les manquantes) : ").strip() or None
    args.path = input("Path (vide=tout le contenu manquant) : ").strip() or None
    _prompt_provider(args)


def interactive_menu(args, config: dict) -> None:
    """Prompt for a batch scope and mutate `args` in place."""
    print("\n=== agent-translate — lancement interactif ===")
    print("\nType de batch :")
    print("  1) Un cours — toutes les langues manquantes")
    print("  2) Un cours — langues au choix")
    print("  3) Une langue — tout le contenu manquant")
    print("  4) Scope personnalisé")
    print("  5) Gérer / relancer un batch publié (PR existante)")
    c = input("Choix [1-5] : ").strip()
    if c == "5":
        _manage_menu(args, config)
        return
    if c == "1":
        args.path = "courses/" + input("Cours (ex. scr403) : ").strip()
    elif c == "2":
        args.path = "courses/" + input("Cours (ex. scr403) : ").strip()
        args.langs = input("Langues csv (ex. fr,de) : ").strip() or None
    elif c == "3":
        args.langs = input("Langue (ex. fr) : ").strip() or None
        args.content = input("Content roots csv (vide=tous) : ").strip() or None
    else:
        args.path = input("Path (vide=tous) : ").strip() or None
        args.langs = input("Langues csv (vide=toutes) : ").strip() or None
        args.content = input("Content csv (vide=tous) : ").strip() or None
        args.subtype = input("Subtype csv (vide=tous) : ").strip() or None
    _prompt_provider(args)
    if input("Ouvrir une PR à la fin ? [O/n] : ").strip().lower() == "n":
        args.no_pr = True


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
    p.add_argument("--provider", choices=["anthropic", "openai", "both"], default="both",
                   help="restrict routing to one provider's models (anthropic=sonnet/opus, openai=gpt-5.5; default: both)")
    p.add_argument("--timeout", type=int, default=1200, help="per-worker timeout seconds")
    p.add_argument("--retries", type=int, default=2, help="retry passes over FAILs (walks the fallback chain)")
    p.add_argument("--base", default="dev", help="base branch for the worktree/PR")
    p.add_argument("--resume", metavar="BRANCH|PR",
                   help="update an existing published batch: attach its branch, translate what is "
                        "still missing, push to the SAME branch and update its PR (accepts a branch "
                        "name, a PR number, or a PR URL)")
    p.add_argument("--list-batches", action="store_true",
                   help="list published auto-translate branches + their PRs and worktrees, then exit")
    p.add_argument("--dry-run", action="store_true", help="show the work list and exit")
    p.add_argument("--in-place", action="store_true", help="translate in the current checkout (no worktree)")
    p.add_argument("--no-pr", action="store_true", help="skip the release agent / PR step")
    p.add_argument("--keep-worktree", action="store_true", help="do not remove the worktree afterward")
    p.add_argument("--max-items", type=int, default=500, help="safety cap; use --force to exceed")
    p.add_argument("--force", action="store_true", help="allow batches larger than --max-items")
    p.add_argument("--batch-size", type=int, help="small-file batch size per session (default: config 15)")
    p.add_argument("--interactive", action="store_true", help="interactive menu to pick the batch + live progress/usage")
    p.add_argument("--usage-threshold", type=float, default=80, help="freeze when ALL in-use subs reach this pct of the 5h window")
    p.add_argument("--usage-hard", type=float, default=95, help="freeze when ANY in-use sub reaches this pct (backstop)")
    p.add_argument("--no-usage-gate", action="store_true", help="disable subscription-usage gating")
    p.add_argument("--repo-root", type=Path, default=find_missing.DEFAULT_REPO_ROOT)
    args = p.parse_args()

    config = find_missing.load_config()
    repo_root = args.repo_root.resolve()
    concurrency = args.concurrency or int(config.get("concurrency", 8))
    if args.model and args.provider != "both" and usage.provider_of(args.model) != args.provider:
        print(f"Note: --model {args.model} ({usage.provider_of(args.model)}) overrides --provider {args.provider}.")
    if args.interactive:
        interactive_menu(args, config)

    if args.list_batches:
        for row in list_batches(repo_root, config["branch_prefix"]):
            pr = row["pr"]
            pr_s = f"PR #{pr['number']} {pr['title']}" if pr else "no open PR"
            wt_s = f" · worktree {row['worktree']}" if row["worktree"] else ""
            print(f"  {row['branch']:<28} {pr_s}{wt_s}")
        return

    # Resume: reattach to an existing published batch (branch + PR) instead of
    # branching fresh from base. Scan the WORKTREE so we see what that branch still
    # lacks (e.g. the FAIL files the release agent dropped), and update the PR in place.
    resume = bool(args.resume)
    existing_pr: dict | None = None
    worktree: Path | None = None
    branch: str | None = None
    reused_worktree = False
    scan_root = repo_root
    if resume:
        if args.in_place:
            sys.exit("--resume and --in-place are mutually exclusive.")
        branch, existing_pr = resolve_resume_target(repo_root, args.resume, config["branch_prefix"])
        worktree, reused_worktree = attach_worktree(repo_root, branch, config["worktree_base"])
        scan_root = worktree
        pr_desc = (f"PR #{existing_pr['number']} ({existing_pr['url']})" if existing_pr
                   else "no open PR — a new one will be opened")
        print(f"Resuming branch {branch} · {pr_desc}\n"
              f"Worktree {'reused' if reused_worktree else 'created'}: {worktree}")

    items = [asdict(w) for w in find_missing.scan(
        config, repo_root=scan_root,
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
            m, th = pick(route_for(config, it["lang"], args.model, args.thinking, args.provider), 0)
            print(f"  · {it['dst']}  [{m} · {th}]")
        if len(items) > 20:
            print(f"  … +{len(items)-20} more")
        if resume and not reused_worktree:
            remove_worktree(repo_root, worktree)
        return

    if not items:
        print("Nothing to translate. \u2705")
        if resume and not reused_worktree:
            remove_worktree(repo_root, worktree)
        return

    if len(items) > args.max_items and not args.force and not args.interactive:
        sys.exit(f"Refusing to run {len(items)} items (> --max-items {args.max_items}). "
                 f"Scope with --langs/--content/--limit or pass --force.")
    # Subscription-usage governor (freezes the batch near the 5h window cap).
    in_use = set()
    for it in items:
        for step in route_for(config, it["lang"], args.model, args.thinking, args.provider):
            in_use.add(usage.provider_of(step["model"]))
    in_use.discard("unknown")
    governor = usage.Governor(in_use, threshold=args.usage_threshold, hard=args.usage_hard,
                              enabled=not args.no_usage_gate, log=print)
    governor.preflight()

    if args.interactive:
        n_sessions = len(make_jobs(items, args.batch_size or int(config.get("batch_size", 15))))
        if resume:
            pr_note = f"update PR #{existing_pr['number']}" if existing_pr else "open new PR"
        else:
            pr_note = "no PR" if args.no_pr else f"1 PR -> {args.base}"
        print(f"\n{len(items)} fichiers · {n_sessions} sessions omp · concurrence {concurrency} · "
              f"providers {sorted(in_use) or ['?']} · {pr_note}")
        if input("Lancer ? [o/N] : ").strip().lower() not in ("o", "y", "oui"):
            print("Annulé.")
            if resume and not reused_worktree:
                remove_worktree(repo_root, worktree)
            return


    # Workspace
    if resume:
        print(f"Translating on branch {branch} in {worktree}.")
    elif args.in_place:
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
    sessions_dir = worktree.parent / f"{worktree.name}.sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    pct_before = usage.percents(governor.fresh())

    # Group work into omp sessions; small YAML files are batched per language (a4).
    def dispatch(jobs: list[list[dict]], attempt: int = 0) -> None:
        total, done = len(jobs), 0
        with cf.ThreadPoolExecutor(max_workers=concurrency) as pool:
            job_iter = iter(jobs)
            job_of: dict = {}
            pending: set = set()

            def fill():
                while len(pending) < concurrency:
                    job = next(job_iter, None)
                    if job is None:
                        break
                    governor.gate()  # blocks new launches while in-use subs are capped
                    m, th = pick(route_for(config, job[0]["lang"], args.model, args.thinking, args.provider), attempt)
                    fut = pool.submit(
                        worker.translate_job, job, worktree=worktree, model=m, thinking=th,
                        system_prompt=system_prompt, knowledge_dir=knowledge_dir,
                        lessons_root=lessons_root, session_dir=sessions_dir, timeout=args.timeout)
                    pending.add(fut)
                    job_of[fut] = job

            fill()
            while pending:
                dset, _ = cf.wait(pending, return_when=cf.FIRST_COMPLETED)
                for fut in dset:
                    pending.discard(fut)
                    job = job_of.pop(fut)
                    r = fut.result()
                    done += 1
                    st = "ok" if r["ok"] else "FAIL"
                    label = job[0]["dst"] if len(job) == 1 else f"{job[0]['lang']} batch×{len(job)}"
                    note = "" if r["ok"] else f"  ({r['error']})"
                    print(f"[{done}/{total}] {st:>4} {label} {r['duration']}s{note}  · {governor.status_line()}")
                fill()

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
    report_path = (worktree / REPORT_NAME) if args.in_place else worktree.parent / f"{worktree.name}.report.json"
    report_path.write_text(
        json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")

    # Consolidate lessons into the persistent knowledge base
    added = consolidate_lessons(lessons_root, knowledge_dir)
    if not args.in_place:
        shutil.rmtree(lessons_root, ignore_errors=True)  # scratch never enters the PR

    # Per-batch usage log: token in/out per model + %-consumption per provider.
    pct_after = usage.percents(governor.fresh(force=True))
    per_model = usage.aggregate_sessions(sessions_dir)
    providers = {sub: {
        "5h_before": pct_before[sub]["5h"], "5h_after": pct_after[sub]["5h"],
        "5h_delta": round(pct_after[sub]["5h"] - pct_before[sub]["5h"], 1),
        "weekly_before": pct_before[sub]["weekly"], "weekly_after": pct_after[sub]["weekly"],
        "weekly_delta": round(pct_after[sub]["weekly"] - pct_before[sub]["weekly"], 1),
    } for sub in usage.SUBS}
    cost_total = round(sum(m["cost"] for m in per_model.values()), 4)
    usage_log = {"ts": datetime.now().isoformat(timespec="seconds"),
                 "scope": {"langs": args.langs, "content": args.content,
                           "subtype": args.subtype, "path": args.path},
                 "files": len(items), "wall_s": round(time.time() - t0),
                 "cost_total": cost_total, "per_model": per_model, "providers": providers}
    usage_log_path = worktree.parent / f"{worktree.name}.usage.json"
    usage_log_path.write_text(json.dumps(usage_log, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n── usage ──")
    for model, m in sorted(per_model.items()):
        print(f"  {model:<20} in {m['input']:>8} · out {m['output']:>7} · "
              f"cacheR {m['cacheRead']:>9} · cacheW {m['cacheWrite']:>10} · ${m['cost']:.2f} ({m['messages']} msg)")
    for sub in usage.SUBS:
        p = providers[sub]
        print(f"  {sub:<10} 5h {p['5h_before']:.0f}%→{p['5h_after']:.0f}% (Δ{p['5h_delta']:+.1f}) · "
              f"weekly {p['weekly_before']:.0f}%→{p['weekly_after']:.0f}% (Δ{p['weekly_delta']:+.1f})")
    print(f"  total cost ≈ ${cost_total:.2f}  · usage log: {usage_log_path}")
    shutil.rmtree(sessions_dir, ignore_errors=True)

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
        print(f"\nSkipping PR. Report: {report_path}")
        if branch:
            print(f"Worktree kept at {worktree} on {branch}.")
        return

    print("\nHanding off to release agent …")
    rc = run_pr_agent(worktree, branch, args.base, summary_text, report_path,
                      model=route_for(config, "__default__", provider=args.provider)[0]["model"],
                      timeout=args.timeout, existing_pr=existing_pr)
    if rc != 0:
        print(f"Release agent exited {rc}; worktree kept at {worktree} on {branch}.")
        return

    if not args.keep_worktree and not reused_worktree:
        remove_worktree(repo_root, worktree)
        action = f"updated PR #{existing_pr['number']}" if existing_pr else "PR"
        print(f"Worktree {worktree} removed. Branch {branch} pushed with {action}.")
    else:
        why = "reused pre-existing" if reused_worktree else "kept (--keep-worktree)"
        print(f"Worktree {why}: {worktree} on {branch}.")


if __name__ == "__main__":
    main()
