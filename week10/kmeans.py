#!/usr/bin/env python3

"""
Usage: ./kmeans.py hema_data.txt

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
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans,vq

df=pd.read_table(sys.argv[1], sep = "\t", header = 0, index_col = 0).loc[:, ("CFU", "poly")]
array = df.values
col_names = df.columns.values.tolist()
#print(df)
Z = linkage(array, 'ward')
kmeans = KMeans(n_clusters = 4)
kmeans.fit(Z)
y_means = kmeans.predict(Z)
fig, ax = plt.subplots()
plt.scatter(Z[:, 0], Z[:, 1], c = y_means, s=50, cmap = "viridis")
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c = "black", s=200, alpha = 0.5)
fig.savefig("kmeans.png")
plt.close(fig)



#kmeans = scipy.cluster.vq.kmeans(Z, 2)
#centroids, _ = kmeans(Z, 2)
#idx, _ = vq(Z, centroids)
#plot(data[idx==0,0], data[idx==0,1], "ob",
       # data[idx==1,0],data[idx==1,1], "or")


# fig, ax = plt.subplots(figsize=(8, 6))
# ax.set_title("Heatmap")
# im = ax.pcolor(
#     array2,
#     cmap="RdBu",
#     vmin=-1*m,
#     vmax=m,
#     )
# ax.grid(False)
# ax.set_xticks(
#     np.arange(0.5, array2.shape[1]+0.5),
#     )
# ax.set_xticklabels(
#     idx_cols,
#     rotation=50,
#     )
# ax.set_yticks([])
#
# cbar = fig.colorbar(im, ax=ax)
# fig.subplots_adjust(
#     left = 0.05,
#     bottom = 0.15,
#     right = 1.0,
#     top = 0.95,
# )
#
# fig.savefig("heatmap.png")
# plt.close(fig)
