#! /usr/local/bin/python3

#Import
import sys
from collections import Counter
from pysam import AlignmentFile

#Load data
filename = sys.argv[1]

#Run program

counts = 0

strands = Counter()
mismatches = Counter()

bamfile = AlignmentFile(filename)

#Identify strandedness and mismatches
for record in bamfile:
    strand = record.flag
    strands[strand] += 1
    nm = record.get_tag("NM")
    mismatches[nm] += 1

#Stranded reads
for strand, count in strands.items():
    if strand == 0:
        print("Positive strand aligned reads:", count)
    if strand == 16:
        print("Negative strand aligned reads:", count)

#Mismatched reads
for nm, count in mismatches.items():
    if nm == 0:
        print("Aligned reads with no mismatches:", count)
    else:
        counts += count
        print("Aligned reads with > 0 mismatches:", counts)

