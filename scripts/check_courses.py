import os
import ruamel.yaml
from typing import List, Dict, Union
from ruamel.yaml.comments import CommentedMap

YAML = ruamel.yaml.YAML()
YAML.indent(sequence=4, offset=2)


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


if __name__ == "__main__":
    find_and_fix_courses("./courses")
