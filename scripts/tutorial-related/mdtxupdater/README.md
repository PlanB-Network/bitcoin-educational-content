# Markdown Translation Updater (mdtxupdater)

Update localized Markdown files using JSON translations, with robust anchors, whitespace-safe edits, and a preview step that reduces mistakes. Ships with a simple Tkinter GUI and an interactive CLI. Cross-platform (Windows, macOS, Linux) and zero external dependencies.

## Key Features

* Flexible anchors to bound the edit section:

  * `START` and `END`
  * Exact image filenames (e.g., `001.webp`, `54.webp`)
  * Chapter UUID markers (e.g., `<chapterId>e4f1c2d3-…</chapterId>` or the bare UUID)
  * Fenced code blocks (the tool matches the most similar block across languages)
* Whitespace preservation around the edited section (prevents broken headings or spacing)
* Paragraphs counted as non-empty lines (simple, predictable indexing)
* Preview on a reference language file before applying changes (choose `en`, `fr`, `es`, `de`, or `it`)
* Built-in generator for a fully formatted LLM translation prompt (English)
* CLI and GUI (Tkinter) included

## Supported Languages

The application looks for files named after the following language codes in the target folder:

`cs`, `de`, `en`, `es`, `et`, `fa`, `fi`, `hi`, `id`, `it`, `ja`, `nb-NO`, `nl`, `pl`, `pt`, `ru`, `si`, `sr-Latn`, `sv`, `sw`, `vi`, `zh-Hans`, `zh-Hant`.

Only the languages that have a corresponding `<lang>.md` file in the folder will be updated.

## Reference Language (Preview)

Choose the file used for preview context among: `en`, `fr`, `es`, `de`, `it`. If the chosen one is missing, the tool falls back to `en`, then `fr`, then any available file.

## Installation

Prerequisites:

* Python 3.10+
* Tkinter (included in standard Python on Windows and macOS; on some Linux distributions you may need to install `python3-tk`)

Install from the project root:

* Editable install: `python -m pip install -e .`
* On macOS/Linux you may prefer: `python3 -m pip install -e .`

No external dependencies are required.

## Quick Start (CLI)

Run `mdtxupdater` and follow the prompts:

1. Folder path containing the Markdown files
2. Reference language for preview (`en`, `fr`, `es`, `de`, `it`)
3. Update mode: Replace or Append
4. LOWER bound (multiline input)
5. UPPER bound (multiline input)
6. Paragraph number (counted across non-empty lines)
7. Optional: auto-generate the LLM prompt
8. Paste the translations JSON (must include the `translations` key)
9. Files are updated and a summary is displayed

Example to pre-set some options: `mdtxupdater -d "/path/to/tutorial" --ref-lang en`

## Quick Start (GUI)

Run `mdtxupdater-gui`.

* Select the Markdown folder and a reference language
* Choose mode (Replace/Append) and the paragraph number
* Paste LOWER and UPPER bounds (multiline fields)
* Paste the translations JSON
* Click “Preview” to verify placement on the reference file
* Click “Run Update” to apply changes
* Click “Generate LLM Prompt” to get a copy-ready translation prompt in English

## How Bounds Work

You provide two inputs: a LOWER bound and an UPPER bound. The tool finds these anchors in each file and edits only the text between them.

Accepted forms:

* `START` or `END`
* Image filename: `001.webp` (exact filename; Markdown and `<img>` HTML forms are supported)
* Chapter UUID: either the full tag `<chapterId>uuid</chapterId>` or the bare UUID string
* Code block: paste the entire fenced block; the tool will find the most similar fenced code block in the file (helpful when code differs slightly across languages)

Search flow:

* The LOWER bound is resolved first; the UPPER bound search starts from there
* For images and chapters:

  * LOWER bound resolves to the end of the marker (so the section starts after it)
  * UPPER bound resolves to the start of the marker (so the section ends before it)
* For code blocks: the tool compares the pasted code to all fenced code blocks and picks the most similar one

## Paragraph Counting

Inside the bounded section, paragraphs are counted as non-empty lines:

* Replace mode: paragraph N replaces the N-th non-empty line
* Append mode: the new text is inserted before paragraph N (use a number greater than the count to append at the end)

This approach avoids ambiguity with blank lines.

## JSON Input Format

You will paste a JSON object containing at least a `translations` key:

{
"source\_text": "original content (optional)",
"translations": {
"<lang>": "translated text",
"en": "…",
"fr": "…",
"es": "…",
"…": "…"
}
}

Only languages present in the folder are updated. Missing keys are reported.

## LLM Prompt Generator

The tool can produce a ready-to-copy English prompt that instructs a professional translation into all supported languages, with strict formatting and a JSON-only output.

* CLI: after preview confirmation you can choose to generate the prompt
* GUI: use the “Generate LLM Prompt” button
* The source language label in the prompt is automatically aligned with your chosen reference language (e.g., “I will provide you a text in French/English/…”)

## Cross-Platform Notes

* Windows/macOS: Tkinter ships with the standard Python installer
* Linux: install your distribution’s Tkinter package (e.g., `sudo apt-get install python3-tk`)
* Paths and encodings: the tool reads and writes UTF-8; filenames follow the exact language codes (case matters)

## Typical Workflow

1. Choose the folder and reference language
2. Pick Replace or Append and the paragraph number
3. Provide LOWER and UPPER bounds (e.g., `START` and the first chapter ID, or two image filenames, or a code block and `END`)
4. Preview and confirm placement
5. Generate the LLM prompt (optional)
6. Paste the returned JSON and run the update
7. Commit your changes in Git per tutorial/module as needed

## Error Handling and Safety

* Preview required: always inspect the preview before applying changes
* Whitespace is preserved around the bounded section, so structure such as headings or chapter tags remains intact
* If a bound is not found, you’ll get a clear error indicating which anchor failed
* For code blocks, the tool uses similarity scoring to find the closest fenced block; verify via preview if you expect multiple similar blocks

## Project Layout

* `src/mdtxupdater/core.py`: core engine (anchors, preview, updates)
* `src/mdtxupdater/cli.py`: interactive command-line interface
* `src/mdtxupdater/gui.py`: Tkinter GUI
* `src/mdtxupdater/prompt.py`: LLM prompt builder
* `pyproject.toml`: packaging and entry points
* `requirements.txt`: intentionally empty (standard library only)
* `README.md`: this document

## Contributing

* Use conventional commits and open focused pull requests
* Keep changes platform-agnostic and dependency-free unless there is a compelling reason
* Add tests or sample fixtures where applicable (e.g., small Markdown sets) and document edge cases

## Versioning and License

* Versioning follows semantic versioning (major.minor.patch)
* License: MIT

## FAQ

**Does it modify `fr.md` differently?**
No. All languages are treated uniformly. You can select any supported reference language for preview; the update applies to all languages present in the folder and provided in the JSON.

**What if my code blocks differ slightly between languages?**
Paste the full fenced block as a bound. The tool scores all fenced blocks and picks the most similar one. Always verify with the preview.

**How are “paragraphs” defined?**
As non-empty lines within the bounded section. This avoids ambiguity with blank lines.

**How do I avoid breaking layout around chapter IDs or headings?**
The tool preserves leading and trailing whitespace around the bounded section, keeping newlines intact (e.g., leaving a blank line before `<chapterId>…</chapterId>`).

**Can I add new languages?**
Yes. Add the new `<lang>.md` file(s). If you want the updater to search for that language by default, add the code to the supported list in the application core, then include it in your JSON under `translations`.

