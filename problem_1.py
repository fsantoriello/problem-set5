#! /usr/local/bin/python3

#Import
import sys
from collections import Counter

#Load data
filename = sys.argv[1]

#Run program
counts = Counter()

for lines in open(filename):
    if lines.startswith('#'): continue
    fields = lines.split('\t')
    chrom = fields[0]
    counts[chrom] += 1

sortme = [(v,k) for k,v in counts.items()]

sortme.sort()

sortme.reverse()

print("Chromosome with most intervals:", sortme[0][1])
