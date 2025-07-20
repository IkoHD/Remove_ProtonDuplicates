import pandas as pd
import os

# 1. Define the file prefix and the name for the output file.
# The script will look for any .csv file that starts with this prefix.
file_prefix = 'protonpass_export'
output_filename = 'protonpass_export_cleaned.csv'

# --- Automatically find the input file ---
input_filename = None
try:
    for file in os.listdir('.'):
        # Check if a file in the current directory starts with the prefix and is a csv
        if file.startswith(file_prefix) and file.endswith('.csv'):
            input_filename = file
            break  # Stop after finding the first matching file

    if not input_filename:
        # Raise an error if no matching file was found
        raise FileNotFoundError(f"No CSV file starting with '{file_prefix}' found in this directory.")

    # --- Process the found file ---
    print(f"Input file found: {input_filename}")
    
    # 2. Read the CSV file
    # Pandas reads the data into a table structure called a DataFrame.
    df = pd.read_csv(input_filename)
    
    print(f"Number of rows before cleaning: {len(df)}")
    
    # 3. Remove duplicates
    # Duplicates are identified based on the combination of these columns.
    df_cleaned = df.drop_duplicates(subset=['name', 'username', 'url'])
    
    # 4. Write the cleaned data to a new CSV file
    # index=False prevents pandas from writing a new column for row numbers.
    df_cleaned.to_csv(output_filename, index=False)
    
    print(f"Number of rows after cleaning: {len(df_cleaned)}")
    print(f"Cleaned data has been saved to '{output_filename}'. ✅")

except FileNotFoundError as e:
    print(f"ERROR: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")