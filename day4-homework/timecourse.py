#!/usr/bin/env python3

"""
Usage: ./timecourse.py <t_name> <samples.csv> <directory> <sex>
Create a timecourse of a given transcript for a given sex 
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(sys.argv[2])
#open the samples.csv and read it
def timecourse(sex):
    #make a function to be able to generalize the commands with input from the command line
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == sex
    #filtering based on the user's choice of sex
    df = df.loc[soi, :]
    #apply the filter to the full dataframe
    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        #add the FPKMs to a list, indexed by t name
    return fpkms

fpkms_f = timecourse("female")
fpkms_m = timecourse("male")
#run the function with input as female and then again with the input as male

fig, ax = plt.subplots()
ax.plot(fpkms_f, color = "red", label = "female")
ax.plot(fpkms_m, color = "blue", label = "male")
fig.suptitle("Sxl")	
plt.xticks(rotation=90)
#plt.xticks(np.arange(8), ("10", "11", "12", "13", "14a", "14b", "14c", "14d"))

ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")	
plt.tight_layout()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc = "center left", bbox_to_anchor=(1, 0.5), frameon = False)
#all of this for the figure legend
fig.savefig("timecourse.png")
plt.close(fig)