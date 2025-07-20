# **Proton Pass CSV Duplicate Cleaner**

A simple Python script to clean duplicate entries from a Proton Pass CSV export. It identifies duplicates based on the combination of name, username, and url, keeping only the first unique entry.

## **What it does**

When you export your data from Proton Pass, you might end up with duplicate entries, especially if you have imported data from other password managers. This script automates the process of cleaning them up.

It finds the exported CSV file in the same directory, removes the duplicate rows, and saves the clean data to a new file called protonpass\_export\_cleaned.csv.

## **How to Use**

### **1\. Prerequisites**

You need to have Python 3 and the Pandas library installed. If you don't have Pandas, you can install it via pip:

pip install pandas

### **2\. Running the Script**

1. **Download the script** and place it in a folder on your computer.  
2. **Export your data** from Proton Pass as a CSV file and place it in the **same folder** as the script. The script will automatically detect any file that starts with protonpass\_export and ends with .csv.  
3. **Open a terminal** or command prompt, navigate to the folder, and run the script:  
   python clean.py
4. A new file named protonpass\_export\_cleaned.csv will be created in the folder. You can now import this cleaned file back into Proton Pass or any other password manager.

### **3\. In Proton Pass**

1. Click on Settings
2. Go to Import
3. Select Proton Pass
4. Select your protonpass\_export\_cleaned.csv
5. Select "New Vault"
6. Delete your old vault


## **License**

This project is licensed under the **MIT License**. See the LICENSE file for more details. You are free to use, modify, and distribute this script.