# Add proofreading metadata

author: asi0

## Purpose

- add the proofreading metadata section in all content yaml file
  - except `podcast.yml` and `event.yml` and `professor.yml`

## Usage

- `add-proofreading-metadata.py` is used to add the template section in all predefined yaml files
- `set-proofreading-reward.py` is used to compute and set the reward of any content for all supported langugages
- `update-proofreading-metadata.py` will be soon™ written and used to update the reward if a new `reviewers_id` has been added

## Depedencies

- `ruamel.yaml`

---

- [ ] create a lib py file
- [ ] function: set urgency to value
- [ ] function: compute reward
- [ ] function: print the reward
- [ ] function: print the urgency
- [ ] function: print state of proofreading
- [ ] function: get specific data for given content and language
- [ ] function: add new language section for update process
- [ ] function: add new supported language
- [ ] function: ask for new contribution
- [ ] function to update proofreading metadata
  - hypothesis: for any new content there is ALWAYS at least the proofreading section in the original language with the author mentionned as the first proofreading
  - hypothesis 2: only check for code language present is a dictionnary with the associated language difficulty factor
  - this allows us to reduce the update process to a single case : check if {code_language}.yml or md does the code language is listed in the proofreading section
  - if so go on
  - otherwise
    - add the 4 properties
    - last_contribution_date
    - contributions_id
    - urgency:
    - reward:
    - set urgency to 1 per default
    - compute the corresponding reward
