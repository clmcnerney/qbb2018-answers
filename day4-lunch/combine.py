#!/usr/bin/env python3

"""
Usage: ./combine.py <threshold value> <sample1/t_data.ctab> <sample2/t_data.ctab> etc
"""

import sys
import os
import pandas as pd

fpkms = {}

for i in range(2, len(sys.argv)):
    #go through each file present in local directory
    name = sys.argv[i].split(os.sep)[-2]
    fpkm = pd.read_csv(sys.argv[i], sep = "\t", index_col = "t_name").loc[:, "FPKM"]
    fpkms[name] = fpkm
    #builds dictionary of names of samples (from the file name) and the fpkm values pulled from each (as well as the transcript name, taking the place of the index)

fpkms_df = pd.DataFrame(fpkms)
#take the dictionary and convert it to a dataframe

fpkms_sum = pd.DataFrame.sum(fpkms_df, 1)
#sum the entries in the data frame (0 to sum down the column, 1 to sum across the rows)

roi_fpkm = fpkms_sum > float(sys.argv[1])
#this filters it - only the sum values that are greater than the inputted threshold value will be added to roi_fpkm

fpkms_df.loc[roi_fpkm, :].to_csv(sys.stdout, sep = "\t", index = True)
#filter the fpkms_df with the roi_fpkm and output the transcript IDs and FPKMs for each sample 