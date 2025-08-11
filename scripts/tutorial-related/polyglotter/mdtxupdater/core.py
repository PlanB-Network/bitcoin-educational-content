import re
import json
import difflib
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class MarkdownTranslationUpdater:
    """
    Core engine to update localized Markdown files with JSON translations.
    - Flexible anchors: START/END, image filenames (*.webp), chapter UUID tags, fenced code blocks.
    - Robust paragraph handling: counts non-empty lines as paragraphs.
    - Whitespace-preserving section replacement.
    - Code-block similarity matching across languages (for slightly differing code blocks).
    """

    # Supported language codes (file names must match these codes)
    SUPPORTED_LANGS: List[str] = [
        "cs", "de", "en", "es", "et", "fa", "fi", "hi", "id", "it",
        "ja", "nb-NO", "nl", "pl", "pt", "ru", "si", "sr-Latn", "sv", "sw",
        "vi", "zh-Hans", "zh-Hant"
    ]

    # Languages allowed as "reference" for preview
    REF_LANG_CHOICES: List[str] = ["en", "fr", "es", "de", "it"]

    def __init__(self) -> None:
        pass

    # --------------------------- File discovery ----------------------------

    def find_markdown_files(self, directory: str) -> Dict[str, str]:
        """
        Find Markdown files per supported language in the given directory.
        Returns a dict: { lang_code: absolute_path }
        """
        files: Dict[str, str] = {}
        dir_path = Path(directory)

        if not dir_path.exists():
            raise ValueError(f"Folder does not exist: {directory}")

        for lang in self.SUPPORTED_LANGS:
            for candidate in (
                dir_path / f"{lang}.md",
                dir_path / f"{lang.lower()}.md",
                dir_path / f"{lang.upper()}.md",
            ):
                if candidate.exists():
                    files[lang] = str(candidate)
                    break

        # Special Chinese casing fallbacks (robustness)
        if "zh-hans" not in files and (dir_path / "zh-Hans.md").exists():
            files["zh-hans"] = str(dir_path / "zh-Hans.md")
        if "zh-Hant" not in files and (dir_path / "zh-Hant.md").exists():
            files["zh-Hant"] = str(dir_path / "zh-Hant.md")

        return files

    # ------------------------------ Anchors --------------------------------

    def _detect_bound_type(self, raw: str) -> Tuple[str, dict]:
        """
        Detect anchor (bound) type among:
          - START / END
          - IMAGE (expects full filename like '001.webp')
          - CHAPTER (UUID within <chapterId>...</chapterId> or bare UUID)
          - CODE (fenced code block or any multiline snippet)
        Returns (type, meta_dict).
        """
        s = raw.strip()

        if s.upper() == "START":
            return ("START", {})
        if s.upper() == "END":
            return ("END", {})

        # Image filename
        if re.fullmatch(r".+\.webp", s, flags=re.IGNORECASE):
            return ("IMAGE", {"filename": s})

        # Chapter UUID
        uuid_match = re.search(
            r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            s,
        )
        if uuid_match:
            return ("CHAPTER", {"uuid": uuid_match.group(0)})

        # Code block
        if "```" in s or "\n" in s:
            payload = self._extract_code_payload(s)
            return ("CODE", {"code": payload})

        # As a safe fallback, treat long tokens as a code snippet anchor
        if len(s) > 40:
            return ("CODE", {"code": s})

        raise ValueError(
            "Unrecognized bound. Use START/END, a .webp filename, a <chapterId>UUID</chapterId>, "
            "or paste a code block/snippet."
        )

    @staticmethod
    def _extract_code_payload(block: str) -> str:
        """Return inner code content from fenced block or raw string if not fenced."""
        m = re.search(r"```[^\n]*\n(.*?)\n```", block, flags=re.DOTALL)
        if m:
            return m.group(1).strip()
        return block.strip()

    def _regex_for_image_filename(self, filename: str) -> List[re.Pattern]:
        """Build patterns to find an image reference by exact filename in Markdown/HTML forms."""
        escaped = re.escape(filename)
        return [
            re.compile(rf'!\[[^\]]*]\([^)"]*{escaped}\)', re.IGNORECASE),
            re.compile(rf'<img[^>]+src="[^"]*{escaped}"[^>]*>', re.IGNORECASE),
            re.compile(rf"<img[^>]+src='[^']*{escaped}'[^>]*>", re.IGNORECASE),
        ]

    def _find_image_marker(
        self, content: str, filename: str, start_from: int = 0
    ) -> Optional[Tuple[int, int]]:
        """Find first image marker containing the filename; returns (start,end) indices or None."""
        hay = content[start_from:]
        for patt in self._regex_for_image_filename(filename):
            m = patt.search(hay)
            if m:
                return (start_from + m.start(), start_from + m.end())
        return None

    def _find_chapter_marker(
        self, content: str, uuid: str, start_from: int = 0
    ) -> Optional[Tuple[int, int]]:
        """Find <chapterId>UUID</chapterId>; allow optional whitespace around UUID."""
        patt = re.compile(rf"<chapterId>\s*{re.escape(uuid)}\s*</chapterId>", re.IGNORECASE)
        hay = content[start_from:]
        m = patt.search(hay)
        if m:
            return (start_from + m.start(), start_from + m.end())
        return None

    def _iter_fenced_code_blocks(
        self, content: str, start_from: int = 0
    ) -> List[Tuple[int, int, str]]:
        """Return list of fenced code blocks as (start_idx, end_idx, payload) from content[start_from:]."""
        blocks: List[Tuple[int, int, str]] = []
        for m in re.finditer(r"```[^\n]*\n(.*?)\n```", content[start_from:], flags=re.DOTALL):
            s = start_from + m.start()
            e = start_from + m.end()
            payload = m.group(1).strip()
            blocks.append((s, e, payload))
        return blocks

    def _find_best_code_block(
        self, content: str, code_query: str, start_from: int = 0
    ) -> Optional[Tuple[int, int]]:
        """
        Among all fenced code blocks after start_from, pick the most similar to code_query.
        Similarity uses difflib.SequenceMatcher ratio on stripped payloads.
        """
        code_query = code_query.strip()
        candidates = self._iter_fenced_code_blocks(content, start_from=start_from)
        if not candidates:
            return None
        best = None
        best_ratio = -1.0
        for (s, e, payload) in candidates:
            ratio = difflib.SequenceMatcher(None, code_query, payload).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best = (s, e)
        return best

    def resolve_bound(self, content: str, bound_raw: str, is_lower: bool, start_from: int = 0) -> int:
        """
        Resolve a bound to an absolute index in content:
          - START -> 0
          - END -> len(content)
          - IMAGE -> end of image for lower bound, start of image for upper bound
          - CHAPTER -> end for lower, start for upper
          - CODE -> best matching fenced code block; end for lower, start for upper
        """
        btype, meta = self._detect_bound_type(bound_raw)

        if btype == "START":
            return 0
        if btype == "END":
            return len(content)

        if btype == "IMAGE":
            hit = self._find_image_marker(content, meta["filename"], start_from=start_from)
            if not hit:
                raise ValueError(f"Image not found: {meta['filename']}")
            return hit[1] if is_lower else hit[0]

        if btype == "CHAPTER":
            hit = self._find_chapter_marker(content, meta["uuid"], start_from=start_from)
            if not hit:
                raise ValueError(f"Chapter anchor not found: {meta['uuid']}")
            return hit[1] if is_lower else hit[0]

        if btype == "CODE":
            hit = self._find_best_code_block(content, meta["code"], start_from=start_from)
            if not hit:
                raise ValueError("No similar code block found for the provided anchor.")
            return hit[1] if is_lower else hit[0]

        raise ValueError("Unknown bound type.")

    # ------------------------- Paragraph handling --------------------------

    @staticmethod
    def _nonempty_line_indices(text: str) -> List[int]:
        """Return indices of non-empty lines within text.splitlines()."""
        lines = text.splitlines()
        return [i for i, ln in enumerate(lines) if ln.strip() != ""]

    def _replace_line_paragraph(self, section: str, paragraph_num: int, new_text: str) -> str:
        """
        Replace the Nth non-empty line (1-based) within section by new_text.
        new_text can be multiline; it will replace a single line position.
        """
        lines = section.splitlines()
        indices = self._nonempty_line_indices(section)
        if not indices:
            raise ValueError("No non-empty paragraph in the selected section.")
        if paragraph_num < 1 or paragraph_num > len(indices):
            raise ValueError(
                f"Paragraph {paragraph_num} does not exist (there are {len(indices)} non-empty paragraphs)."
            )
        target_idx = indices[paragraph_num - 1]
        new_lines = new_text.splitlines()
        lines = lines[:target_idx] + new_lines + lines[target_idx + 1:]
        return "\n".join(lines)

    def _insert_line_paragraph(self, section: str, paragraph_num: int, new_text: str) -> str:
        """
        Insert new_text (possibly multiline) BEFORE the Nth non-empty line.
        If paragraph_num exceeds the count, append at the end.
        """
        lines = section.splitlines()
        indices = self._nonempty_line_indices(section)

        if not indices:
            insert_at = len(lines)
        else:
            if paragraph_num <= 0:
                paragraph_num = 1
            if paragraph_num > len(indices):
                insert_at = len(lines)
            else:
                insert_at = indices[paragraph_num - 1]

        new_lines = new_text.splitlines()
        return "\n".join(lines[:insert_at] + new_lines + lines[insert_at:])

    # ------------------------------ Update ---------------------------------

    def update_file(
        self,
        file_path: str,
        lower_bound_raw: str,
        upper_bound_raw: str,
        paragraph_num: int,
        new_text: str,
        insert_mode: bool = False,
    ) -> bool:
        """
        Write new text into the targeted markdown file.
        Preserves leading/trailing whitespace around the selected section.
        """
        try:
            content = Path(file_path).read_text(encoding="utf-8")

            start_pos = self.resolve_bound(content, lower_bound_raw, is_lower=True, start_from=0)
            end_pos = self.resolve_bound(content, upper_bound_raw, is_lower=False, start_from=start_pos)
            if end_pos < start_pos:
                raise ValueError("Upper bound is before lower bound.")

            section = content[start_pos:end_pos]

            # Preserve whitespace around the section to avoid breaking layout
            leading_match = re.match(r"^\s*", section, flags=re.DOTALL)
            trailing_match = re.search(r"\s*$", section, flags=re.DOTALL)
            leading_ws = leading_match.group(0) if leading_match else ""
            trailing_ws = trailing_match.group(0) if trailing_match else ""
            core = section[len(leading_ws): len(section) - len(trailing_ws)]

            if insert_mode:
                new_core = self._insert_line_paragraph(core, paragraph_num, new_text)
            else:
                new_core = self._replace_line_paragraph(core, paragraph_num, new_text)

            new_section = f"{leading_ws}{new_core}{trailing_ws}"
            new_content = content[:start_pos] + new_section + content[end_pos:]
            Path(file_path).write_text(new_content, encoding="utf-8")
            return True
        except Exception as e:
            print(f"[ERROR] {file_path}: {e}")
            return False

    # ----------------------------- Preview ---------------------------------

    def preview_context(
        self,
        ref_file: str,
        lower_bound_raw: str,
        upper_bound_raw: str,
        paragraph_num: int,
        insert_mode: bool,
    ) -> Tuple[str, str]:
        """
        Return human-readable preview strings:
          - For REPLACE: (target_line_start, target_line_end)
          - For APPEND:  (above_line, below_line) around the insertion spot
        Always uses the reference file for consistency.
        """
        content = Path(ref_file).read_text(encoding="utf-8")

        start_pos = self.resolve_bound(content, lower_bound_raw, is_lower=True, start_from=0)
        end_pos = self.resolve_bound(content, upper_bound_raw, is_lower=False, start_from=start_pos)
        if end_pos < start_pos:
            raise ValueError("Upper bound is before lower bound in the reference file.")

        section = content[start_pos:end_pos]
        lines = section.splitlines()
        nonempty_idx = self._nonempty_line_indices(section)
        if not nonempty_idx:
            raise ValueError("No non-empty paragraph detected between bounds in the reference file.")

        if insert_mode:
            if paragraph_num <= 0:
                paragraph_num = 1
            if paragraph_num > len(nonempty_idx):
                above = lines[nonempty_idx[-1]] if nonempty_idx else ""
                below = "(end of section)"
            else:
                insert_at = nonempty_idx[paragraph_num - 1]
                above = lines[nonempty_idx[paragraph_num - 2]] if paragraph_num - 2 >= 0 else "(start of section)"
                below = lines[insert_at]
            return (above, below)
        else:
            if paragraph_num < 1 or paragraph_num > len(nonempty_idx):
                raise ValueError(
                    f"Paragraph {paragraph_num} does not exist in the reference file "
                    f"(there are {len(nonempty_idx)} non-empty paragraphs)."
                )
            target_line = lines[nonempty_idx[paragraph_num - 1]]
            start_snip = target_line[:200]
            end_snip = target_line[-200:] if len(target_line) > 200 else target_line
            return (start_snip, end_snip)

    # ------------------------ Utility: pick reference ----------------------

    def pick_reference_file(self, files: Dict[str, str], ref_lang: str) -> str:
        """
        Pick a reference file based on requested ref_lang; fallback to en, fr, or any available.
        """
        if ref_lang in files:
            return files[ref_lang]
        for fallback in ["en", "fr"]:
            if fallback in files:
                return files[fallback]
        # deterministic fallback
        return next(iter(files.values()))
