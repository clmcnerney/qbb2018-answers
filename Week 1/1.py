#!/usr/bin/env python3


"""./1.py blastresult.fa maffta.fa"""


import sys
import fasta
import numpy as np
from statsmodels.stats import weightstats as stests
import matplotlib.pyplot as plt
import math

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))

nuc_list = []
master_aa_list = []

for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    new_dna = []
    new_aa = []
    j=0
    for i in range(len(aa)):
        a = aa[i]
        nuc = dna[j:j+3]
        if a == "-":
            new_dna.append("---")
            new_aa.append(a)
        else:
            new_dna.append(nuc)
            j+=3
            new_aa.append(a)
    
    nuc_list.append(new_dna)
    master_aa_list.append(new_aa)
    
#print(master_aa_list)
query_aa_list = master_aa_list[0]
query_nuc_list = nuc_list[0]

dN = [0] * len(query_aa_list)
dS = [0] * len(query_aa_list)

for i in range(1, len(master_aa_list[1:])):
    #i will be for each alignment
    #j will be each position within the alignment
    master_aa_nuc_posn = master_aa_list[i]
    nuc_list_posn = nuc_list[i]
    #query_aa_nuc_posn = query_aa_nuc_posn[i]
    for j in (range(len(master_aa_nuc_posn))):
        if master_aa_nuc_posn[j] != query_aa_list[j]:
            dN[j] += 1
        #elif master_aa_list[j] == query_aa_list[j]:
        else:
            if nuc_list_posn[j] != query_nuc_list[j]:
                dS[j] += 1
            else:
                dN[j] += 1

# def dsSum(numlist):
#     tot = 0
#     for i in dS:
#         tot = tot + i
#     return tot
# print(dsSum(dS))

        
#print(dS)
#print(dN)
ratio = []
for i in range(len(dS)):
    dNdS = float(dN[i]) / (dS[i] + 1)
    ratio.append(dNdS)
#print(ratio)

# ztest_list = []
#
# for i in range(0, len(dNdS[0])):
#     ztest = stests.ztest(dS, dN)
#     ztest_list.append(ztest)
#
# print(ztest_list)
var_dS = []

for i in range(len(dS)):
    var1 = np.var(dS) 
    var_dS.append(var1)

var_dN = []

for i in range(len(dN)):
    var2 = np.var(dN)
    var_dN.append(var2)

ztest_list = []

for i in range(len(var_dS)):
    diff = (dN[i] - dS[i])
    var_tot = var_dS
    denominator = math.sqrt(var_dS[i] + var_dN[i])
    ztest = diff / denominator
    ztest_list.append(ztest)
    
    
#print(ztest_list)


fig, ax = plt.subplots()
plt.scatter(range(0, len(ratio)), ratio, s=2)
ax.set_ylabel("dN/dS")
ax.set_xlabel("Codons")
ax.set_title("Selective Strength per Codon Position")
plt.tight_layout()
fig.savefig("codons.png")
plt.close(fig)

fig, ax = plt.subplots()
plt.scatter(range(0, len(ratio)), ztest_list, s=2)
ax.set_ylabel("Z value")
ax.set_xlabel("Codon Position")
ax.set_title("Statistical Significance of dN/dS per Codon Position")
plt.tight_layout()
fig.savefig("zscores.png")
plt.close(fig)

