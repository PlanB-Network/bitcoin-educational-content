import json
from pathlib import Path
from .object_detector import MDObjectDetector, YMLObjectDetector, get_detector_for_file
from typing import List, Dict, Any, Union

class JsonConverter:
    """Converts Markdown and YAML files to JSON format and back"""
    
    def __init__(self, file_path: str):
        self.detector = get_detector_for_file(file_path)
        self.is_yml = file_path.endswith('.yml')
        self.file_path = file_path
        
        # MD specific states
        self.in_yaml = False
        self.in_snippet = False
        self.in_equation = False
        self.current_block: List[str] = []
        
        # Storage
        self.output: List[Dict[str, Any]] = []

  def get_indent_level(self, line: str) -> int:
      """
      Calculate the indentation level of a line by counting leading spaces.
      Returns the number of spaces at the start of the line.
      
      Args:
          line: The line to analyze
          
      Returns:
          int: Number of leading spaces
      """
      if not line:  
          return 0
          
      leading_spaces = 0
      for char in line:
          if char == ' ':
              leading_spaces += 1
          else:
              break
              
      return leading_spaces

    def process_file(self, content: str) -> None:
        """Process file content based on file type"""
        if self.is_yml:
            self.process_yml_file(content)
        else:
            for line in content.splitlines():
                self.process_md_line(line)

    def process_yml_file(self, content: str) -> None:
        """Process YAML file content"""
        lines = content.splitlines()
        current_key = None
        list_items = []
        multiline_content = []
        base_indent = 0
        is_multiline = False
        list_indent = 0
        
        for i, line in enumerate(lines):
            if not line.strip():
                continue

            indent = self.get_indent_level(line)
            stripped_line = line.strip()

            # Check if this is a new key
            if ':' in stripped_line and not stripped_line.startswith('-'):
                # Save previous content if exists
                if current_key:
                    if list_items:
                        # Get the actual list indent from the first list item
                        for next_line in lines[i-len(list_items):i]:
                            if next_line.strip().startswith('-'):
                                list_indent = self.get_indent_level(next_line)
                                break
                        self.output.append({
                            'type': 'yml_property',
                            'key': current_key,
                            'content': list_items,
                            'indent': base_indent,
                            'is_list': True,
                            'list_indent': list_indent,
                            'translate': self.detector.should_translate_property(current_key)
                        })
                        list_items = []
                    elif multiline_content:
                        # Find content indent by looking at first non-empty line after pipe
                        content_indent = 0
                        for next_line in lines[i-len(multiline_content):i]:
                            if next_line.strip():
                                content_indent = self.get_indent_level(next_line)
                                break
                        self.output.append({
                            'type': 'yml_property',
                            'key': current_key,
                            'content': multiline_content,
                            'indent': base_indent,
                            'is_multiline': True,
                            'content_indent': content_indent,
                            'translate': self.detector.should_translate_property(current_key)
                        })
                        multiline_content = []

                key, value = stripped_line.split(':', 1)
                current_key = key.strip()
                value = value.strip()
                base_indent = indent  # Store original indent for this key
                
                # Check if it's a multiline value with pipe
                if value == '|':
                    is_multiline = True
                    continue
                elif value:
                    self.output.append({
                        'type': 'yml_property',
                        'key': current_key,
                        'content': value,
                        'indent': indent,  # Use actual indent from file
                        'translate': self.detector.should_translate_property(current_key)
                    })
                    current_key = None
                is_multiline = False

            # Handle list items
            elif stripped_line.startswith('-'):
                if not list_items:  # First item in list
                    list_indent = indent  # Store the actual indent of first list item
                list_items.append(stripped_line[1:].strip())

            # Handle multiline content
            elif is_multiline and current_key:
                if line.strip():  # Skip empty lines
                    multiline_content.append(line.strip())

        # Handle last property
        if current_key:
            if list_items:
                self.output.append({
                    'type': 'yml_property',
                    'key': current_key,
                    'content': list_items,
                    'indent': base_indent,
                    'is_list': True,
                    'list_indent': list_indent,
                    'translate': self.detector.should_translate_property(current_key)
                })
            elif multiline_content:
                # Find content indent for last multiline block
                content_indent = 0
                for line in reversed(lines):
                    if line.strip():
                        content_indent = self.get_indent_level(line)
                        break
                self.output.append({
                    'type': 'yml_property',
                    'key': current_key,
                    'content': multiline_content,
                    'indent': base_indent,
                    'is_multiline': True,
                    'content_indent': content_indent,
                    'translate': self.detector.should_translate_property(current_key)
                })

    def process_md_line(self, line: str) -> None:
        """Process a single line from a Markdown file"""
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
                        'language': meta,
                        'translate': False
                    })
                else:
                    self.in_snippet = False
                    if self.current_block:
                        self.output.append({
                            'type': 'snippet',
                            'content': '\n'.join(self.current_block),
                            'lines': self.current_block,
                            'translate': False
                        })
                        self.current_block = []
                return
                
            elif delimiter_type == 'equation':
                if not self.in_equation:
                    self.in_equation = True
                    self.output.append({
                        'type': 'equation_start',
                        'content': line,
                        'translate': False
                    })
                else:
                    self.in_equation = False
                    if self.current_block:
                        self.output.append({
                            'type': 'equation',
                            'content': '\n'.join(self.current_block),
                            'lines': self.current_block,
                            'translate': False
                        })
                        self.current_block = []
                return

        # Handle block content
        if self.in_snippet or self.in_equation:
            self.current_block.append(line)
            return

        # Handle YAML header in markdown files
        if line == '---':
            self.in_yaml = not self.in_yaml
            self.output.append({
                'type': 'header_separator',
                'content': line,
                'translate': False
            })
            return

        if self.in_yaml:
            key, value = self.detector.parse_yml_property(line)
            if key:
                leading_spaces = len(raw_line) - len(raw_line.lstrip())
                if isinstance(value, dict) and 'translate' in value:
                    translate = value['translate']
                    content = value['content']
                else:
                    translate = self.detector.should_translate_property(key)
                    content = value
                    
                self.output.append({
                    'type': 'yml_property',
                    'key': key,
                    'content': content,
                    'prefix': f"{key}:",
                    'indent': leading_spaces,
                    'translate': translate
                })
                return

        # Handle regular content
        obj_type = self.detector.detect_object_type(line)
        translate = self.detector.should_translate_property(obj_type)
        
        if obj_type == 'list':
            indent = len(raw_line) - len(raw_line.lstrip())
            content = line.lstrip('- *').strip()
            self.output.append({
                'type': obj_type,
                'content': content,
                'prefix': '-',
                'indent': indent,
                'translate': translate
            })
        elif obj_type == 'quote':
            content = line.lstrip('> ').strip()
            self.output.append({
                'type': obj_type,
                'content': content,
                'prefix': '>',
                'translate': translate
            })
        elif obj_type == 'markdown_header':
            level = len(line) - len(line.lstrip('#'))
            content = line.lstrip('#').strip()
            self.output.append({
                'type': obj_type,
                'content': content,
                'prefix': '#' * level,
                'translate': translate
            })
        elif obj_type:
            self.output.append({
                'type': obj_type,
                'content': line,
                'translate': translate
            })

    def to_markdown(self) -> str:
        """Convert the JSON structure back to markdown/yaml format."""
        output_lines = []
        
        for obj in self.output:
            obj_type = obj['type']
            
            if obj_type == 'yml_property':
                indent = ' ' * obj.get('indent', 0)
                key = obj['key']
                
                if obj.get('is_list', False):
                    # Handle list property
                    output_lines.append(f"{indent}{key}:")
                    list_indent = ' ' * obj.get('list_indent', obj['indent'] + 2)
                    for item in obj['content']:
                        output_lines.append(f"{list_indent}- {item}")
                
                elif obj.get('is_multiline', False):
                    # Handle multiline property
                    output_lines.append(f"{indent}{key}: |")
                    content_indent = ' ' * obj.get('content_indent', obj['indent'] + 2)
                    for line in obj['content']:
                        output_lines.append(f"{content_indent}{line}")
                
                else:
                    # Handle simple property
                    content = obj['content'] if obj['content'] is not None else ''
                    if obj.get('key') == 'objectives' and not content:
                        output_lines.append(f"{indent}objectives:")
                    else:
                        output_lines.append(f"{indent}{key}: {content}")
            
            elif obj_type == 'header_separator':
                output_lines.append('---')
                
            elif obj_type == 'list':
                indent = ' ' * obj.get('indent', 0)
                output_lines.append(f"{indent}{obj['prefix']} {obj['content']}")
                
            elif obj_type == 'quote':
                output_lines.append(f"{obj['prefix']} {obj['content']}")
                
            elif obj_type == 'markdown_header':
                if output_lines and output_lines[-1]:
                    output_lines.append('')
                output_lines.append(f"{obj['prefix']} {obj['content']}")
                output_lines.append('')
            
            elif obj_type in ['snippet', 'equation']:
                if obj.get('lines'):
                    output_lines.extend(obj['lines'])
                else:
                    output_lines.append(obj['content'])
            
            elif obj_type in ['snippet_start', 'equation_start']:
                output_lines.append(obj['content'])
            
            elif obj_type in ['embed_links', 'paragraph', 'chapterId', 'partId']:
                output_lines.append(obj['content'])
                output_lines.append('')
            
            else:
                output_lines.append(obj['content'])
        
        # Clean up trailing empty lines
        while output_lines and not output_lines[-1]:
            output_lines.pop()
            
        return '\n'.join(output_lines)

    @classmethod
    def convert_file_to_json(cls, input_path: Union[str, Path], output_path: Union[str, Path]) -> Path:
        """Convert a file to JSON format."""
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        converter = cls(str(input_path))
        converter.process_file(content)
            
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(converter.output, f, indent=2, ensure_ascii=False)
            
        return output_path

def main():
    input_file = '../batch-translate/test/quizz/en.yml'
    output_json = 'output_yml.json'
    JsonConverter.convert_file_to_json(input_file, output_json)

    input_file = '../batch-translate/test/tutorial/en.md'
    output_json = 'output_md.json'
    JsonConverter.convert_file_to_json(input_file, output_json)

if __name__ == "__main__":
    main()
