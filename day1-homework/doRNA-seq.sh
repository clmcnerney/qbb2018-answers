#!/bin/bash

GENOME=~/qbb2018-answers/genomes/BDGP6
ANNOTATED=~/qbb2018-answers/genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915

do
    mkdir $SAMPLE
    cd $SAMPLE
    echo "Running fastqc function"
    fastqc ~/data/rawdata/${SAMPLE}.fastq
    echo "Running hisat function"
    hisat2 -x $GENOME -U ~/data/rawdata/${SAMPLE}.fastq -S ${SAMPLE}_mapping.sam
    echo "Running samtools sort"
    samtools sort -o ${SAMPLE}_mapping.bam ${SAMPLE}_mapping.sam
    echo "Running samtools index"
    samtools index -b ${SAMPLE}_mapping.bam
    echo "Running stringtie function"
    stringtie ${SAMPLE}_mapping.bam -p -e -B -G $ANNOTATED -o ${SAMPLE}.gtf
    cd ../
done
