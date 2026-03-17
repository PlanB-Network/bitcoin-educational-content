"""Report command implementations: translation, images, video, proofreading, analytics."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

import click

from bec.lib.content_types import ContentRegistry, ContentType, load_registry
from bec.lib.repo import find_repo_root


# ---------------------------------------------------------------------------
# Content discovery (shared across reports)
# ---------------------------------------------------------------------------

_RESOURCE_DIR_TO_KEY = {
    "bet": "bet",
    "books": "book",
    "channels": "channel",
    "conferences": "conference",
    "glossary": "glossary",
    "movies": "movie",
    "newsletters": "newsletter",
    "papers": "paper",
    "podcasts": "podcast",
    "projects": "project",
}


def _discover_for_type(
    repo_root: Path,
    ct: ContentType,
) -> list[tuple[Path, str]]:
    """Discover all content folders for a single content type."""
    folders: list[tuple[Path, str]] = []
    pattern = ct.path_pattern
    parts = pattern.strip("/").split("/")
    base = repo_root / parts[0]

    if not base.exists() or not base.is_dir():
        return folders

    static_parts: list[str] = []
    for p in parts:
        if "{" in p:
            break
        static_parts.append(p)

    depth_after_static = len(parts) - len(static_parts)
    prefix_dir = repo_root / "/".join(static_parts)

    if not prefix_dir.exists() or not prefix_dir.is_dir():
        return folders

    if depth_after_static == 1:
        for d in sorted(prefix_dir.iterdir()):
            if d.is_dir() and not d.name.startswith("."):
                folders.append((d, ct.key))
    elif depth_after_static == 2:
        for cat_dir in sorted(prefix_dir.iterdir()):
            if not cat_dir.is_dir() or cat_dir.name.startswith("."):
                continue
            for d in sorted(cat_dir.iterdir()):
                if d.is_dir() and not d.name.startswith("."):
                    folders.append((d, ct.key))

    return folders


def _discover_all(
    repo_root: Path,
    registry: ContentRegistry,
) -> list[tuple[Path, str]]:
    """Discover all content folders across all types."""
    folders: list[tuple[Path, str]] = []
    for ct in registry.content_types.values():
        folders.extend(_discover_for_type(repo_root, ct))
    folders.sort(key=lambda t: t[0])
    return folders


# ---------------------------------------------------------------------------
# Translation coverage analysis
# ---------------------------------------------------------------------------

# Content types that use .md for language files
_MD_TYPES = {"course", "tutorial", "glossary"}
# Content types that use .yml for language content files
_YML_CONTENT_TYPES = {"bet", "book", "project"}
# Content types that use .yml for professor profiles
_PROF_TYPE = "professor"
# Content types with no translatable files (metadata-only)
_NO_TRANSLATION_TYPES = {"event", "channel", "conference", "movie", "newsletter", "podcast", "paper"}


def _get_language_files(folder: Path, content_type_key: str) -> dict[str, bool]:
    """Check which language files exist for a content folder.

    Returns dict mapping lang_code -> exists.
    Only checks for languages that actually have files; caller filters.
    """
    result: dict[str, bool] = {}

    if content_type_key in _MD_TYPES:
        # .md files: en.md, fr.md, etc.
        for f in folder.iterdir():
            if f.is_file() and f.suffix == ".md":
                result[f.stem] = True
    elif content_type_key in _YML_CONTENT_TYPES or content_type_key == _PROF_TYPE:
        # .yml files: en.yml, fr.yml, etc.
        # Exclude metadata files (course.yml, tutorial.yml, etc.)
        metadata_names = {
            "bet": "bet.yml",
            "book": "book.yml",
            "project": "project.yml",
            "professor": "professor.yml",
        }
        meta = metadata_names.get(content_type_key, "")
        for f in folder.iterdir():
            if f.is_file() and f.suffix == ".yml" and f.name != meta:
                result[f.stem] = True

    return result


def count_words(file_path: Path) -> int:
    """Count words in a file."""
    try:
        return len(file_path.read_text(encoding="utf-8").split())
    except Exception:
        return 0


def analyze_translation_coverage(
    repo_root: Path,
    registry: ContentRegistry,
) -> dict:
    """Analyze translation coverage for all translatable content types.

    Returns a dict with:
    - by_type: {type_key: {items: [{id, path, languages: {lang: {exists, words}}}], ...}}
    - languages: list of all detected languages
    - summary: {total_items, total_translations, total_possible, coverage_pct}
    """
    # Translatable types: those with markdown or yml content files
    translatable_keys = set()
    for key, ct in registry.content_types.items():
        if key not in _NO_TRANSLATION_TYPES:
            translatable_keys.add(key)

    all_folders = _discover_all(repo_root, registry)

    # Collect all languages seen across the repo
    all_languages: set[str] = set()

    # Group analysis by content type
    by_type: dict[str, list[dict]] = {}

    for folder, type_key in all_folders:
        if type_key not in translatable_keys:
            continue

        lang_files = _get_language_files(folder, type_key)
        all_languages.update(lang_files.keys())

        rel_path = str(folder.relative_to(repo_root))
        item_id = folder.name

        item_data: dict = {
            "id": item_id,
            "path": rel_path,
            "languages": {},
        }

        for lang, exists in lang_files.items():
            words = 0
            if exists:
                if type_key in _MD_TYPES:
                    words = count_words(folder / f"{lang}.md")
                else:
                    words = count_words(folder / f"{lang}.yml")
            item_data["languages"][lang] = {"exists": True, "words": words}

        by_type.setdefault(type_key, []).append(item_data)

    # Sort languages, putting en first
    sorted_langs = sorted(all_languages)
    if "en" in sorted_langs:
        sorted_langs.remove("en")
        sorted_langs.insert(0, "en")

    # Calculate summary statistics
    total_items = sum(len(items) for items in by_type.values())
    total_translations = sum(
        len(item["languages"])
        for items in by_type.values()
        for item in items
    )
    total_possible = total_items * len(sorted_langs) if sorted_langs else 0
    coverage_pct = (total_translations / total_possible * 100) if total_possible > 0 else 0

    # Per-type stats
    type_stats = {}
    for type_key, items in by_type.items():
        ct = registry.content_types.get(type_key)
        type_name = ct.name if ct else type_key
        type_translations = sum(len(item["languages"]) for item in items)
        type_possible = len(items) * len(sorted_langs) if sorted_langs else 0
        type_stats[type_key] = {
            "name": type_name,
            "items": len(items),
            "translations": type_translations,
            "possible": type_possible,
            "coverage_pct": (type_translations / type_possible * 100) if type_possible > 0 else 0,
        }

    # Per-language stats
    lang_stats = {}
    for lang in sorted_langs:
        count = sum(
            1
            for items in by_type.values()
            for item in items
            if lang in item["languages"]
        )
        lang_stats[lang] = {
            "count": count,
            "total": total_items,
            "coverage_pct": (count / total_items * 100) if total_items > 0 else 0,
        }

    return {
        "by_type": by_type,
        "type_stats": type_stats,
        "lang_stats": lang_stats,
        "languages": sorted_langs,
        "summary": {
            "total_items": total_items,
            "total_translations": total_translations,
            "total_possible": total_possible,
            "coverage_pct": round(coverage_pct, 1),
        },
    }


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def _generate_translation_html(analysis: dict) -> str:
    """Generate self-contained HTML report for translation coverage."""
    languages = analysis["languages"]
    by_type = analysis["by_type"]
    type_stats = analysis["type_stats"]
    summary = analysis["summary"]
    lang_stats = analysis["lang_stats"]

    # Type display order
    type_order = ["course", "tutorial", "professor", "glossary", "book", "bet", "project"]
    ordered_types = [t for t in type_order if t in by_type]
    # Add any types not in the order list
    for t in sorted(by_type.keys()):
        if t not in ordered_types:
            ordered_types.append(t)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Translation Overview</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{ color: #333; text-align: center; margin-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 5px; }}
        .stats {{
            margin: 20px auto;
            text-align: center;
            font-size: 14px;
            color: #666;
            max-width: 1200px;
        }}
        .stats strong {{ color: #333; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 6px;
            text-align: center;
            font-size: 11px;
        }}
        th {{
            background-color: #2196F3;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.course-header {{
            background-color: #1976D2;
            text-align: left;
            min-width: 100px;
        }}
        th.type-header {{
            background-color: #1565C0;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
        .translation-exists {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }}
        .translation-missing {{
            background-color: #f44336;
            color: white;
        }}
        .translation-info {{
            font-size: 9px;
            display: block;
            margin-top: 2px;
        }}
        .legend {{
            margin: 20px auto;
            padding: 15px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 900px;
        }}
        .legend h3 {{ margin-top: 0; color: #333; }}
        .legend-item {{
            display: inline-block;
            margin: 5px 15px 5px 0;
        }}
        .legend-color {{
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border-radius: 3px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 20px;
        }}
        .container {{ max-width: 1800px; margin: 0 auto; }}
        .header {{ position: relative; padding: 20px 0; }}
        .back-button {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #f7931a;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-bottom: 20px;
        }}
        .back-button:hover {{ background-color: #e08316; }}
        .back-button::before {{ content: '\\2190 '; }}
        .lang-header {{
            writing-mode: vertical-rl;
            text-orientation: mixed;
            min-width: 30px;
            padding: 8px 4px !important;
        }}
        .type-summary {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 20px auto;
            max-width: 1200px;
            justify-content: center;
        }}
        .type-card {{
            background: white;
            border-radius: 8px;
            padding: 15px 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            min-width: 150px;
            text-align: center;
        }}
        .type-card h4 {{ margin: 0 0 5px 0; color: #333; }}
        .type-card .pct {{ font-size: 24px; font-weight: bold; }}
        .type-card .detail {{ font-size: 12px; color: #666; }}
        .pct-high {{ color: #4CAF50; }}
        .pct-mid {{ color: #FF9800; }}
        .pct-low {{ color: #f44336; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>Markdown Translation Overview</h1>
        </div>
        <div class="stats">
            <strong>Languages detected:</strong> {len(languages)} |
            <strong>Translatable items:</strong> {summary["total_items"]} |
            <strong>Translations:</strong> {summary["total_translations"]}/{summary["total_possible"]} ({summary["coverage_pct"]}% overall)
        </div>

        <div class="type-summary">"""]

    # Type summary cards
    for type_key in ordered_types:
        ts = type_stats[type_key]
        pct = ts["coverage_pct"]
        pct_class = "pct-high" if pct >= 50 else ("pct-mid" if pct >= 20 else "pct-low")
        html_parts.append(f"""
            <div class="type-card">
                <h4>{ts["name"]}s</h4>
                <div class="pct {pct_class}">{pct:.0f}%</div>
                <div class="detail">{ts["translations"]}/{ts["possible"]} translations</div>
                <div class="detail">{ts["items"]} items</div>
            </div>""")

    html_parts.append("""
        </div>

        <div class="legend">
            <h3>Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>Translated (file exists, word count shown)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #f44336;"></span>
                <span>Missing (no file)</span>
            </div>
        </div>""")

    # Per-type tables
    for type_key in ordered_types:
        items = by_type[type_key]
        ts = type_stats[type_key]
        sorted_items = sorted(items, key=lambda x: x["id"])

        html_parts.append(f"""
        <h2>{ts["name"]}s ({ts["items"]} items, {ts["coverage_pct"]:.0f}% coverage)</h2>
        <table>
            <thead>
                <tr>
                    <th class="course-header">{ts["name"]}</th>""")

        for lang in languages:
            html_parts.append(f"                    <th class='lang-header'>{lang}</th>\n")

        html_parts.append("""                </tr>
            </thead>
            <tbody>""")

        for item in sorted_items:
            html_parts.append(f"""
                <tr>
                    <td style='text-align: left; font-weight: bold;'>{item["id"]}</td>""")

            for lang in languages:
                lang_data = item["languages"].get(lang)
                if lang_data and lang_data["exists"]:
                    words = lang_data["words"]
                    html_parts.append(f"""
                    <td class='translation-exists'>
                        <strong>&#10003;</strong>
                        <span class='translation-info'>{words:,}w</span>
                    </td>""")
                else:
                    html_parts.append("""
                    <td class='translation-missing'>
                        <strong>&#10007;</strong>
                    </td>""")

            html_parts.append("\n                </tr>")

        html_parts.append("""
            </tbody>
        </table>""")

    html_parts.append(f"""
        <div class="footer">
            Generated on {now}<br>
            Run <code>bec report translation</code> to update this report<br>
            <br>
            <small>Numbers shown are word counts (w = words). Languages auto-detected from content files.</small>
        </div>
    </div>
</body>
</html>
""")

    return "".join(html_parts)


# ---------------------------------------------------------------------------
# JSON output
# ---------------------------------------------------------------------------

def _translation_to_json(analysis: dict) -> dict:
    """Convert analysis to JSON-serializable output structure."""
    return {
        "summary": analysis["summary"],
        "type_stats": analysis["type_stats"],
        "lang_stats": analysis["lang_stats"],
        "languages": analysis["languages"],
        "items": {
            type_key: [
                {
                    "id": item["id"],
                    "path": item["path"],
                    "languages": {
                        lang: data["words"]
                        for lang, data in item["languages"].items()
                    },
                }
                for item in sorted(items, key=lambda x: x["id"])
            ]
            for type_key, items in analysis["by_type"].items()
        },
    }


# ---------------------------------------------------------------------------
# Command runners
# ---------------------------------------------------------------------------

def run_report_translation(
    output: str | None,
    json_output: bool,
) -> None:
    """Generate markdown translation coverage report."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if not json_output:
        click.echo("Analyzing translation coverage...", err=True)
    analysis = analyze_translation_coverage(repo_root, registry)

    if json_output:
        click.echo(json.dumps(_translation_to_json(analysis), indent=2))
        return

    # Determine output directory
    output_dir = Path(output) if output else repo_root / "docs" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "md_translation_overview.html"

    html = _generate_translation_html(analysis)
    output_file.write_text(html, encoding="utf-8")

    click.echo(f"Report generated: {output_file}")
    click.echo(
        f"  {analysis['summary']['total_translations']}/{analysis['summary']['total_possible']} "
        f"translations ({analysis['summary']['coverage_pct']}% coverage)"
    )


# ---------------------------------------------------------------------------
# Image translation analysis
# ---------------------------------------------------------------------------

_IMAGE_RE = re.compile(r"!\[.*?\]\((.*?)\)")

# Content types that have markdown with embedded images
_IMAGE_TYPES = {"course", "tutorial"}


def _extract_images_from_markdown(md_path: Path) -> list[str]:
    """Extract image reference paths from a markdown file."""
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception:
        return []
    refs = _IMAGE_RE.findall(content)
    # Filter out URLs (only keep local paths)
    return [r for r in refs if not r.startswith(("http://", "https://", "//"))]


def _classify_image(img_path: str, lang: str) -> str:
    """Classify an image reference as 'translated' or 'shared'.

    Images with the language code in the path (e.g., assets/fr/001.webp)
    are considered translated for that language.
    All other images (numbered dirs, no-txt, etc.) are shared/untranslated.
    """
    if f"/{lang}/" in img_path:
        return "translated"
    return "shared"


def analyze_image_translation(
    repo_root: Path,
    registry: ContentRegistry,
) -> dict:
    """Analyze image translation status for all content with markdown.

    For each content item and language, counts how many images use
    language-specific paths (translated) vs shared/generic paths.
    """
    all_folders = _discover_all(repo_root, registry)

    by_type: dict[str, list[dict]] = {}
    all_languages: set[str] = set()

    for folder, type_key in all_folders:
        if type_key not in _IMAGE_TYPES:
            continue

        rel_path = str(folder.relative_to(repo_root))
        item_id = folder.name

        lang_data: dict[str, dict] = {}

        for md_file in sorted(folder.iterdir()):
            if not md_file.is_file() or md_file.suffix != ".md":
                continue
            lang = md_file.stem
            all_languages.add(lang)

            images = _extract_images_from_markdown(md_file)
            if not images:
                lang_data[lang] = {
                    "total_images": 0,
                    "translated_images": 0,
                    "shared_images": 0,
                    "percentage": 0.0,
                }
                continue

            translated = sum(1 for img in images if _classify_image(img, lang) == "translated")
            shared = len(images) - translated
            pct = (translated / len(images) * 100) if images else 0.0

            lang_data[lang] = {
                "total_images": len(images),
                "translated_images": translated,
                "shared_images": shared,
                "percentage": round(pct, 1),
            }

        if lang_data:
            by_type.setdefault(type_key, []).append({
                "id": item_id,
                "path": rel_path,
                "languages": lang_data,
            })

    sorted_langs = sorted(all_languages)
    if "en" in sorted_langs:
        sorted_langs.remove("en")
        sorted_langs.insert(0, "en")

    # Summary stats
    total_images = 0
    total_translated = 0
    for items in by_type.values():
        for item in items:
            for ld in item["languages"].values():
                total_images += ld["total_images"]
                total_translated += ld["translated_images"]

    overall_pct = (total_translated / total_images * 100) if total_images > 0 else 0.0

    # Per-type stats
    type_stats = {}
    for type_key, items in by_type.items():
        ct = registry.content_types.get(type_key)
        type_name = ct.name if ct else type_key
        t_imgs = sum(ld["total_images"] for item in items for ld in item["languages"].values())
        t_trans = sum(ld["translated_images"] for item in items for ld in item["languages"].values())
        type_stats[type_key] = {
            "name": type_name,
            "items": len(items),
            "total_images": t_imgs,
            "translated_images": t_trans,
            "percentage": round((t_trans / t_imgs * 100) if t_imgs > 0 else 0.0, 1),
        }

    return {
        "by_type": by_type,
        "type_stats": type_stats,
        "languages": sorted_langs,
        "summary": {
            "total_images": total_images,
            "translated_images": total_translated,
            "overall_pct": round(overall_pct, 1),
            "content_items": sum(len(items) for items in by_type.values()),
        },
    }


# ---------------------------------------------------------------------------
# Image report — HTML generation
# ---------------------------------------------------------------------------

def _generate_images_html(analysis: dict) -> str:
    """Generate self-contained HTML for image translation report."""
    languages = analysis["languages"]
    by_type = analysis["by_type"]
    type_stats = analysis["type_stats"]
    summary = analysis["summary"]

    type_order = ["course", "tutorial"]
    ordered_types = [t for t in type_order if t in by_type]
    for t in sorted(by_type.keys()):
        if t not in ordered_types:
            ordered_types.append(t)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Translation Overview</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{ color: #333; text-align: center; margin-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 5px; }}
        .stats {{
            margin: 20px auto;
            text-align: center;
            font-size: 14px;
            color: #666;
            max-width: 1200px;
        }}
        .stats strong {{ color: #333; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 6px;
            text-align: center;
            font-size: 11px;
        }}
        th {{
            background-color: #9C27B0;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.course-header {{
            background-color: #673AB7;
            text-align: left;
            min-width: 100px;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
        .translation-complete {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }}
        .translation-partial {{
            background-color: #FFC107;
            color: black;
        }}
        .translation-low {{
            background-color: #FF9800;
            color: white;
        }}
        .translation-none {{
            background-color: #f44336;
            color: white;
        }}
        .translation-na {{
            background-color: #9E9E9E;
            color: white;
        }}
        .translation-info {{
            font-size: 9px;
            display: block;
            margin-top: 2px;
        }}
        .legend {{
            margin: 20px auto;
            padding: 15px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 900px;
        }}
        .legend h3 {{ margin-top: 0; color: #333; }}
        .legend-item {{
            display: inline-block;
            margin: 5px 15px 5px 0;
        }}
        .legend-color {{
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border-radius: 3px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 20px;
        }}
        .container {{ max-width: 1800px; margin: 0 auto; }}
        .header {{ position: relative; padding: 20px 0; }}
        .back-button {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #f7931a;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-bottom: 20px;
        }}
        .back-button:hover {{ background-color: #e08316; }}
        .back-button::before {{ content: '\\2190 '; }}
        .lang-header {{
            writing-mode: vertical-rl;
            text-orientation: mixed;
            min-width: 30px;
            padding: 8px 4px !important;
        }}
        .type-summary {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 20px auto;
            max-width: 1200px;
            justify-content: center;
        }}
        .type-card {{
            background: white;
            border-radius: 8px;
            padding: 15px 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            min-width: 150px;
            text-align: center;
        }}
        .type-card h4 {{ margin: 0 0 5px 0; color: #333; }}
        .type-card .pct {{ font-size: 24px; font-weight: bold; }}
        .type-card .detail {{ font-size: 12px; color: #666; }}
        .pct-high {{ color: #4CAF50; }}
        .pct-mid {{ color: #FF9800; }}
        .pct-low {{ color: #f44336; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>Image Translation Overview</h1>
        </div>
        <div class="stats">
            <strong>Languages detected:</strong> {len(languages)} |
            <strong>Content items:</strong> {summary["content_items"]} |
            <strong>Images:</strong> {summary["translated_images"]:,}/{summary["total_images"]:,} translated ({summary["overall_pct"]}%)
        </div>

        <div class="type-summary">"""]

    for type_key in ordered_types:
        ts = type_stats[type_key]
        pct = ts["percentage"]
        pct_class = "pct-high" if pct >= 50 else ("pct-mid" if pct >= 20 else "pct-low")
        html_parts.append(f"""
            <div class="type-card">
                <h4>{ts["name"]}s</h4>
                <div class="pct {pct_class}">{pct:.0f}%</div>
                <div class="detail">{ts["translated_images"]:,}/{ts["total_images"]:,} images</div>
                <div class="detail">{ts["items"]} items</div>
            </div>""")

    html_parts.append("""
        </div>

        <div class="legend">
            <h3>Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>Complete (100%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FFC107;"></span>
                <span>Partial (50-99%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF9800;"></span>
                <span>Low (1-49%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #f44336;"></span>
                <span>None (0%)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #9E9E9E;"></span>
                <span>N/A (no file or no images)</span>
            </div>
        </div>""")

    for type_key in ordered_types:
        items = by_type[type_key]
        ts = type_stats[type_key]
        sorted_items = sorted(items, key=lambda x: x["id"])

        html_parts.append(f"""
        <h2>{ts["name"]}s ({ts["items"]} items, {ts["percentage"]:.0f}% translated)</h2>
        <table>
            <thead>
                <tr>
                    <th class="course-header">{ts["name"]}</th>""")

        for lang in languages:
            html_parts.append(f"                    <th class='lang-header'>{lang}</th>\n")

        html_parts.append("""                </tr>
            </thead>
            <tbody>""")

        for item in sorted_items:
            html_parts.append(f"""
                <tr>
                    <td style='text-align: left; font-weight: bold;'>{item["id"]}</td>""")

            for lang in languages:
                ld = item["languages"].get(lang)
                if not ld:
                    html_parts.append("""
                    <td class='translation-na'>
                        <strong>N/A</strong>
                        <span class='translation-info'>No file</span>
                    </td>""")
                elif ld["total_images"] == 0:
                    html_parts.append("""
                    <td class='translation-na'>
                        <strong>N/A</strong>
                        <span class='translation-info'>No images</span>
                    </td>""")
                else:
                    pct = ld["percentage"]
                    t = ld["translated_images"]
                    total = ld["total_images"]
                    if pct == 100:
                        css = "translation-complete"
                    elif pct >= 50:
                        css = "translation-partial"
                    elif pct > 0:
                        css = "translation-low"
                    else:
                        css = "translation-none"
                    html_parts.append(f"""
                    <td class='{css}'>
                        <strong>{t}/{total}</strong>
                        <span class='translation-info'>{pct:.0f}%</span>
                    </td>""")

            html_parts.append("\n                </tr>")

        html_parts.append("""
            </tbody>
        </table>""")

    html_parts.append(f"""
        <div class="footer">
            Generated on {now}<br>
            Run <code>bec report images</code> to update this report<br>
            <br>
            <small>Images are considered translated when their path contains the language code (e.g., assets/fr/001.webp).</small>
        </div>
    </div>
</body>
</html>
""")

    return "".join(html_parts)


# ---------------------------------------------------------------------------
# Image report — JSON output
# ---------------------------------------------------------------------------

def _images_to_json(analysis: dict) -> dict:
    """Convert image analysis to JSON-serializable output."""
    return {
        "summary": analysis["summary"],
        "type_stats": analysis["type_stats"],
        "languages": analysis["languages"],
        "items": {
            type_key: [
                {
                    "id": item["id"],
                    "path": item["path"],
                    "languages": {
                        lang: {
                            "total": data["total_images"],
                            "translated": data["translated_images"],
                            "shared": data["shared_images"],
                            "percentage": data["percentage"],
                        }
                        for lang, data in item["languages"].items()
                    },
                }
                for item in sorted(items, key=lambda x: x["id"])
            ]
            for type_key, items in analysis["by_type"].items()
        },
    }


# ---------------------------------------------------------------------------
# Image report — runner
# ---------------------------------------------------------------------------

def run_report_images(
    output: str | None,
    json_output: bool,
) -> None:
    """Generate image translation report."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if not json_output:
        click.echo("Analyzing image translation coverage...", err=True)
    analysis = analyze_image_translation(repo_root, registry)

    if json_output:
        click.echo(json.dumps(_images_to_json(analysis), indent=2))
        return

    output_dir = Path(output) if output else repo_root / "docs" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "image_translation_overview.html"

    html = _generate_images_html(analysis)
    output_file.write_text(html, encoding="utf-8")

    click.echo(f"Report generated: {output_file}")
    click.echo(
        f"  {analysis['summary']['translated_images']:,}/{analysis['summary']['total_images']:,} "
        f"images translated ({analysis['summary']['overall_pct']}%)"
    )


def run_report_all(
    output: str | None,
    json_output: bool,
) -> None:
    """Run all reports."""
    if json_output:
        # Merge all report JSON into a single object
        repo_root = find_repo_root()
        registry = load_registry(repo_root)
        combined: dict = {}

        t_analysis = analyze_translation_coverage(repo_root, registry)
        combined["translation"] = _translation_to_json(t_analysis)

        i_analysis = analyze_image_translation(repo_root, registry)
        combined["images"] = _images_to_json(i_analysis)

        v_analysis = analyze_video_deployment(repo_root, registry)
        combined["video"] = _video_to_json(v_analysis)

        p_analysis = analyze_proofreading(repo_root, registry)
        combined["proofreading"] = _proofreading_to_json(p_analysis)

        a_analysis = analyze_course_analytics(repo_root)
        combined["analytics"] = _analytics_to_json(a_analysis)

        click.echo(json.dumps(combined, indent=2))
        return

    click.echo("Running all reports...", err=True)
    run_report_translation(output=output, json_output=False)
    run_report_images(output=output, json_output=False)
    run_report_video(output=output, json_output=False)
    run_report_proofreading(output=output, json_output=False)
    run_report_analytics(output=output, json_output=False)
    click.echo("All reports complete.", err=True)


# ===========================================================================
# Phase 11: Video deployment report
# ===========================================================================

# Languages to check for video deployment
_VIDEO_LANGUAGES = ["en", "fr", "es", "it", "de", "ru", "zh-Hant"]


def _parse_video_coverage(
    videos: list[dict],
    languages: list[str],
) -> dict[str, dict]:
    """Parse video entries and compute per-language coverage.

    Returns {lang: {youtube: int, peertube: int, both: int, covered: int}}
    """
    coverage: dict[str, dict[str, int]] = {
        lang: {"youtube": 0, "peertube": 0, "both": 0, "covered": 0}
        for lang in languages
    }

    for video in videos:
        yt_langs: set[str] = set()
        pt_langs: set[str] = set()

        for entry in video.get("youtube", []):
            if isinstance(entry, dict):
                yt_langs.update(entry.keys())

        for entry in video.get("peertube", []):
            if isinstance(entry, dict):
                pt_langs.update(entry.keys())

        for entry in video.get("rumble", []):
            if isinstance(entry, dict):
                pt_langs.update(entry.keys())  # treat rumble like peertube

        for lang in languages:
            has_yt = lang in yt_langs
            has_pt = lang in pt_langs
            if has_yt and has_pt:
                coverage[lang]["both"] += 1
                coverage[lang]["covered"] += 1
            elif has_yt:
                coverage[lang]["youtube"] += 1
                coverage[lang]["covered"] += 1
            elif has_pt:
                coverage[lang]["peertube"] += 1
                coverage[lang]["covered"] += 1

    return coverage


def analyze_video_deployment(
    repo_root: Path,
    registry: ContentRegistry,
) -> dict:
    """Analyze video deployment status for all courses."""
    from bec.lib.yaml_utils import load_yaml

    ct = registry.content_types.get("course")
    if not ct:
        return {"courses": [], "languages": _VIDEO_LANGUAGES, "summary": {
            "total_courses": 0, "total_videos": 0,
        }}

    course_folders = _discover_for_type(repo_root, ct)
    languages = list(_VIDEO_LANGUAGES)

    courses: list[dict] = []
    total_videos = 0

    for folder, _type_key in course_folders:
        meta_file = folder / "course.yml"
        if not meta_file.is_file():
            continue
        data = load_yaml(meta_file)
        if not data:
            continue

        course_id = folder.name
        videos = data.get("videos", [])
        if not isinstance(videos, list):
            videos = []

        total_videos += len(videos)
        coverage = _parse_video_coverage(videos, languages)

        courses.append({
            "id": course_id,
            "path": str(folder.relative_to(repo_root)),
            "total_videos": len(videos),
            "coverage": coverage,
        })

    courses.sort(key=lambda c: c["id"])

    # Summary stats
    total_covered = sum(
        c["coverage"][languages[0]]["covered"]
        for c in courses
        if c["total_videos"] > 0
    ) if languages else 0

    return {
        "courses": courses,
        "languages": languages,
        "summary": {
            "total_courses": len(courses),
            "total_videos": total_videos,
            "courses_with_videos": sum(1 for c in courses if c["total_videos"] > 0),
        },
    }


def _generate_video_html(analysis: dict) -> str:
    """Generate self-contained HTML for video deployment report."""
    courses = analysis["courses"]
    languages = analysis["languages"]
    summary = analysis["summary"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Deployment Overview</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{ color: #333; text-align: center; margin-bottom: 10px; }}
        .stats {{
            margin: 20px auto;
            text-align: center;
            font-size: 14px;
            color: #666;
            max-width: 1200px;
        }}
        .stats strong {{ color: #333; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 6px;
            text-align: center;
            font-size: 11px;
        }}
        th {{
            background-color: #E91E63;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.course-header {{
            background-color: #C2185B;
            text-align: left;
            min-width: 100px;
        }}
        th.total-header {{
            background-color: #AD1457;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
        .coverage-complete {{ background-color: #4CAF50; color: white; font-weight: bold; }}
        .coverage-partial {{ background-color: #FFC107; color: black; }}
        .coverage-low {{ background-color: #FF9800; color: white; }}
        .coverage-none {{ background-color: #f44336; color: white; }}
        .coverage-na {{ background-color: #9E9E9E; color: white; }}
        .coverage-info {{ font-size: 9px; display: block; margin-top: 2px; }}
        .provider {{ font-size: 8px; display: inline-block; padding: 1px 3px; border-radius: 2px; margin: 1px; }}
        .prov-yt {{ background-color: rgba(255,0,0,0.15); }}
        .prov-pt {{ background-color: rgba(0,0,255,0.15); }}
        .prov-both {{ background-color: rgba(0,128,0,0.15); }}
        .legend {{
            margin: 20px auto;
            padding: 15px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 900px;
        }}
        .legend h3 {{ margin-top: 0; color: #333; }}
        .legend-item {{ display: inline-block; margin: 5px 15px 5px 0; }}
        .legend-color {{
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border-radius: 3px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 20px;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        .header {{ position: relative; padding: 20px 0; }}
        .back-button {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #f7931a;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-bottom: 20px;
        }}
        .back-button:hover {{ background-color: #e08316; }}
        .back-button::before {{ content: '\\2190 '; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>Video Deployment Overview</h1>
        </div>
        <div class="stats">
            <strong>Courses:</strong> {summary["total_courses"]} |
            <strong>With videos:</strong> {summary["courses_with_videos"]} |
            <strong>Total videos:</strong> {summary["total_videos"]} |
            <strong>Languages tracked:</strong> {len(languages)}
        </div>

        <div class="legend">
            <h3>Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>100% coverage</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FFC107;"></span>
                <span>50-99%</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF9800;"></span>
                <span>1-49%</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #f44336;"></span>
                <span>0%</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #9E9E9E;"></span>
                <span>No videos</span>
            </div>
            <div class="legend-item">
                <span class="provider prov-yt">Y</span> YouTube
                <span class="provider prov-pt">P</span> PeerTube
                <span class="provider prov-both">B</span> Both
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th class="course-header">Course</th>
                    <th class="total-header">Videos</th>"""]

    for lang in languages:
        html_parts.append(f"                    <th>{lang.upper()}</th>\n")

    html_parts.append("""                </tr>
            </thead>
            <tbody>""")

    for course in courses:
        total = course["total_videos"]
        html_parts.append(f"""
                <tr>
                    <td style='text-align: left; font-weight: bold;'>{course["id"]}</td>
                    <td><strong>{total}</strong></td>""")

        for lang in languages:
            cov = course["coverage"][lang]
            covered = cov["covered"]
            if total == 0:
                css = "coverage-na"
                label = "N/A"
                info = "No videos"
            elif covered == total:
                css = "coverage-complete"
                pct = 100
                label = f"{covered}/{total}"
                info = f"{pct}%"
            elif covered > 0:
                pct = round(covered / total * 100)
                css = "coverage-partial" if pct >= 50 else "coverage-low"
                label = f"{covered}/{total}"
                info = f"{pct}%"
            else:
                css = "coverage-none"
                label = f"0/{total}"
                info = "0%"

            providers = ""
            if cov["youtube"] > 0:
                providers += f"<span class='provider prov-yt'>Y:{cov['youtube']}</span>"
            if cov["peertube"] > 0:
                providers += f"<span class='provider prov-pt'>P:{cov['peertube']}</span>"
            if cov["both"] > 0:
                providers += f"<span class='provider prov-both'>B:{cov['both']}</span>"

            html_parts.append(f"""
                    <td class='{css}'>
                        <strong>{label}</strong>
                        <span class='coverage-info'>{info}</span>
                        {providers}
                    </td>""")

        html_parts.append("\n                </tr>")

    html_parts.append(f"""
            </tbody>
        </table>

        <div class="footer">
            Generated on {now}<br>
            Run <code>bec report video</code> to update this report
        </div>
    </div>
</body>
</html>
""")

    return "".join(html_parts)


def _video_to_json(analysis: dict) -> dict:
    """Convert video analysis to JSON-serializable output."""
    return {
        "summary": analysis["summary"],
        "languages": analysis["languages"],
        "courses": [
            {
                "id": c["id"],
                "path": c["path"],
                "total_videos": c["total_videos"],
                "coverage": {
                    lang: {
                        "covered": cov["covered"],
                        "youtube": cov["youtube"],
                        "peertube": cov["peertube"],
                        "both": cov["both"],
                        "percentage": round(cov["covered"] / c["total_videos"] * 100, 1)
                        if c["total_videos"] > 0 else 0.0,
                    }
                    for lang, cov in c["coverage"].items()
                },
            }
            for c in analysis["courses"]
        ],
    }


def run_report_video(
    output: str | None,
    json_output: bool,
) -> None:
    """Generate video deployment status report."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if not json_output:
        click.echo("Analyzing video deployment...", err=True)
    analysis = analyze_video_deployment(repo_root, registry)

    if json_output:
        click.echo(json.dumps(_video_to_json(analysis), indent=2))
        return

    output_dir = Path(output) if output else repo_root / "docs" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "video_deployment_overview.html"

    html = _generate_video_html(analysis)
    output_file.write_text(html, encoding="utf-8")

    click.echo(f"Report generated: {output_file}")
    s = analysis["summary"]
    click.echo(
        f"  {s['courses_with_videos']}/{s['total_courses']} courses have videos "
        f"({s['total_videos']} total)"
    )


# ===========================================================================
# Phase 12: Proofreading dashboard report
# ===========================================================================

# Content types that have proofreading metadata
_PROOFREAD_TYPES = {"course", "tutorial"}


def analyze_proofreading(
    repo_root: Path,
    registry: ContentRegistry,
) -> dict:
    """Analyze proofreading status for courses and tutorials."""
    from bec.lib.yaml_utils import load_yaml

    all_folders: list[tuple[Path, str]] = []
    for type_key in _PROOFREAD_TYPES:
        ct = registry.content_types.get(type_key)
        if ct:
            all_folders.extend(_discover_for_type(repo_root, ct))
    all_folders.sort(key=lambda t: t[0])

    all_languages: set[str] = set()
    contributors_count: dict[str, int] = {}  # contributor -> total count
    contributors_langs: dict[str, set[str]] = {}  # contributor -> set of langs

    by_type: dict[str, list[dict]] = {}

    for folder, type_key in all_folders:
        meta_name = "course.yml" if type_key == "course" else "tutorial.yml"
        meta_file = folder / meta_name
        if not meta_file.is_file():
            continue
        data = load_yaml(meta_file)
        if not data:
            continue

        proofreading = data.get("proofreading", [])
        if not isinstance(proofreading, list):
            proofreading = []

        lang_data: dict[str, dict] = {}
        for entry in proofreading:
            if not isinstance(entry, dict):
                continue
            lang = entry.get("language", "")
            if not lang:
                continue
            all_languages.add(lang)

            contribs = entry.get("contributor_names", []) or []
            reward = entry.get("reward", 0) or 0
            last_date = entry.get("last_contribution_date", "")
            if last_date and not isinstance(last_date, str):
                last_date = str(last_date)

            status = len(contribs)  # 0, 1, or 2+

            for c in contribs:
                contributors_count[c] = contributors_count.get(c, 0) + 1
                contributors_langs.setdefault(c, set()).add(lang)

            lang_data[lang] = {
                "status": min(status, 2),
                "contributors": list(contribs),
                "reward": float(reward),
                "last_date": last_date or None,
            }

        item_data = {
            "id": folder.name,
            "path": str(folder.relative_to(repo_root)),
            "type": type_key,
            "languages": lang_data,
        }
        by_type.setdefault(type_key, []).append(item_data)

    sorted_langs = sorted(all_languages)
    if "en" in sorted_langs:
        sorted_langs.remove("en")
        sorted_langs.insert(0, "en")

    # Language-level stats
    lang_stats: dict[str, dict] = {}
    for lang in sorted_langs:
        total = 0
        proofread = 0
        complete = 0
        for items in by_type.values():
            for item in items:
                ld = item["languages"].get(lang)
                if ld:
                    total += 1
                    if ld["status"] >= 1:
                        proofread += 1
                    if ld["status"] >= 2:
                        complete += 1
        lang_stats[lang] = {
            "total": total,
            "proofread": proofread,
            "complete": complete,
        }

    # Contributor leaderboard (sorted by count desc)
    leaderboard = sorted(
        [
            {
                "name": name,
                "count": count,
                "languages": sorted(contributors_langs.get(name, set())),
            }
            for name, count in contributors_count.items()
        ],
        key=lambda x: x["count"],
        reverse=True,
    )

    total_items = sum(len(items) for items in by_type.values())
    total_proofread = sum(ls["proofread"] for ls in lang_stats.values())

    return {
        "by_type": by_type,
        "languages": sorted_langs,
        "lang_stats": lang_stats,
        "leaderboard": leaderboard,
        "summary": {
            "total_items": total_items,
            "total_languages": len(sorted_langs),
            "total_proofread": total_proofread,
            "total_contributors": len(contributors_count),
        },
    }


def _generate_proofreading_html(analysis: dict) -> str:
    """Generate self-contained HTML for proofreading dashboard."""
    languages = analysis["languages"]
    by_type = analysis["by_type"]
    lang_stats = analysis["lang_stats"]
    leaderboard = analysis["leaderboard"]
    summary = analysis["summary"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    type_order = ["course", "tutorial"]
    ordered_types = [t for t in type_order if t in by_type]

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proofreading Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{ color: #333; text-align: center; margin-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 5px; }}
        h3 {{ color: #555; margin-top: 25px; }}
        .stats {{
            margin: 20px auto;
            text-align: center;
            font-size: 14px;
            color: #666;
            max-width: 1200px;
        }}
        .stats strong {{ color: #333; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 6px;
            text-align: center;
            font-size: 11px;
        }}
        th {{
            background-color: #FF5722;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.item-header {{
            background-color: #E64A19;
            text-align: left;
            min-width: 100px;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
        .status-complete {{ background-color: #27ae60; color: white; font-weight: bold; }}
        .status-partial {{ background-color: #f39c12; color: white; }}
        .status-none {{ background-color: #e74c3c; color: white; }}
        .status-na {{ background-color: #95a5a6; color: white; }}
        .status-info {{ font-size: 9px; display: block; margin-top: 2px; }}
        .lang-header {{
            writing-mode: vertical-rl;
            text-orientation: mixed;
            min-width: 30px;
            padding: 8px 4px !important;
        }}
        .legend {{
            margin: 20px auto;
            padding: 15px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 900px;
        }}
        .legend h3 {{ margin-top: 0; color: #333; }}
        .legend-item {{ display: inline-block; margin: 5px 15px 5px 0; }}
        .legend-color {{
            display: inline-block;
            width: 20px;
            height: 20px;
            margin-right: 5px;
            vertical-align: middle;
            border-radius: 3px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 20px;
        }}
        .container {{ max-width: 1800px; margin: 0 auto; }}
        .header {{ position: relative; padding: 20px 0; }}
        .back-button {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #f7931a;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-bottom: 20px;
        }}
        .back-button:hover {{ background-color: #e08316; }}
        .back-button::before {{ content: '\\2190 '; }}
        .leaderboard {{ max-width: 800px; margin: 0 auto; }}
        .leaderboard td {{ text-align: left; }}
        .leaderboard td:first-child {{ text-align: center; width: 50px; }}
        .leaderboard td:last-child {{ text-align: center; width: 60px; font-weight: bold; font-size: 16px; }}
        .lang-stats {{ max-width: 1000px; margin: 0 auto; }}
        .lang-stats td {{ text-align: center; }}
        .lang-stats td:first-child {{ text-align: left; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>Proofreading Dashboard</h1>
        </div>
        <div class="stats">
            <strong>Content items:</strong> {summary["total_items"]} |
            <strong>Languages:</strong> {summary["total_languages"]} |
            <strong>Proofread entries:</strong> {summary["total_proofread"]} |
            <strong>Contributors:</strong> {summary["total_contributors"]}
        </div>

        <div class="legend">
            <h3>Legend</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #27ae60;"></span>
                <span>Complete (2+ contributors)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #f39c12;"></span>
                <span>Partial (1 contributor)</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #e74c3c;"></span>
                <span>No proofreading</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #95a5a6;"></span>
                <span>N/A</span>
            </div>
        </div>"""]

    # Matrix views per type
    for type_key in ordered_types:
        items = sorted(by_type[type_key], key=lambda x: x["id"])
        type_name = type_key.capitalize()

        html_parts.append(f"""
        <h2>{type_name}s ({len(items)} items)</h2>
        <table>
            <thead>
                <tr>
                    <th class="item-header">{type_name}</th>""")

        for lang in languages:
            html_parts.append(f"                    <th class='lang-header'>{lang}</th>\n")

        html_parts.append("""                </tr>
            </thead>
            <tbody>""")

        for item in items:
            html_parts.append(f"""
                <tr>
                    <td style='text-align: left; font-weight: bold;'>{item["id"]}</td>""")

            for lang in languages:
                ld = item["languages"].get(lang)
                if not ld:
                    html_parts.append("""
                    <td class='status-na'>-</td>""")
                else:
                    s = ld["status"]
                    if s >= 2:
                        css = "status-complete"
                    elif s == 1:
                        css = "status-partial"
                    else:
                        css = "status-none"
                    n = len(ld["contributors"])
                    html_parts.append(f"""
                    <td class='{css}'>
                        {n}
                        <span class='status-info'>{", ".join(ld["contributors"][:2]) if ld["contributors"] else "-"}</span>
                    </td>""")

            html_parts.append("\n                </tr>")

        html_parts.append("""
            </tbody>
        </table>""")

    # Language statistics
    html_parts.append("""
        <h2>Language Statistics</h2>
        <table class="lang-stats">
            <thead>
                <tr>
                    <th style="text-align: left;">Language</th>
                    <th>Items</th>
                    <th>Proofread</th>
                    <th>Complete</th>
                </tr>
            </thead>
            <tbody>""")

    for lang in languages:
        ls = lang_stats[lang]
        html_parts.append(f"""
                <tr>
                    <td>{lang}</td>
                    <td>{ls["total"]}</td>
                    <td>{ls["proofread"]}</td>
                    <td>{ls["complete"]}</td>
                </tr>""")

    html_parts.append("""
            </tbody>
        </table>""")

    # Contributor leaderboard
    html_parts.append("""
        <h2>Contributor Leaderboard</h2>
        <table class="leaderboard">
            <thead>
                <tr>
                    <th>#</th>
                    <th style="text-align: left;">Contributor</th>
                    <th style="text-align: left;">Languages</th>
                    <th>Count</th>
                </tr>
            </thead>
            <tbody>""")

    for i, entry in enumerate(leaderboard[:50], 1):
        html_parts.append(f"""
                <tr>
                    <td>{i}</td>
                    <td>{entry["name"]}</td>
                    <td>{", ".join(entry["languages"])}</td>
                    <td>{entry["count"]}</td>
                </tr>""")

    html_parts.append(f"""
            </tbody>
        </table>

        <div class="footer">
            Generated on {now}<br>
            Run <code>bec report proofreading</code> to update this report
        </div>
    </div>
</body>
</html>
""")

    return "".join(html_parts)


def _proofreading_to_json(analysis: dict) -> dict:
    """Convert proofreading analysis to JSON-serializable output."""
    return {
        "summary": analysis["summary"],
        "languages": analysis["languages"],
        "lang_stats": analysis["lang_stats"],
        "leaderboard": analysis["leaderboard"],
        "items": {
            type_key: [
                {
                    "id": item["id"],
                    "path": item["path"],
                    "type": item["type"],
                    "languages": item["languages"],
                }
                for item in sorted(items, key=lambda x: x["id"])
            ]
            for type_key, items in analysis["by_type"].items()
        },
    }


def run_report_proofreading(
    output: str | None,
    json_output: bool,
) -> None:
    """Generate proofreading dashboard report."""
    repo_root = find_repo_root()
    registry = load_registry(repo_root)

    if not json_output:
        click.echo("Analyzing proofreading status...", err=True)
    analysis = analyze_proofreading(repo_root, registry)

    if json_output:
        click.echo(json.dumps(_proofreading_to_json(analysis), indent=2))
        return

    output_dir = Path(output) if output else repo_root / "docs" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "proofreading_dashboard.html"

    html = _generate_proofreading_html(analysis)
    output_file.write_text(html, encoding="utf-8")

    click.echo(f"Report generated: {output_file}")
    s = analysis["summary"]
    click.echo(
        f"  {s['total_proofread']} proofread entries across {s['total_languages']} languages, "
        f"{s['total_contributors']} contributors"
    )


# ===========================================================================
# Phase 13: Course analytics report
# ===========================================================================

_TAG_RE = re.compile(r"<[^>]+>")
_IMG_RE_CLEAN = re.compile(r"!\[.*?\]\(.*?\)")
_LINK_RE = re.compile(r"\[([^\]]*)\]\([^\)]*\)")
_CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]+`")
_HEADING_MARKER_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
_BOLD_ITALIC_RE = re.compile(r"[*_]{1,3}")
_URL_RE = re.compile(r"https?://\S+")
_CHAPTER_ID_RE = re.compile(r"<chapterId>(.*?)</chapterId>")
_PART_ID_RE = re.compile(r"<partId>(.*?)</partId>")


def _clean_text(text: str) -> str:
    """Remove markdown formatting, tags, links, etc. to get plain text."""
    t = _CODE_BLOCK_RE.sub("", text)
    t = _INLINE_CODE_RE.sub("", t)
    t = _TAG_RE.sub("", t)
    t = _IMG_RE_CLEAN.sub("", t)
    t = _LINK_RE.sub(r"\1", t)
    t = _HEADING_MARKER_RE.sub("", t)
    t = _BOLD_ITALIC_RE.sub("", t)
    t = _URL_RE.sub("", t)
    return t


def _count_content_words(text: str) -> int:
    """Count words in cleaned text."""
    return len(_clean_text(text).split())


def _parse_course_structure(content: str) -> dict:
    """Parse a course markdown file into parts and chapters with metrics.

    Returns:
        {
            "intro_words": int,
            "parts": [{"name": str, "chapters": [{"name": str, "words": int}]}],
        }
    """
    # Split frontmatter
    parts_raw = content.split("---", 2)
    if len(parts_raw) >= 3:
        body = parts_raw[2]
    else:
        body = content

    # Split on +++ separator
    sections = body.split("+++")
    intro_text = sections[0] if sections else ""
    intro_words = _count_content_words(intro_text)

    parts: list[dict] = []

    # Process remaining sections (each starts after a +++ separator)
    for section in sections[1:]:
        lines = section.strip().split("\n")
        part_name = ""
        chapters: list[dict] = []
        current_chapter_name = ""
        current_chapter_lines: list[str] = []

        for line in lines:
            stripped = line.strip()

            # Part title: # heading (level 1)
            if stripped.startswith("# ") and not stripped.startswith("## "):
                part_name = stripped[2:].strip()
                continue

            # Chapter title: ## heading
            if stripped.startswith("## "):
                # Save previous chapter
                if current_chapter_name:
                    chapter_text = "\n".join(current_chapter_lines)
                    chapters.append({
                        "name": current_chapter_name,
                        "words": _count_content_words(chapter_text),
                    })
                current_chapter_name = stripped[3:].strip()
                current_chapter_lines = []
                continue

            current_chapter_lines.append(line)

        # Save last chapter
        if current_chapter_name:
            chapter_text = "\n".join(current_chapter_lines)
            chapters.append({
                "name": current_chapter_name,
                "words": _count_content_words(chapter_text),
            })

        if part_name or chapters:
            parts.append({
                "name": part_name or "(untitled part)",
                "chapters": chapters,
            })

    return {
        "intro_words": intro_words,
        "parts": parts,
    }


def analyze_course_analytics(repo_root: Path) -> dict:
    """Analyze course structure statistics: word counts, chapters, parts, quizzes."""
    courses_dir = repo_root / "courses"
    if not courses_dir.is_dir():
        return {"courses": [], "summary": {}, "aggregated": {}}

    courses: list[dict] = []

    for course_dir in sorted(courses_dir.iterdir()):
        if not course_dir.is_dir() or course_dir.name.startswith("."):
            continue

        course_id = course_dir.name

        # Find primary language file (prefer en, then fr, then first found)
        md_file = None
        lang = None
        for try_lang in ["en", "fr"]:
            candidate = course_dir / f"{try_lang}.md"
            if candidate.is_file():
                md_file = candidate
                lang = try_lang
                break
        if not md_file:
            for f in sorted(course_dir.iterdir()):
                if f.is_file() and f.suffix == ".md":
                    md_file = f
                    lang = f.stem
                    break
        if not md_file:
            continue

        content = md_file.read_text(encoding="utf-8")
        structure = _parse_course_structure(content)

        # Count quizzes
        quiz_dir = course_dir / "quizz"
        quiz_count = 0
        if quiz_dir.is_dir():
            quiz_count = sum(
                1 for d in quiz_dir.iterdir()
                if d.is_dir() and not d.name.startswith(".")
            )

        # Count language files
        lang_files = [
            f.stem for f in course_dir.iterdir()
            if f.is_file() and f.suffix == ".md"
        ]

        part_count = len(structure["parts"])
        chapter_count = sum(len(p["chapters"]) for p in structure["parts"])
        total_words = structure["intro_words"] + sum(
            ch["words"]
            for p in structure["parts"]
            for ch in p["chapters"]
        )

        words_per_chapter = [
            ch["words"]
            for p in structure["parts"]
            for ch in p["chapters"]
        ]

        chapters_per_part = [len(p["chapters"]) for p in structure["parts"]]

        courses.append({
            "id": course_id,
            "language": lang,
            "parts": part_count,
            "chapters": chapter_count,
            "total_words": total_words,
            "intro_words": structure["intro_words"],
            "quizzes": quiz_count,
            "languages": sorted(lang_files),
            "words_per_chapter": words_per_chapter,
            "chapters_per_part": chapters_per_part,
            "parts_detail": [
                {
                    "name": p["name"],
                    "chapters": len(p["chapters"]),
                    "words": sum(ch["words"] for ch in p["chapters"]),
                }
                for p in structure["parts"]
            ],
        })

    # Aggregated stats
    def _stats(values: list[int | float]) -> dict:
        if not values:
            return {"count": 0, "mean": 0, "min": 0, "max": 0, "sum": 0}
        from statistics import mean, median
        return {
            "count": len(values),
            "mean": round(mean(values), 1),
            "median": round(median(values), 1),
            "min": min(values),
            "max": max(values),
            "sum": sum(values),
        }

    all_words = [c["total_words"] for c in courses]
    all_chapters = [c["chapters"] for c in courses]
    all_parts = [c["parts"] for c in courses]
    all_quizzes = [c["quizzes"] for c in courses]
    all_words_per_ch = [w for c in courses for w in c["words_per_chapter"]]
    all_ch_per_part = [n for c in courses for n in c["chapters_per_part"]]

    aggregated = {
        "words_per_course": _stats(all_words),
        "chapters_per_course": _stats(all_chapters),
        "parts_per_course": _stats(all_parts),
        "quizzes_per_course": _stats(all_quizzes),
        "words_per_chapter": _stats(all_words_per_ch),
        "chapters_per_part": _stats(all_ch_per_part),
    }

    return {
        "courses": courses,
        "summary": {
            "total_courses": len(courses),
            "total_parts": sum(c["parts"] for c in courses),
            "total_chapters": sum(c["chapters"] for c in courses),
            "total_words": sum(c["total_words"] for c in courses),
            "total_quizzes": sum(c["quizzes"] for c in courses),
        },
        "aggregated": aggregated,
    }


def _generate_analytics_html(analysis: dict) -> str:
    """Generate self-contained HTML for course analytics report."""
    courses = analysis["courses"]
    summary = analysis["summary"]
    aggregated = analysis["aggregated"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Analytics Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{ color: #333; text-align: center; margin-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 30px; border-bottom: 2px solid #ddd; padding-bottom: 5px; }}
        .stats {{
            margin: 20px auto;
            text-align: center;
            font-size: 14px;
            color: #666;
            max-width: 1200px;
        }}
        .stats strong {{ color: #333; }}
        .summary-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 20px auto;
            max-width: 1200px;
            justify-content: center;
        }}
        .summary-card {{
            background: white;
            border-radius: 8px;
            padding: 15px 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            min-width: 140px;
            text-align: center;
        }}
        .summary-card h4 {{ margin: 0 0 5px 0; color: #333; font-size: 12px; }}
        .summary-card .value {{ font-size: 28px; font-weight: bold; color: #f7931a; }}
        table {{
            border-collapse: collapse;
            width: 100%;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
            font-size: 12px;
        }}
        th {{
            background-color: #3F51B5;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        th.name-header {{
            background-color: #303F9F;
            text-align: left;
            min-width: 100px;
        }}
        tr:hover {{ background-color: #f5f5f5; }}
        .agg-table {{ max-width: 900px; margin: 20px auto; }}
        .agg-table th {{ background-color: #455A64; }}
        .agg-table td:first-child {{ text-align: left; font-weight: bold; }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            color: #666;
            font-size: 12px;
            padding: 20px;
        }}
        .container {{ max-width: 1600px; margin: 0 auto; }}
        .header {{ position: relative; padding: 20px 0; }}
        .back-button {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #f7931a;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            transition: background-color 0.2s;
            margin-bottom: 20px;
        }}
        .back-button:hover {{ background-color: #e08316; }}
        .back-button::before {{ content: '\\2190 '; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="https://surfer.planb.network/translation_report/index.html" class="back-button">Back to Reports</a>
            <h1>Course Analytics Report</h1>
        </div>

        <div class="summary-grid">
            <div class="summary-card">
                <h4>Courses</h4>
                <div class="value">{summary["total_courses"]}</div>
            </div>
            <div class="summary-card">
                <h4>Parts</h4>
                <div class="value">{summary["total_parts"]}</div>
            </div>
            <div class="summary-card">
                <h4>Chapters</h4>
                <div class="value">{summary["total_chapters"]}</div>
            </div>
            <div class="summary-card">
                <h4>Words</h4>
                <div class="value">{summary["total_words"]:,}</div>
            </div>
            <div class="summary-card">
                <h4>Quizzes</h4>
                <div class="value">{summary["total_quizzes"]}</div>
            </div>
        </div>

        <h2>Aggregated Statistics</h2>
        <table class="agg-table">
            <thead>
                <tr>
                    <th style="text-align: left;">Metric</th>
                    <th>Count</th>
                    <th>Mean</th>
                    <th>Median</th>
                    <th>Min</th>
                    <th>Max</th>
                    <th>Sum</th>
                </tr>
            </thead>
            <tbody>"""]

    metric_labels = {
        "words_per_course": "Words per Course",
        "chapters_per_course": "Chapters per Course",
        "parts_per_course": "Parts per Course",
        "quizzes_per_course": "Quizzes per Course",
        "words_per_chapter": "Words per Chapter",
        "chapters_per_part": "Chapters per Part",
    }

    for key, label in metric_labels.items():
        s = aggregated.get(key, {})
        html_parts.append(f"""
                <tr>
                    <td>{label}</td>
                    <td>{s.get("count", 0)}</td>
                    <td>{s.get("mean", 0)}</td>
                    <td>{s.get("median", 0)}</td>
                    <td>{s.get("min", 0)}</td>
                    <td>{s.get("max", 0)}</td>
                    <td>{s.get("sum", 0):,}</td>
                </tr>""")

    html_parts.append("""
            </tbody>
        </table>

        <h2>Course Details</h2>
        <table>
            <thead>
                <tr>
                    <th class="name-header">Course</th>
                    <th>Lang</th>
                    <th>Parts</th>
                    <th>Chapters</th>
                    <th>Words</th>
                    <th>Quizzes</th>
                    <th>Languages</th>
                </tr>
            </thead>
            <tbody>""")

    for c in courses:
        html_parts.append(f"""
                <tr>
                    <td style='text-align: left; font-weight: bold;'>{c["id"]}</td>
                    <td>{c["language"]}</td>
                    <td>{c["parts"]}</td>
                    <td>{c["chapters"]}</td>
                    <td>{c["total_words"]:,}</td>
                    <td>{c["quizzes"]}</td>
                    <td>{len(c["languages"])}</td>
                </tr>""")

    html_parts.append(f"""
            </tbody>
        </table>

        <div class="footer">
            Generated on {now}<br>
            Run <code>bec report analytics</code> to update this report
        </div>
    </div>
</body>
</html>
""")

    return "".join(html_parts)


def _analytics_to_json(analysis: dict) -> dict:
    """Convert course analytics to JSON-serializable output."""
    return {
        "summary": analysis["summary"],
        "aggregated": analysis["aggregated"],
        "courses": [
            {
                "id": c["id"],
                "language": c["language"],
                "parts": c["parts"],
                "chapters": c["chapters"],
                "total_words": c["total_words"],
                "intro_words": c["intro_words"],
                "quizzes": c["quizzes"],
                "languages": c["languages"],
                "words_per_chapter": c["words_per_chapter"],
                "chapters_per_part": c["chapters_per_part"],
                "parts_detail": c["parts_detail"],
            }
            for c in analysis["courses"]
        ],
    }


def run_report_analytics(
    output: str | None,
    json_output: bool,
) -> None:
    """Generate course analytics report."""
    repo_root = find_repo_root()

    if not json_output:
        click.echo("Analyzing course structure...", err=True)
    analysis = analyze_course_analytics(repo_root)

    if json_output:
        click.echo(json.dumps(_analytics_to_json(analysis), indent=2))
        return

    output_dir = Path(output) if output else repo_root / "docs" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "course_analytics_report.html"

    html = _generate_analytics_html(analysis)
    output_file.write_text(html, encoding="utf-8")

    click.echo(f"Report generated: {output_file}")
    s = analysis["summary"]
    click.echo(
        f"  {s['total_courses']} courses, {s['total_chapters']} chapters, "
        f"{s['total_words']:,} words, {s['total_quizzes']} quizzes"
    )
