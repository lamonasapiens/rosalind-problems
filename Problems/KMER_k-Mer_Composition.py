"""
Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.
__________________________________________________________________________
"""
from itertools import product
import re

f = open("datasets/rosalind_kmer.txt", "r")
seq = f.read().strip().split("\n", 1)[1].replace("\n", "")

kmer_length = 4
bases = ["A", "C", "G", "T"]

kmers = ["".join(kmer) for kmer in product(bases, repeat = kmer_length)]
kmer_composition = []

for kmer in kmers:
    count = len(re.findall(f"(?={kmer})", seq))
    kmer_composition.append(count)

print(*kmer_composition)