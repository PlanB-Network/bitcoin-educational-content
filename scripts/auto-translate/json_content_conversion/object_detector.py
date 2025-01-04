import re
import yaml
from typing import Optional, Dict, Any, List, Tuple
from pathlib import Path

class BaseObjectDetector:
    def __init__(self, config_file: str):
        # Load translation configuration with specific config file
        self.translation_config = self.load_translation_config(config_file)

    def load_translation_config(self, config_file: str) -> Dict[str, List[str]]:
        config_path = Path(__file__).parent / config_file
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {
                'translatable': [],
                'non_translatable': []
            }

    def should_translate_property(self, key: str) -> bool:
        """Determine if a property should be translated"""
        if key in self.translation_config.get('non_translatable', []):
            return False
        if key in self.translation_config.get('translatable', []):
            return True
        return False  # Default to not translating unknown properties

class MDObjectDetector(BaseObjectDetector):
    """Handles detection of elements in Markdown files with YAML front matter"""
    
    def __init__(self):
        super().__init__('translation_rule_md.yml')
        self.patterns = {
            'yml_properties': r'^(name|goal|objectives|description|question|answer|wrong_answers|explanation|reviewed|title|publication_year|cover|original|contributors):',
            'header_separator': r'^---$',
            'markdown_header': r'^#{1,6}\s+.+$',
            'partId': r'^<partId>[^<]+</partId>$',
            'chapterId': r'^<chapterId>[^<]+</chapterId>$',
            'description_separator': r'^\+\+\+$',
            'embed_links': r'!\[(?:[^\]]*)\]\((?:[^)]+)\)',
            'list': r'^\s*[-*]\s+.+$',
            'equation_delimiter': r'^\$\$$',
            'snippet_delimiter': r'^```\w*$',
            'planb_links': r'^https://planb\.network/.*$',
            'quote': r'^>\s*(.+)$'
        }

    def detect_object_type(self, line: str) -> Optional[str]:
        """Detect the type of a line in a markdown file"""
        if not line.strip():
            return None
            
        for obj_type, pattern in self.patterns.items():
            if re.match(pattern, line.strip()):
                return obj_type
        return 'paragraph'

    def get_delimiter_info(self, line: str) -> Tuple[Optional[str], Optional[str]]:
        """Get information about code or equation delimiters"""
        line = line.strip()
        
        if re.match(self.patterns['snippet_delimiter'], line):
            return 'snippet', line.lstrip('`').strip()
        elif re.match(self.patterns['equation_delimiter'], line):
            return 'equation', None
            
        return None, None

    def parse_yml_property(self, line: str) -> Tuple[Optional[str], Any]:
        """Parse a YAML property line in markdown front matter"""
        line = line.strip()
        if not re.match(self.patterns['yml_properties'], line):
            return None, None
            
        try:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle special cases
            if key == 'objectives':
                return key, None
            
            # Check if property should be translated
            if not self.should_translate_property(key):
                return key, {'content': value, 'translate': False}
                
            return key, value
        except ValueError:
            return None, None

    def extract_quote_content(self, line: str) -> Optional[str]:
        """Extract content from a quote line"""
        match = re.match(self.patterns['quote'], line.strip())
        if match:
            return match.group(1).strip()
        return None

class YMLObjectDetector(BaseObjectDetector):
    """Handles detection and parsing of pure YAML files"""
    
    def __init__(self):
        super().__init__('translation_rule_yml.yml')

    def parse_content(self, content: str) -> List[Dict[str, Any]]:
        """Parse complete YAML file content"""
        lines = content.split('\n')
        current_key = None
        current_indent = 0
        parsed_objects = []
        content_lines = []
        
        for line in lines:
            if not line.strip():
                if current_key and content_lines:
                    content_lines.append(line)
                continue
                
            indent = len(line) - len(line.lstrip())
            
            # New key detected
            if ':' in line and (not current_key or indent <= current_indent):
                # Save previous content if exists
                if current_key and content_lines:
                    parsed_objects.append({
                        'type': 'yml_property',
                        'key': current_key,
                        'content': '\n'.join(content_lines).strip(),
                        'indent': current_indent,
                        'is_multiline': len(content_lines) > 1 or '\n' in content_lines[0],
                        'is_list': any(l.strip().startswith('-') for l in content_lines),
                        'translate': self.should_translate_property(current_key)
                    })
                    content_lines = []
                
                # Start new key
                key, value = line.split(':', 1)
                current_key = key.strip()
                current_indent = indent
                if value.strip():
                    content_lines.append(value)
            else:
                if current_key:
                    content_lines.append(line)
        
        # Handle last property
        if current_key and content_lines:
            parsed_objects.append({
                'type': 'yml_property',
                'key': current_key,
                'content': '\n'.join(content_lines).strip(),
                'indent': current_indent,
                'is_multiline': len(content_lines) > 1 or '\n' in content_lines[0],
                'is_list': any(l.strip().startswith('-') for l in content_lines),
                'translate': self.should_translate_property(current_key)
            })
            
        return parsed_objects

def get_detector_for_file(file_path: str) -> BaseObjectDetector:
    """Factory function to get the appropriate detector for a file"""
    if file_path.endswith('.yml'):
        return YMLObjectDetector()
    return MDObjectDetector()
