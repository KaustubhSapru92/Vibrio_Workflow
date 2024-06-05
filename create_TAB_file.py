import os

# Get the directory where the script is located
directory_path = os.path.dirname(os.path.abspath(__file__))

# Get lists of .fa and .db files in the directory
fa_files = [f for f in os.listdir(directory_path) if f.endswith('.fa')]
db_files = [f for f in os.listdir(directory_path) if f.endswith('.db')]

# Create a set of .db filenames without extensions for quick lookup
db_files_set = {os.path.splitext(db_file)[0] for db_file in db_files}

# List to store the rows for the tab-delimited file
rows = []

# Check for matching .fa and .db files
for fa_file in fa_files:
    fa_name = os.path.splitext(fa_file)[0]
    if fa_name in db_files_set:
        db_file = fa_name + '.db'
        #contigs_db_path = os.path.join(directory_path, db_file)
        rows.append(f"{fa_name}\t{db_file}")

        
# Write the rows to the tab-delimited file
output_file_path = os.path.join(directory_path, 'external-genomes.txt')
with open(output_file_path, 'w') as output_file:
    output_file.write("name\tcontigs_db_path\n")
    output_file.write("\n".join(rows))

print(f"Tab-delimited file 'external-genomes.txt' has been created successfully.")

