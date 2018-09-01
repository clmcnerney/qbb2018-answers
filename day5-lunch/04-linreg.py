#!/usr/bin/env python3

"""
Usage: ./04-linreg.py  <5x .bw files> <.ctab> etc
Do OLS fitting over all 5 histone markers
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
#add in a column at the end for the FPKMs 
compiled_means = {hist1 : mean1, hist2 : mean2, hist3 : mean3, hist4 : mean4, hist5 : mean5, fpkms_name : fpkm}
#manually compile the dictionary - it would be cleaner to have some sort of for loop or function here, which we started to work on, but it was more trouble than it was worth
compiled_means_df = pd.DataFrame(compiled_means)
#converted the compiled_means dictionary to a dataframe to be able to then drop data

compiled_means_df = compiled_means_df.dropna()
#because we skipped over transcripts whose promoter regions were at the ends of the chromosomes, we had to account for those blanks in the dataframe. We accomplished this by dropping the empty data. A better method would have been to change how we designated the promoter locations to account for this

y = compiled_means_df.loc[:,fpkms_name]
#set the y component of the model to be the fpkms_name column of the data frame
X = compiled_means_df.loc[:,[hist1,hist2,hist3,hist4,hist5,]]
#set the X value to be everything else (ie all of the histone names)
X = sm.add_constant(X)

model = sm.OLS(y, X)
# model = sm.OLS(y, X)
# print(model)
results = model.fit()
print(results.summary())