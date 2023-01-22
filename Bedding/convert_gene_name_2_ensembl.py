import pandas as pd
from bioservices import *

# Read in the gene mapping file
gene_mapping = pd.read_csv("gene_mapping.csv")

# Create an instance of the BioMart service
ensembl = BioMart()

# Connect to the Ensembl database
ensembl.new_query()
ensembl.add_dataset_to_xml("hsapiens_gene_ensembl")

# Map the gene names to their Ensembl IDs
ensembl_ids = []
for name in gene_mapping['Gene Symbol']:
    ensembl.add_attribute_to_xml("external_gene_name")
    ensembl.add_filter_to_xml("external_gene_name", name)
    result = ensembl.results()
    if result:
        ensembl_ids.append(result[0][0])
    else:
        ensembl_ids.append(None)

# Add the Ensembl IDs as a new column in the gene mapping file
gene_mapping['ensembl_id'] = ensembl_ids

# Output the mapped gene mapping file
gene_mapping.to_csv("mapped_gene_mapping.csv", index=False)
