from PIL import Image
import os
import re

def convert_to_webp_and_calculate_savings(root_dir):
    total_reduction_percentage = 0
    num_converted_files = 0

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower() == 'thumbnail.png':
                print(f"Skipping conversion for {file}")
                continue

            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)
                original_size = os.path.getsize(img_path)  # Get original file size
                img = Image.open(img_path)
                webp_path = f"{os.path.splitext(img_path)[0]}.webp"

                img.save(webp_path, "WEBP")
                converted_size = os.path.getsize(webp_path)  # Get converted file size

                reduction_percentage = (original_size - converted_size) / original_size * 100
                total_reduction_percentage += reduction_percentage
                num_converted_files += 1

                print(f"Converted {img_path} to {webp_path}. Size reduction: {reduction_percentage:.2f}%")

                # Remove the original file
                os.remove(img_path)
                print(f"Removed original file: {img_path}")

    if num_converted_files > 0:
        average_reduction = total_reduction_percentage / num_converted_files
        print(f"Average size reduction: {average_reduction:.2f}%")
    else:
        print("No files were converted.")

def update_md_links(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.md'):
                md_path = os.path.join(root, file)
                with open(md_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()

                # Replace image extensions except for 'thumbnail.png'
                updated_content = re.sub(r'(?<!thumbnail)\.(png|jpg|jpeg)(?!\.webp)', '.webp', content, flags=re.IGNORECASE)

                with open(md_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(updated_content)

                print(f"Updated image links in {md_path}")

if __name__ == "__main__":
    root_dir = '../courses/btc101/'
    convert_to_webp_and_calculate_savings(root_dir)
    update_md_links(root_dir)

