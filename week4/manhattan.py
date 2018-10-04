#!/usr/bin/env python3

"""
Usage: ./manhattan.py /plink_output/
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta
from collections import defaultdict
import math
import os

all_plinks = ["plink.P1.qassoc", "plink.P2.qassoc", "plink.P3.qassoc", "plink.P4.qassoc", "plink.P5.qassoc", "plink.P6.qassoc", "plink.P7.qassoc", "plink.P8.qassoc", "plink.P9.qassoc", "plink.P10.qassoc", "plink.P11.qassoc", "plink.P12.qassoc", "plink.P13.qassoc", "plink.P14.qassoc", "plink.P15.qassoc", "plink.P16.qassoc", "plink.P17.qassoc", "plink.P18.qassoc", "plink.P19.qassoc", "plink.P20.qassoc", "plink.P21.qassoc", "plink.P22.qassoc", "plink.P23.qassoc", "plink.P24.qassoc", "plink.P25.qassoc", "plink.P26.qassoc", "plink.P27.qassoc", "plink.P28.qassoc", "plink.P29.qassoc", "plink.P30.qassoc", "plink.P31.qassoc", "plink.P32.qassoc", "plink.P33.qassoc", "plink.P34.qassoc", "plink.P35.qassoc", "plink.P36.qassoc", "plink.P37.qassoc", "plink.P38.qassoc", "plink.P39.qassoc", "plink.P40.qassoc", "plink.P41.qassoc", "plink.P42.qassoc", "plink.P43.qassoc", "plink.P44.qassoc", "plink.P45.qassoc", "plink.P46.qassoc"]



#f = open(sys.argv[1])   

def whatisafunction(filename):
    #psn_list = []
    #pval_list = []
    sig_psn = []
    sig_pval = []
    insig_psn = []
    insig_pval = []
    threshold_val = 0.00001
    file_number = 0
    for line in open(filename):
        if "NA" in line or "BETA" in line:
            continue
        else:
            fields = line.rstrip("\r\n").split()
            file_number += 1
            #chr = fields[0]
            psn = float(fields[2])
            pval = float(fields[8])
            pval2 = -(math.log(pval, 10))
            if pval < threshold_val:
                sig_psn.append(psn)
                sig_pval.append(pval2)
            elif pval > threshold_val:
                insig_psn.append(psn)
                insig_pval.append(pval2)  
    return sig_psn, sig_pval, insig_psn, insig_pval, file_number       

def graphfxn(sig_psn, sig_pval, insig_psn, insig_pval, file_number):
    fig, ax = plt.subplots()
    plt.scatter(sig_psn, sig_pval, color = "maroon", alpha = 0.9, label = "significant")
    plt.scatter(insig_psn, insig_pval, color = "grey", alpha = 0.5, label = "insignificant")
    ax.set_xlabel("SNP position")
    ax.set_ylabel("-log10(p-value)")
    fig.savefig(str(all_plinks[p]) + ".png")
    plt.close()


for p in range(len(all_plinks)):
    the_path = "./plink_output/" + all_plinks[p]
    print(the_path)
    
    sig_psn, sig_pval, insig_psn, insig_pval, file_number = whatisafunction(the_path)
    graphfxn(sig_psn, sig_pval, insig_psn, insig_pval, file_number)
#print(len(psn_list))
#print(len(pval_list))
#print(val)
    #fig.savefig("manhattan_{}.png".format(treatment))=