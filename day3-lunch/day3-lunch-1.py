#!/usr/bin/env python3

#Determine the number of protein coding genes that flies have. Run with ./day3-lunch-1.py < BDGP6.Ensembl.81.gtf

import sys

protein_genes_count = 0
#set the counter to 0, will add to it when conditions below are met

for i, line in enumerate(sys.stdin):
    #using enumerate gives the lines a numerical value with which to keep track of them 
    if i <= 5:
        continue
    #skip over the first 5 lines, which are the metadata
    fields = line.rstrip("\r\n").split("\t")
    #use this command for just about every iterative script
    read_type = fields[2]
    #use to see if it's a gene
    last_column = fields[8]
    #contains lots of extra information, including what type of gene is listed
    if read_type == "gene" and "protein_coding" in last_column:
        protein_genes_count += 1
        #if both conditions are true, add 1 value to the counter
print("Number of protein coding genes in flies is " + str(protein_genes_count))