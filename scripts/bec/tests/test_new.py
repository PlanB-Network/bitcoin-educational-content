"""Tests for bec new course command."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.new import (
    COURSE_ID_RE,
    build_course_md,
    build_course_yml,
    level_from_number,
    validate_course_id,
)


# ---- Unit tests for helpers ----


class TestCourseIdRegex:
    def test_valid_ids(self):
        assert COURSE_ID_RE.match("btc101")
        assert COURSE_ID_RE.match("dev301")
        assert COURSE_ID_RE.match("min200")

    def test_invalid_ids(self):
        assert not COURSE_ID_RE.match("BTC101")  # uppercase
        assert not COURSE_ID_RE.match("bt101")  # 2 chars
        assert not COURSE_ID_RE.match("btc10")  # 2 digits
        assert not COURSE_ID_RE.match("btc1011")  # 4 digits
        assert not COURSE_ID_RE.match("101btc")  # reversed
        assert not COURSE_ID_RE.match("")


class TestValidateCourseId:
    @pytest.fixture
    def registry(self, repo_root):
        from bec.lib.content_types import load_registry

        return load_registry(repo_root)

    def test_valid_id(self, registry):
        assert validate_course_id("btc101", registry) is None
        assert validate_course_id("dev301", registry) is None

    def test_bad_format(self, registry):
        err = validate_course_id("BTC101", registry)
        assert err is not None
        assert "3-letter discipline code" in err

    def test_unknown_discipline(self, registry):
        err = validate_course_id("xyz101", registry)
        assert err is not None
        assert "Unknown discipline" in err

    def test_number_out_of_range(self, registry):
        err = validate_course_id("btc001", registry)
        assert err is not None
        assert "out of range" in err

    def test_number_too_high(self, registry):
        err = validate_course_id("btc999", registry)
        assert err is not None
        assert "out of range" in err


class TestLevelFromNumber:
    @pytest.fixture
    def registry(self, repo_root):
        from bec.lib.content_types import load_registry

        return load_registry(repo_root)

    def test_beginner(self, registry):
        assert level_from_number(101, registry) == "beginner"
        assert level_from_number(199, registry) == "beginner"

    def test_intermediate(self, registry):
        assert level_from_number(200, registry) == "intermediate"
        assert level_from_number(299, registry) == "intermediate"

    def test_advanced(self, registry):
        assert level_from_number(300, registry) == "advanced"

    def test_expert(self, registry):
        assert level_from_number(400, registry) == "expert"


class TestBuildCourseYml:
    def test_required_fields(self):
        data = build_course_yml(
            course_uuid="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            topic="bitcoin",
            subtopic="bitcoin",
            level="beginner",
            lang="en",
            professor_id="11111111-2222-3333-4444-555555555555",
        )
        assert data["id"] == "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        assert data["topic"] == "bitcoin"
        assert data["subtopic"] == "bitcoin"
        assert data["level"] == "beginner"
        assert data["original_language"] == "en"
        assert len(data["professors_id"]) == 1
        assert data["professors_id"][0] == "11111111-2222-3333-4444-555555555555"
        assert data["hours"] == 1
        assert data["teaching_format"] == "self_paced"
        assert len(data["proofreading"]) == 1
        assert data["proofreading"][0]["language"] == "en"

    def test_uuid_format(self):
        data = build_course_yml(
            course_uuid="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            topic="bitcoin",
            subtopic="bitcoin",
            level="beginner",
            lang="en",
            professor_id="11111111-2222-3333-4444-555555555555",
        )
        uuid_re = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        assert uuid_re.match(data["id"])


class TestBuildCourseMd:
    def test_has_frontmatter(self):
        md = build_course_md("btc101", "en")
        assert md.startswith("---\n")
        assert "\n---\n" in md

    def test_has_separator(self):
        md = build_course_md("btc101", "en")
        assert "\n+++\n" in md

    def test_has_part_and_chapter(self):
        md = build_course_md("btc101", "en")
        assert "# Part 1" in md
        assert "## Chapter 1" in md
        assert "<partId>" in md
        assert "<chapterId>" in md

    def test_has_frontmatter_fields(self):
        md = build_course_md("btc101", "en")
        assert "name:" in md
        assert "goal:" in md
        assert "objectives:" in md

    def test_references_course_id(self):
        md = build_course_md("btc101", "en")
        assert "BTC101" in md


# ---- CLI integration tests ----


class TestNewCourseCommand:
    """Integration tests using CliRunner against the real repo."""

    PROF_UUID = "2e1b5182-567e-453a-af29-36009340ff02"  # existing professor

    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def clean_course(self, repo_root):
        """Fixture that cleans up any test course after the test."""
        course_dir = repo_root / "courses" / "btc199"
        yield course_dir
        # Cleanup
        if course_dir.exists():
            import shutil

            shutil.rmtree(course_dir)

    def test_non_interactive_creates_files(self, runner, repo_root, clean_course):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 0, result.output
        assert clean_course.exists()
        assert (clean_course / "course.yml").exists()
        assert (clean_course / "en.md").exists()
        assert (clean_course / "assets").is_dir()
        assert (clean_course / "assets" / ".gitkeep").exists()

    def test_course_yml_valid_structure(self, runner, repo_root, clean_course):
        runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        with open(clean_course / "course.yml") as f:
            data = yaml.safe_load(f)
        # Check required schema fields
        assert "id" in data
        assert "topic" in data
        assert "subtopic" in data
        assert "level" in data
        assert "hours" in data
        assert "professors_id" in data
        assert "original_language" in data
        assert "proofreading" in data
        assert data["topic"] == "bitcoin"
        assert data["level"] == "beginner"
        # UUID format
        uuid_re = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        assert uuid_re.match(data["id"])

    def test_course_md_structure(self, runner, repo_root, clean_course):
        runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        md = (clean_course / "en.md").read_text()
        assert md.startswith("---\n")
        assert "\n+++\n" in md
        assert "<partId>" in md
        assert "<chapterId>" in md
        assert "name:" in md
        assert "goal:" in md
        assert "objectives:" in md

    def test_json_output(self, runner, repo_root, clean_course):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
                "--json",
            ],
        )
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["course_id"] == "btc199"
        assert "uuid" in data
        assert "files" in data
        assert len(data["files"]) == 3

    def test_invalid_course_id_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "INVALID",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "Invalid course ID" in result.output

    def test_invalid_topic_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "nosuch",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "invalid topic" in result.output

    def test_invalid_level_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "grandmaster",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "invalid level" in result.output

    def test_invalid_language_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "zz",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "invalid language" in result.output

    def test_invalid_professor_uuid_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", "not-a-uuid",
            ],
        )
        assert result.exit_code == 1
        assert "invalid professor ID" in result.output

    def test_duplicate_course_rejected(self, runner, repo_root, clean_course):
        # Create the first time
        runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        # Try again
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc199",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "already exists" in result.output

    def test_unknown_discipline_code_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "xyz101",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "Unknown discipline" in result.output

    def test_number_out_of_range_rejected(self, runner):
        result = runner.invoke(
            cli,
            [
                "new", "course",
                "--id", "btc001",
                "--topic", "bitcoin",
                "--subtopic", "bitcoin",
                "--level", "beginner",
                "--lang", "en",
                "--professor-id", self.PROF_UUID,
            ],
        )
        assert result.exit_code == 1
        assert "out of range" in result.output
