import json
import yaml
import os
import statistics
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class CostConfig:
    PRICE_PER_MILLION_CHARS = 20  # euros
    NUM_LANGUAGES = 14
    
@dataclass
class CourseStats:
    total_chars: int
    cost_per_language: float
    total_cost: float

class TranslationCostAnalyzer:
    def __init__(self):
        self.cost_config = CostConfig()
        self.course_stats: Dict[str, CourseStats] = {}
        
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
            
    def count_translatable_chars(self, json_data: List[Dict[str, Any]]) -> int:
        """Count translatable characters in JSON content."""
        total_chars = 0
        
        # Define which fields should be translated for each type
        TRANSLATABLE_TYPES = {
            'yml_property': ['content'],
            'list': ['content'],
            'paragraph': ['content'],
            'markdown_header': ['content'],
            'quote': ['content']
        }
        
        # Types that should skip translation
        SKIP_TYPES = {
            'header_separator',
            'snippet_start',
            'snippet',
            'equation_start',
            'equation'
        }
        
        for obj in json_data:
            obj_type = obj.get('type')
            
            # Skip non-translatable types
            if obj_type in SKIP_TYPES or obj_type not in TRANSLATABLE_TYPES:
                continue
                
            # Count characters in translatable fields
            fields = TRANSLATABLE_TYPES.get(obj_type, [])
            for field in fields:
                if field in obj:
                    content = obj[field]
                    if isinstance(content, list):
                        total_chars += sum(len(str(item)) for item in content)
                    else:
                        total_chars += len(str(content))
                        
        return total_chars
        
    def calculate_course_cost(self, total_chars: int) -> float:
        """Calculate translation cost for a given number of characters."""
        return (total_chars / 1_000_000) * self.cost_config.PRICE_PER_MILLION_CHARS
        
    def analyze_course(self, course_dir: Path) -> Optional[CourseStats]:
        """Analyze translation costs for a single course."""
        original_language = self.get_original_language(course_dir)
        if not original_language:
            return None
            
        json_file = course_dir / 'assets' / 'translation' / f"{original_language}.json"
        if not json_file.exists():
            print(f"Warning: No {original_language}.json found in {course_dir}/assets/translation")
            return None
            
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                
            total_chars = self.count_translatable_chars(json_data)
            cost_per_language = self.calculate_course_cost(total_chars)
            total_cost = cost_per_language * self.cost_config.NUM_LANGUAGES
            
            return CourseStats(total_chars, cost_per_language, total_cost)
            
        except Exception as e:
            print(f"Error analyzing {json_file}: {e}")
            return None
            
    def generate_report(self, output_path: str) -> None:
        """Generate a detailed cost analysis report."""
        costs_per_language = [stats.cost_per_language for stats in self.course_stats.values()]
        total_costs = [stats.total_cost for stats in self.course_stats.values()]
        
        if not costs_per_language:
            print("No data to generate report")
            return
            
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("Translation Cost Analysis Report\n")
            f.write("===============================\n\n")
            
            # Per-course breakdown
            f.write("Cost Breakdown by Course\n")
            f.write("----------------------\n")
            for course_name, stats in self.course_stats.items():
                f.write(f"\nCourse: {course_name}\n")
                f.write(f"  Total Characters: {stats.total_chars:,}\n")
                f.write(f"  Cost per Language: €{stats.cost_per_language:.2f}\n")
                f.write(f"  Total Cost (all languages): €{stats.total_cost:.2f}\n")
                
            # Overall statistics
            f.write("\nOverall Statistics\n")
            f.write("-----------------\n")
            f.write(f"Number of Courses: {len(self.course_stats)}\n")
            f.write(f"Number of Target Languages: {self.cost_config.NUM_LANGUAGES}\n\n")
            
            f.write("Per Language Statistics:\n")
            f.write(f"  Mean Cost: €{statistics.mean(costs_per_language):.2f}\n")
            f.write(f"  Standard Deviation: €{statistics.stdev(costs_per_language):.2f}\n")
            f.write(f"  Minimum Cost: €{min(costs_per_language):.2f}\n")
            f.write(f"  Maximum Cost: €{max(costs_per_language):.2f}\n\n")
            
            f.write("Total Project Statistics:\n")
            f.write(f"  Total Project Cost: €{sum(total_costs):.2f}\n")
            f.write(f"  Mean Cost per Course (all languages): €{statistics.mean(total_costs):.2f}\n")
            f.write(f"  Standard Deviation: €{statistics.stdev(total_costs):.2f}\n")
            f.write(f"  Minimum Course Cost: €{min(total_costs):.2f}\n")
            f.write(f"  Maximum Course Cost: €{max(total_costs):.2f}\n")
            
    def analyze_all_courses(self, base_dir: str) -> None:
        """Analyze all courses in the base directory."""
        base_path = Path(base_dir)
        if not base_path.exists():
            raise ValueError(f"Base directory does not exist: {base_dir}")
            
        # Find all course directories (containing course.yml)
        course_dirs = [d for d in base_path.rglob('course.yml')]
        course_dirs = sorted(course_dirs)
        if not course_dirs:
            print("No course.yml files found in any subdirectory")
            return
            
        for course_yml in course_dirs:
            course_dir = course_yml.parent
            course_name = course_dir.name
            
            stats = self.analyze_course(course_dir)
            if stats:
                self.course_stats[course_name] = stats

def main():
    base_dir = '../../../courses/'
    analyzer = TranslationCostAnalyzer()
    
    try:
        print("Analyzing translation costs...")
        analyzer.analyze_all_courses(base_dir)
        
        # Generate report
        output_path = 'translation_cost_analysis.txt'
        analyzer.generate_report(output_path)
        print(f"\nAnalysis completed! Report generated at: {output_path}")
        
    except Exception as e:
        print(f"\nError during analysis: {e}")

if __name__ == "__main__":
    main()
