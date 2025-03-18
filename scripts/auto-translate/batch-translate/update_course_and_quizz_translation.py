import os
import sys
import shutil
import subprocess
from pathlib import Path
from functools import wraps
from typing import List, Callable, Any, Optional, Set
from dataclasses import dataclass

@dataclass
class TranslationConfig:
    """Configuration class for translation settings."""
    script_dir: Path = Path(__file__).resolve().parent
    project_root: Path = script_dir.parent.parent.parent
    excluded_subfolders: Set[str] = frozenset({'his204', 'biz221'})  
    to_en_dir: Path = script_dir / "translate-to-en"
    from_en_dir: Path = script_dir / "translate-from-en"

class TranslationManager:
    """Manages the translation process for course content."""
    
    def __init__(self, config: TranslationConfig):
        self.config = config
        self.setup_directories()

    def setup_directories(self) -> None:
        """Initialize required directories."""
        self.config.to_en_dir.mkdir(parents=True, exist_ok=True)
        self.config.from_en_dir.mkdir(parents=True, exist_ok=True)

    def cleanup(self) -> None:
        """Remove temporary translation directories."""
        shutil.rmtree(self.config.to_en_dir, ignore_errors=True)
        shutil.rmtree(self.config.from_en_dir, ignore_errors=True)
        print("Cleaned up temporary directories")

    def get_supported_languages(self) -> List[str]:
        """Get list of supported languages from course directory."""
        directory = self.config.project_root / "courses" / "lnp201"
        if not directory.exists():
            print("Course directory does not exist")
            return []
        
        return [
            filename.split(".")[0]
            for filename in os.listdir(directory)
            if filename.endswith(".md") and filename != "en.md"
        ]

    def is_excluded_path(self, path: str) -> bool:
        """Check if path contains any excluded subfolder."""
        path_parts = Path(path).parts
        return any(excluded in path_parts for excluded in self.config.excluded_subfolders)

    def content_exists(self, filenames: List[str], lang: str) -> bool:
        """Check if content exists for a specific language."""
        return any(f.endswith(f"{lang}.md") or f.endswith(f"{lang}.yml") for f in filenames)

    def create_translation_list(self, source_lang: str, target_lang: str) -> None:
        """Create list of files needing translation."""
        base_dir = self.config.project_root / "courses"
        output_dir = (self.config.to_en_dir if target_lang == 'en' 
                     else self.config.from_en_dir)
        output_file = output_dir / f"{source_lang if target_lang == 'en' else target_lang}.txt"
        file_written = False

        with open(output_file, "w") as f:
            for dirpath, _, filenames in os.walk(base_dir):
                if self.is_excluded_path(dirpath):
                    continue
                
                for filename in filenames:
                    if (filename.startswith(f"{source_lang}.") and 
                        not self.content_exists(filenames, target_lang)):
                        file_path = Path(dirpath) / filename
                        relative_path = os.path.relpath(file_path, self.config.script_dir)
                        f.write(f"{relative_path}\n")
                        file_written = True

        if not file_written:
            output_file.unlink(missing_ok=True)
            print(f"No translations needed from {source_lang} to {target_lang}")

    def translate_file(self, input_file: str, target_lang: str) -> None:
        """Translate a single file."""
        try:
            translation_controller = self.config.script_dir.parent / "translation_controller.py"
            command = ["python3", str(translation_controller), input_file, target_lang]
            subprocess.run(command, check=True)
            print(f"Translated {input_file} to {target_lang}")
        except subprocess.CalledProcessError as e:
            print(f"Error translating {input_file}: {e}")

    def process_translation_list(self, list_file: Path) -> None:
        """Process a list of files for translation."""
        if not list_file.exists():
            return

        with open(list_file, 'r') as f:
            files = [line.strip() for line in f if line.strip()]
        
        for file_path in files:
            if "translate-to-en" in str(list_file):
                self.translate_file(file_path, 'en')
            else:
                self.translate_file(file_path, list_file.stem)

    def run_translation_workflow(self) -> None:
        """Execute the complete translation workflow."""
        print(f"Excluded subfolders: {self.config.excluded_subfolders}")
        languages = self.get_supported_languages()
        
        if not languages:
            print("No languages to process")
            return

        print(f"Processing languages: {languages}")

        # First pass: non-English to English
        for lang in languages:
            print(f"\nProcessing {lang} -> English translations")
            self.create_translation_list(lang, 'en')
            to_en_list = self.config.to_en_dir / f"{lang}.txt"
            if to_en_list.exists():
                self.process_translation_list(to_en_list)

        # Second pass: English to other languages
        for lang in languages:
            print(f"\nProcessing English -> {lang} translations")
            self.create_translation_list('en', lang)
            from_en_list = self.config.from_en_dir / f"{lang}.txt"
            if from_en_list.exists():
                self.process_translation_list(from_en_list)

def main():
    """Main entry point."""
    try:
        config = TranslationConfig()
        translator = TranslationManager(config)
        translator.run_translation_workflow()
    except Exception as e:
        print(f"Error during translation: {e}")
    finally:
        translator.cleanup()
        print("Translation process completed!")

if __name__ == "__main__":
    main()

