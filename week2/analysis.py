#!/usr/bin/env python3

"""./analysis.py 
compute the number of contigs, minimum/maximum/average contig length, and N50.
"""

import sys
import fasta
import numpy as np

reader = fasta.FASTAReader(open(sys.argv[1]))

 

idents = []

for ident, sequence in reader:
    idents.append(ident)
    
# print(idents)

   
# line = sys.stdin.readline()
length_contigs = []

for i in range(len(idents)):
    #fields = idents[i].split("_")
    num_nodes = idents[-1].split("_")[1]
    length_contigs.append(float(idents[i].split("_")[3]))

max_length = np.max(length_contigs)
min_length = np.min(length_contigs)
avg_length = np.mean(length_contigs)
print("Number of contigs is: " + str(num_nodes))
print("Max contig length is: " + str(max_length))
print("Min contig length is: " + str(min_length))
print("Avg contig length is: " + str(avg_length))

sorted_length_list = sorted(length_contigs)
sum = 0
#halfway = sorted_length_list[int(len(sorted_length_list)/2)]
halfway = np.sum(sorted_length_list)/2

#print(halfway)
for j in range(len(sorted_length_list)):
    if sum < halfway:
        sum += sorted_length_list[j]
    elif sum > halfway:
        print("N50 value is: " + str(sorted_length_list[j]))
        break
    

#print(sorted_length_list)


#print(num_nodes)
# print(length_contigs)

