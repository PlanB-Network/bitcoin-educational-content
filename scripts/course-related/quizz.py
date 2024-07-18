import os
import re
import yaml

def lire_course_yml(base_path):
    course_yml_path = os.path.join(base_path, 'course.yml')
    if not os.path.exists(course_yml_path):
        print(f"Error: {course_yml_path} does not exist.")
        return None, None

    with open(course_yml_path, 'r', encoding='utf-8') as file:
        course_data = yaml.safe_load(file)
    
    difficulty = course_data.get('level')
    authors = course_data.get('professors', [])
    author = authors[0] if authors else None

    return difficulty, author

def create_quiz_directories(base_path, chapter_id, difficulty, author, num_directories=5):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    existing_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    existing_nums = sorted([int(d) for d in existing_dirs if d.isdigit()])
    last_num = existing_nums[-1] if existing_nums else -1

    fr_template = """question: 
answer: 
wrong_answers:
  - 
explanation: |

reviewed: false
"""

    question_template = f"""chapterId: {chapter_id}
difficulty: {difficulty}
duration: 15
author: {author}
tags:
  - Bitcoin
"""

    for i in range(1, num_directories + 1):
        new_dir_num = last_num + i
        new_dir_name = f"{new_dir_num:03}"
        new_dir_path = os.path.join(base_path, new_dir_name)
        os.makedirs(new_dir_path, exist_ok=True)

        with open(os.path.join(new_dir_path, 'fr.yml'), 'w', encoding='utf-8') as file:
            file.write(fr_template)

        with open(os.path.join(new_dir_path, 'question.yml'), 'w', encoding='utf-8') as file:
            file.write(question_template)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(script_dir, os.pardir))
    quiz_path = os.path.join(base_path, 'quizz')

    difficulty, author = lire_course_yml(base_path)
    if not difficulty or not author:
        print("Error: Could not find required information in course.yml.")
        return

    chapter_id = input("Chapter UUID ? ")

    create_quiz_directories(quiz_path, chapter_id, difficulty, author)

if __name__ == "__main__":
    main()
