#!/usr/bin/env python3

"""
./meme_plot.py meme_edit.txt
Produce a plot showing where motif matches occur in the input sequences.
This should be a density plot, where the x-axis is the relative position in the sequences where the motif matches are found, and the y-axis is a representation of how often we see motifs at that position.
"""

import sys
import numpy as np
from statsmodels.stats import weightstats as stests
import matplotlib.pyplot as plt
import math
import pandas as pd

meme_dict = {}

for line in open(sys.argv[1]):
    fields = line.rstrip("\t").split()
    offset = float(fields[2])
    if offset not in meme_dict:
        meme_dict[offset] = 1
    else:
        meme_dict[offset] += 1
        
#print(meme_dict)
#meme_df = pd.DataFrame(meme_dict, index = [offset])
fig, ax = plt.subplots()
for key in meme_dict:
    plt.scatter([key], meme_dict[key])
#ax.scatter(offset, meme_df)
#pd.DataFrame.plot(meme_df[0], meme_df[1])
#plt.scatter(float(offset), float(meme_dict[offset]))
ax.set_xlabel("Relative Offset from Reference")
ax.set_ylabel("Number of Probable Motifs")
ax.set_title("Motif Positions")
fig.savefig("plot.png")
plt.close()

#print(meme_df)