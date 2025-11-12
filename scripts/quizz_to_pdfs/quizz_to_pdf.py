#!/usr/bin/env python3
"""
Quiz to PDF Generator
Converts quiz YML files to PDF with randomized answer order and answer key.
"""

import argparse
import os
import random
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Tuple

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)


class QuizQuestion:
    """Represents a single quiz question with randomized answers."""

    def __init__(self, question: str, correct_answer: str, wrong_answers: List[str],
                 explanation: str = "", quiz_number: str = ""):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers
        self.explanation = explanation
        self.quiz_number = quiz_number
        self.answers = []
        self.correct_index = -1
        self._randomize_answers()

    def _randomize_answers(self):
        """Randomize the order of answers and track correct answer position."""
        all_answers = [self.correct_answer] + self.wrong_answers
        random.shuffle(all_answers)
        self.answers = all_answers
        self.correct_index = self.answers.index(self.correct_answer)

    def get_correct_letter(self) -> str:
        """Return the letter (A, B, C, D) of the correct answer."""
        return chr(65 + self.correct_index)  # 65 is ASCII 'A'


def escape_latex(text) -> str:
    """Escape special LaTeX characters."""
    # Convert to string if not already
    text = str(text) if text is not None else ""

    # Order matters! Backslash must be escaped first
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\^{}'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def find_course_dirs(base_path: Path) -> List[str]:
    """Find all course directories."""
    courses = []
    if base_path.exists():
        for item in base_path.iterdir():
            if item.is_dir() and (item / "quizz").exists():
                courses.append(item.name)
    return sorted(courses)


def load_quiz_files(course: str, language: str, base_path: Path) -> List[QuizQuestion]:
    """Load all quiz files for a given course and language."""
    quiz_dir = base_path / course / "quizz"
    questions = []

    if not quiz_dir.exists():
        print(f"Error: Quiz directory not found: {quiz_dir}")
        return questions

    # Find all 3-digit directories
    quiz_numbers = sorted([d.name for d in quiz_dir.iterdir()
                          if d.is_dir() and d.name.isdigit() and len(d.name) == 3])

    for quiz_num in quiz_numbers:
        quiz_file = quiz_dir / quiz_num / f"{language}.yml"
        if quiz_file.exists():
            try:
                with open(quiz_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data and 'question' in data and 'answer' in data:
                        question = QuizQuestion(
                            question=data['question'],
                            correct_answer=data['answer'],
                            wrong_answers=data.get('wrong_answers', []),
                            explanation=data.get('explanation', ''),
                            quiz_number=quiz_num
                        )
                        questions.append(question)
            except Exception as e:
                print(f"Warning: Failed to load {quiz_file}: {e}")

    return questions


def generate_latex(questions: List[QuizQuestion], course: str, language: str) -> str:
    """Generate LaTeX document from quiz questions."""

    # Map languages to IBM Plex font directories
    font_map = {
        'hi': 'IBM-Plex-Sans-Devanagari',  # Hindi
        'ja': 'IBM-Plex-Sans-JP',           # Japanese
        'ko': 'IBM-Plex-Sans-KR',           # Korean
        'zh-Hans': 'IBM-Plex-Sans-TC',      # Chinese Simplified (using TC)
        'zh-Hant': 'IBM-Plex-Sans-TC',      # Chinese Traditional
        'ar': 'IBM-Plex-Sans-Arabic',       # Arabic
        'fa': 'IBM-Plex-Sans-Arabic',       # Persian (uses Arabic script)
        'th': 'IBM-Plex-Sans-Thai',         # Thai
    }

    # Detect if language needs special Unicode support (non-Latin scripts)
    needs_unicode = language in font_map or language in ['ru', 'sr-Latn']

    # Get base fonts directory
    fonts_base = Path(__file__).parent / "fonts" / "TrueType"

    # Determine font configuration
    if language in font_map:
        # Use specific IBM Plex variant for this language
        font_dir = fonts_base / font_map[language]
        font_name = font_map[language].replace('-', '')  # IBMPlexSansDevanagari, etc.
    else:
        # Use IBM Plex Sans for Latin scripts and Russian/Serbian
        font_dir = fonts_base / "IBM-Plex-Sans"
        font_name = "IBMPlexSans"

    # Generate LaTeX header using fontspec (works for all languages with XeLaTeX/LuaLaTeX)
    latex = r"""\documentclass[12pt,a4paper]{article}
\usepackage{fontspec}
\usepackage{geometry}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{lastpage}
\usepackage{hyperref}

% Configure IBM Plex Sans font family
\setmainfont{""" + font_name + r"""}[
  Path=""" + str(font_dir) + r"""/,
  Extension=.ttf,
  UprightFont=*-Regular,
  BoldFont=*-Bold,
  Scale=1.0
]

\geometry{margin=2.5cm}
\pagestyle{fancy}
\fancyhf{}
\rhead{Page \thepage\ of \pageref{LastPage}}
\lhead{""" + f"{course.upper()} - Quiz ({language})" + r"""}
\renewcommand{\headrulewidth}{0.4pt}

\title{""" + f"Quiz: {course.upper()}" + r"""}
\author{Language: """ + language + r"""}
\date{\today}

\begin{document}

\maketitle
\thispagestyle{fancy}

\section*{Instructions}
Answer all questions by selecting the best option (A, B, C, or D). The answer key is provided at the end of this document.

\bigskip

"""

    # Add questions (no escaping needed with fontspec/Unicode)
    for idx, q in enumerate(questions, 1):
        latex += f"\n\\subsection*{{Question {idx}}}\n"
        latex += q.question + "\n\n"
        latex += "\\begin{enumerate}[label=\\Alph*., leftmargin=*]\n"

        for answer in q.answers:
            latex += f"\\item {answer}\n"

        latex += "\\end{enumerate}\n\n"
        latex += "\\bigskip\n\n"

    # Add answer key
    latex += r"""
\newpage
\section*{Answer Key}

\begin{enumerate}
"""

    for idx, q in enumerate(questions, 1):
        latex += f"\\item \\textbf{{Question {idx}:}} {q.get_correct_letter()}\n"
        if q.explanation:
            # Clean explanation: remove extra newlines and normalize whitespace
            explanation = ' '.join(q.explanation.strip().split())
            # Always escape % to prevent LaTeX comments
            explanation = explanation.replace('%', r'\%')
            latex += f"\\\\ \\textit{{{explanation}}}\n"
        latex += "\n"

    latex += r"""
\end{enumerate}

\end{document}
"""

    return latex


def compile_pdf(latex_content: str, output_name: str, output_dir: Path, language: str) -> bool:
    """Compile LaTeX to PDF using xelatex or lualatex (fontspec requires Unicode engine)."""

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    tex_file = output_dir / f"{output_name}.tex"

    # Write LaTeX file
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)

    print(f"Generated LaTeX file: {tex_file}")

    # Choose LaTeX engine (try xelatex first, fallback to lualatex)
    # All languages now use fontspec, which requires XeLaTeX or LuaLaTeX
    latex_cmd = None
    for cmd in ['xelatex', 'lualatex']:
        try:
            subprocess.run([cmd, '--version'], capture_output=True, check=True)
            latex_cmd = cmd
            break
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue

    if not latex_cmd:
        print(f"Error: Neither xelatex nor lualatex found. IBM Plex fonts require XeLaTeX or LuaLaTeX.")
        print(f"Install with: sudo apt-get install texlive-xetex texlive-luatex")
        return False

    print(f"Using {latex_cmd} for compilation...")

    # Compile with chosen LaTeX engine (run 3 times to resolve all references)
    try:
        for _ in range(3):
            subprocess.run(
                [latex_cmd, '-interaction=nonstopmode', '-output-directory', str(output_dir), str(tex_file)],
                capture_output=True,
                check=False
            )

        pdf_file = output_dir / f"{output_name}.pdf"

        # Check if PDF was created (even if return code was non-zero)
        if pdf_file.exists():
            print(f"✓ PDF generated: {pdf_file}")

            # Clean up auxiliary files (keep .log for debugging if needed)
            for ext in ['.aux', '.out']:
                aux_file = output_dir / f"{output_name}{ext}"
                if aux_file.exists():
                    aux_file.unlink()

            return True
        else:
            print("Error: PDF file was not created")
            return False

    except FileNotFoundError:
        print(f"Error: {latex_cmd} not found. Please install texlive-xetex or texlive-luatex.")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate PDF quiz from YML files with randomized answers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s btc101              # Generate quiz for btc101 in English
  %(prog)s btc101 -l fr        # Generate quiz for btc101 in French
  %(prog)s eco204 -l es -o ./output  # Generate quiz with custom output directory
  %(prog)s --list-courses      # List all available courses
        """
    )

    parser.add_argument('course', nargs='?', help='Course code (e.g., btc101, eco204)')
    parser.add_argument('-l', '--language', default='en',
                        help='Language code (default: en)')
    parser.add_argument('-o', '--output', default='./output',
                        help='Output directory (default: ./output)')
    parser.add_argument('--list-courses', action='store_true',
                        help='List all available courses')
    parser.add_argument('--base-path', type=Path,
                        default=Path(__file__).parent.parent.parent / 'courses',
                        help='Base path to courses directory')

    args = parser.parse_args()

    # List courses if requested
    if args.list_courses:
        courses = find_course_dirs(args.base_path)
        print("Available courses:")
        for course in courses:
            print(f"  - {course}")
        return

    # Validate course argument
    if not args.course:
        parser.error("course is required (or use --list-courses)")

    print(f"Generating quiz PDF for {args.course} in {args.language}...")

    # Load quiz questions
    questions = load_quiz_files(args.course, args.language, args.base_path)

    if not questions:
        print(f"Error: No quiz questions found for {args.course} in {args.language}")
        sys.exit(1)

    print(f"Loaded {len(questions)} questions")

    # Generate LaTeX
    latex_content = generate_latex(questions, args.course, args.language)

    # Compile to PDF
    output_dir = Path(args.output)
    output_name = f"{args.course}_quiz_{args.language}"

    success = compile_pdf(latex_content, output_name, output_dir, args.language)

    if success:
        print(f"\n✓ Quiz PDF generated successfully!")
        sys.exit(0)
    else:
        print(f"\n✗ Failed to generate PDF")
        sys.exit(1)


if __name__ == '__main__':
    main()
