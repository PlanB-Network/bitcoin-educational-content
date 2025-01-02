import json
from pathlib import Path
from .object_detector import MDObjectDetector
from typing import List, Dict, Any, Union

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

    def to_markdown(self) -> str:
        """Convert the JSON structure back to markdown format."""
        markdown_lines = []
        for obj in self.output:
            obj_type = obj['type']
            
            if obj_type == 'header_separator':
                markdown_lines.append(obj['content'])
            
            elif obj_type == 'yml_property':
                markdown_lines.append(f"{obj['prefix']} {obj['content']}")
            
            elif obj_type == 'list':
                indent = ' ' * obj.get('indent', 0)
                markdown_lines.append(f"{indent}{obj['prefix']} {obj['content']}")
            
            elif obj_type == 'quote':
                markdown_lines.append(f"{obj['prefix']} {obj['content']}")
            
            elif obj_type == 'markdown_header':
                markdown_lines.append(f"{obj['prefix']} {obj['content']}")
            
            elif obj_type in ['snippet', 'equation']:
                if obj.get('lines'):
                    markdown_lines.extend(obj['lines'])
                else:
                    markdown_lines.append(obj['content'])
            
            elif obj_type in ['snippet_start', 'equation_start']:
                markdown_lines.append(obj['content'])
            
            else:
                markdown_lines.append(obj['content'])
        
        return '\n'.join(markdown_lines)

    @classmethod
    def convert_file_to_json(cls, input_path, output_path) -> Path:
        """
        Convert a markdown file to JSON format.
        
        Args:
            input_path: Path to input markdown file
            output_path: Path where JSON should be saved
            
        Returns:
            Path to the created JSON file
        """
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Read input file
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Convert to JSON
        converter = cls()
        for line in lines:
            converter.process_line(line)
            
        # Write JSON output
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(converter.output, f, indent=2, ensure_ascii=False)
            
        return output_path

def main():
    # Read input file
    with open('../../../courses/btc101/en.md', 'r') as f:
        lines = f.readlines()
        
    # Convert to JSON
    converter = JsonConverter()
    for line in lines:
        converter.process_line(line)
        
    # Write JSON output
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(converter.output, f, indent=2, ensure_ascii=False)
    
    # Optionally verify roundtrip conversion
    markdown = converter.to_markdown()
    with open('output.md', 'w', encoding='utf-8') as f:
        f.write(markdown)

if __name__ == "__main__":
    main()
