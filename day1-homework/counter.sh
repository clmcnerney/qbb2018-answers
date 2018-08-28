#!/bin/bash

grep -v "^@" /Users/cmdb/qbb2018-answers/day1-homework/SRR072893/SRR072893_mapping.sam | grep -v 211100000 /Users/cmdb/qbb2018-answers/day1-homework/SRR072893/SRR072893_mapping.sam | cut -f 3 | sort | uniq -c > counts_per_chrom_SRR072893.sam
