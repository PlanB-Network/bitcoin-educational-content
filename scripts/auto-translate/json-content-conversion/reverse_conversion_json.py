import json
from typing import List, Dict, Any

class JsonToMarkdownConverter:
    def __init__(self):
        self.in_yaml = False
        self.output_lines: List[str] = []
        
    def handle_yml_property(self, item: Dict[str, Any]) -> str:
        if item.get('key') == 'objectives':
            return f"{item['key']}:"
        return item['value']
        
    def handle_list(self, item: Dict[str, Any]) -> str:
        indent = ' ' * item.get('indent', 0)
        return f"{indent}- {item['content']}"
        
    def handle_quote(self, item: Dict[str, Any]) -> str:
        return f"> {item.get('content', item['value'])}"
        
    def handle_snippet(self, item: Dict[str, Any]) -> List[str]:
        if item['type'] == 'snippet_start':
            return [f"```{item.get('language', '')}"]
        elif item['type'] == 'snippet':
            content = item.get('content', [])
            if isinstance(content, str):
                content = content.split('\n')
            lines = content + ['```']
            if item['type'] == 'snippet':  # Add extra break after closing snippet
                lines.append('')
            return lines
        return []
        
    def handle_equation(self, item: Dict[str, Any]) -> List[str]:
        if item['type'] == 'equation_start':
            return ['$$']
        elif item['type'] == 'equation':
            content = item.get('content', [])
            if isinstance(content, str):
                content = content.split('\n')
            lines = content + ['$$']
            lines.append('')  # Add extra break after equation
            return lines
        return []

    def convert_item(self, item: Dict[str, Any]) -> List[str]:
        item_type = item['type']
        
        if item_type == 'header_separator':
            self.in_yaml = not self.in_yaml
            return ['---']
            
        if item_type == 'yml_property':
            return [self.handle_yml_property(item)]
            
        if item_type == 'list':
            return [self.handle_list(item)]
            
        if item_type == 'quote':
            return [self.handle_quote(item)]
            
        if item_type in ['snippet_start', 'snippet']:
            return self.handle_snippet(item)
            
        if item_type in ['equation_start', 'equation']:
            return self.handle_equation(item)
            
        # Elements that need an extra break line
        if item_type in ['embed_links', 'markdown_header', 'paragraph', 'chapterId', 'partId']:
            return [item['value'], '']

        # Default handling for other types
        return [item['value']]

    def convert(self, json_data: List[Dict[str, Any]]) -> str:
        formatted_lines = []
        
        for item in json_data:
            lines = self.convert_item(item)
            formatted_lines.extend(lines)
            
        return '\n'.join(formatted_lines)

def main():
    # Read JSON file
    with open('output.json', 'r') as f:
        json_data = json.load(f)
    
    # Convert to markdown
    converter = JsonToMarkdownConverter()
    markdown_content = converter.convert(json_data)
    
    # Write to file
    with open('output.md', 'w') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    main()
