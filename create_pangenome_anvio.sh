#!/bin/bash

# Check if external-genomes.txt exists
if [[ ! -f "external-genomes.txt" ]]; then
    echo "Error: external-genomes.txt not found!"
    exit 1
fi

# Step 1: Generate anvi'o genomes storage
echo "Running anvi-gen-genomes-storage..."
anvi-gen-genomes-storage -e external-genomes.txt \
                         -o household_58-GENOMES.db

# Check if the output file was created
if [[ ! -f "Salmonella-GENOMES.db" ]]; then
    echo "Error: Salmonella-GENOMES.db not created!"
    exit 1
fi

# Step 2: Perform pangenomic analysis
echo "Running anvi-pan-genome..."
anvi-pan-genome -g household_58-GENOMES.db \
                --project-name household_58 \
                --num-threads 8

# Check if the output directory and database were created
if [[ ! -d "Salmonella" || ! -f "Salmonella/Salmonella-PAN.db" ]]; then
    echo "Error: Pangenome analysis did not complete successfully!"
    exit 1
fi

# Step 3: Display the pangenome
echo "Running anvi-display-pan..."
anvi-display-pan -g household_58-GENOMES.db \
                 -p household_58/household_58-PAN.db

echo "Pangenome analysis script executed successfully!"

