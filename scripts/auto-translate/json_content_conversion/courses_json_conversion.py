import json
import yaml
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from object_detector import MDObjectDetector

class CourseContentConverter:
    def __init__(self):
        self.detector = MDObjectDetector()
        
    def get_original_language(self, course_dir: Path) -> Optional[str]:
        """Read the course.yml file to get the original language."""
        course_config_path = course_dir / 'course.yml'
        if not course_config_path.exists():
            print(f"Warning: No course.yml found in {course_dir}")
            return None
            
        try:
            with open(course_config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                return config.get('original_language')
        except Exception as e:
            print(f"Error reading course config {course_config_path}: {e}")
            return None

    def process_markdown_content(self, content: List[str]) -> List[Dict[str, Any]]:
        """Process markdown content and return JSON structure."""
        converter = JsonConverter()
        for line in content:
            converter.process_line(line)
        return converter.output

    def setup_translation_directory(self, course_dir: Path) -> Path:
        """Create and return the translation assets directory path."""
        translation_dir = course_dir / 'assets' / 'translation'
        translation_dir.mkdir(parents=True, exist_ok=True)
        return translation_dir

    def process_course_directory(self, course_dir: Path) -> None:
        """Process a single course directory."""
        print(f"\nProcessing course directory: {course_dir}")
        
        # Get original language from course config
        original_language = self.get_original_language(course_dir)
        if not original_language:
            print(f"Skipping {course_dir}: No original_language specified in course.yml")
            return
            
        # Find the original language markdown file
        markdown_file = course_dir / f"{original_language}.md"
        if not markdown_file.exists():
            print(f"Skipping {course_dir}: No {original_language}.md file found")
            return
            
        try:
            # Read markdown content
            print(f"Reading {markdown_file}")
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.readlines()
                
            # Process content
            json_content = self.process_markdown_content(content)
            
            # Setup translation directory and save JSON
            translation_dir = self.setup_translation_directory(course_dir)
            output_file = translation_dir / f"{original_language}.json"
            
            print(f"Writing JSON to {output_file}")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_content, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Error processing {markdown_file}: {e}")

    def process_all_courses(self, base_dir: str) -> None:
        """Process all course directories under the base directory."""
        base_path = Path(base_dir)
        if not base_path.exists():
            raise ValueError(f"Base directory does not exist: {base_dir}")
            
        print(f"Starting to process courses in: {base_dir}")
        
        # Find all course directories (containing course.yml)
        course_dirs = [d for d in base_path.rglob('course.yml')]
        if not course_dirs:
            print("No course.yml files found in any subdirectory")
            return
            
        for course_yml in course_dirs:
            course_dir = course_yml.parent
            self.process_course_directory(course_dir)

class JsonConverter:
    def __init__(self):
        self.detector = MDObjectDetector()
        self.in_yaml = False
        self.in_snippet = False
        self.in_equation = False
        self.current_block: List[str] = []
        self.output: List[Dict[str, Any]] = []
        
    def process_line(self, line: str) -> None:
        raw_line = line
        line = line.strip()
        if not line:
            return
            
        # Check for delimiters first
        delimiter_type, meta = self.detector.get_delimiter_info(line)
        if delimiter_type:
            if delimiter_type == 'snippet':
                if not self.in_snippet:
                    self.in_snippet = True
                    self.output.append({
                        'type': 'snippet_start',
                        'content': line,
                        'language': meta
                    })
                else:
                    self.in_snippet = False
                    if self.current_block:
                        self.output.append({
                            'type': 'snippet',
                            'content': '\n'.join(self.current_block),
                            'lines': self.current_block
                        })
                        self.current_block = []
                return
                
            elif delimiter_type == 'equation':
                if not self.in_equation:
                    self.in_equation = True
                    self.output.append({
                        'type': 'equation_start',
                        'content': line
                    })
                else:
                    self.in_equation = False
                    if self.current_block:
                        self.output.append({
                            'type': 'equation',
                            'content': '\n'.join(self.current_block),
                            'lines': self.current_block
                        })
                        self.current_block = []
                return

        # Handle block content
        if self.in_snippet or self.in_equation:
            self.current_block.append(line)
            return

        # Handle YAML header
        if line == '---':
            self.in_yaml = not self.in_yaml
            self.output.append({
                'type': 'header_separator',
                'content': line
            })
            return

        if self.in_yaml:
            key, value = self.detector.parse_yml_property(line)
            if key:
                self.output.append({
                    'type': 'yml_property',
                    'content': value,
                    'prefix': f"{key}:"
                })
                return

        # Handle regular content
        obj_type = self.detector.detect_object_type(line)
        if obj_type == 'list':
            indent = len(raw_line) - len(raw_line.lstrip())
            content = line.lstrip('- *').strip()
            self.output.append({
                'type': obj_type,
                'content': content,
                'prefix': '-',
                'indent': indent
            })
        elif obj_type == 'quote':
            content = line.lstrip('> ').strip()
            self.output.append({
                'type': obj_type,
                'content': content,
                'prefix': '>'
            })
        elif obj_type == 'markdown_header':
            level = len(line) - len(line.lstrip('#'))
            content = line.lstrip('#').strip()
            self.output.append({
                'type': obj_type,
                'content': content,
                'prefix': '#' * level
            })
        elif obj_type:
            self.output.append({
                'type': obj_type,
                'content': line
            })

def main():
    base_dir = '../../../courses/'
    converter = CourseContentConverter()
    
    try:
        converter.process_all_courses(base_dir)
        print("\nProcessing completed successfully!")
    except Exception as e:
        print(f"\nError during processing: {e}")

if __name__ == "__main__":
    main()
