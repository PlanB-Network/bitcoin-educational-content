import json
from typing import List, Dict, Any
from pathlib import Path


class JsonToMarkdownConverter:
    def __init__(self):
        self.in_yaml = False
        self.output_lines: List[str] = []
        
    def handle_yml_property(self, item: Dict[str, Any]) -> str:
        """Handle YAML property with prefix and content preserving indentation"""
        # Special handling for objectives
        if item['prefix'] == 'objectives:' and item['content'] is None:
            return f"{indent}objectives:"
        indent = ' ' * item.get('indent', 0)
        return f"{indent}{item['prefix']} {item['content']}"
        
    def handle_list(self, item: Dict[str, Any]) -> str:
        """Handle list items with indent and content"""
        indent = ' ' * item.get('indent', 0)
        return f"{indent}{item['prefix']} {item['content']}"
        
    def handle_quote(self, item: Dict[str, Any]) -> str:
        """Handle quote with prefix and content"""
        return f"{item['prefix']} {item['content']}"
        
    def handle_snippet(self, item: Dict[str, Any]) -> List[str]:
        """Handle code snippets and their delimiters"""
        if item['type'] == 'snippet_start':
            return [item['content']]  # Use the full content as it includes the backticks and language
        elif item['type'] == 'snippet':
            if item.get('lines'):
                lines = item['lines']
            else:
                lines = item['content'].split('\n')
            lines.append('```')
            lines.append('')  # Add extra break after closing snippet
            return lines
        return []
        
    def handle_equation(self, item: Dict[str, Any]) -> List[str]:
        """Handle equations and their delimiters"""
        if item['type'] == 'equation_start':
            return [item['content']]  # Use the full content as it includes the equation delimiter
        elif item['type'] == 'equation':
            if item.get('lines'):
                lines = item['lines']
            else:
                lines = item['content'].split('\n')
            lines.append('$$')
            lines.append('')  # Add extra break after equation
            return lines
        return []
        
    def handle_header(self, item: Dict[str, Any]) -> List[str]:
        """Handle markdown headers with prefix and content"""
        return [f"{item['prefix']} {item['content']}", '']

    def convert_item(self, item: Dict[str, Any]) -> List[str]:
        """Convert a single JSON item to markdown lines"""
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
            
        if item_type == 'markdown_header':
            return self.handle_header(item)
            
        # Elements that need an extra break line
        if item_type in ['embed_links', 'paragraph', 'chapterId', 'partId']:
            return [item['content'], '']
            
        # Default handling for other types
        return [item['content']]

    def convert(self, json_data: List[Dict[str, Any]]) -> str:
      """Convert entire JSON structure to markdown"""
      formatted_lines = []
      prev_was_list = False
      
      for item in json_data:
          lines = self.convert_item(item)
          
          # Handle spacing between items
          if item['type'] == 'list':
              if not prev_was_list and formatted_lines:
                  formatted_lines.append('')  # Add space before first list item
              prev_was_list = True
          else:
              if prev_was_list:
                  formatted_lines.append('')  # Add space after last list item
              prev_was_list = False
          
          formatted_lines.extend(lines)
      
      # Clean up any trailing empty lines
      while formatted_lines and not formatted_lines[-1]:
          formatted_lines.pop()
      
      return '\n'.join(formatted_lines)
    
    @classmethod
    def convert_file_to_markdown(cls, input_path, output_path) -> Path:
        """
        Convert a JSON file back to markdown format.
        
        Args:
            input_path: Path to input JSON file
            output_path: Path where markdown should be saved
            
        Returns:
            Path to the created markdown file
        """
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Read JSON file
        with open(input_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        # Convert to markdown
        converter = cls()
        markdown_content = converter.convert(json_data)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        return output_path


def main():
    # Read JSON file
    with open('../translation-logic/output/lnp201_en_it.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Convert to markdown
    converter = JsonToMarkdownConverter()
    markdown_content = converter.convert(json_data)
    
    # Write to file
    with open('lnp201-it.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    main()
