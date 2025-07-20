import os
import glob

# --- Configuration ---
# The script will look for any CSV file starting with this prefix.
FILE_PREFIX = 'protonpass_export'

print("--- Proton Pass CSV File Deleter ---")

try:
    print(f"--> Searching for CSV files starting with '{FILE_PREFIX}'...")

    # Find all CSV files that start with the defined prefix
    # This will include both 'protonpass_export_*.csv' and 'protonpass_export_cleaned.csv'
    files_to_delete = glob.glob(f"{FILE_PREFIX}*.csv")

    if files_to_delete:
        deleted_count = 0
        for file_path in files_to_delete:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"--> Successfully deleted: {file_path}")
                deleted_count += 1
            else:
                print(f"--> File not found (already deleted?): {file_path}")

        if deleted_count > 0:
            print(f"\n✅ Success! Removed {deleted_count} specified CSV file(s).")
        else:
            print("\n--> No matching CSV files were found to delete.")

    else:
        print("\n--> No matching CSV files were found to delete.")

    print("Remember to empty your computer's trash/recycle bin for full security.")

# --- Error Handling ---
except OSError as e:
    # This catches errors like permission denied or other OS-related issues
    print(f"\nERROR: Could not delete a file. Please check permissions or if the file is open. You can also delete it manually and empty your bin afterwards.")
    print(f"Details: {e}")
except Exception as e:
    # Catch any other unexpected errors
    print(f"\nAn unexpected error occurred: {e}")

