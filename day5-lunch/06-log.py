#!/usr/bin/env python3

"""
Usage: ./06-log.py  <sample1/t_data.ctab> <sample2/t_data.ctab> etc
Transform response variable gene expression into units of log(FPKM + 1)
"""

import sys
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

compiled_means = {}

hist1 = sys.argv[1].split(os.sep)[-1]
mean1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = 0).iloc[:,4]
hist2 = sys.argv[2].split(os.sep)[-1]
mean2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = 0).iloc[:,4]
hist3 = sys.argv[3].split(os.sep)[-1]
mean3 = pd.read_csv(sys.argv[3], sep = "\t", index_col = 0).iloc[:,4]
hist4 = sys.argv[4].split(os.sep)[-1]
mean4 = pd.read_csv(sys.argv[4], sep = "\t", index_col = 0).iloc[:,4]
hist5 = sys.argv[5].split(os.sep)[-1]
mean5 = pd.read_csv(sys.argv[5], sep = "\t", index_col = 0).iloc[:,4]
#connect histone name to the mean value
fpkms_name = sys.argv[6].split(os.sep)[-1]
fpkm = pd.read_csv(sys.argv[6], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
fpkm = np.log(fpkm + 1)
#this is the only new aspect to this code, taking the original FPKMs, adding one and then log transforming them, overwriting the original FPKM values in the process

compiled_means = {hist1 : mean1, hist2 : mean2, hist3 : mean3, hist4 : mean4, hist5 : mean5, fpkms_name : fpkm}
compiled_means_df = pd.DataFrame(compiled_means)
compiled_means_df = compiled_means_df.dropna()

#print(compiled_means_df)

y = compiled_means_df.loc[:,fpkms_name]
X = compiled_means_df.loc[:,[hist1,hist2,hist3,hist4,hist5,]]
X = sm.add_constant(X)

model = sm.OLS(y, X)
# model = sm.OLS(y, X)
# print(model)
results = model.fit()
print(results.summary())

#The R^2 value does improve upon log transforming the data