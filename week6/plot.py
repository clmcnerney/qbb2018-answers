#!/usr/bin/env python3

"""
./plot.py combined.bed sortedmousegenome.bed genomecompare.bed
Produce a two panel plot containing two bar plots. The right panel should plot the number of sites lost and gained between the two cell types. The left panel should plot the number of sites in each type of region (exon, intron…) for each cell type.

cell types | mousegenome
"""

import sys
import numpy as np
from statsmodels.stats import weightstats as stests
import matplotlib.pyplot as plt
import math
import pandas as pd

gained = []
lost = []

for line in open(sys.argv[1]):
    fields = line.rstrip("\t").split()
    if fields[5] == "1" and fields[6] == "0":
        gained += str(1)
        #gained += fields[5]
    elif fields[5] == "0" and fields[6] == "1":
        lost += str(1)
        #lost += fields[6]
    else:
        continue
#print(len(gained))
#print(len(lost))
objects = ("Sites Gained", "Sites Lost")
y_pos = np.arange(len(objects))
values = (len(gained), len(lost))


"""this is now the left panel of the figure
i'll need to take the information from sortedmousegenomebed (fields4) and use that as the key against which i can compare the positions from the genome compare"""
category = {}

for line in open(sys.argv[2]):
    fields = line.rstrip("\t").split()
    begin_type = int(fields[1])
    #print(begin_type)
    end_type = int(fields[2])
    #print(end_type)
    type = fields[3]
    #print(type)
    for bases in range(begin_type, end_type):
    	category[bases] = type
#print(category)

mutation_cat = []

for i, line in enumerate(open(sys.argv[3])):
	fields = line.rstrip("\t").split()
	mut_start = int(fields[1])
	mut_end = int(fields[2])
	for bases in range(mut_start, mut_end):
		if bases in category:
			mutation_cat.append(category[bases])
#print(mutation_cat)
introns = []
exons = []
promoters = []

for cat in mutation_cat:
	if cat == "intron":
		introns += str(1)
	elif cat == "exon":
		exons += str(1)
	elif cat == "promoter":
		promoters += str(1)
# print(len(introns))
# print(len(exons))
# print(len(promoters))

objects2 = ("Introns", "Exons", "Promoters")
y_pos2 = np.arange(len(objects2))
values2 = (len(introns), len(exons), len(promoters))





fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (20, 10))
# fig, ax = plt.subplots(figsize = (4, 7))
ax1.bar(y_pos, values, width = 0.4, color = ["maroon", "lightcoral"])
ax1.set_xticklabels(objects)
ax1.set_xticks(y_pos)
ax1.set_xlabel("Gained vs Lost")
ax1.set_ylabel("Counts")
ax1.set_title("Number of Sites Lost and Gained")

#ax2.bar(range(len(mutation_cat)), list(mutation_cat.keys()))
ax2.bar(y_pos2, values2, width = 0.4, color = ["violet", "rebeccapurple", "slateblue"])
ax2.set_xticklabels(objects2)
ax2.set_xticks(y_pos2)
ax2.set_xlabel("Type of Mutation")
ax2.set_ylabel("Number")
ax2.set_title("Number of Types of Mutations")
fig.savefig("entireplot.png")
plt.close()


