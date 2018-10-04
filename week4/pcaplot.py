#!/usr/bin/env python3

"""
Usage: ./pcaplot.py plink.eigenvec
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta


eigenvec = open(sys.argv[1])

pca_1 = []
pca_2 = []

for line in eigenvec:
    fields = line.rstrip("\r\n").split(" ")
    pca_1_vals = fields[2]
    pca_2_vals = fields[3]
    pca_1.append(float(pca_1_vals))
    pca_2.append(float(pca_2_vals))
    
#print(pca_1)
#print(pca_2)

fig, ax = plt.subplots()
ax.scatter(pca_1, pca_2)
fig.suptitle("PCA Analysis of Yeast Data")
#plt.xticks(rotation=90)
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
fig.savefig("pca.png")
plt.close(fig)