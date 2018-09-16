#!/usr/bin/env python3


"""./plotcontigs.py <lastzoutputfile>
lastz reference.fasta ~/qbb2018-answers/week2/directory/contigs.fa[nameparse=tag:NODE_] 
--chain --format=general-:name1,start1,end1,name2,start2,end2,strand2 > lastz_velvet.txt
sort -k 4n lastz_velvet.txt > sorted_velvet.txt


"""


import sys
import fasta
import numpy as np
from statsmodels.stats import weightstats as stests
import matplotlib.pyplot as plt
import math
import pandas as pd

# ref_start = pd.read_csv(sys.argv[1], sep = "\t", index_col = "name1").loc[:, "start1"]
# ref_end = pd.read_csv(sys.argv[1], sep = "\t", index_col = "name1").loc[:, "end1"]
# contig_start = pd.read_csv(sys.argv[1], sep = "\t", index_col = "name2").loc[:, "start2"]
# contig_end = pd.read_csv(sys.argv[1], sep = "\t", index_col = "name2").loc[:, "end2"]
#contig_strand = pd.read_csv(sys.argv[1], sep = "\t", index_col = "name2").loc[:"strand2"]

# mapping = {ref_start : ref_end,
#            contig_start : contig_end}
#
# mapping_df = pd.DataFrame(mapping)
# mapping_df.to_csv(sys.stdout)


#reader = fasta.FASTAReader(open(sys.argv[1]))



position = 0

fig, ax = plt.subplots()

for i in open(sys.argv[1]):
    fields = i.split("\t")
    ref_ident = fields[0]
    ref_start = fields[1]
    ref_end = fields[2]
    contig_ident = fields[3]
    contig_start = fields[4]
    contig_end = fields[5]
    contig_strand = fields[6]
    contig_length = int(contig_end) - int(contig_start)
    plt.plot([int(ref_start), int(ref_end)], [position, position + int(contig_length)])
    #plt.plot([int(ref_start), position], [int(ref_end), position + int(contig_length)])
    position += contig_length
    #elif contig_strand == "-":
        #plt.plot([int(ref_start), int(ref_end)], [-position, position +     int(contig_length)])
       

plt.xlabel("position in reference")
plt.ylabel("contigs")
plt.tight_layout()
plt.xlim(0, 100000)
plt.ylim(0, 120000)
fig.savefig("velvet2.png")
plt.close(fig)


