## Proofreading Scripts

As the proofreading progress for each educational content has been added to the associated `yml` file. It would be far easier to manage it via in
CLI-interactive script, hence `update_proofreading_metadata.py`.

In the near future a complementary script for reporting the progress of any
content in any language would be available.

## Usage

Note that these scripts have only been tested on a linux distro.

### Set python environment

Use the below command to create a env in the `./scripts/proofreading_metadata`
folder.

```
python3 -m venv env
```

Use this command to activate the env

```
source env/bin/activate
```

And use `deactivate` to quit the environment.

Then make sure you have the required librairies with the following command

```
pip3 install -r requirements.txt
```

### Run the interactive Proofreading Update Script

Please verify that you're environment is activated before running the below
command:

```
python3 update_proofreading_metadata.py
```

Then follow the workflow by answering to the prompted questions via the CLI.

### Run the interactive Proofreading Reward Calculator Script

Please verify that you're environment is activated before running the below
command:

```
python3 evaluate_proofreading_reward.py
```

Then follow the workflow by answering to the prompted question via the CLI.

## Miscellouneous notes

- note that `proofreading.py` is used as a common 'library' for functions
  related to proofreading propreties
- note that the automatic process in `update_proofreading_metadata.py` is quite
  slow, especially when the full update (reward re-evaluation) is chosen.
  - would be cool in the future to replace that part with a dedicated C script
    to do the full update in a way more faster way.
    - the use of a `.sh` file would be used to run the C script and then the
      python script
