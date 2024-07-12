# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:46:21 2024

@author: Ariadna Canari
"""
'''
This script does the following:

Loads the Dataset: It loads the dataset from the specified file path using 
pandas' read_csv function.

Displays Basic Statistics: It prints out basic statistics of the dataset 
using the describe function, which includes count, mean, standard deviation, 
minimum, and maximum values for each numeric column.

Displays Correlation Matrix: It prints out the correlation matrix of the 
dataset using the corr function, which shows the correlation coefficients 
between all pairs of numeric columns in the dataset.

To use this script, you would run it and provide the file path of the dataset
you want to analyze when prompted. Then, it will output the basic statistics 
and correlation matrix of the dataset.
'''
import pandas as pd
import os
import matplotlib.pyplot as plt

def save_statistics(file_path, statistics):
    """
    Saves statistics to a text file.

    Args:
        file_path (str): The path to the output file.
        statistics (str): The statistics to be saved.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(statistics)
    print("Statistics saved to", file_path)

def save_parameter_description(file_path):
    """
    Saves parameter descriptions to a text file.

    Args:
        file_path (str): The path to the output file.

    Returns:
        None
    """
    parameter_description = """Parameter Description:
- count: The number of non-missing (non-zero) observations in each column.
- mean: The average of the values in each column.
- std: The standard deviation of the values in each column. The standard deviation measures the dispersion of the data. The larger the standard deviation, the more scattered the data are around the mean.
- min: The minimum value in each column.
- 25%: The 25th percentile (or first quartile) of the data, which is the value below which 25% of the data falls.
- 50%: The 50th percentile (or median) of the data, which is the value below which 50% of the data falls.
- 75%: The 75th percentile (or third quartile) of the data, which is the value below which 75% of the data falls.
- max: The maximum value in each column.

These statistics provide an overview of the distribution and variability of your data in each column. For example, you can look at the mean, median, and percentiles to understand the central tendency and dispersion of the data, as well as the minimum and maximum to understand the range of values."""
    
    with open(file_path, 'w') as file:
        file.write(parameter_description)
    print("Parameter description saved to", file_path)

def plot_histogram(y_sh_values, output_folder):
    """
    Plots a histogram for the Y_SH column in the dataset.

    Args:
        y_sh_values (pd.Series): Series containing Y_SH values.
        output_folder (str): The path to the output folder where the histogram will be saved.

    Returns:
        None
    """
    # Set a nicer style for the plot
    plt.style.use('seaborn-darkgrid')

    # Create figure and axis objects
    fig, ax = plt.subplots(figsize=(10, 6), dpi=500)

    # Create histogram
    ax.hist(y_sh_values, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

    # Add labels and title
    ax.set_xlabel('Scarp-heigth (m)', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.set_title('Scarp-Heigth Histogram', fontsize=16,fontweight='bold', y=1.05)
    ax.xaxis.labelpad = 12  # Ajusta el espaciado entre la etiqueta del eje x y el eje x
    ax.yaxis.labelpad = 12  # Ajusta el espaciado entre la etiqueta del eje y y el eje y

    # Set tick parameters for better visibility
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.tick_params(axis='both', which='minor', labelsize=12)

    # Add grid
    ax.grid(True)

    # Save histogram to a file
    histogram_file = os.path.join(output_folder, "Y_SH_histogram.jpg")
    plt.savefig(histogram_file)

    # Show plot
    plt.show()

    print("Histogram saved to", histogram_file)


def basic_statistics(dataset_path, output_folder):
    """
    Performs basic statistical analysis on a dataset.

    Args:
        dataset_path (str): The path to the dataset file or directory.
        output_folder (str): The path to the output folder where statistics files will be saved.

    Returns:
        None
    """
    # Check if the path exists
    if not os.path.exists(dataset_path):
        print("Path not found:", dataset_path)
        return

    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Check if the path is a file
    if os.path.isfile(dataset_path):
        # Load the dataset
        try:
            df = pd.read_excel(dataset_path, engine='openpyxl')
        except Exception as e:
            print("Error reading Excel file:", e)
            return

        # Check if DataFrame has columns
        if df.columns.empty:
            print("DataFrame has no columns.")
            return

        # Perform basic statistics
        statistics = df.describe().to_string()

        # Save statistics to a text file
        file_name = os.path.basename(dataset_path) + "_statistics.txt"
        save_statistics(os.path.join(output_folder, file_name), statistics)

        # Save parameter description to a text file
        parameter_description_file = os.path.join(output_folder, "statistics_parameters.txt")
        save_parameter_description(parameter_description_file)

        # Plot histogram for Y_SH column
        if 'Y_SH' in df.columns:
            plot_histogram(df['Y_SH'], output_folder)
        else:
            print("Column 'Y_SH' not found in the dataset.")
        
        # Display basic statistics
        print("Basic Statistics for", os.path.basename(dataset_path) + ":")
        print(statistics)
        
        # Display correlation matrix
        print("\nCorrelation Matrix for", os.path.basename(dataset_path) + ":")
        print(df.corr())
        
    else:
        # Check files in the directory
        files = os.listdir(dataset_path)
        files = [f for f in files if f.endswith('.xlsx')]

        if not files:
            print("No supported files found in the directory:", dataset_path)
            return

        # Combine data from all files
        combined_df = pd.DataFrame()
        for file in files:
            file_path = os.path.join(dataset_path, file)
            if file.endswith('.xlsx'):
                try:
                    df = pd.read_excel(file_path, engine='openpyxl')
                except Exception as e:
                    print("Error reading Excel file:", e)
                    continue
                combined_df = pd.concat([combined_df, df], ignore_index=True)

                # Perform basic statistics on individual file
                file_statistics = df.describe().to_string()

                # Save individual file statistics to a text file
                file_name = os.path.basename(file_path) + "_statistics.txt"
                save_statistics(os.path.join(output_folder, file_name), file_statistics)

                # Save parameter description to a text file
                parameter_description_file = os.path.join(output_folder, "statistics_parameters.txt")
                save_parameter_description(parameter_description_file)

                # Display basic statistics for individual file
                print("Basic Statistics for", os.path.basename(file_path) + ":")
                print(file_statistics)

                # Display correlation matrix for individual file
                print("\nCorrelation Matrix for", os.path.basename(file_path) + ":")
                print(df.corr())

        # Plot histogram for combined data
        if not combined_df.empty:
            plot_histogram(combined_df['Y_SH'], output_folder)

        # Perform basic statistics on combined data
        if not combined_df.empty:
            combined_statistics = combined_df.describe().to_string()

            # Save combined statistics to a text file
            combined_statistics_file = os.path.join(output_folder, "combined_statistics.txt")
            save_statistics(combined_statistics_file, combined_statistics)

            # Display combined statistics
            print("Combined Basic Statistics:")
            print(combined_statistics)

            # Display correlation matrix
            print("\nCombined Correlation Matrix:")
            print(combined_df.corr())
            
if __name__ == "__main__":
    dataset_path = input("Enter the dataset file path or directory: ")
    output_folder = input("Enter the output folder path: ")
    basic_statistics(dataset_path, output_folder)


