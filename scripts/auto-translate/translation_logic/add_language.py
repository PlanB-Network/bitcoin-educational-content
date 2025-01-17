import json
import argparse
from pathlib import Path
from typing import Dict, Optional
import readline

def load_supported_languages() -> Dict:
   config_path = Path(__file__).parent / 'supported_languages.json'
   try:
       with open(config_path, 'r', encoding='utf-8') as f:
           return json.load(f)
   except FileNotFoundError:
       return {"languages": []}
   except json.JSONDecodeError as e:
       print(f"Error parsing supported_languages.json: {e}")
       raise

def display_current_languages():
   config = load_supported_languages()
   languages = config.get('languages', [])
   
   print("\n=== Current Supported Languages ===")
   print(f"Total languages: {len(languages)}\n")
   
   for lang in sorted(languages, key=lambda x: x['code'].lower()):
       print(f"{lang['code']:<8} : {lang['name']:<20} ({lang['translator']})")
   print()

def save_supported_languages(config: Dict) -> None:
   config['languages'].sort(key=lambda x: x['code'].lower())
   
   config_path = Path(__file__).parent / 'supported_languages.json'
   with open(config_path, 'w', encoding='utf-8') as f:
       json.dump(config, f, indent=2, ensure_ascii=False)

def language_exists(config: Dict, code: str) -> bool:
   return any(lang['code'] == code for lang in config['languages'])

def validate_language_code(code: str) -> bool:
   return (
       len(code) >= 2 and 
       (len(code) <= 7 or '-' in code) and 
       all(c.isalnum() or c in '-' for c in code)
   )

def select_translator() -> str:
   providers = {
       '1': 'deepl',
       '2': 'openai'
   }
   
   print("\nAvailable translator providers:")
   for key, provider in providers.items():
       print(f"{key}. {provider}")
   
   while True:
       choice = input("\nSelect translator provider (1-2): ").strip()
       if choice in providers:
           return providers[choice]
       print("Invalid choice. Please try again.")

def prompt_for_language_info() -> tuple:
   display_current_languages()
   print("\n=== Add New Language ===")
   
   while True:
       code = input("Enter language code (e.g., en, zh-Hans): ").strip()
       if validate_language_code(code):
           break
       print("Invalid language code format. Please try again.")
   
   name = input("Enter language name (e.g., English): ").strip()
   while not name:
       print("Language name cannot be empty.")
       name = input("Enter language name (e.g., English): ").strip()
   
   name = ' '.join(word.capitalize() for word in name.split())
   
   translator = select_translator()
   
   print("\nEnter translator-specific language code")
   print("(press Enter to auto-generate from language code)")
   code_translator = input(f"Translator code [{code.upper()}]: ").strip()
   code_translator = code_translator if code_translator else code.upper()
   
   return code, name, translator, code_translator

def add_language(
   code: str,
   name: str,
   translator: str = "deepl",
   code_translator: Optional[str] = None,
   interactive: bool = False
) -> None:
   if not validate_language_code(code):
       raise ValueError(f"Invalid language code format: {code}")

   config = load_supported_languages()

   if language_exists(config, code):
       if interactive:
           print(f"\nWarning: Language with code '{code}' already exists.")
           if input("Do you want to overwrite it? (y/n): ").lower() != 'y':
               print("Operation cancelled.")
               return
       else:
           raise ValueError(f"Language with code '{code}' already exists")

   if not code_translator:
       code_translator = code.upper()

   new_language = {
       "code": code,
       "name": name,
       "translator": translator,
       "code_translator": code_translator
   }

   config['languages'] = [lang for lang in config['languages'] if lang['code'] != code]
   
   config['languages'].append(new_language)

   if interactive:
       print("\nNew language entry:")
       print(f"  Code: {code}")
       print(f"  Name: {name}")
       print(f"  Translator: {translator}")
       print(f"  Translator Code: {code_translator}")
       
       if input("\nSave this entry? (y/n): ").lower() != 'y':
           print("Operation cancelled.")
           return

   save_supported_languages(config)
   print(f"\nSuccessfully added {name} ({code}) to supported languages")
   display_current_languages()

def main():
   parser = argparse.ArgumentParser(description='Add a new language to supported_languages.json')
   parser.add_argument('-i', '--interactive', action='store_true', 
                       help='Run in interactive mode')
   parser.add_argument('code', nargs='?', help='Language code (e.g., en, zh-Hans)')
   parser.add_argument('name', nargs='?', help='Language name (e.g., English)')
   parser.add_argument('--translator', help='Translator service (default: deepl)')
   parser.add_argument('--code-translator', help='Translator-specific language code')

   args = parser.parse_args()

   try:
       if args.interactive or not (args.code and args.name):
           code, name, translator, code_translator = prompt_for_language_info()
           add_language(code, name, translator, code_translator, interactive=True)
       else:
           name = ' '.join(word.capitalize() for word in args.name.split())
           add_language(
               code=args.code,
               name=name,
               translator=args.translator or 'deepl',
               code_translator=args.code_translator,
               interactive=False
           )
   except Exception as e:
       print(f"Error: {e}")
       exit(1)

if __name__ == "__main__":
   main()
