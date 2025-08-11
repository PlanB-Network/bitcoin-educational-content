# Markdown Translation Updater

This Python app with a GUI allows you to modify or add paragraphs in all translations of a specific piece of content (course or tutorial) in a markdown file, based on a source language that has been updated, using a translation JSON in conjunction with an LLM:
* flexible bounds to locate the paragraph (START/END, `.webp` image, `<chapterId>…</chapterId>` tag, code block),
* preview on a reference file,
* generation of a ready-to-use LLM translation prompt.

## Prerequisites

* Python 3.10+
* Tkinter (included on Windows/macOS; on Linux: `python3-tk` via your package manager)

## Launch

Run `run.py`

## Usage

- **Folder**: select the folder of the content to modify (course or tutorial).

- **Reference language**: choose `en`, `fr`, `es`, `de`, or `it`. This is the source language in which you have already manually made the content modification.

- **Mode**:
  - *Replace*: replaces an existing paragraph (non-empty line no. N)
  - *Append*: inserts before paragraph no. N (or at the end if N exceeds)

- **Bounds**: paste the **LOWER bound** then the **UPPER bound**. This defines the area in which you will search for the target paragraph. Try to define the smallest possible area to reduce errors. Accepted formats:
  - `START` / `END` (start or end of the complete markdown file)
  - `001.webp` (exact image file name. Just the name, not the path)
  - `<chapterId>UUID</chapterId>` or the UUID alone
  - complete code block with 3 backticks (for code blocks only, a similarity search is performed, and the software will take the most similar block in all the content. This avoids blocking everything in case of a translation of a code comment or micro-change in one language).

- **Paragraph number**: select the number of the paragraph to replace (*Replace mode*) or the paragraph before which you want to add the new paragraph (*Append mode*). You can adjust this number based on the **Preview** result.

- **Original paragraph**: paste the paragraph (either the new paragraph to add or the paragraph after modification) in the language in which the modification was made (the same language as the one selected at the top of the GUI).

- **Copy LLM Prompt**: click this button. The adapted English prompt is copied to your clipboard.

- Paste your prompt into an LLM chatbot to get the translation (tested with ChatGPT-4o and ChatGPT-5). Check that the LLM returns the complete JSON file with all translations, not cut off.

- Paste your JSON into **Translations JSON**.

- **Preview** to check the placement in the logs to ensure the modification will be in the correct spot in the translations. If needed, adjust the **Paragraph number** parameter, then click "Preview" again. You can select the language in which you want to see the preview (do not select the original language—it makes no sense ^^).

- **Run Update** to write the translations.

## Tips

* If a bound is not found, adjust it (exact image name, correct UUID, complete code block).
* In *Replace mode*, make sure to preview the targeted paragraph before applying.
* In *Append mode*, use a number beyond the last paragraph of your section to add at the end of the section.

If you have any questions, feel free to contact me (Loïc)