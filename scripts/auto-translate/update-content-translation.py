import os


def prepare_git_branch():

    os.system("git checkout dev")
    os.system("git pull")
    os.system("git checkout -b auto-batch-translation")
    print("New branch updated and ready to proceed!")


def main():
#    prepare_git_branch()


if __name__ == "__main__":
    main()
