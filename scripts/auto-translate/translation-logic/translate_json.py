import json
import os
import time
import deepl
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

@dataclass
class TranslationConfig:
    source_lang: str
    target_lang: str

class FileTranslator:
    # Define which types and fields should be translated
    TRANSLATABLE_TYPES = {
        'yml_property': ['content'],
        'list': ['content'],
        'paragraph': ['content'],
        'markdown_header': ['content'],
        'quote': ['content'],
        'snippet': [],  # Don't translate code snippets
        'equation': []  # Don't translate equations
    }
    
    def __init__(self, config: TranslationConfig):
        self.config = config
        api_key = os.getenv('DEEPL_API_KEY')
        if not api_key:
            raise ValueError("DEEPL_API_KEY not found in environment variables")
        self.translator = deepl.Translator(api_key)
        self.last_request_time = 0
        self.min_request_interval = 0.1  # 100ms between requests to avoid rate limits

    def translate_text(self, text: str) -> str:
        """Translate text using DeepL API."""
        if not text or not text.strip():
            return text
            
        # Rate limiting
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()
            
        try:
            result = self.translator.translate_text(
                text,
                source_lang=self.config.source_lang,
                target_lang=self.config.target_lang,
                preserve_formatting=True
            )
            return str(result)
        except Exception as e:
            print(f"\nError translating text: {text}")
            print(f"Error: {e}")
            return text

    def translate_object(self, obj: Dict[str, Any]) -> Dict[str, Any]:
        """Translate a single content object based on its type."""
        obj_type = obj.get('type')
        
        # Skip if type is not translatable
        if obj_type not in self.TRANSLATABLE_TYPES:
            return obj.copy()
        
        new_obj = obj.copy()
        fields_to_translate = self.TRANSLATABLE_TYPES[obj_type]
        
        # Skip empty fields list (non-translatable types)
        if not fields_to_translate:
            return new_obj
            
        for field in fields_to_translate:
            if field in obj:
                content = obj[field]
                if content:  # Only translate non-empty content
                    new_obj[field] = self.translate_text(str(content))
                    
        return new_obj

    def translate_file(self, input_path: Union[str, Path], output_path: Union[str, Path]) -> None:
        """
        Translate a JSON file from input_path to output_path.
        
        Args:
            input_path: Path to the input JSON file
            output_path: Path where the translated JSON should be saved
        """
        try:
            input_path = Path(input_path)
            output_path = Path(output_path)
            
            # Ensure input file exists
            if not input_path.exists():
                raise FileNotFoundError(f"Input file not found: {input_path}")
            
            print(f"\nTranslating file:")
            print(f"From: {input_path}")
            print(f"To: {output_path}")
            
            # Read source content
            with open(input_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
            
            total_objects = len(content)
            translated_content = []
            
            # Process each object with progress bar
            with tqdm(total=total_objects, desc="Translating", unit="obj") as pbar:
                for obj in content:
                    translated_obj = self.translate_object(obj)
                    translated_content.append(translated_obj)
                    pbar.update(1)
            
            # Create output directory if it doesn't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save translated content
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(translated_content, f, ensure_ascii=False, indent=2)
                
            print(f"\nTranslation completed: {output_path}")
            print(f"Processed {total_objects} objects")
            
        except Exception as e:
            print(f"\nError processing file {input_path}")
            print(f"Error: {e}")
            raise

def main():
    # Configuration
    config = TranslationConfig(
        source_lang="EN",  # DeepL language codes: FR, EN, DE, etc.
        target_lang="IT"
    )
    
    # Initialize translator
    translator = FileTranslator(config)
    
    # Setup default paths
    script_dir = Path(__file__).parent
    input_file = "lnp201_en.json"  # Change this for different files
    input_path = script_dir / "inputs" / input_file
    output_path = script_dir / "output" / f"{input_file.rsplit('.', 1)[0]}_{config.target_lang.lower()}.json"
    
    try:
        # Translate the file
        translator.translate_file(input_path, output_path)
        print("\nTranslation process completed successfully!")
    except Exception as e:
        print(f"\nTranslation process failed: {e}")

if __name__ == "__main__":
    main()
