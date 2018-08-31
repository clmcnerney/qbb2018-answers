#!/usr/bin/env python3

"""
Usage: ./genescript.py <gene name> <samples.csv> <directory> 
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(sys.argv[2])
dictionary = {}
for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col = "t_name")
    roi = ctab_df.loc[:, "gene_name"] == sys.argv[1]
    dictionary = ctab_df.loc[roi, "FPKM"]
    dictionary_df = pd.DataFrame(dictionary)

avg = dictionary_df.mean(axis = 1)
fig, ax = plt.subplots()
ax.plot(list(dictionary_df.index), list(avg))
fig.suptitle("Sxl")	
ax.set_xlabel("gene")
ax.set_ylabel("average FPKM")	
fig.savefig("grahp2.png")
plt.close(fig)