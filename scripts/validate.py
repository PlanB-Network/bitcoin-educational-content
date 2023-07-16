import os
import re
import ruamel.yaml
from typing import List, Dict, Union
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import PreservedScalarString
from unidecode import unidecode
import frontmatter

YAML = ruamel.yaml.YAML()
YAML.indent(mapping=2, sequence=4, offset=2)
YAML.width = 100000

INVALID_CHARS_PATTERN = re.compile(r"[^\w\d_.-]", re.UNICODE)


class ValidationError(Exception):
    pass


class ValidationMixin:
    data: Dict[str, Union[str, int, List[str], Dict[str, str]]]

    REQUIRED_FIELDS = []
    OPTIONAL_FIELDS = []

    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def validate_required_fields(self):
        missing_fields = set(self.REQUIRED_FIELDS) - set(self.data.keys())
        if missing_fields:
            self.errors.append(f"Missing required fields: {', '.join(missing_fields)}")

    def validate_optional_fields(self):
        if self.OPTIONAL_FIELDS:
            missing_fields = set(self.OPTIONAL_FIELDS) - set(self.data.keys())
            if missing_fields:
                self.warnings.append(
                    f"Missing optional fields: {', '.join(missing_fields)}"
                )

    def validate_unrecognized_fields(self):
        allowed_fields = set(self.REQUIRED_FIELDS + self.OPTIONAL_FIELDS)
        unrecognized_fields = set(self.data.keys()) - allowed_fields
        if unrecognized_fields:
            self.warnings.append(
                f"Unrecognized fields: {', '.join(unrecognized_fields)}"
            )

    def fix_order(self):
        sorted_fields = []
        unrecognized_fields = []

        for field in self.REQUIRED_FIELDS:
            if field in self.data:
                sorted_fields.append(field)

        for field in self.data.keys():
            if field not in self.REQUIRED_FIELDS and field in self.OPTIONAL_FIELDS:
                sorted_fields.append(field)
            else:
                unrecognized_fields.append(field)

        self.data = CommentedMap(
            sorted(
                self.data.items(),
                key=lambda pair: (
                    sorted_fields.index(pair[0])
                    if pair[0] in sorted_fields
                    else len(sorted_fields) + self.OPTIONAL_FIELDS.index(pair[0])
                    if pair[0] in self.OPTIONAL_FIELDS
                    else len(sorted_fields)
                    + len(self.OPTIONAL_FIELDS)
                    + unrecognized_fields.index(pair[0]),
                ),
            )
        )

    def print_report(self, header: str):
        if self.errors or self.warnings:
            print(header)

        if self.errors:
            print(f"  Errors:")
            for error in self.errors:
                print(f"   - {error}")

        if self.warnings:
            print(f"  Warnings:")
            for warning in self.warnings:
                print(f"   - {warning}")

        if self.errors or self.warnings:
            print("")


class Course(ValidationMixin):
    REQUIRED_FIELDS = ["level", "hours", "teacher", "contributors"]
    REQUIRED_TRANSLATABLE_FIELDS = ["name", "goal"]
    LEVELS = ["beginner", "intermediate", "advanced", "expert"]

    def __init__(self, course_dir: str):
        super().__init__()
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
        self.validate_required_fields()
        self.validate_optional_fields()
        self.validate_unrecognized_fields()

        if self.data["level"] not in self.LEVELS:
            self.errors.append(f"Invalid level: {self.data['level']}")

        if "hours" in self.data and not isinstance(self.data["hours"], int):
            self.errors.append(f"'hours' should be an integer: {self.data['hours']}")

        if "teacher" in self.data and not isinstance(self.data["teacher"], str):
            self.errors.append(f"'teacher' should be a string: {self.data['teacher']}")

        if "contributors" in self.data and (
            not isinstance(self.data["contributors"], list)
            or not all(isinstance(c, str) for c in self.data["contributors"])
        ):
            self.errors.append(
                f"'contributors' should be a list of strings: {self.data['contributors']}"
            )

    def validate_md_files(self):
        for lang in self.languages:
            lang_file = os.path.join(self.course_dir, f"{lang}.md")
            if not os.path.isfile(lang_file):
                self.errors.append(f"Language file '{lang}.md' not found")
                continue

            with open(lang_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            post = frontmatter.loads("\n".join(lines))
            if not set(self.REQUIRED_TRANSLATABLE_FIELDS) <= set(post.keys()):
                missing_fields = set(self.REQUIRED_TRANSLATABLE_FIELDS) - set(
                    post.keys()
                )
                self.errors.append(
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
                self.errors.append(f"Missing excerpt in {lang}.md")
            else:
                excerpt_lines = lines[start_line + 1 : end_line]
                excerpt = "".join(excerpt_lines).strip()

                if not excerpt:
                    self.warnings.append(f"Empty excerpt in {lang}.md")


class Podcast(ValidationMixin):
    REQUIRED_FIELDS = ["name", "host", "language"]
    OPTIONAL_FIELDS = [
        "links",
        "description",
        "tags",
        "contributors",
    ]

    def __init__(self, podcast_dir: str):
        super().__init__()
        self.podcast_dir = podcast_dir
        self.podcast_yml = os.path.join(podcast_dir, "podcast.yml")

        self.load_podcast()

    def load_podcast(self):
        self.data = self.load_podcast_yml()

    def load_podcast_yml(self) -> CommentedMap:
        with open(self.podcast_yml, encoding="utf-8") as f:
            return YAML.load(f)

    def save(self):
        with open(self.podcast_yml, "w", encoding="utf-8") as f:
            YAML.dump(self.data, f)

    def validate(self):
        self.validate_required_fields()
        self.validate_unrecognized_fields()

        if "links" not in self.data:
            self.warnings.append(f"No links found")

        if "description" not in self.data:
            self.warnings.append(f"No description")

        if "links" in self.data:
            self.validate_links()

    def validate_links(self):
        links = self.data["links"]

        if not isinstance(links, dict):
            self.errors.append("'links' should be an object")

        for link_name, link_url in links.items():
            if not isinstance(link_url, str):
                self.errors.append(f"'{link_name}' link should be a string: {link_url}")


def replace_in_files(files: List[str], old: str, new: str):
    for file_path in files:
      with open(file_path, "r+", encoding="utf-8") as file:
        file_data = file.read()
        file_data = file_data.replace(old, new)
        file.seek(0)
        file.write(file_data)
        file.truncate()


def find_and_fix_courses(directory: str):
    course_dirs = [
        os.path.join(directory, d)
        for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d))
    ]

    print("🔎 Checking courses")

    for course_dir in course_dirs:
        course = Course(course_dir)
        course.validate()
        course.validate_md_files()
        course.fix_order()
        course.save()
        course.print_report(f"Course {course_dir.split('/')[-1]}")

    print("✅ Finished checking courses\n")


def find_and_fix_podcasts(directory: str):
    podcast_dirs = [
        os.path.join(directory, d)
        for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d))
    ]

    print("🔎 Checking podcasts")

    for podcast_dir in podcast_dirs:
        podcast = Podcast(podcast_dir)
        podcast.validate()
        podcast.fix_order()
        podcast.save()
        podcast.print_report(f"Podcast {podcast_dir.split('/')[-1]}")

    print("✅ Finished checking podcasts\n")


def find_and_fix_assets(directory: str, folders: []):
    print("🔎 Checking file names")

    for folder in folders:
      for root, _, files in os.walk(os.path.join(directory, folder)):
          for file in files:
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

      print("✅ Finished checking file names")


if __name__ == "__main__":
    directory = ".."
    find_and_fix_courses(os.path.join(directory, "courses"))
    find_and_fix_podcasts(os.path.join(directory, "resources/podcasts"))
    folders = [
      'courses',
      'resources',
      'soon',
      'tutorials',
    ]
    find_and_fix_assets(directory, folders)
