# Script Documentation

## Overview

The 3 Python scripts can be copied and pasted into any other courses to help the writer and automate certain tasks. You just need to copy and paste the `/scripts` folder into your main course folder.

## Dependencies

To install the external Python module, run the following command:

```sh
pip install pyyaml
```

## Scripts

### 1. `add_uuid.py`

The `add_uuid.py` script is used to create UUIDs below the titles of parts and chapters in the markdown file of your course without removing any existing UUIDs. This allows the writer to execute the script every time they add a new title. 

#### How It Works

- **Functionality**: Adds UUIDs to part and chapter titles in a markdown file.
- **Input**: If there is only one markdown file, it modifies it directly without asking anything. If there are multiple files, it prompts for input on which file to process.
- **Output**: The script updates the markdown file with UUIDs added to new titles.

#### Usage

1. Ensure the markdown file is in the parent directory of the script.
2. Run the script:

```sh
python add_uuid.py
```

or

```sh
python3 add_uuid.py
```

#### Example Output

If a title does not have a UUID, the script will add one:

```markdown
# Part 1 - Introduction
<partId>123e4567-e89b-12d3-a456-426614174000</partId>
## Chapter 1 - Overview
<chapterId>123e4567-e89b-12d3-a456-426614174001</chapterId>
```

### 2. `plan.py`

The `plan.py` script generates and updates a `plan.txt` file that includes all titles from your course markdown file. It also adds UUIDs for easy reference. This helps in quickly locating and identifying titles.

#### How It Works

- **Functionality**: Creates a clear text file (`plan.txt`) with all titles and their UUIDs.
- **Input**: If there is only one markdown file, it uses it directly without asking anything. If there are multiple files, it prompts for input on which file to use as the source for the plan.
- **Output**: A `plan.txt` file in the parent directory of the script.

#### Usage

1. Ensure the markdown file is in the parent directory of the script.
2. Run the script:

```sh
python plan.py
```

or

```sh
python3 plan.py
```

#### Example Output

The generated `plan.txt` will look like this:

```txt
Part 0 - Protect your privacy in Bitcoin
Part 1 - Introduction (123e4567-e89b-12d3-a456-426614174000)
    Chapter 1 - Overview (123e4567-e89b-12d3-a456-426614174001)
```

### 3. `quizz.py`

The `quizz.py` script creates five new quiz question directories with YAML templates. It prompts the user to input the UUID of the chapter for the questions and automatically fetches the difficulty and author information from the `course.yml` file.

#### How It Works

- **Functionality**: Creates directories with question templates for quizzes.
- **Input**: Chapter UUID.
- **Output**: Five new directories with `fr.yml` and `question.yml` files.

#### Usage

1. Ensure the `course.yml` file is in the parent directory of the script.
2. Run the script:

```sh
python quizz.py
```

or

```sh
python3 quizz.py
```

3. Input the required chapter UUID when prompted.

#### Example Output

The script creates directories named sequentially (e.g., `000`, `001`, etc.) and populates them with the following templates:

`fr.yml`:

```yaml
question: 
answer: 
wrong_answers:
  - 
explanation: |

reviewed: false
```

`question.yml`:

```yaml
chapterId: <input_uuid>
difficulty: <difficulty_from_course_yml>
duration: 15
author: <author_from_course_yml>
tags:
  - Bitcoin
```

If needed, don't hesitate to contact me! (Loïc)