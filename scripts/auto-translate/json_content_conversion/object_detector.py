import re
from typing import Optional, Dict, Any

class MDObjectDetector:
    def __init__(self):
        self.patterns = {
            'yml_properties':
      r'^(name|goal|objectives|description|question|answer|wrong_answers|explanation|reviewed):',
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
        if not line.strip():
            return None
            
        for obj_type, pattern in self.patterns.items():
            if re.match(pattern, line.strip()):
                return obj_type
        return 'paragraph'

    def get_delimiter_info(self, line: str) -> tuple[Optional[str], Optional[str]]:
        line = line.strip()
        
        if re.match(self.patterns['snippet_delimiter'], line):
            return 'snippet', line.lstrip('`').strip()
        elif re.match(self.patterns['equation_delimiter'], line):
            return 'equation', None
            
        return None, None

    def parse_yml_property(self, line: str) -> tuple[Optional[str], Any]:
        line = line.strip()
        if not re.match(self.patterns['yml_properties'], line):
            return None, None
            
        try:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            if key == 'objectives':
                return key, []
            return key, value
        except ValueError:
            return None, None

    def extract_quote_content(self, line: str) -> Optional[str]:
        match = re.match(self.patterns['quote'], line.strip())
        if match:
            return match.group(1).strip()
        return None

def test_detector():
    detector = MDObjectDetector()
    
    # Test delimiters
    delimiter_tests = [
        ('```python', ('snippet', 'python')),
        ('```', ('snippet', '')),
        ('$$', ('equation', None)),
        ('# Header', (None, None))
    ]
    for input_line, expected in delimiter_tests:
        result = detector.get_delimiter_info(input_line)
        assert result == expected, f"Delimiter test failed on '{input_line}': expected {expected}, got {result}"

    # Test quotes
    quote_tests = [
        ('> This is a quote', 'This is a quote'),
        ('>   Indented quote', 'Indented quote'),
        ('Not a quote', None)
    ]
    for input_line, expected in quote_tests:
        result = detector.extract_quote_content(input_line)
        assert result == expected, f"Quote test failed on '{input_line}': expected {expected}, got {result}"
        if expected:
            assert detector.detect_object_type(input_line) == 'quote', f"Quote type detection failed for '{input_line}'"

    # Test YML properties
    yml_tests = [
        ('name: The Bitcoin Journey', ('name', 'The Bitcoin Journey')),
        ('goal: Learn Bitcoin', ('goal', 'Learn Bitcoin')),
        ('objectives:', ('objectives', [])),
        ('invalid line', (None, None))
    ]
    for input_line, expected in yml_tests:
        result = detector.parse_yml_property(input_line)
        assert result == expected, f"YML test failed on '{input_line}': expected {expected}, got {result}"

    print("All tests passed!")

if __name__ == "__main__":
    test_detector()
