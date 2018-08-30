#!/usr/bin/env python3

"""
Usage: ./plotting.py <ctab_file> 
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

# transform the data rather than the axes
fpkm1_log = np.log(fpkm1 + 1)
fpkm2_log = np.log(fpkm2 + 1)

fitting = np.polyfit(fpkm1, fpkm2, 1)
print(fitting)

x = np.linspace(min(fpkm1_log), max(fpkm2_log))
fit = np.poly1d(fitting)


fig, ax = plt.subplots()
ax.scatter(fpkm1_log, fpkm2_log, alpha = 0.3)
plt.plot(x, fit(x), "r")
ax.set_title("Comparison of FPKM Values: %s vs %s" %(name1, name2))
#ax.set_xscale('log')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
#ax.set_yscale('log')
ax.set_xlabel("log FPKM Value of %s" %name1)
ax.set_ylabel("log FPKM Value %s" %name2)
ax.text(7, 1, "Best fit line: " + str(fit))
fig.savefig("fpkmplot.png")
plt.close(fig)

