import os


def prepare_git_branch():

    os.system("git checkout dev")
    os.system("git pull")
    os.system("git checkout -b auto-batch-translation")
    print("New branch updated and ready to proceed!")


def get_supported_languages():
    """Returns an array of strings with the names of all Markdown (*.md) files in the directory, excluding 'en.md'."""

    directory = "../../courses/btc101/"
    supported_languages = []

    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".md") and filename != "en.md":
                supported_languages.append(filename.split(".")[0])

    else:
        print("Directory does not exist.")

    return supported_languages


# Example usage:


def main():
    # prepare_git_branch()
    languages = get_supported_languages()
    print(languages)
    print("So far so good!")


if __name__ == "__main__":
    main()
