# Quiz to PDF Generator

Converts quiz YML files to PDF with randomized answer order and answer key.

## Requirements

- Python 3.6+
- PyYAML
- XeLaTeX or LuaLaTeX (for IBM Plex font support)
- **IBM Plex fonts included** in the repository (no additional font installation needed)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install LaTeX (if not already installed):
   - **Ubuntu/Debian**:
     ```bash
     sudo apt-get install texlive-xetex texlive-luatex
     ```
   - **macOS**:
     ```bash
     brew install mactex
     ```
   - **Windows**: Download from [miktex.org](https://miktex.org/)
     - XeLaTeX/LuaLaTeX is included in the default installation

## Usage

### Basic Usage

Generate quiz PDF for a course in English (default):
```bash
python quizz_to_pdf.py btc101
```

### With Language Selection

Generate quiz in French:
```bash
python quizz_to_pdf.py btc101 -l fr
```

Generate quiz in Spanish:
```bash
python quizz_to_pdf.py eco204 -l es
```

### Custom Output Directory

```bash
python quizz_to_pdf.py btc101 -l en -o ./my_output
```

### List Available Courses

```bash
python quizz_to_pdf.py --list-courses
```

## Available Languages

The script supports all languages available in the quiz files using **IBM Plex fonts** (included in repository):

### Latin Script Languages
Uses **IBM Plex Sans**:
- `en` - English (default)
- `fr` - French
- `es` - Spanish
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `nl` - Dutch
- `pl` - Polish
- `cs` - Czech
- `sv` - Swedish
- `fi` - Finnish
- `et` - Estonian
- `tr` - Turkish
- `ru` - Russian (Cyrillic)
- And others...

### Non-Latin Script Languages
Uses **IBM Plex specialized variants**:
- `hi` - Hindi (Devanagari) - IBM Plex Sans Devanagari
- `ja` - Japanese - IBM Plex Sans JP
- `ko` - Korean - IBM Plex Sans KR
- `zh-Hans` - Chinese (Simplified) - IBM Plex Sans TC
- `zh-Hant` - Chinese (Traditional) - IBM Plex Sans TC
- `ar` - Arabic - IBM Plex Sans Arabic
- `fa` - Persian - IBM Plex Sans Arabic
- `th` - Thai - IBM Plex Sans Thai

## Output

The script generates:
1. **Quiz questions** with randomized answer order (A, B, C, D)
2. **Answer key** at the end with correct answers and explanations

Output files:
- `{course}_quiz_{language}.tex` - LaTeX source
- `{course}_quiz_{language}.pdf` - Final PDF

## Examples

### Single Course
```bash
# Generate BTC101 quiz in English
python3 quizz_to_pdf.py btc101

# Generate ECO204 quiz in French
python3 quizz_to_pdf.py eco204 -l fr

# Custom output location
python3 quizz_to_pdf.py btc101 -o ~/Desktop/quizzes
```

### Multiple Courses (Batch)
```bash
# Generate multiple courses in English
./batch_generate.sh btc101 btc102 btc202

# Generate multiple courses in French
./batch_generate.sh -l fr btc101 eco204 his201

# Custom output directory
./batch_generate.sh -l es -o ./spanish_quizzes btc101 btc102
```

## Features

- ✅ Automatic quiz discovery from course directories
- ✅ Answer randomization for each question
- ✅ Answer key with explanations
- ✅ Professional PDF formatting with IBM Plex fonts
- ✅ Multi-language support (Latin and non-Latin scripts)
- ✅ Consistent typography across all languages
- ✅ Page numbering and headers
- ✅ Clean auxiliary file cleanup
- ✅ No additional font installation required (fonts included)

## Troubleshooting

**Error: PyYAML is required**
```bash
pip install pyyaml
```

**Error: Neither xelatex nor lualatex found**
- Install Unicode LaTeX engines:
  - Ubuntu/Debian: `sudo apt-get install texlive-xetex texlive-luatex`
  - macOS: `brew install mactex`
  - Windows: Install MikTeX from [miktex.org](https://miktex.org/)

**Characters showing as boxes**
- IBM Plex fonts are included in the `fonts/` directory and load automatically
- Ensure XeLaTeX or LuaLaTeX is installed (required for fontspec package)
- Check that the `fonts/TrueType/` directory exists and contains IBM Plex fonts

**Error: No quiz questions found**
- Verify the course code is correct
- Check if quiz files exist for the specified language
- Use `--list-courses` to see available courses

## Directory Structure

Expected quiz file structure:
```
courses/
├── btc101/
│   └── quizz/
│       ├── 000/
│       │   ├── en.yml
│       │   ├── fr.yml
│       │   └── ...
│       ├── 001/
│       └── ...
├── eco204/
└── ...
```

## Quiz File Format

Each quiz YML file should contain:
```yaml
question: "Question text here?"
answer: "Correct answer"
wrong_answers:
  - "Wrong answer 1"
  - "Wrong answer 2"
  - "Wrong answer 3"
explanation: |
  Optional explanation text that appears in the answer key.
reviewed: true
```
