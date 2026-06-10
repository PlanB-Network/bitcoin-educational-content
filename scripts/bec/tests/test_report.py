"""Tests for bec report commands."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.report import (
    _classify_image,
    _extract_images_from_markdown,
    _get_language_files,
    _parse_video_coverage,
    analyze_course_analytics,
    analyze_image_translation,
    analyze_proofreading,
    analyze_translation_coverage,
    analyze_video_deployment,
    count_words,
)
from bec.lib.content_types import load_registry


# ---- Fixtures -----------------------------------------------------------------

@pytest.fixture
def mini_repo(tmp_path):
    """Create a minimal repo structure with translatable content."""
    # content-types.yml marker
    (tmp_path / "content-types.yml").write_text(
        "content_types:\n"
        "  course:\n"
        "    name: Course\n"
        "    path_pattern: 'courses/{id}/'\n"
        "    metadata_file: course.yml\n"
        "    schema: schemas/course-scheme.json\n"
        "    has_markdown_content: true\n"
        "    has_quizzes: true\n"
        "    example: courses/btc101\n"
        "  tutorial:\n"
        "    name: Tutorial\n"
        "    path_pattern: 'tutorials/{category}/{id}/'\n"
        "    metadata_file: tutorial.yml\n"
        "    schema: schemas/tutorial-scheme.json\n"
        "    has_markdown_content: true\n"
        "    example: tutorials/wallet/sparrow\n"
        "  professor:\n"
        "    name: Professor\n"
        "    path_pattern: 'professors/{id}/'\n"
        "    metadata_file: professor.yml\n"
        "    schema: schemas/professor-scheme.json\n"
        "    content_uses_yml: true\n"
        "    has_markdown_content: false\n"
        "    example: professors/satoshi\n"
        "  event:\n"
        "    name: Event\n"
        "    path_pattern: 'events/{id}/'\n"
        "    metadata_file: event.yml\n"
        "    schema: schemas/event-scheme.json\n"
        "    has_markdown_content: false\n"
        "    example: events/conf-2025\n"
        "  book:\n"
        "    name: Book\n"
        "    path_pattern: 'resources/books/{id}/'\n"
        "    metadata_file: book.yml\n"
        "    schema: schemas/book-scheme.json\n"
        "    content_uses_yml: true\n"
        "    has_markdown_content: false\n"
        "    example: resources/books/mastering-bitcoin\n"
        "  channel:\n"
        "    name: Channel\n"
        "    path_pattern: 'resources/channels/{id}/'\n"
        "    metadata_file: channel.yml\n"
        "    schema: schemas/channel-scheme.json\n"
        "    has_markdown_content: false\n"
        "    example: resources/channels/robin\n"
        "languages:\n"
        "  - en\n"
        "  - fr\n"
        "  - es\n"
        "tutorial_categories:\n"
        "  - wallet\n"
        "tags: []\n"
        "discipline_codes: {}\n"
        "level_range: {}\n"
    )

    # Course btc101 with en and fr
    btc101 = tmp_path / "courses" / "btc101"
    btc101.mkdir(parents=True)
    (btc101 / "course.yml").write_text("id: abc\nlevel: beginner\n")
    (btc101 / "en.md").write_text("# Bitcoin 101\n\nThis is the English version with some words here.")
    (btc101 / "fr.md").write_text("# Bitcoin 101\n\nCeci est la version francaise.")

    # Course btc201 with en only
    btc201 = tmp_path / "courses" / "btc201"
    btc201.mkdir(parents=True)
    (btc201 / "course.yml").write_text("id: def\nlevel: intermediate\n")
    (btc201 / "en.md").write_text("# Bitcoin 201\n\nAdvanced bitcoin content here.")

    # Tutorial wallet/sparrow with en, fr, es
    tuto = tmp_path / "tutorials" / "wallet" / "sparrow"
    tuto.mkdir(parents=True)
    (tuto / "tutorial.yml").write_text("id: ghi\nlevel: beginner\n")
    (tuto / "en.md").write_text("# Sparrow Tutorial\n\nEnglish tutorial content.")
    (tuto / "fr.md").write_text("# Sparrow Tutoriel\n\nContenu francais.")
    (tuto / "es.md").write_text("# Tutorial Sparrow\n\nContenido en espanol.")

    # Professor with en.yml and fr.yml
    prof = tmp_path / "professors" / "satoshi"
    prof.mkdir(parents=True)
    (prof / "professor.yml").write_text("id: jkl\n")
    (prof / "en.yml").write_text("name: Satoshi\nbio: A mysterious figure.\n")
    (prof / "fr.yml").write_text("name: Satoshi\nbio: Un personnage mysterieux.\n")

    # Event (no translations)
    evt = tmp_path / "events" / "conf-2025"
    evt.mkdir(parents=True)
    (evt / "event.yml").write_text("id: mno\nname: Conference 2025\n")

    # Book with en.yml only
    book = tmp_path / "resources" / "books" / "mastering-bitcoin"
    book.mkdir(parents=True)
    (book / "book.yml").write_text("id: pqr\n")
    (book / "en.yml").write_text("name: Mastering Bitcoin\nauthor: Andreas\n")

    # Channel (no translations)
    chan = tmp_path / "resources" / "channels" / "robin"
    chan.mkdir(parents=True)
    (chan / "channel.yml").write_text("id: stu\n")

    return tmp_path


# ---- Unit tests: count_words --------------------------------------------------

def test_count_words_basic(tmp_path):
    f = tmp_path / "test.md"
    f.write_text("Hello world foo bar baz")
    assert count_words(f) == 5


def test_count_words_empty(tmp_path):
    f = tmp_path / "empty.md"
    f.write_text("")
    assert count_words(f) == 0


def test_count_words_nonexistent(tmp_path):
    f = tmp_path / "nope.md"
    assert count_words(f) == 0


# ---- Unit tests: _get_language_files -------------------------------------------

def test_get_language_files_md(mini_repo):
    btc101 = mini_repo / "courses" / "btc101"
    result = _get_language_files(btc101, "course")
    assert "en" in result
    assert "fr" in result
    assert result["en"] is True
    assert result["fr"] is True


def test_get_language_files_yml(mini_repo):
    prof = mini_repo / "professors" / "satoshi"
    result = _get_language_files(prof, "professor")
    assert "en" in result
    assert "fr" in result
    # professor.yml should NOT be treated as a language file
    assert "professor" not in result


def test_get_language_files_book(mini_repo):
    book = mini_repo / "resources" / "books" / "mastering-bitcoin"
    result = _get_language_files(book, "book")
    assert "en" in result
    assert "book" not in result


def test_get_language_files_event_returns_nothing(mini_repo):
    """Events have no translatable files."""
    evt = mini_repo / "events" / "conf-2025"
    result = _get_language_files(evt, "event")
    assert result == {}


# ---- Unit tests: analyze_translation_coverage ---------------------------------

def test_analyze_coverage_structure(mini_repo):
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    assert "by_type" in analysis
    assert "languages" in analysis
    assert "summary" in analysis
    assert "type_stats" in analysis
    assert "lang_stats" in analysis


def test_analyze_coverage_detects_languages(mini_repo):
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    # Should detect en, fr, es from the content files
    assert "en" in analysis["languages"]
    assert "fr" in analysis["languages"]
    assert "es" in analysis["languages"]


def test_analyze_coverage_courses(mini_repo):
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    courses = analysis["by_type"].get("course", [])
    assert len(courses) == 2  # btc101, btc201

    btc101 = next(c for c in courses if c["id"] == "btc101")
    assert "en" in btc101["languages"]
    assert "fr" in btc101["languages"]
    assert btc101["languages"]["en"]["words"] > 0

    btc201 = next(c for c in courses if c["id"] == "btc201")
    assert "en" in btc201["languages"]
    assert "fr" not in btc201["languages"]


def test_analyze_coverage_excludes_events(mini_repo):
    """Events have no translatable files and should not appear in by_type."""
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    assert "event" not in analysis["by_type"]


def test_analyze_coverage_excludes_channels(mini_repo):
    """Channels have no translatable files and should not appear in by_type."""
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    assert "channel" not in analysis["by_type"]


def test_analyze_coverage_summary(mini_repo):
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    summary = analysis["summary"]
    assert summary["total_items"] > 0
    assert summary["total_translations"] > 0
    assert summary["total_possible"] >= summary["total_translations"]
    assert 0 <= summary["coverage_pct"] <= 100


def test_analyze_coverage_type_stats(mini_repo):
    os.chdir(mini_repo)
    registry = load_registry(mini_repo)
    analysis = analyze_translation_coverage(mini_repo, registry)

    ts = analysis["type_stats"]
    assert "course" in ts
    assert ts["course"]["items"] == 2
    assert ts["course"]["translations"] == 3  # btc101: en+fr, btc201: en


# ---- CLI integration tests -----------------------------------------------------

def test_cli_report_translation_json(mini_repo):
    os.chdir(mini_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "translation", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "summary" in data
    assert "type_stats" in data
    assert "languages" in data
    assert "items" in data
    assert data["summary"]["total_items"] > 0


def test_cli_report_translation_html(mini_repo, tmp_path):
    os.chdir(mini_repo)
    runner = CliRunner()
    output_dir = tmp_path / "test_output"
    result = runner.invoke(cli, ["report", "translation", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    html_file = output_dir / "md_translation_overview.html"
    assert html_file.exists()

    html = html_file.read_text()
    assert "<!DOCTYPE html>" in html
    assert "Markdown Translation Overview" in html
    assert "btc101" in html
    assert "btc201" in html
    assert "sparrow" in html


def test_cli_report_translation_html_self_contained(mini_repo, tmp_path):
    """HTML report should be self-contained (no external CSS/JS dependencies)."""
    os.chdir(mini_repo)
    runner = CliRunner()
    output_dir = tmp_path / "test_output"
    result = runner.invoke(cli, ["report", "translation", "--output", str(output_dir)])
    assert result.exit_code == 0

    html = (output_dir / "md_translation_overview.html").read_text()
    # Should have inline styles
    assert "<style>" in html
    # Should NOT reference external stylesheets
    assert 'rel="stylesheet"' not in html
    assert "<script src=" not in html


def test_cli_report_translation_default_output(mini_repo):
    os.chdir(mini_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "translation"])
    assert result.exit_code == 0, result.output

    html_file = mini_repo / "docs" / "reports" / "md_translation_overview.html"
    assert html_file.exists()


def test_cli_report_all(mini_repo, tmp_path):
    os.chdir(mini_repo)
    runner = CliRunner()
    output_dir = tmp_path / "all_output"
    result = runner.invoke(cli, ["report", "--all", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    # Both reports should have been generated
    assert (output_dir / "md_translation_overview.html").exists()
    assert (output_dir / "image_translation_overview.html").exists()


def test_cli_report_all_json(mini_repo):
    os.chdir(mini_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "--all", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    # Merged JSON has top-level keys for each report
    assert "translation" in data
    assert "images" in data
    assert "summary" in data["translation"]
    assert "summary" in data["images"]


def test_cli_report_translation_json_structure(mini_repo):
    """Verify the JSON output has the expected structure for per-content-type, per-language data."""
    os.chdir(mini_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "translation", "--json"])
    assert result.exit_code == 0

    data = json.loads(result.output)

    # Check type_stats has per-type coverage percentages
    assert "course" in data["type_stats"]
    cs = data["type_stats"]["course"]
    assert "coverage_pct" in cs
    assert "items" in cs
    assert "translations" in cs

    # Check lang_stats has per-language coverage
    assert "en" in data["lang_stats"]
    assert "coverage_pct" in data["lang_stats"]["en"]

    # Check items grouping
    assert "course" in data["items"]
    courses = data["items"]["course"]
    assert len(courses) == 2
    btc101 = next(c for c in courses if c["id"] == "btc101")
    assert "en" in btc101["languages"]
    assert btc101["languages"]["en"] > 0  # word count


def test_cli_report_translation_html_word_counts(mini_repo, tmp_path):
    """HTML report should show word counts."""
    os.chdir(mini_repo)
    runner = CliRunner()
    output_dir = tmp_path / "wc_output"
    result = runner.invoke(cli, ["report", "translation", "--output", str(output_dir)])
    assert result.exit_code == 0

    html = (output_dir / "md_translation_overview.html").read_text()
    # Word count notation
    assert "w</span>" in html


def test_cli_report_exit_code_zero(mini_repo):
    os.chdir(mini_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "translation"])
    assert result.exit_code == 0


# ---- Unit tests: image report --------------------------------------------------

@pytest.fixture
def image_repo(tmp_path):
    """Create a repo with markdown files containing image references."""
    (tmp_path / "content-types.yml").write_text(
        "content_types:\n"
        "  course:\n"
        "    name: Course\n"
        "    path_pattern: 'courses/{id}/'\n"
        "    metadata_file: course.yml\n"
        "    schema: schemas/course-scheme.json\n"
        "    has_markdown_content: true\n"
        "    has_quizzes: true\n"
        "    example: courses/btc101\n"
        "  tutorial:\n"
        "    name: Tutorial\n"
        "    path_pattern: 'tutorials/{category}/{id}/'\n"
        "    metadata_file: tutorial.yml\n"
        "    schema: schemas/tutorial-scheme.json\n"
        "    has_markdown_content: true\n"
        "    example: tutorials/wallet/sparrow\n"
        "  event:\n"
        "    name: Event\n"
        "    path_pattern: 'events/{id}/'\n"
        "    metadata_file: event.yml\n"
        "    schema: schemas/event-scheme.json\n"
        "    has_markdown_content: false\n"
        "    example: events/conf-2025\n"
        "languages:\n"
        "  - en\n"
        "  - fr\n"
        "tutorial_categories:\n"
        "  - wallet\n"
        "tags: []\n"
        "discipline_codes: {}\n"
        "level_range: {}\n"
    )

    # Course with translated and shared images
    c = tmp_path / "courses" / "btc101"
    c.mkdir(parents=True)
    (c / "course.yml").write_text("id: abc\n")
    (c / "en.md").write_text(
        "# BTC101\n\n"
        "![img1](assets/en/step1.webp)\n"
        "![img2](assets/en/step2.webp)\n"
        "![shared](assets/no-txt/logo.webp)\n"
    )
    (c / "fr.md").write_text(
        "# BTC101\n\n"
        "![img1](assets/fr/step1.webp)\n"
        "![img2](assets/no-txt/step2.webp)\n"
        "![shared](assets/no-txt/logo.webp)\n"
    )

    # Tutorial with no images
    t = tmp_path / "tutorials" / "wallet" / "sparrow"
    t.mkdir(parents=True)
    (t / "tutorial.yml").write_text("id: def\n")
    (t / "en.md").write_text("# Sparrow\n\nNo images here.")

    return tmp_path


def test_extract_images_from_markdown(tmp_path):
    md = tmp_path / "test.md"
    md.write_text(
        "# Hello\n\n"
        "![a](assets/en/01.webp)\n"
        "![b](https://example.com/img.png)\n"
        "![c](assets/no-txt/logo.webp)\n"
    )
    images = _extract_images_from_markdown(md)
    # Only local paths, not URLs
    assert len(images) == 2
    assert "assets/en/01.webp" in images
    assert "assets/no-txt/logo.webp" in images


def test_extract_images_nonexistent(tmp_path):
    images = _extract_images_from_markdown(tmp_path / "nope.md")
    assert images == []


def test_classify_image_translated():
    assert _classify_image("assets/fr/step1.webp", "fr") == "translated"
    assert _classify_image("assets/en/step1.webp", "en") == "translated"


def test_classify_image_shared():
    assert _classify_image("assets/no-txt/logo.webp", "fr") == "shared"
    assert _classify_image("assets/01/step1.webp", "fr") == "shared"


def test_analyze_image_translation_structure(image_repo):
    os.chdir(image_repo)
    registry = load_registry(image_repo)
    analysis = analyze_image_translation(image_repo, registry)

    assert "by_type" in analysis
    assert "type_stats" in analysis
    assert "languages" in analysis
    assert "summary" in analysis


def test_analyze_image_translation_course(image_repo):
    os.chdir(image_repo)
    registry = load_registry(image_repo)
    analysis = analyze_image_translation(image_repo, registry)

    courses = analysis["by_type"].get("course", [])
    assert len(courses) == 1
    btc101 = courses[0]
    assert btc101["id"] == "btc101"

    # en: 2 translated (assets/en/), 1 shared (assets/no-txt/)
    en = btc101["languages"]["en"]
    assert en["total_images"] == 3
    assert en["translated_images"] == 2
    assert en["shared_images"] == 1

    # fr: 1 translated (assets/fr/), 2 shared
    fr = btc101["languages"]["fr"]
    assert fr["total_images"] == 3
    assert fr["translated_images"] == 1
    assert fr["shared_images"] == 2


def test_analyze_image_translation_no_images(image_repo):
    """Tutorial without images should still appear but with 0 counts."""
    os.chdir(image_repo)
    registry = load_registry(image_repo)
    analysis = analyze_image_translation(image_repo, registry)

    tutorials = analysis["by_type"].get("tutorial", [])
    assert len(tutorials) == 1
    sparrow = tutorials[0]
    en = sparrow["languages"]["en"]
    assert en["total_images"] == 0


def test_analyze_image_excludes_non_image_types(image_repo):
    """Events should not appear in image analysis."""
    (image_repo / "events" / "conf-2025").mkdir(parents=True)
    (image_repo / "events" / "conf-2025" / "event.yml").write_text("id: x\n")
    os.chdir(image_repo)
    registry = load_registry(image_repo)
    analysis = analyze_image_translation(image_repo, registry)

    assert "event" not in analysis["by_type"]


def test_cli_report_images_json(image_repo):
    os.chdir(image_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "images", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "summary" in data
    assert "type_stats" in data
    assert "languages" in data
    assert "items" in data


def test_cli_report_images_html(image_repo, tmp_path):
    os.chdir(image_repo)
    runner = CliRunner()
    output_dir = tmp_path / "img_output"
    result = runner.invoke(cli, ["report", "images", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    html_file = output_dir / "image_translation_overview.html"
    assert html_file.exists()

    html = html_file.read_text()
    assert "<!DOCTYPE html>" in html
    assert "Image Translation Overview" in html
    assert "btc101" in html


def test_cli_report_images_html_self_contained(image_repo, tmp_path):
    os.chdir(image_repo)
    runner = CliRunner()
    output_dir = tmp_path / "img_sc"
    result = runner.invoke(cli, ["report", "images", "--output", str(output_dir)])
    assert result.exit_code == 0

    html = (output_dir / "image_translation_overview.html").read_text()
    assert "<style>" in html
    assert 'rel="stylesheet"' not in html


def test_cli_report_images_default_output(image_repo):
    os.chdir(image_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "images"])
    assert result.exit_code == 0

    assert (image_repo / "docs" / "reports" / "image_translation_overview.html").exists()


def test_cli_report_images_json_structure(image_repo):
    """Verify per-content-type image translation stats in JSON."""
    os.chdir(image_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "images", "--json"])
    assert result.exit_code == 0

    data = json.loads(result.output)
    assert "course" in data["type_stats"]
    cs = data["type_stats"]["course"]
    assert "total_images" in cs
    assert "translated_images" in cs
    assert "percentage" in cs

    # Items should have per-language breakdown
    assert "course" in data["items"]
    courses = data["items"]["course"]
    btc101 = next(c for c in courses if c["id"] == "btc101")
    assert "en" in btc101["languages"]
    assert "total" in btc101["languages"]["en"]
    assert "translated" in btc101["languages"]["en"]


# ---- Unit tests: video deployment (Phase 11) -----------------------------------

def test_parse_video_coverage_basic():
    videos = [
        {"id": "v1", "youtube": [{"fr": "abc"}], "peertube": [{"en": "xyz"}]},
        {"id": "v2", "youtube": [{"fr": "def"}, {"en": "ghi"}]},
    ]
    cov = _parse_video_coverage(videos, ["en", "fr", "es"])
    # v1: fr has youtube only -> youtube+=1; en has peertube only -> peertube+=1
    # v2: fr has youtube only -> youtube+=1; en has youtube only -> youtube+=1
    assert cov["fr"]["youtube"] == 2
    assert cov["fr"]["both"] == 0
    assert cov["fr"]["covered"] == 2
    assert cov["en"]["youtube"] == 1
    assert cov["en"]["peertube"] == 1
    assert cov["en"]["covered"] == 2
    assert cov["es"]["covered"] == 0


def test_parse_video_coverage_both():
    videos = [
        {"id": "v1", "youtube": [{"en": "a"}], "peertube": [{"en": "b"}]},
    ]
    cov = _parse_video_coverage(videos, ["en"])
    assert cov["en"]["both"] == 1
    assert cov["en"]["youtube"] == 0
    assert cov["en"]["peertube"] == 0
    assert cov["en"]["covered"] == 1


def test_parse_video_coverage_empty():
    cov = _parse_video_coverage([], ["en", "fr"])
    assert cov["en"]["covered"] == 0
    assert cov["fr"]["covered"] == 0


@pytest.fixture
def video_repo(tmp_path):
    """Create a repo with courses that have video metadata."""
    (tmp_path / "content-types.yml").write_text(
        "content_types:\n"
        "  course:\n"
        "    name: Course\n"
        "    path_pattern: 'courses/{id}/'\n"
        "    metadata_file: course.yml\n"
        "    schema: schemas/course-scheme.json\n"
        "    has_markdown_content: true\n"
        "    has_quizzes: true\n"
        "    example: courses/btc101\n"
        "languages:\n"
        "  - en\n"
        "  - fr\n"
        "tutorial_categories: []\n"
        "tags: []\n"
        "discipline_codes: {}\n"
        "level_range: {}\n"
    )

    c1 = tmp_path / "courses" / "btc101"
    c1.mkdir(parents=True)
    (c1 / "course.yml").write_text(
        "id: abc\n"
        "level: beginner\n"
        "videos:\n"
        "  - id: v1\n"
        "    youtube:\n"
        "      - fr: PdiL6_1wbQY\n"
        "  - id: v2\n"
        "    youtube:\n"
        "      - fr: ljHLhTzrLsw\n"
        "    peertube:\n"
        "      - en: xyz123\n"
    )

    c2 = tmp_path / "courses" / "btc202"
    c2.mkdir(parents=True)
    (c2 / "course.yml").write_text(
        "id: def\n"
        "level: intermediate\n"
    )

    return tmp_path


def test_analyze_video_deployment(video_repo):
    os.chdir(video_repo)
    registry = load_registry(video_repo)
    analysis = analyze_video_deployment(video_repo, registry)

    assert len(analysis["courses"]) == 2
    assert analysis["summary"]["total_videos"] == 2
    assert analysis["summary"]["courses_with_videos"] == 1

    btc101 = next(c for c in analysis["courses"] if c["id"] == "btc101")
    assert btc101["total_videos"] == 2
    assert btc101["coverage"]["fr"]["covered"] == 2
    assert btc101["coverage"]["en"]["covered"] == 1

    btc202 = next(c for c in analysis["courses"] if c["id"] == "btc202")
    assert btc202["total_videos"] == 0


def test_cli_report_video_json(video_repo):
    os.chdir(video_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "video", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "summary" in data
    assert "courses" in data
    assert data["summary"]["total_courses"] == 2


def test_cli_report_video_html(video_repo, tmp_path):
    os.chdir(video_repo)
    runner = CliRunner()
    output_dir = tmp_path / "vid_output"
    result = runner.invoke(cli, ["report", "video", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    html_file = output_dir / "video_deployment_overview.html"
    assert html_file.exists()
    html = html_file.read_text()
    assert "<!DOCTYPE html>" in html
    assert "Video Deployment Overview" in html
    assert "btc101" in html
    assert "<style>" in html
    assert 'rel="stylesheet"' not in html


def test_cli_report_video_json_structure(video_repo):
    os.chdir(video_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "video", "--json"])
    assert result.exit_code == 0

    data = json.loads(result.output)
    assert "languages" in data
    btc101 = next(c for c in data["courses"] if c["id"] == "btc101")
    assert "coverage" in btc101
    assert "fr" in btc101["coverage"]
    assert "percentage" in btc101["coverage"]["fr"]


# ---- Unit tests: proofreading dashboard (Phase 12) -----------------------------

@pytest.fixture
def proof_repo(tmp_path):
    """Create a repo with proofreading metadata."""
    (tmp_path / "content-types.yml").write_text(
        "content_types:\n"
        "  course:\n"
        "    name: Course\n"
        "    path_pattern: 'courses/{id}/'\n"
        "    metadata_file: course.yml\n"
        "    schema: schemas/course-scheme.json\n"
        "    has_markdown_content: true\n"
        "    has_quizzes: true\n"
        "    example: courses/btc101\n"
        "  tutorial:\n"
        "    name: Tutorial\n"
        "    path_pattern: 'tutorials/{category}/{id}/'\n"
        "    metadata_file: tutorial.yml\n"
        "    schema: schemas/tutorial-scheme.json\n"
        "    has_markdown_content: true\n"
        "    example: tutorials/wallet/sparrow\n"
        "languages:\n"
        "  - en\n"
        "  - fr\n"
        "  - es\n"
        "tutorial_categories:\n"
        "  - wallet\n"
        "tags: []\n"
        "discipline_codes: {}\n"
        "level_range: {}\n"
    )

    c1 = tmp_path / "courses" / "btc101"
    c1.mkdir(parents=True)
    (c1 / "course.yml").write_text(
        "id: abc\n"
        "level: beginner\n"
        "proofreading:\n"
        "  - language: en\n"
        "    last_contribution_date: '2025-01-01'\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "      - alice\n"
        "      - bob\n"
        "    reward: 9.8\n"
        "  - language: fr\n"
        "    last_contribution_date: '2025-02-01'\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "      - charlie\n"
        "    reward: 14.68\n"
    )

    t1 = tmp_path / "tutorials" / "wallet" / "sparrow"
    t1.mkdir(parents=True)
    (t1 / "tutorial.yml").write_text(
        "id: def\n"
        "level: beginner\n"
        "proofreading:\n"
        "  - language: en\n"
        "    last_contribution_date: '2025-03-01'\n"
        "    urgency: 1\n"
        "    contributor_names:\n"
        "      - alice\n"
        "    reward: 5.0\n"
    )

    return tmp_path


def test_analyze_proofreading_structure(proof_repo):
    os.chdir(proof_repo)
    registry = load_registry(proof_repo)
    analysis = analyze_proofreading(proof_repo, registry)

    assert "by_type" in analysis
    assert "languages" in analysis
    assert "lang_stats" in analysis
    assert "leaderboard" in analysis
    assert "summary" in analysis


def test_analyze_proofreading_items(proof_repo):
    os.chdir(proof_repo)
    registry = load_registry(proof_repo)
    analysis = analyze_proofreading(proof_repo, registry)

    assert "course" in analysis["by_type"]
    assert "tutorial" in analysis["by_type"]

    courses = analysis["by_type"]["course"]
    assert len(courses) == 1
    btc101 = courses[0]
    assert btc101["id"] == "btc101"
    assert btc101["languages"]["en"]["status"] == 2  # 2 contributors
    assert btc101["languages"]["fr"]["status"] == 1  # 1 contributor


def test_analyze_proofreading_leaderboard(proof_repo):
    os.chdir(proof_repo)
    registry = load_registry(proof_repo)
    analysis = analyze_proofreading(proof_repo, registry)

    leaderboard = analysis["leaderboard"]
    # alice appears in both course (en) and tutorial (en) -> count 2
    alice = next(e for e in leaderboard if e["name"] == "alice")
    assert alice["count"] == 2


def test_analyze_proofreading_lang_stats(proof_repo):
    os.chdir(proof_repo)
    registry = load_registry(proof_repo)
    analysis = analyze_proofreading(proof_repo, registry)

    ls = analysis["lang_stats"]
    assert "en" in ls
    assert ls["en"]["proofread"] == 2  # btc101 (2 contribs) + sparrow (1 contrib)
    assert ls["en"]["complete"] == 1  # btc101 has 2+ contributors
    assert "fr" in ls
    assert ls["fr"]["proofread"] == 1


def test_cli_report_proofreading_json(proof_repo):
    os.chdir(proof_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "proofreading", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "summary" in data
    assert "leaderboard" in data
    assert "items" in data
    assert data["summary"]["total_items"] == 2
    assert data["summary"]["total_contributors"] == 3


def test_cli_report_proofreading_html(proof_repo, tmp_path):
    os.chdir(proof_repo)
    runner = CliRunner()
    output_dir = tmp_path / "proof_output"
    result = runner.invoke(cli, ["report", "proofreading", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    html_file = output_dir / "proofreading_dashboard.html"
    assert html_file.exists()
    html = html_file.read_text()
    assert "<!DOCTYPE html>" in html
    assert "Proofreading Dashboard" in html
    assert "btc101" in html
    assert "alice" in html
    assert "<style>" in html
    assert 'rel="stylesheet"' not in html


def test_cli_report_proofreading_json_structure(proof_repo):
    os.chdir(proof_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "proofreading", "--json"])
    assert result.exit_code == 0

    data = json.loads(result.output)
    assert "lang_stats" in data
    assert "en" in data["lang_stats"]
    assert "course" in data["items"]
    btc101 = data["items"]["course"][0]
    assert "languages" in btc101
    assert btc101["languages"]["en"]["status"] == 2


# ---- Unit tests: course analytics (Phase 13) -----------------------------------

@pytest.fixture
def analytics_repo(tmp_path):
    """Create a repo with course markdown for analytics."""
    (tmp_path / "content-types.yml").write_text(
        "content_types:\n"
        "  course:\n"
        "    name: Course\n"
        "    path_pattern: 'courses/{id}/'\n"
        "    metadata_file: course.yml\n"
        "    schema: schemas/course-scheme.json\n"
        "    has_markdown_content: true\n"
        "    has_quizzes: true\n"
        "    example: courses/btc101\n"
        "languages:\n"
        "  - en\n"
        "  - fr\n"
        "tutorial_categories: []\n"
        "tags: []\n"
        "discipline_codes: {}\n"
        "level_range: {}\n"
    )

    c1 = tmp_path / "courses" / "btc101"
    c1.mkdir(parents=True)
    (c1 / "course.yml").write_text("id: abc\n")
    (c1 / "en.md").write_text(
        "---\n"
        "name: Bitcoin 101\n"
        "goal: Learn Bitcoin\n"
        "objectives:\n"
        "  - Understand Bitcoin\n"
        "---\n"
        "This is the intro section with some words here.\n\n"
        "+++\n\n"
        "# Part One\n\n"
        "<partId>abc-def-ghi</partId>\n\n"
        "## Chapter One\n\n"
        "<chapterId>111-222-333</chapterId>\n\n"
        "This is chapter one content with enough words to count properly.\n"
        "Another sentence in chapter one.\n\n"
        "## Chapter Two\n\n"
        "<chapterId>444-555-666</chapterId>\n\n"
        "Chapter two has different content.\n\n"
        "+++\n\n"
        "# Part Two\n\n"
        "<partId>jkl-mno-pqr</partId>\n\n"
        "## Chapter Three\n\n"
        "<chapterId>777-888-999</chapterId>\n\n"
        "The third chapter is here with some content.\n"
    )
    (c1 / "fr.md").write_text("---\nname: Bitcoin 101 FR\n---\nContenu.\n")

    # Add quizzes
    q1 = c1 / "quizz" / "001"
    q1.mkdir(parents=True)
    (q1 / "question.yml").write_text("chapterId: 111-222-333\n")
    q2 = c1 / "quizz" / "002"
    q2.mkdir(parents=True)
    (q2 / "question.yml").write_text("chapterId: 444-555-666\n")

    return tmp_path


def test_analyze_course_analytics_structure(analytics_repo):
    analysis = analyze_course_analytics(analytics_repo)

    assert "courses" in analysis
    assert "summary" in analysis
    assert "aggregated" in analysis


def test_analyze_course_analytics_btc101(analytics_repo):
    analysis = analyze_course_analytics(analytics_repo)

    assert len(analysis["courses"]) == 1
    c = analysis["courses"][0]
    assert c["id"] == "btc101"
    assert c["language"] == "en"
    assert c["parts"] == 2
    assert c["chapters"] == 3
    assert c["quizzes"] == 2
    assert c["total_words"] > 0
    assert len(c["words_per_chapter"]) == 3
    assert len(c["chapters_per_part"]) == 2
    assert c["chapters_per_part"] == [2, 1]
    assert "en" in c["languages"]
    assert "fr" in c["languages"]


def test_analyze_course_analytics_summary(analytics_repo):
    analysis = analyze_course_analytics(analytics_repo)

    s = analysis["summary"]
    assert s["total_courses"] == 1
    assert s["total_parts"] == 2
    assert s["total_chapters"] == 3
    assert s["total_quizzes"] == 2
    assert s["total_words"] > 0


def test_analyze_course_analytics_aggregated(analytics_repo):
    analysis = analyze_course_analytics(analytics_repo)

    agg = analysis["aggregated"]
    assert "words_per_course" in agg
    assert "chapters_per_course" in agg
    assert agg["chapters_per_course"]["count"] == 1
    assert agg["chapters_per_course"]["sum"] == 3


def test_analyze_course_analytics_parts_detail(analytics_repo):
    analysis = analyze_course_analytics(analytics_repo)

    c = analysis["courses"][0]
    assert len(c["parts_detail"]) == 2
    assert c["parts_detail"][0]["name"] == "Part One"
    assert c["parts_detail"][0]["chapters"] == 2
    assert c["parts_detail"][1]["name"] == "Part Two"
    assert c["parts_detail"][1]["chapters"] == 1


def test_cli_report_analytics_json(analytics_repo):
    os.chdir(analytics_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "analytics", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "summary" in data
    assert "courses" in data
    assert "aggregated" in data
    assert data["summary"]["total_courses"] == 1
    assert data["summary"]["total_chapters"] == 3


def test_cli_report_analytics_html(analytics_repo, tmp_path):
    os.chdir(analytics_repo)
    runner = CliRunner()
    output_dir = tmp_path / "analytics_output"
    result = runner.invoke(cli, ["report", "analytics", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    html_file = output_dir / "course_analytics_report.html"
    assert html_file.exists()
    html = html_file.read_text()
    assert "<!DOCTYPE html>" in html
    assert "Course Analytics Report" in html
    assert "btc101" in html
    assert "<style>" in html
    assert 'rel="stylesheet"' not in html


def test_cli_report_analytics_json_structure(analytics_repo):
    os.chdir(analytics_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "analytics", "--json"])
    assert result.exit_code == 0

    data = json.loads(result.output)
    c = data["courses"][0]
    assert "words_per_chapter" in c
    assert "parts_detail" in c
    assert c["parts_detail"][0]["name"] == "Part One"


# ---- CLI integration: report --all includes all 5 reports ----------------------

def test_cli_report_all_five_reports(mini_repo, tmp_path):
    """report --all generates all 5 HTML report files."""
    # Add video and proofreading data to mini_repo
    btc101 = mini_repo / "courses" / "btc101"
    (btc101 / "course.yml").write_text(
        "id: abc\n"
        "level: beginner\n"
        "videos:\n"
        "  - id: v1\n"
        "    youtube:\n"
        "      - en: abc123\n"
        "proofreading:\n"
        "  - language: en\n"
        "    contributor_names:\n"
        "      - alice\n"
        "    reward: 5.0\n"
    )

    os.chdir(mini_repo)
    runner = CliRunner()
    output_dir = tmp_path / "all5"
    result = runner.invoke(cli, ["report", "--all", "--output", str(output_dir)])
    assert result.exit_code == 0, result.output

    assert (output_dir / "md_translation_overview.html").exists()
    assert (output_dir / "image_translation_overview.html").exists()
    assert (output_dir / "video_deployment_overview.html").exists()
    assert (output_dir / "proofreading_dashboard.html").exists()
    assert (output_dir / "course_analytics_report.html").exists()


def test_cli_report_all_json_five_keys(mini_repo):
    """report --all --json includes all 5 report sections."""
    btc101 = mini_repo / "courses" / "btc101"
    (btc101 / "course.yml").write_text(
        "id: abc\nlevel: beginner\n"
        "videos:\n  - id: v1\n    youtube:\n      - en: abc123\n"
        "proofreading:\n  - language: en\n    contributor_names: [alice]\n    reward: 5.0\n"
    )

    os.chdir(mini_repo)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "--all", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "translation" in data
    assert "images" in data
    assert "video" in data
    assert "proofreading" in data
    assert "analytics" in data


# ---- Real repo tests (skipped if not in repo) ----------------------------------

@pytest.fixture
def real_repo_root():
    """Return the real repo root, or skip if not available."""
    root = Path(__file__).resolve().parent.parent.parent.parent
    if not (root / "content-types.yml").is_file():
        pytest.skip("Not in the real repo")
    return root


def test_real_repo_translation_coverage(real_repo_root):
    """Spot-check: translation analysis runs on the real repo without errors."""
    os.chdir(real_repo_root)
    registry = load_registry(real_repo_root)
    analysis = analyze_translation_coverage(real_repo_root, registry)

    # Should find many items
    assert analysis["summary"]["total_items"] > 100
    assert analysis["summary"]["total_translations"] > 200
    assert len(analysis["languages"]) > 10

    # Courses should be present
    assert "course" in analysis["by_type"]
    assert len(analysis["by_type"]["course"]) > 20


def test_real_repo_report_json(real_repo_root):
    """Run the CLI on the real repo with --json."""
    os.chdir(real_repo_root)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "translation", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert data["summary"]["total_items"] > 100


def test_real_repo_image_analysis(real_repo_root):
    """Spot-check: image analysis runs on the real repo without errors."""
    os.chdir(real_repo_root)
    registry = load_registry(real_repo_root)
    analysis = analyze_image_translation(real_repo_root, registry)

    assert analysis["summary"]["content_items"] > 0
    assert analysis["summary"]["total_images"] > 0
    assert "course" in analysis["by_type"]


def test_real_repo_image_report_json(real_repo_root):
    """Run image report CLI on the real repo with --json."""
    os.chdir(real_repo_root)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "images", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert data["summary"]["content_items"] > 0
    assert "course" in data["type_stats"]


def test_real_repo_video_analysis(real_repo_root):
    """Spot-check: video analysis runs on the real repo without errors."""
    os.chdir(real_repo_root)
    registry = load_registry(real_repo_root)
    analysis = analyze_video_deployment(real_repo_root, registry)

    assert analysis["summary"]["total_courses"] > 20
    assert analysis["summary"]["courses_with_videos"] > 10
    assert analysis["summary"]["total_videos"] > 100


def test_real_repo_video_report_json(real_repo_root):
    """Run video report CLI on the real repo with --json."""
    os.chdir(real_repo_root)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "video", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert data["summary"]["total_courses"] > 20


def test_real_repo_proofreading_analysis(real_repo_root):
    """Spot-check: proofreading analysis runs on the real repo without errors."""
    os.chdir(real_repo_root)
    registry = load_registry(real_repo_root)
    analysis = analyze_proofreading(real_repo_root, registry)

    assert analysis["summary"]["total_items"] > 100
    assert analysis["summary"]["total_contributors"] > 20
    assert len(analysis["languages"]) > 10


def test_real_repo_analytics(real_repo_root):
    """Spot-check: course analytics runs on the real repo without errors."""
    analysis = analyze_course_analytics(real_repo_root)

    assert analysis["summary"]["total_courses"] > 20
    assert analysis["summary"]["total_chapters"] > 100
    assert analysis["summary"]["total_words"] > 100000
    assert analysis["summary"]["total_quizzes"] > 100

    # Spot-check btc101
    btc101 = next((c for c in analysis["courses"] if c["id"] == "btc101"), None)
    assert btc101 is not None
    assert btc101["parts"] > 0
    assert btc101["chapters"] > 0
    assert btc101["total_words"] > 1000


def test_real_repo_report_all_json(real_repo_root):
    """Run report --all --json on the real repo."""
    os.chdir(real_repo_root)
    runner = CliRunner()
    result = runner.invoke(cli, ["report", "--all", "--json"])
    assert result.exit_code == 0, result.output

    data = json.loads(result.output)
    assert "translation" in data
    assert "images" in data
    assert "video" in data
    assert "proofreading" in data
    assert "analytics" in data
    assert data["translation"]["summary"]["total_items"] > 100
