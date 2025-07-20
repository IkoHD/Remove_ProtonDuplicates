import pandas as pd
import os

# --- Configuration ---
# The script will look for a file in this folder that starts with 'protonpass_export'.
FILE_PREFIX = 'protonpass_export'
# The clean data will be saved to this new file.
OUTPUT_FILENAME = 'protonpass_export_cleaned.csv'
# These columns are used to decide if a row is a duplicate.
DUPLICATE_CHECK_COLUMNS = ['name', 'username', 'password', 'url']


print("--- Proton Pass Duplicate Cleaner ---")

try:
    # --- Step 1: Find the input file ---
    print("--> Searching for your exported CSV file...")
    
    input_filename = None
    # This loop looks at all files in the current folder.
    for file in os.listdir('.'):
        # It checks if a file starts with the prefix and is a .csv file.
        if file.startswith(FILE_PREFIX) and file.endswith('.csv'):
            input_filename = file
            print(f"--> Found file: {input_filename}")
            break # We stop the loop after finding the first matching file.

    # If the loop finishes and no file was found, we stop the script with an error.
    if not input_filename:
        raise FileNotFoundError(
            f"No CSV file starting with '{FILE_PREFIX}' found in this folder.\n"
            "Please make sure your exported CSV file is in the same folder as this script."
        )

    # --- Step 2: Load the data from the CSV ---
    print(f"--> Loading data from {input_filename}...")
    df = pd.read_csv(input_filename)
    original_row_count = len(df)
    print(f"--> Loaded {original_row_count} total entries.")

    # --- Step 3: Remove the duplicate rows ---
    print(f"--> Removing duplicate entries...")
    # This is the core command. It finds and removes rows where the values
    # in the specified columns are all identical.
    df_cleaned = df.drop_duplicates(subset=DUPLICATE_CHECK_COLUMNS, keep='first')
    
    cleaned_row_count = len(df_cleaned)
    duplicates_found = original_row_count - cleaned_row_count
    print(f"--> Removed {duplicates_found} duplicate entries.")

    # --- Step 4: Save the clean data to a new file ---
    df_cleaned.to_csv(OUTPUT_FILENAME, index=False)
    print(f"\n✅ Success! Clean data saved to '{OUTPUT_FILENAME}'.")
    print(f"   The new file has {cleaned_row_count} unique entries.")

    # --- Step 5: IMPORTANT FINAL WARNING ---
    # This is the final, crucial reminder for security.
    print("\n" + "="*40)
    print("          IMPORTANT SECURITY NOTICE")
    print("="*40)
    print("The process is not finished yet!")
    print("Follow the steps in the README to import the new file")
    print("and securely delete the old vault and CSV files.")
    print("\n1. Import the cleaned file into a NEW vault in Proton Pass.")
    print("2. Delete your OLD vault in Proton Pass.")
    print("3. Securely delete BOTH .csv files from your computer.")
    print("4. Empty your computer's trash/recycle bin.")
    print("="*40)

# --- Error Handling ---
# If the file is not found, this message will be displayed.
except FileNotFoundError as e:
    print(f"\nERROR: {e}")
# If the CSV is missing a required column, this message will be displayed.
except KeyError:
    print("\nERROR: A required column was not found in the CSV file.")
    print(f"Please ensure the file has these columns: {', '.join(DUPLICATE_CHECK_COLUMNS)}")
# This will catch any other unexpected errors.
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
