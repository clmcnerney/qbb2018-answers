#!/usr/bin/env python3

"""
Usage: ./heatmap.py hema_data.txt

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
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list, optimal_leaf_ordering
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')


df=pd.read_table(sys.argv[1], sep = "\t", header = 0, index_col = 0)
array = df.values
col_names = df.columns.values.tolist()

Z = linkage(array, 'ward')


Zalt = linkage(array.T, 'ward')


idx_rows = leaves_list(Z)
data = array[idx_rows, :]
idx_cols = leaves_list(Zalt)
data = data[:, idx_cols]

array2 = (data-np.average(data,axis=0))/np.std(data,axis=0)
m = np.max(np.abs(array2))

fig, ax = plt.subplots(figsize=(8, 6))      
ax.set_title("Heatmap") 
im = ax.pcolor(                           
	array2,                                       
	cmap="RdBu",                          
	vmin=-1*m,                             
	vmax=m,                               
	)
ax.grid(False)                    
ax.set_xticks(                    
	np.arange(0.5, array2.shape[1]+0.5), 
	)
ax.set_xticklabels(                 
	idx_cols,                        
	rotation=50,                   
	)
ax.set_yticks([])                  

cbar = fig.colorbar(im, ax=ax)      
fig.subplots_adjust( 
    left = 0.05,
    bottom = 0.15,
    right = 1.0,
    top = 0.95,
)

fig.savefig("heatmap.png")
plt.close(fig)
