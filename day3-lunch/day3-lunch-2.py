#!/usr/bin/env python3

#Make a dictionary that has a key of type of gene and value equal to the number of instances of each type of gene. Run with ./day3-lunch-2.py < BDGP6.Ensembl.81.gtf

import sys

#set the counter to 0, will add to it when conditions below are met
types_of_genes = {}
#empty dictionary to add to

for i, line in enumerate(sys.stdin):
    #using enumerate gives the lines a numerical value with which to keep track of them 
    if i <= 5:
        continue
    #skip over the first 5 lines, which are the metadata
    fields = line.rstrip("\r\n").split("\t")
    #use this command for just about every iterative script
    read_type = fields[2]
    #use to see if it's a gene
    if read_type == "gene":
        #if the type of read is a gene then these following things will be done
        fields = line.rstrip("\r\n").split()
        #re-designated the fields to be split by whitespace because the last
        #column was a block of text not tab delineated
        gene_type = fields[17]
        #the gene type is within the 17th field if counting by whitespace
        if gene_type in types_of_genes:
            types_of_genes[gene_type] += 1
            #if the gene type has been seen before and exists in the dictionary,
            #increase the count by 1
        else:
            types_of_genes[gene_type] = 1
            #if the gene type has never been seen before,
            #add it to the dictionary and set the count value to 1

for name, value in types_of_genes.items():
    print(name, value)
    
    #prints a list of the names of gene types as the keys and the number of
    #times seen as values
        
