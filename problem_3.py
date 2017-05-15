#! /usr/local/bin/python3

#Import
import sys
from collections import Counter

#Load data
filename = sys.argv[1]

#Define functions
def fivePrimeHexamer(seq):
    return seq[0:6]

def threePrimeHexamer(seq):
    return seq[-6:]

#Run program
count = 0

hexamers_5prime = Counter()
hexamers_3prime = Counter()

for line in open(filename):
    line = line.rstrip()

    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        hexamer_5prime = fivePrimeHexamer(seq)
        hexamers_5prime[hexamer_5prime] += 1
        
        hexamer_3prime = threePrimeHexamer(seq)
        hexamers_3prime[hexamer_3prime] += 1

for hexamer, count in hexamers_5prime.most_common(1):
    print("The most common 5' hexamer is", hexamer,"[ Count:", count, "]")

for hexamer, count in hexamers_3prime.most_common(1):
    print("The most common 3' hexamer is", hexamer,"[ Count:", count, "]")
