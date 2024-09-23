# Vibrio_Workflow
Workflow to analyze symptomatic and asymptomatic vibrio genomes  

Anvio Flow:
We have to make sure we get all the necessary files in one place. Let’s have all the 80 files we
have. First we filter the all household 58 fasta files.
1) Copy all the SRR129.. files to a new folder:
  ● Use the copy_SRR129_fa_files.py with the folder you want to copy the household 58
    files in. I chose the folder name to be 'household58'.
  ● Usage : python copy_SRR129_fa_files.py household58, where household58 is my
    new folder name.
2) Rename all the SRR129.. files, from the household format. Follow these steps:
  ● Go into the new folder you have created. cd household58/
  ● Execute python script rename_fasta_to_household.py with the csv containing the
    household key. Execute it like this:
  ● python rename_fasta_to_household.py Hypermutator_cholera_strains.csv

Start the anvi'o code flow :
1. We need to convert all the fasta files to their respective anvio contigs database files with
   extension .db
  ● Run the create_contigs_db.sh script. These files need to be arranged in a
    TAB-delimited way to be used.
2. Create a TAB delimited text file which has the .fa file name and its respective .db
   filename under two columns.
  ● First column 'name' has the fasta filenames. Second column 'contigs_db_path' has the
    respective path to the .db file.
  ● An external-genomes.txt file will be created. This file will be used to create a
    concatenated-protein.fa file by anvio. This file is automatically created once you run the
    create_contigs_db.sh.
3. Once we have the external-genomes.txt. Run the create_tree_with_anvio.sh script to
   get the phylogenomic tree for our samples.
4. To get the pangenome that will help us analyze the common core genes and the
   uncommon genes run the create_pangenome_anvio.sh script.
