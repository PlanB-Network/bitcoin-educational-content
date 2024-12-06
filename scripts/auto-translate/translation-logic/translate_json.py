import json
import os
import time
import anthropic
from typing import Dict, Any, List
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables from .env file in parent directory
load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

@dataclass
class TranslationConfig:
    source_lang: str
    target_lang: str
    
class MarkdownTranslator:
    TRANSLATABLE_TYPES = {
        'yml_property': ['content'],
        'list': ['content'],
        'paragraph': ['value'],
        'markdown_header': ['value'],
        'quote': ['content']
    }
    
    def __init__(self, config: TranslationConfig):
        self.config = config
        api_key = os.getenv('CLAUDE_API_KEY')
        if not api_key:
            raise ValueError("CLAUDE_API_KEY not found in environment variables")
        self.client = anthropic.Client(api_key=api_key)
        self.last_request_time = 0
        self.min_request_interval = 1  # Minimum time between requests in seconds
        
    def create_translation_prompt(self, text: str) -> str:
        return f"""Translate the following text from {self.config.source_lang} to {self.config.target_lang}. 
Provide only the direct translation without any explanations or additional context.
Keep all markdown formatting intact. Preserve any technical terms, proper nouns, and code snippets unchanged.

Text to translate:
{text}

Translation:"""

    def translate_text(self, text: str) -> str:
        if not text.strip():
            return text
            
        # Add rate limiting
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()
            
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                temperature=0.1,
                messages=[{
                    "role": "user",
                    "content": self.create_translation_prompt(text)
                }]
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"Error translating text: {text}")
            print(f"Error: {e}")
            print(f"Error type: {type(e)}")
            return text
            
    def translate_object(self, obj: Dict[str, Any]) -> Dict[str, Any]:
        obj_type = obj.get('type')
        
        if obj_type not in self.TRANSLATABLE_TYPES:
            return obj.copy()
            
        new_obj = obj.copy()
        fields_to_translate = self.TRANSLATABLE_TYPES[obj_type]
        
        for field in fields_to_translate:
            if field in obj:
                # Handle nested content in yml_property
                if obj_type == 'yml_property' and isinstance(obj[field], list):
                    new_obj[field] = []
                    for item in obj[field]:
                        translated_item = self.translate_text(str(item))
                        new_obj[field].append(translated_item)
                else:
                    new_obj[field] = self.translate_text(str(obj[field]))
                    
                # Update value field for yml_property if content was translated
                if obj_type == 'yml_property' and field == 'content':
                    new_obj['value'] = f"{obj['key']}: {new_obj[field]}"
                    
        return new_obj
        
    def translate_file(self, input_path: str, output_path: str):
        try:
            print(f"Reading input file: {input_path}")
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            total_objects = len(data)
            print(f"\nStarting translation of {total_objects} objects...")
            translated_objects = []
            
            # Create progress bar
            with tqdm(total=total_objects, desc="Translating", unit="obj") as pbar:
                for obj in data:
                    translated_obj = self.translate_object(obj)
                    translated_objects.append(translated_obj)
                    pbar.update(1)
                    
                    # Optional: display current object type
                    pbar.set_postfix({'type': obj.get('type', 'unknown')})
                
            print(f"\nCreating output directory: {output_path}")
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                
            print("Writing translated content...")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(translated_objects, f, ensure_ascii=False, indent=2)
                
            print(f"\nTranslation completed: {output_path}")
            print(f"Processed {total_objects} objects")
            
        except Exception as e:
            print(f"\nError processing file: {input_path}")
            print(f"Error: {e}")
            raise

def main():
    # Configuration
    config = TranslationConfig(
        source_lang="English",
        target_lang="French",  # Change this for different target languages
    )
    
    translator = MarkdownTranslator(config)
    
    # File paths
    script_dir = Path(__file__).parent
    input_file = script_dir.parent / "json-content-conversion" / "output.json"
    output_dir = script_dir / "output"
    output_file = output_dir / f"content_{config.target_lang.lower()}.json"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    translator.translate_file(str(input_file), str(output_file))

if __name__ == "__main__":
    main()
