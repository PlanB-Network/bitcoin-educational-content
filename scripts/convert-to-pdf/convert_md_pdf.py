import os
import markdown
from weasyprint import HTML
import inquirer
from bs4 import BeautifulSoup
import shutil
import re

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_folders(base_path):
    """Get all folders in the base path"""
    try:
        return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return []

def get_md_files(folder_path):
    """Get all markdown files in the specified folder"""
    try:
        return [f for f in os.listdir(folder_path) if f.endswith('.md')]
    except Exception as e:
        print(f"Error accessing files: {e}")
        return []

def process_images(html_content, md_file_path):
    """Process images in HTML content to use absolute paths"""
    soup = BeautifulSoup(html_content, 'html.parser')
    md_dir = os.path.dirname(md_file_path)
    
    # Process all img tags
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and not src.startswith(('http://', 'https://', 'data:')):
            # Convert relative path to absolute path
            absolute_path = os.path.abspath(os.path.join(md_dir, src))
            if os.path.exists(absolute_path):
                img['src'] = f'file://{absolute_path}'
    
    return str(soup)

def convert_md_to_pdf(input_file, output_file):
    """Convert markdown file to PDF"""
    try:
        # Read markdown content
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert markdown to HTML
        html_content = markdown.markdown(
            md_content,
            extensions=['extra', 'codehilite', 'tables', 'md_in_html']
        )

        # Process images to use absolute paths
        html_content = process_images(html_content, input_file)

        # Add basic CSS for better formatting
        css = """
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 40px;
                line-height: 1.6;
            }
            img { 
                max-width: 100%; 
                height: auto; 
                display: block;
                margin: 20px auto;
            }
            code { 
                background-color: #f5f5f5; 
                padding: 2px 5px;
                border-radius: 3px;
                font-family: monospace;
            }
            pre { 
                background-color: #f5f5f5; 
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }
            a { 
                color: #0066cc;
                text-decoration: none;
            }
            table { 
                border-collapse: collapse; 
                width: 100%;
                margin: 20px 0;
            }
            th, td { 
                border: 1px solid #ddd; 
                padding: 12px 8px;
            }
            th { 
                background-color: #f5f5f5;
                font-weight: bold;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #333;
                margin-top: 24px;
                margin-bottom: 16px;
            }
            p {
                margin-bottom: 16px;
            }
            blockquote {
                border-left: 4px solid #ddd;
                padding-left: 16px;
                margin-left: 0;
                color: #666;
            }
        </style>
        """

        # Combine CSS and HTML content
        full_html = f"""
        <html>
            <head>{css}</head>
            <body>{html_content}</body>
        </html>
        """

        # Convert HTML to PDF
        HTML(string=full_html).write_pdf(output_file)
        return True
    except Exception as e:
        print(f"Error converting file: {e}")
        return False

def main():
    # Base path
    base_path = os.path.abspath("../../courses")
    
    # Get available folders
    folders = get_folders(base_path)
    if not folders:
        print("No folders found in the specified path!")
        return

    # Ask user to select a folder
    questions = [
        inquirer.List('folder',
                     message="Choose a folder for conversion",
                     choices=folders)
    ]
    answers = inquirer.prompt(questions)
    
    if not answers:
        print("No folder selected!")
        return

    selected_folder = answers['folder']
    folder_path = os.path.join(base_path, selected_folder)
    
    # Get markdown files in selected folder
    md_files = get_md_files(folder_path)
    if not md_files:
        print(f"No markdown files found in {selected_folder}!")
        return

    # Ask user to select files for conversion
    questions = [
        inquirer.Checkbox('files',
                         message="Select markdown files to convert (space to select, enter to confirm)",
                         choices=md_files)
    ]
    answers = inquirer.prompt(questions)
    
    if not answers or not answers['files']:
        print("No files selected!")
        return

    # Create output directory in script location if it doesn't exist
    output_dir = os.path.join(SCRIPT_DIR, 'pdf_output')
    os.makedirs(output_dir, exist_ok=True)

    # Convert selected files
    for md_file in answers['files']:
        input_path = os.path.join(folder_path, md_file)
        output_path = os.path.join(output_dir, f"{os.path.splitext(md_file)[0]}.pdf")
        
        print(f"\nConverting {md_file}...")
        if convert_md_to_pdf(input_path, output_path):
            print(f"Successfully converted {md_file} to PDF!")
            print(f"PDF saved at: {output_path}")
        else:
            print(f"Failed to convert {md_file}")

if __name__ == "__main__":
    main()

