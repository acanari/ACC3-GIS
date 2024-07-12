# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:34:46 2024

@author: Ariadna Canari
"""

'''
The function clean_data defines takes two parameters: 
input_file and output_file. This function will be responsible 
for cleaning the data from the input CSV file and saving the cleaned 
data to the output CSV file.
'''
import pandas as pd

def clean_data(input_file, output_file):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # Remove special characters
    df = df.applymap(lambda x: ''.join(filter(str.isalnum, str(x))))
    
    # Drop rows with null values
    df = df.dropna()
    
    # Save the cleaned data
    df.to_csv(output_file, index=False)
    
    print("Cleaned data saved to", output_file)

if __name__ == "__main__":
    input_file = input("Enter the input file name (CSV): ")
    output_file = input("Enter the output file name (CSV): ")
    
    clean_data(input_file, output_file)
