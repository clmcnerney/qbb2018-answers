#!/usr/bin/env python3

"""
Usage: ./depthplot.py ann_calls.vcf snpEff_genes.txt

Plot read depth distribution across each called variant
genotype quality distribution
allele frequency spectrum of identified variants
summary of predicted effect of each variant as determined by snpEff (barplot?)

"""

"""sorry Peter"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta


annotated = open(sys.argv[1])

read_depth = []


for i in annotated:
    if i.startswith("#"):
        pass
    else:
        fields = i.rstrip("\r\n").split("\t")
        info = fields[7]
        depth = info.split(";")[7].lstrip("DP=")
        if "," in depth:
            depth2 = depth.split(",")
            read_depth.append(float(depth2[0]))
            read_depth.append(float(depth2[1]))
            #for item in depth2: 
                #read_depth.append(list(map(float, depth.split(","))))
        else:
            read_depth.append(float(depth))

#print(read_depth)      

# fig, ax = plt.subplots()
# plt.hist(read_depth, bins=1000)
# #plt.axis([0, 20, 0, 100000])
# ax.set_xlim(left = 0, right = 140)
# #ax.set_ylim(0, 1000)
#
# plt.xlabel("Read Depth")
# plt.ylabel("Counts")
# plt.title("Read Depth Across Variants")
# plt.savefig("readdepth.png")
# plt.close()

""""""

annotated = open(sys.argv[1])

all_quality = []

for i in annotated:
    if i.startswith("#"):
        pass
    else:
        fields = i.rstrip("\r\n").split("\t")
        quals = "".join(fields[5])
        all_quality.append(float(quals))
    
# #print(all_quality)
#     #cat = fields[7].split(;)[].lstrip()
# fig, ax = plt.subplots()
# plt.hist(all_quality, bins=1000)
# #plt.axis([0, 20, 0, 100000])
# ax.set_xlim(left = 0, right = 2500)
# #ax.set_ylim(0, 1000)
#
# plt.xlabel("Genome Quality")
# plt.ylabel("Counts")
# plt.title("Genome Quality Across Variants")
# plt.savefig("genqual.png")
# plt.close()

""""""

annotated = open(sys.argv[1])

all_freq = []
blank_freq = []

for i in annotated:
    if i.startswith("#"):
        pass
    else:
        fields = i.rstrip("\r\n").split("\t")
        info = fields[7]
        allele = info.split(";")[4][3:]
        if "AN" in allele:
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
#print(all_freq)      

# fig, ax = plt.subplots()
# plt.hist(all_freq,rwidth=.75)
# ax.set_xlim(left = 0, right = 20)
# #ax.set_ylim(0, 15000)
#
# plt.xlabel("Allele Frequency")
# plt.ylabel("Counts")
# plt.title("Allele Frequency Across Variants")
# plt.savefig("allelefreq.png")
# plt.close()

""""""

conservative_inframe_deletion = []
conservative_inframe_insertion = []
disruptive_inframe_deletion = []
disruptive_inframe_insertion = []
downstream_gene_variant = []
frameshift = []
initiator_codon_variant = []
intron = []
missense = []
noncoding_transcript_exon = []
splice_deceptor = []
splice_donor = []
splice_region = []
start_lost = []
stop_gained = []
stop_lost = []
stop_retained = []
synonymous = []
upstream_gene_variant = []

conservative_inframe_deletion = 0
conservative_inframe_insertion = 0
disruptive_inframe_deletion = 0
disruptive_inframe_insertion = 0
downstream_gene_variant = 0
frameshift = 0
initiator_codon_variant = 0
intron = 0
missense = 0
noncoding_transcript_exon = 0
splice_deceptor = 0
splice_donor = 0
splice_region = 0
start_lost = 0
stop_gained = 0
stop_lost = 0
stop_retained = 0
synonymous = 0
upstream_gene_variant = 0


for line in open(sys.argv[2]):
    fields = line.rstrip('\r\n').split('\t')
    if line.startswith("#"):
        pass
    else:
        conservative_inframe_deletion += int(fields[8])
        conservative_inframe_insertion += int(fields[9])
        disruptive_inframe_deletion += int(fields[10])
        disruptive_inframe_insertion += int(fields[11])
        downstream_gene_variant += int(fields[12])
        frameshift += int(fields[13])
        initiator_codon_variant += int(fields[14])
        intron += int(fields[15])
        missense += int(fields[16])
        noncoding_transcript_exon += int(fields[17])
        splice_deceptor += int(fields[18])
        splice_donor += int(fields[19])
        splice_region += int(fields[20])
        start_lost += int(fields[21])
        stop_gained += int(fields[22])
        stop_lost += int(fields[23])
        stop_retained += int(fields[24])
        synonymous += int(fields[25])
        upstream_gene_variant += int(fields[26])
#print(conservative_inframe_deletion)
labels = ["conservative_inframe_deletion", "conservative_inframe_insertion", "disruptive_inframe_deletion", "disruptive_inframe_insertion", "dowstream_gene_variant", "frameshift", "initiator_codon_variant", "intron", "missense", "noncoding_transcript_exon", "splice_deceptor", "splice_donor", "splice_region", "start_lost", "stop_gained", "stop_lost", "stop_retained", "synonymous", "upstream_gene_variant"]

quant_mut_types = [conservative_inframe_deletion, conservative_inframe_insertion, disruptive_inframe_deletion, disruptive_inframe_insertion, downstream_gene_variant, frameshift, initiator_codon_variant, intron, missense, noncoding_transcript_exon, splice_deceptor, splice_donor, splice_region, start_lost, stop_gained, stop_lost, stop_retained, synonymous, upstream_gene_variant]

index = np.arange(len(labels))

# fig, ax = plt.subplots()
# plt.bar(index, quant_mut_types)
# plt.xticks(index, labels, fontsize=5, rotation=60)
# plt.ylabel("number of mutations")
# plt.xlabel("types of mutation effects")
# ax.set_title("effect as determined by snpEff")
# fig.savefig("effects.png")
# plt.close(fig)


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, constrained_layout = True, figsize=(20,20))
plt.rcParams.update({'font.size': 18})

#fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, constrained_layout = True)
#fig.subplots_adjust(hspace=5)
ax1.hist(read_depth, bins=1000, color="teal", edgecolor="black", linewidth=.5, alpha=0.8)
ax1.set(title="Read Depth Across Variants", ylabel = "Counts", xlabel = "Read Depth")
ax1.set_xlim(0,140)
# ax1.xlabel("Read Depth")
# ax1.ylabel("Counts")
# ax1.set_title("Read Depth Across Variants")
# ax[0,0].plt.savefig("readdepth.png")
# ax[0,0].plt.close(fig)

ax2.hist(all_quality, bins=1000, color="teal", edgecolor="black", linewidth=.5, alpha=0.8)
ax2.set(title = "Genome Quality Across Variants", ylabel = "Counts", xlabel = "Genome Quality")
ax2.set_xlim(0,2500)
# ax2.plt.xlabel("Genome Quality")
# ax2.plt.ylabel("Counts")
# ax2.plt.title("Genome Quality Across Variants")
# ax[0,1].plt.savefig("genqual.png")
# ax[0,1].plt.close(fig)

ax3.hist(all_freq, rwidth=.75, color="teal", edgecolor="black", linewidth=.5, alpha=0.8)
ax3.set(title="Allele Frequency Across Variants", ylabel = "Counts", xlabel = "Allele Frequency")
# ax3.plt.hist(all_freq,rwidth=.75)
ax3.set_xlim(0,20)
# ax3.plt.xlabel("Allele Frequency")
# ax3.plt.ylabel("Counts")
# ax3.plt.title("Allele Frequency Across Variants")
# ax[1,0].plt.savefig("allelefreq.png")
# ax[1,0].plt.close(fig)

ax4.bar(index, quant_mut_types, color="teal", edgecolor="black", linewidth=.5, alpha=0.8)
ax4.set(title = "Effect as Determined by snpEff", ylabel = "Number of Mutations", xlabel = "Types of Mutation Effects")

#ax4.set_xticks(labels)
ax4.set_xticklabels(labels, fontweight = 1, rotation = 60, alpha=0.8)
#ax4.locator_params(fontsize = 5, rotation = 90)
# ax4.plt.ylabel("number of mutations")
# ax4.plt.xlabel("types of mutation effects")
# ax4.set_title("effect as determined by snpEff")
# ax4.fig.savefig("allfourgraphs.png")
fig.savefig("allfour.png")
#plt.tight_layout()
plt.close(fig)

