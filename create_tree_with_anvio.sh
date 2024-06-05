#!/bin/bash

# Check if external-genomes.txt exists
if [[ ! -f "external-genomes.txt" ]]; then
    echo "Error: external-genomes.txt not found!"
    exit 1
fi

# Step 1: Get sequences for HMM hits
echo "Running anvi-get-sequences-for-hmm-hits..."
anvi-get-sequences-for-hmm-hits --external-genomes external-genomes.txt \
                                -o concatenated-ribosomal-proteins.fa \
                                --hmm-source Bacteria_71 \
                                --gene-names gene-names.txt \
                                --return-best-hit \
                                --get-aa-sequences \
                                --concatenate

# Check if the output file was created
if [[ ! -f "concatenated-proteins.fa" ]]; then
    echo "Error: concatenated-proteins.fa not created!"
    exit 1
fi

# Step 2: Compute the phylogenomic tree
echo "Running anvi-gen-phylogenomic-tree..."
anvi-gen-phylogenomic-tree -f concatenated-ribosomal-proteins.fa \
                           -o phylogenomic-tree.txt

# Check if the output file was created
if [[ ! -f "phylogenomic-tree.txt" ]]; then
    echo "Error: phylogenomic-tree.txt not created!"
    exit 1
fi

# Step 3: Run the interactive interface
echo "Running anvi-interactive..."
anvi-interactive -p phylogenomic-profile.db \
                 -t phylogenomic-tree.txt \
                 --title "Phylogenomics Tree for Household" \
                 --manual

echo "Script executed successfully!"
