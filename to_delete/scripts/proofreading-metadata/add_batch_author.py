import os

from proofreading import *
from datetime import datetime

current_date = datetime.now()
current_date = current_date.date()


root_directory = "../../"
#
for root, dirs, files in os.walk(root_directory):
    if 'docs' in dirs:
      dirs.remove('docs')
    for file in files:
        if file in specific_files:
            
            yml_file_path = os.path.join(root, file)
            print(yml_file_path)
            data = get_yml_content(yml_file_path)
            
            language = get_orignal(data)
            state = get_proofreading_state(data, language)
            if state == 0:
                add_proofreading_contributor(data, language, 'Asi0Flammeus')

                date = '2024-09-01'
                date = datetime.strptime(date, "%Y-%m-%d").date()
                update_proofreading_inline_property(data, language,
                                                    'last_contribution_date', date)
                update_yml_data(yml_file_path, data)
                print(data)
                print()
                print(f'{yml_file_path} has been updated')
#             
#
