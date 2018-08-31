#!/usr/bin/env python3

"""
Usage: ./genescript.py <gene_name> <samples.csv> <directory> <sex>
Given the gene name and sex, generate a scatter plot of the average FPKM values by transcript
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(sys.argv[2])
#open samples.csv
dictionary = {}
for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col = "t_name")
    roi = ctab_df.loc[:, "gene_name"] == sys.argv[1]
    dictionary = ctab_df.loc[roi, "FPKM"]
    dictionary_df = pd.DataFrame(dictionary)
avg = dictionary_df.mean(axis = 1)
#axis 1 changes the averaging to be from going across the rows to going down the columns
#this builds a dataframe from a dictionary containing the ctab_df filtered by the gene name, containing an average of the FPKMs

fig, ax = plt.subplots()
ax.scatter(list(dictionary_df.index), list(avg))
fig.suptitle(sys.argv[1])
plt.xticks(rotation=90)
ax.set_xlabel("transcript")
ax.set_ylabel("average FPKM")
fig.savefig("gene.png")
plt.close(fig)