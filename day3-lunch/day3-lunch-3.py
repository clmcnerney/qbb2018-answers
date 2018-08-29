#!/usr/bin/env python3

#Makes two dictionaries that will contain the name of each gene and the distance from the given position. The first dictionary only contains protein-coding genes and the second only contains non-protein-coding genes. The minimum value is calculated for both and printed along with the associated gene name. Run with ./day3-lunch-3.py < BDGP6.Ensembl.81.gtf. 
#Output will be "closest protein coding name; distance"
               #"closest non-protein-coding name; distance"

import sys

closest_protein_gene = {}
closest_nonprotein_gene = {}
#Making two empty dictionaries


my_dist = 0


for i, line in enumerate(sys.stdin):
    if i <= 5:
        continue
    #skip metadata
    fields = line.rstrip("\r\n").split("\t")
    read_type = fields[2]
    chrom = fields[0]
    gene_start = int(fields[3])
    gene_end = int(fields[4])
    last_column = fields[8]
    near_gene = line.rstrip("\r\n").split(" ")[1]
    find_pos = int(21378950)
    #defining all the variables I will use later on - note that some must be
    #set to be integers in order to perform math on them
    if read_type == "gene" and chrom == "3R" and "protein_coding" in last_column:
       #first scenario looks at only protein coding genes
        if find_pos < gene_start:
            my_dist = gene_start - find_pos
            closest_protein_gene[near_gene] = my_dist
        elif find_pos > gene_start:
            my_dist = find_pos - gene_end
            closest_protein_gene[near_gene] = my_dist
            #sets my_dist to be absolute value distance from the position provided
    elif read_type == "gene" and chrom == "3R":
        #second scenario looks only at non-protein coding genes
        if find_pos < gene_start:
            my_dist = gene_start - find_pos
            closest_nonprotein_gene[near_gene] = my_dist
        elif find_pos > gene_start:
            my_dist = find_pos - gene_end
            closest_nonprotein_gene[near_gene] = my_dist
            #sets my_dist to be absolute value distance from the position provided
        
min_1 = min(closest_protein_gene, key=closest_protein_gene.get)
print(min_1, closest_protein_gene[min_1])

min_2 = min(closest_nonprotein_gene, key=closest_nonprotein_gene.get)
print(min_2, closest_nonprotein_gene[min_2])

#credit to google and stackoverflow - calculated the min value of each dictionary and printed the min along with the associated gene name
