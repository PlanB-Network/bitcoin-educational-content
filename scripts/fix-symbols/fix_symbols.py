#!/usr/bin/env python3
"""
Hybrid Markdown Format Fixer (Balanced Detection)
-------------------------------------------------
- User selects ONE folder (courses/tutorials/resources)
- Files processed recursively, alphabetically (.md & .yml)
- Suspicion detection: balance count + regex + parser confirmation
- Uses Claude Sonnet API for fixes only when needed
- Live terminal reporting
- Final correction_summary.md with stats
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime

from markdown_it import MarkdownIt

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
    def __init__(self, repo_root: str, anthropic_api_key: str):
        self.repo_root = Path(repo_root)
        self.client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.model = "claude-sonnet-4-20250514"
        self.md = MarkdownIt()

    # -------------------
    # Suspicion detection (hybrid)
    # -------------------
    def _is_suspicious(self, line: str) -> bool:
        """Check for broken emphasis markers with hybrid strategy."""
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
            return False  # balanced and no overlaps → fine

        # 3. Parser confirmation
        try:
            tokens = self.md.parse(line)
        except Exception:
            return True  # parser blew up

        for t in tokens:
            if t.type == "text" and "*" in t.content:
                return True  # leftover raw '*' → suspicious

        return False

    # -------------------
    # Claude correction
    # -------------------
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

    # -------------------
    # Validate (re-run suspicion check)
    # -------------------
    def _validate(self, line: str) -> bool:
        return not self._is_suspicious(line)

    # -------------------
    # Process files
    # -------------------
    def process_folder(self, folder: str, stats: Stats):
        target_dir = self.repo_root / folder
        if not target_dir.exists():
            print(f"Error: folder {folder} not found.")
            return

        files = sorted(target_dir.rglob("*.md")) + sorted(target_dir.rglob("*.yml"))

        for file_path in files:
            stats.files_analyzed += 1
            rel_path = file_path.relative_to(self.repo_root)
            print(f"\nchecking {rel_path}")

            corrected = False
            try:
                lines = file_path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                print("  Skipping (encoding error)")
                continue

            new_lines = lines[:]
            for i, line in enumerate(lines):
                if not self._is_suspicious(line):
                    continue

                print(f"  line {i+1}: flagged suspicious")
                attempts = 0
                while attempts < 3:
                    attempts += 1
                    stats.total_attempts += 1
                    print(f"    attempt {attempts}: calling Claude...")

                    proposal = self._fix_with_claude(line)
                    if self._validate(proposal):
                        new_lines[i] = proposal
                        stats.total_corrections += 1
                        corrected = True
                        print(f"    attempt {attempts}: accepted ✅")
                        break
                    else:
                        print(f"    attempt {attempts}: failed ❌")

            if corrected:
                stats.files_corrected += 1
                file_path.write_text("\n".join(new_lines), encoding="utf-8")
                print(f"→ corrections applied to {file_path.name}")

    # -------------------
    # Final report
    # -------------------
    def generate_report(self, stats: Stats):
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


# -------------------
# Main
# -------------------
def main():
    import argparse
    from dotenv import load_dotenv

    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default="../..")
    parser.add_argument("--api-key", help="Anthropic API key")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Anthropic API key required.")
        exit(1)

    choice = input("Select folder to check (courses/tutorials/resources): ").strip()
    if choice not in ["courses", "tutorials", "resources"]:
        print("Invalid choice. Exiting.")
        return

    fixer = MarkdownFixerHybrid(args.repo_root, api_key)
    stats = Stats()
    fixer.process_folder(choice, stats)
    fixer.generate_report(stats)


if __name__ == "__main__":
    main()

