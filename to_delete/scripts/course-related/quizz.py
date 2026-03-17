import os
import re
import yaml
import uuid
from datetime import date

def lire_course_yml(base_path):
    course_yml_path = os.path.join(base_path, 'course.yml')
    if not os.path.exists(course_yml_path):
        print(f"Error: {course_yml_path} does not exist.")
        return None, None, None
    
    with open(course_yml_path, 'r', encoding='utf-8') as file:
        course_data = yaml.safe_load(file)
    
    difficulty = course_data.get('level')
    
    professors_ids = course_data.get('professors_id', [])
    professor_id = professors_ids[0] if professors_ids else None

    contributors = []
    proofreading = course_data.get('proofreading', []) or []
    for pr in proofreading:
        if isinstance(pr, dict) and str(pr.get('language', '')).lower() == 'fr':
            cn = pr.get('contributor_names') or []
            if cn:
                contributors = cn
            break

    if not contributors:
        contributors = course_data.get('contributor_names', []) or []
    
    return difficulty, professor_id, contributors


def validate_uuid(uuid_string):
    """Check if the string is a valid UUID."""
    try:
        uuid.UUID(uuid_string)
        return True
    except ValueError:
        return False

def find_chapter_in_markdown(base_path, chapter_uuid):
    """Find chapter UUID in fr.md and return the chapter title."""
    fr_md_path = os.path.join(base_path, 'fr.md')
    
    if not os.path.exists(fr_md_path):
        print(f"Error: {fr_md_path} does not exist.")
        return None
    
    with open(fr_md_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Match: "## Title" then "<chapterId>uuid</chapterId>"
    pattern = r'##\s+(.+?)\n<chapterId>([a-f0-9-]+)</chapterId>'
    matches = re.findall(pattern, content, re.IGNORECASE)
    
    for title, uuid in matches:
        if uuid.lower() == chapter_uuid.lower():
            return title.strip()
    
    return None


def choose_from_list(options, header, prompt):
    options = [o for o in (options or []) if o]
    if not options:
        return None
    if len(options) == 1:
        print(f"✓ Using {header}: {options[0]}")
        return options[0]

    print(f"\n{header} found:")
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")

    while True:
        choice = input(prompt).strip()
        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(options):
                picked = options[n - 1]
                print(f"✓ Selected {header.lower()}: {picked}")
                return picked
        print("Invalid choice. Please try again.")


def create_quiz_directories(base_path, chapter_id, difficulty, author, contributor_name, num_directories=5):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    existing_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    existing_nums = sorted([int(d) for d in existing_dirs if d.isdigit()])
    last_num = existing_nums[-1] if existing_nums else -1
    
    fr_template = ""
    
    # Use professor_id as author
    today = date.today().strftime("%Y-%m-%d")
    
    for i in range(1, num_directories + 1):
        new_dir_num = last_num + i
        new_dir_name = f"{new_dir_num:03}"
        new_dir_path = os.path.join(base_path, new_dir_name)
        
        os.makedirs(new_dir_path, exist_ok=True)
        
        # One UUID per question
        question_id = str(uuid.uuid4())
        
        question_template = f"""id: {question_id}
chapterId: {chapter_id}
difficulty: {difficulty}
duration: 15
author: {author}
original_language: fr

# Proofreading metadata

proofreading:
  - language: fr
    last_contribution_date: {today}
    urgency: 1
    contributor_names:
      - {contributor_name}
    reward: 0
"""
        
        with open(os.path.join(new_dir_path, 'fr.yml'), 'w', encoding='utf-8') as file:
            file.write(fr_template)
        
        with open(os.path.join(new_dir_path, 'question.yml'), 'w', encoding='utf-8') as file:
            file.write(question_template)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.abspath(os.path.join(script_dir, os.pardir))
    quiz_path = os.path.join(base_path, 'quizz')
    
    _, professor_id, contributor_candidates = lire_course_yml(base_path)
    
    if not professor_id:
        print("Error: Could not find professor_id in course.yml.")
        return
    
    contributor_name = choose_from_list(
    contributor_candidates,
    "Contributor name(s)",
    "Choose a number: "
    )

    if not contributor_name:
        print("Error: Could not find contributor_names in course.yml.")
        return

    # Ask + validate chapter UUID
    while True:
        chapter_input = input("Chapter UUID ? ").strip()
        
        # Extract UUID if pasted as an HTML tag
        if '<chapterId>' in chapter_input and '</chapterId>' in chapter_input:
            match = re.search(r'<chapterId>([a-f0-9-]+)</chapterId>', chapter_input, re.IGNORECASE)
            if match:
                chapter_id = match.group(1)
                print(f"→ Extracted UUID: {chapter_id}")
            else:
                print("Error: Could not extract UUID from HTML tag.")
                continue
        else:
            chapter_id = chapter_input
        
        if not validate_uuid(chapter_id):
            print("Error: Invalid UUID format. Please enter a valid UUID.")
            continue
        
        chapter_title = find_chapter_in_markdown(base_path, chapter_id)
        if chapter_title:
            print(f"✓ Chapter found: '{chapter_title}'")
            break
        else:
            print(f"Error: Chapter UUID '{chapter_id}' not found in fr.md")
            continue
    
    # Pick difficulty
    print("\nSelect difficulty level:")
    print("1. easy")
    print("2. intermediate")
    print("3. hard")
    
    difficulty_map = {
        '1': 'easy',
        '2': 'intermediate',
        '3': 'hard'
    }
    
    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice in difficulty_map:
            difficulty = difficulty_map[choice]
            print(f"✓ Selected difficulty: {difficulty}")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    create_quiz_directories(quiz_path, chapter_id, difficulty, professor_id, contributor_name)

if __name__ == "__main__":
    main()
