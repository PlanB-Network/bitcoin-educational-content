import json
import os
import time
from abc import ABC, abstractmethod
from openai import OpenAI
import deepl
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')
load_dotenv(ENV_PATH)

@dataclass
class TranslationConfig:
    source_lang: str
    target_lang: str
    source_translator_code: str
    target_translator_code: str

class BaseTranslator(ABC):
    @abstractmethod
    def translate_text(self, text: str) -> str:
        pass

class DeepLTranslator(BaseTranslator):
    def __init__(self, source_lang: str, target_lang: str):
        self.api_key = os.getenv('DEEPL_API_KEY')
        if not self.api_key:
            raise ValueError("DEEPL_API_KEY not found in environment variables")
        self.translator = deepl.Translator(self.api_key)
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.last_request_time = 0
        self.min_request_interval = 0.1

    def translate_text(self, text: str) -> str:
        if not text or not text.strip():
            return text
        
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()
        
        try:
            result = self.translator.translate_text(
                text,
                source_lang=self.source_lang,
                target_lang=self.target_lang,
                preserve_formatting=True
            )
            return str(result)
        except Exception as e:
            print(f"\nError translating text: {text}")
            print(f"Error: {e}")
            return text

class OpenAITranslator(BaseTranslator):
    def __init__(self, source_lang: str, target_lang: str):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key)
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.last_request_time = 0
        self.min_request_interval = 0.1

    def translate_text(self, text: str) -> str:
        if not text or not text.strip():
            return text
        
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are a translator from {self.source_lang} to {self.target_lang}. EXCLUSIVELY Translate the text exactly as provided, preserving formatting and special characters."},
                    {"role": "user", "content": text}
                ],
                temperature=0.1
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"\nError translating text: {text}")
            print(f"Error: {e}")
            return text

class DeepSeekTranslator(BaseTranslator):
    def __init__(self, source_lang: str, target_lang: str):
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.last_request_time = 0
        self.min_request_interval = 0.1

    def translate_text(self, text: str) -> str:
        if not text or not text.strip():
            return text
        
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()

        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": f"You are a translator from {self.source_lang} to {self.target_lang}. EXCLUSIVELY Translate the text exactly as provided, preserving formatting and special characters."},
                    {"role": "user", "content": text}
                ],
                temperature=0.1
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"\nError translating text: {text}")
            print(f"Error: {e}")
            return text


class FileTranslator:
    def __init__(self, config: TranslationConfig):
        self.config = config
        script_dir = os.path.dirname(os.path.abspath(__file__))
        lang_file = os.path.join(script_dir, 'supported_languages.json')
        
        try:
            with open(lang_file, 'r') as f:
                self.supported_languages = json.load(f)
        except FileNotFoundError:
            print(f"Could not find language file at: {lang_file}")
            raise
        
        lang = None
        for l in self.supported_languages['languages']:
            if l['code'] == config.target_lang:
                lang = l
                break
                
        if not lang:
            raise ValueError(f"Unsupported target language: {config.target_lang}")
        
        translator_type = lang['translator']
        if translator_type == "deepl":
            self.translator = DeepLTranslator(
                config.source_lang.upper(),
                config.target_translator_code
            )
        elif translator_type == "openai":
            self.translator = OpenAITranslator(
                config.source_translator_code,
                config.target_translator_code
            )
        else:
            raise ValueError(f"Unsupported translator type: {translator_type}")

    def translate_object(self, obj: Dict[str, Any]) -> Dict[str, Any]:
        """Translate an object based on its type and translation flag"""
        if not obj.get('translate', True):  # Skip if explicitly marked as non-translatable
            return obj.copy()
            
        new_obj = obj.copy()
        obj_type = obj.get('type')
        
        if obj_type == 'yml_property':
            if obj.get('is_list', False):
                # Translate each item in the list
                new_obj['content'] = [
                    self.translator.translate_text(str(item))
                    for item in obj['content']
                ]
            elif obj.get('is_multiline', False):
                # Translate each line of multiline content
                new_obj['content'] = [
                    self.translator.translate_text(str(line))
                    for line in obj['content']
                ]
            else:
                # Translate simple content
                content = obj.get('content')
                if content is not None:
                    new_obj['content'] = self.translator.translate_text(str(content))
                    
        elif obj_type in ['list', 'paragraph', 'markdown_header', 'quote']:
            content = obj.get('content')
            if content:
                new_obj['content'] = self.translator.translate_text(str(content))
                
        return new_obj

    def translate_file(self, input_path: Union[str, Path], output_path: Union[str, Path]) -> None:
        try:
            input_path = Path(input_path)
            output_path = Path(output_path)
            
            if not input_path.exists():
                raise FileNotFoundError(f"Input file not found: {input_path}")
            
            print(f"\nTranslating file:")
            print(f"From: {input_path}")
            print(f"To: {output_path}")
            
            with open(input_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
            
            total_objects = len(content)
            translated_content = []
            
            with tqdm(total=total_objects, desc="Translating", unit="obj") as pbar:
                for obj in content:
                    translated_obj = self.translate_object(obj)
                    translated_content.append(translated_obj)
                    pbar.update(1)
            
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(translated_content, f, ensure_ascii=False, indent=2)
            
            print(f"\nTranslation completed: {output_path}")
            print(f"Processed {total_objects} objects")
            
        except Exception as e:
            print(f"\nError processing file {input_path}")
            print(f"Error: {e}")
            raise

    @classmethod
    def translate_file_content(cls, 
                             input_path: Union[str, Path], 
                             output_path: Union[str, Path],
                             source_lang: str,
                             target_lang: str) -> Path:
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        lang_file = os.path.join(script_dir, 'translation_logic/supported_languages.json')
        
        with open(lang_file, 'r') as f:
            lang_config = json.load(f)
            
        source_info = next((l for l in lang_config['languages'] if l['code'] == source_lang), None)
        target_info = next((l for l in lang_config['languages'] if l['code'] == target_lang), None)
        
        if not source_info or not target_info:
            raise ValueError(f"Language not supported: source={source_lang}, target={target_lang}")
        
        config = TranslationConfig(
            source_lang=source_lang,
            target_lang=target_lang,
            source_translator_code=source_info['code_translator'],
            target_translator_code=target_info['code_translator']
        )
        
        translator = cls(config)
        translator.translate_file(input_path, output_path)
        
        return output_path
