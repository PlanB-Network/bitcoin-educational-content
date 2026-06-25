"""Load JSON schemas and validate data against them."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

from bec.lib.yaml_utils import load_yaml

# Module-level registry cache: schemas_dir → Registry
_registry_cache: dict[str, Registry] = {}


@dataclass
class ValidationResult:
    """Holds validation results for a single file or content check."""

    path: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "valid": self.is_valid,
            "errors": self.errors,
            "warnings": self.warnings,
        }


def load_json_schema(schema_path: Path) -> dict:
    """Load a JSON Schema file from disk."""
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _build_registry(schemas_dir: Path) -> Registry:
    """Build a referencing Registry from JSON Schema files in the schemas directory.

    Loads tags-definitions.json (and any future shared definitions) so that
    $ref pointers like "tags-definitions.json#/definitions/tag_item" resolve.
    """
    key = str(schemas_dir)
    if key in _registry_cache:
        return _registry_cache[key]

    registry = Registry()
    tags_path = schemas_dir / "tags-definitions.json"
    if tags_path.exists():
        with open(tags_path, "r", encoding="utf-8") as f:
            tags_schema = json.load(f)
        resource = Resource.from_contents(tags_schema, default_specification=DRAFT7)
        registry = registry.with_resource("tags-definitions.json", resource)

    _registry_cache[key] = registry
    return registry


def _allows_null(schema: Any) -> bool:
    """Whether a known schema node accepts null (per jsonschema semantics).

    Untyped nodes accept anything, including null. Unknown nodes (None, i.e.
    field not described by the schema) and unresolvable $refs return False so
    their nulls keep the legacy strip-and-warn behavior.
    """
    if isinstance(schema, bool):
        return schema
    if not isinstance(schema, dict):
        return False
    try:
        return Draft7Validator(schema).is_valid(None)
    except Exception:
        return False


def _strip_nulls(
    obj: Any,
    schema: Any = None,
    path: str = "",
) -> tuple[Any, list[str]]:
    """Recursively remove schema-disallowed null values.

    Returns cleaned data and the paths of stripped nulls. Nulls explicitly
    allowed by the schema (type: [x, "null"], enum with null, anyOf/oneOf)
    are kept so jsonschema validates them normally.
    """
    schema = schema if isinstance(schema, dict) else {}
    null_paths: list[str] = []

    if obj is None:
        return None, [path] if path else []
    elif isinstance(obj, dict):
        props = schema.get("properties", {})
        additional = schema.get("additionalProperties")
        cleaned: dict[str, Any] = {}
        for k, v in obj.items():
            current = f"{path} -> {k}" if path else k
            sub_schema = props.get(k, additional)
            if v is None:
                if _allows_null(sub_schema):
                    cleaned[k] = None
                else:
                    null_paths.append(current)
            else:
                cleaned_v, sub = _strip_nulls(v, sub_schema, current)
                null_paths.extend(sub)
                if cleaned_v is not None:
                    cleaned[k] = cleaned_v
        return cleaned, null_paths
    elif isinstance(obj, list):
        items_schema = schema.get("items")
        cleaned_list: list[Any] = []
        for i, item in enumerate(obj):
            current = f"{path}[{i}]"
            if item is None:
                if _allows_null(items_schema):
                    cleaned_list.append(None)
                else:
                    null_paths.append(current)
            else:
                cleaned_item, sub = _strip_nulls(item, items_schema, current)
                null_paths.extend(sub)
                if cleaned_item is not None:
                    cleaned_list.append(cleaned_item)
        return cleaned_list, null_paths
    return obj, null_paths


def validate_yaml_against_schema(
    yaml_data: dict,
    schema: dict,
    file_path: str,
    schema_dir: Path | None = None,
) -> ValidationResult:
    """Validate a YAML-loaded dict against a JSON Schema Draft 7.

    Null values are stripped and reported as warnings.
    When schema_dir is provided, $ref pointers to sibling schema files are resolved.
    """
    result = ValidationResult(path=file_path)

    cleaned, null_paths = _strip_nulls(yaml_data, schema)
    for p in null_paths:
        result.add_warning(f"[{p}] Empty/null value")

    registry = _build_registry(schema_dir) if schema_dir else Registry()
    validator = Draft7Validator(schema, registry=registry)
    for error in validator.iter_errors(cleaned):
        path_str = (
            " -> ".join(str(p) for p in error.absolute_path)
            if error.absolute_path
            else "root"
        )
        result.add_error(f"[{path_str}] {error.message}")

    return result


def validate_markdown_frontmatter(
    md_path: Path,
    content_schema: dict,
    schema_dir: Path | None = None,
) -> ValidationResult:
    """Validate markdown frontmatter and content rules.

    Uses python-frontmatter to parse the file, validates the YAML metadata
    against the schema's properties/required, then applies content_rules.
    """
    import frontmatter

    result = ValidationResult(path=str(md_path))

    try:
        post = frontmatter.load(md_path)
    except Exception as e:
        result.add_error(f"Failed to parse markdown: {e}")
        return result

    _validate_content_fields(
        result,
        dict(post.metadata),
        content_schema,
        "Missing required frontmatter field: '{}'",
        schema_dir,
    )

    # Apply content_rules if present
    content_rules = content_schema.get("content_rules", {})
    if content_rules:
        _validate_content_rules(result, post.content, content_rules, md_path)

    return result


def validate_yml_content(
    yml_path: Path,
    content_schema: dict,
    schema_dir: Path | None = None,
) -> ValidationResult:
    """Validate YML content files (books, bet, projects) against a schema."""
    result = ValidationResult(path=str(yml_path))

    try:
        data = load_yaml(yml_path)
        if data is None:
            data = {}
    except Exception as e:
        result.add_error(f"Failed to parse YAML: {e}")
        return result

    _validate_content_fields(
        result, data, content_schema, "Missing required field: '{}'", schema_dir,
    )

    return result


def _validate_content_fields(
    result: ValidationResult,
    data: Any,
    content_schema: dict,
    missing_msg: str,
    schema_dir: Path | None = None,
) -> None:
    """Validate data against a content schema's properties/required.

    Builds a plain object schema (dropping the non-standard content_rules key)
    and runs Draft7Validator so pattern/items/nested/additionalProperties and
    bool-vs-integer distinctions are all enforced.
    """
    schema: dict[str, Any] = {
        "type": "object",
        "properties": content_schema.get("properties", {}),
        "required": content_schema.get("required", []),
    }
    if "additionalProperties" in content_schema:
        schema["additionalProperties"] = content_schema["additionalProperties"]

    registry = _build_registry(schema_dir) if schema_dir else Registry()
    validator = Draft7Validator(schema, registry=registry)
    for error in validator.iter_errors(data):
        if error.validator == "required" and not error.absolute_path:
            field_name = error.message.split("'")[1]
            result.add_error(missing_msg.format(field_name))
        elif error.absolute_path:
            path_str = " -> ".join(str(p) for p in error.absolute_path)
            result.add_error(f"Field '{path_str}': {error.message}")
        else:
            result.add_error(error.message)


def _validate_content_rules(
    result: ValidationResult,
    content: str,
    rules: dict,
    md_path: Path,
) -> None:
    """Validate markdown body against content_rules from the schema."""
    # Check cover image
    cover_rule = rules.get("cover_image", {})
    if cover_rule.get("required", False):
        cover_pattern = re.compile(r"!\[.*?\]\((?:assets/)?cover\.webp\)")
        first_10 = "\n".join(content.split("\n")[:10])
        if not cover_pattern.search(first_10):
            result.add_error(
                "Cover image ![...](cover.webp) or ![...](assets/cover.webp) "
                "must appear within the first 10 lines after YAML front-matter"
            )

    # Check headings
    heading_rules = rules.get("headings", {})
    h1_rule = heading_rules.get("h1", {})
    if h1_rule.get("allowed") is False:
        # Strip code blocks before checking
        no_code = re.sub(r"```[\s\S]*?```", "", content)
        no_code = re.sub(r"~~~[\s\S]*?~~~", "", no_code)
        no_code = re.sub(r"^(?:    |\t).*$", "", no_code, flags=re.MULTILINE)
        if re.findall(r"^# [^#]", no_code, re.MULTILINE):
            result.add_error(
                "H1 headings (# Title) are not allowed - title comes from YAML 'name' field"
            )

    # Check list markers
    list_rules = rules.get("lists", {})
    unordered = list_rules.get("unordered", {})
    if unordered.get("marker") == "-":
        asterisk = re.findall(r"^\* ", content, re.MULTILINE)
        if asterisk:
            result.add_warning(
                f"Found {len(asterisk)} asterisk (*) list markers. Use dash (-) instead."
            )

    # Check image formats
    image_rules = rules.get("images", {})
    if image_rules.get("format") == "WebP only (.webp extension)":
        non_webp = re.findall(
            r"!\[.*?\]\([^)]+\.(png|jpg|jpeg|gif)\)", content, re.IGNORECASE
        )
        if non_webp:
            result.add_error("Non-WebP images found. All images must be .webp format.")

    # Check alt text
    alt_text_rule = image_rules.get("alt_text", {})
    if alt_text_rule.get("required"):
        empty_alt = re.findall(r"!\[\]\(", content)
        if empty_alt:
            result.add_warning(f"Found {len(empty_alt)} images without alt text")

    # Check assets folder
    assets_path = md_path.parent / "assets"
    if cover_rule.get("required") and not assets_path.exists():
        result.add_error("Assets folder is missing")

    if cover_rule.get("required") and assets_path.exists():
        if not (assets_path / "cover.webp").exists():
            result.add_error("Cover image 'assets/cover.webp' is missing")
