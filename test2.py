import matplotlib.pyplot as plt
import pandas as pd
import os
import glob


def plot_score_over_time(filenames, labels):
    """
    Plots the 'score' variable over time for multiple CSV files.

    Args:
        filenames: A list of CSV file paths.
        labels: A list of labels corresponding to the files (for the legend).
    """

    if len(filenames) != len(labels):
        raise ValueError("The number of filenames and labels must match.")

    plt.figure(figsize=(12, 6))

    for filename, label in zip(filenames, labels):
        try:
            # Read the CSV file, handling potential errors. Use ; as separator.
            df = pd.read_csv(filename, sep=';')

            # Check if the required columns exist
            if 'score' not in df.columns or 'tick_nr' not in df.columns:
                print(f"Warning: File '{filename}' is missing 'score' or 'tick_nr' column. Skipping.")
                continue
            
            # Convert to numeric and handle NaNs
            df['score'] = pd.to_numeric(df['score'], errors='coerce')  # Convert to numeric, invalid parsing will result in NaN
            df['tick_nr'] = pd.to_numeric(df['tick_nr'], errors='coerce')
            df.dropna(subset=['score', 'tick_nr'], inplace=True) #remove rows with invalid data

            # Ensure the DataFrame isn't empty *after* cleaning
            if df.empty:
                 print(f"Warning: File '{filename}' contains no valid data after cleaning. Skipping.")
                 continue

            # Plot the score over time
            plt.plot(df['tick_nr'], df['score'], label=label)

        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return  # Exit if a file is not found
        except pd.errors.EmptyDataError:
            print(f"Error: File is empty: {filename}")
            return
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")
            return

    plt.xlabel('Tick Number')
    plt.ylabel('Score')
    plt.title('Score Over Time')
    plt.legend()
    plt.grid(True)  # Add grid for better readability
    plt.tight_layout()
    plt.savefig("ben_score_comparisons.png")


# Example usage (assuming you have files named 'file1.csv', 'file2.csv', etc.):
# Method 1: Specify filenames directly
# filenames = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv']

# Method 2: Using glob (much more robust and preferred)
filenames = ['logs/exp_normal_at_time_17h-57m-26s_date_09d-03m-2025y/world_1/actions__2025-03-09_175727.csv', 'logs/exp_normal_at_time_18h-34m-26s_date_09d-03m-2025y/world_1/actions__2025-03-09_183427.csv', 'logs/exp_normal_at_time_19h-03m-12s_date_09d-03m-2025y/world_1/actions__2025-03-09_190313.csv', 'logs/exp_normal_at_time_19h-22m-03s_date_09d-03m-2025y/world_1/actions__2025-03-09_192204.csv']
runnames = [
    "run 1 - never trust",
    "run 2 - always trust",
    "run 3 - random trust",
    "run 4 - normal",
]

# Method 3: Manually enter file paths and provide their names.

if not filenames:
    print("No CSV files found in the current directory.")
else:
    # Create corresponding labels.  Extract names from filenames, handling different OS paths
    labels = [os.path.splitext(os.path.basename(f))[0] for f in filenames] #extracts file name
    plot_score_over_time(filenames, runnames)