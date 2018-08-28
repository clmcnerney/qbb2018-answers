#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else:
    f = sys.stdin
#just open file of interest with standard argument, first part is unnecessary   
for line in f:
    if "DROME" in line:
        #drome refers to correct species
        fields = line.rstrip("\r\n").split()
        #whitespace deliniation
        if fields[-1].startswith("FBgn"):
            #look at the last column, they have to start with the FBgn to be counted in the printed dataset
            print(fields[3] + "    " + fields[2])
            #prints two columns, first has flybase ID and second has uniprot ID