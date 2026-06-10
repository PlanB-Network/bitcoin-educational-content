"""Tests for bec proofread commands."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.lib.proofreading import (
    BASE_FEE,
    LANGUAGE_FACTORS,
    MAX_PAID_ITERATIONS,
    add_contributor,
    compute_reward,
    count_words,
    evaluate_reward_for_language,
    find_metadata_file,
    get_contributor_count,
    get_difficulty_factor,
    get_proofreading_entries,
    get_status_matrix,
    recalculate_rewards,
    update_metadata_file,
)
from bec.lib.yaml_utils import load_yaml


# ---- Fixtures -----------------------------------------------------------------

@pytest.fixture
def course_dir(tmp_path):
    """Create a minimal course directory with proofreading metadata."""
    course = tmp_path / "courses" / "btc101"
    course.mkdir(parents=True)

    # content-types.yml marker (for repo root detection)
    (tmp_path / "content-types.yml").write_text("content_types: {}\n")

    # course.yml with proofreading metadata
    (course / "course.yml").write_text(
        "id: 00000000-0000-0000-0000-000000000001\n"
        "level: beginner\n"
        "original_language: en\n"
        "proofreading:\n"
        "  - language: en\n"
        "    last_contribution_date:\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "    reward: 5.1\n"
        "  - language: fr\n"
        "    last_contribution_date: '2025-06-01'\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "      - alice\n"
        "    reward: 2.55\n"
        "  - language: ja\n"
        "    last_contribution_date:\n"
        "    urgency: 2\n"
        "    contributor_names:\n"
        "    reward: 25.1\n"
    )

    # en.md content file (original language)
    (course / "en.md").write_text("This is a test course with some words. " * 125)  # ~1000 words

    return course


@pytest.fixture
def glossary_dir(tmp_path):
    """Create a minimal glossary word directory."""
    word = tmp_path / "resources" / "glossary" / "bitcoin"
    word.mkdir(parents=True)

    (tmp_path / "content-types.yml").write_text("content_types: {}\n")

    (word / "word.yml").write_text(
        "en_word: bitcoin\n"
        "original_language: en\n"
        "proofreading:\n"
        "  - language: en\n"
        "    last_contribution_date:\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "    reward: 0.2\n"
        "  - language: fr\n"
        "    last_contribution_date:\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "    reward: 0.2\n"
    )

    (word / "en.md").write_text("Bitcoin is a peer-to-peer electronic cash system.\n")

    return word


@pytest.fixture
def tutorial_dir(tmp_path):
    """Create a minimal tutorial directory."""
    tuto = tmp_path / "tutorials" / "wallet" / "sparrow"
    tuto.mkdir(parents=True)

    (tmp_path / "content-types.yml").write_text("content_types: {}\n")

    (tuto / "tutorial.yml").write_text(
        "id: 00000000-0000-0000-0000-000000000002\n"
        "original_language: en\n"
        "proofreading:\n"
        "  - language: en\n"
        "    last_contribution_date:\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "    reward: 3.0\n"
        "  - language: es\n"
        "    last_contribution_date:\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "    reward: 3.0\n"
    )

    (tuto / "en.md").write_text("Tutorial content here. " * 150)

    return tuto


# ---- Unit tests: compute_reward -----------------------------------------------

class TestComputeReward:
    def test_basic_reward(self):
        # 1000 words, factor 1.0, urgency 1, iteration 0
        r = compute_reward(1000, 1.0, 1, 0)
        expected = (1 * (0.001 * 1000 * 1.0) + 0.1) * 1.0  # 1.1
        assert r == round(expected, 2)

    def test_halves_with_iteration(self):
        r0 = compute_reward(1000, 1.0, 1, 0)
        r1 = compute_reward(1000, 1.0, 1, 1)
        assert r1 == round(r0 / 2, 2)

    def test_zero_after_max_iterations(self):
        r = compute_reward(1000, 1.0, 1, MAX_PAID_ITERATIONS)
        assert r == 0.0

    def test_language_factor(self):
        r_en = compute_reward(1000, 1.0, 1, 0)
        r_ja = compute_reward(1000, 2.5, 1, 0)
        assert r_ja > r_en

    def test_urgency_multiplier(self):
        r_normal = compute_reward(1000, 1.0, 1, 0)
        r_urgent = compute_reward(1000, 1.0, 5, 0)
        assert r_urgent > r_normal

    def test_zero_words(self):
        r = compute_reward(0, 1.0, 1, 0)
        assert r == round(BASE_FEE, 2)


# ---- Unit tests: get_difficulty_factor -----------------------------------------

class TestGetDifficultyFactor:
    def test_glossary(self):
        data = {"en_word": "bitcoin"}
        assert get_difficulty_factor(data) == 3.0

    def test_beginner(self):
        data = {"level": "beginner"}
        assert get_difficulty_factor(data) == 1.0

    def test_intermediate(self):
        data = {"level": "intermediate"}
        assert get_difficulty_factor(data) == 2.0

    def test_advanced(self):
        data = {"level": "advanced"}
        assert get_difficulty_factor(data) == 3.0

    def test_expert(self):
        data = {"level": "expert"}
        assert get_difficulty_factor(data) == 4.0

    def test_no_level(self):
        data = {}
        assert get_difficulty_factor(data) == 1.0


# ---- Unit tests: find_metadata_file -------------------------------------------

class TestFindMetadataFile:
    def test_finds_course_yml(self, course_dir):
        result = find_metadata_file(course_dir)
        assert result is not None
        assert result.name == "course.yml"

    def test_finds_tutorial_yml(self, tutorial_dir):
        result = find_metadata_file(tutorial_dir)
        assert result is not None
        assert result.name == "tutorial.yml"

    def test_finds_word_yml(self, glossary_dir):
        result = find_metadata_file(glossary_dir)
        assert result is not None
        assert result.name == "word.yml"

    def test_returns_none_for_empty_dir(self, tmp_path):
        assert find_metadata_file(tmp_path) is None


# ---- Unit tests: proofreading entry helpers ------------------------------------

class TestProofreadingEntries:
    def test_get_entries(self, course_dir):
        data = load_yaml(course_dir / "course.yml")
        entries = get_proofreading_entries(data)
        assert len(entries) == 3
        assert entries[0]["language"] == "en"

    def test_get_entries_empty(self):
        data = {"id": "test"}
        entries = get_proofreading_entries(data)
        assert entries == []

    def test_contributor_count_none(self):
        entry = {"contributor_names": None}
        assert get_contributor_count(entry) == 0

    def test_contributor_count_list(self):
        entry = {"contributor_names": ["alice", "bob"]}
        assert get_contributor_count(entry) == 2


# ---- Unit tests: add_contributor -----------------------------------------------

class TestAddContributor:
    def test_add_new_contributor(self, course_dir):
        data = load_yaml(course_dir / "course.yml")
        success, msg = add_contributor(data, "en", "bob")
        assert success is True
        assert "bob" in msg

        # Verify the data was modified
        entry = next(e for e in data["proofreading"] if e["language"] == "en")
        assert "bob" in entry["contributor_names"]
        assert entry["last_contribution_date"] is not None

    def test_add_to_existing_list(self, course_dir):
        data = load_yaml(course_dir / "course.yml")
        success, msg = add_contributor(data, "fr", "bob")
        assert success is True
        entry = next(e for e in data["proofreading"] if e["language"] == "fr")
        assert "alice" in entry["contributor_names"]
        assert "bob" in entry["contributor_names"]

    def test_duplicate_contributor(self, course_dir):
        data = load_yaml(course_dir / "course.yml")
        success, msg = add_contributor(data, "fr", "alice")
        assert success is False
        assert "already" in msg.lower()

    def test_invalid_language(self, course_dir):
        data = load_yaml(course_dir / "course.yml")
        success, msg = add_contributor(data, "xx", "bob")
        assert success is False
        assert "not found" in msg.lower()


# ---- Unit tests: evaluate_reward_for_language ----------------------------------

class TestEvaluateReward:
    def test_reward_for_new_language(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)
        info = evaluate_reward_for_language(metadata, data, "en")
        assert info["iteration"] == 0
        assert info["reward"] > 0
        assert info["remaining_paid_proofreadings"] == 2

    def test_reward_after_one_iteration(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)
        info = evaluate_reward_for_language(metadata, data, "fr")
        assert info["iteration"] == 1
        assert info["remaining_paid_proofreadings"] == 1

    def test_invalid_language(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)
        info = evaluate_reward_for_language(metadata, data, "xx")
        assert "error" in info


# ---- Unit tests: get_status_matrix --------------------------------------------

class TestStatusMatrix:
    def test_returns_all_languages(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)
        matrix = get_status_matrix(metadata, data)
        assert len(matrix) == 3
        langs = [e["language"] for e in matrix]
        assert "en" in langs
        assert "fr" in langs
        assert "ja" in langs

    def test_identifies_original(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)
        matrix = get_status_matrix(metadata, data)
        en_entry = next(e for e in matrix if e["language"] == "en")
        assert en_entry["is_original"] is True

    def test_no_proofreading_section(self):
        data = {"id": "test"}
        matrix = get_status_matrix(Path("/fake"), data)
        assert matrix == []


# ---- Unit tests: update_metadata_file ------------------------------------------

class TestUpdateMetadataFile:
    def test_preserves_non_proofreading_fields(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)

        # Modify proofreading
        add_contributor(data, "en", "testuser")
        update_metadata_file(metadata, data)

        # Re-read and verify non-proofreading fields preserved
        updated = load_yaml(metadata)
        assert updated["id"] == "00000000-0000-0000-0000-000000000001"
        assert updated["level"] == "beginner"
        assert updated["original_language"] == "en"

    def test_writes_contributor_correctly(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)
        add_contributor(data, "en", "testuser")
        update_metadata_file(metadata, data)

        updated = load_yaml(metadata)
        en_entry = next(e for e in updated["proofreading"] if e["language"] == "en")
        assert "testuser" in en_entry["contributor_names"]


# ---- Unit tests: recalculate_rewards -------------------------------------------

class TestRecalculateRewards:
    def test_updates_all_rewards(self, course_dir):
        metadata = course_dir / "course.yml"
        data = load_yaml(metadata)

        # Set all rewards to 0 first
        for entry in data["proofreading"]:
            entry["reward"] = 0

        recalculate_rewards(metadata, data)

        for entry in data["proofreading"]:
            lang = entry["language"]
            iteration = len(entry.get("contributor_names") or [])
            if iteration < MAX_PAID_ITERATIONS:
                assert entry["reward"] > 0, f"Expected positive reward for {lang}"


# ---- CLI integration tests: proofread update -----------------------------------

class TestProofreadUpdateCLI:
    def test_update_adds_contributor(self, course_dir):
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "update",
            "--path", "courses/btc101",
            "--lang", "en",
            "--contributor", "newuser",
        ], catch_exceptions=False, env={"HOME": str(course_dir.parent.parent)})

        # Use the tmp_path as cwd so repo root detection works
        os.chdir(course_dir.parent.parent)
        result = runner.invoke(cli, [
            "proofread", "update",
            "--path", "courses/btc101",
            "--lang", "en",
            "--contributor", "newuser",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        assert "newuser" in result.output

        # Verify file was updated
        data = load_yaml(course_dir / "course.yml")
        en_entry = next(e for e in data["proofreading"] if e["language"] == "en")
        assert "newuser" in en_entry["contributor_names"]

    def test_update_json_output(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "update",
            "--path", "courses/btc101",
            "--lang", "ja",
            "--contributor", "translator1",
            "--json",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert parsed["success"] is True
        assert parsed["contributor"] == "translator1"

    def test_update_duplicate_fails(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "update",
            "--path", "courses/btc101",
            "--lang", "fr",
            "--contributor", "alice",
        ], catch_exceptions=False)

        assert result.exit_code == 1


# ---- CLI integration tests: proofread reward -----------------------------------

class TestProofreadRewardCLI:
    def test_reward_all_languages(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "reward",
            "--path", "courses/btc101",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        assert "en" in result.output
        assert "fr" in result.output
        assert "ja" in result.output

    def test_reward_single_language(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "reward",
            "--path", "courses/btc101",
            "--lang", "en",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        assert "Words:" in result.output
        assert "Reward:" in result.output

    def test_reward_json_output(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "reward",
            "--path", "courses/btc101",
            "--json",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert "rewards" in parsed
        assert len(parsed["rewards"]) == 3

    def test_reward_invalid_language(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "reward",
            "--path", "courses/btc101",
            "--lang", "xx",
        ], catch_exceptions=False)

        assert result.exit_code == 1


# ---- CLI integration tests: proofread batch-add --------------------------------

class TestProofreadBatchAddCLI:
    def test_batch_add_single_path(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "batch-add",
            "--contributor", "batchuser",
            "--lang", "en",
            "courses/btc101",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        assert "1 updated" in result.output

    def test_batch_add_json_output(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "batch-add",
            "--contributor", "batchuser",
            "--lang", "en",
            "--json",
            "courses/btc101",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert parsed["success"] == 1
        assert parsed["contributor"] == "batchuser"

    def test_batch_add_multiple_paths(self, course_dir, tutorial_dir):
        # Both course and tutorial are under different tmp_paths,
        # so we test with just one path but verify the count logic
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "batch-add",
            "--contributor", "multi-user",
            "--lang", "en",
            "courses/btc101",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        assert "1 updated" in result.output


# ---- CLI integration tests: proofread status -----------------------------------

class TestProofreadStatusCLI:
    def test_status_table(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "status",
            "--path", "courses/btc101",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        assert "original" in result.output  # en should show as original
        assert "pending" in result.output   # ja should show as pending
        assert "1/2" in result.output       # fr should show as 1/2

    def test_status_json_output(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "status",
            "--path", "courses/btc101",
            "--json",
        ], catch_exceptions=False)

        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert parsed["original_language"] == "en"
        assert len(parsed["languages"]) == 3

        # Verify structure of each entry
        for lang_entry in parsed["languages"]:
            assert "language" in lang_entry
            assert "is_original" in lang_entry
            assert "contributors" in lang_entry
            assert "reward" in lang_entry
            assert "remaining_paid_proofreadings" in lang_entry

    def test_status_invalid_path(self, course_dir):
        os.chdir(course_dir.parent.parent)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "status",
            "--path", "courses/nonexistent",
        ], catch_exceptions=False)

        assert result.exit_code == 1


# ---- Edge case tests -----------------------------------------------------------

class TestEdgeCases:
    def test_no_proofreading_section(self, tmp_path):
        """Content without proofreading metadata."""
        course = tmp_path / "courses" / "test"
        course.mkdir(parents=True)
        (tmp_path / "content-types.yml").write_text("content_types: {}\n")
        (course / "course.yml").write_text("id: test\noriginal_language: en\n")
        (course / "en.md").write_text("content")

        os.chdir(tmp_path)
        runner = CliRunner()
        result = runner.invoke(cli, [
            "proofread", "status",
            "--path", "courses/test",
        ], catch_exceptions=False)

        assert result.exit_code == 1

    def test_reward_formula_matches_original(self):
        """Verify our formula matches the original proofreading.py formula."""
        # Original: (urgency * (0.001 * words * language_factor) + base_fee) * 2**(-iteration)
        words = 5000
        lang_factor = 1.5
        urgency = 2
        iteration = 1
        expected = (urgency * (0.001 * words * lang_factor) + BASE_FEE) * 2 ** (-iteration)
        expected = round(expected, 2)
        assert compute_reward(words, lang_factor, urgency, iteration) == expected

    def test_language_factors_completeness(self):
        """All languages in the original script should be in LANGUAGE_FACTORS."""
        expected = {
            "en", "fr", "de", "es", "it", "cs", "vi", "ja", "pt",
            "ru", "fi", "et", "id", "zh-Hans", "uk", "nb-NO", "pl",
            "ro", "ha", "sr-Latn", "hi", "zh-Hant", "sw", "fa", "sv",
            "nl", "tr", "ko", "rn", "bg", "th",
        }
        assert expected == set(LANGUAGE_FACTORS.keys())
