import os
from pathlib import Path
import pandas as pd

def find_project_root():
    """
    Find the project root by looking for 'bitcoin-educational-content' directory
    in parent directories.
    """
    current_dir = Path(__file__).resolve().parent
    while current_dir.name != 'bitcoin-educational-content' and current_dir != current_dir.parent:
        current_dir = current_dir.parent
    if current_dir.name != 'bitcoin-educational-content':
        raise FileNotFoundError("Could not find 'bitcoin-educational-content' directory in parent path")
    return current_dir

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return len(file.read().split())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def process_courses(base_path):
    results = []
    for folder in base_path.iterdir():
        if folder.is_dir():
            md_file = folder / 'en.md'
            if md_file.exists():
                results.append({
                    'Folder': folder.name,
                    'Word Count': count_words_in_file(md_file)
                })
    return results

def process_tutorials(base_path):
    results = []
    # Only process level 2 directories (sub-sub-folders)
    for level1 in base_path.iterdir():
        if level1.is_dir():
            for level2 in level1.iterdir():
                if level2.is_dir():
                    md_file = level2 / 'en.md'
                    if md_file.exists():
                        results.append({
                            'Folder': level2.name,
                            'Word Count': count_words_in_file(md_file)
                        })
    return results

def add_payment_calculations(df):
    """
    Add payment calculations for different language factors from 1.0 to 3.0
    """
    base_rate = 0.006
    multipliers = [x/2 for x in range(2, 7)]  # Creates [1.0, 1.5, 2.0, 2.5, 3.0]
    
    for multiplier in multipliers:
        column_name = f'Language factor {multiplier}'
        df[column_name] = df['Word Count'] * base_rate * multiplier
    
    # Add totals row
    totals = pd.Series({'Folder': 'TOTAL'})
    totals['Word Count'] = df['Word Count'].sum()
    
    # Calculate totals for each language factor column
    for column in df.columns:
        if column.startswith('Language factor'):
            totals[column] = df[column].sum()
    
    # Append totals row to DataFrame
    df = pd.concat([df, pd.DataFrame([totals])], ignore_index=True)
    
    return df

def main():
    try:
        # Find the project root directory
        project_root = find_project_root()
        
        # Define paths relative to the project root
        courses_path = project_root / 'courses'
        tutorials_path = project_root / 'tutorials'
        
        results = []
        results.extend(process_courses(courses_path))
        results.extend(process_tutorials(tutorials_path))
        
        # Create DataFrame and add payment calculations
        df = pd.DataFrame(results)
        df = add_payment_calculations(df)
        
        # Save results in the same directory as the script
        output_path = Path(__file__).parent / 'word_counts_with_payments.xlsx'
        
        # Save to Excel with number formatting
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            
            # Format currency columns with Euro symbol
            for col in range(3, worksheet.max_column + 1):  # Starting from first language factor column
                for row in range(2, worksheet.max_row + 1):  # Starting from first data row
                    cell = worksheet.cell(row=row, column=col)
                    cell.number_format = '€#,##0.00'
        
        print(f"Results saved to {output_path}")
        
        # Print summary
        print("\nSummary:")
        print(f"Total word count: {df['Word Count'].iloc[-1]:,}")
        for column in df.columns:
            if column.startswith('Language factor'):
                total = df[column].iloc[-1]
                print(f"{column}: €{total:.2f}")
        
    except FileNotFoundError as e:
        print("Error: Make sure this script is placed within the bitcoin-educational-content "
              "project directory structure.")
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
