#!/usr/bin/env python3

"""
Usage: ./combine.py <samples.csv> <ctab_dire>
Make a new ctab file that contains the transcript name and corresponding FPKM values for all 16 samples
"""

import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(sys.argv[1])

#soi = df.loc[:, "sex"] == "female"
#df = df.loc[soi, :]

compiled = {}

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col = "t_name")
    compiled[sex + stage] = ctab_df.loc[:, "FPKM"]

dfcompiled = pd.DataFrame(compiled)

dfcompiled.to_csv(sys.stdout)

print(dfcompiled)
