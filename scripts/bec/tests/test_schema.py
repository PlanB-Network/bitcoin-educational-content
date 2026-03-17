"""Tests for bec.lib.schema — JSON schema loading and validation."""

import json
from pathlib import Path

import pytest

from bec.lib.schema import (
    ValidationResult,
    _build_registry,
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


# ---------------------------------------------------------------------------
# Tags definitions & $ref resolution (Phase 15)
# ---------------------------------------------------------------------------

VALID_TAGS = [
    "proof-of-work", "software", "mining", "fees", "hardware",
    "hardware-wallet-ready", "wallets", "investment", "keys", "market-trends",
    "finance", "onchain", "offchain", "lightning", "decentralization",
    "smart-contracts", "DIY", "node", "backup", "guides", "use-case",
    "user-friendly", "historical", "scalability", "protocols", "layers",
    "sidechains", "personal-security", "network-security", "privacy",
    "regulation", "risks", "future-outlook", "adoption", "case-studies",
    "good-practice", "innovation", "cypherpunk", "self-sovereignty", "DIY-IT",
    "consensus", "development", "interoperability", "technical-analysis",
    "update", "legacy", "deep-dive", "high-level", "easy-explain",
    "experimental", "business", "evaluation",
]

SCHEMAS_WITH_TAGS = [
    "bet-scheme.json", "book-scheme.json", "channel-scheme.json",
    "conference-scheme.json", "course-scheme.json", "event-scheme.json",
    "movie-scheme.json", "newsletter-scheme.json", "podcast-scheme.json",
    "professor-scheme.json", "project-scheme.json", "quizz-question-scheme.json",
    "tutorial-scheme.json", "word-scheme.json",
]


class TestTagsDefinitions:
    """Tests for tags-definitions.json and $ref resolution."""

    def test_tags_definitions_exists(self, repo_root):
        path = repo_root / "schemas" / "tags-definitions.json"
        assert path.exists(), "tags-definitions.json must exist in schemas/"

    def test_tags_definitions_valid_json_schema(self, repo_root):
        path = repo_root / "schemas" / "tags-definitions.json"
        data = json.loads(path.read_text())
        assert data["$schema"] == "http://json-schema.org/draft-07/schema#"
        assert "definitions" in data
        assert "tag_item" in data["definitions"]
        assert "tags_array" in data["definitions"]

    def test_tag_item_has_enum_with_52_tags(self, repo_root):
        path = repo_root / "schemas" / "tags-definitions.json"
        data = json.loads(path.read_text())
        enum = data["definitions"]["tag_item"]["enum"]
        assert len(enum) == 52, f"Expected 52 tags, got {len(enum)}"
        assert set(enum) == set(VALID_TAGS)

    def test_all_52_descriptions_present(self, repo_root):
        path = repo_root / "schemas" / "tags-definitions.json"
        data = json.loads(path.read_text())
        descs = data.get("x-tag-descriptions", {})
        assert len(descs) == 52, f"Expected 52 descriptions, got {len(descs)}"
        for tag in VALID_TAGS:
            assert tag in descs, f"Missing description for tag: {tag}"
            assert len(descs[tag]) > 10, f"Description too short for tag: {tag}"

    @pytest.mark.parametrize("schema_file", SCHEMAS_WITH_TAGS)
    def test_schema_references_shared_tags(self, repo_root, schema_file):
        path = repo_root / "schemas" / schema_file
        data = json.loads(path.read_text())
        tags = data["properties"]["tags"]
        ref = tags["items"].get("$ref", "")
        assert "tags-definitions.json" in ref, (
            f"{schema_file}: tags.items should $ref tags-definitions.json"
        )

    def test_all_schemas_remain_valid_draft7(self, repo_root):
        from jsonschema import Draft7Validator
        schemas_dir = repo_root / "schemas"
        registry = _build_registry(schemas_dir)
        for schema_file in SCHEMAS_WITH_TAGS:
            path = schemas_dir / schema_file
            schema = json.loads(path.read_text())
            # Should not raise
            Draft7Validator.check_schema(schema)

    def test_ref_resolution_valid_tag(self, repo_root):
        schemas_dir = repo_root / "schemas"
        schema = load_json_schema(schemas_dir / "course-scheme.json")
        data = {
            "id": "2b7dc507-81e3-4b70-88e6-41ed44239966",
            "topic": "bitcoin",
            "subtopic": "bitcoin",
            "level": "beginner",
            "hours": 7,
            "professors_id": ["2e1b5182-567e-453a-af29-36009340ff02"],
            "original_language": "en",
            "proofreading": [{"language": "en", "urgency": 1, "reward": 0}],
            "tags": ["software", "wallets"],
        }
        result = validate_yaml_against_schema(
            data, schema, "test.yml", schema_dir=schemas_dir,
        )
        assert result.is_valid, f"Valid tags should pass: {result.errors}"

    def test_ref_resolution_invalid_tag(self, repo_root):
        schemas_dir = repo_root / "schemas"
        schema = load_json_schema(schemas_dir / "course-scheme.json")
        data = {
            "id": "2b7dc507-81e3-4b70-88e6-41ed44239966",
            "topic": "bitcoin",
            "subtopic": "bitcoin",
            "level": "beginner",
            "hours": 7,
            "professors_id": ["2e1b5182-567e-453a-af29-36009340ff02"],
            "original_language": "en",
            "proofreading": [{"language": "en", "urgency": 1, "reward": 0}],
            "tags": ["invalid-tag-name"],
        }
        result = validate_yaml_against_schema(
            data, schema, "test.yml", schema_dir=schemas_dir,
        )
        assert not result.is_valid, "Invalid tag should fail validation"
        assert any("invalid-tag-name" in e for e in result.errors)

    def test_build_registry_caches(self, repo_root):
        from bec.lib.schema import _registry_cache
        schemas_dir = repo_root / "schemas"
        _registry_cache.clear()
        r1 = _build_registry(schemas_dir)
        r2 = _build_registry(schemas_dir)
        assert r1 is r2, "Registry should be cached"
