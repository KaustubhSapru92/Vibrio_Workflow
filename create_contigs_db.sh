#!/bin/bash

# Reformat FASTA files to comply with anvi'o requirements
for i in `ls *fa | awk 'BEGIN{FS=".fa"}{print $1}'`
do
    anvi-script-reformat-fasta -o $i.reformatted.fa -l 0 --simplify-names $i.fa
    mv $i.reformatted.fa $i.fa
done

# Run anvi'o commands
for i in `ls *fa | awk 'BEGIN{FS=".fa"}{print $1}'`
do
    anvi-gen-contigs-database -f $i.fa -o $i.db -T 8
    anvi-run-hmms -c $i.db
done

# Run the Python script
python create_TAB_file.py
