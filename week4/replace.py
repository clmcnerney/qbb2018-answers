#!/usr/bin/env python3

"""
Usage: ./replace.py BYxRM_PhenoData.txt > phenodata.txt
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta

vcf = open(sys.argv[1])

for line in vcf:
    if line.startswith("\t"):
        print(line.strip())
        continue
    nl = line.replace('_', "\t")
    print(nl.strip())
    