import os
import re
import sys
import pandas as pd

def rename_fasta(household_path, directory_path):
    # Load the CSV file
    df = pd.read_csv(household_path)
    
    # Get a list of all .fa files in the directory that contain 'S129'
    files = [f for f in os.listdir(directory_path) if f.endswith('.fa') and 'SRR129' in f]
    
    # Process each file
    for file in files:
        file_path = os.path.join(directory_path, file)
        
        # Extract the number from the file name
        file_number = re.findall(r'\d+', file)[0]
        
        # Find matching row in the CSV file
        matching_row = df[df['filenames'].astype(str).str.contains(file_number)].head(1)
        
        if not matching_row.empty:
            # Create the new name using strain_type and household columns
            strain_type_initial = matching_row['strain_type'].values[0][0]
            household = matching_row['household'].values[0].replace('.', '')
            new_name = f"{strain_type_initial}_{household}.fa"
            new_file_path = os.path.join(directory_path, new_name)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed {file} to {new_name}")
        else:
            print(f"No match found for {file}")

if __name__ == "__main__":
    # Ensure that a CSV filename is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <household.csv>")
        sys.exit(1)
    
    # Get the CSV filename from the argument
    household_filename = sys.argv[1]
    
    # Get the directory where the script is located
    directory_path = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the CSV file
    household_path = os.path.join(directory_path, household_filename)
    
    # Run the renaming function
    rename_fasta(household_path, directory_path)

