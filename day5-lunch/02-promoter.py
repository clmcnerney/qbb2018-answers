#!/usr/bin/env python3

"""
Usage: ./02-promoter.py <ctab_file>
Convert ctab to bed format, converts 
-bed: chr start stop name 
"""

import sys

new_start = []
new_end = []
#initialize two empty lists that will contain the start and stop positions of the promoter regions

ctab_file = open(sys.argv[1])

for i, line in enumerate(ctab_file):
    if i == 0:
        continue
        #skip the header line
    fields = line.rstrip("\r\n").split("\t")
    chrom = fields[1]
    start = fields[3]
    end = fields[4]
    t_name = fields[5]
    strand = fields[2]
    #rename variables for convenience
    if "+" in strand:
        if float(start) > 500:
            new_start = int(start) - 500
            new_end = int(start) + 500
        else:
            continue
        #+ strands' promoters will have a promoter region +- 500 bp from the TSS
    elif "-" in strand:
        if float(end) > 500:
            new_start = int(end) + 500
            new_end = int(end) - 500
        else:
            continue
        
        #- strands' promoters will have a promoter region +- 500bp from the TSS as defined in the ctab file
    bed_order = [chrom, str(new_start), str(new_end), fields[5]]
    #smush them together
    print("\t".join(bed_order))
    #print the joined list
    