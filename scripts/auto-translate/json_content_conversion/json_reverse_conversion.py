import json
from typing import List, Dict, Any, Union
from pathlib import Path

class JsonToFileConverter:
    def __init__(self, output_path: Union[str, Path]):
        self.output_path = Path(output_path)
        self.is_yml = self.output_path.suffix == '.yml'
        self.output_lines: List[str] = []
    
    @staticmethod
    def is_yml_json(json_data: List[Dict[str, Any]]) -> bool:
        """Determine if JSON represents a YML file"""
        if not json_data:
            return False
            
        
        first_items = json_data[:3]  
        return all(
            item['type'] == 'yml_property' 
            and 'key' in item 
            and ('is_list' in item or 'is_multiline' in item or 'content' in item)
            for item in first_items
        )



    def handle_yml_property(self, item: Dict[str, Any]) -> List[str]:
        """Handle YAML property with proper formatting"""
        indent = ' ' * item.get('indent', 0)
        key = item['key']

        if item.get('is_list', False):
            
            lines = [f"{indent}{key}:"]
            list_indent = ' ' * item.get('list_indent', item['indent'] + 2)
            list_content = item.get('content', []) 
            if list_content is None: 
                list_content = []
            
            if not list_content:
                 
                 
                 
                 
                 lines = [f"{indent}{key}:"]
            else:
                for list_item in list_content:
                    
                    lines.append(f"{list_indent}- {str(list_item)}")
            return lines

        elif item.get('is_multiline', False):
            
            lines = [f"{indent}{key}: |"]
            content_indent_spaces = ' ' * item.get('content_indent', item['indent'] + 2)

            multiline_content_raw = item.get('content', '') 

            
            
            
            if isinstance(multiline_content_raw, list):
                
                
                print(f"Warning: Multiline content for key '{key}' was a list. Joining elements.")
                try:
                    
                    multiline_content_str = "".join(map(str, multiline_content_raw))
                except Exception as e:
                    print(f"Error joining list content for key '{key}': {e}. Using empty string.")
                    multiline_content_str = "" 
            elif multiline_content_raw is None:
                multiline_content_str = "" 
            else:
                
                multiline_content_str = str(multiline_content_raw)
            

            
            content_lines = multiline_content_str.split('\n')

            for content_line in content_lines:
                
                lines.append(f"{content_indent_spaces}{content_line}")
            return lines

        else:
            
            content = item.get('content') 
            if key == 'objectives' and content is None:
                 return [f"{indent}{key}:"]
            if content is None:
                
                
                content = ''
            
            return [f"{indent}{key}: {str(content)}"]


    def handle_md_property(self, item: Dict[str, Any]) -> List[str]:
        """Handle markdown-specific properties"""
        item_type = item['type']
        
        if item_type == 'header_separator':
            return ['---']
            
        elif item_type == 'yml_property':
            indent = ' ' * item.get('indent', 0)
            prefix = item.get('prefix', f"{item['key']}:")
            content = item['content'] if item['content'] is not None else ''
            return [f"{indent}{prefix} {content}"]
            
        elif item_type == 'list':
            indent = ' ' * item.get('indent', 0)
            return [f"{indent}{item['prefix']} {item['content']}"]
            
        elif item_type == 'quote':
            return [f"{item['prefix']} {item['content']}"]
            
        elif item_type == 'markdown_header':
            return [f"{item['prefix']} {item['content']}", '']
            
        elif item_type in ['snippet_start', 'snippet']:
            if item_type == 'snippet_start':
                return [item['content']]
            else:
                lines = item.get('lines', item['content'].split('\n'))
                return lines + ['```', '']
                
        elif item_type in ['equation_start', 'equation']:
            if item_type == 'equation_start':
                return [item['content']]
            else:
                lines = item.get('lines', item['content'].split('\n'))
                return lines + ['$$', '']
                
        elif item_type in ['embed_links', 'paragraph', 'chapterId', 'partId']:
            return [item['content'], '']
            
        return [item['content']]

    def convert(self, json_data: List[Dict[str, Any]]) -> str:
        """Convert JSON back to either YML or MD format"""
        is_yml = self.is_yml_json(json_data)
        formatted_lines = []
        prev_was_list = False
        
        for item in json_data:
            if is_yml:
                lines = self.handle_yml_property(item)
            else:
                lines = self.handle_md_property(item)
            
            
            if not is_yml:
                if item['type'] == 'list':
                    if not prev_was_list and formatted_lines:
                        formatted_lines.append('')
                    prev_was_list = True
                else:
                    if prev_was_list:
                        formatted_lines.append('')
                    prev_was_list = False
            
            formatted_lines.extend(lines)
        
        
        while formatted_lines and not formatted_lines[-1]:
            formatted_lines.pop()
        
        return '\n'.join(formatted_lines)

    @classmethod
    def convert_file(cls, input_path: Union[str, Path], output_path: Union[str, Path]) -> Path:
        """Convert JSON file back to appropriate format"""
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(input_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        converter = cls(output_path)
        content = converter.convert(json_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return output_path

def main():
    
    test_cases = [
        ('output_yml.json', 'output_reverse.yml'),
        ('output_md.json', 'output_reverse.md'),
    ]
    
    for input_json, output_file in test_cases:
        try:
            JsonToFileConverter.convert_file(input_json, output_file)
            print(f"Successfully converted {input_json} to {output_file}")
        except Exception as e:
            print(f"Error converting {input_json}: {str(e)}")

if __name__ == "__main__":
    main()
