# -*- coding: utf-8 -*-
"""
This file is part of Project Pyconvert_format.
Copyright (c) 2024 Canari.A
This code is licensed under the MIT License.
See the LICENSE file in the project root for license terms.
"""

import os
import pandas as pd

def convert_format(input_folder, output_folder):
    """
    Converts files from one format to another.

    Args:
        input_folder (str): The input folder path containing files to be converted.
        output_folder (str): The output folder path where converted files will be saved.

    Returns:
        None
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("Output folder created:", output_folder)

    # Iterate over each file in the input folder
    for file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, file_name)
        
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            # Construct the output file path with the same name but with .xlsx extension
            output_file_path = os.path.join(output_folder, file_name[:-4] + '.xlsx')
            
            # Load the input CSV file
            df = pd.read_csv(input_file_path)
            
            # Convert to Excel format and save the file
            df.to_excel(output_file_path, index=False)
            
            print("Conversion successful. File saved as", output_file_path)

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ")
    
    # Set the output folder path by adding the .xlsx extension to the input folder name
    output_folder = input_folder + "_xlsx"
    
    convert_format(input_folder, output_folder)

