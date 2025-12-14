#!/usr/bin/env python3
"""
Course Analytics Script
Analyzes Bitcoin Educational Content courses and generates an HTML report.

Metrics extracted:
- Number of parts per course
- Number of chapters per course/part
- Number of subsections (###) per chapter
- Word counts at various levels
- Statistical measures (mean, std, median)
"""

import os
import re
import json
import statistics
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class ChapterMetrics:
    """Metrics for a single chapter."""
    name: str
    word_count: int
    subsection_count: int  # Number of ### headers
    paragraph_count: int
    sentence_count: int


@dataclass
class PartMetrics:
    """Metrics for a single part."""
    name: str
    chapters: list[ChapterMetrics] = field(default_factory=list)

    @property
    def chapter_count(self) -> int:
        return len(self.chapters)

    @property
    def total_words(self) -> int:
        return sum(c.word_count for c in self.chapters)

    @property
    def total_subsections(self) -> int:
        return sum(c.subsection_count for c in self.chapters)

    @property
    def total_paragraphs(self) -> int:
        return sum(c.paragraph_count for c in self.chapters)

    @property
    def total_sentences(self) -> int:
        return sum(c.sentence_count for c in self.chapters)


@dataclass
class CourseMetrics:
    """Metrics for a single course."""
    course_id: str
    language: str
    parts: list[PartMetrics] = field(default_factory=list)
    intro_word_count: int = 0

    @property
    def part_count(self) -> int:
        return len(self.parts)

    @property
    def chapter_count(self) -> int:
        return sum(p.chapter_count for p in self.parts)

    @property
    def total_words(self) -> int:
        return self.intro_word_count + sum(p.total_words for p in self.parts)

    @property
    def total_subsections(self) -> int:
        return sum(p.total_subsections for p in self.parts)

    @property
    def total_paragraphs(self) -> int:
        return sum(p.total_paragraphs for p in self.parts)

    @property
    def total_sentences(self) -> int:
        return sum(p.total_sentences for p in self.parts)

    @property
    def words_per_chapter(self) -> list[int]:
        return [c.word_count for p in self.parts for c in p.chapters]

    @property
    def chapters_per_part(self) -> list[int]:
        return [p.chapter_count for p in self.parts]

    @property
    def subsections_per_chapter(self) -> list[int]:
        return [c.subsection_count for p in self.parts for c in p.chapters]

    @property
    def paragraphs_per_chapter(self) -> list[int]:
        return [c.paragraph_count for p in self.parts for c in p.chapters]

    @property
    def sentences_per_chapter(self) -> list[int]:
        return [c.sentence_count for p in self.parts for c in p.chapters]


def clean_text_for_analysis(text: str) -> str:
    """Clean markdown text for analysis, removing syntax elements."""
    # Remove HTML-like tags (partId, chapterId, etc.)
    text = re.sub(r'<[^>]+>', '', text)
    # Remove image references
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    # Remove links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '', text)
    # Remove markdown headers markers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r'\*{1,2}([^*]+)\*{1,2}', r'\1', text)
    text = re.sub(r'_{1,2}([^_]+)_{1,2}', r'\1', text)
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    return text


def count_words(text: str) -> int:
    """Count words in text, excluding markdown syntax and HTML tags."""
    cleaned = clean_text_for_analysis(text)
    words = cleaned.split()
    return len(words)


def count_paragraphs(text: str) -> int:
    """Count paragraphs in text (blocks separated by blank lines)."""
    # Clean the text first
    cleaned = clean_text_for_analysis(text)
    # Split by double newlines (paragraph separator)
    # A paragraph is text separated by one or more blank lines
    paragraphs = re.split(r'\n\s*\n', cleaned)
    # Filter out empty paragraphs and those that are just whitespace
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    # Filter out very short "paragraphs" that are likely just headers or list markers
    paragraphs = [p for p in paragraphs if len(p.split()) >= 3]
    return len(paragraphs)


def count_sentences(text: str) -> int:
    """Count sentences in text using punctuation-based heuristics."""
    cleaned = clean_text_for_analysis(text)
    # Remove list markers and bullet points
    cleaned = re.sub(r'^\s*[-*•]\s*', '', cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r'^\s*\d+\.\s*', '', cleaned, flags=re.MULTILINE)

    # Sentence endings: . ! ? followed by space or end of string
    # But avoid counting abbreviations like "e.g.", "i.e.", "Dr.", "Mr.", etc.
    # Simple approach: count sentence-ending punctuation followed by space + capital or end

    # First, normalize multiple spaces
    cleaned = re.sub(r'\s+', ' ', cleaned)

    # Count sentences by splitting on sentence-ending punctuation
    # This regex matches . ! ? that end sentences (not abbreviations)
    sentences = re.split(r'[.!?]+(?:\s|$)', cleaned)
    # Filter out empty strings and very short fragments
    sentences = [s.strip() for s in sentences if s.strip() and len(s.split()) >= 2]

    return max(len(sentences), 1) if cleaned.strip() else 0


def parse_course_file(filepath: Path) -> Optional[CourseMetrics]:
    """Parse a course markdown file and extract metrics."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

    course_id = filepath.parent.name
    language = filepath.stem

    metrics = CourseMetrics(course_id=course_id, language=language)

    # Split by +++ to separate intro from main content
    if '+++' in content:
        parts = content.split('+++', 1)
        intro = parts[0]
        main_content = parts[1] if len(parts) > 1 else ""
        # Remove YAML frontmatter from intro
        if intro.strip().startswith('---'):
            intro_parts = intro.split('---', 2)
            if len(intro_parts) >= 3:
                intro = intro_parts[2]
        metrics.intro_word_count = count_words(intro)
    else:
        main_content = content
        # Try to remove YAML frontmatter
        if content.strip().startswith('---'):
            content_parts = content.split('---', 2)
            if len(content_parts) >= 3:
                main_content = content_parts[2]

    # Parse parts and chapters
    # Parts are marked by "# Title" followed by <partId>
    # Chapters are marked by "## Title" followed by <chapterId>

    # Split content by part headers
    part_pattern = r'\n#\s+([^\n]+)\n+<partId>[^<]+</partId>'
    chapter_pattern = r'\n##\s+([^\n]+)\n+<chapterId>[^<]+</chapterId>'
    subsection_pattern = r'\n###\s+[^\n]+'

    # Find all parts
    part_matches = list(re.finditer(part_pattern, main_content))

    if not part_matches:
        # No parts found, treat entire content as single implicit part
        part = PartMetrics(name="Main Content")
        chapter_matches = list(re.finditer(chapter_pattern, main_content))

        for i, match in enumerate(chapter_matches):
            chapter_name = match.group(1).strip()
            start = match.end()
            end = chapter_matches[i + 1].start() if i + 1 < len(chapter_matches) else len(main_content)
            chapter_content = main_content[start:end]

            subsection_count = len(re.findall(subsection_pattern, chapter_content))
            word_count = count_words(chapter_content)
            paragraph_count = count_paragraphs(chapter_content)
            sentence_count = count_sentences(chapter_content)

            part.chapters.append(ChapterMetrics(
                name=chapter_name,
                word_count=word_count,
                subsection_count=subsection_count,
                paragraph_count=paragraph_count,
                sentence_count=sentence_count
            ))

        if part.chapters:
            metrics.parts.append(part)
    else:
        # Process each part
        for i, part_match in enumerate(part_matches):
            part_name = part_match.group(1).strip()
            part = PartMetrics(name=part_name)

            part_start = part_match.end()
            part_end = part_matches[i + 1].start() if i + 1 < len(part_matches) else len(main_content)
            part_content = main_content[part_start:part_end]

            # Find chapters within this part
            chapter_matches = list(re.finditer(chapter_pattern, '\n' + part_content))

            for j, ch_match in enumerate(chapter_matches):
                chapter_name = ch_match.group(1).strip()
                ch_start = ch_match.end()
                ch_end = chapter_matches[j + 1].start() if j + 1 < len(chapter_matches) else len(part_content) + 1
                chapter_content = ('\n' + part_content)[ch_start:ch_end]

                subsection_count = len(re.findall(subsection_pattern, chapter_content))
                word_count = count_words(chapter_content)
                paragraph_count = count_paragraphs(chapter_content)
                sentence_count = count_sentences(chapter_content)

                part.chapters.append(ChapterMetrics(
                    name=chapter_name,
                    word_count=word_count,
                    subsection_count=subsection_count,
                    paragraph_count=paragraph_count,
                    sentence_count=sentence_count
                ))

            metrics.parts.append(part)

    return metrics


def find_course_file(course_dir: Path) -> Optional[Path]:
    """Find the best course file (en.md preferred, then fr.md)."""
    en_file = course_dir / "en.md"
    fr_file = course_dir / "fr.md"

    if en_file.exists():
        return en_file
    elif fr_file.exists():
        return fr_file
    return None


def calculate_stats(values: list[int | float]) -> dict:
    """Calculate statistical measures for a list of values."""
    if not values:
        return {"count": 0, "mean": 0, "std": 0, "median": 0, "min": 0, "max": 0, "sum": 0}

    return {
        "count": len(values),
        "mean": round(statistics.mean(values), 2),
        "std": round(statistics.stdev(values), 2) if len(values) > 1 else 0,
        "median": round(statistics.median(values), 2),
        "min": min(values),
        "max": max(values),
        "sum": sum(values)
    }


def analyze_courses(courses_dir: Path) -> dict:
    """Analyze all courses and return aggregated metrics."""
    all_courses: list[CourseMetrics] = []

    for item in sorted(courses_dir.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            course_file = find_course_file(item)
            if course_file:
                metrics = parse_course_file(course_file)
                if metrics and metrics.part_count > 0:
                    all_courses.append(metrics)
                    print(f"✓ Parsed {metrics.course_id} ({metrics.language}): {metrics.part_count} parts, {metrics.chapter_count} chapters, {metrics.total_words} words")

    # Aggregate metrics
    all_parts_per_course = [c.part_count for c in all_courses]
    all_chapters_per_course = [c.chapter_count for c in all_courses]
    all_words_per_course = [c.total_words for c in all_courses]
    all_subsections_per_course = [c.total_subsections for c in all_courses]
    all_paragraphs_per_course = [c.total_paragraphs for c in all_courses]
    all_sentences_per_course = [c.total_sentences for c in all_courses]

    all_chapters_per_part = [cp for c in all_courses for cp in c.chapters_per_part]
    all_words_per_chapter = [w for c in all_courses for w in c.words_per_chapter]
    all_subsections_per_chapter = [s for c in all_courses for s in c.subsections_per_chapter]
    all_paragraphs_per_chapter = [p for c in all_courses for p in c.paragraphs_per_chapter]
    all_sentences_per_chapter = [s for c in all_courses for s in c.sentences_per_chapter]

    return {
        "generated_at": datetime.now().isoformat(),
        "total_courses": len(all_courses),
        "courses": [
            {
                "id": c.course_id,
                "language": c.language,
                "parts": c.part_count,
                "chapters": c.chapter_count,
                "total_words": c.total_words,
                "total_subsections": c.total_subsections,
                "total_paragraphs": c.total_paragraphs,
                "total_sentences": c.total_sentences,
                "intro_words": c.intro_word_count,
                "chapters_per_part": c.chapters_per_part,
                "words_per_chapter": c.words_per_chapter,
                "subsections_per_chapter": c.subsections_per_chapter,
                "paragraphs_per_chapter": c.paragraphs_per_chapter,
                "sentences_per_chapter": c.sentences_per_chapter,
                "parts_detail": [
                    {
                        "name": p.name,
                        "chapters": p.chapter_count,
                        "words": p.total_words,
                        "subsections": p.total_subsections,
                        "paragraphs": p.total_paragraphs,
                        "sentences": p.total_sentences
                    }
                    for p in c.parts
                ]
            }
            for c in all_courses
        ],
        "aggregated": {
            "parts_per_course": calculate_stats(all_parts_per_course),
            "chapters_per_course": calculate_stats(all_chapters_per_course),
            "words_per_course": calculate_stats(all_words_per_course),
            "subsections_per_course": calculate_stats(all_subsections_per_course),
            "paragraphs_per_course": calculate_stats(all_paragraphs_per_course),
            "sentences_per_course": calculate_stats(all_sentences_per_course),
            "chapters_per_part": calculate_stats(all_chapters_per_part),
            "words_per_chapter": calculate_stats(all_words_per_chapter),
            "subsections_per_chapter": calculate_stats(all_subsections_per_chapter),
            "paragraphs_per_chapter": calculate_stats(all_paragraphs_per_chapter),
            "sentences_per_chapter": calculate_stats(all_sentences_per_chapter)
        },
        "distributions": {
            "parts_per_course": all_parts_per_course,
            "chapters_per_course": all_chapters_per_course,
            "words_per_course": all_words_per_course,
            "chapters_per_part": all_chapters_per_part,
            "words_per_chapter": all_words_per_chapter,
            "subsections_per_chapter": all_subsections_per_chapter,
            "paragraphs_per_course": all_paragraphs_per_course,
            "sentences_per_course": all_sentences_per_course,
            "paragraphs_per_chapter": all_paragraphs_per_chapter,
            "sentences_per_chapter": all_sentences_per_chapter
        }
    }


def generate_html_report(data: dict) -> str:
    """Generate a standalone HTML report with embedded data and charts."""

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Analytics Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {{
            --primary: #f7931a;
            --secondary: #4d4d4d;
            --bg-dark: #1a1a2e;
            --bg-card: #16213e;
            --text: #eaeaea;
            --text-muted: #a0a0a0;
            --border: #0f3460;
            --success: #00d26a;
            --warning: #f7931a;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-dark);
            color: var(--text);
            line-height: 1.6;
            padding: 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            padding: 40px 20px;
            margin-bottom: 30px;
            background: linear-gradient(135deg, var(--bg-card), var(--border));
            border-radius: 16px;
            border: 1px solid var(--border);
        }}

        h1 {{
            color: var(--primary);
            font-size: 2.5rem;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1.1rem;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}

        .stat-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 25px rgba(247, 147, 26, 0.15);
        }}

        .stat-value {{
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 8px;
        }}

        .stat-label {{
            color: var(--text-muted);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .section {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
        }}

        .section h2 {{
            color: var(--primary);
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--border);
        }}

        .chart-container {{
            position: relative;
            height: 350px;
            margin: 20px 0;
        }}

        .chart-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
        }}

        .chart-box {{
            background: rgba(15, 52, 96, 0.3);
            border-radius: 12px;
            padding: 20px;
        }}

        .chart-box h3 {{
            color: var(--text);
            margin-bottom: 15px;
            font-size: 1.1rem;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}

        th, td {{
            padding: 14px 16px;
            text-align: center;
            border-bottom: 1px solid var(--border);
        }}

        th {{
            background: var(--border);
            color: var(--primary);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
        }}

        tr:hover td {{
            background: rgba(247, 147, 26, 0.05);
        }}

        .metric-table {{
            margin-top: 20px;
        }}

        .metric-table td:first-child {{
            text-align: left;
        }}

        .metric-table td:not(:first-child) {{
            text-align: center;
            font-family: 'Consolas', monospace;
        }}

        /* Sortable table styles */
        .sortable th {{
            cursor: pointer;
            user-select: none;
            position: relative;
            padding-right: 25px;
        }}

        .sortable th:hover {{
            background: rgba(247, 147, 26, 0.2);
        }}

        .sortable th::after {{
            content: '⇅';
            position: absolute;
            right: 8px;
            opacity: 0.4;
            font-size: 0.8rem;
        }}

        .sortable th.sort-asc::after {{
            content: '↑';
            opacity: 1;
        }}

        .sortable th.sort-desc::after {{
            content: '↓';
            opacity: 1;
        }}

        #courseTable td:first-child {{
            text-align: left;
        }}

        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }}

        .badge-en {{
            background: #2e7d32;
            color: white;
        }}

        .badge-fr {{
            background: #1565c0;
            color: white;
        }}

        .progress-bar {{
            height: 8px;
            background: var(--border);
            border-radius: 4px;
            overflow: hidden;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--success));
            border-radius: 4px;
            transition: width 0.3s;
        }}

        footer {{
            text-align: center;
            padding: 30px;
            color: var(--text-muted);
            font-size: 0.9rem;
        }}

        .tabs {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--border);
            padding-bottom: 10px;
        }}

        .tab {{
            padding: 10px 20px;
            background: transparent;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            border-radius: 8px 8px 0 0;
            font-size: 1rem;
            transition: all 0.2s;
        }}

        .tab:hover {{
            color: var(--text);
            background: rgba(247, 147, 26, 0.1);
        }}

        .tab.active {{
            color: var(--primary);
            background: var(--border);
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        .highlight {{
            color: var(--primary);
            font-weight: 600;
        }}

        @media (max-width: 768px) {{
            h1 {{
                font-size: 1.8rem;
            }}

            .chart-row {{
                grid-template-columns: 1fr;
            }}

            .stats-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}

            table {{
                font-size: 0.85rem;
            }}

            th, td {{
                padding: 10px 8px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Course Analytics Report</h1>
            <p class="subtitle">Bitcoin Educational Content Analysis</p>
            <p class="subtitle" style="margin-top: 10px; font-size: 0.9rem;">
                Generated: {data['generated_at'][:19].replace('T', ' ')}
            </p>
        </header>

        <!-- Summary Stats -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{data['total_courses']}</div>
                <div class="stat-label">Total Courses</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{data['aggregated']['parts_per_course']['sum']}</div>
                <div class="stat-label">Total Parts</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{data['aggregated']['chapters_per_course']['sum']}</div>
                <div class="stat-label">Total Chapters</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{data['aggregated']['words_per_course']['sum']:,}</div>
                <div class="stat-label">Total Words</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{data['aggregated']['paragraphs_per_course']['sum']:,}</div>
                <div class="stat-label">Total Paragraphs</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{data['aggregated']['sentences_per_course']['sum']:,}</div>
                <div class="stat-label">Total Sentences</div>
            </div>
        </div>

        <!-- Aggregated Statistics -->
        <div class="section">
            <h2>📈 Aggregated Statistics</h2>
            <table class="metric-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Count</th>
                        <th>Mean</th>
                        <th>Std Dev</th>
                        <th>Median</th>
                        <th>Min</th>
                        <th>Max</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Parts per Course</td>
                        <td>{data['aggregated']['parts_per_course']['count']}</td>
                        <td>{data['aggregated']['parts_per_course']['mean']}</td>
                        <td>{data['aggregated']['parts_per_course']['std']}</td>
                        <td>{data['aggregated']['parts_per_course']['median']}</td>
                        <td>{data['aggregated']['parts_per_course']['min']}</td>
                        <td>{data['aggregated']['parts_per_course']['max']}</td>
                    </tr>
                    <tr>
                        <td>Chapters per Course</td>
                        <td>{data['aggregated']['chapters_per_course']['count']}</td>
                        <td>{data['aggregated']['chapters_per_course']['mean']}</td>
                        <td>{data['aggregated']['chapters_per_course']['std']}</td>
                        <td>{data['aggregated']['chapters_per_course']['median']}</td>
                        <td>{data['aggregated']['chapters_per_course']['min']}</td>
                        <td>{data['aggregated']['chapters_per_course']['max']}</td>
                    </tr>
                    <tr>
                        <td>Chapters per Part</td>
                        <td>{data['aggregated']['chapters_per_part']['count']}</td>
                        <td>{data['aggregated']['chapters_per_part']['mean']}</td>
                        <td>{data['aggregated']['chapters_per_part']['std']}</td>
                        <td>{data['aggregated']['chapters_per_part']['median']}</td>
                        <td>{data['aggregated']['chapters_per_part']['min']}</td>
                        <td>{data['aggregated']['chapters_per_part']['max']}</td>
                    </tr>
                    <tr>
                        <td>Subsections (###) per Chapter</td>
                        <td>{data['aggregated']['subsections_per_chapter']['count']}</td>
                        <td>{data['aggregated']['subsections_per_chapter']['mean']}</td>
                        <td>{data['aggregated']['subsections_per_chapter']['std']}</td>
                        <td>{data['aggregated']['subsections_per_chapter']['median']}</td>
                        <td>{data['aggregated']['subsections_per_chapter']['min']}</td>
                        <td>{data['aggregated']['subsections_per_chapter']['max']}</td>
                    </tr>
                    <tr>
                        <td>Words per Chapter</td>
                        <td>{data['aggregated']['words_per_chapter']['count']}</td>
                        <td>{data['aggregated']['words_per_chapter']['mean']}</td>
                        <td>{data['aggregated']['words_per_chapter']['std']}</td>
                        <td>{data['aggregated']['words_per_chapter']['median']}</td>
                        <td>{data['aggregated']['words_per_chapter']['min']}</td>
                        <td>{data['aggregated']['words_per_chapter']['max']}</td>
                    </tr>
                    <tr>
                        <td>Words per Course</td>
                        <td>{data['aggregated']['words_per_course']['count']}</td>
                        <td>{data['aggregated']['words_per_course']['mean']:,.0f}</td>
                        <td>{data['aggregated']['words_per_course']['std']:,.0f}</td>
                        <td>{data['aggregated']['words_per_course']['median']:,.0f}</td>
                        <td>{data['aggregated']['words_per_course']['min']:,}</td>
                        <td>{data['aggregated']['words_per_course']['max']:,}</td>
                    </tr>
                    <tr>
                        <td>Paragraphs per Chapter</td>
                        <td>{data['aggregated']['paragraphs_per_chapter']['count']}</td>
                        <td>{data['aggregated']['paragraphs_per_chapter']['mean']}</td>
                        <td>{data['aggregated']['paragraphs_per_chapter']['std']}</td>
                        <td>{data['aggregated']['paragraphs_per_chapter']['median']}</td>
                        <td>{data['aggregated']['paragraphs_per_chapter']['min']}</td>
                        <td>{data['aggregated']['paragraphs_per_chapter']['max']}</td>
                    </tr>
                    <tr>
                        <td>Paragraphs per Course</td>
                        <td>{data['aggregated']['paragraphs_per_course']['count']}</td>
                        <td>{data['aggregated']['paragraphs_per_course']['mean']:,.0f}</td>
                        <td>{data['aggregated']['paragraphs_per_course']['std']:,.0f}</td>
                        <td>{data['aggregated']['paragraphs_per_course']['median']:,.0f}</td>
                        <td>{data['aggregated']['paragraphs_per_course']['min']:,}</td>
                        <td>{data['aggregated']['paragraphs_per_course']['max']:,}</td>
                    </tr>
                    <tr>
                        <td>Sentences per Chapter</td>
                        <td>{data['aggregated']['sentences_per_chapter']['count']}</td>
                        <td>{data['aggregated']['sentences_per_chapter']['mean']}</td>
                        <td>{data['aggregated']['sentences_per_chapter']['std']}</td>
                        <td>{data['aggregated']['sentences_per_chapter']['median']}</td>
                        <td>{data['aggregated']['sentences_per_chapter']['min']}</td>
                        <td>{data['aggregated']['sentences_per_chapter']['max']}</td>
                    </tr>
                    <tr>
                        <td>Sentences per Course</td>
                        <td>{data['aggregated']['sentences_per_course']['count']}</td>
                        <td>{data['aggregated']['sentences_per_course']['mean']:,.0f}</td>
                        <td>{data['aggregated']['sentences_per_course']['std']:,.0f}</td>
                        <td>{data['aggregated']['sentences_per_course']['median']:,.0f}</td>
                        <td>{data['aggregated']['sentences_per_course']['min']:,}</td>
                        <td>{data['aggregated']['sentences_per_course']['max']:,}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Distribution Charts -->
        <div class="section">
            <h2>📊 Distributions</h2>
            <div class="chart-row">
                <div class="chart-box">
                    <h3>Parts per Course Distribution</h3>
                    <div class="chart-container">
                        <canvas id="partsDistChart"></canvas>
                    </div>
                </div>
                <div class="chart-box">
                    <h3>Chapters per Course Distribution</h3>
                    <div class="chart-container">
                        <canvas id="chaptersDistChart"></canvas>
                    </div>
                </div>
            </div>
            <div class="chart-row">
                <div class="chart-box">
                    <h3>Words per Course Distribution</h3>
                    <div class="chart-container">
                        <canvas id="wordsDistChart"></canvas>
                    </div>
                </div>
                <div class="chart-box">
                    <h3>Words per Chapter Distribution</h3>
                    <div class="chart-container">
                        <canvas id="wordsChapterDistChart"></canvas>
                    </div>
                </div>
            </div>
            <div class="chart-row">
                <div class="chart-box">
                    <h3>Chapters per Part Distribution</h3>
                    <div class="chart-container">
                        <canvas id="chaptersPartDistChart"></canvas>
                    </div>
                </div>
                <div class="chart-box">
                    <h3>Subsections per Chapter Distribution</h3>
                    <div class="chart-container">
                        <canvas id="subsectionsDistChart"></canvas>
                    </div>
                </div>
            </div>
            <div class="chart-row">
                <div class="chart-box">
                    <h3>Paragraphs per Chapter Distribution</h3>
                    <div class="chart-container">
                        <canvas id="paragraphsChapterDistChart"></canvas>
                    </div>
                </div>
                <div class="chart-box">
                    <h3>Sentences per Chapter Distribution</h3>
                    <div class="chart-container">
                        <canvas id="sentencesChapterDistChart"></canvas>
                    </div>
                </div>
            </div>
            <div class="chart-row">
                <div class="chart-box">
                    <h3>Paragraphs per Course Distribution</h3>
                    <div class="chart-container">
                        <canvas id="paragraphsCourseDistChart"></canvas>
                    </div>
                </div>
                <div class="chart-box">
                    <h3>Sentences per Course Distribution</h3>
                    <div class="chart-container">
                        <canvas id="sentencesCourseDistChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- Course Comparison -->
        <div class="section">
            <h2>📚 Course Comparison</h2>
            <div class="chart-box" style="margin-bottom: 20px;">
                <div class="chart-container" style="height: 450px;">
                    <canvas id="courseComparisonChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Per-Course Analysis -->
        <div class="section">
            <h2>🔍 Per-Course Analysis</h2>
            <div style="margin-bottom: 20px;">
                <label for="courseSelector" style="margin-right: 10px; font-weight: 600;">Select a course:</label>
                <select id="courseSelector" style="padding: 10px 15px; font-size: 1rem; border-radius: 8px; border: 1px solid var(--border); background: var(--bg-dark); color: var(--text); cursor: pointer; min-width: 200px;">
                    <option value="">-- Select a course --</option>
                    {"".join(f'<option value="{c["id"]}">{c["id"]} ({c["chapters"]} chapters, {c["total_words"]:,} words)</option>' for c in sorted(data['courses'], key=lambda x: x['id']))}
                </select>
            </div>
            <div id="courseAnalysisContent" style="display: none;">
                <div class="stats-grid" style="margin-bottom: 20px;">
                    <div class="stat-card">
                        <div class="stat-value" id="selectedCourseParts">-</div>
                        <div class="stat-label">Parts</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="selectedCourseChapters">-</div>
                        <div class="stat-label">Chapters</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="selectedCourseWords">-</div>
                        <div class="stat-label">Words</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="selectedCourseParagraphs">-</div>
                        <div class="stat-label">Paragraphs</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="selectedCourseSentences">-</div>
                        <div class="stat-label">Sentences</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="selectedCourseAvgWords">-</div>
                        <div class="stat-label">Avg Words/Ch</div>
                    </div>
                </div>
                <div class="chart-row">
                    <div class="chart-box">
                        <h3>Words per Chapter</h3>
                        <div class="chart-container">
                            <canvas id="selectedCourseWordsChart"></canvas>
                        </div>
                    </div>
                    <div class="chart-box">
                        <h3>Subsections (###) per Chapter</h3>
                        <div class="chart-container">
                            <canvas id="selectedCourseSubsectionsChart"></canvas>
                        </div>
                    </div>
                </div>
                <div class="chart-row">
                    <div class="chart-box">
                        <h3>Paragraphs per Chapter</h3>
                        <div class="chart-container">
                            <canvas id="selectedCourseParagraphsChart"></canvas>
                        </div>
                    </div>
                    <div class="chart-box">
                        <h3>Sentences per Chapter</h3>
                        <div class="chart-container">
                            <canvas id="selectedCourseSentencesChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
            <div id="courseAnalysisPlaceholder" style="text-align: center; padding: 40px; color: var(--text-muted);">
                <p style="font-size: 1.2rem;">Select a course above to see detailed chapter-by-chapter analysis</p>
            </div>
        </div>

        <!-- Individual Course Details -->
        <div class="section">
            <h2>📖 Course Details</h2>
            <p style="color: var(--text-muted); margin-bottom: 15px; font-size: 0.9rem;">Click on column headers to sort</p>
            <div style="overflow-x: auto;">
            <table id="courseTable" class="sortable">
                <thead>
                    <tr>
                        <th data-sort="string">Course ID</th>
                        <th data-sort="string">Lang</th>
                        <th data-sort="number">Parts</th>
                        <th data-sort="number">Chapters</th>
                        <th data-sort="number">Subsections</th>
                        <th data-sort="number">Paragraphs</th>
                        <th data-sort="number">Sentences</th>
                        <th data-sort="number">Words</th>
                        <th data-sort="number">Avg Words/Ch</th>
                    </tr>
                </thead>
                <tbody>
                    {"".join(f'''
                    <tr>
                        <td><strong>{c['id']}</strong></td>
                        <td><span class="badge badge-{c['language']}">{c['language'].upper()}</span></td>
                        <td>{c['parts']}</td>
                        <td>{c['chapters']}</td>
                        <td>{c['total_subsections']}</td>
                        <td>{c['total_paragraphs']}</td>
                        <td>{c['total_sentences']}</td>
                        <td>{c['total_words']:,}</td>
                        <td>{round(c['total_words'] / c['chapters']) if c['chapters'] > 0 else 0:,}</td>
                    </tr>
                    ''' for c in sorted(data['courses'], key=lambda x: x['total_words'], reverse=True))}
                </tbody>
            </table>
            </div>
        </div>

        <footer>
            <p>Bitcoin Educational Content Analytics • Generated with Python</p>
        </footer>
    </div>

    <script>
        // Embedded data
        const analyticsData = {json.dumps(data, indent=2)};

        // Chart.js default configuration
        Chart.defaults.color = '#a0a0a0';
        Chart.defaults.borderColor = '#0f3460';

        const chartColors = {{
            primary: '#f7931a',
            secondary: '#4d4d4d',
            success: '#00d26a',
            warning: '#ff9800',
            info: '#2196f3',
            gradient: ['#f7931a', '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7']
        }};

        // Helper function to create histogram data
        function createHistogram(data, bins = 10) {{
            if (!data.length) return {{ labels: [], values: [] }};

            const min = Math.min(...data);
            const max = Math.max(...data);
            const binSize = (max - min) / bins || 1;

            const histogram = new Array(bins).fill(0);
            const labels = [];

            for (let i = 0; i < bins; i++) {{
                const binStart = min + i * binSize;
                const binEnd = min + (i + 1) * binSize;
                labels.push(`${{Math.round(binStart)}}-${{Math.round(binEnd)}}`);
            }}

            data.forEach(value => {{
                let binIndex = Math.floor((value - min) / binSize);
                if (binIndex >= bins) binIndex = bins - 1;
                if (binIndex < 0) binIndex = 0;
                histogram[binIndex]++;
            }});

            return {{ labels, values: histogram }};
        }}

        // Parts per Course Distribution
        const partsHist = createHistogram(analyticsData.distributions.parts_per_course, 8);
        new Chart(document.getElementById('partsDistChart'), {{
            type: 'bar',
            data: {{
                labels: partsHist.labels,
                datasets: [{{
                    label: 'Number of Courses',
                    data: partsHist.values,
                    backgroundColor: chartColors.primary,
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Courses' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Parts per Course' }}
                    }}
                }}
            }}
        }});

        // Chapters per Course Distribution
        const chaptersHist = createHistogram(analyticsData.distributions.chapters_per_course, 10);
        new Chart(document.getElementById('chaptersDistChart'), {{
            type: 'bar',
            data: {{
                labels: chaptersHist.labels,
                datasets: [{{
                    label: 'Number of Courses',
                    data: chaptersHist.values,
                    backgroundColor: chartColors.info,
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Courses' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Chapters per Course' }}
                    }}
                }}
            }}
        }});

        // Words per Course Distribution
        const wordsHist = createHistogram(analyticsData.distributions.words_per_course, 10);
        new Chart(document.getElementById('wordsDistChart'), {{
            type: 'bar',
            data: {{
                labels: wordsHist.labels,
                datasets: [{{
                    label: 'Number of Courses',
                    data: wordsHist.values,
                    backgroundColor: chartColors.success,
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Courses' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Words per Course' }}
                    }}
                }}
            }}
        }});

        // Words per Chapter Distribution
        const wordsChapterHist = createHistogram(analyticsData.distributions.words_per_chapter, 12);
        new Chart(document.getElementById('wordsChapterDistChart'), {{
            type: 'bar',
            data: {{
                labels: wordsChapterHist.labels,
                datasets: [{{
                    label: 'Number of Chapters',
                    data: wordsChapterHist.values,
                    backgroundColor: chartColors.warning,
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Chapters' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Words per Chapter' }}
                    }}
                }}
            }}
        }});

        // Chapters per Part Distribution
        const chaptersPartHist = createHistogram(analyticsData.distributions.chapters_per_part, 8);
        new Chart(document.getElementById('chaptersPartDistChart'), {{
            type: 'bar',
            data: {{
                labels: chaptersPartHist.labels,
                datasets: [{{
                    label: 'Number of Parts',
                    data: chaptersPartHist.values,
                    backgroundColor: '#9c27b0',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Parts' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Chapters per Part' }}
                    }}
                }}
            }}
        }});

        // Subsections per Chapter Distribution
        const subsectionsHist = createHistogram(analyticsData.distributions.subsections_per_chapter, 10);
        new Chart(document.getElementById('subsectionsDistChart'), {{
            type: 'bar',
            data: {{
                labels: subsectionsHist.labels,
                datasets: [{{
                    label: 'Number of Chapters',
                    data: subsectionsHist.values,
                    backgroundColor: '#e91e63',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Chapters' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Subsections per Chapter' }}
                    }}
                }}
            }}
        }});

        // Paragraphs per Chapter Distribution
        const paragraphsChapterHist = createHistogram(analyticsData.distributions.paragraphs_per_chapter, 10);
        new Chart(document.getElementById('paragraphsChapterDistChart'), {{
            type: 'bar',
            data: {{
                labels: paragraphsChapterHist.labels,
                datasets: [{{
                    label: 'Number of Chapters',
                    data: paragraphsChapterHist.values,
                    backgroundColor: '#00bcd4',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Chapters' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Paragraphs per Chapter' }}
                    }}
                }}
            }}
        }});

        // Sentences per Chapter Distribution
        const sentencesChapterHist = createHistogram(analyticsData.distributions.sentences_per_chapter, 10);
        new Chart(document.getElementById('sentencesChapterDistChart'), {{
            type: 'bar',
            data: {{
                labels: sentencesChapterHist.labels,
                datasets: [{{
                    label: 'Number of Chapters',
                    data: sentencesChapterHist.values,
                    backgroundColor: '#8bc34a',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Chapters' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Sentences per Chapter' }}
                    }}
                }}
            }}
        }});

        // Paragraphs per Course Distribution
        const paragraphsCourseHist = createHistogram(analyticsData.distributions.paragraphs_per_course, 10);
        new Chart(document.getElementById('paragraphsCourseDistChart'), {{
            type: 'bar',
            data: {{
                labels: paragraphsCourseHist.labels,
                datasets: [{{
                    label: 'Number of Courses',
                    data: paragraphsCourseHist.values,
                    backgroundColor: '#795548',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Courses' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Paragraphs per Course' }}
                    }}
                }}
            }}
        }});

        // Sentences per Course Distribution
        const sentencesCourseHist = createHistogram(analyticsData.distributions.sentences_per_course, 10);
        new Chart(document.getElementById('sentencesCourseDistChart'), {{
            type: 'bar',
            data: {{
                labels: sentencesCourseHist.labels,
                datasets: [{{
                    label: 'Number of Courses',
                    data: sentencesCourseHist.values,
                    backgroundColor: '#607d8b',
                    borderRadius: 6
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Number of Courses' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Sentences per Course' }}
                    }}
                }}
            }}
        }});

        // Course Comparison Chart
        const sortedCourses = [...analyticsData.courses].sort((a, b) => b.total_words - a.total_words);
        new Chart(document.getElementById('courseComparisonChart'), {{
            type: 'bar',
            data: {{
                labels: sortedCourses.map(c => c.id),
                datasets: [
                    {{
                        label: 'Words (÷100)',
                        data: sortedCourses.map(c => Math.round(c.total_words / 100)),
                        backgroundColor: chartColors.primary,
                        borderRadius: 4
                    }},
                    {{
                        label: 'Chapters (×10)',
                        data: sortedCourses.map(c => c.chapters * 10),
                        backgroundColor: chartColors.info,
                        borderRadius: 4
                    }},
                    {{
                        label: 'Parts (×50)',
                        data: sortedCourses.map(c => c.parts * 50),
                        backgroundColor: chartColors.success,
                        borderRadius: 4
                    }}
                ]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'top'
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                const course = sortedCourses[context.dataIndex];
                                if (context.dataset.label.includes('Words')) {{
                                    return `Words: ${{course.total_words.toLocaleString()}}`;
                                }} else if (context.dataset.label.includes('Chapters')) {{
                                    return `Chapters: ${{course.chapters}}`;
                                }} else {{
                                    return `Parts: ${{course.parts}}`;
                                }}
                            }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{ display: true, text: 'Scaled Values' }}
                    }},
                    x: {{
                        title: {{ display: true, text: 'Course ID' }}
                    }}
                }}
            }}
        }});

        // Sortable table functionality
        document.querySelectorAll('.sortable').forEach(table => {{
            const headers = table.querySelectorAll('th');
            const tbody = table.querySelector('tbody');

            headers.forEach((header, index) => {{
                header.addEventListener('click', () => {{
                    const sortType = header.dataset.sort;
                    const isAsc = header.classList.contains('sort-asc');

                    // Remove sort classes from all headers
                    headers.forEach(h => h.classList.remove('sort-asc', 'sort-desc'));

                    // Add appropriate class
                    header.classList.add(isAsc ? 'sort-desc' : 'sort-asc');

                    // Get rows and sort
                    const rows = Array.from(tbody.querySelectorAll('tr'));
                    rows.sort((a, b) => {{
                        let aVal = a.cells[index].textContent.trim();
                        let bVal = b.cells[index].textContent.trim();

                        if (sortType === 'number') {{
                            aVal = parseFloat(aVal.replace(/,/g, '')) || 0;
                            bVal = parseFloat(bVal.replace(/,/g, '')) || 0;
                        }}

                        if (isAsc) {{
                            return aVal > bVal ? -1 : aVal < bVal ? 1 : 0;
                        }} else {{
                            return aVal < bVal ? -1 : aVal > bVal ? 1 : 0;
                        }}
                    }});

                    // Re-append sorted rows
                    rows.forEach(row => tbody.appendChild(row));
                }});
            }});
        }});

        // Per-course analysis functionality
        let selectedCourseWordsChart = null;
        let selectedCourseSubsectionsChart = null;
        let selectedCourseParagraphsChart = null;
        let selectedCourseSentencesChart = null;

        document.getElementById('courseSelector').addEventListener('change', function() {{
            const courseId = this.value;
            const contentDiv = document.getElementById('courseAnalysisContent');
            const placeholderDiv = document.getElementById('courseAnalysisPlaceholder');

            if (!courseId) {{
                contentDiv.style.display = 'none';
                placeholderDiv.style.display = 'block';
                return;
            }}

            const course = analyticsData.courses.find(c => c.id === courseId);
            if (!course) return;

            // Show content, hide placeholder
            contentDiv.style.display = 'block';
            placeholderDiv.style.display = 'none';

            // Update stats
            document.getElementById('selectedCourseParts').textContent = course.parts;
            document.getElementById('selectedCourseChapters').textContent = course.chapters;
            document.getElementById('selectedCourseWords').textContent = course.total_words.toLocaleString();
            document.getElementById('selectedCourseParagraphs').textContent = course.total_paragraphs.toLocaleString();
            document.getElementById('selectedCourseSentences').textContent = course.total_sentences.toLocaleString();
            document.getElementById('selectedCourseAvgWords').textContent = Math.round(course.total_words / course.chapters).toLocaleString();

            // Generate chapter labels
            const chapterLabels = course.words_per_chapter.map((_, i) => `Ch ${{i + 1}}`);

            // Destroy existing charts if they exist
            if (selectedCourseWordsChart) selectedCourseWordsChart.destroy();
            if (selectedCourseSubsectionsChart) selectedCourseSubsectionsChart.destroy();
            if (selectedCourseParagraphsChart) selectedCourseParagraphsChart.destroy();
            if (selectedCourseSentencesChart) selectedCourseSentencesChart.destroy();

            // Words per Chapter Chart
            selectedCourseWordsChart = new Chart(document.getElementById('selectedCourseWordsChart'), {{
                type: 'bar',
                data: {{
                    labels: chapterLabels,
                    datasets: [{{
                        label: 'Words',
                        data: course.words_per_chapter,
                        backgroundColor: chartColors.primary,
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return `Words: ${{context.raw.toLocaleString()}}`;
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            title: {{ display: true, text: 'Words' }}
                        }},
                        x: {{
                            title: {{ display: true, text: 'Chapter' }}
                        }}
                    }}
                }}
            }});

            // Subsections per Chapter Chart
            selectedCourseSubsectionsChart = new Chart(document.getElementById('selectedCourseSubsectionsChart'), {{
                type: 'bar',
                data: {{
                    labels: chapterLabels,
                    datasets: [{{
                        label: 'Subsections (###)',
                        data: course.subsections_per_chapter,
                        backgroundColor: chartColors.info,
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return `Subsections: ${{context.raw}}`;
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            title: {{ display: true, text: 'Subsections (###)' }}
                        }},
                        x: {{
                            title: {{ display: true, text: 'Chapter' }}
                        }}
                    }}
                }}
            }});

            // Paragraphs per Chapter Chart
            selectedCourseParagraphsChart = new Chart(document.getElementById('selectedCourseParagraphsChart'), {{
                type: 'bar',
                data: {{
                    labels: chapterLabels,
                    datasets: [{{
                        label: 'Paragraphs',
                        data: course.paragraphs_per_chapter,
                        backgroundColor: '#00bcd4',
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return `Paragraphs: ${{context.raw}}`;
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            title: {{ display: true, text: 'Paragraphs' }}
                        }},
                        x: {{
                            title: {{ display: true, text: 'Chapter' }}
                        }}
                    }}
                }}
            }});

            // Sentences per Chapter Chart
            selectedCourseSentencesChart = new Chart(document.getElementById('selectedCourseSentencesChart'), {{
                type: 'bar',
                data: {{
                    labels: chapterLabels,
                    datasets: [{{
                        label: 'Sentences',
                        data: course.sentences_per_chapter,
                        backgroundColor: '#8bc34a',
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    return `Sentences: ${{context.raw}}`;
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            title: {{ display: true, text: 'Sentences' }}
                        }},
                        x: {{
                            title: {{ display: true, text: 'Chapter' }}
                        }}
                    }}
                }}
            }});
        }});
    </script>
</body>
</html>
'''
    return html


def main():
    """Main entry point."""
    # Determine courses directory
    script_dir = Path(__file__).parent
    courses_dir = script_dir.parent.parent / "courses"

    if not courses_dir.exists():
        print(f"Error: Courses directory not found at {courses_dir}")
        return 1

    print(f"Analyzing courses in: {courses_dir}")
    print("-" * 50)

    # Analyze courses
    data = analyze_courses(courses_dir)

    print("-" * 50)
    print(f"Total courses analyzed: {data['total_courses']}")

    # Generate HTML report
    html_content = generate_html_report(data)

    # Save report
    output_path = script_dir / "course_analytics_report.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ Report generated: {output_path}")

    # Also save raw JSON data for reference
    json_path = script_dir / "course_analytics_data.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Raw data saved: {json_path}")

    return 0


if __name__ == "__main__":
    exit(main())
