#!/usr/bin/env python3

"""
Usage: ./allele_freq.py BYxRM_segs_saccer3.bam.simplified.vcf
allele frequency spectrum of identified variants
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta


annotated = open(sys.argv[1])

all_freq = []
blank_freq = []

for i in annotated:
    if i.startswith("#"):
        pass
    else:
        fields = i.rstrip("\r\n").split("\t")
        info = fields[7]
        allele = info.split(";")[0][3:]
        if "AF" in allele:
            if allele not in blank_freq:
                blank_freq[float(allele)] = 1
                all_freq.append(float(allele))
            else:
                blank_freq[float(allele)] += 1
                all_freq.append(float(allele))
        #all_freq.append(float(blank_freq))
        else:    
            if "," in allele:
                allele_spl = allele.split(",")
                all_freq.append(float(allele_spl[0]))
                all_freq.append(float(allele_spl[1]))
            else:
                all_freq.append(float(allele))
print(all_freq)      

fig, ax = plt.subplots()
plt.hist(all_freq, bins = 1000)
#ax.set_xlim(left = 0, right = 20)
#ax.set_ylim(0, 15000)

plt.xlabel("Allele Frequency")
plt.ylabel("Counts")
plt.title("Allele Frequency Across Variants")
plt.savefig("allelefreq.png")
plt.close()
