#!/usr/bin/env python3

"""
Usage: ./timecourse2.py <t_name> <samples.csv> <directory> <replicates.csv>
Create a timecourse of a given transcript (FBtr0331261) for a given sex 
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_csv(sys.argv[2])
#open the file.csv and read it
def timecourse(sex, file):
    #make a function to be able to generalize the commands with input from the command line
    df = pd.read_csv(file)
    soi = df.loc[:, "sex"] == sex
    #filtering based on the user's choice of sex
    df = df.loc[soi, :]
    #apply the filter to the full dataframe
    if file == sys.argv[2]:
        fpkms = []
        #if the file is samples.csv then proceed as the last script did
    elif file == sys.argv[4]:
        fpkms = [None, None, None, None]
        #if the file is replicates.csv, then add four empty entries to account for skipping the first four life stages
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        #add the FPKMs to a list, indexed by t name
    return fpkms

fpkms_f1 = timecourse("female", "samples.csv")
fpkms_m1 = timecourse("male", "samples.csv")
fpkms_f2 = timecourse("female", "replicates.csv")
fpkms_m2 = timecourse("male", "replicates.csv")
#run the function with input as female and then again with the input as male


fig, ax = plt.subplots()
ax.plot(fpkms_f1, color = "red", label = "female1")
ax.plot(fpkms_m1, color = "blue", label = "male1")
ax.plot(fpkms_f2, color = "red", label = "female2")
ax.plot(fpkms_m2, color = "blue", label = "male2")
fig.suptitle(sys.argv[1])	
plt.xticks(rotation=90)
plt.xticks(np.arange(8), ("10", "11", "12", "13", "14a", "14b", "14c", "14d"))
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance (RPKM)")	
plt.tight_layout()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc = "center left", bbox_to_anchor=(1, 0.5), frameon = False)
#all of this for the figure legend
fig.savefig("timecourse2.png")
plt.close(fig)