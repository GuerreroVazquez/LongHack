import csv

# list of genes
genes = []

# read in list of genes from first CSV file
with open('gene_list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        genes.append(row[0])

# open second CSV file and create a new file to write filtered rows to
with open('ULLS.csv', 'r') as f, open('f_ULLS.csv', 'w') as f_out:
    reader = csv.reader(f)
    writer = csv.writer(f_out)
    for row in reader:
        # check if first column value is in list of genes
        if row[0] in genes:
            writer.writerow(row)