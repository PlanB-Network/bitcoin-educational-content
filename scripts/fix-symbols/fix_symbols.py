#!/usr/bin/env python3
"""
Parallel Hybrid Markdown Fixer (Stable Bars via Thread Binding)
---------------------------------------------------------------
- ThreadPoolExecutor with 8 workers
- Each real thread permanently mapped to its own tqdm bar
- 9 total bars: 1 global + 8 workers
- Bars reset on each new file for that thread
- Suspicion detection: balance + regex + parser
"""

import os
import re
import threading
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from markdown_it import MarkdownIt
from tqdm import tqdm

try:
    import anthropic
except ImportError:
    print("Error: please install anthropic (pip install anthropic)")
    exit(1)


@dataclass
class Stats:
    files_analyzed: int = 0
    files_corrected: int = 0
    total_corrections: int = 0
    total_attempts: int = 0


class MarkdownFixerHybrid:
    def __init__(self, anthropic_api_key: str):
        self.client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.model = "claude-sonnet-4-20250514"
        self.md = MarkdownIt()

    def _is_suspicious(self, line: str) -> bool:
        if "*" not in line:
            return False

        # 1. Balance check
        double = line.count("**")
        single = line.count("*") - 2 * double
        if single % 2 != 0 or double % 2 != 0:
            return True

        # 2. Regex overlaps
        regex_sus = bool(
            re.search(r"\*\*[^*]+\*", line) or re.search(r"\*[^*]+\*\*", line)
        )
        if not regex_sus:
            return False

        # 3. Parser confirmation
        try:
            tokens = self.md.parse(line)
        except Exception:
            return True

        for t in tokens:
            if t.type == "text" and "*" in t.content:
                return True
        return False

    def _fix_with_claude(self, line: str) -> str:
        system_prompt = (
            "You are a Markdown formatting expert. "
            "Fix unbalanced, mismatched, or nested * or ** markers. "
            "Rules:\n"
            "- Balance all markers\n"
            "- Preserve original wording\n"
            "- Use ** for bold, * for italic\n"
            "Return ONLY the corrected line."
        )
        message = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            temperature=0.1,
            system=system_prompt,
            messages=[{"role": "user", "content": line}],
        )
        return message.content[0].text.strip()

    def _validate(self, line: str) -> bool:
        return not self._is_suspicious(line)


# ----------------------
# Thread → worker bar mapping (Option A)
# ----------------------
thread_to_wid = {}
thread_lock = threading.Lock()  # guard mapping


def worker_task(file_path: Path, repo_root: Path, top_level: str,
                fixer: MarkdownFixerHybrid, worker_bars):
    """Worker function: each thread bound once to a persistent bar."""
    tid = threading.get_ident()

    # Assign persistent wid for this thread
    with thread_lock:
        if tid not in thread_to_wid:
            wid = len(thread_to_wid) + 1
            thread_to_wid[tid] = wid
        else:
            wid = thread_to_wid[tid]

    bar = worker_bars[wid - 1]

    stats = Stats()
    stats.files_analyzed = 1
    corrected = False

    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return stats

    new_lines = lines[:]

    # relative path without top-level
    rel_path = file_path.relative_to(repo_root / top_level)

    # reset worker bar for this file
    bar.reset(total=len(lines))
    bar.set_description(f"Worker {wid}: {rel_path}")

    for i, line in enumerate(lines):
        if not fixer._is_suspicious(line):
            bar.update(1)
            continue

        attempts = 0
        while attempts < 3:
            attempts += 1
            stats.total_attempts += 1
            proposal = fixer._fix_with_claude(line)
            if fixer._validate(proposal):
                new_lines[i] = proposal
                stats.total_corrections += 1
                corrected = True
                break
        bar.update(1)

    if corrected:
        stats.files_corrected = 1
        file_path.write_text("\n".join(new_lines), encoding="utf-8")

    return stats


# ----------------------
# Stats merging & report
# ----------------------
def merge_stats(all_stats):
    merged = Stats()
    for s in all_stats:
        merged.files_analyzed += s.files_analyzed
        merged.files_corrected += s.files_corrected
        merged.total_corrections += s.total_corrections
        merged.total_attempts += s.total_attempts
    return merged


def generate_report(stats: Stats):
    avg_per_file = (
        stats.total_corrections / stats.files_corrected
        if stats.files_corrected
        else 0
    )
    avg_attempts = (
        stats.total_attempts / stats.total_corrections
        if stats.total_corrections
        else 0
    )
    report = f"""# Correction Summary ({datetime.now().isoformat()})

- Total files analyzed: {stats.files_analyzed}
- Files corrected: {stats.files_corrected}
- Total corrections made: {stats.total_corrections}
- Average corrections per corrected file: {avg_per_file:.2f}
- Average attempts per correction: {avg_attempts:.2f}
"""
    Path("correction_summary.md").write_text(report, encoding="utf-8")
    print("\n=== Summary written to correction_summary.md ===")
    print(report)


# ----------------------
# Main
# ----------------------
def main():
    import argparse
    from dotenv import load_dotenv

    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default="../..")
    parser.add_argument("--api-key", help="Anthropic API key")
    parser.add_argument("--workers", type=int, default=8,
                        help="Number of worker threads")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Anthropic API key required.")
        exit(1)

    choice = input("Select folder to check (courses/tutorials/resources): ").strip()
    if choice not in ["courses", "tutorials", "resources"]:
        print("Invalid choice. Exiting.")
        return

    repo_root = Path(args.repo_root)
    files = sorted((repo_root / choice).rglob("*.md")) + sorted(
        (repo_root / choice).rglob("*.yml")
    )
    if not files:
        print("No files found in", choice)
        return

    fixer = MarkdownFixerHybrid(api_key)
    all_stats = []

    # global bar
    global_bar = tqdm(total=len(files), desc="Global Progress",
                      position=0, leave=True, ncols=100)

    # persistent worker bars (fixed positions)
    worker_bars = [
        tqdm(total=1, desc=f"Worker {wid}", position=wid,
             leave=True, ncols=100)
        for wid in range(1, args.workers + 1)
    ]

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(worker_task,
                                   f, repo_root, choice,
                                   fixer, worker_bars): f
                   for f in files}

        for done in as_completed(futures):
            stats = done.result()
            all_stats.append(stats)
            global_bar.update(1)

    global_bar.close()
    for bar in worker_bars:
        bar.close()

    merged = merge_stats(all_stats)
    generate_report(merged)


if __name__ == "__main__":
    main()
