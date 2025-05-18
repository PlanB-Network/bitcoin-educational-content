import os
import re
import uuid
from datetime import datetime

def create_folder_structure(content):
    # Regular expressions to extract chapter ID
    chapter_pattern = r'<chapterId>(.*?)</chapterId>'
    question_pattern = r'## (.*?)\na\) (.*?)\nb\) (.*?)\nc\) (.*?)\nd\) (.*?)\nbonne reponse: (.*?)\ndifficulty: (.*?)\nexplanation: (.*?)(?=\n\n|$)'
    
    current_chapter = None
    question_counter = 1
    
    # Find all chapter IDs and questions
    chapters = re.finditer(chapter_pattern, content)
    questions = re.finditer(question_pattern, content, re.DOTALL)
    
    for question in questions:
        # Create folder name with leading zeros
        folder_name = f"{question_counter:03d}"
        os.makedirs(folder_name, exist_ok=True)
        
        # Extract question components
        question_text = question.group(1).strip()
        options = [
            question.group(2).strip(),
            question.group(3).strip(),
            question.group(4).strip(),
            question.group(5).strip()
        ]
        correct_answer = question.group(6).strip()
        difficulty = question.group(7).strip()
        explanation = question.group(8).strip()
        
        # Find the current chapter ID
        chapter_text = content[:question.start()]
        chapter_matches = list(re.finditer(chapter_pattern, chapter_text))
        if chapter_matches:
            current_chapter = chapter_matches[-1].group(1)
        
        # Create fr.yml
        with open(f"{folder_name}/fr.yml", 'w', encoding='utf-8') as f:
            f.write(f"question: {question_text}\n")
            f.write(f"answer: {options[ord(correct_answer) - ord('a')]}\n")
            f.write("wrong_answers:\n")
            for i, option in enumerate(options):
                if chr(i + ord('a')) != correct_answer:
                    f.write(f"  - {option}\n")
            f.write(f"explanation: |\n  {explanation}\n")
            
        # Create question.yml
        with open(f"{folder_name}/question.yml", 'w', encoding='utf-8') as f:
            f.write(f"id: {str(uuid.uuid4())}\n")
            f.write(f"chapterId: {current_chapter}\n")
            f.write(f"difficulty: {difficulty}\n")
            f.write("duration: 30\n")
            f.write("author: Rearden78\n")
            f.write("original_language: fr\n")
            f.write("proofreading:\n")
            f.write("  - language: fr\n")
            f.write("    last_contribution_date: 2025-05-17\n")
            f.write("    urgency: 1\n")
            f.write("    contributor_names:\n")
            f.write("      - Rearden78\n")
            f.write("    reward: 0\n")
            
        question_counter += 1

# Read the file and process it
with open('quizz.md', 'r', encoding='utf-8') as file:
    content = file.read()
    create_folder_structure(content)

