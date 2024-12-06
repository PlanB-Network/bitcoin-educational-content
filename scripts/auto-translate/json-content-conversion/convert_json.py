import json
from object_detector import MDObjectDetector
from typing import List, Dict, Any

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
                        'value': line,
                        'language': meta
                    })
                else:
                    self.in_snippet = False
                    if self.current_block:
                        self.output.append({
                            'type': 'snippet',
                            'value': '\n'.join(self.current_block),
                            'content': self.current_block
                        })
                        self.current_block = []
                return
                
            elif delimiter_type == 'equation':
                if not self.in_equation:
                    self.in_equation = True
                    self.output.append({
                        'type': 'equation_start',
                        'value': line
                    })
                else:
                    self.in_equation = False
                    if self.current_block:
                        self.output.append({
                            'type': 'equation',
                            'value': '\n'.join(self.current_block),
                            'content': self.current_block
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
                'value': line
            })
            return

        if self.in_yaml:
            key, value = self.detector.parse_yml_property(line)
            if key:
                self.output.append({
                    'type': 'yml_property',
                    'value': line,
                    'key': key,
                    'content': value
                })
                return

        # Handle regular content
        obj_type = self.detector.detect_object_type(line)
        if obj_type == 'list':
            indent = len(raw_line) - len(raw_line.lstrip())
            self.output.append({
                'type': obj_type,
                'value': raw_line.rstrip(),
                'indent': indent,
                'content': line.lstrip('- *').strip()
            })
        elif obj_type == 'quote':
            # Modified quote handling to extract content
            quote_content = line.lstrip('> ').strip()
            self.output.append({
                'type': obj_type,
                'value': line,
                'content': quote_content
            })
        elif obj_type:
            self.output.append({
                'type': obj_type,
                'value': line
            })

def main():
    with open('../../../courses/btc101/en_test.md', 'r') as f:
        lines = f.readlines()
        
    converter = JsonConverter()
    for line in lines:
        converter.process_line(line)
        
    with open('output.json', 'w') as f:
        json.dump(converter.output, f, indent=2)

if __name__ == "__main__":
    main()
