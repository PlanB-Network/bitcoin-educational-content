from PIL import Image
import os
import re
import sys

def convert_to_webp_and_remove_metadata(root_dir):
    total_reduction_percentage = 0
    num_converted_files = 0

    # Debugging: Print the absolute path to verify correct directory
    print("Root directory absolute path:", os.path.abspath(root_dir))

    total_files = sum([len(files) for r, d, files in os.walk(root_dir) if any(f.lower().endswith(('.png', '.jpg', '.jpeg')) for f in files)])
    print(f"Total image files found: {total_files}")

    for root, dirs, files in os.walk(root_dir):
        # Debugging: Print each directory being walked
        print("Walking through:", root)
        if not files:
            print("No files in this directory.")
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)
                print("Processing file:", img_path)  # Debugging: Show which file is being processed

                original_size = os.path.getsize(img_path)  # Get original file size
                img = Image.open(img_path)
                webp_path = f"{os.path.splitext(img_path)[0]}.webp"

                # Save as WebP without metadata
                img.save(webp_path, "WEBP", quality=90, optimize=True, method=6, save_all=True, include_metadata=False)
                converted_size = os.path.getsize(webp_path)  # Get converted file size

                reduction_percentage = (original_size - converted_size) / original_size * 100
                total_reduction_percentage += reduction_percentage
                num_converted_files += 1

                # Remove the original file
                os.remove(img_path)

                # Print update progress
                sys.stdout.write(f"\rConverted {num_converted_files}/{total_files} files. Last: {file} -> {os.path.basename(webp_path)} | Reduction: {reduction_percentage:.2f}%")
                sys.stdout.flush()

    if num_converted_files > 0:
        average_reduction = total_reduction_percentage / num_converted_files
        print(f"\nAverage size reduction: {average_reduction:.2f}%")
    else:
        print("\nNo files were converted.")

def remove_metadata_from_existing_webp(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.webp'):
                webp_path = os.path.join(root, file)
                img = Image.open(webp_path)

                # Save WebP without metadata
                img.save(webp_path, "WEBP", quality=90, optimize=True, method=6, save_all=True, include_metadata=False)
                print(f"Metadata removed from: {webp_path}")

def update_md_links(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.md'):
                md_path = os.path.join(root, file)
                with open(md_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()

                # Replace image extensions except for 'thumbnail.png'
                updated_content = re.sub(r'\.(png|jpg|jpeg)(?!\.webp)', '.webp', content, flags=re.IGNORECASE)

                with open(md_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(updated_content)

                print(f"Updated image links in {md_path}")

if __name__ == "__main__":
    root_dir = './../resources/conference/lecture-pierre-rochard/assets/'
    convert_to_webp_and_remove_metadata(root_dir)  # Converts non-WebP files and strips metadata
    remove_metadata_from_existing_webp(root_dir)   # Ensures existing WebP files have no metadata
    update_md_links(root_dir)                      # Updates markdown links

