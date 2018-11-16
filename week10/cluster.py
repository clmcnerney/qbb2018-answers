#!/usr/bin/env python3

"""
Usage: ./cluster.py hema_data.txt

Cluster the data matrix both directions, plot heatmap of gene expression
Recreate differentiation sequence (ie dendrogram)
Use k-means clustering, plot results for CFU and poly using # of k blocks

~microarray paper~
Genes differentially expressed between two earliest stages vs two latest stages
use SciPy stats package - t test for significance in difference in mean expression level
ID gene most upregulated in late diff. stage, use to ID genes w/ similar expression patterns (kmeans output) --> gene ontology analysis using Panther
"""
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_table(sys.argv[1], sep = "\t", header = 0, index_col = 0)
array = df.values
#print(array)

Z = linkage(array.T, 'ward')

fig, ax = plt.subplots()
plt.title("Dendrogram")
plt.xlabel("sample")
plt.ylabel("distance")
dendrogram(
    Z,
    show_leaf_counts=False,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True)

fig.savefig("dendrogram.png")
plt.close(fig)