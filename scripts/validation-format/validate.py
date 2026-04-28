#!/usr/bin/env python3
"""
PlanB Network Content Schema Validator

Validates content folders against JSON schema definitions.
Checks both YAML metadata files and markdown content files.

The validator auto-detects the repository root and uses centralized schemas
from scripts/validation-format/schemas/.

Usage:
    python validate.py <folder_path>
    python validate.py courses/btc101
    python validate.py tutorials/wallet/sparrow-wallet
    python validate.py professors/pbn-author
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Optional

try:
    import jsonschema
    from jsonschema import Draft7Validator, ValidationError as JsonSchemaError
except ImportError:
    print("Error: jsonschema package required. Install with: pip install jsonschema")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("Error: PyYAML package required. Install with: pip install pyyaml")
    sys.exit(1)

try:
    import frontmatter
except ImportError:
    print("Error: python-frontmatter package required. Install with: pip install python-frontmatter")
    sys.exit(1)


# ANSI color codes for terminal output
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


@dataclass
class ValidationResult:
    """Holds validation results for a single file or content check."""
    file_path: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def add_error(self, msg: str):
        self.errors.append(msg)

    def add_warning(self, msg: str):
        self.warnings.append(msg)


@dataclass
class ContentTypeConfig:
    """Configuration for a content type."""
    name: str
    yaml_file: str  # e.g., "tutorial.yml", "professor.yml"
    schema_file: str  # e.g., "tutorial-scheme.json"
    content_schema_file: Optional[str] = None  # e.g., "tutorial-content-scheme.json"
    has_markdown_content: bool = True
    content_uses_frontmatter: bool = True  # True for .md files with YAML frontmatter
    content_uses_yml: bool = False  # True for .yml content files (e.g., books, bet)
    has_quizzes: bool = False  # True for content types with quizz subfolder


# Content type configurations
CONTENT_TYPES: dict[str, ContentTypeConfig] = {
    "tutorials": ContentTypeConfig(
        name="Tutorial",
        yaml_file="tutorial.yml",
        schema_file="tutorial-scheme.json",
        content_schema_file="tutorial-content-scheme.json",
    ),
    "courses": ContentTypeConfig(
        name="Course",
        yaml_file="course.yml",
        schema_file="course-scheme.json",
        content_schema_file="course-content-scheme.json",
        has_quizzes=True,
    ),
    "professors": ContentTypeConfig(
        name="Professor",
        yaml_file="professor.yml",
        schema_file="professor-scheme.json",
        content_schema_file="professor-content-scheme.json",
    ),
    "events": ContentTypeConfig(
        name="Event",
        yaml_file="event.yml",
        schema_file="event-scheme.json",
        has_markdown_content=False,
    ),
    "resources/bet": ContentTypeConfig(
        name="BET",
        yaml_file="bet.yml",
        schema_file="bet-scheme.json",
        content_schema_file="bet-content-scheme.json",
        content_uses_yml=True,
    ),
    "resources/books": ContentTypeConfig(
        name="Book",
        yaml_file="book.yml",
        schema_file="book-scheme.json",
        content_schema_file="book-content-scheme.json",
        content_uses_yml=True,
    ),
    "resources/channels": ContentTypeConfig(
        name="Channel",
        yaml_file="channel.yml",
        schema_file="channel-scheme.json",
        has_markdown_content=False,
    ),
    "resources/conferences": ContentTypeConfig(
        name="Conference",
        yaml_file="conference.yml",
        schema_file="conference-scheme.json",
        has_markdown_content=False,
    ),
    "resources/glossary": ContentTypeConfig(
        name="Glossary Word",
        yaml_file="word.yml",
        schema_file="word-scheme.json",
        content_schema_file="word-content-scheme.json",
    ),
    "resources/movies": ContentTypeConfig(
        name="Movie",
        yaml_file="movie.yml",
        schema_file="movie-scheme.json",
        has_markdown_content=False,
    ),
    "resources/newsletters": ContentTypeConfig(
        name="Newsletter",
        yaml_file="newsletter.yml",
        schema_file="newsletter-scheme.json",
        has_markdown_content=False,
    ),
    "resources/podcasts": ContentTypeConfig(
        name="Podcast",
        yaml_file="podcast.yml",
        schema_file="podcast-scheme.json",
        has_markdown_content=False,
    ),
    "resources/projects": ContentTypeConfig(
        name="Project",
        yaml_file="project.yml",
        schema_file="project-scheme.json",
        content_schema_file="project-content-scheme.json",
        content_uses_yml=True,
    ),
    "resources/papers": ContentTypeConfig(
        name="Paper",
        yaml_file="paper.yml",
        schema_file="paper-scheme.json",
        has_markdown_content=False,
    ),
}


class SchemaValidator:
    """Validates content folders against JSON schemas."""

    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()
        # Schema path is now centralized in scripts/validation-format/schemas/
        self.schema_path = self.base_path / "scripts" / "validation-format" / "schemas"
        self.results: list[ValidationResult] = []

    def _find_repo_root(self, folder_path: Path) -> Path:
        """Find the repository root by looking for .git directory (primary) or known directories (fallback)."""
        current = folder_path
        # First pass: look for .git (most reliable)
        for _ in range(15):  # Max 15 levels up
            if (current / ".git").exists():
                return current
            if current.parent == current:
                break
            current = current.parent

        # Second pass: fallback to known directory structure
        current = folder_path
        for _ in range(15):
            if all((current / d).exists() for d in ["courses", "tutorials", "professors"]):
                # Make sure we're not in a template/docs subfolder
                if "docs" not in current.parts[-3:] and "PBN-template-repo" not in current.parts:
                    return current
            if current.parent == current:
                break
            current = current.parent
        return folder_path

    def detect_content_type(self, folder_path: Path) -> Optional[ContentTypeConfig]:
        """Detect content type from folder path."""
        # First, find the repo root relative to the folder
        repo_root = self._find_repo_root(folder_path)

        try:
            rel_path = str(folder_path.relative_to(repo_root))
        except ValueError:
            # If folder is not relative to found repo root, try using base_path
            try:
                rel_path = str(folder_path.relative_to(self.base_path))
            except ValueError:
                # Last resort: use folder name parts to detect type
                rel_path = str(folder_path)

        # Check for nested content types (tutorials have category subfolder)
        parts = rel_path.split(os.sep)

        # Try matching from most specific to least specific
        for content_path, config in CONTENT_TYPES.items():
            content_parts = content_path.split("/")
            if parts[:len(content_parts)] == content_parts:
                return config

        return None

    def find_schema_file(self, config: ContentTypeConfig) -> Optional[Path]:
        """Find the schema file for the content type from centralized location."""
        schema_file = self.schema_path / config.schema_file
        if schema_file.exists():
            return schema_file
        return None

    def find_content_schema_file(self, config: ContentTypeConfig) -> Optional[Path]:
        """Find the content schema file for the content type from centralized location."""
        if not config.content_schema_file:
            return None

        schema_file = self.schema_path / config.content_schema_file
        if schema_file.exists():
            return schema_file
        return None

    def load_json_schema(self, schema_path: Path) -> dict:
        """Load a JSON schema file."""
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_yaml_file(self, yaml_path: Path) -> dict:
        """Load a YAML file."""
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
        # Convert datetime objects to strings for JSON schema validation
        return self._convert_dates_to_strings(data)

    def _convert_dates_to_strings(self, obj: Any) -> Any:
        """Recursively convert datetime.date and datetime.datetime objects to ISO format strings."""
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, dict):
            return {k: self._convert_dates_to_strings(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_dates_to_strings(item) for item in obj]
        return obj

    def _find_and_remove_null_values(self, obj: Any, path: str = "") -> tuple[Any, list[str]]:
        """
        Recursively find null values and remove them from the data structure.
        Returns the cleaned object and a list of paths where null values were found.
        """
        null_paths = []

        if obj is None:
            return None, [path] if path else []
        elif isinstance(obj, dict):
            cleaned = {}
            for k, v in obj.items():
                current_path = f"{path} -> {k}" if path else k
                if v is None:
                    null_paths.append(current_path)
                    # Don't include null values in cleaned dict
                else:
                    cleaned_v, sub_nulls = self._find_and_remove_null_values(v, current_path)
                    null_paths.extend(sub_nulls)
                    if cleaned_v is not None:
                        cleaned[k] = cleaned_v
            return cleaned, null_paths
        elif isinstance(obj, list):
            cleaned = []
            for i, item in enumerate(obj):
                current_path = f"{path}[{i}]"
                if item is None:
                    null_paths.append(current_path)
                else:
                    cleaned_item, sub_nulls = self._find_and_remove_null_values(item, current_path)
                    null_paths.extend(sub_nulls)
                    if cleaned_item is not None:
                        cleaned.append(cleaned_item)
            return cleaned, null_paths
        return obj, null_paths

    def validate_yaml_against_schema(self, yaml_data: dict, schema: dict, file_path: str) -> ValidationResult:
        """Validate YAML data against a JSON schema."""
        result = ValidationResult(file_path=file_path)

        # Find and remove null values, reporting them as warnings
        cleaned_data, null_paths = self._find_and_remove_null_values(yaml_data)
        for null_path in null_paths:
            result.add_warning(f"[{null_path}] Empty/null value")

        validator = Draft7Validator(schema)
        errors = list(validator.iter_errors(cleaned_data))

        for error in errors:
            path = " -> ".join(str(p) for p in error.absolute_path) if error.absolute_path else "root"
            result.add_error(f"[{path}] {error.message}")

        return result

    def validate_markdown_content(self, md_path: Path, content_schema: dict) -> ValidationResult:
        """Validate markdown content file against content schema."""
        result = ValidationResult(file_path=str(md_path))

        try:
            post = frontmatter.load(md_path)
        except Exception as e:
            result.add_error(f"Failed to parse markdown file: {e}")
            return result

        # Validate frontmatter against schema properties
        schema_props = content_schema.get("properties", {})
        required_fields = content_schema.get("required", [])

        # Check required frontmatter fields
        for field in required_fields:
            if field not in post.metadata:
                result.add_error(f"Missing required frontmatter field: '{field}'")

        # Validate frontmatter field types and constraints
        for field, value in post.metadata.items():
            if field in schema_props:
                field_schema = schema_props[field]
                self._validate_field(result, field, value, field_schema)

        # Validate content rules if present
        content_rules = content_schema.get("content_rules", {})
        if content_rules:
            self._validate_content_rules(result, post.content, content_rules, md_path)

        return result

    def _validate_field(self, result: ValidationResult, field: str, value: Any, schema: dict):
        """Validate a single field against its schema."""
        expected_type = schema.get("type")

        type_mapping = {
            "string": str,
            "integer": int,
            "number": (int, float),
            "boolean": bool,
            "array": list,
            "object": dict,
        }

        if expected_type and expected_type in type_mapping:
            expected = type_mapping[expected_type]
            if not isinstance(value, expected):
                result.add_error(f"Field '{field}' should be {expected_type}, got {type(value).__name__}")

        # Check minLength/maxLength for strings
        if expected_type == "string" and isinstance(value, str):
            min_len = schema.get("minLength")
            max_len = schema.get("maxLength")
            if min_len and len(value) < min_len:
                result.add_error(f"Field '{field}' is too short (min {min_len} chars)")
            if max_len and len(value) > max_len:
                result.add_error(f"Field '{field}' is too long (max {max_len} chars)")

        # Check enum values
        if "enum" in schema and value not in schema["enum"]:
            result.add_error(f"Field '{field}' has invalid value '{value}'. Allowed: {schema['enum']}")

    def _validate_content_rules(self, result: ValidationResult, content: str, rules: dict, md_path: Path):
        """Validate markdown content against content rules."""
        lines = content.split('\n')

        # Check cover image
        cover_rule = rules.get("cover_image", {})
        if cover_rule.get("required", False):
            # Cover must appear within the first 10 lines after frontmatter
            # Pattern: ![any-alt-text](cover.webp) or ![any-alt-text](assets/cover.webp)
            cover_pattern = re.compile(r'!\[.*?\]\((?:assets/)?cover\.webp\)')
            first_10_lines = '\n'.join(lines[:10])
            if not cover_pattern.search(first_10_lines):
                result.add_error("Cover image ![...](cover.webp) or ![...](assets/cover.webp) must appear within the first 10 lines after YAML front-matter")

        # Check headings
        heading_rules = rules.get("headings", {})
        h1_rule = heading_rules.get("h1", {})
        if h1_rule.get("allowed") is False:
            # Remove code blocks before checking for H1 headings
            # Remove fenced code blocks (``` or ~~~)
            content_no_code = re.sub(r'```[\s\S]*?```', '', content)
            content_no_code = re.sub(r'~~~[\s\S]*?~~~', '', content_no_code)
            # Remove indented code blocks (4 spaces or 1 tab at line start)
            content_no_code = re.sub(r'^(?:    |\t).*$', '', content_no_code, flags=re.MULTILINE)

            h1_matches = re.findall(r'^# [^#]', content_no_code, re.MULTILINE)
            if h1_matches:
                result.add_error("H1 headings (# Title) are not allowed - title comes from YAML 'name' field")

        # Check list markers
        list_rules = rules.get("lists", {})
        unordered_rule = list_rules.get("unordered", {})
        if unordered_rule.get("marker") == "-":
            # Check for asterisk list markers
            asterisk_lists = re.findall(r'^\* ', content, re.MULTILINE)
            if asterisk_lists:
                result.add_warning(f"Found {len(asterisk_lists)} asterisk (*) list markers. Use dash (-) instead.")

        # Check images format
        image_rules = rules.get("images", {})
        if image_rules.get("format") == "WebP only (.webp extension)":
            non_webp = re.findall(r'!\[.*?\]\([^)]+\.(png|jpg|jpeg|gif)\)', content, re.IGNORECASE)
            if non_webp:
                result.add_error(f"Non-WebP images found. All images must be .webp format.")

        # Check for alt text on images
        alt_text_rule = image_rules.get("alt_text", {})
        if alt_text_rule.get("required"):
            empty_alt = re.findall(r'!\[\]\(', content)
            if empty_alt:
                result.add_warning(f"Found {len(empty_alt)} images without alt text")

        # Check assets folder exists
        assets_path = md_path.parent / "assets"
        if cover_rule.get("required") and not assets_path.exists():
            result.add_error("Assets folder is missing")

        # Check cover.webp exists
        if cover_rule.get("required") and assets_path.exists():
            cover_path = assets_path / "cover.webp"
            if not cover_path.exists():
                result.add_error("Cover image 'assets/cover.webp' is missing")

    def validate_yml_content(self, yml_path: Path, content_schema: dict) -> ValidationResult:
        """Validate YML content files (used by books, bet, etc.)."""
        result = ValidationResult(file_path=str(yml_path))

        try:
            data = self.load_yaml_file(yml_path)
        except Exception as e:
            result.add_error(f"Failed to parse YAML file: {e}")
            return result

        # Use JSON schema validation
        schema_props = content_schema.get("properties", {})
        required_fields = content_schema.get("required", [])

        for field in required_fields:
            if field not in data:
                result.add_error(f"Missing required field: '{field}'")

        for field, value in data.items():
            if field in schema_props:
                self._validate_field(result, field, value, schema_props[field])

        return result

    def validate_quiz_folder(self, quiz_folder: Path) -> list[ValidationResult]:
        """Validate a single quiz folder (e.g., quizz/000/)."""
        results = []

        # Check for question.yml (required)
        question_file = quiz_folder / "question.yml"
        if not question_file.exists():
            result = ValidationResult(file_path=str(question_file))
            result.add_error("Missing required file: question.yml")
            results.append(result)
            return results

        # Validate question.yml structure
        result = ValidationResult(file_path=str(question_file))
        try:
            data = self.load_yaml_file(question_file)

            # Required fields in question.yml
            required_fields = ["id", "chapterId", "difficulty", "duration", "author"]
            for field in required_fields:
                if field not in data:
                    result.add_error(f"Missing required field: '{field}'")

            # Validate UUID format for id and chapterId
            uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
            if "id" in data and not re.match(uuid_pattern, str(data.get("id", "")), re.IGNORECASE):
                result.add_error(f"Field 'id' is not a valid UUID: {data.get('id')}")
            if "chapterId" in data and not re.match(uuid_pattern, str(data.get("chapterId", "")), re.IGNORECASE):
                result.add_error(f"Field 'chapterId' is not a valid UUID: {data.get('chapterId')}")

            # Validate difficulty enum
            valid_difficulties = ["easy", "intermediate", "hard"]
            if "difficulty" in data and data["difficulty"] not in valid_difficulties:
                result.add_error(f"Field 'difficulty' has invalid value '{data['difficulty']}'. Allowed: {valid_difficulties}")

            # Validate duration is a positive number
            if "duration" in data:
                if not isinstance(data["duration"], (int, float)) or data["duration"] <= 0:
                    result.add_error(f"Field 'duration' must be a positive number, got: {data['duration']}")

        except Exception as e:
            result.add_error(f"Failed to parse question.yml: {e}")

        results.append(result)

        # Check for at least one translation file
        translation_files = [f for f in quiz_folder.glob("*.yml") if f.name != "question.yml"]
        if not translation_files:
            result = ValidationResult(file_path=str(quiz_folder))
            result.add_error("No translation files found (e.g., en.yml, fr.yml)")
            results.append(result)
        else:
            # Validate each translation file structure
            for trans_file in translation_files:
                trans_result = self._validate_quiz_translation(trans_file)
                if trans_result.errors or trans_result.warnings:
                    results.append(trans_result)

        return results

    def _validate_quiz_translation(self, trans_file: Path) -> ValidationResult:
        """Validate a quiz translation file (e.g., en.yml, fr.yml)."""
        result = ValidationResult(file_path=str(trans_file))

        try:
            data = self.load_yaml_file(trans_file)

            # Required fields in translation files
            required_fields = ["question", "answer", "wrong_answers"]
            for field in required_fields:
                if field not in data:
                    result.add_error(f"Missing required field: '{field}'")

            # Validate wrong_answers is a list with at least 1 item
            if "wrong_answers" in data:
                if not isinstance(data["wrong_answers"], list):
                    result.add_error("Field 'wrong_answers' must be a list")
                elif len(data["wrong_answers"]) < 1:
                    result.add_error("Field 'wrong_answers' must have at least 1 item")

        except Exception as e:
            result.add_error(f"Failed to parse translation file: {e}")

        return result

    def validate_quizzes(self, folder: Path) -> list[ValidationResult]:
        """Validate all quizzes in a content folder's quizz/ subdirectory."""
        results = []
        quizz_folder = folder / "quizz"

        if not quizz_folder.exists():
            # Quiz folder is optional - just return empty results
            return results

        if not quizz_folder.is_dir():
            result = ValidationResult(file_path=str(quizz_folder))
            result.add_error("'quizz' exists but is not a directory")
            return [result]

        # Get all quiz subfolders (numbered folders like 000, 001, etc.)
        # Skip hidden folders (starting with '.')
        quiz_subfolders = sorted([d for d in quizz_folder.iterdir() if d.is_dir() and not d.name.startswith('.')])

        if not quiz_subfolders:
            result = ValidationResult(file_path=str(quizz_folder))
            result.add_warning("Quiz folder exists but contains no quiz subfolders")
            return [result]

        # Validate each quiz subfolder
        for quiz_folder in quiz_subfolders:
            quiz_results = self.validate_quiz_folder(quiz_folder)
            results.extend(quiz_results)

        # Create summary result for quiz validation
        summary_result = ValidationResult(file_path=str(quizz_folder))
        total_quizzes = len(quiz_subfolders)
        quizzes_with_errors = sum(1 for r in results if r.errors)

        if quizzes_with_errors == 0:
            # All quizzes valid - don't add to results (will show in summary)
            pass
        else:
            summary_result.add_warning(f"Validated {total_quizzes} quizzes, {quizzes_with_errors} with errors")
            results.insert(0, summary_result)

        return results

    def _validate_event_semantics(self, yaml_data: dict, file_path: str) -> ValidationResult:
        """Validate semantic rules for events that go beyond schema type checking."""
        result = ValidationResult(file_path=file_path)

        booking_enabled = yaml_data.get("book_online") is True or yaml_data.get("book_in_person") is True

        if booking_enabled and "available_seats" not in yaml_data:
            result.add_warning("Booking enabled but available_seats not set. Internal events should specify capacity.")

        if booking_enabled and "project_id" not in yaml_data:
            result.add_warning("Booking enabled but no project_id. If this is an external event, set book_online/book_in_person to false.")

        if not booking_enabled and yaml_data.get("price_dollars", 0) > 0:
            result.add_warning("Price set but booking is disabled. External events should not have a price.")

        return result

    def validate_folder(self, folder_path: str) -> list[ValidationResult]:
        """Validate a content folder."""
        folder = Path(folder_path)

        if not folder.is_absolute():
            # Try resolving from current directory first
            resolved_from_cwd = (Path.cwd() / folder).resolve()

            if resolved_from_cwd.exists():
                folder = resolved_from_cwd
            else:
                # Try resolving from repo root (for paths like "courses/btc101")
                resolved_from_repo = (self.base_path / folder).resolve()
                if resolved_from_repo.exists():
                    folder = resolved_from_repo
                else:
                    # Last try: strip leading "../" and try from repo root
                    # This handles cases like "../courses/btc101" when user is deep in the repo
                    clean_path = str(folder)
                    while clean_path.startswith("../") or clean_path.startswith("..\\"):
                        clean_path = clean_path[3:]
                    resolved_clean = (self.base_path / clean_path).resolve()
                    if resolved_clean.exists():
                        folder = resolved_clean
                    else:
                        folder = resolved_from_cwd  # Use original for error message
        else:
            folder = folder.resolve()

        if not folder.exists():
            result = ValidationResult(file_path=str(folder))
            result.add_error(f"Folder does not exist. Try using absolute path or run from repo root.")
            return [result]

        if not folder.is_dir():
            result = ValidationResult(file_path=str(folder))
            result.add_error("Path is not a directory")
            return [result]

        # Detect content type
        config = self.detect_content_type(folder)
        if not config:
            result = ValidationResult(file_path=str(folder))
            result.add_error(f"Could not detect content type for folder. Supported types: {list(CONTENT_TYPES.keys())}")
            return [result]

        results = []

        # Find and validate main YAML file
        yaml_path = folder / config.yaml_file
        if not yaml_path.exists():
            result = ValidationResult(file_path=str(yaml_path))
            result.add_warning(f"Missing metadata file: {config.yaml_file} (empty folder?)")
            results.append(result)
            return results
        else:
            schema_path = self.find_schema_file(config)
            if schema_path:
                schema = self.load_json_schema(schema_path)
                yaml_data = self.load_yaml_file(yaml_path)
                result = self.validate_yaml_against_schema(yaml_data, schema, str(yaml_path))
                results.append(result)

                # Run semantic validation for events
                if config.name == "Event":
                    semantic_result = self._validate_event_semantics(yaml_data, str(yaml_path))
                    if semantic_result.warnings or semantic_result.errors:
                        results.append(semantic_result)
            else:
                result = ValidationResult(file_path=str(yaml_path))
                result.add_warning(f"Schema file '{config.schema_file}' not found - skipping validation")
                results.append(result)

        # Validate content files if applicable
        if config.has_markdown_content:
            content_schema_path = self.find_content_schema_file(config)
            content_schema = self.load_json_schema(content_schema_path) if content_schema_path else None

            if config.content_uses_yml:
                # Validate .yml content files (books, bet, projects)
                for yml_file in folder.glob("*.yml"):
                    if yml_file.name != config.yaml_file:  # Skip main metadata file
                        if content_schema:
                            result = self.validate_yml_content(yml_file, content_schema)
                        else:
                            result = ValidationResult(file_path=str(yml_file))
                            result.add_warning("Content schema not found - skipping validation")
                        results.append(result)
            else:
                # Validate .md content files
                # Skip presentation.md as it has no frontmatter requirements
                for md_file in folder.glob("*.md"):
                    if md_file.name == "presentation.md":
                        continue  # Skip presentation files - they don't have frontmatter
                    if content_schema:
                        result = self.validate_markdown_content(md_file, content_schema)
                    else:
                        result = ValidationResult(file_path=str(md_file))
                        result.add_warning("Content schema not found - skipping validation")
                    results.append(result)

        # Validate quizzes if applicable
        if config.has_quizzes:
            quiz_results = self.validate_quizzes(folder)
            results.extend(quiz_results)

        return results

    def print_results(self, results: list[ValidationResult]):
        """Print validation results in a formatted way."""
        total_errors = sum(len(r.errors) for r in results)
        total_warnings = sum(len(r.warnings) for r in results)

        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}Validation Results{Colors.END}")
        print(f"{'='*60}\n")

        for result in results:
            rel_path = result.file_path
            # Try to make path relative to repo root for cleaner output
            file_path = Path(result.file_path)
            repo_root = self._find_repo_root(file_path.parent if file_path.is_file() else file_path)
            try:
                rel_path = str(file_path.relative_to(repo_root))
            except ValueError:
                try:
                    rel_path = str(file_path.relative_to(self.base_path))
                except ValueError:
                    pass

            if result.errors or result.warnings:
                status = f"{Colors.RED}FAILED{Colors.END}" if result.errors else f"{Colors.YELLOW}WARNINGS{Colors.END}"
                print(f"{Colors.CYAN}{rel_path}{Colors.END} - {status}")

                for error in result.errors:
                    print(f"  {Colors.RED}ERROR:{Colors.END} {error}")

                for warning in result.warnings:
                    print(f"  {Colors.YELLOW}WARNING:{Colors.END} {warning}")

                print()
            else:
                print(f"{Colors.CYAN}{rel_path}{Colors.END} - {Colors.GREEN}PASSED{Colors.END}")

        print(f"\n{'='*60}")
        if total_errors == 0:
            print(f"{Colors.GREEN}{Colors.BOLD}All validations passed!{Colors.END}")
        else:
            print(f"{Colors.RED}{Colors.BOLD}Validation failed:{Colors.END} {total_errors} error(s), {total_warnings} warning(s)")
        print(f"{'='*60}\n")

        return total_errors == 0


def main():
    parser = argparse.ArgumentParser(
        description="Validate PlanB Network content against JSON schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate.py tutorials/wallet/sparrow-wallet
  python validate.py courses/btc101
  python validate.py professors/pbn-author
  python validate.py resources/bet/a-game-on-bitcoin
  python validate.py events/awesome-workshop-YYYY

Supported content types:
  - tutorials/<category>/<tutorial-name>
  - courses/<course-name>
  - professors/<professor-name>
  - events/<event-name>
  - resources/bet/<bet-name>
  - resources/books/<book-name>
  - resources/channels/<channel-name>
  - resources/conferences/<conference-name>
  - resources/glossary/<word-name>
  - resources/movies/<movie-name>
  - resources/newsletters/<newsletter-name>
  - resources/podcasts/<podcast-name>
  - resources/projects/<project-name>
        """
    )

    parser.add_argument(
        "folder",
        help="Path to the content folder to validate (relative to repo root or absolute)"
    )

    parser.add_argument(
        "--base-path",
        default=None,
        help="Base path of the repository (auto-detected if not specified)"
    )

    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()

    # Resolve the folder path first to help with repo root detection
    folder_path = Path(args.folder)
    if not folder_path.is_absolute():
        folder_path = Path.cwd() / folder_path
    folder_path = folder_path.resolve()

    # Auto-detect repo root from folder path or base-path
    def find_repo_root(start_path: Path) -> Path:
        """Find repo root by looking for .git directory (primary) or known directories (fallback)."""
        current = start_path
        # First pass: look for .git (most reliable)
        for _ in range(15):  # Max 15 levels up
            if (current / ".git").exists():
                return current
            if current.parent == current:
                break
            current = current.parent

        # Second pass: fallback to known directory structure (but require .git to not be deeper)
        current = start_path
        for _ in range(15):
            # Check for known directories AND verify this isn't inside a docs/template folder
            if all((current / d).exists() for d in ["courses", "tutorials", "professors"]):
                # Make sure we're not in a template/docs subfolder
                if "docs" not in current.parts[-3:] and "PBN-template-repo" not in current.parts:
                    return current
            if current.parent == current:
                break
            current = current.parent
        return start_path

    if args.base_path:
        base_path = Path(args.base_path).resolve()
    else:
        base_path = find_repo_root(folder_path)

    validator = SchemaValidator(str(base_path))
    results = validator.validate_folder(args.folder)

    if args.json:
        output = {
            "folder": args.folder,
            "results": [
                {
                    "file": r.file_path,
                    "valid": r.is_valid,
                    "errors": r.errors,
                    "warnings": r.warnings
                }
                for r in results
            ],
            "total_errors": sum(len(r.errors) for r in results),
            "total_warnings": sum(len(r.warnings) for r in results),
        }
        print(json.dumps(output, indent=2))
        total_errors = output["total_errors"]
        total_warnings = output["total_warnings"]
    else:
        validator.print_results(results)
        total_errors = sum(len(r.errors) for r in results)
        total_warnings = sum(len(r.warnings) for r in results)

    # Exit codes: 0 = passed, 1 = errors, 2 = warnings only
    if total_errors > 0:
        sys.exit(1)
    elif total_warnings > 0:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
