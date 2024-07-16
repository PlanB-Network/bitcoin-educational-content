import os

def update_files():
    builder_folder = "../resources/builders"
    folders = os.listdir(builder_folder)
    total_folders = len(folders)
    processed_folders = 0

    for folder in folders:
        folder_path = os.path.join(builder_folder, folder)
        if os.path.isdir(folder_path):
            builder_file_path = os.path.join(folder_path, "builder.yml")
            en_file_path = os.path.join(folder_path, "en.yml")

            # Update builder.yml file
            with open(builder_file_path, "r+") as builder_file:
                lines = builder_file.readlines()
                builder_file.seek(0)

                for line in lines:
                    if not (line.startswith("contributors:") or line.startswith("  - rabbit-hole")):
                        builder_file.write(line)

                builder_file.truncate()

            # Update en.yml file
            with open(en_file_path, "a") as en_file:
                en_file.write("\n")
                en_file.write("contributors:\n")
                en_file.write("  - rabbit-hole\n")

        processed_folders += 1
        progress_percentage = (processed_folders / total_folders) * 100
        print(f"Progress: {progress_percentage:.2f}%")

update_files()

