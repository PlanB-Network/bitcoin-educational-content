import os

def create_quiz_directories(base_path, part, chapter, num_directories=5):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    existing_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    existing_nums = sorted([int(d) for d in existing_dirs if d.isdigit()], reverse=True)
    last_num = existing_nums[0] if existing_nums else 0

    fr_template = """question: 
answer: 
wrong_answers:
  - 
explanation: |

reviewed: false
"""

    question_template = f"""course: btc204
part: {part}
chapter: {chapter}
difficulty: intermediate
duration: 15
author: pretty-private
tags:
  - Bitcoin
"""

    for i in range(1, num_directories + 1):
        new_dir = os.path.join(base_path, str(last_num + i))
        os.makedirs(new_dir, exist_ok=True)

        with open(os.path.join(new_dir, 'fr.yml'), 'w', encoding='utf-8') as file:
            file.write(fr_template)

        with open(os.path.join(new_dir, 'question.yml'), 'w', encoding='utf-8') as file:
            file.write(question_template)

def main():
    base_path = "../../../quizzes/questions"

    part = input("Partie ? ")
    chapter = input("Chapitre ? ")

    create_quiz_directories(base_path, part, chapter)

if __name__ == "__main__":
    main()
