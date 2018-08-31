#!/usr/bin/env python3

"""
Usage: ./03-timecourse.py <t_name> <samples.csv> <directory> <sex>
Create a timecourse of a given transcript (FBtr0331261) for females 
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(sys.argv[2])

def timecourse(sex):
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == sex
    df = df.loc[soi, :]
    fpkms = []
    stages = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col = "t_name")
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages.append(stage)
    return fpkms, stages

fpkms_f, stages = timecourse("female")
fpkms_m, stages = timecourse("male")
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

fig.savefig("timecourse.png")
plt.close(fig)