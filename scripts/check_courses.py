import os
import re
import ruamel.yaml
from typing import List, Dict, Union
from ruamel.yaml.comments import CommentedMap
from unidecode import unidecode

YAML = ruamel.yaml.YAML()
YAML.indent(sequence=4, offset=2)

INVALID_CHARS_PATTERN = re.compile(r"[^\w\d_.-]", re.UNICODE)


class ValidationError(Exception):
    pass


class Course:
    REQUIRED_FIELDS = ["level", "hours", "teacher", "contributors"]
    LEVELS = ["beginner", "intermediate", "advanced", "expert"]

    def __init__(self, path: str):
        self.path = path
        self.data = self.load()

    def load(self) -> CommentedMap:
        with open(self.path, encoding="utf-8") as f:
            return YAML.load(f)

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            YAML.dump(self.data, f)

    def validate(self):
        if not set(self.REQUIRED_FIELDS) <= set(self.data.keys()):
            missing_fields = set(self.REQUIRED_FIELDS) - set(self.data.keys())
            raise ValidationError(
                f"Missing required fields: {', '.join(missing_fields)}"
            )

        if self.data["level"] not in self.LEVELS:
            raise ValidationError(f"Invalid level: {self.data['level']}")

        if not isinstance(self.data["hours"], int):
            raise ValidationError(f"'hours' should be an integer: {self.data['hours']}")

        if not isinstance(self.data["teacher"], str):
            raise ValidationError(
                f"'teacher' should be a string: {self.data['teacher']}"
            )

        if not isinstance(self.data["contributors"], list) or not all(
            isinstance(c, str) for c in self.data["contributors"]
        ):
            raise ValidationError(
                f"'contributors' should be a list of strings: {self.data['contributors']}"
            )

    def fix_order(self):
        self.data = CommentedMap(
            sorted(
                self.data.items(), key=lambda pair: self.REQUIRED_FIELDS.index(pair[0])
            )
        )


def find_and_fix_courses(directory: str):
    for root, _, files in os.walk(directory):
        for file in files:
            if file != "course.yml":
                continue

            path = os.path.join(root, file)
            course = Course(path)

            try:
                course.validate()
            except ValidationError as e:
                print(f"Validation error in {path}: {e}")
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
    print(f"Fixing file names in {directory}")
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


if __name__ == "__main__":
    directory = "."
    find_and_fix_courses(os.path.join(directory, "courses"))
    find_and_fix_assets(os.path.join(directory))
