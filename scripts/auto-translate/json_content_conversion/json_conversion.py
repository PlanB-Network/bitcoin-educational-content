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
        
        
        self.in_yaml = False
        self.in_snippet = False
        self.in_equation = False
        self.current_block: List[str] = []
        
        
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
        """Process YAML file content (Revised Logic)"""
        lines = content.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped_line = line.strip()
            indent = self.get_indent_level(line)

            if not stripped_line:
                i += 1
                continue 

            
            
            
            if ':' in stripped_line and not stripped_line.startswith('-'):
                try:
                    key, value = stripped_line.split(':', 1)
                    key = key.strip()
                    value_stripped = value.strip()
                    base_indent = indent 

                    
                    if value_stripped == '|':
                        multiline_raw_lines = []
                        content_indent = -1 
                        
                        
                        block_index = i + 1
                        while block_index < len(lines):
                            block_line = lines[block_index]
                            block_indent = self.get_indent_level(block_line)
                            block_stripped = block_line.strip()

                            
                            if block_stripped and block_indent <= base_indent:
                                break 
                            
                            
                            if content_indent == -1 and block_stripped:
                                content_indent = block_indent

                            
                            multiline_raw_lines.append(block_line)
                            block_index += 1
                        
                        
                        processed_content_lines = []
                        if content_indent != -1:
                             
                             actual_content_indent = max(content_indent, base_indent + 1) if content_indent > base_indent else base_indent + 2

                             for ml_line in multiline_raw_lines:
                                 
                                 if len(ml_line) >= actual_content_indent:
                                     processed_content_lines.append(ml_line[actual_content_indent:])
                                 else: 
                                     processed_content_lines.append(ml_line.lstrip(' ')) 
                        
                        single_string_content = '\n'.join(processed_content_lines)

                        self.output.append({
                            'type': 'yml_property',
                            'key': key,
                            'content': single_string_content, 
                            'indent': base_indent,
                            'is_multiline': True,
                            'content_indent': actual_content_indent if content_indent != -1 else base_indent + 2, 
                            'translate': self.detector.should_translate_property(key)
                        })
                        
                        i = block_index 
                        continue 

                    
                    
                    elif value_stripped == '' or value_stripped == '[]':
                        is_list = False
                        list_items = []
                        list_indent = -1
                        
                        
                        block_index = i + 1
                        if block_index < len(lines):
                            next_line = lines[block_index]
                            next_indent = self.get_indent_level(next_line)
                            next_stripped = next_line.strip()

                            
                            if next_stripped.startswith('-') and next_indent > base_indent:
                                is_list = True
                                list_indent = next_indent
                                
                                
                                while block_index < len(lines):
                                    list_line = lines[block_index]
                                    list_line_indent = self.get_indent_level(list_line)
                                    list_line_stripped = list_line.strip()

                                    
                                    if not list_line_stripped.startswith('-') or list_line_indent != list_indent:
                                         
                                         if list_line_stripped and list_line_indent <= base_indent:
                                             break
                                         
                                         
                                         break 

                                    list_items.append(list_line_stripped[1:].strip())
                                    block_index += 1
                        
                        
                        if is_list:
                            self.output.append({
                                'type': 'yml_property',
                                'key': key,
                                'content': list_items, 
                                'indent': base_indent,
                                'is_list': True,
                                'list_indent': list_indent,
                                'translate': self.detector.should_translate_property(key) 
                            })
                            i = block_index 
                            continue
                        else:
                            
                             self.output.append({
                                'type': 'yml_property',
                                'key': key,
                                'content': None, 
                                'indent': base_indent,
                                'translate': self.detector.should_translate_property(key)
                            })
                             i += 1 
                             continue

                    
                    else:
                        self.output.append({
                            'type': 'yml_property',
                            'key': key,
                            'content': value_stripped,
                            'indent': base_indent,
                            'translate': self.detector.should_translate_property(key)
                        })
                        i += 1 
                        continue
                
                except ValueError:
                     
                     print(f"Warning: Skipping line with unexpected colon format: {line}")
                     i += 1
                     continue

            
            else:
                
                
                print(f"Warning: Skipping non-key definition line: {line}")
                i += 1
                
        



    def process_md_line(self, line: str) -> None:
        """Process a single line from a Markdown file"""
        raw_line = line
        line = line.strip()
        if not line:
            return
            
        
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

        
        if self.in_snippet or self.in_equation:
            self.current_block.append(line)
            return

        
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
                    
                    output_lines.append(f"{indent}{key}:")
                    list_indent = ' ' * obj.get('list_indent', obj['indent'] + 2)
                    for item in obj['content']:
                        output_lines.append(f"{list_indent}- {item}")
                
                elif obj.get('is_multiline', False):
                    
                    output_lines.append(f"{indent}{key}: |")
                    content_indent = ' ' * obj.get('content_indent', obj['indent'] + 2)
                    for line in obj['content']:
                        output_lines.append(f"{content_indent}{line}")
                
                else:
                    
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
