import os
import re
import ruamel.yaml
from typing import List, Dict, Union
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import PreservedScalarString
from unidecode import unidecode
import frontmatter

YAML = ruamel.yaml.YAML()
YAML.indent(sequence=4, offset=2)

INVALID_CHARS_PATTERN = re.compile(r"[^\w\d_.-]", re.UNICODE)


class ValidationError(Exception):
    pass


class Course:
    REQUIRED_FIELDS = ["level", "hours", "teacher", "contributors"]
    REQUIRED_TRANSLATABLE_FIELDS = ["name", "goal"]
    LEVELS = ["beginner", "intermediate", "advanced", "expert"]

    def __init__(self, course_dir: str):
        self.course_dir = course_dir
        self.course_yml = os.path.join(course_dir, "course.yml")
        self.languages = []

        self.load_course()

    def load_course(self):
        self.data = self.load_course_yml()
        self.load_languages()

    def load_course_yml(self) -> CommentedMap:
        with open(self.course_yml, encoding="utf-8") as f:
            return YAML.load(f)

    def load_languages(self):
        for file in os.listdir(self.course_dir):
            if file.endswith(".md"):
                lang = file[:-3]
                self.languages.append(lang)

    def save(self):
        with open(self.course_yml, "w", encoding="utf-8") as f:
            YAML.dump(self.data, f)

    def validate(self):
        if not set(self.REQUIRED_FIELDS) <= set(self.data.keys()):
            missing_fields = set(self.REQUIRED_FIELDS) - set(self.data.keys())
            raise ValidationError(
                f"Missing required fields in {self.course_yml}: {', '.join(missing_fields)}"
            )

        if self.data["level"] not in self.LEVELS:
            raise ValidationError(
                f"Invalid level in {self.course_yml}: {self.data['level']}"
            )

        if not isinstance(self.data["hours"], int):
            raise ValidationError(
                f"'hours' should be an integer in {self.course_yml}: {self.data['hours']}"
            )

        if not isinstance(self.data["teacher"], str):
            raise ValidationError(
                f"'teacher' should be a string in {self.course_yml}: {self.data['teacher']}"
            )

        if not isinstance(self.data["contributors"], list) or not all(
            isinstance(c, str) for c in self.data["contributors"]
        ):
            raise ValidationError(
                f"'contributors' should be a list of strings in {self.course_yml}: {self.data['contributors']}"
            )

    def validate_md_files(self):
        for lang in self.languages:
            lang_file = os.path.join(self.course_dir, f"{lang}.md")
            if not os.path.isfile(lang_file):
                print(
                    f"Validation error: Language file '{lang}.md' not found in {self.course_dir}"
                )
                continue

            with open(lang_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            post = frontmatter.loads("\n".join(lines))
            if not set(self.REQUIRED_TRANSLATABLE_FIELDS) <= set(post.keys()):
                missing_fields = set(self.REQUIRED_TRANSLATABLE_FIELDS) - set(
                    post.keys()
                )
                raise ValidationError(
                    f"Missing required fields in {lang}: {', '.join(missing_fields)}"
                )

            start_line = None
            end_line = None

            for i, line in enumerate(lines[1:]):
                if line.strip() == "---" and start_line is None:
                    start_line = i
                if line.strip() == "+++" and end_line is None:
                    end_line = i
                    break

            start_line = start_line + 1 if start_line is not None else None
            end_line = end_line + 1 if end_line is not None else None

            if start_line is None or end_line is None:
                raise ValidationError(f"Missing excerpt in {lang}.md")

            excerpt_lines = lines[start_line + 1 : end_line]
            excerpt = "".join(excerpt_lines).strip()

            if not excerpt:
                raise ValidationError(f"Empty excerpt in {lang}.md")

    def fix_order(self):
        self.data = CommentedMap(
            sorted(
                self.data.items(), key=lambda pair: self.REQUIRED_FIELDS.index(pair[0])
            )
        )


def find_and_fix_courses(directory: str):
    course_dirs = [
        os.path.join(directory, d)
        for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d))
    ]

    for course_dir in course_dirs:
        course = Course(course_dir)

        try:
            course.validate()
            course.validate_md_files()
        except ValidationError as e:
            print(f"Validation error in course {course_dir} - {e}")
            continue

        course.fix_order()
        course.save()


def replace_in_files(files: List[str], old: str, new: str):
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            file_data = file.read()

        file_data = file_data.replace(old, new)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_data)


def find_and_fix_assets(directory: str):
    print(f"Checking file names")
    for root, _, files in os.walk(directory):
        for file in files:
            # Skip hidden files and those with a hidden parent
            if file.startswith(".") or "/." in os.path.join(root, file):
                continue

            old_file_path = os.path.join(root, file)
            new_file_name = re.sub(
                "_+|-+", "_", INVALID_CHARS_PATTERN.sub("_", unidecode(file).lower())
            )

            new_file_path = os.path.join(root, new_file_name)

            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed file {old_file_path} to {new_file_path}")

                files = [
                    os.path.join(r, f)
                    for r, _, fs in os.walk(directory)
                    for f in fs
                    if f.endswith(".md") or f.endswith(".yml")
                ]
                replace_in_files(files, file, new_file_name)
    print(f"Done!")


if __name__ == "__main__":
    directory = "."
    find_and_fix_courses(os.path.join(directory, "courses"))
    find_and_fix_assets(os.path.join(directory))
