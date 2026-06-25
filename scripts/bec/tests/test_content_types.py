"""Tests for bec.lib.content_types."""

from pathlib import Path

import pytest

from bec.lib.content_types import load_registry, ContentRegistry


@pytest.fixture
def registry(repo_root) -> ContentRegistry:
    """Load the real content-types.yml registry."""
    return load_registry(repo_root)


class TestLoadRegistry:
    def test_loads_all_14_content_types(self, registry):
        assert len(registry.content_types) == 14

    def test_content_type_keys(self, registry):
        expected = {
            "course", "tutorial", "professor", "event",
            "bet", "book", "channel", "conference",
            "glossary", "movie", "newsletter", "podcast",
            "project", "paper",
        }
        assert set(registry.content_types.keys()) == expected

    def test_each_type_has_required_fields(self, registry):
        for key, ct in registry.content_types.items():
            assert ct.name, f"{key} missing name"
            assert ct.path_pattern, f"{key} missing path_pattern"
            assert ct.metadata_file, f"{key} missing metadata_file"
            assert ct.schema, f"{key} missing schema"

    def test_tutorial_categories(self, registry):
        assert len(registry.tutorial_categories) == 8
        assert "wallet" in registry.tutorial_categories
        assert "mining" in registry.tutorial_categories

    def test_discipline_codes(self, registry):
        assert len(registry.discipline_codes) >= 17
        assert registry.discipline_codes["btc"] == "Bitcoin Core"
        assert registry.discipline_codes["lnp"] == "Lightning Network"

    def test_tags_count(self, registry):
        assert len(registry.tags) == 52

    def test_languages(self, registry):
        assert "en" in registry.languages
        assert "fr" in registry.languages
        assert len(registry.languages) >= 30

    def test_quiz_schemas(self, registry):
        assert "question" in registry.quiz_schemas
        assert "translation" in registry.quiz_schemas


class TestGetSchemaPath:
    def test_course_schema_path(self, registry, repo_root):
        path = registry.get_schema_path("course", repo_root)
        assert path.name == "course-scheme.json"

    def test_content_schema_path(self, registry, repo_root):
        path = registry.get_content_schema_path("course", repo_root)
        assert path is not None
        assert path.name == "course-content-scheme.json"

    def test_no_content_schema(self, registry, repo_root):
        path = registry.get_content_schema_path("event", repo_root)
        assert path is None


class TestDetectTypeFromPath:
    def test_detect_course(self, registry, repo_root):
        path = repo_root / "courses" / "btc101"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is not None
        assert ct.key == "course"

    def test_detect_tutorial(self, registry, repo_root):
        path = repo_root / "tutorials" / "wallet" / "sparrow"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is not None
        assert ct.key == "tutorial"

    def test_detect_professor(self, registry, repo_root):
        path = repo_root / "professors" / "asi0"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is not None
        assert ct.key == "professor"

    def test_detect_event(self, registry, repo_root):
        path = repo_root / "events" / "bitcoin-nashville-2024"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is not None
        assert ct.key == "event"

    def test_detect_book(self, registry, repo_root):
        path = repo_root / "resources" / "books" / "mastering-bitcoin"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is not None
        assert ct.key == "book"

    def test_detect_glossary(self, registry, repo_root):
        path = repo_root / "resources" / "glossary" / "51-percent-attack"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is not None
        assert ct.key == "glossary"

    def test_detect_unknown(self, registry, repo_root):
        path = repo_root / "unknown" / "something"
        ct = registry.detect_type_from_path(path, repo_root)
        assert ct is None


class TestSchemaPathsExist:
    def test_all_schema_files_exist(self, registry, repo_root):
        for key, ct in registry.content_types.items():
            schema_path = repo_root / ct.schema
            assert schema_path.is_file(), f"Schema missing for {key}: {ct.schema}"

    def test_all_content_schema_files_exist(self, registry, repo_root):
        for key, ct in registry.content_types.items():
            if ct.content_schema:
                schema_path = repo_root / ct.content_schema
                assert schema_path.is_file(), f"Content schema missing for {key}: {ct.content_schema}"

    def test_quiz_schema_files_exist(self, registry, repo_root):
        for key, path_str in registry.quiz_schemas.items():
            schema_path = repo_root / path_str
            assert schema_path.is_file(), f"Quiz schema missing for {key}: {path_str}"

    def test_all_example_paths_exist(self, registry, repo_root):
        for key, ct in registry.content_types.items():
            if ct.example:
                example_path = repo_root / ct.example
                assert example_path.is_dir(), f"Example missing for {key}: {ct.example}"
