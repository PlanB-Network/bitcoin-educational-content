"""Tests for bec add quiz / add language commands."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.add import (
    _create_language_md,
    _create_language_yml,
    _find_source_lang,
    _next_quiz_number,
    _list_chapter_ids,
)


# ---- Unit tests for quiz helpers ----


class TestNextQuizNumber:
    def test_empty_dir(self, tmp_path):
        quizz_dir = tmp_path / "quizz"
        quizz_dir.mkdir()
        assert _next_quiz_number(quizz_dir) == 0

    def test_nonexistent_dir(self, tmp_path):
        assert _next_quiz_number(tmp_path / "nope") == 0

    def test_sequential(self, tmp_path):
        quizz_dir = tmp_path / "quizz"
        quizz_dir.mkdir()
        (quizz_dir / "000").mkdir()
        (quizz_dir / "001").mkdir()
        (quizz_dir / "002").mkdir()
        assert _next_quiz_number(quizz_dir) == 3

    def test_with_gaps(self, tmp_path):
        quizz_dir = tmp_path / "quizz"
        quizz_dir.mkdir()
        (quizz_dir / "000").mkdir()
        (quizz_dir / "005").mkdir()
        # Should use max + 1, so 6
        assert _next_quiz_number(quizz_dir) == 6

    def test_ignores_non_numeric_dirs(self, tmp_path):
        quizz_dir = tmp_path / "quizz"
        quizz_dir.mkdir()
        (quizz_dir / "000").mkdir()
        (quizz_dir / "readme.txt").touch()
        (quizz_dir / "old").mkdir()
        assert _next_quiz_number(quizz_dir) == 1


class TestListChapterIds:
    def test_extracts_chapter_ids(self, tmp_path, repo_root):
        # Use a temp course in the real repo
        course_dir = repo_root / "courses" / "_test_chapter_list"
        course_dir.mkdir(parents=True, exist_ok=True)
        try:
            (course_dir / "course.yml").write_text("id: test\n", encoding="utf-8")
            (course_dir / "en.md").write_text(
                "---\nname: Test\n---\n\n"
                "## Ch1\n\n<chapterId>aaa-bbb-ccc</chapterId>\n\n"
                "## Ch2\n\n<chapterId>ddd-eee-fff</chapterId>\n",
                encoding="utf-8",
            )
            result = _list_chapter_ids("_test_chapter_list", repo_root)
            assert result == ["aaa-bbb-ccc", "ddd-eee-fff"]
        finally:
            shutil.rmtree(course_dir)

    def test_deduplicates(self, tmp_path, repo_root):
        course_dir = repo_root / "courses" / "_test_chapter_dedup"
        course_dir.mkdir(parents=True, exist_ok=True)
        try:
            (course_dir / "course.yml").write_text("id: test\n", encoding="utf-8")
            # Same chapterId in two language files
            for lang in ("en", "fr"):
                (course_dir / f"{lang}.md").write_text(
                    f"---\nname: Test\n---\n\n## Ch1\n\n<chapterId>same-id</chapterId>\n",
                    encoding="utf-8",
                )
            result = _list_chapter_ids("_test_chapter_dedup", repo_root)
            assert result == ["same-id"]
        finally:
            shutil.rmtree(course_dir)

    def test_missing_course(self, repo_root):
        assert _list_chapter_ids("nonexistent999", repo_root) == []


# ---- Unit tests for language helpers ----


class TestFindSourceLang:
    def test_prefers_en(self, tmp_path):
        (tmp_path / "en.md").touch()
        (tmp_path / "fr.md").touch()
        assert _find_source_lang(tmp_path) == "en"

    def test_prefers_en_yml(self, tmp_path):
        (tmp_path / "en.yml").touch()
        (tmp_path / "fr.yml").touch()
        assert _find_source_lang(tmp_path) == "en"

    def test_falls_back_to_first(self, tmp_path):
        (tmp_path / "fr.md").touch()
        (tmp_path / "es.md").touch()
        assert _find_source_lang(tmp_path) == "es"  # sorted: es < fr

    def test_accepts_regional_codes(self, tmp_path):
        (tmp_path / "zh-Hans.md").touch()
        assert _find_source_lang(tmp_path) == "zh-Hans"

    def test_accepts_regional_codes_yml(self, tmp_path):
        (tmp_path / "nb-NO.yml").touch()
        assert _find_source_lang(tmp_path) == "nb-NO"
        (tmp_path / "nb-NO.yml").unlink()
        (tmp_path / "sr-Latn.yml").touch()
        assert _find_source_lang(tmp_path) == "sr-Latn"

    def test_returns_none_if_empty(self, tmp_path):
        assert _find_source_lang(tmp_path) is None

    def test_ignores_non_lang_files(self, tmp_path):
        (tmp_path / "course.yml").touch()
        (tmp_path / "tutorial.yml").touch()
        (tmp_path / "README.md").touch()
        assert _find_source_lang(tmp_path) is None


class TestCreateLanguageMd:
    def test_preserves_frontmatter_keys(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            '---\nname: "Bitcoin 101"\ngoal: "Learn Bitcoin"\nobjectives:\n  - "Understand keys"\n  - "Use wallets"\n---\n\nContent.\n',
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "---\n" in text
        assert 'name: "TODO"' in text
        assert 'goal: "TODO"' in text

    def test_preserves_chapter_ids(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            "---\nname: Test\n---\n\n"
            "## Chapter 1\n\n"
            "<chapterId>abc-def-ghi</chapterId>\n\n"
            "Content here.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "<chapterId>abc-def-ghi</chapterId>" in text

    def test_preserves_part_ids(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            "---\nname: Test\n---\n\n"
            "+++\n\n"
            "# Part 1\n\n"
            "<partId>part-uuid-here</partId>\n\n"
            "## Chapter 1\n\n"
            "<chapterId>ch-uuid</chapterId>\n\n"
            "Content.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "<partId>part-uuid-here</partId>" in text
        assert "+++" in text

    def test_preserves_separators(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            "---\nname: Test\n---\n\n+++\n\n# Part\n\nText.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "+++" in text

    def test_replaces_prose_with_todo(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            "---\nname: Test\n---\n\n## Heading\n\nSome prose content here.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "Some prose content here" not in text
        assert "TODO" in text

    def test_preserves_images(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            "---\nname: Test\n---\n\n![cover](assets/cover.webp)\n\nText.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "![cover](assets/cover.webp)" in text

    def test_unterminated_frontmatter_raises_click_error(self, tmp_path):
        import click

        source = tmp_path / "en.md"
        source.write_text("---\nname: Broken\nno closing fence\n", encoding="utf-8")
        target = tmp_path / "fr.md"
        with pytest.raises(click.ClickException, match=r"Unterminated frontmatter.*en\.md"):
            _create_language_md(source, target, "fr")

    def test_heading_structure_preserved(self, tmp_path):
        source = tmp_path / "en.md"
        source.write_text(
            "---\nname: Test\n---\n\n"
            "# Big Heading\n\n"
            "## Sub Heading\n\n"
            "### Sub Sub Heading\n\n"
            "Paragraph.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.md"
        _create_language_md(source, target, "fr")
        text = target.read_text(encoding="utf-8")
        assert "# TODO\n" in text
        assert "## TODO\n" in text
        assert "### TODO\n" in text


class TestCreateLanguageYml:
    def test_replaces_strings(self, tmp_path):
        source = tmp_path / "en.yml"
        source.write_text(
            "title: Bitcoin Book\ndescription: A great book about Bitcoin.\n",
            encoding="utf-8",
        )
        target = tmp_path / "fr.yml"
        _create_language_yml(source, target)

        from bec.lib.yaml_utils import load_yaml
        data = load_yaml(target)
        assert data["title"] == "TODO"
        assert data["description"] == "TODO"

    def test_preserves_booleans(self, tmp_path):
        source = tmp_path / "en.yml"
        source.write_text("original: true\ntitle: Test\n", encoding="utf-8")
        target = tmp_path / "fr.yml"
        _create_language_yml(source, target)

        from bec.lib.yaml_utils import load_yaml
        data = load_yaml(target)
        assert data["original"] is True
        assert data["title"] == "TODO"

    def test_preserves_numbers(self, tmp_path):
        source = tmp_path / "en.yml"
        source.write_text("publication_year: 2024\ntitle: Test\n", encoding="utf-8")
        target = tmp_path / "fr.yml"
        _create_language_yml(source, target)

        from bec.lib.yaml_utils import load_yaml
        data = load_yaml(target)
        assert data["publication_year"] == 2024
        assert data["title"] == "TODO"


# ---- CLI integration tests ----


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def quiz_course(repo_root):
    """Create a temporary course with chapters for quiz testing."""
    course_dir = repo_root / "courses" / "_test_quiz_course"
    course_dir.mkdir(parents=True, exist_ok=True)

    (course_dir / "course.yml").write_text(
        "id: 00000000-0000-0000-0000-000000000099\ntopic: bitcoin\n",
        encoding="utf-8",
    )

    (course_dir / "en.md").write_text(
        "---\nname: Test Quiz Course\ngoal: Testing quizzes\nobjectives:\n  - Test\n---\n\n"
        "+++\n\n"
        "# Part 1\n\n"
        "<partId>00000000-0000-0000-0000-000000000001</partId>\n\n"
        "## Chapter 1\n\n"
        "<chapterId>test-chapter-id-001</chapterId>\n\n"
        "Content.\n",
        encoding="utf-8",
    )

    yield course_dir

    if course_dir.exists():
        shutil.rmtree(course_dir)


@pytest.fixture
def lang_course(repo_root):
    """Create a temporary course for language testing."""
    course_dir = repo_root / "courses" / "_test_lang_course"
    course_dir.mkdir(parents=True, exist_ok=True)

    (course_dir / "course.yml").write_text(
        "id: 00000000-0000-0000-0000-000000000098\ntopic: bitcoin\n",
        encoding="utf-8",
    )

    (course_dir / "en.md").write_text(
        '---\nname: "Language Test Course"\ngoal: "Test language addition"\nobjectives:\n  - "First objective"\n  - "Second objective"\n---\n\n'
        "# Course Description\n\n"
        "This is the course description.\n\n"
        "+++\n\n"
        "# Part 1 — Introduction\n\n"
        "<partId>00000000-0000-0000-0000-000000000010</partId>\n\n"
        "## Chapter 1 — Getting Started\n\n"
        "<chapterId>00000000-0000-0000-0000-000000000011</chapterId>\n\n"
        "Chapter content here.\n\n"
        "![diagram](assets/en/diagram.webp)\n\n"
        "More content.\n",
        encoding="utf-8",
    )

    yield course_dir

    if course_dir.exists():
        shutil.rmtree(course_dir)


@pytest.fixture
def lang_tutorial(repo_root):
    """Create a temporary tutorial for language testing."""
    tuto_dir = repo_root / "tutorials" / "wallet" / "_test_lang_tuto"
    tuto_dir.mkdir(parents=True, exist_ok=True)

    (tuto_dir / "tutorial.yml").write_text(
        "id: 00000000-0000-0000-0000-000000000097\nlevel: beginner\n",
        encoding="utf-8",
    )

    (tuto_dir / "en.md").write_text(
        '---\nname: "Test Tutorial"\ndescription: "A test tutorial"\n---\n\n'
        "![cover](assets/cover.webp)\n\n"
        "## Introduction\n\n"
        "Tutorial content here.\n\n"
        "## Step 1\n\n"
        "Step content.\n",
        encoding="utf-8",
    )

    yield tuto_dir

    if tuto_dir.exists():
        shutil.rmtree(tuto_dir)


@pytest.fixture
def lang_resource(repo_root):
    """Create a temporary book resource for language testing."""
    book_dir = repo_root / "resources" / "books" / "_test_lang_book"
    book_dir.mkdir(parents=True, exist_ok=True)

    (book_dir / "book.yml").write_text(
        "author: Test Author\nlevel: beginner\ntags:\n  - software\n",
        encoding="utf-8",
    )

    (book_dir / "en.yml").write_text(
        "title: Test Book Title\npublication_year: 2024\ncover: cover_en.webp\noriginal: true\ndescription: |\n  A great book about Bitcoin.\n",
        encoding="utf-8",
    )

    (book_dir / "assets").mkdir(exist_ok=True)

    yield book_dir

    if book_dir.exists():
        shutil.rmtree(book_dir)


# ---- Quiz CLI tests ----


class TestAddQuizCommand:
    def test_creates_quiz_folder(self, runner, quiz_course, repo_root):
        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "easy",
            "--author", "test-author",
        ])
        assert result.exit_code == 0, result.output
        assert "Created quiz 000" in result.output

        quiz_dir = quiz_course / "quizz" / "000"
        assert quiz_dir.is_dir()
        assert (quiz_dir / "question.yml").is_file()
        assert (quiz_dir / "en.yml").is_file()

    def test_question_yml_content(self, runner, quiz_course):
        runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "intermediate",
            "--author", "satoshi",
        ])
        from bec.lib.yaml_utils import load_yaml
        data = load_yaml(quiz_course / "quizz" / "000" / "question.yml")
        # LMS uses question id as primary key — must be a UUID
        assert re.match(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
            data["id"],
        )
        assert data["chapterId"] == "test-chapter-id-001"
        assert data["difficulty"] == "intermediate"
        assert data["author"] == "satoshi"
        assert data["tags"] == ["software"]

    def test_translation_yml_content(self, runner, quiz_course):
        runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "easy",
            "--author", "test",
        ])
        from bec.lib.yaml_utils import load_yaml
        data = load_yaml(quiz_course / "quizz" / "000" / "en.yml")
        assert "question" in data
        assert "answer" in data
        assert "wrong_answers" in data
        assert len(data["wrong_answers"]) == 3
        assert "explanation" in data
        assert data["reviewed"] is False

    def test_auto_numbering(self, runner, quiz_course):
        """Creating multiple quizzes increments the number."""
        base_args = [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "easy",
            "--author", "test",
        ]
        # First quiz
        runner.invoke(cli, base_args)
        assert (quiz_course / "quizz" / "000").is_dir()

        # Second quiz
        runner.invoke(cli, base_args)
        assert (quiz_course / "quizz" / "001").is_dir()

        # Third quiz
        runner.invoke(cli, base_args)
        assert (quiz_course / "quizz" / "002").is_dir()

    def test_auto_numbering_with_existing(self, runner, quiz_course):
        """Numbering continues from highest existing number."""
        quizz_dir = quiz_course / "quizz"
        quizz_dir.mkdir()
        (quizz_dir / "000").mkdir()
        (quizz_dir / "003").mkdir()

        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "easy",
            "--author", "test",
        ])
        assert result.exit_code == 0
        assert (quizz_dir / "004").is_dir()

    def test_json_output(self, runner, quiz_course):
        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "hard",
            "--author", "test",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["action"] == "add_quiz"
        assert data["course"] == "_test_quiz_course"
        assert data["quiz_number"] == "000"
        assert data["chapter_id"] == "test-chapter-id-001"
        assert data["difficulty"] == "hard"
        assert "files" in data
        assert len(data["files"]) == 2

    def test_missing_course_fails(self, runner):
        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "nonexistent999",
            "--chapter-id", "some-id",
            "--lang", "en",
        ])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_invalid_difficulty_fails(self, runner, quiz_course):
        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "en",
            "--difficulty", "impossible",
        ])
        assert result.exit_code != 0
        assert "invalid difficulty" in result.output.lower()

    def test_unknown_chapter_id_fails(self, runner, quiz_course):
        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "does-not-exist",
            "--lang", "en",
            "--difficulty", "easy",
            "--author", "test",
        ])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()
        assert not (quiz_course / "quizz").exists()

    def test_invalid_lang_fails(self, runner, quiz_course):
        result = runner.invoke(cli, [
            "add", "quiz",
            "--course", "_test_quiz_course",
            "--chapter-id", "test-chapter-id-001",
            "--lang", "xx",
            "--difficulty", "easy",
            "--author", "test",
        ])
        assert result.exit_code != 0
        assert "invalid language" in result.output.lower()
        assert not (quiz_course / "quizz").exists()

    def test_interactive_prompts(self, runner, quiz_course):
        result = runner.invoke(
            cli,
            ["add", "quiz"],
            input="_test_quiz_course\ntest-chapter-id-001\nen\neasy\ntest-author\n",
        )
        assert result.exit_code == 0, result.output
        assert "Created quiz 000" in result.output


# ---- Language CLI tests ----


class TestAddLanguageCommand:
    def test_course_language(self, runner, lang_course, repo_root):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "courses/_test_lang_course",
            "--lang", "fr",
        ])
        assert result.exit_code == 0, result.output
        assert "Added language 'fr'" in result.output

        fr_md = lang_course / "fr.md"
        assert fr_md.is_file()
        text = fr_md.read_text(encoding="utf-8")
        # Frontmatter preserved
        assert "---\n" in text
        # IDs preserved
        assert "<partId>00000000-0000-0000-0000-000000000010</partId>" in text
        assert "<chapterId>00000000-0000-0000-0000-000000000011</chapterId>" in text
        # Separators preserved
        assert "+++" in text
        # Prose replaced
        assert "Chapter content here" not in text

    def test_tutorial_language(self, runner, lang_tutorial, repo_root):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "tutorials/wallet/_test_lang_tuto",
            "--lang", "es",
        ])
        assert result.exit_code == 0, result.output
        assert "Added language 'es'" in result.output

        es_md = lang_tutorial / "es.md"
        assert es_md.is_file()
        text = es_md.read_text(encoding="utf-8")
        # Frontmatter keys preserved
        assert "name:" in text
        assert "description:" in text
        # Image preserved
        assert "![cover](assets/cover.webp)" in text
        # Heading structure preserved
        assert "## TODO" in text

    def test_resource_yml_language(self, runner, lang_resource, repo_root):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "resources/books/_test_lang_book",
            "--lang", "fr",
        ])
        assert result.exit_code == 0, result.output
        assert "Added language 'fr'" in result.output

        fr_yml = lang_resource / "fr.yml"
        assert fr_yml.is_file()

        from bec.lib.yaml_utils import load_yaml
        data = load_yaml(fr_yml)
        assert data["title"] == "TODO"
        assert data["publication_year"] == 2024  # number preserved
        assert data["original"] is True  # bool preserved

    def test_duplicate_language_fails(self, runner, lang_course):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "courses/_test_lang_course",
            "--lang", "en",
        ])
        assert result.exit_code != 0
        assert "already exists" in result.output.lower()

    def test_invalid_language_fails(self, runner, lang_course):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "courses/_test_lang_course",
            "--lang", "xx",
        ])
        assert result.exit_code != 0
        assert "invalid language" in result.output.lower()

    def test_missing_path_fails(self, runner):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "courses/nonexistent999",
            "--lang", "fr",
        ])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_json_output(self, runner, lang_course):
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "courses/_test_lang_course",
            "--lang", "de",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["action"] == "add_language"
        assert data["source_lang"] == "en"
        assert data["target_lang"] == "de"
        assert data["content_type"] == "course"
        assert len(data["files"]) >= 1

    def test_preserves_chapter_ids_in_course(self, runner, lang_course):
        runner.invoke(cli, [
            "add", "language",
            "--path", "courses/_test_lang_course",
            "--lang", "ja",
        ])
        ja_md = lang_course / "ja.md"
        text = ja_md.read_text(encoding="utf-8")

        # All structural IDs must be present
        assert "<partId>00000000-0000-0000-0000-000000000010</partId>" in text
        assert "<chapterId>00000000-0000-0000-0000-000000000011</chapterId>" in text

    def test_preserves_images(self, runner, lang_course):
        runner.invoke(cli, [
            "add", "language",
            "--path", "courses/_test_lang_course",
            "--lang", "pt",
        ])
        pt_md = lang_course / "pt.md"
        text = pt_md.read_text(encoding="utf-8")
        assert "![diagram](assets/en/diagram.webp)" in text

    def test_interactive_prompts(self, runner, lang_course):
        result = runner.invoke(
            cli,
            ["add", "language"],
            input="courses/_test_lang_course\nit\n",
        )
        assert result.exit_code == 0, result.output
        assert "Added language 'it'" in result.output

    def test_works_for_tutorials_too(self, runner, lang_tutorial):
        """Language addition is not course-specific."""
        result = runner.invoke(cli, [
            "add", "language",
            "--path", "tutorials/wallet/_test_lang_tuto",
            "--lang", "fr",
        ])
        assert result.exit_code == 0, result.output
        fr_md = lang_tutorial / "fr.md"
        assert fr_md.is_file()
        text = fr_md.read_text(encoding="utf-8")
        # Tutorial prose replaced with TODO
        assert "Tutorial content here" not in text
        assert "TODO" in text
