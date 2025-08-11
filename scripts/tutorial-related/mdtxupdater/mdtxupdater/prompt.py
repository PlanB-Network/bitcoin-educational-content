from typing import List, Dict

LANGUAGE_NAMES_EN: Dict[str, str] = {
    "cs": "Czech", "de": "German", "en": "English", "es": "Spanish", "et": "Estonian",
    "fa": "Persian (Farsi)", "fi": "Finnish", "hi": "Hindi", "id": "Indonesian",
    "it": "Italian", "ja": "Japanese", "nb-NO": "Norwegian Bokmål", "nl": "Dutch",
    "pl": "Polish", "pt": "Portuguese", "ru": "Russian", "si": "Sinhala",
    "sr-Latn": "Serbian (Latin script)", "sv": "Swedish", "sw": "Swahili",
    "vi": "Vietnamese", "zh-Hans": "Chinese (Simplified)", "zh-Hant": "Chinese (Traditional)"
}

SOURCE_LANG_NAMES_EN: Dict[str, str] = {
    "en": "English", "fr": "French", "es": "Spanish", "de": "German", "it": "Italian"
}

ORDERED_CODES: List[str] = [
    "cs","de","en","es","et","fa","fi","hi","id","it","ja","nb-NO","nl",
    "pl","pt","ru","si","sr-Latn","sv","sw","vi","zh-Hans","zh-Hant"
]


def generate_llm_prompt(source_lang: str) -> str:
    """
    Generate an English prompt instructing a professional translation into all
    supported languages, with strict formatting and JSON output.
    The source language phrase is adapted based on `source_lang`.
    """
    src_name = SOURCE_LANG_NAMES_EN.get(source_lang, "French")
    # Build the LANGUAGES section
    lang_lines = []
    for code in ORDERED_CODES:
        name = LANGUAGE_NAMES_EN.get(code, code)
        lang_lines.append(f"- {code} : {name}")

    # Build the JSON skeleton
    json_lines = []
    json_lines.append('{')
    json_lines.append('  "source_text": "[original source text]",')
    json_lines.append('  "translations": {')
    for i, code in enumerate(ORDERED_CODES):
        comma = "," if i < len(ORDERED_CODES) - 1 else ""
        name = LANGUAGE_NAMES_EN.get(code, code)
        json_lines.append(f'    "{code}": "[{name} translation]"{comma}')
    json_lines.append('  }')
    json_lines.append('}')
    json_block = "\n".join(json_lines)

    prompt = f"""You are a professional translator. I will provide you with a text in {src_name} that you must translate into ALL the languages listed below.

CRITICAL INSTRUCTIONS:
- Translate the text into ALL {len(ORDERED_CODES)} target languages without exception.
- Preserve EXACT formatting (line breaks, spaces, indentation...).
- DO NOT translate:
    - YAML keys
    - HTML/Markdown tags
    - File paths
    - Variables inside {{ {{ }} }}
    - https links and URLs
- Translate ONLY the textual content.
- Respond as a single valid JSON code block — no text before or after.

TARGET LANGUAGES (in this exact order):
{chr(10).join(lang_lines)}

OUTPUT FORMAT:
Return ONLY a valid JSON:
{json_block}

TEXT TO TRANSLATE:
[PASTE YOUR TEXT HERE]
"""
    return prompt
