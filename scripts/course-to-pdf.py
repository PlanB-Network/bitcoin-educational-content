#!/usr/bin/env python3
"""
Unified Course to PDF Converter
Converts Bitcoin educational course markdown files to PDF with proper formatting.
"""

import os
import re
import base64
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

def get_available_courses() -> List[str]:
    """Get list of available course codes from the project directory."""
    courses = []
    project_root = Path(__file__).parent.parent
    courses_dir = project_root / "courses"

    # Get all course directories
    if courses_dir.exists():
        for course_dir in sorted(courses_dir.iterdir()):
            if course_dir.is_dir() and not course_dir.name.startswith('.'):
                md_file = course_dir / "en.md"
                if md_file.exists():
                    courses.append(course_dir.name)

    return courses

def convert_webp_to_data_url(image_path: Path) -> Optional[str]:
    """Convert webp image to data URL for embedding in HTML."""
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            return f"data:image/webp;base64,{b64_data}"
    except Exception as e:
        print(f"  ⚠️  Could not load image {image_path}: {e}")
        return None

def clean_content(content: str) -> str:
    """Remove unwanted elements from markdown content."""
    # Remove file paths at the bottom of pages
    content = re.sub(r'file://[^\s\n]+', '', content)

    # Remove hex IDs like 3cd2ac82-026c-53e1-874a-baf5842adc6d
    content = re.sub(r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}', '', content)

    # Remove +++ lines
    content = re.sub(r'^\+\+\+\s*$', '', content, flags=re.MULTILINE)

    # Remove "true" or "false" standing alone on lines
    content = re.sub(r'^\s*(true|false)\s*$', '', content, flags=re.MULTILINE)

    # Remove --- name: ... --- blocks
    content = re.sub(r'^---\s*\n.*?name:.*?\n---\s*$', '', content, flags=re.MULTILINE | re.DOTALL)

    # Remove sections we don't want in PDF
    content = re.sub(r'^#+\s*(Conclusion|Final Exam|Reviews & Ratings|Final Section)\s*$.*?(?=^#|\Z)', '',
                     content, flags=re.MULTILINE | re.DOTALL)

    # Clean up excessive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content

def extract_toc(content: str) -> List[Tuple[int, str, str]]:
    """Extract table of contents from headers."""
    toc = []
    headers = re.findall(r'^(#{1,4})\s+(.+)$', content, re.MULTILINE)

    for header in headers:
        level = len(header[0])
        text = header[1].strip()
        # Skip certain headers from TOC
        if text.lower() in ['conclusion', 'final exam', 'reviews & ratings', 'final section']:
            continue
        # Create anchor id from header text
        anchor = re.sub(r'[^a-z0-9\-_]', '', text.lower().replace(' ', '-'))
        toc.append((level, text, anchor))

    return toc

def generate_toc_html(toc: List[Tuple[int, str, str]]) -> str:
    """Generate HTML for table of contents."""
    if not toc:
        return ""

    html = '<div class="toc">\n<h2>Table of Contents</h2>\n<ul class="toc-list">\n'

    current_level = 0
    for level, text, anchor in toc:
        # Close previous nested lists if going to a higher level
        while current_level > level:
            html += '</ul></li>\n'
            current_level -= 1

        # Open new nested lists if going deeper
        while current_level < level and current_level > 0:
            html += '<ul>\n'
            current_level += 1

        if current_level == 0:
            current_level = level

        html += f'<li class="toc-h{level}"><a href="#{anchor}">{text}</a>'

        # Check if next item is a sublevel
        idx = toc.index((level, text, anchor))
        if idx < len(toc) - 1 and toc[idx + 1][0] > level:
            html += '\n<ul>\n'
            current_level += 1
        else:
            html += '</li>\n'

    # Close any remaining open lists
    while current_level > 1:
        html += '</ul></li>\n'
        current_level -= 1

    html += '</ul>\n</div>\n<div class="page-break"></div>\n'
    return html

def convert_tables(text: str) -> str:
    """Convert markdown tables to HTML tables with proper structure."""
    table_pattern = r'(\|[^\n]+\|(?:\n\|[-: ]+\|)?(?:\n\|[^\n]+\|)*)'

    def process_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 2:
            return match.group(0)

        # Check if second line is separator line
        is_header = bool(re.match(r'^[\|\s\-:]+$', lines[1]))

        html = '<table>\n'

        if is_header:
            # Process header row
            html += '<thead>\n<tr>\n'
            cells = [cell.strip() for cell in lines[0].split('|')[1:-1]]
            for cell in cells:
                html += f'<th>{cell}</th>\n'
            html += '</tr>\n</thead>\n'

            # Process body rows
            html += '<tbody>\n'
            for line in lines[2:]:
                if line.strip():
                    html += '<tr>\n'
                    cells = [cell.strip() for cell in line.split('|')[1:-1]]
                    for cell in cells:
                        html += f'<td>{cell}</td>\n'
                    html += '</tr>\n'
            html += '</tbody>\n'
        else:
            # All rows are body rows
            html += '<tbody>\n'
            for line in lines:
                if line.strip():
                    html += '<tr>\n'
                    cells = [cell.strip() for cell in line.split('|')[1:-1]]
                    for cell in cells:
                        html += f'<td>{cell}</td>\n'
                    html += '</tr>\n'
            html += '</tbody>\n'

        html += '</table>'
        return html

    return re.sub(table_pattern, process_table, text, flags=re.MULTILINE)

def convert_lists(html: str) -> str:
    """Improved list conversion."""
    lines = html.split('\n')
    new_lines = []
    list_stack = []

    for line in lines:
        # Check for unordered list item
        ul_match = re.match(r'^(\s*)([\*\-])\s+(.+)$', line)
        # Check for ordered list item
        ol_match = re.match(r'^(\s*)(\d+)\.\s+(.+)$', line)

        if ul_match or ol_match:
            if ul_match:
                indent_level = len(ul_match.group(1)) // 2
                list_type = 'ul'
                content = ul_match.group(3)
            else:
                indent_level = len(ol_match.group(1)) // 2
                list_type = 'ol'
                content = ol_match.group(3)

            # Manage list stack
            while len(list_stack) > indent_level + 1:
                tag = list_stack.pop()
                new_lines.append(f'</{tag}>')

            if len(list_stack) == indent_level:
                # Start new list
                new_lines.append(f'<{list_type}>')
                list_stack.append(list_type)
            elif len(list_stack) == indent_level + 1:
                # Check if we need to switch list type
                if list_stack[-1] != list_type:
                    new_lines.append(f'</{list_stack[-1]}>')
                    list_stack.pop()
                    new_lines.append(f'<{list_type}>')
                    list_stack.append(list_type)

            new_lines.append(f'<li>{content}</li>')
        else:
            # Close all open lists
            while list_stack:
                tag = list_stack.pop()
                new_lines.append(f'</{tag}>')
            new_lines.append(line)

    # Close any remaining open lists
    while list_stack:
        tag = list_stack.pop()
        new_lines.append(f'</{tag}>')

    return '\n'.join(new_lines)

def convert_paragraphs(html: str) -> str:
    """Convert text into proper paragraphs."""
    blocks = re.split(r'\n\n+', html)
    processed_blocks = []

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Check if block is already an HTML element
        if (block.startswith('<h') or block.startswith('<ul') or
            block.startswith('<ol') or block.startswith('<blockquote') or
            block.startswith('<pre') or block.startswith('<table') or
            block.startswith('<div')):
            processed_blocks.append(block)
        else:
            # Wrap in paragraph tags
            processed_blocks.append(f'<p>{block}</p>')

    return '\n\n'.join(processed_blocks)

def convert_markdown_to_html_improved(markdown_text: str, toc: List) -> str:
    """Improved markdown to HTML conversion with better table support."""
    html = markdown_text

    # Process tables first (before other conversions)
    html = convert_tables(html)

    # Headers with IDs for TOC linking
    def add_header_id(match):
        level = len(match.group(1))
        text = match.group(2)
        anchor = re.sub(r'[^a-z0-9\-_]', '', text.lower().replace(' ', '-'))
        return f'<h{level} id="{anchor}">{text}</h{level}>'

    html = re.sub(r'^(#{1,4})\s+(.+)$', add_header_id, html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'__(.+?)__', r'<strong>\1</strong>', html)
    html = re.sub(r'_(.+?)_', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

    # Code blocks
    html = re.sub(r'```([^`]+)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Lists (improved support)
    html = convert_lists(html)

    # Paragraphs
    html = convert_paragraphs(html)

    return html

def process_markdown_to_html(course_code: str, project_root: Path) -> Optional[str]:
    """Convert markdown course file to HTML with embedded images."""
    course_dir = project_root / "courses" / course_code.lower()
    md_file = course_dir / "en.md"
    assets_dir = course_dir / "assets" / "en"

    if not md_file.exists():
        print(f"  ❌ Course file {md_file} not found")
        return None

    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean content first
    content = clean_content(content)

    # Extract TOC before processing
    toc = extract_toc(content)

    # Process images - convert relative paths to embedded data URLs
    def replace_image(match):
        img_path = match.group(2)
        # Remove leading ./ or / if present
        img_path = img_path.lstrip('./')

        # Check different possible paths
        possible_paths = [
            course_dir / img_path,
            course_dir / "assets" / "en" / img_path,
            course_dir / "assets" / img_path,
            project_root / img_path
        ]

        # Also check if it's just a filename
        if '/' not in img_path:
            possible_paths.append(assets_dir / img_path)

        for path in possible_paths:
            if path.exists():
                data_url = convert_webp_to_data_url(path)
                if data_url:
                    return f'<img src="{data_url}" alt="{match.group(1)}" style="max-width: 100%; height: auto;">'
                break

        # If image not found, return original markdown
        print(f"  ⚠️  Image not found: {img_path}")
        return f'<img src="{img_path}" alt="{match.group(1)}" style="max-width: 100%; height: auto;">'

    # Replace markdown image syntax with HTML img tags
    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_image, content)

    # Convert markdown to HTML with improved conversion
    html_content = convert_markdown_to_html_improved(content, toc)

    # Generate TOC HTML
    toc_html = generate_toc_html(toc)

    # Create full HTML document with CSS
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course_code.upper()} - Bitcoin Educational Course</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: white;
        }}
        .toc {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 30px;
            border: 1px solid #e9ecef;
        }}
        .toc h2 {{
            color: #2c3e50;
            margin-top: 0;
            margin-bottom: 20px;
            font-size: 24px;
            border-bottom: 2px solid #f39c12;
            padding-bottom: 10px;
        }}
        .toc-list {{
            list-style: none;
            padding-left: 0;
        }}
        .toc-list ul {{
            list-style: none;
            padding-left: 20px;
        }}
        .toc li {{
            margin: 8px 0;
            line-height: 1.5;
        }}
        .toc-h1 {{
            font-weight: bold;
            font-size: 16px;
            margin-top: 15px;
        }}
        .toc-h2 {{
            font-size: 14px;
        }}
        .toc-h3 {{
            font-size: 13px;
            color: #555;
        }}
        .toc-h4 {{
            font-size: 12px;
            color: #777;
        }}
        .toc a {{
            color: #3498db;
            text-decoration: none;
        }}
        .toc a:hover {{
            text-decoration: underline;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #f39c12;
            padding-bottom: 10px;
            page-break-after: avoid;
            margin-top: 40px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 8px;
            page-break-after: avoid;
        }}
        h3 {{
            color: #34495e;
            margin-top: 25px;
            page-break-after: avoid;
        }}
        h4 {{
            color: #34495e;
            margin-top: 20px;
            page-break-after: avoid;
        }}
        p {{
            margin: 15px 0;
            text-align: justify;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            page-break-inside: avoid;
        }}
        blockquote {{
            border-left: 4px solid #f39c12;
            padding-left: 20px;
            margin: 20px 0;
            color: #555;
            font-style: italic;
            background: #f8f9fa;
            padding: 15px 20px;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            page-break-inside: avoid;
            font-size: 14px;
        }}
        thead {{
            background-color: #f2f2f2;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
            vertical-align: top;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .page-break {{
            page-break-after: always;
        }}
        @media print {{
            body {{
                margin: 0;
                padding: 10px;
                font-size: 11pt;
            }}
            .toc {{ page-break-after: always; }}
            h1, h2, h3, h4 {{ page-break-after: avoid; }}
            img, pre, blockquote, table {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>
    {toc_html}
    {html_content}
</body>
</html>"""

    return html_template

def html_to_pdf_chromium(html_file: Path, pdf_file: Path) -> bool:
    """Convert HTML to PDF using Chromium browser."""
    try:
        # Use Chromium in headless mode to convert HTML to PDF
        cmd = [
            'chromium-browser',
            '--headless',
            '--disable-gpu',
            '--no-sandbox',
            f'--print-to-pdf={pdf_file}',
            '--print-to-pdf-no-header',
            '--no-margins',
            f'file://{html_file.absolute()}'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0 and pdf_file.exists():
            # Sometimes chromium returns non-zero but still creates the PDF
            return True

        return result.returncode == 0
    except FileNotFoundError:
        print("  ⚠️  Chromium not found. Trying alternative browsers...")
        return False

def html_to_pdf_wkhtmltopdf(html_file: Path, pdf_file: Path) -> bool:
    """Convert HTML to PDF using wkhtmltopdf as fallback."""
    try:
        cmd = [
            'wkhtmltopdf',
            '--enable-local-file-access',
            '--no-header-line',
            '--no-footer-line',
            '--margin-top', '10mm',
            '--margin-bottom', '10mm',
            '--margin-left', '10mm',
            '--margin-right', '10mm',
            str(html_file),
            str(pdf_file)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def convert_course_to_pdf(course_code: str, output_dir: Path) -> bool:
    """Convert a single course to PDF with course-based naming."""
    project_root = Path(__file__).parent.parent

    print(f"\n📚 Processing {course_code.upper()}...")

    # Generate HTML content
    html_content = process_markdown_to_html(course_code, project_root)
    if not html_content:
        return False

    # Save HTML to temporary file
    temp_html = output_dir / f"{course_code}_temp.html"
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"  ✓ Generated HTML")

    # Convert HTML to PDF with course-based naming
    pdf_file = output_dir / f"{course_code.lower()}_en.pdf"

    print(f"  🔄 Converting to PDF...")
    success = html_to_pdf_chromium(temp_html, pdf_file)

    if not success:
        print("  ⚠️  Trying wkhtmltopdf as fallback...")
        success = html_to_pdf_wkhtmltopdf(temp_html, pdf_file)

    # Clean up temporary HTML file
    temp_html.unlink()

    if success and pdf_file.exists():
        size = pdf_file.stat().st_size / (1024 * 1024)  # Size in MB
        print(f"  ✅ Generated PDF: {pdf_file.name} ({size:.2f} MB)")
        return True
    else:
        print(f"  ❌ Failed to generate PDF")
        return False

def main():
    """Main function to run the interactive course to PDF converter."""
    print("=" * 60)
    print("📖 Bitcoin Educational Content - Course to PDF Converter")
    print("=" * 60)

    # Get available courses
    courses = get_available_courses()

    if not courses:
        print("\n❌ No courses found in the project directory")
        sys.exit(1)

    print("\n📋 Available courses:")
    for i, course in enumerate(courses, 1):
        print(f"  {i}. {course.upper()}")
    print(f"  {len(courses) + 1}. Convert all courses")

    print("\n📝 Instructions:")
    print("  • Enter single numbers: 1")
    print("  • Enter multiple numbers separated by commas: 1,3,5")
    print("  • Enter ranges with dash: 1-5")
    print("  • Combine ranges and numbers: 1-3,7,9-11")
    print(f"  • Enter {len(courses) + 1} for all courses")
    print("  • Enter 'q' to quit")

    # Get user choice
    while True:
        try:
            choice = input("\n🎯 Select course(s): ").strip()

            if choice.lower() == 'q':
                print("\n👋 Goodbye!")
                sys.exit(0)

            selected_indices = []

            # Check if "all" option was selected
            if choice == str(len(courses) + 1):
                selected_indices = list(range(1, len(courses) + 1))
            else:
                # Parse the input for ranges and individual numbers
                parts = choice.split(',')
                for part in parts:
                    part = part.strip()
                    if '-' in part:
                        # Handle range
                        start, end = part.split('-')
                        start_num = int(start.strip())
                        end_num = int(end.strip())
                        if 1 <= start_num <= len(courses) and 1 <= end_num <= len(courses):
                            selected_indices.extend(range(start_num, end_num + 1))
                        else:
                            raise ValueError("Range out of bounds")
                    else:
                        # Handle single number
                        num = int(part)
                        if 1 <= num <= len(courses):
                            selected_indices.append(num)
                        else:
                            raise ValueError("Number out of bounds")

            # Remove duplicates and sort
            selected_indices = sorted(set(selected_indices))

            if selected_indices:
                selected_courses = [courses[idx - 1] for idx in selected_indices]
                print(f"\n✓ Selected {len(selected_courses)} course(s): {', '.join([c.upper() for c in selected_courses])}")
                break
            else:
                print("  ❌ No valid courses selected. Please try again.")
        except (ValueError, IndexError) as e:
            print(f"  ❌ Invalid input. Please use the format shown in the instructions.")

    # Create output directory in scripts folder
    output_dir = Path(__file__).parent / "pdf_courses"
    output_dir.mkdir(exist_ok=True)
    print(f"\n📁 Output directory: {output_dir}")

    # Convert selected courses
    successful = []
    failed = []

    for course_code in selected_courses:
        if convert_course_to_pdf(course_code, output_dir):
            successful.append(course_code)
        else:
            failed.append(course_code)

    # Print summary
    print("\n" + "=" * 60)
    print("📊 Conversion Summary:")
    print("=" * 60)

    if successful:
        print(f"\n✅ Successfully converted ({len(successful)}):")
        for course_code in successful:
            pdf_path = output_dir / f"{course_code.lower()}_en.pdf"
            print(f"  - {course_code.upper()} → {pdf_path}")

    if failed:
        print(f"\n❌ Failed to convert ({len(failed)}):")
        for course_code in failed:
            print(f"  - {course_code.upper()}")

    print("\n📝 Features included in PDFs:")
    print("  ✓ Table of Contents with clickable links")
    print("  ✓ Proper table formatting with headers")
    print("  ✓ Clean content (no IDs, URLs, or unnecessary sections)")
    print("  ✓ Professional layout with embedded images")
    print("  ✓ Optimized for both viewing and printing")

    print("\n💡 Tips:")
    print("  • PDFs are saved in: scripts/pdf_courses/")
    print("  • You can also print from browser for custom settings")
    print("  • For best results, ensure Chromium is installed")
    print("=" * 60)

if __name__ == "__main__":
    main()