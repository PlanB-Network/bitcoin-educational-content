# Auto-translation script for PBN content

When runned this script will

- switch to dedicated branch `auto-batch-translation`
- for each supported language,
  - check if any content is not translated in english
  - if so, run [LLM-Translator](https://github.com/Asi0Flammeus/LLM-Translator) and move back the translated files to corresponding subfolders and commit
- for each supported language
  - check if the english content has not been translated in that language
  - if so, run LLM-Translator and move back the translated files to
    corresponding subfolders and commit
- Push the branch and do a PR

## Requirements

- make sure that the branch `auto-batch-translation` doesn't exists
  - delete it after each PR
- both repo (this one and LLM-Translator) must be located in at the same level
  of hierarchy
- obviously LLM-Translator should be already set up
- `Hub` is necessary on your system to run the PR command
- need a fine-grained token to PR
- as relative path has been based on working directory, the python command must
  be runned in the same folder as the script
- if runned on a server, a ssh-key would have to be added in github
- to remove the manual authentication part for github, use `it config --global credential.helper cache` and run the script once (comment some functions to go directly to the authentication part) and enter username and token. Next time, nothing would be asked.
