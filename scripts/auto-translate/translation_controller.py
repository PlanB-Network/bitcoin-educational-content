import sys
import json
import os
from pathlib import Path
from typing import Optional, Union, Dict
from json_content_conversion.convert_json import JsonConverter
from json_content_conversion.reverse_conversion_json import JsonToMarkdownConverter
from translation_logic.translate_json import FileTranslator

CACHE_DIR = Path(os.path.dirname(os.path.abspath(__file__))) / 'json_content_conversion' / 'cache'

def get_language_from_filename(filepath: Union[str, Path]) -> str:
    return Path(filepath).stem.split('.')[-1]

def create_cache_name(input_path: Union[str, Path]) -> str:
    path = Path(input_path)
    parts = [part for part in path.parts if part != '.' and part != '..']
    return '_'.join(parts)

def translate_content(input_path: Union[str, Path], 
                     target_lang: str,
                     cache_dir: Optional[Path] = None) -> Path:
    input_path = Path(input_path)
    source_lang = get_language_from_filename(input_path)
    
    if cache_dir is None:
        cache_dir = CACHE_DIR
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    cache_base_name = create_cache_name(input_path)
    source_json = cache_dir / f"{cache_base_name}.json"
    translated_json = cache_dir / f"{cache_base_name}_{target_lang}.json"
    
    output_path = input_path.parent / f"{target_lang}{''.join(input_path.suffixes)}"
    
    print(f"Converting {input_path} to JSON...")
    JsonConverter.convert_file_to_json(input_path, source_json)
    
    print(f"Translating from {source_lang} to {target_lang}...")
    FileTranslator.translate_file_content(
        input_path=source_json,
        output_path=translated_json,
        source_lang=source_lang,
        target_lang=target_lang
    )
    
    print(f"Converting back to {output_path.suffix[1:]}...")
    final_path = JsonToMarkdownConverter.convert_file_to_markdown(
        translated_json,
        output_path
    )
    
    return final_path

def main():
    if len(sys.argv) != 3:
        print("Usage: python translation_controller.py <input_file> <target_lang>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    target_lang = sys.argv[2]
    
    try:
        output_path = translate_content(input_file, target_lang)
        print(f"Translation completed successfully. Output saved to: {output_path}")
    except Exception as e:
        print(f"Error during translation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
