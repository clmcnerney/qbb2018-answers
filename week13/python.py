#!/usr/bin/env python

import sys
import numpy as np
import hifive
import pandas as pd

#import matplotlib.pyplot as plt

hic = hifive.HiC('norm_out.hcp') 

data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')

data[:, :, 1] *= np.sum(data[:, :, 0]) / np.sum(data[:, :, 1])
where = np.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]


ctcf = []

for line in open(sys.argv[1]):
    fields = line.strip("\r\n").split("\t")
    if fields[0] == "chr17":
        if int(fields[1]) >= 15000000:
            if int(fields[2]) <= 17500000:
                midpoint = (int(fields[1]) + int(fields[2]))/2
                ctcf.append(midpoint)
#print ctcf

bins = []

for mdpt in ctcf:
    interval = (mdpt-15000000)/10000
    bins.append(interval)
bins = np.unique(bins)

enrichment_val = []

for i in range(len(bins)):
    for j in range(i, len(bins)):
        enrichment = float(data[bins[i], bins[j]])
        if enrichment >= 1:
            start = (bins[i]*10000 + 15000000)
            end = (bins[j]*10000 + 15000000)
            #enrichment_val.append((bins[i]*10000)+15000000, (bins[j]*10000)+15000000, enrichment)
            enrichment_val.append(start, end, enrichment)

#pd.DataFrame()
print enrichment_val
#for line in data