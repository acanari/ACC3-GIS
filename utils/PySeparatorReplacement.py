# -*- coding: utf-8 -*-
"""
This file is part of Project PySeparatorReplacement.
Copyright (c) 2024 Canari.A
This code is licensed under the GNU GPL License.
See the LICENSE file in the project root for license terms.
"""
'''
This script processes all Excel, CSV, and TXT files in a specified directory, performing character 
replacements in the text cells of the DataFrames. The default operation replaces commas with periods. 
You can easily switch to other replacements by uncommenting the appropriate lines.

Operations:
1. Replace commas with periods (default).
2. Replace periods with commas.
3. Replace periods with semicolons.
4. Replace semicolons with commas.

Instructions:
- To replace commas with periods: no action needed, this is the default behavior.
- To replace periods with commas: uncomment the respective line in the code.
- To replace periods with semicolons: uncomment the respective line in the code.
- To replace semicolons with commas: uncomment the respective line in the code.
'''

import pandas as pd
import os

# Path to the directory containing the files
directory = 'D:/Py_Plots-SH/data-results'

# List of files in the directory
files = os.listdir(directory)

# Iterate over each file in the directory
for file in files:
    file_path = os.path.join(directory, file)
    if file.endswith('.xlsx'):  # Process Excel files
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        
        # Replace commas with periods in the entire DataFrame
        df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace periods with commas
        # df = df.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace periods with semicolons
        # df = df.applymap(lambda x: str(x).replace('.', ';') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace semicolons with commas
        # df = df.applymap(lambda x: str(x).replace(';', ',') if isinstance(x, str) else x)
        
        # Save the modified DataFrame back to the same Excel file
        df.to_excel(file_path, index=False)
        
        print(f"Separators of Excel files have been replaced in '{file}' successfull :)")
        
    elif file.endswith('.csv'):  # Process CSV files
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Replace commas with periods in the entire DataFrame
        df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace periods with commas
        # df = df.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace periods with semicolons
        # df = df.applymap(lambda x: str(x).replace('.', ';') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace semicolons with commas
        # df = df.applymap(lambda x: str(x).replace(';', ',') if isinstance(x, str) else x)
        
        # Save the modified DataFrame back to the same CSV file
        df.to_csv(file_path, index=False)
        
        print(f"Separators of CSV files have been replaced in '{file}' successfull :)")
        
    elif file.endswith('.txt'):  # Process TXT files
        # Read the TXT file into a DataFrame
        df = pd.read_csv(file_path, delimiter='\t')  # Assuming tab-delimited TXT file
        
        # Replace commas with periods in the entire DataFrame
        df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace periods with commas
        # df = df.applymap(lambda x: str(x).replace('.', ',') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace periods with semicolons
        # df = df.applymap(lambda x: str(x).replace('.', ';') if isinstance(x, str) else x)
        
        # Uncomment the following line to replace semicolons with commas
        # df = df.applymap(lambda x: str(x).replace(';', ',') if isinstance(x, str) else x)
        
        # Save the modified DataFrame back to the same TXT file
        df.to_csv(file_path, sep='\t', index=False)
        
        print(f"Separators of txt files have been replaced in '{file}' successfull :)")
