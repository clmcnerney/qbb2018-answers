#!/usr/bin/env python3

"""
Usage: ./genescript.py <samples.csv> <directory> <sex> <gene_name> 
Given the gene name and sex, generate a scatter plot of the average FPKM values by transcript
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(sys.argv[1])
dictionary = {}
for i in range(0, len(sys.argv)):
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        roi = ctab_df.loc[:, "gene_name"] == sys.argv[i]
        dictionary = ctab_df.loc[roi, "FPKM"]
        dictionary_df = pd.DataFrame(dictionary)
    avg = dictionary_df.mean(axis = 1)
    #axis 1 changes the averaging to be from going across the rows to going down the columns

    fig, ax = plt.subplots()
    ax.scatter(list(dictionary_df.index), list(avg))
    fig.suptitle(str(sys.argv[i]))
    plt.xticks(rotation=90)
    ax.set_xlabel("transcript")
    ax.set_ylabel("average FPKM")
    fig.savefig(str(sys.argv[i]) + ".png")
    plt.close(fig)