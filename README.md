# **Proton Pass CSV Duplicate Cleaner**

A simple Python script to clean duplicate entries from a Proton Pass CSV export. It identifies duplicates based on the combination of name, username, password and url, keeping only the first unique entry.

## **What it does**

When you export your data from Proton Pass, you might end up with duplicate entries, especially if you have imported data from other password managers. This script automates the process of cleaning them up.

It finds the exported CSV file in the same directory, removes the duplicate rows, and saves the clean data to a new file called `protonpass_export_cleaned.csv`.

## **How to Use** 
**(don't skip step 5)**

### **1. Prerequisites**

You need to have Python 3 and the Pandas library installed. If you don't have Pandas, you can install it via pip:

```bash 
pip install pandas
```
**Download the script** and place it in a new folder on your computer.  


### **2. Export your Vault as CDV**
1.  Click on Settings (bottom left next to your profile)
2.  Go to Export
3.  Export as CSV
4.  Authenticate
5.  Save it to the same new folder where the script is located

### **3. Running the Script**

1. **Open a terminal** or command prompt, navigate to the folder, and run the script:
   ```bash 
   python clean.py
   ```
2. A new file named `protonpass_export_cleaned.csv` will be created in the folder. You can now import this cleaned file back into Proton Pass or any other password manager.

### **4. In Proton Pass**

1. Click on Settings
2. Go to Import
3. Select Proton Pass
4. Select your `protonpass_export_cleaned.csv`
5. Select "New Vault"
6. Delete your old vault

### **5. IMPORTANT! Clean up your files**

After successfully importing your cleaned data and deleting your old vault in Proton Pass, it is **CRUCIAL** to securely delete the CSV files from your computer. You have two options for this:

**Option A: Use the delete.py script (Recommended for automation)**

The delete.py script automates the deletion process for you.

1. **Open a terminal** or command prompt, navigate to the folder where you saved the scripts and CSV files, and run the deletion script:  
   python delete.py

   This script will automatically find and delete both the original protonpass_export_*.csv file(s) and the protonpass_export_cleaned.csv file.

**Option B: Manual Deletion**

If you prefer to delete the files manually:

1. Locate the protonpass_export_*.csv file (your original export) and the protonpass_export_cleaned.csv file in the folder where you ran the scripts.  
2. **Securely delete both .csv files** from your computer.
3. **Empty your computer's trash/recycle bin** immediately after deleting the files.  

## **License**

This project is licensed under the **MIT License**. See the LICENSE file for more details. You are free to use, modify, and distribute this script.