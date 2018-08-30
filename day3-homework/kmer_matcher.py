#!/usr/bin/env python3

"""
Prints the target sequence name and start position, query start position, and the kmer matched
"""

import sys
import fasta

reader1 = fasta.FASTAReader(sys.stdin)
#read the subset.fa target file
reader2 = fasta.FASTAReader(open(sys.argv[1]))
#read the droYak2_seq.fa query file
k = int(sys.argv[2])

query_kmers = {}

for ident, sequence in reader2:
    for posn, v in enumerate(range(0, len(sequence) - k)):
        kmer = sequence[posn:posn+k]
        query_kmers[posn] = kmer
        if kmer not in query_kmers:
            query_kmers[kmer] = [posn]
        else:
            query_kmers[kmer].append(posn)

for ident, sequence in reader1:
    for i, value in enumerate(range(0, len(sequence) - k)):
        target_kmer = sequence[i:i+k]
        if target_kmer in query_kmers:
            print(ident, i, query_kmers[target_kmer], target_kmer)