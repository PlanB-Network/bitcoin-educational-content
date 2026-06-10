"""Tests for bec new tutorial/professor/event/resource commands (Phase 5)."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner

from bec.cli import cli
from bec.commands.new import (
    RESOURCE_TYPE_KEYS,
    _PLACEHOLDER_WEBP,
    _validate_slug,
    build_event_yml,
    build_professor_lang_yml,
    build_professor_yml,
    build_tutorial_md,
    build_tutorial_yml,
    prompt_enum,
)

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
PROF_UUID = "2e1b5182-567e-453a-af29-36009340ff02"


# ---- Slug validation ----


class TestValidateSlug:
    def test_valid_slugs(self):
        assert _validate_slug("my-tutorial") is None
        assert _validate_slug("sparrow") is None
        assert _validate_slug("btc-101") is None
        assert _validate_slug("test-event-2025") is None

    def test_invalid_slugs(self):
        assert _validate_slug("a") is not None  # too short
        assert _validate_slug("My-Tutorial") is not None  # uppercase
        assert _validate_slug("-leading") is not None  # leading hyphen


# ---- prompt_enum ----


class TestPromptEnum:
    def test_case_insensitive_returns_canonical(self):
        from unittest.mock import patch

        with patch("click.prompt", return_value="cc-by-sa-v4"):
            assert prompt_enum("license", ["CC-BY-SA-V4", "MIT"]) == "CC-BY-SA-V4"
        with patch("click.prompt", return_value="MIT"):
            assert prompt_enum("license", ["CC-BY-SA-V4", "MIT"]) == "MIT"

    def test_invalid_reprompts(self):
        from unittest.mock import patch

        with patch("click.prompt", side_effect=["nope", "mit"]):
            assert prompt_enum("license", ["CC-BY-SA-V4", "MIT"]) == "MIT"


# ---- Placeholder WebP ----


class TestPlaceholderWebp:
    def test_valid_webp_structure(self):
        data = _PLACEHOLDER_WEBP
        assert data[:4] == b"RIFF"
        assert int.from_bytes(data[4:8], "little") == len(data) - 8
        assert data[8:12] == b"WEBP"
        assert data[12:16] == b"VP8L"
        vp8l_size = int.from_bytes(data[16:20], "little")
        assert len(data) == 20 + vp8l_size + (vp8l_size % 2)
        assert data[20] == 0x2F  # VP8L signature byte

    def test_decodable(self):
        import subprocess
        import tempfile

        if shutil.which("dwebp") is None:
            pytest.skip("dwebp not available")
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "ph.webp"
            src.write_bytes(_PLACEHOLDER_WEBP)
            result = subprocess.run(
                ["dwebp", str(src), "-o", str(Path(tmp) / "ph.png")],
                capture_output=True,
            )
            assert result.returncode == 0, result.stderr.decode()


# ---- Tutorial unit tests ----


class TestBuildTutorialYml:
    def test_required_fields(self):
        data = build_tutorial_yml(
            tutorial_uuid="aaaa-bbbb-cccc-dddd",
            level="beginner",
            schema_category="desktop",
            professor_id=PROF_UUID,
            license_type="CC-BY-SA-V4",
            lang="en",
        )
        assert data["id"] == "aaaa-bbbb-cccc-dddd"
        assert data["level"] == "beginner"
        assert data["category"] == "desktop"
        assert data["professor_id"] == PROF_UUID
        assert data["license"] == "CC-BY-SA-V4"
        assert data["original_language"] == "en"
        assert len(data["proofreading"]) == 1
        assert data["proofreading"][0]["language"] == "en"

    def test_tags_default(self):
        data = build_tutorial_yml("x", "beginner", "desktop", PROF_UUID, "CC-BY-SA-V4", "en")
        assert data["tags"] == ["software"]


class TestBuildTutorialMd:
    def test_has_frontmatter(self):
        md = build_tutorial_md("my-tuto")
        assert md.startswith("---\n")
        assert "\n---\n" in md

    def test_has_cover(self):
        md = build_tutorial_md("my-tuto")
        assert "![cover](assets/cover.webp)" in md

    def test_has_required_frontmatter_fields(self):
        md = build_tutorial_md("my-tuto")
        assert "name:" in md
        assert "description:" in md

    def test_references_tutorial_id(self):
        md = build_tutorial_md("my-tuto")
        assert "my-tuto" in md


# ---- Professor unit tests ----


class TestBuildProfessorYml:
    def test_required_fields(self):
        data = build_professor_yml("test-uuid", "Satoshi Nakamoto")
        assert data["id"] == "test-uuid"
        assert data["name"] == "Satoshi Nakamoto"
        assert "links" in data

    def test_has_tags(self):
        data = build_professor_yml("test-uuid", "Test")
        assert "tags" in data


class TestBuildProfessorLangYml:
    def test_required_fields(self):
        data = build_professor_lang_yml()
        assert "bio" in data
        assert "short_bio" in data


# ---- Event unit tests ----


class TestBuildEventYml:
    def test_required_fields(self):
        data = build_event_yml(
            event_uuid="test-uuid",
            name="Bitcoin Paris 2025",
            event_type="meetup",
            start_date="2025-06-15 09:00:00",
            end_date="2025-06-15 17:00:00",
            timezone="Europe/Paris",
            city="Paris, France",
            lang="en",
        )
        assert data["id"] == "test-uuid"
        assert data["name"] == "Bitcoin Paris 2025"
        assert data["type"] == "meetup"
        assert data["start_date"] == "2025-06-15 09:00:00"
        assert data["end_date"] == "2025-06-15 17:00:00"
        assert data["timezone"] == "Europe/Paris"
        assert data["address_city_country"] == "Paris, France"
        assert data["language"] == ["en"]
        assert "links" in data
        assert "tags" in data


# ---- CLI integration tests: Tutorial ----


class TestNewTutorialCommand:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def clean_tutorial(self, repo_root):
        tuto_dir = repo_root / "tutorials" / "wallet" / "test-tuto"
        yield tuto_dir
        if tuto_dir.exists():
            shutil.rmtree(tuto_dir)

    def test_non_interactive_creates_files(self, runner, clean_tutorial):
        result = runner.invoke(cli, [
            "new", "tutorial",
            "--category", "wallet",
            "--id", "test-tuto",
            "--lang", "en",
            "--level", "beginner",
            "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4",
            "--tool-type", "desktop",
        ])
        assert result.exit_code == 0, result.output
        assert clean_tutorial.exists()
        assert (clean_tutorial / "tutorial.yml").exists()
        assert (clean_tutorial / "en.md").exists()
        assert (clean_tutorial / "assets").is_dir()
        assert (clean_tutorial / "assets" / "cover.webp").exists()

    def test_tutorial_yml_valid(self, runner, clean_tutorial):
        runner.invoke(cli, [
            "new", "tutorial",
            "--category", "wallet", "--id", "test-tuto", "--lang", "en",
            "--level", "intermediate", "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4", "--tool-type", "hardware",
        ])
        with open(clean_tutorial / "tutorial.yml") as f:
            data = yaml.safe_load(f)
        assert UUID_RE.match(data["id"])
        assert data["level"] == "intermediate"
        assert data["category"] == "hardware"
        assert data["professor_id"] == PROF_UUID
        assert data["license"] == "CC-BY-SA-V4"
        assert data["original_language"] == "en"

    def test_tutorial_md_structure(self, runner, clean_tutorial):
        runner.invoke(cli, [
            "new", "tutorial",
            "--category", "wallet", "--id", "test-tuto", "--lang", "en",
            "--level", "beginner", "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4", "--tool-type", "desktop",
        ])
        md = (clean_tutorial / "en.md").read_text()
        assert md.startswith("---\n")
        assert "name:" in md
        assert "description:" in md
        assert "![cover](assets/cover.webp)" in md

    def test_json_output(self, runner, clean_tutorial):
        result = runner.invoke(cli, [
            "new", "tutorial",
            "--category", "wallet", "--id", "test-tuto", "--lang", "en",
            "--level", "beginner", "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4", "--tool-type", "desktop",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["type"] == "tutorial"
        assert data["id"] == "test-tuto"
        assert "uuid" in data
        assert "files" in data
        assert data["folder_category"] == "wallet"

    def test_invalid_category_rejected(self, runner):
        result = runner.invoke(cli, [
            "new", "tutorial",
            "--category", "nosuch",
            "--id", "test-tuto", "--lang", "en",
            "--level", "beginner", "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4", "--tool-type", "desktop",
        ])
        assert result.exit_code == 1
        assert "invalid tutorial category" in result.output

    def test_duplicate_rejected(self, runner, clean_tutorial):
        args = [
            "new", "tutorial",
            "--category", "wallet", "--id", "test-tuto", "--lang", "en",
            "--level", "beginner", "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4", "--tool-type", "desktop",
        ]
        runner.invoke(cli, args)
        result = runner.invoke(cli, args)
        assert result.exit_code == 1
        assert "already exists" in result.output

    def test_validates_structurally(self, runner, clean_tutorial):
        """Scaffolded tutorial passes bec validate."""
        runner.invoke(cli, [
            "new", "tutorial",
            "--category", "wallet", "--id", "test-tuto", "--lang", "en",
            "--level", "beginner", "--professor-id", PROF_UUID,
            "--license", "CC-BY-SA-V4", "--tool-type", "desktop",
        ])
        result = runner.invoke(cli, ["validate", "tutorials/wallet/test-tuto"])
        assert result.exit_code == 0, result.output


# ---- CLI integration tests: Professor ----


class TestNewProfessorCommand:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def clean_professor(self, repo_root):
        prof_dir = repo_root / "professors" / "test-prof"
        yield prof_dir
        if prof_dir.exists():
            shutil.rmtree(prof_dir)

    def test_non_interactive_creates_files(self, runner, clean_professor):
        result = runner.invoke(cli, [
            "new", "professor",
            "--id", "test-prof",
            "--name", "Test Professor",
            "--lang", "en",
        ])
        assert result.exit_code == 0, result.output
        assert clean_professor.exists()
        assert (clean_professor / "professor.yml").exists()
        assert (clean_professor / "en.yml").exists()
        assert (clean_professor / "assets").is_dir()
        assert (clean_professor / "assets" / ".gitkeep").exists()

    def test_professor_yml_valid(self, runner, clean_professor):
        runner.invoke(cli, [
            "new", "professor",
            "--id", "test-prof", "--name", "Satoshi Nakamoto", "--lang", "en",
        ])
        with open(clean_professor / "professor.yml") as f:
            data = yaml.safe_load(f)
        assert UUID_RE.match(data["id"])
        assert data["name"] == "Satoshi Nakamoto"

    def test_lang_yml_structure(self, runner, clean_professor):
        runner.invoke(cli, [
            "new", "professor",
            "--id", "test-prof", "--name", "Test", "--lang", "en",
        ])
        with open(clean_professor / "en.yml") as f:
            data = yaml.safe_load(f)
        assert "bio" in data
        assert "short_bio" in data

    def test_json_output(self, runner, clean_professor):
        result = runner.invoke(cli, [
            "new", "professor",
            "--id", "test-prof", "--name", "Test", "--lang", "en",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["type"] == "professor"
        assert data["id"] == "test-prof"

    def test_duplicate_rejected(self, runner, clean_professor):
        args = ["new", "professor", "--id", "test-prof", "--name", "T", "--lang", "en"]
        runner.invoke(cli, args)
        result = runner.invoke(cli, args)
        assert result.exit_code == 1
        assert "already exists" in result.output

    def test_validates_structurally(self, runner, clean_professor):
        runner.invoke(cli, [
            "new", "professor", "--id", "test-prof", "--name", "Test", "--lang", "en",
        ])
        result = runner.invoke(cli, ["validate", "professors/test-prof"])
        assert result.exit_code == 0, result.output


# ---- CLI integration tests: Event ----


class TestNewEventCommand:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def clean_event(self, repo_root):
        event_dir = repo_root / "events" / "test-event-2025"
        yield event_dir
        if event_dir.exists():
            shutil.rmtree(event_dir)

    def _default_args(self):
        return [
            "new", "event",
            "--id", "test-event-2025",
            "--name", "Test Event 2025",
            "--type", "meetup",
            "--start-date", "2025-06-15 09:00:00",
            "--end-date", "2025-06-15 17:00:00",
            "--timezone", "Europe/Paris",
            "--city", "Paris, France",
            "--lang", "en",
        ]

    def test_non_interactive_creates_files(self, runner, clean_event):
        result = runner.invoke(cli, self._default_args())
        assert result.exit_code == 0, result.output
        assert clean_event.exists()
        assert (clean_event / "event.yml").exists()
        assert (clean_event / "assets").is_dir()
        assert (clean_event / "assets" / ".gitkeep").exists()

    def test_event_yml_valid(self, runner, clean_event):
        runner.invoke(cli, self._default_args())
        with open(clean_event / "event.yml") as f:
            data = yaml.safe_load(f)
        assert UUID_RE.match(data["id"])
        assert data["name"] == "Test Event 2025"
        assert data["type"] == "meetup"
        assert data["timezone"] == "Europe/Paris"
        assert data["address_city_country"] == "Paris, France"
        assert data["language"] == ["en"]

    def test_json_output(self, runner, clean_event):
        result = runner.invoke(cli, self._default_args() + ["--json"])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["type"] == "event"
        assert data["id"] == "test-event-2025"

    def test_schema_enum_type_accepted(self, runner, clean_event):
        """Event types come from the event schema enum."""
        args = self._default_args()
        args[args.index("meetup")] = "lecture"
        result = runner.invoke(cli, args)
        assert result.exit_code == 0, result.output

    def test_invalid_event_type_rejected(self, runner):
        result = runner.invoke(cli, [
            "new", "event",
            "--id", "test-event-2025", "--name", "T", "--type", "party",
            "--start-date", "2025-01-01 09:00:00", "--end-date", "2025-01-01 17:00:00",
            "--timezone", "UTC", "--city", "X", "--lang", "en",
        ])
        assert result.exit_code == 1
        assert "invalid event type" in result.output

    def test_duplicate_rejected(self, runner, clean_event):
        runner.invoke(cli, self._default_args())
        result = runner.invoke(cli, self._default_args())
        assert result.exit_code == 1
        assert "already exists" in result.output

    def test_validates_structurally(self, runner, clean_event):
        """Scaffolded event passes bec validate (exit 0 or 2 for warnings)."""
        runner.invoke(cli, self._default_args())
        result = runner.invoke(cli, ["validate", "events/test-event-2025"])
        assert result.exit_code in (0, 2), result.output


# ---- CLI integration tests: Resource ----


class TestNewResourceCommand:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def clean_book(self, repo_root):
        d = repo_root / "resources" / "books" / "test-book"
        yield d
        if d.exists():
            shutil.rmtree(d)

    @pytest.fixture
    def clean_podcast(self, repo_root):
        d = repo_root / "resources" / "podcasts" / "test-pod"
        yield d
        if d.exists():
            shutil.rmtree(d)

    def test_book_creates_files(self, runner, clean_book):
        result = runner.invoke(cli, [
            "new", "resource", "--type", "book", "--id", "test-book", "--lang", "en",
        ])
        assert result.exit_code == 0, result.output
        assert clean_book.exists()
        assert (clean_book / "book.yml").exists()
        assert (clean_book / "en.yml").exists()
        assert (clean_book / "assets").is_dir()
        assert (clean_book / "assets" / ".gitkeep").exists()

    def test_book_yml_valid(self, runner, clean_book):
        runner.invoke(cli, [
            "new", "resource", "--type", "book", "--id", "test-book", "--lang", "en",
        ])
        with open(clean_book / "book.yml") as f:
            data = yaml.safe_load(f)
        assert data["author"] == "TODO: Author Name"
        assert data["level"] == "beginner"
        assert "tags" in data

    def test_book_content_yml(self, runner, clean_book):
        runner.invoke(cli, [
            "new", "resource", "--type", "book", "--id", "test-book", "--lang", "en",
        ])
        with open(clean_book / "en.yml") as f:
            data = yaml.safe_load(f)
        assert "title" in data
        assert "publication_year" in data
        assert "cover" in data
        assert "original" in data
        assert "description" in data

    def test_podcast_creates_files(self, runner, clean_podcast):
        result = runner.invoke(cli, [
            "new", "resource", "--type", "podcast", "--id", "test-pod", "--lang", "en",
        ])
        assert result.exit_code == 0, result.output
        assert clean_podcast.exists()
        assert (clean_podcast / "podcast.yml").exists()
        # Podcasts have no content schema -> no language file
        assert not (clean_podcast / "en.yml").exists()

    def test_podcast_yml_valid(self, runner, clean_podcast):
        runner.invoke(cli, [
            "new", "resource", "--type", "podcast", "--id", "test-pod", "--lang", "en",
        ])
        with open(clean_podcast / "podcast.yml") as f:
            data = yaml.safe_load(f)
        assert UUID_RE.match(data["id"])
        assert data["name"] == "TODO: Podcast Name"
        assert "host" in data
        assert "links" in data

    def test_invalid_type_rejected(self, runner):
        result = runner.invoke(cli, [
            "new", "resource", "--type", "invalid", "--id", "test", "--lang", "en",
        ])
        assert result.exit_code == 1
        assert "invalid resource type" in result.output

    def test_json_output(self, runner, clean_book):
        result = runner.invoke(cli, [
            "new", "resource", "--type", "book", "--id", "test-book", "--lang", "en",
            "--json",
        ])
        assert result.exit_code == 0, result.output
        data = json.loads(result.output)
        assert data["resource_type"] == "book"
        assert data["id"] == "test-book"
        assert "files" in data

    def test_duplicate_rejected(self, runner, clean_book):
        args = ["new", "resource", "--type", "book", "--id", "test-book", "--lang", "en"]
        runner.invoke(cli, args)
        result = runner.invoke(cli, args)
        assert result.exit_code == 1
        assert "already exists" in result.output

    def test_book_validates(self, runner, clean_book):
        runner.invoke(cli, [
            "new", "resource", "--type", "book", "--id", "test-book", "--lang", "en",
        ])
        result = runner.invoke(cli, ["validate", "resources/books/test-book"])
        assert result.exit_code == 0, result.output

    def test_podcast_validates(self, runner, clean_podcast):
        runner.invoke(cli, [
            "new", "resource", "--type", "podcast", "--id", "test-pod", "--lang", "en",
        ])
        result = runner.invoke(cli, ["validate", "resources/podcasts/test-pod"])
        assert result.exit_code == 0, result.output


# ---- Resource type coverage ----


class TestResourceTypeCoverage:
    """Verify all resource types can be scaffolded."""

    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture(params=sorted(RESOURCE_TYPE_KEYS))
    def resource_type_and_cleanup(self, request, repo_root):
        rtype = request.param
        from bec.commands.new import _resource_dir_prefix
        from bec.lib.content_types import load_registry

        registry = load_registry(repo_root)
        prefix = _resource_dir_prefix(registry, rtype)
        test_id = f"test-{rtype}-scaffold"
        d = repo_root / prefix / test_id
        yield rtype, test_id, d
        if d.exists():
            shutil.rmtree(d)

    def test_scaffold_all_types(self, runner, resource_type_and_cleanup):
        rtype, test_id, expected_dir = resource_type_and_cleanup
        result = runner.invoke(cli, [
            "new", "resource",
            "--type", rtype,
            "--id", test_id,
            "--lang", "en",
            "--json",
        ])
        assert result.exit_code == 0, f"Failed for {rtype}: {result.output}"
        assert expected_dir.exists(), f"Dir not created for {rtype}"

        data = json.loads(result.output)
        assert data["resource_type"] == rtype
        assert data["id"] == test_id
