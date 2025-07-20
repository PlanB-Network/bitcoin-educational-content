These scripts are designed to calculate the word count for all courses and tutorials in the repository, enabling the extraction of rewards for any language. The results are then saved in an Excel file.

Specifically:

- **pending_rewards.py** generates a report of all available rewards for the content.
- **total_reward_budget.py** provides the total budget allocated for a specific language.

To use these scripts, follow these steps:

- Activate the environment as outlined in the "README" file of the previous directory.
- Install the necessary dependencies for Excel file handling by running the following command in your terminal:

```
pip install pandas openpyxl
```

Install the dependency for reading YAML files with this command:

```
pip install pyyaml
```