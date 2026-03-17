"""Tests for bec add part / add chapter commands."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.lib.markdown import (
    append_to_markdown,
    build_chapter_block,
    build_part_block,
    generate_chapter_id,
)


# ---- Unit tests for lib/markdown.py ----


class TestGenerateChapterId:
    def test_format_three_words(self):
        cid = generate_chapter_id()
        parts = cid.split("-")
        assert len(parts) == 3, f"Expected 3 words, got {len(parts)}: {cid}"

    def test_all_lowercase(self):
        cid = generate_chapter_id()
        assert cid == cid.lower()

    def test_words_are_from_bip39(self):
        from bec.lib.markdown import _load_wordlist

        wordlist = _load_wordlist()
        cid = generate_chapter_id()
        for word in cid.split("-"):
            assert word in wordlist, f"'{word}' not in BIP39 wordlist"

    def test_unique_words(self):
        """Each chapter ID should have 3 distinct words (random.sample)."""
        for _ in range(20):
            cid = generate_chapter_id()
            parts = cid.split("-")
            assert len(set(parts)) == 3, f"Duplicate words in: {cid}"

    def test_randomness(self):
        """Two generated IDs should (almost certainly) differ."""
        ids = {generate_chapter_id() for _ in range(10)}
        assert len(ids) > 1, "Generated IDs are all identical"


class TestBuildPartBlock:
    def test_has_separator(self):
        block = build_part_block("My Part", "test-uuid")
        assert block.startswith("+++\n")

    def test_has_h1(self):
        block = build_part_block("My Part", "test-uuid")
        assert "# My Part" in block

    def test_has_part_id(self):
        block = build_part_block("My Part", "abc-123")
        assert "<partId>abc-123</partId>" in block

    def test_structure(self):
        block = build_part_block("Title", "id-1")
        lines = block.split("\n")
        assert lines[0] == "+++"
        assert lines[1] == ""
        assert lines[2] == "# Title"
        assert lines[3] == ""
        assert lines[4] == "<partId>id-1</partId>"


class TestBuildChapterBlock:
    def test_has_h2(self):
        block = build_chapter_block("My Chapter", "test-id")
        assert "## My Chapter" in block

    def test_has_chapter_id(self):
        block = build_chapter_block("My Chapter", "test-id")
        assert "<chapterId>test-id</chapterId>" in block

    def test_auto_generates_bip39_id(self):
        block = build_chapter_block("My Chapter")
        match = re.search(r"<chapterId>(.+?)</chapterId>", block)
        assert match
        cid = match.group(1)
        parts = cid.split("-")
        assert len(parts) == 3, f"Expected BIP39 3-word ID, got: {cid}"

    def test_structure(self):
        block = build_chapter_block("Title", "cid")
        lines = block.split("\n")
        assert lines[0] == "## Title"
        assert lines[1] == ""
        assert lines[2] == "<chapterId>cid</chapterId>"


class TestAppendToMarkdown:
    def test_appends_with_separation(self, tmp_path):
        md = tmp_path / "test.md"
        md.write_text("# Heading\n\nContent here.\n", encoding="utf-8")
        append_to_markdown(md, "## New Section\n")
        result = md.read_text(encoding="utf-8")
        assert result.endswith("## New Section\n")
        # Should have blank line separation
        assert "\n\n## New Section\n" in result

    def test_appends_to_file_without_trailing_newline(self, tmp_path):
        md = tmp_path / "test.md"
        md.write_text("# Heading\n\nContent", encoding="utf-8")
        append_to_markdown(md, "## New\n")
        result = md.read_text(encoding="utf-8")
        assert "\n\n## New\n" in result

    def test_appends_to_file_with_double_newline(self, tmp_path):
        md = tmp_path / "test.md"
        md.write_text("# Heading\n\n", encoding="utf-8")
        append_to_markdown(md, "## New\n")
        result = md.read_text(encoding="utf-8")
        assert "# Heading\n\n## New\n" in result


class TestBip39Wordlist:
    def test_wordlist_loads(self):
        from bec.lib.markdown import _load_wordlist

        words = _load_wordlist()
        assert len(words) == 2048

    def test_wordlist_no_empty(self):
        from bec.lib.markdown import _load_wordlist

        words = _load_wordlist()
        assert all(w for w in words)

    def test_known_words_present(self):
        from bec.lib.markdown import _load_wordlist

        words = _load_wordlist()
        assert "abandon" in words
        assert "zoo" in words
        assert "bitcoin" not in words  # not in BIP39


# ---- CLI integration tests ----


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def test_course(repo_root):
    """Create a temporary course for testing, clean up after."""
    course_dir = repo_root / "courses" / "_test_add_course"
    course_dir.mkdir(parents=True, exist_ok=True)

    # Minimal course.yml
    (course_dir / "course.yml").write_text(
        "id: 00000000-0000-0000-0000-000000000000\ntopic: bitcoin\n",
        encoding="utf-8",
    )

    # Minimal en.md
    (course_dir / "en.md").write_text(
        "---\nname: Test Course\ngoal: Testing\nobjectives:\n  - Test\n---\n\n"
        "# Description\n\nTest course.\n\n"
        "+++\n\n"
        "# Part 1\n\n"
        "<partId>00000000-0000-0000-0000-000000000001</partId>\n\n"
        "## Chapter 1\n\n"
        "<chapterId>00000000-0000-0000-0000-000000000002</chapterId>\n\n"
        "Content here.\n",
        encoding="utf-8",
    )

    yield course_dir

    # Cleanup
    import shutil

    if course_dir.exists():
        shutil.rmtree(course_dir)


class TestAddPartCommand:
    def test_non_interactive(self, runner, test_course, repo_root):
        result = runner.invoke(cli, [
            "add", "part",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "New Part",
        ])
        assert result.exit_code == 0, result.output
        assert "Added part 'New Part'" in result.output

        content = (test_course / "en.md").read_text(encoding="utf-8")
        assert "+++\n\n# New Part\n\n<partId>" in content

    def test_json_output(self, runner, test_course):
        result = runner.invoke(cli, [
            "add", "part",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "JSON Part",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["action"] == "add_part"
        assert data["course"] == "_test_add_course"
        assert data["title"] == "JSON Part"
        assert "part_id" in data
        # part_id should be a UUID
        uuid_re = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        assert uuid_re.match(data["part_id"])

    def test_part_separator_format(self, runner, test_course):
        runner.invoke(cli, [
            "add", "part",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "Separator Test",
        ])
        content = (test_course / "en.md").read_text(encoding="utf-8")
        # Part block should be: +++\n\n# Title\n\n<partId>uuid</partId>
        assert "+++\n\n# Separator Test\n\n<partId>" in content

    def test_missing_course_fails(self, runner):
        result = runner.invoke(cli, [
            "add", "part",
            "--course", "nonexistent999",
            "--lang", "en",
            "--title", "Nope",
        ])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_missing_lang_file_fails(self, runner, test_course):
        result = runner.invoke(cli, [
            "add", "part",
            "--course", "_test_add_course",
            "--lang", "zz",
            "--title", "Nope",
        ])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_interactive_prompts(self, runner, test_course):
        result = runner.invoke(
            cli,
            ["add", "part"],
            input="_test_add_course\nen\nInteractive Part\n",
        )
        assert result.exit_code == 0, result.output
        assert "Added part 'Interactive Part'" in result.output


class TestAddChapterCommand:
    def test_non_interactive(self, runner, test_course, repo_root):
        result = runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "New Chapter",
        ])
        assert result.exit_code == 0, result.output
        assert "Added chapter 'New Chapter'" in result.output

        content = (test_course / "en.md").read_text(encoding="utf-8")
        assert "## New Chapter\n\n<chapterId>" in content

    def test_bip39_chapter_id(self, runner, test_course):
        result = runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "BIP39 Test",
        ])
        assert result.exit_code == 0
        assert "chapterId:" in result.output

        content = (test_course / "en.md").read_text(encoding="utf-8")
        match = re.search(r"<chapterId>([a-z]+-[a-z]+-[a-z]+)</chapterId>", content)
        assert match, "Expected BIP39 3-word chapter ID"
        words = match.group(1).split("-")
        assert len(words) == 3

    def test_json_output(self, runner, test_course):
        result = runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "JSON Chapter",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["action"] == "add_chapter"
        assert data["course"] == "_test_add_course"
        assert data["title"] == "JSON Chapter"
        assert "chapter_id" in data
        # chapter_id should be 3 BIP39 words
        words = data["chapter_id"].split("-")
        assert len(words) == 3

    def test_chapter_heading_is_h2(self, runner, test_course):
        runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "H2 Test",
        ])
        content = (test_course / "en.md").read_text(encoding="utf-8")
        # Should be ## not # or ###
        assert "## H2 Test" in content
        assert "### H2 Test" not in content

    def test_missing_course_fails(self, runner):
        result = runner.invoke(cli, [
            "add", "chapter",
            "--course", "nonexistent999",
            "--lang", "en",
            "--title", "Nope",
        ])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_interactive_prompts(self, runner, test_course):
        result = runner.invoke(
            cli,
            ["add", "chapter"],
            input="_test_add_course\nen\nInteractive Chapter\n",
        )
        assert result.exit_code == 0, result.output
        assert "Added chapter 'Interactive Chapter'" in result.output

    def test_multiple_additions(self, runner, test_course):
        """Adding multiple parts and chapters preserves structure."""
        runner.invoke(cli, [
            "add", "part",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "Part A",
        ])
        runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "Chapter A1",
        ])
        runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "Chapter A2",
        ])

        content = (test_course / "en.md").read_text(encoding="utf-8")
        # All should be present in order
        assert content.index("# Part A") < content.index("## Chapter A1")
        assert content.index("## Chapter A1") < content.index("## Chapter A2")

    def test_modified_md_still_valid_structure(self, runner, test_course):
        """After additions, the file still has valid course markdown structure."""
        runner.invoke(cli, [
            "add", "part",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "Validation Part",
        ])
        runner.invoke(cli, [
            "add", "chapter",
            "--course", "_test_add_course",
            "--lang", "en",
            "--title", "Validation Chapter",
        ])

        content = (test_course / "en.md").read_text(encoding="utf-8")
        # Must have frontmatter
        assert content.startswith("---\n")
        # Must have at least one +++ separator
        assert "\n+++\n" in content
        # Must have partId and chapterId tags
        assert "<partId>" in content
        assert "<chapterId>" in content
