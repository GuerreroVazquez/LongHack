import pandas as pd

# Read in the gene mapping file
gene_mapping = pd.read_csv("gene_mapping.csv")

# Read in the bedding file
bedding = pd.read_csv("bedding.csv")

# Merge the bedding file with the gene mapping file
bedding = pd.merge(bedding, gene_mapping, on='ID', how='left')

# Rename the column 'gene_name' to the first column
bedding = bedding.rename(columns={'gene_name': bedding.columns[0]})

# Output the mapped bedding file
bedding.to_csv("mapped_bedding.csv", index=False)
