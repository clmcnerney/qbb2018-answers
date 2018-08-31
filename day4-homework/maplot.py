#!/usr/bin/env python3

"""
Usage: ./maplot.py <ctab_file> 
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")
df2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name")

fpkm1 = df1.loc[:, "FPKM"]
fpkm2 = df2.loc[:, "FPKM"]

name1 = sys.argv[1].split(os.sep)[-2]
name2 = sys.argv[2].split(os.sep)[-2]

#fpkm1_log = np.log2(fpkm1 + 1)
#fpkm2_log = np.log2(fpkm2 + 1)

ratio =  np.log2( (fpkm2 + 1)  / (fpkm1 + 1)   )
avg = (np.log2(fpkm1 + 1) + np.log2(fpkm2 + 1)) / 2
#determine the two paramaters we will be graphing below


fig, ax = plt.subplots()
ax.scatter(avg, ratio, alpha = 0.3)

ax.set_title("MA Plot of FPKM Values: %s vs %s" %(name1, name2))
#ax.set_xscale('log')
#ax.set_xlim(0, 10)
#ax.set_ylim(-2, 30)
#ax.set_yscale('log')
ax.set_xlabel("Average FPKM Abundance Value of %s and %s" %(name1, name2))
ax.set_ylabel("Ratio of FPKM Values %s / %s" %(name2, name1))
fig.savefig("maplot.png")
plt.close(fig)

