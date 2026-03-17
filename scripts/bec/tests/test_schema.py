"""Tests for bec.lib.schema — JSON schema loading and validation."""

from pathlib import Path

import pytest

from bec.lib.schema import (
    ValidationResult,
    _strip_nulls,
    load_json_schema,
    validate_markdown_frontmatter,
    validate_yaml_against_schema,
    validate_yml_content,
)


# ---------------------------------------------------------------------------
# ValidationResult
# ---------------------------------------------------------------------------


class TestValidationResult:
    def test_empty_is_valid(self):
        r = ValidationResult(path="test.yml")
        assert r.is_valid
        assert r.errors == []
        assert r.warnings == []

    def test_error_makes_invalid(self):
        r = ValidationResult(path="test.yml")
        r.add_error("bad")
        assert not r.is_valid

    def test_warning_keeps_valid(self):
        r = ValidationResult(path="test.yml")
        r.add_warning("watch out")
        assert r.is_valid

    def test_to_dict(self):
        r = ValidationResult(path="x.yml")
        r.add_error("e1")
        r.add_warning("w1")
        d = r.to_dict()
        assert d["path"] == "x.yml"
        assert d["valid"] is False
        assert d["errors"] == ["e1"]
        assert d["warnings"] == ["w1"]


# ---------------------------------------------------------------------------
# _strip_nulls
# ---------------------------------------------------------------------------


class TestStripNulls:
    def test_dict_nulls_removed(self):
        data = {"a": 1, "b": None, "c": "x"}
        cleaned, nulls = _strip_nulls(data)
        assert cleaned == {"a": 1, "c": "x"}
        assert "b" in nulls[0]

    def test_nested_nulls(self):
        data = {"a": {"b": None, "c": 1}}
        cleaned, nulls = _strip_nulls(data)
        assert cleaned == {"a": {"c": 1}}
        assert len(nulls) == 1

    def test_list_nulls(self):
        data = {"items": [1, None, 3]}
        cleaned, nulls = _strip_nulls(data)
        assert cleaned == {"items": [1, 3]}
        assert len(nulls) == 1

    def test_no_nulls(self):
        data = {"a": 1, "b": "two"}
        cleaned, nulls = _strip_nulls(data)
        assert cleaned == data
        assert nulls == []


# ---------------------------------------------------------------------------
# load_json_schema
# ---------------------------------------------------------------------------


def test_load_json_schema(repo_root):
    schema = load_json_schema(repo_root / "schemas" / "course-scheme.json")
    assert schema["type"] == "object"
    assert "properties" in schema
    assert "id" in schema["properties"]


# ---------------------------------------------------------------------------
# validate_yaml_against_schema
# ---------------------------------------------------------------------------


class TestValidateYamlAgainstSchema:
    def test_valid_data(self, repo_root):
        schema = load_json_schema(repo_root / "schemas" / "course-scheme.json")
        data = {
            "id": "2b7dc507-81e3-4b70-88e6-41ed44239966",
            "topic": "bitcoin",
            "subtopic": "bitcoin",
            "level": "beginner",
            "hours": 7,
            "professors_id": ["2e1b5182-567e-453a-af29-36009340ff02"],
            "original_language": "en",
            "proofreading": [
                {"language": "en", "urgency": 1, "reward": 0}
            ],
        }
        result = validate_yaml_against_schema(data, schema, "test.yml")
        assert result.is_valid, f"Unexpected errors: {result.errors}"

    def test_invalid_data_missing_required(self, repo_root):
        schema = load_json_schema(repo_root / "schemas" / "course-scheme.json")
        data = {"id": "not-a-uuid", "topic": "invalid"}
        result = validate_yaml_against_schema(data, schema, "test.yml")
        assert not result.is_valid
        assert len(result.errors) > 0

    def test_null_values_become_warnings(self, repo_root):
        schema = load_json_schema(repo_root / "schemas" / "course-scheme.json")
        data = {
            "id": "2b7dc507-81e3-4b70-88e6-41ed44239966",
            "topic": "bitcoin",
            "subtopic": "bitcoin",
            "level": "beginner",
            "hours": 7,
            "professors_id": ["2e1b5182-567e-453a-af29-36009340ff02"],
            "original_language": "en",
            "proofreading": [
                {"language": "en", "urgency": 1, "reward": 0}
            ],
            "project_id": None,
        }
        result = validate_yaml_against_schema(data, schema, "test.yml")
        assert len(result.warnings) > 0
        assert any("null" in w.lower() or "empty" in w.lower() for w in result.warnings)


# ---------------------------------------------------------------------------
# validate_markdown_frontmatter
# ---------------------------------------------------------------------------


class TestValidateMarkdownFrontmatter:
    def test_valid_tutorial_md(self, fixtures_dir, repo_root):
        md_path = fixtures_dir / "good-tutorial" / "en.md"
        schema = load_json_schema(repo_root / "schemas" / "tutorial-content-scheme.json")
        result = validate_markdown_frontmatter(md_path, schema)
        assert result.is_valid, f"Unexpected errors: {result.errors}"

    def test_missing_required_frontmatter(self, fixtures_dir, repo_root):
        md_path = fixtures_dir / "bad-course" / "en.md"
        schema = load_json_schema(repo_root / "schemas" / "course-content-scheme.json")
        result = validate_markdown_frontmatter(md_path, schema)
        assert not result.is_valid
        assert any("name" in e for e in result.errors)

    def test_valid_course_md(self, fixtures_dir, repo_root):
        md_path = fixtures_dir / "good-course" / "en.md"
        schema = load_json_schema(repo_root / "schemas" / "course-content-scheme.json")
        result = validate_markdown_frontmatter(md_path, schema)
        assert result.is_valid, f"Unexpected errors: {result.errors}"


# ---------------------------------------------------------------------------
# validate_yml_content
# ---------------------------------------------------------------------------


class TestValidateYmlContent:
    def test_valid_quiz_translation(self, fixtures_dir, repo_root):
        yml_path = fixtures_dir / "good-course" / "quizz" / "001" / "en.yml"
        schema = load_json_schema(repo_root / "schemas" / "quizz-translation-scheme.json")
        result = validate_yml_content(yml_path, schema)
        assert result.is_valid, f"Unexpected errors: {result.errors}"
