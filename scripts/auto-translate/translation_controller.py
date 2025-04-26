import sys
import json
import os
from pathlib import Path
from typing import Optional, Union, Dict
from json_content_conversion.json_conversion import JsonConverter
from json_content_conversion.json_reverse_conversion import JsonToFileConverter
from translation_logic.translate_json import FileTranslator

CACHE_DIR = Path(os.path.dirname(os.path.abspath(__file__))) / 'json_content_conversion' / 'cache'

def get_language_from_filename(filepath: Union[str, Path]) -> str:
    """Extract language code from filename."""
    return Path(filepath).stem.split('.')[0]

def create_cache_name(input_path: Union[str, Path]) -> str:
    """Create a cache filename from input path."""
    path = Path(input_path)
    parts = [part for part in path.parts if part != '.' and part != '..']
    return '_'.join(parts)

def translate_content(input_path: Union[str, Path], 
                     target_lang: str,
                     output_path: Optional[Union[str, Path]] = None) -> Path:
    """Translate content using JSON-based conversion and translation."""
    input_path = Path(input_path)
    source_lang = get_language_from_filename(input_path)
    
    # Ensure cache directory exists
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    cache_base_name = create_cache_name(input_path)
    source_json = CACHE_DIR / f"{cache_base_name}.json"
    translated_json = CACHE_DIR / f"{cache_base_name}_{target_lang}.json"
    
    # Determine output path
    if output_path is None:
        output_path = input_path.parent / f"{target_lang}{input_path.suffix}"
    else:
        output_path = Path(output_path)
    
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
    final_path = JsonToFileConverter.convert_file(
        translated_json,
        output_path
    )
    
    # Clean up cache files
    # if source_json.exists():
    #     os.remove(source_json)
    # if translated_json.exists():
    #     os.remove(translated_json)
    
    return final_path

def main():
    """Main entry point for translation controller."""
    if len(sys.argv) not in [3, 4]:
        print("Usage: python translation_controller.py <input_file> <target_lang> [output_file]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    target_lang = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    try:
        output_path = translate_content(input_file, target_lang, output_file)
        print(f"Translation completed successfully. Output saved to: {output_path}")
    except Exception as e:
        print(f"Error during translation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
