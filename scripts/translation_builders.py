import os
import io
import shutil
import yaml
import re
import time
import openai
from openai.error import RateLimitError, Timeout, APIError
from dotenv import load_dotenv
from tqdm import tqdm


def translate_text(prompt, temperature=0.1, model_engine="gpt-3.5-turbo"):
    """
    Translates the transcript text using OpenAI's GPT API.

    Args:
        prompt (str, optional): The prompt to use for text manipulation.

    Returns:
        str: The translated transcript in text format.
    """
    # Use the OpenAI GPT API to translate the transcript
    response = openai.ChatCompletion.create(
        model = model_engine,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    chatgpt_output = content = response['choices'][0]['message']['content']

    return chatgpt_output

def process_files():
    languages = ['french', 'german', 'spanish', 'portuguese', 'italian']
    language_codes = ['fr', 'de', 'es', 'pt', 'it']

    # Load environment variables from .env file
    load_dotenv()

    # Set OpenAI key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    folder_count = sum([len(d) for r, d, files in os.walk('../resources/builders')])

    with tqdm(total=folder_count, desc="Folders") as folder_progress:
        for root, dirs, files in os.walk('../resources/builders'):
            with tqdm(total=len(languages), desc="Languages in a folder", leave=False) as language_progress:
                for language, lang_code in zip(languages, language_codes):
                    file_name = f'{lang_code}.yml'
                    if 'en.yml' in files:
                        with open(os.path.join(root, 'en.yml')) as file:
                            data = yaml.safe_load(file)

                        description = data.get('description', '')
                        contributors = data.get('contributors', [])

                        if file_name not in files:
                            tmp_file = io.StringIO()  # create a temporary file in memory

                            if description:
                                # Extract description and use manipulate_text function to translate it in the {language}
                                prompt = f"translate the following text into {language} :\n '{description}'"
                                while True:
                                    try:
                                        translation = translate_text(prompt)
                                        break
                                    except RateLimitError as e:
                                        print("Rate limit error occurred. Retrying in 5 seconds...")
                                        time.sleep(5)
                                    except Timeout as e:
                                        print("Timeout error occurred. Retrying in 5 seconds...")
                                        time.sleep(5)
                                    except APIError as e:
                                        print("API error occurred. Retrying in 5 seconds...")
                                        time.sleep(5)

                                # Write the translated description to the temporary file
                                tmp_file.write('description: |\n')
                                tmp_file.write("  " + '\n  '.join(translation.splitlines()) + '\n' )

                            # If contributors field is not present or is not a list, create an empty list
                            if not isinstance(contributors, list):
                                contributors = []

                            # Add 'another-satoshi' to the list of contributors
                            contributors.append('another-satoshi')

                            # Write the contributors to the temporary file
                            tmp_file.write('contributors:\n')
                            for contributor in contributors:
                                tmp_file.write('  - ' + contributor + '\n')

                            # Save the temporary file as {language_code}.yml
                            with open(os.path.join(root, file_name), 'w') as file:
                                file.write(tmp_file.getvalue())
                            tmp_file.close()
                    language_progress.update()
                folder_progress.update()


# Translate all builders description
process_files()
